#!/usr/bin/env python3
"""
Latitude 43 — Hotel Deal Finder
================================

Two-layer model:
  * MASTER CATALOG  (catalog/<city>.json) — the full, stable roster of
    business-relevant hotels, INCLUDING ones that rarely discount (Four
    Seasons, Shangri-La...). Curated attributes only, no pricing.
  * OBSERVATIONS    (data/observations.csv) — a time-series of priced
    searches. Each ingest appends rows; a deal is detected from the
    Expedia strikeout price, not from the `discounted_only` filter.

The Expedia search is an MCP tool available to the agent, not a public
API. So the workflow is:

    1.  The agent runs Expedia `search_hotels` and saves each raw JSON
        response into deals/raw/  (e.g. raw/2026-06-16_18.json).
    2.  python latitude43_deals.py ingest deals/raw/*.json
            -> upserts new hotels into the catalog (flagged for review)
            -> appends price observations
    3.  python latitude43_deals.py report --window 2026-06-16..2026-06-18
            -> ranked, business-first deal report (Markdown) to deals/out/

Ranking is QUALITY-FIRST (star -> guest rating -> review volume), with the
discount decoupled — so a prime hotel at 8% off outranks a motel at 50% off.
The email/artifact features the hotels that are ON DEAL; the catalog still
records full-rate observations for everything so we can later tell a real
deal from an inflated strikeout.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import math
import os
import sys
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG_DIR = os.path.join(HERE, "catalog")
DATA_DIR = os.path.join(HERE, "data")
OUT_DIR = os.path.join(HERE, "out")
OBSERVATIONS_CSV = os.path.join(DATA_DIR, "observations.csv")

OBS_FIELDS = [
    "scanned_at", "city", "hotel_id", "checkin", "checkout", "nights",
    "adults", "nightly_price", "total_price", "strikeout_price",
    "on_deal", "discount_pct",
]


# --------------------------------------------------------------------------
# Catalog
# --------------------------------------------------------------------------

HUBS_PATH = os.path.join(CATALOG_DIR, "_hubs.json")


def slug(city: str) -> str:
    return city.lower().replace(",", "").replace(".", "").replace(" ", "-")


def load_hubs() -> dict:
    if not os.path.exists(HUBS_PATH):
        return {}
    with open(HUBS_PATH, "r", encoding="utf-8") as fh:
        hubs = json.load(fh)
    hubs.pop("_notes", None)
    return hubs


def catalog_path(city: str) -> str:
    return os.path.join(CATALOG_DIR, f"{slug(city)}.json")


def load_catalog(city: str) -> dict:
    path = catalog_path(city)
    if not os.path.exists(path):
        hub = load_hubs().get(slug(city), {})
        return {
            "city": hub.get("city", city.title()),
            "country": hub.get("country", ""),
            "currency": hub.get("currency", "USD"),
            "financial_core_anchor": (
                {**hub["core"], "label": hub["core"].get("label", "")}
                if hub.get("core") else None
            ),
            "airports": hub.get("airports", []),
            "notes": hub.get("notes", ""),
            "hotels": {},
        }
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_catalog(city: str, catalog: dict) -> None:
    os.makedirs(CATALOG_DIR, exist_ok=True)
    with open(catalog_path(city), "w", encoding="utf-8") as fh:
        json.dump(catalog, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def haversine_km(lat1, lon1, lat2, lon2) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


AIRPORT_RADIUS_KM = 2.8


def derive_tier(catalog: dict, lat: float, lon: float) -> str:
    """Fallback tier for hotels not yet curated. Curated 'tier' always wins."""
    if lat is None or lon is None:
        return "Unclassified"
    for ap in catalog.get("airports", []) or []:
        if haversine_km(lat, lon, ap["lat"], ap["long"]) <= AIRPORT_RADIUS_KM:
            return "Airport"
    anchor = catalog.get("financial_core_anchor")
    if not anchor:
        return "Unclassified"
    d = haversine_km(lat, lon, anchor["lat"], anchor["long"])
    if d <= 1.2:
        return "Core"
    if d <= 3.0:
        return "Prime"
    if d <= 8.0:
        return "Secondary"
    return "Suburban"


# --------------------------------------------------------------------------
# Brand curation
# --------------------------------------------------------------------------

# Keyword (lowercased, first match wins) -> (brand, segment). Used by the
# `curate` command to fill obvious brands on _needs_review hotels; tier and
# area stay hand-curated.
BRAND_RULES = [
    ("four seasons", ("Four Seasons", "Luxury")),
    ("ritz-carlton", ("Ritz-Carlton", "Luxury")),
    ("st. regis", ("St. Regis", "Luxury")),
    ("waldorf astoria", ("Waldorf Astoria", "Luxury")),
    ("park hyatt", ("Park Hyatt", "Luxury")),
    ("grand hyatt", ("Grand Hyatt", "Upper upscale")),
    ("peninsula", ("Peninsula", "Luxury")),
    ("shangri-la", ("Shangri-La", "Luxury")),
    ("mandarin oriental", ("Mandarin Oriental", "Luxury")),
    ("rosewood", ("Rosewood", "Luxury")),
    ("faena", ("Faena", "Luxury")),
    ("salamander", ("Salamander", "Luxury")),
    ("nobu hotel", ("Nobu", "Luxury")),
    ("1 hotel", ("1 Hotels", "Luxury")),
    ("edition", ("EDITION", "Luxury")),
    ("thompson", ("Thompson (Hyatt)", "Upper upscale")),
    ("kimpton", ("Kimpton (IHG)", "Upper upscale")),
    ("intercontinental", ("InterContinental (IHG)", "Upper upscale")),
    ("fairmont", ("Fairmont", "Upper upscale")),
    ("jw marriott", ("JW Marriott", "Upper upscale")),
    ("w hotel", ("W Hotels", "Upper upscale")),
    ("westin", ("Westin (Marriott)", "Upper upscale")),
    ("sheraton", ("Sheraton (Marriott)", "Upscale")),
    ("renaissance", ("Renaissance (Marriott)", "Upper upscale")),
    ("le méridien", ("Le Méridien (Marriott)", "Upper upscale")),
    ("le meridien", ("Le Méridien (Marriott)", "Upper upscale")),
    ("autograph", ("Autograph Collection", "Upper upscale")),
    ("tribute portfolio", ("Tribute Portfolio (Marriott)", "Upscale")),
    ("moxy", ("Moxy (Marriott)", "Select / lifestyle")),
    ("ac hotel", ("AC Hotels (Marriott)", "Upscale")),
    ("residence inn", ("Residence Inn (Marriott)", "Extended stay")),
    ("courtyard", ("Courtyard (Marriott)", "Select service")),
    ("fairfield", ("Fairfield (Marriott)", "Select service")),
    ("city express", ("City Express (Marriott)", "Select service")),
    ("marriott", ("Marriott", "Upper upscale")),
    ("conrad", ("Conrad (Hilton)", "Luxury")),
    ("signia", ("Signia (Hilton)", "Upper upscale")),
    ("curio collection", ("Curio Collection (Hilton)", "Upper upscale")),
    ("tapestry collection", ("Tapestry Collection (Hilton)", "Upscale")),
    ("canopy by hilton", ("Canopy (Hilton)", "Upscale / lifestyle")),
    ("graduate by hilton", ("Graduate (Hilton)", "Upscale / lifestyle")),
    ("doubletree", ("DoubleTree (Hilton)", "Upscale")),
    ("embassy suites", ("Embassy Suites (Hilton)", "Upscale")),
    ("hilton garden inn", ("Hilton Garden Inn", "Select service")),
    ("hampton", ("Hampton (Hilton)", "Select service")),
    ("home2 suites", ("Home2 Suites (Hilton)", "Extended stay")),
    ("hilton", ("Hilton", "Upper upscale")),
    ("hyatt house", ("Hyatt House", "Extended stay")),
    ("hyatt place", ("Hyatt Place", "Select service")),
    ("hyatt centric", ("Hyatt Centric", "Upscale / lifestyle")),
    ("hyatt regency", ("Hyatt Regency", "Upper upscale")),
    ("unbound collection", ("Unbound Collection (Hyatt)", "Upper upscale")),
    ("hyatt", ("Hyatt", "Upper upscale")),
    ("voco", ("voco (IHG)", "Upscale")),
    ("hotel indigo", ("Hotel Indigo (IHG)", "Upscale / boutique")),
    ("even hotel", ("EVEN (IHG)", "Select service")),
    ("candlewood", ("Candlewood Suites (IHG)", "Extended stay")),
    ("holiday inn express", ("Holiday Inn Express (IHG)", "Select service")),
    ("holiday inn", ("Holiday Inn (IHG)", "Midscale")),
    ("crowne plaza", ("Crowne Plaza (IHG)", "Upscale")),
    ("omni", ("Omni", "Upper upscale")),
    ("sonesta es suites", ("Sonesta ES Suites", "Extended stay")),
    ("royal sonesta", ("Royal Sonesta", "Upper upscale")),
    ("sonesta", ("Sonesta", "Upscale")),
    ("pullman", ("Pullman (Accor)", "Upper upscale")),
    ("sofitel", ("Sofitel (Accor)", "Luxury")),
    ("citizenm", ("citizenM", "Select / lifestyle")),
    ("yotel", ("YOTEL", "Select / lifestyle")),
    ("riu plaza", ("RIU Plaza", "Upscale")),
    ("eurostars", ("Eurostars", "Upscale")),
    ("club quarters", ("Club Quarters", "Business value")),
    ("virgin hotels", ("Virgin Hotels", "Upscale / lifestyle")),
    ("hoxton", ("The Hoxton", "Upscale / lifestyle")),
    ("staypineapple", ("Staypineapple", "Upscale / boutique")),
    ("warwick", ("Warwick", "Upscale")),
    ("wyndham", ("Wyndham", "Midscale")),
    ("ramada", ("Ramada (Wyndham)", "Midscale")),
    ("la quinta", ("La Quinta (Wyndham)", "Midscale")),
    ("days inn", ("Days Inn (Wyndham)", "Economy")),
    ("travelodge", ("Travelodge (Wyndham)", "Economy")),
    ("best western premier", ("Best Western Premier", "Upscale")),
    ("bw premier", ("Best Western Premier", "Upscale")),
    ("bw signature", ("BW Signature Collection", "Midscale")),
    ("best western", ("Best Western", "Midscale")),
    ("comfort suites", ("Comfort Suites (Choice)", "Midscale")),
    ("comfort inn", ("Comfort Inn (Choice)", "Midscale")),
    ("cambria", ("Cambria (Choice)", "Upscale")),
    ("ascend collection", ("Ascend Collection (Choice)", "Midscale")),
    ("four points", ("Four Points (Marriott)", "Select service")),
    ("trump", ("Trump Hotels", "Luxury")),
    ("waldorf", ("Waldorf Astoria", "Luxury")),
    ("public,", ("PUBLIC (Schrager)", "Upscale / lifestyle")),
    ("pod ", ("Pod Hotels", "Micro / value")),
]


def infer_brand(name: str):
    n = (name or "").lower()
    for kw, hit in BRAND_RULES:
        if kw in n:
            return hit
    return None


def curate(city: str) -> dict:
    """Fill brand/segment from name keywords on hotels still flagged for
    review. Tier/area remain manual; the flag is kept until those are set."""
    catalog = load_catalog(city)
    stats = {"branded": 0, "still_unknown": 0}
    for h in catalog["hotels"].values():
        if h.get("brand") not in (None, "", "Unknown"):
            continue
        hit = infer_brand(h.get("name", ""))
        if hit:
            h["brand"], h["segment"] = hit
            stats["branded"] += 1
        else:
            h["brand"] = "Independent"
            stats["still_unknown"] += 1
    save_catalog(city, catalog)
    return stats


# --------------------------------------------------------------------------
# Ingest
# --------------------------------------------------------------------------

def _to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def parse_results(raw: dict) -> tuple[list[dict], int]:
    """Pull the hotel records and adult count out of one Expedia response."""
    adults = 1
    occ = raw.get("occupants") or []
    if occ and isinstance(occ, list):
        adults = occ[0].get("adults", 1)
    return raw.get("data", []) or [], adults


def ingest_files(city: str, paths: list[str], scanned_at: str) -> dict:
    catalog = load_catalog(city)
    hotels = catalog["hotels"]

    os.makedirs(DATA_DIR, exist_ok=True)
    file_exists = os.path.exists(OBSERVATIONS_CSV)

    stats = {"files": 0, "observations": 0, "new_hotels": [], "deals": 0}

    with open(OBSERVATIONS_CSV, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=OBS_FIELDS)
        if not file_exists:
            writer.writeheader()

        for path in paths:
            with open(path, "r", encoding="utf-8") as f:
                raw = json.load(f)
            records, adults = parse_results(raw)
            stats["files"] += 1

            for rec in records:
                hid = str(rec.get("hotel_id", "")).strip()
                if not hid:
                    continue

                lat = _to_float(rec.get("geo_location", {}).get("latitude"))
                lon = _to_float(rec.get("geo_location", {}).get("longitude"))

                # Upsert into catalog (curated entries are preserved).
                if hid not in hotels:
                    hotels[hid] = {
                        "name": rec.get("hotel_name", ""),
                        "brand": "Unknown",
                        "star": _to_float(rec.get("star_rating")),
                        "guest_rating": _to_float(rec.get("guest_rating")),
                        "review_count": rec.get("guest_review_count", 0),
                        "lat": lat, "long": lon,
                        "area": "",
                        "tier": derive_tier(catalog, lat, lon),
                        "segment": "",
                        "_needs_review": True,
                    }
                    stats["new_hotels"].append(rec.get("hotel_name", hid))
                else:
                    # Refresh volatile quality signals.
                    h = hotels[hid]
                    if _to_float(rec.get("guest_rating")) is not None:
                        h["guest_rating"] = _to_float(rec.get("guest_rating"))
                    if rec.get("guest_review_count"):
                        h["review_count"] = rec.get("guest_review_count")

                checkin = rec.get("checkin_date")
                checkout = rec.get("checkout_date")
                nights = _nights(checkin, checkout)
                total = _to_float(rec.get("total_price"))
                strike = _to_float(rec.get("total_strikeout_price"))
                nightly = _to_float(rec.get("avg_nightly_rate_with_fees"))
                on_deal = strike is not None and total is not None and strike > total
                discount = round((strike - total) / strike * 100, 1) if on_deal else 0.0
                if on_deal:
                    stats["deals"] += 1

                writer.writerow({
                    "scanned_at": scanned_at, "city": city,
                    "hotel_id": hid, "checkin": checkin, "checkout": checkout,
                    "nights": nights, "adults": adults,
                    "nightly_price": nightly, "total_price": total,
                    "strikeout_price": strike if strike is not None else "",
                    "on_deal": "1" if on_deal else "0",
                    "discount_pct": discount,
                })
                stats["observations"] += 1

    save_catalog(city, catalog)
    return stats


def _nights(checkin: str, checkout: str) -> int:
    try:
        a = datetime.strptime(checkin, "%Y-%m-%d").date()
        b = datetime.strptime(checkout, "%Y-%m-%d").date()
        return (b - a).days
    except (TypeError, ValueError):
        return 0


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

TIER_ORDER = {"Core": 0, "Prime": 1, "Secondary": 2, "Airport": 3,
              "Suburban": 4, "Unclassified": 5}


def load_observations() -> list[dict]:
    if not os.path.exists(OBSERVATIONS_CSV):
        return []
    with open(OBSERVATIONS_CSV, "r", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def quality_key(hotel: dict) -> tuple:
    return (
        -(hotel.get("star") or 0),
        -(hotel.get("guest_rating") or 0),
        -(hotel.get("review_count") or 0),
    )


def report(city: str, window: str | None, min_rating: float,
           min_star: float, top: int | None, include_full_rate: bool) -> str:
    catalog = load_catalog(city)
    hotels = catalog["hotels"]
    obs = [o for o in load_observations() if slug(o["city"]) == slug(city)]

    if window:
        ci, co = window.split("..")
        obs = [o for o in obs if o["checkin"] == ci and o["checkout"] == co]

    if not obs:
        return f"No observations found for {city}" + (f" ({window})" if window else "") + "."

    # Latest observation per (hotel, checkin, checkout).
    latest: dict[tuple, dict] = {}
    for o in obs:
        key = (o["hotel_id"], o["checkin"], o["checkout"])
        if key not in latest or o["scanned_at"] > latest[key]["scanned_at"]:
            latest[key] = o

    rows = []
    for o in latest.values():
        h = hotels.get(o["hotel_id"])
        if not h:
            continue
        if (h.get("star") or 0) < min_star:
            continue
        if (h.get("guest_rating") or 0) < min_rating:
            continue
        rows.append({**o, "hotel": h})

    on_deal = [r for r in rows if r["on_deal"] == "1"]
    full_rate = [r for r in rows if r["on_deal"] != "1"]

    on_deal.sort(key=lambda r: (TIER_ORDER.get(r["hotel"].get("tier"), 9),
                                quality_key(r["hotel"])))
    full_rate.sort(key=lambda r: (TIER_ORDER.get(r["hotel"].get("tier"), 9),
                                  quality_key(r["hotel"])))
    if top:
        on_deal = on_deal[:top]

    win = window or "all windows"
    nights = next(iter(latest.values()))["nights"] if latest else "?"
    lines = []
    lines.append(f"# Latitude 43 — {catalog.get('city', city)} Hotel Deals")
    lines.append("")
    lines.append(f"**Stay window:** {win} · {nights} night(s) · 1 guest  ")
    lines.append(f"**Generated:** {date.today().isoformat()}  ")
    lines.append(f"**Hotels on deal:** {len(on_deal)} of {len(rows)} tracked "
                 f"(min {min_star:g}★ / {min_rating:g} rating)")
    lines.append("")
    lines.append("_Quality-first ranking: star → guest rating → review volume. "
                 "The discount is shown but does not drive the order — a prime "
                 "hotel at a small discount still leads._")
    lines.append("")
    lines.append("## On deal now")
    lines.append("")
    lines.append("| # | Hotel | ★ | Rating | Area (tier) | Nightly | Was | Off |")
    lines.append("|---|-------|---|--------|-------------|---------|-----|-----|")
    for i, r in enumerate(on_deal, 1):
        h = r["hotel"]
        strike = r["strikeout_price"]
        was = _money(_strike_nightly(r)) if strike else "—"
        lines.append(
            f"| {i} | {h['name']} | {_star(h)} | {h.get('guest_rating','?')} "
            f"({_revs(h)}) | {h.get('area','')} ({h.get('tier','')}) | "
            f"{_money(r['nightly_price'])} | {was} | {r['discount_pct']}% |"
        )

    if include_full_rate and full_rate:
        lines.append("")
        lines.append("## In catalog, full rate (no deal this window)")
        lines.append("")
        names = ", ".join(
            f"{r['hotel']['name']} ({_star(r['hotel'])}★, "
            f"{r['hotel'].get('guest_rating','?')}, {_money(r['nightly_price'])})"
            for r in full_rate
        )
        lines.append(names)

    lines.append("")
    return "\n".join(lines)


def _money(v):
    f = _to_float(v)
    return f"${f:,.0f}" if f is not None else "—"


def _strike_nightly(r):
    strike = _to_float(r["strikeout_price"])
    nights = int(r.get("nights") or 0)
    if strike and nights:
        return strike / nights
    return None


def _star(h):
    s = h.get("star")
    if s is None:
        return "?"
    return f"{s:g}"


def _revs(h):
    n = h.get("review_count") or 0
    return f"{int(n):,}"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def report_consolidated(city: str, min_rating: float, min_star: float,
                        top: int | None, deals_only: bool) -> str:
    """Aggregate across ALL scanned windows: per hotel, the best deal found
    and the nightly-rate range. This is the multi-window planning view."""
    catalog = load_catalog(city)
    hotels = catalog["hotels"]
    obs = [o for o in load_observations() if slug(o["city"]) == slug(city)]
    if not obs:
        return f"No observations found for {city}."

    # Latest observation per (hotel, window).
    latest: dict[tuple, dict] = {}
    for o in obs:
        key = (o["hotel_id"], o["checkin"], o["checkout"])
        if key not in latest or o["scanned_at"] > latest[key]["scanned_at"]:
            latest[key] = o

    # Group by hotel.
    by_hotel: dict[str, list[dict]] = {}
    for o in latest.values():
        by_hotel.setdefault(o["hotel_id"], []).append(o)

    agg = []
    windows_seen = set()
    for hid, rows in by_hotel.items():
        h = hotels.get(hid)
        if not h or (h.get("star") or 0) < min_star or (h.get("guest_rating") or 0) < min_rating:
            continue
        deal_rows = [r for r in rows if r["on_deal"] == "1"]
        for r in rows:
            windows_seen.add((r["checkin"], r["checkout"]))
        nightlies = [_to_float(r["nightly_price"]) for r in rows if _to_float(r["nightly_price"])]
        best = max(deal_rows, key=lambda r: float(r["discount_pct"]), default=None)
        agg.append({
            "hotel": h,
            "deal_windows": len(deal_rows),
            "total_windows": len(rows),
            "best_discount": float(best["discount_pct"]) if best else 0.0,
            "best_window": (best["checkin"], best["checkout"]) if best else None,
            "best_nightly": _to_float(best["nightly_price"]) if best else None,
            "min_nightly": min(nightlies) if nightlies else None,
            "max_nightly": max(nightlies) if nightlies else None,
        })

    if deals_only:
        agg = [a for a in agg if a["deal_windows"] > 0]
    agg.sort(key=lambda a: (TIER_ORDER.get(a["hotel"].get("tier"), 9), quality_key(a["hotel"])))
    if top:
        agg = agg[:top]

    wins = sorted(windows_seen)
    span = f"{wins[0][0]} → {wins[-1][1]}" if wins else "—"
    lines = [
        f"# Latitude 43 — {catalog.get('city', city)} Multi-Window Deal Scan",
        "",
        f"**Check-in span:** {span} · {len(wins)} windows scanned · 1 guest  ",
        f"**Generated:** {date.today().isoformat()}  ",
        f"**Filter:** ≥{min_star:g}★ / ≥{min_rating:g} rating  ",
        "",
        "_Per hotel: the best discount found across all scanned windows, and the "
        "nightly-rate range. Quality-first order. 'Deal wins' = how many of the "
        "scanned windows had an active discount (a signal of a real vs. one-off deal)._",
        "",
        "| # | Hotel | ★ | Rating | Area (tier) | Nightly range | Best deal | When | Deal wins |",
        "|---|-------|---|--------|-------------|---------------|-----------|------|-----------|",
    ]
    for i, a in enumerate(agg, 1):
        h = a["hotel"]
        rng = f"{_money(a['min_nightly'])}–{_money(a['max_nightly'])}" if a["min_nightly"] else "—"
        if a["best_discount"] > 0:
            bw = a["best_window"]
            best = f"{a['best_discount']:g}% @ {_money(a['best_nightly'])}"
            when = f"{bw[0][5:]}" if bw else "—"
        else:
            best, when = "— full rate —", "—"
        lines.append(
            f"| {i} | {h['name']} | {_star(h)} | {h.get('guest_rating','?')} "
            f"({_revs(h)}) | {h.get('area','')} ({h.get('tier','')}) | {rng} | "
            f"{best} | {when} | {a['deal_windows']}/{a['total_windows']} |"
        )
    lines.append("")
    return "\n".join(lines)


def report_coverage(city: str, min_rating: float, min_star: float,
                    checkin_from: str | None, top: int | None) -> str:
    """Forward-horizon view for FLEXIBLE travel: across all sampled future
    check-ins, how often is each quality hotel discounting? A hotel on deal in
    most/all sampled windows is a safe bet whenever the client travels.

    Denominator = total distinct windows sampled at/after checkin_from, so a
    hotel absent from a window counts as 'not on deal' that window. Designed for
    lean discounted_only scans where only on-deal hotels are returned."""
    catalog = load_catalog(city)
    hotels = catalog["hotels"]
    obs = [o for o in load_observations() if slug(o["city"]) == slug(city)]
    if checkin_from:
        obs = [o for o in obs if o["checkin"] >= checkin_from]
    if not obs:
        return f"No observations found for {city}."

    # Latest obs per (hotel, window); collect the full set of windows sampled.
    latest: dict[tuple, dict] = {}
    windows = set()
    for o in obs:
        windows.add((o["checkin"], o["checkout"]))
        key = (o["hotel_id"], o["checkin"], o["checkout"])
        if key not in latest or o["scanned_at"] > latest[key]["scanned_at"]:
            latest[key] = o
    total_windows = len(windows)

    by_hotel: dict[str, list[dict]] = {}
    for o in latest.values():
        if o["on_deal"] == "1":
            by_hotel.setdefault(o["hotel_id"], []).append(o)

    rows = []
    for hid, deals in by_hotel.items():
        h = hotels.get(hid)
        if not h or (h.get("star") or 0) < min_star or (h.get("guest_rating") or 0) < min_rating:
            continue
        nightlies = [_to_float(d["nightly_price"]) for d in deals if _to_float(d["nightly_price"])]
        discounts = [float(d["discount_pct"]) for d in deals]
        rows.append({
            "hotel": h,
            "n_deal": len(deals),
            "coverage": len(deals) / total_windows if total_windows else 0,
            "min_nightly": min(nightlies) if nightlies else None,
            "max_nightly": max(nightlies) if nightlies else None,
            "med_discount": sorted(discounts)[len(discounts) // 2] if discounts else 0,
            "max_discount": max(discounts) if discounts else 0,
        })

    def band(cov):
        if cov >= 0.999:
            return "Always on deal"
        if cov >= 0.6:
            return "Usually on deal"
        return "Sometimes on deal"

    rows.sort(key=lambda r: (-r["coverage"],
                             TIER_ORDER.get(r["hotel"].get("tier"), 9),
                             quality_key(r["hotel"])))
    if top:
        rows = rows[:top]

    lines = [
        f"# Latitude 43 — {catalog.get('city', city)}: Hotels Reliably on Deal",
        "",
        f"**Forward horizon:** {total_windows} future check-in windows sampled"
        + (f" (from {checkin_from})" if checkin_from else "") + "  ",
        f"**Generated:** {date.today().isoformat()} · ≥{min_star:g}★ / ≥{min_rating:g} rating  ",
        "",
        "_For flexible travel: a deal is tied to a date, but these hotels are "
        "discounting across most/all sampled future dates — so whenever the trip "
        "lands, they're the ones likely to be on sale. 'Coverage' = share of "
        "sampled windows on deal._",
        "",
        "| Hotel | ★ | Rating | Area (tier) | Coverage | Typical off | Nightly range |",
        "|-------|---|--------|-------------|----------|-------------|---------------|",
    ]
    current = None
    for r in rows:
        b = band(r["coverage"])
        if b != current:
            lines.append(f"| **— {b} —** | | | | | | |")
            current = b
        h = r["hotel"]
        rng = f"{_money(r['min_nightly'])}–{_money(r['max_nightly'])}" if r["min_nightly"] else "—"
        lines.append(
            f"| {h['name']} | {_star(h)} | {h.get('guest_rating','?')} ({_revs(h)}) | "
            f"{h.get('area','')} ({h.get('tier','')}) | {r['n_deal']}/{total_windows} | "
            f"~{r['med_discount']:g}% (max {r['max_discount']:g}%) | {rng} |"
        )
    lines.append("")
    return "\n".join(lines)


def _outlook_grid(city: str, min_rating: float, min_star: float,
                  checkin_from: str | None):
    """Shared builder for the outlook matrix: quality hotels x sampled windows."""
    catalog = load_catalog(city)
    hotels = catalog["hotels"]
    obs = [o for o in load_observations() if slug(o["city"]) == slug(city)]
    if checkin_from:
        obs = [o for o in obs if o["checkin"] >= checkin_from]

    latest: dict[tuple, dict] = {}
    windows = set()
    for o in obs:
        windows.add(o["checkin"])
        key = (o["hotel_id"], o["checkin"], o["checkout"])
        if key not in latest or o["scanned_at"] > latest[key]["scanned_at"]:
            latest[key] = o
    windows = sorted(windows)

    grid: dict[str, dict[str, dict]] = {}
    for o in latest.values():
        h = hotels.get(o["hotel_id"])
        if not h or (h.get("star") or 0) < min_star or (h.get("guest_rating") or 0) < min_rating:
            continue
        cell = grid.setdefault(o["hotel_id"], {})
        prev = cell.get(o["checkin"])
        # If a hotel was sampled twice for one check-in, keep the deal row.
        if prev is None or (prev["on_deal"] != "1" and o["on_deal"] == "1"):
            cell[o["checkin"]] = o

    rows = []
    for hid, cells in grid.items():
        deals = [c for c in cells.values() if c["on_deal"] == "1"]
        if not deals:
            continue
        rows.append({
            "hid": hid, "hotel": hotels[hid], "cells": cells,
            "n_deal": len(deals),
            "best": max(float(c["discount_pct"]) for c in deals),
        })
    rows.sort(key=lambda r: (-r["n_deal"], TIER_ORDER.get(r["hotel"].get("tier"), 9),
                             quality_key(r["hotel"])))
    return catalog, windows, rows


def report_outlook(city: str, min_rating: float, min_star: float,
                   checkin_from: str | None) -> str:
    """Markdown matrix: which hotels have deals on which sampled check-in dates."""
    catalog, windows, rows = _outlook_grid(city, min_rating, min_star, checkin_from)
    if not windows:
        return f"No observations found for {city}."

    def d(w):  # 2026-07-21 -> 7/21
        return f"{int(w[5:7])}/{int(w[8:10])}"

    lines = [
        f"# Latitude 43 — {catalog.get('city', city)} 3-Month Deal Outlook",
        "",
        f"**Sampled check-ins:** {d(windows[0])} → {d(windows[-1])} "
        f"({len(windows)} dates, 2-night stays, 1 guest) · "
        f"**Generated:** {date.today().isoformat()}",
        "",
        "_Cell = % off Expedia standard rate for that check-in date. Blank = no "
        "discount observed that date. Rows ordered by how many sampled dates the "
        "hotel was on deal._",
        "",
        "| Hotel (★ rating) | " + " | ".join(d(w) for w in windows) + " | Hit |",
        "|---" * (len(windows) + 2) + "|",
    ]
    for r in rows:
        h = r["hotel"]
        cells = []
        for w in windows:
            o = r["cells"].get(w)
            if o and o["on_deal"] == "1":
                cells.append(f"{float(o['discount_pct']):.0f}%")
            else:
                cells.append("")
        lines.append(
            f"| {h['name']} ({_star(h)}★ {h.get('guest_rating','?')}) | "
            + " | ".join(cells) + f" | {r['n_deal']}/{len(windows)} |"
        )
    lines.append("")
    return "\n".join(lines)


def report_outlook_html(city: str, min_rating: float, min_star: float,
                        checkin_from: str | None) -> str:
    """Self-contained HTML heatmap of the outlook matrix (Latitude 43 styling)."""
    catalog, windows, rows = _outlook_grid(city, min_rating, min_star, checkin_from)

    def d(w):
        return f"{int(w[5:7])}/{int(w[8:10])}"

    head = "".join(f"<th>{d(w)}</th>" for w in windows)
    body = []
    for r in rows:
        h = r["hotel"]
        tds = []
        for w in windows:
            o = r["cells"].get(w)
            if o and o["on_deal"] == "1":
                pct = float(o["discount_pct"])
                # 0-50%+ mapped to background intensity
                alpha = min(pct / 50.0, 1.0) * 0.85 + 0.12
                nightly = _money(o["nightly_price"])
                tds.append(
                    f'<td class="deal" style="background:rgba(31,122,90,{alpha:.2f})" '
                    f'title="{h["name"]} — check-in {w}: {nightly}/nt, {pct:.0f}% off">'
                    f"{pct:.0f}%</td>"
                )
            else:
                tds.append('<td class="nodeal">·</td>')
        meta = (f'{_star(h)}★ · {h.get("guest_rating","?")} · '
                f'{h.get("area","")}')
        body.append(
            f'<tr><td class="hotel"><strong>{h["name"]}</strong>'
            f'<span class="meta">{meta}</span></td>{"".join(tds)}'
            f'<td class="hit">{r["n_deal"]}/{len(windows)}</td></tr>'
        )

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Latitude 43 — {catalog.get('city', city)} 3-Month Deal Outlook</title>
<style>
  body {{ font-family: Georgia, 'Times New Roman', serif; background:#0E1A2B; color:#EAE6DD;
         margin:0; padding:40px 24px; }}
  .wrap {{ max-width:1180px; margin:0 auto; }}
  h1 {{ font-weight:normal; font-size:26px; letter-spacing:.02em; margin:0 0 4px; }}
  h1 .deg {{ color:#C8A96A; font-size:14px; vertical-align:super; margin-left:6px; }}
  .sub {{ color:#9AA7B8; font-size:14px; margin-bottom:28px; }}
  table {{ border-collapse:collapse; width:100%; font-size:13px;
           font-family:'Helvetica Neue', Arial, sans-serif; }}
  th {{ color:#C8A96A; font-weight:600; padding:6px 4px; border-bottom:1px solid #2A3A50;
        text-align:center; white-space:nowrap; }}
  th.hotel-h {{ text-align:left; }}
  td {{ padding:6px 4px; border-bottom:1px solid #1C2A3E; text-align:center; }}
  td.hotel {{ text-align:left; min-width:230px; }}
  td.hotel .meta {{ display:block; color:#9AA7B8; font-size:11px; }}
  td.deal {{ color:#fff; font-weight:600; border-radius:3px; }}
  td.nodeal {{ color:#3A4A60; }}
  td.hit {{ color:#C8A96A; font-weight:600; }}
  .legend {{ margin-top:18px; color:#9AA7B8; font-size:12px;
             font-family:'Helvetica Neue', Arial, sans-serif; }}
</style></head><body><div class="wrap">
<h1>Latitude 43<span class="deg">43°N</span> &nbsp;—&nbsp; {catalog.get('city', city)} 3-Month Deal Outlook</h1>
<div class="sub">Sampled check-ins {d(windows[0])} → {d(windows[-1])} ({len(windows)} dates ·
2-night stays · 1 guest) · % shown is off the Expedia standard rate · generated {date.today().isoformat()}</div>
<table>
<tr><th class="hotel-h">Hotel</th>{head}<th>Hit</th></tr>
{''.join(body)}
</table>
<div class="legend">Darker green = deeper discount. Hover any cell for the nightly rate.
A dot means no discount was observed for that check-in date.</div>
</div></body></html>"""


