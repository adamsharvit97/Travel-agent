#!/usr/bin/env python3
"""
Latitude 43 — client-facing Toronto deal calendar.

Reads the master catalog + price observations and renders a polished,
website-styled page: the full roster of Toronto's business/event hotels
(4-star and up), week by week, with sale weeks clearly badged. Hotels that
never discount (Four Seasons, St. Regis...) still appear — at full rate —
because the roster is the product, not just the deals.

    python3 build_client_calendar.py            # -> ../website/toronto-deal-calendar.html
"""

from __future__ import annotations

import csv
import json
import os
from datetime import date, datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(HERE, "catalog", "toronto.json")
OBSERVATIONS = os.path.join(HERE, "data", "observations.csv")
DEFAULT_OUT = os.path.join(HERE, "..", "website", "toronto-deal-calendar.html")

# Marquee business hotels with no Expedia deal history in our scans yet.
# They belong on the page at full rate; tracked here until they surface
# in a scan with a real Expedia id.
OVERLAY = {
    "x-st-regis":       {"name": "The St. Regis Toronto", "star": 5.0, "area": "Bay & Adelaide (Financial District)"},
    "x-ritz-carlton":   {"name": "The Ritz-Carlton, Toronto", "star": 5.0, "area": "Wellington St W (Financial / Entertainment)"},
    "x-park-hyatt":     {"name": "Park Hyatt Toronto", "star": 5.0, "area": "Avenue Rd & Bloor (Yorkville)"},
    "x-w-toronto":      {"name": "W Toronto", "star": 4.5, "area": "Bloor-Yorkville"},
    "x-westin-harbour": {"name": "The Westin Harbour Castle", "star": 4.0, "area": "Queens Quay (Waterfront)"},
}

