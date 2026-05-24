# 10 — Capital, Runway & Exit (v3.0 Lens)

**Evaluator framing:** Pre-revenue capital evaluator. McKinsey-trained operator. The founder has a primary income from Renmac that covers personal burn for the first 18–24 months. The plan calls for $0 outside capital. The business is sized to throw off $400K–$800K of personal income by Y5 in the base case, not to clear a venture hurdle. This memo evaluates whether that capital posture is achievable, what the realistic Y1 burn actually is, and what the seven-year outcome distribution looks like under v3.0 economics.

**Verdict up front:** **B**. The capital plan is internally consistent with the lifestyle framing, and the Renmac backstop genuinely removes the Y1 personal-burn risk that would have been fatal under any other framing. But the plan understates true Y1 cash-out by roughly an order of magnitude — the $4–6K/yr operating cost line in §14.2 omits the PHT VA ($36–60K/yr), insurance, software at scale, marketing, contractor labor, and accounting. The realistic Y1 cash-out is $50–95K, not $4–6K. That is survivable on a Renmac primary income, but it is not "zero capital" — it is "founder-subsidized capital," and the plan should name it as such. The exit distribution in §14.2 (40/25/15/5/15) is approximately right but the dollar amounts behind each bucket are not in the document and need to be. The Renmac dependency is a single point of failure that the plan acknowledges as Risk #10 but does not stress-test in dollars. Fixing those three things is roughly half a working day and produces a plan that survives investor-grade scrutiny — not because it will be raised on, but because the founder will be making decisions against honest numbers.

---

## A. What's right (the capital posture is structurally correct)

### A.1 Zero outside capital is the right answer for this business

A solo professional services business with the unit-economics profile in §5 — 50–70% gross margin, founder time as binding constraint, brand-and-relationship as moat — cannot absorb venture capital without becoming a worse version of itself. A $500K seed at a $3M cap is 17% of the business; at Y5 base case $870K revenue and a 2–4× strategic exit multiple, that 17% is worth $300–600K to the investor against a required $5M return on a seed check. The math does not clear. The founder would lose 17% of equity in exchange for capital she does not need (Renmac covers personal burn) and oversight she does not want (board cadence on a one-person shop).

The plan correctly identifies this in §14.2: *"This is not a venture-backable business. It is a lifestyle practice."* That sentence removes the entire class of bad decisions that a founder with capital-market access would otherwise be tempted to make. The v2.0 evaluation memo spent 4,000 words arguing for the lifestyle framing. v3.0 just declares it. That is the correct level of confidence.

### A.2 The Renmac backstop is the load-bearing fact

The single fact that makes the $0 outside capital posture work is the Renmac primary income. The v2.0 evaluation memo had to model "founder personal capital required $130K–$180K over 24 months." The v3.0 plan says: *"Holds primary income from Renmac (research) that fully covers personal burn. Latitude 43 is supplemental income for the first 18–24 months."* That changes the analysis entirely.

The cash gap that would otherwise need to be plugged by personal savings or F&F debt is, in v3.0, plugged by a separate paycheck. The founder can take a $0 draw from Latitude through all of Y1 and most of Y2, run the business as a parallel-track operation, and let revenue compound without the panic of cash-out at month 9. This is structurally cleaner than any financing path I evaluated in v2.0. **The Renmac job is, functionally, a 24-month interest-free loan to Latitude 43 with no equity dilution and no reporting cadence.** No outside investor offers that.

### A.3 The founder draw schedule (Y1 $0 / Y2 conditional / Y3+ real) is correct

The draw schedule in §14.2 (Y1 $0, Y2 only if revenue justifies, Y3+ real) matches the unit-economics curve in §6 (Y1 $115K, Y2 $222K, Y3 $467K, Y4 $740K, Y5 $870K). The Ontario CCPC structure lets the founder accumulate retained earnings at the small business deduction rate (~12.2% on the first $500K of active business income) for the first two years, then begin paying eligible or non-eligible dividends starting Y3. Holding the draw at zero for 24 months is not just financially conservative — it is **tax-optimal**, because corporate-retained earnings compound faster than personally-taxed dividends. The plan should say this explicitly. **The Y1 $0 draw is not a sacrifice; it is the right tax decision.**

