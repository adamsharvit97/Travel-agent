---
name: business-travel-research
description: Research a destination in depth for business travel and produce a polished, in-depth report — best business hotels by tier, neighborhoods where business travelers stay, conference and convention venues, airport/transport logistics, meeting-friendly dining, connectivity, etiquette, and concrete booking recommendations with live prices. Use when the user asks to research a city for a business trip, find business hotels, prepare for a conference trip, or wants a business travel guide/report for a location.
---

# Business Travel Research

Produce a decision-ready report for business travel to one destination. The deliverable is a polished markdown report saved to `research/business-travel/<city-slug>.md` — not a chat summary.

## Step 1: Intake

Required: **destination city**. If the user is present and any of these are missing, ask once (one AskUserQuestion call, max 3 questions); otherwise proceed with the defaults in parentheses:

- Travel dates (none — research seasonally, skip live pricing specifics)
- Purpose: specific conference/event, client meetings, or general (general)
- Hotel budget tier: luxury / upscale / value (cover all three)
- Origin city, for flight options (skip flights)
- Loyalty programs, e.g. Marriott/Hilton/Hyatt (note all major chains)

Never block on intake when running autonomously — state assumptions in the report header instead.

## Step 2: Research fan-out

Run parallel research agents (Explore or general-purpose with WebSearch/WebFetch) — one per track, all at once. Tracks and the questions each must answer are in [RESEARCH_TRACKS.md](RESEARCH_TRACKS.md):

1. **Business geography** — business districts, where business travelers actually stay, areas to avoid
2. **Hotels** — best business hotels per tier, with evidence (renovations, club lounges, meeting facilities, reviews from business travelers)
3. **Venues & events** — convention centers, major conference hotels, citywide events that spike prices
4. **Logistics** — airports, transfer options/times/costs, getting around, visa & entry
5. **Working & entertaining** — client-dinner restaurants, breakfast-meeting spots, coworking/day offices, connectivity (eSIM, wifi reliability)
6. **Ground truth** — safety, business etiquette, tipping, power plugs, payments, time-zone/jet-lag notes

Require sources from the last 18 months for anything that changes (prices, renovations, openings/closures). Cross-check hotel claims against at least two sources.

## Step 3: Live booking data

If the `mcp__Expedia__search_hotels` tool is available (load via ToolSearch):

- Search the destination with `property_themes: ["BUSINESS_FRIENDLY"]`, real dates if known (else defaults), `star_ratings: [4, 5]` for the upscale/luxury tiers and a second call without it for value
- Run a `show_output_on_map: true` search near the convention center or primary business district when the trip is conference-driven
- Record live nightly rates in the report next to each recommended hotel

If origin and dates are known and `mcp__Expedia__search_flights` is available, pull 2–3 sensible flight options (nonstop preferred, business-hours arrivals).

If Expedia tools are unavailable, note rates as "indicative, from web research" — never invent live prices.

## Step 4: Write the report

Follow [REPORT_TEMPLATE.md](REPORT_TEMPLATE.md) exactly for structure. Standards:

- Every hotel recommendation gets a verdict: who it's for, one concrete reason, walking/transit distance to the relevant business area
- Name **specific picks**: Best overall, Best value, Best for the convention center, Best for long stays
- Tables for comparisons (hotels, transfer options); prose for judgment calls
- Cite sources inline as links; date-stamp the report and the price data
- No filler ("vibrant city", "something for everyone") — every sentence should help someone book or plan

Save the report, then give the user a 5-line executive summary in chat with the file path, and send the file with SendUserFile.

## Quality bar

Before finishing, verify: all six research tracks appear in the report; at least 6 hotels compared across tiers; the four "Best for" picks are named; transfer table has times and costs; every time-sensitive claim has a dated source.