# The curated roster: section -> ordered hotel ids. This is the editorial
# answer to "which hotels do business travelers actually use in Toronto."
ROSTER = [
    ("The Financial District & Union Station", [
        ("x-st-regis",  "Toronto's definitive financial-core luxury address — in the Adelaide & Bay tower, Louix Louis on 31, and the city's most senior-meeting-friendly suites."),
        ("5178153",     "Five-star calm directly on University Avenue; the lobby lounge is a default for discreet client conversations, minutes on foot from the courts and the banks."),
        ("25713",       "The 1903 grande dame of King Street — ballrooms, the Consort Bar, and a St. Lawrence / Financial District location that flatters any meeting on Bay."),
        ("17289",       "1,300+ rooms across from Union Station with direct PATH access — Toronto's institutional conference hotel and the safest one-answer for groups and events."),
        ("4978",        "Quietly excellent Front Street base attached to the convention-centre corridor; a long-time favourite for board cycles at the towers above."),
        ("1234327",     "A working bank tower turned all-suite hotel at Yonge & King — kitchens, separate workspaces, and the Financial District outside the front door."),
        ("8301308",     "Modern Marriott flagship in the South Core, skybridged toward Union and the CN-corridor offices; dependable for project teams in for the week."),
        ("3988366",     "Le Germain's boutique at Maple Leaf Square — the polished choice when the trip mixes business with a Scotiabank Arena evening."),
        ("3571492",     "Eleven-suite hideaway above Verity club on Queen East — private, quiet, and beloved by principals who don't want a lobby."),
        ("x-westin-harbour", "The waterfront convention anchor — vast meeting inventory and harbour views, ten minutes from Bay Street and the island airport."),
        ("23541",       "The city's biggest meeting machine at Queen & Bay — 130,000 sq ft of event space, PATH-connected, across from City Hall."),
        ("900502",      "Reliable upscale Hilton at Richmond & University — walkable to the courts, hospitals, and the western Financial District."),
        ("17503",       "Built into Rogers Centre at the South Core; convenient for events at the stadium and the rail-corridor towers."),
        ("18781",       "All-suite value in the downtown core — every room a suite with workspace, and one of the most consistently discounted quality hotels in the city."),
        ("8214",        "Compact, sharp, and steps from Union Station — the efficient overnight for an in-and-out day on Bay Street."),
        ("1056271",     "Boutique quiet at Yonge & Dundas with suite-style rooms — a value-forward base two subway stops from King."),
    ]),
    ("Yorkville, Downtown & the Entertainment District", [
        ("14358",       "The global flagship of the brand born in Toronto — Yorkville's power address, with d|bar deal-making downstairs and the city's best suites upstairs."),
        ("1688828",     "Toronto's small luxury benchmark (9.8 on Expedia) — 77 rooms, ONE restaurant, and the discretion that draws film and finance alike."),
        ("x-ritz-carlton", "Wellington Street's club-level standby between the Financial and Entertainment districts — Forbes five-star service, steps from Roy Thomson Hall."),
        ("x-park-hyatt", "Reborn on Avenue Road with the Writers Room bar over the museum district — midtown gravitas for academic, medical, and cultural business."),
        ("2920159",     "Sustainable five-star on King West — the design-forward choice for tech and media meetings, and one of the most reliably discounted luxury hotels in the city."),
        ("52918",       "A 1927 Yorkville institution with butler-attended suites and a tea room that still closes deals the old way."),
        ("x-w-toronto", "Bloor-Yorkville's high-energy option — rooftop bar and studio spaces suited to launches, press days, and creative teams."),
        ("898670",      "Boutique luxury on Wellington West with serious soundproofing and a loyal entertainment-industry following."),
        ("83844945",    "Canopy by Hilton's Yorkville lifestyle play — fresh rooms and a rooftop with skyline views, attached to the Bloor-Yonge business spine."),
        ("2232458",     "Curio-collection style on the Entertainment District's quiet edge — 9.6-rated and walkable to King West's client dinners."),
        ("9495",        "Yorkville's dependable upscale Sonesta on Avenue Road — generous rooms for longer stays near the museum and Bloor corridors."),
        ("19752581",    "JdV by Hyatt's house-party boutique at Church & Charles — character rooms and a barber shop, minutes from Bloor."),
        ("106831048",   "TOOR's new-build JdV at Dundas & Jarvis — smart rooms, a rooftop, and consistent 15%-off pricing all season."),
        ("117279789",   "RIU's 29-storey plaza at Bay & Dundas — big-hotel polish at the city's most aggressive quality discount, regularly 40–50% off."),
        ("21783",       "DoubleTree's full-service downtown anchor at Chestnut & Dundas, beside City Hall and the hospital row."),
        ("19371",       "King West's Entertainment District regular — steps from TIFF Lightbox and the restaurant row where client dinners actually happen."),
    ]),
    ("Beyond the core", [
        ("19822661",    "Hotel X's lakefront resort campus at Exhibition Place — tennis, cinema, rooftop pools, and the default for trade shows at the grounds."),
        ("13735",       "Kimpton's Annex boutique on Bloor — first choice for University of Toronto and Yorkville-adjacent academic business."),
        ("18382156",    "The east side's 1891 landmark at Queen & Broadview — rooftop views and boutique character for Riverside and Leslieville work."),
        ("914322",      "A Tudor-style events estate on the Humber — 60,000 sq ft of function space, gardens for offsites, and steady ~20% discounts."),
    ]),
    ("Airport & Greater Toronto", [
        ("19627",       "The composed choice at YYZ — Westin calm, terminal-adjacent, for the one-night turnaround."),
        ("1754017",     "Sandman's flagship by the airport — fresh build, strong value, and frequent sale pricing."),
        ("16617",       "Full-service Marriott on the airport strip with dependable meeting rooms for fly-in/fly-out sessions."),
        ("19088",       "Delta's airport conference centre — the workhorse for suburban group meetings."),
        ("441192",      "DoubleTree's airport option — solid, predictable, points-friendly."),
        ("444543",      "Mississauga's best-rated business base, close to the Airport Corporate Centre office parks."),
        ("94900038",    "The casino-resort surprise at Woodbine — genuinely excellent rooms (9.0, ~6,000 reviews) at the deepest reliable discounts in the GTA; 25 minutes from downtown."),
    ]),
]