### A.4 The lifestyle ceiling is honestly priced

The plan does not pretend the business is something other than what it is. §14.2 explicitly says:

> "7-year outcome distribution roughly: 40% lifestyle (carries founder, no exit), 25% acqui-hire by a larger advisor, 15% strategic acquisition by a host or platform, 5% venture-shaped breakout, 15% failure / wind-down."

This is approximately the same distribution I derived in the v2.0 evaluation memo from first principles (35/22/13/5/25 in v2.0; 40/25/15/5/15 in v3.0). The shift from 25% failure to 15% failure between v2.0 and v3.0 is justified by the Renmac backstop — the dominant Y1 failure mode in v2.0 was "founder runs out of cash," and that mode is removed when personal burn is covered by a separate paycheck. The remaining 15% failure modes are anchor churn at month 18, founder burnout, or external shock (recession, platform shift). Those are real but smaller.

### A.5 The CCPC structure is the right corporate vessel

Latitude 43 Inc. as an Ontario CCPC is the correct structure for this business. The advantages stack: 12.2% combined corporate tax on first $500K of active business income (vs ~26.5% general rate); LCGE of $1,016,836 (2024) on disposition of QSBC shares; W-8BEN-E US treaty position blocking 30% withholding; future income-splitting and holdco optionality. One missing line in the plan: **the LCGE is the single largest tax-advantaged event available to the founder on exit.** That should be named in §14 so it doesn't get accidentally forfeited by structural choices (issuing the wrong share class, premature holdco transfers, failing the 24-month QSBC asset test).

### A.6 The 7-year outcome distribution lines up with the comparable benchmarks

The plan's outcome distribution maps reasonably onto observable benchmarks: **Cadence Travel** took roughly 8 years to reach $5M ARR, founder-led, no meaningful outside capital — the lifestyle-compound path. **Indagare** took roughly 15 years to scale to a multi-advisor firm with $20M+ GBV, with modest capital deployed into content and trip-design products Latitude has not built. **Bell & Bly Travel** may raise; if they execute, the "competitor consolidates" exit becomes more likely for Latitude. **SmartFlyer** built to ~$1B GBV over 15+ years with no outside capital — the boutique-compound ceiling.

Against those reference points, the 7-year exit distribution in §14.2 is well-calibrated. It is neither falsely optimistic nor falsely pessimistic.

---

## B. What's questionable (the burn line is off by 10×, and Renmac dependency is undermodeled)

### B.1 The $4–6K Y1 burn line in §14.2 is wrong

This is the single largest analytic error in v3.0. §14.2 says:

> "Year 1 burn: Fora monthly fee + tools (Stripe, Apollo, Smartlead, Notion, Substack, Honeybook) ≈ $4–6K/yr operating"

That number reflects only the software stack. It omits every other operating cost. A realistic Y1 cash-out, line by line:

| Y1 cost item | Low | Mid | High | Notes |
|---|---:|---:|---:|---|
| Fora host fees | $1,800 | $2,400 | $3,000 | $150–250/mo |
| Software stack (Stripe fees, Apollo, Smartlead, Notion, Substack, Honeybook, scheduling, accounting, CRM) | $3,000 | $5,000 | $8,000 | The §14.2 line, isolated |
| **PHT VA from month 4–6 (the omitted line)** | **$18,000** | **$30,000** | **$45,000** | $1,500–$2,500/mo × 6–8 months in Y1, single VA; doubles to $36–60K full year |
| E&O insurance, general liability, cyber | $3,000 | $5,000 | $8,000 | E&O is mandatory for travel advisors; cyber once carrying PII |
| Networking ($15–20K per §10.1) | $15,000 | $18,000 | $20,000 | Soho House + EO + dinners |
| Cold email spend (Apollo seats, Smartlead inbox warming, list buys) | $3,000 | $5,000 | $9,000 | Above the basic software line |
| Marketing (LinkedIn ads, sponsored placements, photography) | $2,000 | $5,000 | $12,000 | Plan says "no paid social Y1" but newsletter growth costs money in practice |
| Contractor labor (editor for the Journal, designer, occasional VA outside PHT) | $4,000 | $10,000 | $18,000 | The 43rd Parallel monthly + Desk Diary 2x/week implies editorial support |
| Legal, accounting, corporate setup (Ontario CCPC, US contracting templates, MSA, privacy policy, TOS) | $4,000 | $7,000 | $12,000 | One-time-ish, weighted to Y1 |
| Travel costs (founder client visits, one FAM trip, conference attendance) | $3,000 | $7,000 | $15,000 | Society principals expect in-person eventually |
| Contingency (10%) | $5,680 | $9,440 | $15,000 | Y1 line items always come in over |
| **Total Y1 cash-out** | **$62,480** | **$103,840** | **$165,000** | |

Round to **$60–105K Y1 cash-out at the lean-to-mid case, $165K at the maximalist case**. Even excluding the PHT VA (the largest single line and the most contested), the floor is $35–60K — still an order of magnitude above the $4–6K stated in §14.2.

This is a documentation problem, not a strategic problem. The Renmac primary income covers founder personal burn ($80–120K Toronto), and Y1 revenue of $60–115K can cover most of the operating cash-out by Q4 if the cash-collection timing works. But the plan should be honest about the actual cash flow through the business. An investor — even an F&F lender — reading §14.2 will spot this in two minutes and lose trust in the rest of the financial discipline.

### B.2 The PHT VA cost is the load-bearing omission

The v3.0 short-eval flagged this (Lens 4): *"That single line item changes the burn profile materially."* I want to put a sharper number on it.

The plan's SLA in §8.1:
- **Founder coverage:** 7am–11pm ET, 16 hours/day, 7 days/week
- **PHT VA coverage:** 11pm–7am ET, 8 hours/day, 7 days/week
- **60-minute SLA on all member inquiries, 24/7**

For PHT VA coverage at 8 hours/day × 7 days = **56 hours/week**. A single PHT VA at 40 hours/week cannot cover this. The plan implicitly requires either:
- Two part-time PHT VAs (each ~28 hours/week), or
- One full-time PHT VA + founder coverage on PHT-off-shift weekends, or
- A reduced SLA on the overnight window

PHT VA rates for travel-experienced contractors are $8–15/hr loaded. At 56 hours/week × 52 weeks × $10/hr blended = **$29,000/yr at a minimum, $40,000–$50,000/yr realistically once you factor in management time, training, US-supplier portal access, and overlap windows for handoff**. The v3.0 short-eval put the range at $36–60K/yr. I think that range is right for a steady-state Y2 onward, with a partial-year Y1 cost of $18–35K depending on hire date.

This omission from §14.2 is the single most important fix the plan needs. The fact that Renmac primary income covers the founder's personal burn does not extend to covering business operating expenses. The PHT VA gets paid by the business, not by the founder's day job.

The downstream impact on the financial model:
- Y1 burn corrected: **$80–105K, not $4–6K**.
- Y1 revenue: **$60–115K** (depending on whether you use the plan's $115K or the v3 short-eval's honest $60–80K planning case).
- Y1 cash flow: **breakeven to mildly negative** in the optimistic case, **-$20–45K** in the planning case.
- That negative gap, even at the planning case, **must be funded from founder savings or retained earnings from the prior tax year of Renmac income**.

This is still survivable. It is not "zero capital." Call it what it is: **$20–45K of founder-subsidized working capital in Y1, recoverable from operating cash flow in Y2.**

### B.3 The Renmac dependency is mentioned but not stress-tested

