#!/usr/bin/env python3
"""
Latitude 43 — city alert email builder.

Renders the deal data for one hub into the branded alert letter, following
the approved lookbook direction (deals/brand/mockup-3): full-bleed city
photograph with the deepest softening captioned on the image, two photo
tiles for the next two, the rest as quiet ledger rows, and the luxury
houses that are holding rate.

Email-client constraints honored: table layout, inline styles, web-safe
serif stack (Georgia) standing in for Playfair Display. Photography is set
as cell backgrounds, the standard responsive-email pattern.

    python3 build_alert_email.py --city chicago \
        --out out/email_chicago.html

The recipient list for the city comes from the subscriber sheet:

    python3 alerts/subscribers.py list --city chicago
"""

from __future__ import annotations

import argparse
import html
import os
from datetime import datetime

from latitude43_deals import (
    HERE, TIER_ORDER, _to_float, load_catalog, load_hubs, load_observations,
    quality_key, slug,
)

# Interior/lifestyle shots from the approved brand mockups — stand-ins until
# the desk drops in licensed photography per hotel.
TILE_IMAGES = [
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1551918120-9739cb430c6d",
    "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b",
    "https://images.unsplash.com/photo-1540541338287-41700207dee6",
]

# Palette (lookbook)
BG, BG2, LINE = "#0C0A09", "#13110F", "#2A241C"
TEXT, SOFT, MUTE = "#F2ECDF", "#C6BCA6", "#827763"
GOLD, GOLDB = "#D9B987", "#F2D29E"

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Courier New', Courier, monospace"


def mono(size, color, extra=""):
    return (f"font-family:{MONO};font-size:{size}px;letter-spacing:3px;"
            f"text-transform:uppercase;color:{color};{extra}")


def gather(city: str, window: str | None, min_star: float, min_rating: float):
    catalog = load_catalog(city)
    hotels = catalog["hotels"]
    obs = [o for o in load_observations() if slug(o["city"]) == slug(city)]
    if not obs:
        raise SystemExit(f"No observations for {city}.")

    if window is None:
        window = max((o["checkin"], o["checkout"]) for o in obs)
    else:
        window = tuple(window.split(".."))
    obs = [o for o in obs if (o["checkin"], o["checkout"]) == window]

    latest: dict[str, dict] = {}
    for o in obs:
        if o["hotel_id"] not in latest or o["scanned_at"] > latest[o["hotel_id"]]["scanned_at"]:
            latest[o["hotel_id"]] = o

    rows, holding = [], []
    for o in latest.values():
        h = hotels.get(o["hotel_id"])
        if not h or (h.get("star") or 0) < min_star or (h.get("guest_rating") or 0) < min_rating:
            continue
        if o["on_deal"] == "1":
            rows.append({**o, "hotel": h, "pct": float(o["discount_pct"])})
        elif (h.get("star") or 0) >= 4.5 or h.get("segment") == "Luxury":
            holding.append(h)
    rows.sort(key=lambda r: -r["pct"])
    holding.sort(key=quality_key)
    return catalog, window, rows, holding


def _nt(o) -> str:
    f = _to_float(o["nightly_price"])
    return f"${f:,.0f}" if f is not None else "—"


def _was(o) -> str:
    strike, n = _to_float(o["strikeout_price"]), int(o.get("nights") or 0)
    return f"${strike / n:,.0f}" if strike and n else "—"


def _meta(h, with_reviews=True) -> str:
    e = html.escape
    m = f"{h.get('star'):g}&#9733; &#183; {h.get('guest_rating', '?')}"
    if with_reviews and h.get("review_count"):
        m += f" ({int(h['review_count']):,})"
    place = h.get("area") or (h.get("tier") if h.get("tier") not in (None, "", "Unclassified") else "")
    if place:
        m += f" &#183; {e(place)}"
    return m