def main(argv=None):
    p = argparse.ArgumentParser(description="Latitude 43 hotel deal finder")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("ingest", help="Ingest raw Expedia search JSON")
    pi.add_argument("paths", nargs="+", help="raw JSON files (globs ok)")
    pi.add_argument("--city", default="Toronto")
    pi.add_argument("--scanned-at", default=datetime.now().isoformat(timespec="seconds"))

    pc = sub.add_parser("curate", help="Infer brand/segment from hotel names")
    pc.add_argument("--city", default="Toronto")

    pl = sub.add_parser("cities", help="List hub cities and catalog status")

    pr = sub.add_parser("report", help="Generate a ranked deal report")
    pr.add_argument("--city", default="Toronto")
    pr.add_argument("--window", help="checkin..checkout, e.g. 2026-06-16..2026-06-18")
    pr.add_argument("--consolidated", action="store_true",
                    help="aggregate across all scanned windows (multi-window view)")
    pr.add_argument("--coverage", action="store_true",
                    help="forward-horizon 'reliably discounting' leaderboard")
    pr.add_argument("--outlook", action="store_true",
                    help="hotels x sampled-dates deal matrix (3-month outlook)")
    pr.add_argument("--html-out",
                    help="outlook: also write a self-contained HTML heatmap here")
    pr.add_argument("--checkin-from",
                    help="coverage: only count windows with check-in on/after this date")
    pr.add_argument("--deals-only", action="store_true",
                    help="consolidated: show only hotels with at least one deal")
    pr.add_argument("--min-rating", type=float, default=9.0)
    pr.add_argument("--min-star", type=float, default=4.0)
    pr.add_argument("--top", type=int, default=None)
    pr.add_argument("--no-full-rate", action="store_true")
    pr.add_argument("--out", help="write Markdown to this path (else stdout)")

    args = p.parse_args(argv)

    if args.cmd == "ingest":
        files = []
        for pat in args.paths:
            files.extend(sorted(glob.glob(pat)))
        if not files:
            print("No files matched.", file=sys.stderr)
            return 1
        stats = ingest_files(args.city, files, args.scanned_at)
        print(f"Ingested {stats['files']} file(s): {stats['observations']} "
              f"observations, {stats['deals']} on deal.")
        if stats["new_hotels"]:
            print(f"Added {len(stats['new_hotels'])} new hotel(s) "
                  f"(flagged _needs_review): {', '.join(stats['new_hotels'])}")
        return 0

    if args.cmd == "curate":
        stats = curate(args.city)
        print(f"{args.city}: branded {stats['branded']} hotel(s), "
              f"{stats['still_unknown']} marked Independent.")
        return 0

    if args.cmd == "cities":
        hubs = load_hubs()
        obs = load_observations()
        for key, hub in hubs.items():
            cat = load_catalog(key)
            n_obs = sum(1 for o in obs if slug(o["city"]) == key)
            print(f"{key:15s} {hub['city']:18s} "
                  f"{len(cat.get('hotels', {})):3d} hotels in catalog, "
                  f"{n_obs:4d} observations")
        return 0

    if args.cmd == "report":
        if args.outlook:
            md = report_outlook(args.city, args.min_rating, args.min_star,
                                args.checkin_from)
            if args.html_out:
                html = report_outlook_html(args.city, args.min_rating,
                                           args.min_star, args.checkin_from)
                os.makedirs(os.path.dirname(os.path.abspath(args.html_out)), exist_ok=True)
                with open(args.html_out, "w", encoding="utf-8") as fh:
                    fh.write(html)
                print(f"Wrote {args.html_out}")
        elif args.coverage:
            md = report_coverage(args.city, args.min_rating, args.min_star,
                                 args.checkin_from, args.top)
        elif args.consolidated:
            md = report_consolidated(args.city, args.min_rating, args.min_star,
                                     args.top, args.deals_only)
        else:
            md = report(args.city, args.window, args.min_rating, args.min_star,
                        args.top, not args.no_full_rate)
        if args.out:
            os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(md + "\n")
            print(f"Wrote {args.out}")
        else:
            print(md)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