Risk #10 in §12:
> "Founder primary income falls (Renmac, other). Medium probability, medium severity. Y1 plan assumes Latitude is supplemental; not sized to replace primary income until Y3+."

This is the single most important risk in the business and it gets one row. The plan does not specify:

- **What happens to Latitude if Renmac ends in Y1 (month 4, month 9, month 12)?**
- **What happens if Renmac ends in Y2 at a $150K Latitude run-rate?**
- **What is the Latitude revenue threshold at which the founder could survive on Latitude alone in Toronto?**
- **What is the contingency plan: pause new marketing spend, draw down savings, hire a co-founder, accelerate the F&F bridge, take a partial Renmac engagement?**

Let me work through the Toronto sole-income math. A Toronto-based founder with no dependents at a moderate level of austerity (rent ~$2,500–3,500, food $800–1,200, healthcare top-ups $200–400, transit $150, phone $100, modest social $500–1,000, savings/RRSP $1,500–3,000, retirement long-tail $1,000) has a monthly personal burn of $6,250–$10,150, call it **$8,000/mo, $96K/yr**. After Ontario CCPC dividend tax (~25% blended on non-eligible dividends at this income level), the founder needs **~$128K/yr in gross corporate dividends, or ~$135K/yr in salary** to net $96K personally.

That gross-to-net math means the Latitude revenue threshold for sole-income survival is approximately:
- **$135K/yr in personal compensation** required to net $96K of personal burn.
- Add ~$50–100K/yr in business operating costs (PHT VA, software, insurance, networking, marketing, contractor) that must come from revenue before any draw.
- **Total revenue threshold: $185–235K/yr** to support a founder sole-income lifestyle plus business operations.

Cross-reference to the v3.0 revenue model: that threshold is hit **mid-Y2** in the base case ($222K) and **early-Y3** in the bear case. Until then, the business cannot stand on its own without primary-income support.

**If Renmac ends in Y2 at a $150K Latitude run-rate**, the founder has three options:
1. **Stretch the runway with savings:** If personal savings can cover 6–12 months of the gap (~$50–100K), bridge to Y3 when Latitude crosses the threshold.
2. **Take a transitional consulting income:** A 1–2 day/week consulting gig at $100–200/hr produces $50–100K/yr at modest founder-time cost. This is the right answer for most founders.
3. **Accelerate Latitude growth via F&F debt:** $100–150K of F&F debt at 6% interest gives 12 months of runway against the gap. This is the wrong answer if the underlying member-acquisition rate hasn't proven out; right answer if it has.

**The plan should specify which of these three is the contingency.** Without a written contingency, the founder is making a 24-month bet on Renmac without a fallback plan.

### B.4 Cash flow timing is undermodeled

The plan treats Y1 revenue as a single annual number ($115K). The reality is monthly:

- **Subscription cash:** Charged monthly via Stripe on the first of each month. Stripe payouts arrive in 2–7 days. This is the cleanest, most predictable cash line.
- **Fora commission cash:** Supplier pays Fora 30–60 days after the trip is completed; Fora reconciles and pays the advisor on a monthly cadence with a 30-day lag. **Total: 60–90 days from trip date to advisor's bank account.**
- **Design fees (non-member):** Paid in full before design begins (per §2.4). This is cash-positive but episodic.
- **Society launch (H2 2027):** Annual prepay for the subscription portion is common at this tier. If Society launches in H2 of Y2 with 1 member at $14K average, that's $14K of cash-in but $14K of deferred-revenue liability on the balance sheet.

A realistic Y1 monthly cash-in curve, against the plan's 22 Light + 8 Office Y1 close target (assuming the plan's optimistic case):