def build(city: str, window: str | None, min_star: float,
          min_rating: float) -> tuple[str, str]:
    catalog, win, deals, holding = gather(city, window, min_star, min_rating)
    city_name = catalog.get("city", city.title())
    hub = load_hubs().get(slug(city), {})
    city_photo = hub.get("photo", TILE_IMAGES[3])
    ci = datetime.strptime(win[0], "%Y-%m-%d").date()
    co = datetime.strptime(win[1], "%Y-%m-%d").date()
    month = ci.strftime("%B %Y")
    when = f"{ci.strftime('%b %-d')} &#8594; {co.strftime('%b %-d')}"
    when_plain = f"{ci.strftime('%b %-d')} → {co.strftime('%b %-d')}"

    subject = (f"{city_name}: {deals[0]['hotel']['name']} −{deals[0]['pct']:.0f}%, "
               f"and {len(deals) - 1} more softenings" if deals
               else f"{city_name}: the houses are holding rate")

    feat = deals[0] if deals else None
    tiles = deals[1:3]
    rest = deals[3:]
    # Ledger rows in quality-first order, like every Latitude 43 artifact.
    rest.sort(key=lambda r: (TIER_ORDER.get(r["hotel"].get("tier"), 9),
                             quality_key(r["hotel"])))

    e = html.escape
    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Latitude 43 — The {e(city_name)} Letter</title></head>
<body style="margin:0;padding:0;background:#050403;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#050403;">
<tr><td align="center">
<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="width:640px;max-width:100%;background:{BG};">

<tr><td style="padding:28px 36px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
    <td style="font-family:{SERIF};font-size:20px;letter-spacing:1px;color:{TEXT};">Latitude <i style="color:{GOLD};">43&#176;</i></td>
    <td align="right" style="{mono(9, MUTE)}">The {e(city_name)} Letter &#183; {month}</td>
  </tr></table>
</td></tr>

<tr><td style="padding:14px 36px 30px;">
  <div style="{mono(10, GOLD, 'margin-bottom:16px;')}">This week, in {e(city_name)}</div>
  <div style="font-family:{SERIF};font-size:34px;line-height:1.14;color:{TEXT};">
    The good rooms,<br>and <i style="color:{GOLDB};">when</i> they soften.</div>
  <div style="font-family:{SANS};font-size:14.5px;line-height:1.7;color:{SOFT};max-width:470px;margin-top:16px;">
    You asked to hear when {e(city_name)} moves. It has. The deepest softenings we're
    seeing for a two-night stay, {when} &mdash; then the rest, plainly. Reply with a
    week and we'll take it from there.</div>
</td></tr>""")

    if feat:
        h = feat["hotel"]
        parts.append(f"""
<tr><td background="{city_photo}?auto=format&fit=crop&w=1280&q=85"
        style="background-image:url('{city_photo}?auto=format&fit=crop&w=1280&q=85');background-size:cover;background-position:center;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
    <tr><td style="height:185px;line-height:185px;font-size:0;">&nbsp;</td></tr>
    <tr><td style="padding:70px 32px 28px;background:linear-gradient(180deg,rgba(12,10,9,0) 0%,rgba(12,10,9,.55) 45%,rgba(12,10,9,.97) 100%);">
      <div style="{mono(10, GOLDB, 'margin-bottom:10px;')}">Deepest this week &#183; {when}</div>
      <div style="font-family:{SERIF};font-size:26px;color:{TEXT};">{e(h['name'])}</div>
      <div style="font-family:{SANS};font-size:12px;color:{SOFT};margin-top:4px;">{_meta(h)}</div>
      <table role="presentation" cellpadding="0" cellspacing="0" style="margin-top:14px;"><tr>
        <td style="font-family:{SERIF};font-size:30px;color:{GOLDB};">&minus;{feat['pct']:.0f}%</td>
        <td style="font-family:{SANS};font-size:12px;color:{SOFT};padding-left:12px;">
          {_nt(feat)} <s style="color:{MUTE};">/ {_was(feat)}</s> a night</td>
      </tr></table>
    </td></tr>
  </table>
</td></tr>""")

    if tiles:
        tds = []
        for i, r in enumerate(tiles):
            h = r["hotel"]
            img = TILE_IMAGES[(sum(ord(c) for c in str(r['hotel_id'])) + i) % len(TILE_IMAGES)]
            tds.append(f"""
    <td width="50%" background="{img}?auto=format&fit=crop&w=720&q=80"
        style="background-image:url('{img}?auto=format&fit=crop&w=720&q=80');background-size:cover;background-position:center;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
        <tr><td style="height:92px;line-height:92px;font-size:0;">&nbsp;</td></tr>
        <tr><td style="padding:42px 18px 16px;background:linear-gradient(180deg,rgba(12,10,9,0) 0%,rgba(12,10,9,.96) 100%);">
          <div style="font-family:{SERIF};font-size:17px;line-height:1.15;color:{TEXT};">{e(h['name'])}</div>
          <div style="font-family:{SANS};font-size:10px;color:{SOFT};margin-top:3px;">{_meta(h, with_reviews=False)}</div>
          <div style="margin-top:8px;"><span style="font-family:{SERIF};font-size:20px;color:{GOLDB};">&minus;{r['pct']:.0f}%</span>
            <span style="font-family:{SANS};font-size:11px;color:{SOFT};padding-left:6px;">{_nt(r)}/nt</span></div>
        </td></tr>
      </table>
    </td>""")
        gap = f'<td width="6" style="width:6px;font-size:0;background:{BG};">&nbsp;</td>'
        parts.append(f"""
