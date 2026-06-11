# Example: a filled seller profile

A fictional fractional-CFO firm, to show the level of specificity that makes briefs sharp. Vague entries produce vague briefs.

---

## Company
- **Name:** Meridian CFO Partners
- **Tagline:** Fractional CFOs for founder-led companies, $2M–$30M revenue
- **Website:** meridiancfo.example
- **Location:** Chicago

## Brand
- **Primary color:** `#13294B`
- **Accent color:** `#9A7B2D`
- **Footer line:** Meridian CFO Partners · Fractional finance leadership for founder-led companies

## Sender
- **Name:** Jordan Avery — **Email:** javery@meridiancfo.example — **Phone:** +1 312 555 0148

## The offer
We place a senior CFO into founder-led companies two days a week. The pitch in one sentence: "A real CFO, two days a week, for a third of the cost of a bad full-time hire."

| Product / tier | Price | Who it's for | What's included |
|---|---|---|---|
| Embedded CFO | $8,500/mo | $5M–$30M revenue, raising or scaling | 2 days/week, board pack, 13-week cash model, fundraise support |
| Finance Foundation | $3,900/mo | $2M–$5M revenue | Monthly close, KPI dashboard, quarterly forecast |

## Audience types

### Founder / CEO, $2M–$30M revenue
- **Pain:** flying blind between board meetings; the bookkeeper can't model anything forward.
- **Recommended tier:** Foundation under $5M; Embedded above or when raising.
- **Triggers:** a raise announced, a controller departure, a missed-forecast post, acquisition rumors.

### PE operating partner
- **Pain:** portfolio companies with founder-grade finance functions post-acquisition.
- **Recommended tier:** Embedded, multi-company.
- **Triggers:** new platform acquisition, add-on activity, CFO turnover in the portfolio.

## Voice rules
- **Do:** short sentences; numbers with units ("13-week cash model", "$8,500 a month"); name the deliverable, not the value cloud.
- **Don't:** no exclamation marks; never "passionate", "holistic", "trusted advisor", "reach out", "circle back".
- **The test:** sounds like a board memo, not a marketing email.

## Objection bank
- **"My bookkeeper handles this."** → A bookkeeper records the past. A CFO prices the future. The question is who builds the model your board sees next quarter.
- **"Why not hire full-time?"** → At your stage a full-time CFO is $300K+ and underutilized three days a week. Two embedded days covers the board cycle. When you outgrow us, we help hire our replacement — that's in the engagement letter.
- **"We tried fractional and it didn't stick."** → Usually that's a junior controller sold as a CFO. Ask the last one who presented to the board. Ours do, every quarter, and you can call two references first.

## Cadence rules
- **First touch:** Tuesday–Thursday, 8:30–10:00 a.m. prospect-local.
- **Follow-up:** +5 business days, one paragraph, a single specific observation about their company — no second pitch.
- **Stop rule:** two touches, then park unless a trigger fires.

## Anti-pitch notes
No discounting on the first call. No free "audits". No proposals before a 30-minute diagnostic.

## Compliance constraints
None.

---

# Example render run

```bash
python3 scripts/build_brief.py input.json -o Jane_Doe_brief.html
```

where `input.json` carries the `seller` block built from the profile above and the `brief` block from the analysis. Open the HTML in any browser; print to PDF.