def monday(d: str) -> date:
    dt = datetime.strptime(d, "%Y-%m-%d").date()
    return dt - timedelta(days=dt.weekday())


def load():
    with open(CATALOG, encoding="utf-8") as fh:
        catalog = json.load(fh)
    hotels = dict(catalog["hotels"])
    for hid, h in OVERLAY.items():
        hotels.setdefault(hid, {**h, "guest_rating": None, "review_count": 0})
    with open(OBSERVATIONS, encoding="utf-8") as fh:
        obs = list(csv.DictReader(fh))
    return hotels, obs


def weekly_best(obs):
    """(hotel_id, week_monday) -> best deal observation that week."""
    best, weeks = {}, set()
    for o in obs:
        wk = monday(o["checkin"])
        weeks.add(wk)
        if o["on_deal"] != "1":
            continue
        key = (o["hotel_id"], wk)
        if key not in best or float(o["discount_pct"]) > float(best[key]["discount_pct"]):
            best[key] = o
    return best, sorted(weeks)


def money(v):
    try:
        return f"${float(v):,.0f}"
    except (TypeError, ValueError):
        return "—"


def build(out_path: str) -> str:
    hotels, obs = load()
    best, weeks = weekly_best(obs)

    def wk_label(w):
        return w.strftime("%b %-d") if os.name != "nt" else w.strftime("%b %d")

    n_deal_hotels = len({hid for (hid, _) in best})

    # ---- matrix rows ----
    sections_html = []
    directory_html = []
    for section, entries in ROSTER:
        rows = []
        dir_cards = []
        for hid, blurb in entries:
            h = hotels.get(hid)
            if not h:
                continue
            star = f"{h.get('star'):g}" if h.get("star") else "?"
            rating = h.get("guest_rating")
            revs = h.get("review_count") or 0
            rating_str = (f'{rating} <span class="revs">({revs:,})</span>'
                          if rating else '<span class="revs">—</span>')
            cells = []
            hit = 0
            best_pct = 0.0
            best_rate = None
            for w in weeks:
                o = best.get((hid, w.isoformat()[:10])) or best.get((hid, w))
                if o:
                    pct = float(o["discount_pct"])
                    hit += 1
                    if pct > best_pct:
                        best_pct, best_rate = pct, o["nightly_price"]
                    cells.append(
                        f'<td><span class="pill" title="{h["name"]} — week of '
                        f'{wk_label(w)}: {money(o["nightly_price"])}/nt, {pct:.0f}% off">'
                        f'&minus;{pct:.0f}%</span></td>'
                    )
                else:
                    cells.append('<td><span class="dot">·</span></td>')
            rows.append(
                f'<tr><th scope="row"><span class="hname">{h["name"]}</span>'
                f'<span class="hmeta">{star}★ · {rating_str} · {h.get("area","")}</span></th>'
                f'{"".join(cells)}</tr>'
            )
            if hit:
                deal_line = (f'On sale {hit} of {len(weeks)} weeks this summer — '
                             f'best seen {best_pct:.0f}% off ({money(best_rate)}/night).')
            else:
                deal_line = ('Holds rate all summer. We book it for the property — '
                             'and add the advisor perks the public rate never shows.')
            dir_cards.append(
                f'<div class="card"><h4>{h["name"]} <span class="cstar">{star}★</span></h4>'
                f'<p class="carea">{h.get("area","")}</p>'
                f'<p>{blurb}</p>'
                f'<p class="cdeal{" full" if not hit else ""}">{deal_line}</p></div>'
            )
        head_cells = "".join(f"<th>{wk_label(w)}</th>" for w in weeks)
        sections_html.append(
            f'<tr class="sec"><th scope="row" colspan="{len(weeks)+1}">{section}</th></tr>'
            + "".join(rows)
        )
        directory_html.append(f'<h3 class="dirsec">{section}</h3><div class="cards">{"".join(dir_cards)}</div>')

    head_cells = "".join(f'<th><span class="wk">wk of</span>{wk_label(w)}</th>' for w in weeks)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Toronto Hotel Sale Calendar — Latitude 43</title>
