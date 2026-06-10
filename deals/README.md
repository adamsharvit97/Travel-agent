# Latitude 43 — Hotel Deal Finder

A quality-first hotel deal engine for business travel. Maintains a **master
catalog** of business-relevant hotels per city (including ones that rarely
discount, like the Four Seasons) and detects which are **on deal right now**,
ranked by quality rather than by raw price.

## Major travel hubs

The engine now tracks 10 hubs, registered in `catalog/_hubs.json` (each with a
financial-core anchor for distance tiers and airport anchors for the Airport
tier): **Toronto, New York, Chicago, Boston, San Francisco, Los Angeles,
Miami, Washington D.C., Dallas, Atlanta**. City keys are slugs
(`new-york`, `washington-dc`, ...). Adding a hub = add a registry entry, scan,
ingest.

```bash
python3 latitude43_deals.py cities          # hub list + catalog/observation counts
python3 latitude43_deals.py curate --city chicago   # infer brands from names
```

## Why two layers

- **Master catalog** (`catalog/<city>.json`) — the full, stable roster of
  business hotels. Curated attributes only (brand, star, rating, area, tier).
  A hotel stays in the catalog whether or not it currently has a deal, so the
  Four Seasons surfaces the moment it discounts and never disappears when it
  doesn't.
- **Observations** (`data/observations.csv`) — an append-only time-series of
  priced searches. A deal is detected from Expedia's **strikeout price**, not
  the `discounted_only` filter (which would silently drop full-rate luxury).

Over time the observation history lets us tell a *real* deal from an inflated
strikethrough.

## The workflow

The Expedia search is an MCP tool available to the Claude agent, not a public
API. So data collection is done by the agent; processing is done by this tool.

1. **Agent runs Expedia `search_hotels`** for the city / date windows and saves
   each raw JSON response into `raw/` — e.g. `raw/2026-06-16_2026-06-18_toronto.json`.
   Pull the *full* 4–5★ roster (do **not** set `discounted_only`).
2. **Ingest** — upserts hotels into the catalog and appends price observations:
   ```bash
   python3 latitude43_deals.py ingest 'raw/*.json'
   ```
   New hotels are added with `_needs_review: true` so curated fields (area,
   tier, brand, segment) can be filled in by hand.
3. **Report** — quality-first ranked deal list (Markdown), ready for the
   client email/artifact:
   ```bash
   python3 latitude43_deals.py report --window 2026-06-16..2026-06-18 \
       --out out/toronto_2026-06-16.md
   ```

## Ranking

Quality-first: **tier → star → guest rating → review volume**. The discount is
shown but does **not** drive the order — a Core-location hotel at 8% off
outranks a suburban motel at 50% off. Tiers: `Core` (Financial District /
Union Station walkable) → `Prime` (downtown / Entertainment District /
Yorkville) → `Secondary` → `Airport` → `Suburban`.

## `report` options

| Flag | Default | Meaning |
|------|---------|---------|
| `--city` | `Toronto` | Which catalog to use |
| `--window` | all | `checkin..checkout`, e.g. `2026-06-16..2026-06-18` |
| `--min-star` | `4.0` | Floor on star rating |
| `--min-rating` | `9.0` | Floor on Expedia guest rating |
| `--top` | none | Cap the on-deal list to N |
| `--no-full-rate` | off | Hide the full-rate (no-deal) catalog section |
| `--out` | stdout | Write Markdown to a file |

## City alerts (signup page → Excel list → email)

The subscription loop lives next to the pipeline:

1. **Signup page** — `alerts/index.html` + `alerts/server.py` (stdlib HTTP +
   `openpyxl`). The page renders the hub list from `catalog/_hubs.json` as
   checkboxes; a visitor picks cities, leaves name + email.
   ```bash
   python3 alerts/server.py          # http://localhost:8043
   ```
2. **Subscriber list (Excel, for now)** — `data/subscribers.xlsx`, one row per
   subscriber: `email | name | cities | subscribed_at | updated_at`.
   Re-subscribing with the same email updates that person's city list.
   ```bash
   python3 alerts/subscribers.py list --city chicago   # who to email for Chicago
   python3 alerts/subscribers.py all
   ```
3. **The alert email** — `build_alert_email.py` renders a city's current
   deals into the branded letter (lookbook direction, email-safe tables +
   inline styles): hero, "Deepest right now" feature, ledger of other
   softenings, the luxury houses holding rate, desk sign-off. Prints a
   suggested subject line.
   ```bash
   python3 build_alert_email.py --city chicago         # -> out/email_chicago.html
   python3 build_alert_email.py --city toronto --window 2026-06-16..2026-06-18
   ```

Sending is manual for now: build the email, pull the city's list, send via
the desk's mail client (BCC).

## Files

```
deals/
  latitude43_deals.py     # pipeline (stdlib only, no dependencies)
  build_alert_email.py    # branded city-alert email generator
  catalog/_hubs.json      # hub registry: anchors, airports, display names
  catalog/<city>.json     # master catalogs — curated, stable
  data/observations.csv   # appended price observations (time-series)
  data/subscribers.xlsx   # alert subscriber list (Excel, for now)
  alerts/                 # signup page + server + subscriber store
  raw/                    # raw Expedia search JSON dropped here by the agent
  out/                    # generated reports + sample emails
```
