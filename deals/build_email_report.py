#!/usr/bin/env python3
"""
Latitude 43 — hotel deal EMAIL report generator (city-agnostic).

Renders the "cinematic x lookbook" hybrid the founder approved:
  - photographic masthead + short letter (cinematic)
  - a featured hero deal + two tiles for the deepest softenings (lookbook)
  - the full season, week by week, with every sampled date (more dates)

Reads catalog/<city>.json + data/observations.csv (already ingested by
latitude43_deals.py) and writes a self-contained HTML email.

    python3 build_email_report.py --city Toronto --out out/toronto_email.html

The skill `hotel-deal-report` drives the scan + ingest before calling this.
Photography is placeholder dark-luxury stock — the office swaps real imagery.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from datetime import datetime, timedelta, date

HERE = os.path.dirname(os.path.abspath(__file__))

# Placeholder dark-luxury imagery (cycled deterministically per hotel).
MAST = "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?auto=format&fit=crop&w=1280&q=85"
TILES = [
    "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1280&q=85",
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=720&q=85",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=720&q=85",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1280&q=85",
    "https://images.unsplash.com/photo-1564501049412-61c2a3083791?auto=format&fit=crop&w=1280&q=85",
]


def monday(d: str):
    dt = datetime.strptime(d, "%Y-%m-%d").date()
    return dt - timedelta(days=dt.weekday())


def fmt_day(d):
    return d.strftime("%b %-d") if os.name != "nt" else d.strftime("%b %d")


def money(v):
    try:
        return f"${float(v):,.0f}"
    except (TypeError, ValueError):
        return "—"


def img_for(hid, i=None):
    if i is not None:
        return TILES[i % len(TILES)]
    return TILES[sum(ord(c) for c in str(hid)) % len(TILES)]


def load(city):
    cat_path = os.path.join(HERE, "catalog", f"{city.lower()}.json")
    with open(cat_path, encoding="utf-8") as fh:
        catalog = json.load(fh)
    with open(os.path.join(HERE, "data", "observations.csv"), encoding="utf-8") as fh:
        obs = [o for o in csv.DictReader(fh) if o["city"].lower() == city.lower()]
    return catalog, obs


def weekly_best(obs, hotels, min_star, min_rating, checkin_from):
    """(hid, week) -> best deal obs; plus the ordered list of weeks."""
    best, weeks = {}, set()
    for o in obs:
        if checkin_from and o["checkin"] < checkin_from:
            continue
        wk = monday(o["checkin"])
        weeks.add(wk)
        if o["on_deal"] != "1":
            continue
        h = hotels.get(o["hotel_id"])
        if not h or (h.get("star") or 0) < min_star or (h.get("guest_rating") or 0) < min_rating:
            continue
        k = (o["hotel_id"], wk)
        if k not in best or float(o["discount_pct"]) > float(best[k]["discount_pct"]):
            best[k] = o
    return best, sorted(weeks)


def build(city, out_path, min_star=4.0, min_rating=9.0, checkin_from=None):
    catalog, obs = load(city)
    hotels = catalog["hotels"]
    best, weeks = weekly_best(obs, hotels, min_star, min_rating, checkin_from)
    if not weeks:
        raise SystemExit(f"No deal observations for {city}.")
    city_name = catalog.get("city", city)

    def meta(hid):
        h = hotels[hid]
        star = f"{h.get('star'):g}" if h.get("star") else "?"
        rev = h.get("review_count") or 0
        loc = h.get("area") or ""
        return star, h.get("guest_rating"), rev, loc

    # Featured: the three deepest distinct hotels across the whole period.
    by_hotel = {}
    for (hid, wk), o in best.items():
        cur = by_hotel.get(hid)
        if cur is None or float(o["discount_pct"]) > float(cur[1]["discount_pct"]):
            by_hotel[hid] = (wk, o)
    feat = sorted(by_hotel.items(), key=lambda kv: -float(kv[1][1]["discount_pct"]))[:3]

    # --- featured hero ---
    fhid, (fwk, fo) = feat[0]
    fstar, frat, frev, floc = meta(fhid)
    hero = f"""
  <div class="feat">
    <img src="{img_for(fhid, 0)}" alt="">
    <div class="feat-veil"></div>
    <div class="feat-cap">
      <div class="tier mono">Deepest this season · week of {fmt_day(fwk)}</div>
      <h2>{hotels[fhid]['name']}</h2>
      <div class="loc">{fstar}★ · {frat} ({frev:,} reviews){(' · ' + floc) if floc else ''}</div>
      <div class="deal"><span class="pct">&minus;{float(fo['discount_pct']):.0f}%</span>
        <span class="rate">{money(fo['nightly_price'])} a night</span></div>
    </div>
  </div>"""

    tiles = []
    for i, (hid, (wk, o)) in enumerate(feat[1:3], start=1):
        st, rt, rv, lc = meta(hid)
        tiles.append(f"""
    <div class="tile">
      <img src="{img_for(hid, i)}" alt="">
      <div class="tile-veil"></div>
      <div class="tile-cap"><h3>{hotels[hid]['name']}</h3>
        <div class="loc">{st}★{(' · ' + lc) if lc else ''}</div>
        <div class="pct">&minus;{float(o['discount_pct']):.0f}%<small>{money(o['nightly_price'])}/nt</small></div></div>
    </div>""")
    tiles_html = f'<div class="tiles">{"".join(tiles)}</div>' if tiles else ""

    # --- full season, week by week ---
    wk_blocks = []
    for wk in weeks:
        rows = sorted(
            [(hid, o) for (hid, w), o in best.items() if w == wk],
            key=lambda r: -float(r[1]["discount_pct"]),
        )
        if not rows:
            continue
        body = []
        for hid, o in rows[:6]:
            st, rt, rv, lc = meta(hid)
            body.append(f"""
      <div class="row"><div class="nm"><div class="h">{hotels[hid]['name']}</div>
        <div class="s">{st}★ · {rt}{(' · ' + lc) if lc else ''}</div></div>
        <div class="off"><span class="opct">&minus;{float(o['discount_pct']):.0f}%</span>
          <span class="orate">{money(o['nightly_price'])}/nt</span></div></div>""")
        more = len(rows) - 6
        more_html = (f'<div class="more">+ {more} more rooms softening this week</div>'
                     if more > 0 else "")
        wk_blocks.append(f"""
    <div class="wk">
      <div class="wk-h"><span class="date">Week of {fmt_day(wk)}</span>
        <span class="count mono">{len(rows)} on sale</span></div>
      {''.join(body)}
      {more_html}
    </div>""")

    n_hotels = len(by_hotel)
    span = f"{fmt_day(weeks[0])} – {fmt_day(weeks[-1])}"
    today = date.today().strftime("%B %-d, %Y") if os.name != "nt" else date.today().strftime("%B %d, %Y")

    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Latitude 43 — The {city_name} Calendar</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>
  :root{{ --bg:#0C0A09; --bg2:#13110F; --line:#2A241C; --text:#F2ECDF; --soft:#C6BCA6;
         --mute:#827763; --gold:#D9B987; --goldb:#F2D29E; }}
  *{{margin:0;padding:0;box-sizing:border-box;}}
  body{{background:#050403;font-family:'Inter',sans-serif;color:var(--text);-webkit-font-smoothing:antialiased;}}
  .frame{{max-width:640px;margin:0 auto;background:var(--bg);}}
  .mono{{font-family:'JetBrains Mono',monospace;letter-spacing:.22em;text-transform:uppercase;}}
  .cover{{position:relative;height:340px;overflow:hidden;}}
  .cover img{{width:100%;height:100%;object-fit:cover;filter:saturate(.85) brightness(.72);display:block;}}
  .cover-veil{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,10,9,.5) 0%,rgba(12,10,9,.12) 38%,rgba(12,10,9,.97) 100%);}}
  .cover-top{{position:absolute;top:28px;left:0;right:0;display:flex;justify-content:space-between;align-items:center;padding:0 34px;}}
  .brand{{font-family:'Playfair Display',serif;font-size:20px;letter-spacing:.04em;}}
  .brand i{{color:var(--gold);font-style:italic;}}
  .cover-top .tag{{font-size:9.5px;color:var(--soft);}}
  .cover-cap{{position:absolute;left:34px;right:34px;bottom:32px;}}
  .eyebrow{{font-size:10px;color:var(--gold);margin-bottom:14px;}}
  h1{{font-family:'Playfair Display',serif;font-weight:400;font-size:36px;line-height:1.13;}}
  h1 i{{font-style:italic;color:var(--goldb);}}
  .letter{{padding:38px 38px 6px;}}
  .letter p{{font-size:15px;line-height:1.72;color:var(--soft);}}
  .letter .lead{{color:var(--text);font-size:16px;}}
  .letter p + p{{margin-top:13px;}}
  .feat{{position:relative;margin:26px 0 6px;}}
  .feat img{{width:100%;height:320px;object-fit:cover;filter:brightness(.74) saturate(.9);display:block;}}
  .feat-veil{{position:absolute;inset:0;background:linear-gradient(180deg,transparent 32%,rgba(12,10,9,.96) 100%);}}
  .feat-cap{{position:absolute;left:32px;right:32px;bottom:26px;}}
  .feat-cap .tier{{font-size:10px;color:var(--goldb);margin-bottom:10px;}}
  .feat-cap h2{{font-family:'Playfair Display',serif;font-weight:400;font-size:26px;}}
  .feat-cap .loc{{font-size:12px;color:var(--soft);margin-top:4px;}}
  .feat-cap .deal{{margin-top:13px;display:flex;align-items:baseline;gap:12px;}}
  .feat-cap .pct{{font-family:'Playfair Display',serif;font-size:30px;color:var(--goldb);}}
  .feat-cap .rate{{font-size:12px;color:var(--soft);}}
  .tiles{{display:flex;gap:6px;}}
  .tile{{flex:1;position:relative;}}
  .tile img{{width:100%;height:180px;object-fit:cover;filter:brightness(.7) saturate(.9);display:block;}}
  .tile-veil{{position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(12,10,9,.96) 100%);}}
  .tile-cap{{position:absolute;left:16px;right:16px;bottom:16px;}}
  .tile-cap h3{{font-family:'Playfair Display',serif;font-weight:400;font-size:16px;line-height:1.15;}}
  .tile-cap .loc{{font-size:10px;color:var(--soft);margin-top:3px;}}
  .tile-cap .pct{{font-family:'Playfair Display',serif;font-size:19px;color:var(--goldb);margin-top:7px;}}
  .tile-cap .pct small{{font-family:'Inter';font-size:11px;color:var(--soft);margin-left:6px;}}
  .season{{padding:30px 38px 8px;}}
  .season-h{{font-size:10px;color:var(--gold);margin-bottom:6px;}}
  .season-sub{{font-family:'Playfair Display',serif;font-size:23px;margin-bottom:6px;}}
  .season-note{{font-size:12.5px;color:var(--mute);margin-bottom:8px;}}
  .wk{{padding:24px 0 18px;border-top:1px solid var(--line);}}
  .wk-h{{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:12px;}}
  .wk-h .date{{font-family:'Playfair Display',serif;font-size:20px;}}
  .wk-h .count{{font-size:9.5px;color:var(--mute);}}
  .row{{display:flex;align-items:baseline;gap:14px;padding:9px 0;border-bottom:1px solid rgba(42,36,28,.5);}}
  .row:last-of-type{{border-bottom:none;}}
  .nm{{flex:1;}} .nm .h{{font-family:'Playfair Display',serif;font-size:16px;line-height:1.2;}}
  .nm .s{{font-size:10.5px;color:var(--mute);margin-top:2px;}}
  .off{{text-align:right;white-space:nowrap;}}
  .off .opct{{font-family:'Playfair Display',serif;font-size:18px;color:var(--goldb);}}
  .off .orate{{display:block;font-size:10.5px;color:var(--soft);margin-top:1px;}}
  .more{{font-size:11px;color:var(--mute);font-style:italic;padding-top:10px;}}
  .foot{{margin-top:28px;padding:30px 38px 44px;border-top:1px solid var(--line);background:var(--bg2);}}
  .foot p{{font-size:12px;line-height:1.7;color:var(--mute);}}
  .foot a{{color:var(--gold);text-decoration:none;border-bottom:1px solid rgba(217,185,135,.4);padding-bottom:2px;}}
  .sig{{font-size:9.5px;color:var(--mute);text-align:center;margin-top:18px;}}
  @media (max-width:600px){{ h1{{font-size:30px;}} }}
</style></head>
<body><div class="frame">

  <div class="cover">
    <img src="{MAST}" alt="">
    <div class="cover-veil"></div>
    <div class="cover-top"><span class="brand">Latitude <i>43°</i></span>
      <span class="tag mono">The Desk · {city_name}</span></div>
    <div class="cover-cap">
      <div class="eyebrow mono">The {city_name} Calendar · {span}</div>
      <h1>The weeks the city's<br>best rooms <i>soften.</i></h1>
    </div>
  </div>

  <div class="letter">
    <p class="lead">A quiet note from the office. We keep an eye on the rooms our members
    use in {city_name}, and we mark the weeks they go on sale — so a trip can be timed,
    not just booked.</p>
    <p>You think about the meeting, or the people you brought with you. We'll watch the
    rate, hold the booking, and be reachable when something needs handling. Below: the
    deepest softenings of the season, then every week of it.</p>
  </div>
{hero}
  {tiles_html}

  <div class="season">
    <div class="season-h mono">The season, week by week</div>
    <div class="season-sub">{len(weeks)} weeks · {n_hotels} hotels on sale</div>
    <div class="season-note">Best softening seen each week, against the hotel's standard rate.</div>
{''.join(wk_blocks)}
  </div>

  <div class="foot">
    <p>Rates are watched for two-night stays against each hotel's standard published rate;
    figures are the best softening seen that week and move daily — a guide to <em>when</em>
    a room tends to sell, not a quote. Rooms that hold rate are no less worth booking; there,
    our value is the upgrade, the breakfast, the late checkout we add quietly. Refreshed {today}.</p>
    <p style="margin-top:16px;">When a week suits you, simply reply, or <a href="#">reach the desk</a>.</p>
    <p class="sig mono">Latitude 43 · The Travel Office · 43°N</p>
  </div>

</div></body></html>"""

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out_path, len(weeks), n_hotels


def main(argv=None):
    p = argparse.ArgumentParser(description="Latitude 43 hotel deal email report")
    p.add_argument("--city", default="Toronto")
    p.add_argument("--out", default=None)
    p.add_argument("--min-star", type=float, default=4.0)
    p.add_argument("--min-rating", type=float, default=9.0)
    p.add_argument("--checkin-from", default=None,
                   help="only weeks with check-in on/after YYYY-MM-DD")
    args = p.parse_args(argv)
    out = args.out or os.path.join(HERE, "out", f"{args.city.lower()}_email.html")
    path, nweeks, nhotels = build(args.city, out, args.min_star, args.min_rating,
                                  args.checkin_from)
    print(f"Wrote {path} — {nweeks} weeks, {nhotels} hotels on sale.")


if __name__ == "__main__":
    main()