| Quarter | Cumulative members | Q-end subscription MRR | Cumulative subscription cash | Commission cash arriving (60–90 day lag) | **Cumulative cash in** |
|---|---:|---:|---:|---:|---:|
| Q1 | 3 (2 Light + 1 Office) | $727 | $1,500 | $0 | $1,500 |
| Q2 | 9 (7 Light + 2 Office) | $2,021 | $7,500 | $200 (Q1 trips, lagged) | $7,700 |
| Q3 | 18 (13 Light + 5 Office) | $4,202 | $18,000 | $2,500 | $20,500 |
| Q4 | 30 (22 Light + 8 Office) | $6,950 | $34,000 | $8,500 | $42,500 |
| End Y1 (collected) | 30 | — | — | — | **~$80K** (includes design fees + Y1 commission tail collecting into Q1 of Y2) |

Against this collection curve, the operating cash-out of ~$80–105K is **front-loaded** (insurance, legal, software annual contracts, networking dues paid Q1) and **fixed-monthly** (PHT VA from month 6, software subscriptions). Realistic operating cash-out monthly profile:

| Quarter | Cash out |
|---|---:|
| Q1 | $25,000 (front-loaded one-times + setup) |
| Q2 | $15,000 |
| Q3 | $25,000 (PHT VA starts month 6) |
| Q4 | $20,000 |
| **Total Y1 cash-out** | **$85,000** |

Cumulative cash gap by quarter:
- End Q1: -$23,500
- End Q2: -$30,800
- End Q3: -$35,300
- End Q4: -$42,500 (improving to -$30K once Q4 commissions collect into Q1 of Y2)

**The cumulative Y1 cash gap is $30–45K at year-end, all of which must be funded by the founder.** This is the working-capital number the plan needs to name. It is much smaller than the v2.0 evaluation's $80–120K gap (because of the Renmac backstop removing personal-burn-from-business-cash), but it is not zero.

### B.5 Working capital needs are undiscussed

The plan does not address three working-capital realities that bite for travel advisors specifically:

**1. Airfare on advisor credit card.** Many premium air bookings (especially international business class with consolidator fares) require the advisor to put the ticket on their own card and re-bill the member. The advisor carries the float for 7–30 days depending on member payment terms. At an average $5K/ticket and 5 tickets/month outstanding, the founder needs **$25K of available credit** as routine working capital. A $25K business credit card is achievable in Y1 but requires personal guarantee until the business has trade credit history.

**2. Hotel pre-pay deposits.** Group bookings, Belmond properties, and some independent hotels require 25–50% pre-pay 30–60 days before stay. Member typically reimburses the advisor on receipt of the booking confirmation but there are 1–4 weeks of float in between. Society members may book $20K+ trips; a single pre-pay deposit can be $5–10K of working capital.

**3. Supplier deposit cycles.** Some preferred-partner programs (Virtuoso, FSPP) charge annual or quarterly access fees. Fora is paying these on the advisor's behalf as part of the hosting structure, so the founder is mostly insulated. But the plan should confirm in writing which fees Fora absorbs and which pass through.

**Recommendation:** the plan should specify a working-capital line of **$25–50K** as either (a) personal-savings reserve held outside the business for cash-call events, or (b) a business credit card with personal guarantee. This is separate from the Y1 cash gap and does not get spent — it sits there to absorb timing mismatches.

### B.6 The "Renmac as 24-month bridge" framing is undocumented

I argued in §A.2 that the Renmac primary income is, functionally, a 24-month interest-free loan to the business. The plan does not name this framing. It should, for three reasons: (1) **decision discipline** — naming the Renmac contribution as finite-duration forces the founder to plan against the day it ends; (2) **personal tax planning** — Renmac is high-marginal-rate personal income that should be aggressively sheltered (RRSP, TFSA, FHSA) while it lasts, against the low-marginal-rate retained earnings inside the CCPC; (3) **spousal alignment** — if the founder marries, the household should plan against the Renmac income ending, not against it continuing.

---

## C. What's wrong or missing (exit math needs detail; LCGE is unflagged)

### C.1 The exit distribution is named but the dollars behind it are not