<tr><td style="padding-top:6px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{gap.join(tds)}</tr></table>
</td></tr>""")

    if rest:
        rows_html = []
        for r in rest:
            h = r["hotel"]
            rows_html.append(f"""
    <tr>
      <td style="padding:12px 0;border-top:1px solid {LINE};">
        <div style="font-family:{SERIF};font-size:16px;color:{TEXT};">{e(h['name'])}</div>
        <div style="font-family:{SANS};font-size:10.5px;color:{MUTE};margin-top:2px;">{_meta(h, with_reviews=False)}</div>
      </td>
      <td align="right" style="padding:12px 0;border-top:1px solid {LINE};white-space:nowrap;">
        <span style="font-family:{SERIF};font-size:18px;color:{GOLDB};">&minus;{r['pct']:.0f}%</span>
        <span style="font-family:{SANS};font-size:11px;color:{SOFT};padding-left:6px;">{_nt(r)}/nt</span>
      </td>
    </tr>""")
        parts.append(f"""
<tr><td style="padding:32px 36px 8px;">
  <div style="{mono(10, GOLD, 'margin-bottom:5px;')}">Also softening &#183; {when}</div>
  <div style="font-family:{SERIF};font-size:21px;color:{TEXT};margin-bottom:16px;">The rest of the week</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0">{''.join(rows_html)}</table>
</td></tr>""")

    if holding:
        names = " &#183; ".join(e(h["name"]) for h in holding[:4])
        pad_top = "6px" if rest else "32px"
        parts.append(f"""
<tr><td style="padding:{pad_top} 36px 8px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
    <td style="padding:12px 0;border-top:1px solid {LINE};">
      <div style="font-family:{SERIF};font-size:16px;color:{TEXT};">{names}</div>
      <div style="font-family:{SANS};font-size:10.5px;color:{MUTE};margin-top:2px;">The luxury houses &mdash; holding rate this week</div>
    </td>
    <td align="right" style="padding:12px 0;border-top:1px solid {LINE};white-space:nowrap;">
      <span style="font-family:{SANS};font-size:12px;font-style:italic;color:{MUTE};">we add the perks</span>
    </td>
  </tr></table>
</td></tr>""")

    parts.append(f"""
<tr><td style="height:26px;font-size:0;">&nbsp;</td></tr>
<tr><td style="padding:28px 36px 42px;border-top:1px solid {LINE};background:{BG2};">
  <div style="font-family:{SANS};font-size:12px;line-height:1.7;color:{MUTE};">
    Softenings are measured against the hotel's Expedia standard rate for the stay shown
    ({when_plain}); they move daily and guide <i>when</i> to go rather than quote a price.
    When a week suits you, reply to this letter &mdash; the booking, and everything after,
    is ours. To change your cities or step off the list, reply and say so; a person reads it.</div>
  <div style="{mono(9, MUTE, 'text-align:center;margin-top:20px;')}">Latitude 43 &#183; The Travel Office &#183; Toronto 43&#176;N</div>
</td></tr>

</table>
</td></tr></table>
</body></html>""")

    return subject, "".join(parts)


def main(argv=None):
    p = argparse.ArgumentParser(description="Build a Latitude 43 city alert email")
    p.add_argument("--city", required=True, help="hub slug, e.g. chicago")
    p.add_argument("--window", help="checkin..checkout; default latest scanned")
    p.add_argument("--min-star", type=float, default=4.0)
    p.add_argument("--min-rating", type=float, default=8.5)
    p.add_argument("--out", help="output HTML path (default out/email_<city>.html)")
    args = p.parse_args(argv)

    subject, body = build(args.city, args.window, args.min_star, args.min_rating)
    out = args.out or os.path.join(HERE, "out", f"email_{slug(args.city)}.html")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(body + "\n")
    print(f"Subject: {subject}")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
