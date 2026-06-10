---
name: hotel-deal-report
description: Generate a Latitude 43 hotel deal email report for a city. Use when the user wants to run/produce a hotel deal calendar, deal report, or "the hotels thing" for a destination. Asks for the location, scans Expedia across the next ~3 months, and renders the cinematic×lookbook branded email (deals/build_email_report.py).
argument-hint: "[city, optional — will ask if omitted]"
---

Produce the Latitude 43 hotel-deal email for a city: scan the next ~3 months on
Expedia, ingest into the pipeline, and render the branded email artifact.

The Expedia search is an MCP tool only the agent can call, so YOU run the scans
and the Python pipeline (`deals/`) does catalog + rendering. Work from the repo
root.

## 1. Get the location

If the user named a city in the arguments, use it. Otherwise ask: **"Which city
should I run the deal calendar for?"** Normalize to `City, Region, Country`
(e.g. `Toronto, Ontario, Canada`) for the Expedia `destination`, and a short
`City` label (e.g. `Toronto`) for `--city` / filenames. Do not ask anything else
unless the user volunteers constraints — default to 1 guest, 2-night stays, 4–5★
business-friendly hotels.

## 2. Build the date list (next ~3 months, weekly)

Use today's date. Generate **13 weekly check-in dates**, the first one ~7 days
out, each a 2-night stay (checkout = checkin + 2). Example if today is 2026-06-09:
check-ins 06-16, 06-23, 06-30, 07-07, 07-14, 07-21, 07-28, 08-04, 08-11, 08-18,
08-25, 09-01, 09-08.

## 3. Scan Expedia

Load the tool: `ToolSearch` → `select:mcp__Expedia__search_hotels`.

- **One roster pull** (seeds the catalog, including non-discounting luxury):
  same destination, `star_ratings:[4,5]`, `property_themes:["BUSINESS_FRIENDLY"]`,
  `property_types:["HOTEL"]`, `limit:40`, NO `discounted_only`, first check-in date.
- **13 deal pulls**, one per check-in date: same filters plus
  `discounted_only:true`, `limit:30`. These are lean (only on-sale hotels) and
  fast — run them in parallel batches.

Always pass `adult_count:1`, `client_device_info:{"agent_name":"ClaudeCode","device_type":"desktop"}`,
a `user_location`, and `user_locale:"en-US"`.

Save each response's JSON to `deals/raw/<city>_<checkin>.json` (and the roster to
`deals/raw/<city>_roster.json`). Keep only the fields the pipeline reads:
`hotel_id, hotel_name, geo_location{latitude,longitude}, star_rating,
guest_rating, guest_review_count, avg_nightly_rate_with_fees, total_price,
total_strikeout_price, checkin_date, checkout_date, currency`, plus the top-level
`occupants` and `data` keys.

## 4. Ingest + render

```bash
python3 deals/latitude43_deals.py ingest 'deals/raw/<city>_*.json' --city "<City>"
python3 deals/build_email_report.py --city "<City>" --checkin-from <first-checkin> \
    --out deals/out/<city>_email.html
```

For a brand-new city the catalog auto-creates and hotels are added with
`_needs_review` (areas derive from coordinates) — that is expected; the email
still renders cleanly from name/star/rating/discount/nightly.

## 5. Deliver

Send the rendered file with `SendUserFile` (status `normal`). In one or two lines,
note the city, how many weeks and hotels are on sale, and the standout deal.
Mention that photography is placeholder dark-luxury stock to be swapped for real
imagery, and that figures guide *when* to book rather than quote a price.

## Notes

- The email design is the founder-approved cinematic×lookbook hybrid; do not
  redesign it here — just run it. Tuning lives in `deals/build_email_report.py`.
- Don't commit/push unless the user asks. The artifact is the deliverable.
- If a city returns almost no deals, say so plainly rather than padding.