§14.2 says: *"40% lifestyle, 25% acqui-hire, 15% strategic, 5% venture-shaped, 15% failure."* The plan does not say what dollar outcome corresponds to each bucket. That gap matters because the founder needs to make planning decisions against expected exit value, not just probability bucket names. Let me work the numbers and the plan should incorporate them.

**Bucket 1 — Lifestyle (40%).** No exit; founder runs the business 10–20 years. Y5 personal income $400–800K; Y10 personal income $700K–$1.5M under a Cadence-trajectory compound assumption. Cumulative Y1–Y10 founder cash, PV-discounted at 6%: **$3.5–5.5M**. Dominant EV contributor.

**Bucket 2 — Acqui-hire by larger advisor (25%).** Brownell, Tzell, Internova, or similar. 2–4× revenue multiple (typical for boutique advisory books with strong renewal). Y5 revenue base ~$870K → $1.7–3.5M gross. Founder net after tax with LCGE: **$1.3–2.8M**. Typical structure: 30–50% cash at close, 50–70% earnout against 2–3 year retention.

**Bucket 3 — Strategic acquisition by host or platform (15%).** Fora is the primary candidate; private aviation broker is the secondary. 3–6× revenue multiple (higher because the buyer values strategic adjacency, not just book). Y5 revenue ~$870K → $2.6–5.2M gross. Founder net after tax with LCGE: **$2–4.5M**. Heavier on cash, lighter on earnout — the strategic is buying capability.

**Bucket 4 — Venture-shaped breakout (5%).** Latitude scales beyond solo to a multi-advisor firm with $3–5M ARR by Y7. Requires hiring 3–5 advisors and a real operations layer by Y4–Y5. 4–6× multiple at this scale → **$12–30M gross, midpoint $20M**. Founder net after tax with LCGE: **$10–22M**. Single largest contributor to upside variance.

**Bucket 5 — Failure / wind-down (15%).** Founder shuts down or sells the book for asset value $50–200K. Recoverable: brand, member list, supplier relationships. Founder net: -$50K to +$100K.

**Probability-weighted expected founder outcome (7-year horizon):**

| Bucket | P | Founder net (midpoint) | EV |
|---|---:|---:|---:|
| Lifestyle (10-yr cumulative PV-discounted personal income) | 40% | $4,500,000 | $1,800,000 |
| Acqui-hire | 25% | $2,000,000 | $500,000 |
| Strategic acquisition | 15% | $3,250,000 | $487,500 |
| Venture-shaped breakout | 5% | $16,000,000 | $800,000 |
| Failure | 15% | $25,000 | $3,750 |
| **EV (founder net)** | **100%** | | **~$3.6M** |

**Probability-weighted founder outcome: ~$3.6M over 7–10 years.** This is approximately the same number I derived in the v2.0 evaluation memo ($3.88M). It is the right number for the founder to plan against. It is not in the document.

### C.2 The LCGE is the biggest unflagged tax efficiency

The Lifetime Capital Gains Exemption shelters the first **$1,016,836** (2024 indexed) of capital gains on disposition of QSBC shares from tax. For a founder selling the business at Y5 for $2–3M:

- Pre-LCGE: $2–3M gain × ~26.76% Ontario marginal capital gains tax = **$535K–$800K of tax**
- With LCGE: First $1.01M tax-free, remaining $1–2M × 26.76% = **$265–535K of tax**
- **Tax savings from LCGE: $270–270K**

For a single founder, LCGE is the most consequential tax decision in the business. To preserve LCGE eligibility:
- Shares must be **QSBC shares at the time of sale** (24-month asset test: 50% of corporate assets used in active business in Canada throughout 24 months prior to sale; 90% test at moment of sale).
- Shares must be **owned by the disposing individual for 24 months prior** (no recent share-issuance shenanigans).
- Founder must be **resident in Canada** at time of sale.