<meta name="description" content="Every business hotel that matters in Toronto, week by week through the summer — and which ones are on sale.">
<meta name="theme-color" content="#0E1A2B">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root {{ --navy:#0E1A2B; --ivory:#F4EFE6; --bone:#E8E0D0; --brass:#B8924C; --sand:#C9BFAB;
        --serif:'EB Garamond', Georgia, serif; --sans:'Inter', -apple-system, sans-serif; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:var(--navy); color:var(--ivory); font-family:var(--serif); }}
.header {{ display:flex; justify-content:space-between; align-items:center;
           padding:26px 48px; border-bottom:1px solid rgba(244,239,230,.12); }}
.mark {{ text-decoration:none; color:var(--ivory); font-size:21px; letter-spacing:.04em; }}
.mark .num {{ color:var(--brass); font-style:italic; margin-left:4px; }}
.header nav a {{ color:var(--sand); text-decoration:none; font-family:var(--sans);
                 font-size:13px; letter-spacing:.08em; text-transform:uppercase; }}
.hero {{ max-width:1180px; margin:64px auto 48px; padding:0 48px; }}
.eyebrow {{ font-family:var(--sans); font-size:12px; letter-spacing:.22em; text-transform:uppercase;
            color:var(--brass); margin-bottom:18px; }}
h1 {{ font-weight:500; font-size:46px; line-height:1.12; max-width:760px; }}
.lede {{ margin-top:20px; font-size:19px; line-height:1.6; color:var(--bone); max-width:680px; }}
.stats {{ display:flex; gap:48px; margin-top:36px; font-family:var(--sans); }}
.stat b {{ display:block; font-family:var(--serif); font-weight:500; font-size:30px; color:var(--ivory); }}
.stat span {{ font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--sand); }}
.calwrap {{ max-width:1320px; margin:24px auto 0; padding:0 48px; overflow-x:auto; }}
table {{ border-collapse:collapse; width:100%; min-width:1100px; font-family:var(--sans); font-size:12.5px; }}
thead th {{ position:sticky; top:0; background:var(--navy); color:var(--brass); font-weight:600;
            padding:10px 6px; border-bottom:1px solid rgba(184,146,76,.45); text-align:center; white-space:nowrap; }}
thead th:first-child {{ text-align:left; }}
thead .wk {{ display:block; font-weight:400; font-size:10px; letter-spacing:.14em;
             text-transform:uppercase; color:var(--sand); }}
tbody th[scope=row] {{ text-align:left; padding:10px 14px 10px 0; border-bottom:1px solid rgba(244,239,230,.08);
                       min-width:250px; font-weight:400; }}
tbody td {{ text-align:center; border-bottom:1px solid rgba(244,239,230,.08); padding:6px 3px; }}
.hname {{ font-family:var(--serif); font-size:16px; display:block; }}
.hmeta {{ font-size:11px; color:var(--sand); }}
.hmeta .revs {{ color:rgba(201,191,171,.6); }}
.pill {{ display:inline-block; background:var(--brass); color:var(--navy); font-weight:600;
         border-radius:20px; padding:3px 8px; font-size:11.5px; white-space:nowrap; }}
.dot {{ color:rgba(244,239,230,.22); }}
tr.sec th {{ padding:30px 0 10px; border-bottom:1px solid rgba(184,146,76,.45) !important;
             font-family:var(--serif); font-style:italic; font-size:19px; color:var(--brass); }}
.legend {{ max-width:1320px; margin:18px auto 0; padding:0 48px; font-family:var(--sans);
           font-size:12px; color:var(--sand); }}
