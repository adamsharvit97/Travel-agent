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

def catalog_path(city: str) -> str:
    return os.path.join(CATALOG_DIR, f"{city.lower()}.json")


def load_catalog(city: str) -> dict:
    path = catalog_path(city)
    if not os.path.exists(path):
        return {
            "city": city.title(), "country": "", "currency": "USD",
            "financial_core_anchor": None, "notes": "", "hotels": {},
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


def derive_tier(catalog: dict, lat: float, lon: float) -> str:
    """Fallback tier for hotels not yet curated. Curated 'tier' always wins."""
    # Airport cluster sits well west of downtown.
    if lon is not None and lon < -79.55 and lat is not None and lat > 43.66:
        return "Airport"
    anchor = catalog.get("financial_core_anchor")
    if not anchor or lat is None or lon is None:
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
    obs = [o for o in load_observations() if o["city"].lower() == city.lower()]

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

def main(argv=None):
    p = argparse.ArgumentParser(description="Latitude 43 hotel deal finder")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("ingest", help="Ingest raw Expedia search JSON")
    pi.add_argument("paths", nargs="+", help="raw JSON files (globs ok)")
    pi.add_argument("--city", default="Toronto")
    pi.add_argument("--scanned-at", default=datetime.now().isoformat(timespec="seconds"))

    pr = sub.add_parser("report", help="Generate a ranked deal report")
    pr.add_argument("--city", default="Toronto")
    pr.add_argument("--window", help="checkin..checkout, e.g. 2026-06-16..2026-06-18")
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

    if args.cmd == "report":
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