This means specific decisions need to be made early:
- **Do not issue shares to a holdco before the QSBC clock has been running long enough** — selling holdco shares does not qualify for LCGE the same way (though there are crystallization techniques).
- **Avoid passive income accumulation in the operating company** in the years before sale. Investment income above $50K/yr reduces the small business deduction and can disqualify QSBC status.
- **Get a Canadian tax lawyer involved by Y3** to plan the disposition structure. A pre-sale "purification" reorganization can be needed if passive assets have accumulated.

The plan says none of this. It should. Even one line in §14.2 — *"On exit, LCGE shelters the first $1M+ of capital gains if QSBC structure is maintained throughout."* — flags it for the founder's accountant.

### C.3 The "wedding gift" exit is real and unaddressed

The brief raises the possibility that the founder marries into capital, at which point the business becomes a hobby and the financial pressure releases. This is not a frivolous scenario. It is a real exit path with real probability for a founder in this demographic and this geography.

The decision implications:
- If the spouse-as-capital path materializes, the right answer is **not** to wind down Latitude. The right answer is to reduce founder draws to $0 indefinitely, let the CCPC compound retained earnings at 12.2%, and run the business at a steady 30–40 member cap for 5–10 years until a strategic acquirer offer arrives or the founder decides to exit on her own timeline.
- The "wedding gift" exit is, in tax terms, **not an exit at all** — the business keeps running, the founder gets non-business income elsewhere, and the eventual disposition happens at the time of the founder's choosing under optimal LCGE conditions.
- The plan should acknowledge this scenario in §14 alongside the other exit paths. Not because it's planned for, but because the operating model should not preclude it.

### C.4 When to start optimizing for exit vs. cash flow

The plan doesn't address the multi-year planning question: **at what point does the founder pivot from "compound the business" to "groom for sale"?**

The two modes are operationally different:
- **Compound mode:** Maximize retained earnings, hire selectively, take small founder draws, reinvest in member acquisition. Member book is sticky but founder-bound. Optimal for Y1–Y4.
- **Groom-for-sale mode:** De-risk founder dependency, document everything, hire a second advisor who can carry 50% of relationships, build a clean accounting trail for due diligence, freeze pricing changes for 12 months pre-sale, sign multi-year agreements with key members. Optimal for Y5–Y7 if exit is on the table.

The transition cost between modes is roughly 12–18 months. A founder who decides in Y6 that she wants to sell in Y7 is too late — the buyer will discount the offer because the business is still founder-bound.

**Recommendation:** the plan should specify a **decision checkpoint at end of Y3** (revenue ~$467K, member book ~80 active accounts). At that point the founder reviews:
- Is the business compounding faster than the founder can deliver? → Hire and pivot toward groom-for-sale.
- Is the business at a stable plateau that the founder can run forever? → Stay in compound mode indefinitely.
- Is the Renmac primary income still durable? → Continue building retained earnings tax-advantaged.
- Has a strategic conversation become real? → Open the optionality book formally.

Without a defined decision checkpoint, the founder will drift through Y4–Y5 without making the explicit "compound or groom" choice, and Y6–Y7 will be a forced decision in less favorable conditions.

---

## D. Recommendations (10, prioritized)

1. **Correct the Y1 burn line in §14.2.** The $4–6K/yr operating cost is wrong. Replace with: *"Y1 operating burn: $80–105K (PHT VA $30K, software stack $5K, insurance $5K, networking $18K, marketing $5K, contractor labor $10K, legal/accounting $7K, travel $7K, contingency $9K). Funded by Y1 revenue ($60–115K) plus $20–45K of founder working-capital subsidy from Renmac retained income. Recoverable in Y2."*

2. **Add a line for the PHT VA staffing model.** Specify in §8.1 whether overnight coverage is one VA or two, what the loaded cost is ($30–50K/yr), and what the Y1 hire date is. Reduce ambiguity for the operating reader.