.legend .pill {{ font-size:10.5px; }}
.directory {{ max-width:1180px; margin:80px auto 0; padding:0 48px; }}
.directory h2 {{ font-weight:500; font-size:32px; }}
.dirsec {{ margin:42px 0 16px; font-style:italic; font-weight:500; font-size:21px; color:var(--brass); }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(330px, 1fr)); gap:18px; }}
.card {{ border:1px solid rgba(244,239,230,.12); padding:20px 22px; }}
.card h4 {{ font-weight:500; font-size:18px; }}
.card .cstar {{ color:var(--brass); font-size:14px; }}
.card .carea {{ font-family:var(--sans); font-size:11px; letter-spacing:.08em; text-transform:uppercase;
                color:var(--sand); margin:4px 0 10px; }}
.card p {{ font-size:15px; line-height:1.55; color:var(--bone); }}
.card .cdeal {{ margin-top:12px; font-family:var(--sans); font-size:12.5px; color:var(--brass); }}
.card .cdeal.full {{ color:var(--sand); }}
.note {{ max-width:1180px; margin:72px auto 0; padding:32px 48px; border-top:1px solid rgba(244,239,230,.12);
         font-family:var(--sans); font-size:12.5px; line-height:1.7; color:var(--sand); }}
.footer {{ text-align:center; padding:40px 0 56px; font-family:var(--sans); font-size:12px;
           letter-spacing:.12em; text-transform:uppercase; color:var(--sand); }}
@media (max-width:720px) {{ .hero, .calwrap, .legend, .directory, .note {{ padding:0 22px; }}
  h1 {{ font-size:32px; }} .header {{ padding:20px 22px; }} }}
</style>
</head>
<body>

<header class="header">
  <a class="mark" href="index.html">Latitude <span class="num">43°</span></a>
  <nav><a href="contact.html">The Desk</a></nav>
</header>

<section class="hero">
  <div class="eyebrow">Toronto · Summer {weeks[0].year}</div>
  <h1>The hotels that matter in Toronto — and the weeks they go on sale.</h1>
  <p class="lede">Every 4- and 5-star property business travelers actually use, tracked
  week by week from {wk_label(weeks[0])} through {wk_label(weeks[-1])}. A brass badge
  means the hotel is selling below its standard rate that week. No badge means it is
  holding rate — and we book it for the property, with the perks our desk adds either way.</p>
  <div class="stats">
    <div class="stat"><b>{sum(len(e) for _, e in ROSTER)}</b><span>hotels tracked</span></div>
    <div class="stat"><b>{len(weeks)}</b><span>weeks scanned</span></div>
    <div class="stat"><b>{n_deal_hotels}</b><span>on sale this season</span></div>
  </div>
</section>

<div class="calwrap">
<table>
  <thead><tr><th>Hotel</th>{head_cells}</tr></thead>
  <tbody>
  {''.join(sections_html)}
  </tbody>
</table>
</div>
<p class="legend"><span class="pill">&minus;25%</span>&nbsp; on sale that week (vs. the hotel's standard
rate; hover for the nightly figure) &nbsp;·&nbsp; a dot means holding full rate.</p>

<section class="directory">
  <h2>The roster, hotel by hotel.</h2>
  {''.join(directory_html)}
</section>

<div class="note">
  <strong>How this is built.</strong> Rates are sampled for two-night, single-guest stays at
  check-ins across each week shown, against each property's published standard rate. Sale
  percentages reflect the best discount observed that week and change daily; they are a guide
  to <em>when</em> a hotel tends to sell, not a quoted price. Hotels shown without sale weeks
  rarely discount publicly — for those, the desk's value is the negotiated extras: breakfast,
  upgrades, property credits, and late checkout. Refreshed {date.today().strftime('%B %-d, %Y') if os.name != 'nt' else date.today().strftime('%B %d, %Y')}.
</div>

<footer class="footer">Latitude 43 · The Travel Office · Toronto, 43°N</footer>

</body>
</html>"""

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out_path


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT
    print(f"Wrote {build(out)}")
