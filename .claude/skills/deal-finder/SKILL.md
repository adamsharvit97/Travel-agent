---
name: deal-finder
description: Run the Latitude 43 hotel deal pipeline — scan Expedia for a city's full 4–5★ business-hotel roster, ingest into the master catalog and price-observation time-series, and generate quality-first deal reports, multi-window views, coverage leaderboards, 3-month outlook heatmaps, and the client-facing deal calendar. Use when the user asks to find or refresh hotel deals, run a deal scan or deal report, update the deal calendar, or mentions Latitude 43, the catalog, or observations.
---

# Latitude 43 — Hotel Deal Finder

Everything lives in `deals/`. Two layers: the **master catalog**
(`catalog/<city>.json`, curated, stable — hotels stay listed whether or not
they're discounting) and **observations** (`data/observations.csv`,
append-only price time-series). A deal = Expedia's strikeout price > the
actual total. Full background: `deals/README.md`.

## The pipeline

### 1. Scan (agent does this)

Call the Expedia MCP tool `search_hotels` for the city and date window(s).

- Pull the **full 4–5★ roster**. **Never set `discounted_only`** — it silently
  drops full-rate luxury (Four Seasons, St. Regis), and deal detection uses
  the strikeout price instead.
- Save each tool response **verbatim** (it must keep the top-level `data`
  array and `occupants`) to `deals/raw/<checkin>_<checkout>_<city>.json`,
  e.g. `deals/raw/2026-06-16_2026-06-18_toronto.json`.
- For outlook/coverage runs, sweep several check-in dates (e.g. weekly
  Tuesdays, 2-night stays) and save one file per window.

### 2. Ingest

```bash
cd deals && python3 latitude43_deals.py ingest 'raw/*.json'
```

Upserts hotels into the catalog and appends observations. Re-ingesting the
same file appends duplicate rows — pass only the new files when possible.
New hotels land with `_needs_review: true`; afterwards, fill in their
curated fields (`area`, `tier`, `brand`, `segment`) in `catalog/<city>.json`
by hand. Tiers: `Core` → `Prime` → `Secondary` → `Airport` → `Suburban`.

### 3. Report

```bash
cd deals && python3 latitude43_deals.py report --window 2026-06-16..2026-06-18 --out out/toronto_2026-06-16.md
```

Ranking is **quality-first** (tier → star → guest rating → review volume);
the discount is shown but never drives the order.

Modes (mutually exclusive; default is the single-window report):

| Mode | Flag | What it gives |
|------|------|---------------|
| Single window | `--window CI..CO` | Ranked on-deal list + full-rate roster for one stay |
| Multi-window | `--consolidated` (+ `--deals-only`) | Best deal per hotel across all scanned windows |
| Coverage | `--coverage` (+ `--checkin-from DATE`) | "Reliably discounting" leaderboard over the forward horizon |
| Outlook | `--outlook` (+ `--html-out FILE`) | Hotels × dates deal matrix; HTML version is a heatmap |

Common flags: `--city` (default Toronto), `--min-star` (4.0),
`--min-rating` (9.0), `--top N`, `--no-full-rate`, `--out FILE`.
Reports go in `deals/out/`.

### 4. Client calendar (optional)

```bash
cd deals && python3 build_client_calendar.py
```

Rebuilds `website/toronto-deal-calendar.html` — the polished week-by-week
roster page. The editorial roster and the marquee-hotel overlay (St. Regis,
Ritz, Park Hyatt…) are hardcoded in `build_client_calendar.py`; edit there
to add hotels or blurbs.

## Rules of thumb

- Scripts are stdlib-only; no installs needed.
- Don't hand-edit `data/observations.csv`; it's the append-only history that
  lets us tell a real deal from an inflated strikethrough.
- After any ingest that reports new hotels, review them before shipping a
  report — un-curated tier/area makes the quality ranking lie.