3. **Stress-test Risk #10 (Renmac primary income falls).** Add a paragraph to §12 or §14 specifying: (a) the Latitude revenue threshold for sole-income survival in Toronto ($185–235K/yr), (b) the contingency hierarchy (savings bridge first, consulting income second, F&F debt third), (c) the specific revenue level at which Latitude can stand alone (mid-Y2 base case, early-Y3 bear case).

4. **Name the LCGE in §14.2.** One line. *"Exit shelter: Lifetime Capital Gains Exemption (~$1.02M as of 2024, indexed) shelters QSBC capital gains on sale. Preserve QSBC structure throughout — avoid passive asset accumulation, no premature holdco transfers, get Canadian tax counsel by Y3."*

5. **Specify the working-capital reserve.** Add to §14.2: *"Working capital reserve of $25–50K maintained in business credit availability or personal-savings buffer to absorb airfare float, hotel pre-pay deposits, and supplier deposit cycles. Not spent; held for timing mismatches."*

6. **Quantify the exit distribution in dollars.** Replace the §14.2 outcome distribution with a table showing probability × founder-net-midpoint × EV contribution, totaling to a probability-weighted founder outcome (~$3.6M over 7 years). This is the number the founder should plan against, not the unlabeled buckets.

7. **Add a Y3 decision checkpoint to the plan.** A new §14.3 or §15 paragraph: *"End of Y3 (revenue ~$467K, ~80 active members) is the decision checkpoint between compound mode and groom-for-sale mode. Compound continues current operating posture indefinitely. Groom requires hiring a second advisor and beginning a 24-month de-risking program. Defer the choice until evidence supports it; force the choice no later than end of Y3."*

8. **Address the "wedding gift" exit scenario.** Add to §14 or the risk register: *"In the event of changed household economics (spouse income, inheritance, life event), the optimal response is reduced founder draw and indefinite hold under CCPC retained-earnings structure, not wind-down. The business is designed to be optional, not obligatory."*

9. **Build a 24-month monthly cash flow forecast separate from the annual revenue model.** Y1 cash flow is dominated by timing — Q1 expenses front-loaded, Q4 commissions collecting into Q1 of Y2, PHT VA hire in Q3. An annual view hides this entirely. The monthly view exposes the $30–45K cumulative Y1 cash gap that the founder must plan to fund.

10. **Pre-qualify F&F debt now.** Even though Renmac covers the cash gap in the base case, the bear case (Renmac ends in Y2) requires a bridge. Have 3–5 conversations with potential F&F lenders **before** they're needed, at a pace of "not asking yet, but want to know if it's possible." Have $100–200K of soft-committed debt available. Do not draw it unless triggered. The worst time to raise F&F money is when it's needed.

---

## E. Closing

The v3.0 business plan gets the capital posture structurally right: zero outside capital, Renmac primary income as the bridge, CCPC for tax efficiency, lifestyle framing for honest sizing. The probability-weighted founder outcome of ~$3.6M over 7 years is a strong result for a Toronto solo founder running a parallel-track services business with $0 in outside investment.

What the plan needs is honest financial discipline on the operating-cost line. The $4–6K Y1 burn figure in §14.2 is an order of magnitude understatement, and the gap is dominated by one line item — the PHT VA — that is named operationally in §8.1 but absent from the financial section. Correct that, name the LCGE, stress-test the Renmac dependency in dollars, and the plan becomes investor-grade in the only sense that matters: the founder making decisions against numbers that survive contact with reality.

The Renmac job is the single biggest piece of capital structure in this business and the plan should name it as such. Functionally, it is an interest-free, equity-free, board-free 24-month bridge with no reporting cadence and no acceleration clause. No outside investor offers terms that good. The founder should use the bridge with discipline, plan for the day it ends, and let the business compound under the CCPC umbrella until either a strategic opportunity emerges or the founder decides on her own timeline that the cash-flow ceiling is the right place to stop. Either outcome is a good life. Both are achievable from the v3.0 plan as written, with the financial-discipline corrections named above.

— Capital, runway & exit evaluator
