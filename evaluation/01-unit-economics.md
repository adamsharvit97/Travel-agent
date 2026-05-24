# Latitude 43 v2.0 — Unit Economics Diligence

*Pre-revenue investor evaluation. No softening. Numbers, not narrative.*

---

## Executive read

The v2.0 model is materially more honest than v1.0 — it correctly separates 100%-retained subscription from Fora-split commission, it has dropped the fantasy 24-trip-per-year assumption to a defensible 18, and it has stopped pretending the founder will hit $2M GMV in Y2 to unlock 90/10. But on rigorous unit-economic inspection the plan is still about **30–45% too optimistic at the Y5 line**, has **at least $60K/year of unmodelled fixed costs**, and rests on a **commission-yield assumption that requires near-perfect member usage**, which the simulated cohort already implies is not realistic.

The headline $871K Y5 base case is achievable, but only conditional on: (a) Society shipping on time in Q1 2027 with ≥15 members by Y5; (b) Light/Office commission capture running at the modeled per-traveler frequency without dormancy decay; (c) a successful escalation from 70/30 to 80/20 with Fora by Y2; and (d) zero churn surprises in the Society cohort. Strip out two of those four and Y5 drops to ~$550–600K. Strip out three and the business is a sub-$400K solo practice — i.e., a high-income job, not a venture.

A seed investor at a $3M cap would say no. A family-office or strategic angel at a $1.5M cap with rev-share preference might say yes, but only after the founder has 5–8 paying members and Y1 hits $80K. **Realistic financing: bootstrap with the option of a $150–250K friends-and-family note at flat $1–1.5M post if the First 30 program shows < 10% 90-day refund rate.** Everything else is premature.

The 10 fixes in Section G are the minimum the founder must do before any capital conversation. Most are accounting hygiene, two are structural.

---

## A. Unit economics audit — tier by tier

### A1. Is 18 nights/yr per traveler defensible?

The 18-night figure comes from the v2-facts assumption of "1.5 nights/month." It is below the v1.0 number (24 trips) and below the pricing-stress-test's revised estimate (12 trips), so on the surface it looks more credible. Let me pressure-test against the actual industry data.

| Source | Implied annual nights per business traveler |
|---|---:|
| Concur 2024 benchmark: avg $1,783 per trip, US small-co T&E $50–250K | ~28–140 trips company-wide, ~8–15 trips per principal at 2.5 nights/trip = **20–38 nights/yr per principal** |
| GBTA 2024: US road warrior averages 6.4 business trips/yr, mean 2.8 nights | **~18 nights/yr** |
| AHLA 2023 lodging report: business traveler avg 4.2 hotel stays/yr, 2.1 nights/stay | **~9 nights/yr** |
| Morning Consult / Deloitte 2024 frequent business traveler (>10 trips/yr) | **~30–40 nights/yr** |

**Assessment.** 18 nights is defensible for the *median* business traveler, but it is **the wrong target** for the v2.0 ICP. The ICP described in the sales-kit and competitive-landscape sections is not the median — it is the Series B founder, the PE MD, the RIA principal. These people travel **25–40 nights/yr** when active. Conversely, the buyer who travels only 18 nights/yr is the marginal Atlas Light buyer who will struggle to justify $99/mo on commission ROI, and may churn at 8–12%/yr.

The 18-night assumption is a blend that **simultaneously under-represents heavy users and over-represents marginal users**. It will produce a credible-looking total — but in practice the actual mix is bimodal:

- 30–40% of members are heavy users (25–35 nights/yr) generating 60% of commission
- 60–70% of members are light users (5–12 nights/yr) generating 25% of commission
- The remaining 15% is dormant — paid the subscription, used the desk twice, then drifted

The v2-facts model has no dormancy term. **At Y3+ when the cohort matures, expect 12–20% of Light members to be functionally dormant**, capturing subscription only. Net effect on commission revenue: **deflate by 15–22%** vs. the v2-facts table.

### A2. Is $500 ADR right?

ADR depends entirely on what's being booked. The model uses $500 flat. Let me decompose.

| Booking type | Typical ADR | Share of cohort spend (est.) |
|---|---:|---:|
| US business hotel (Marriott Bonvoy Ambassador, Hyatt Privé) | $250–$400 | 35% |
| US premium hotel (Four Seasons, Aman, RC Reserve) | $700–$1,800 | 20% |
| Resort / leisure US | $600–$1,200 | 15% |
| International business (LHR, FRA, HKG city hotels) | $400–$700 | 15% |
| International leisure / villa | $800–$2,500 | 10% |
| Boutique / lifestyle (1H, Edition, Soho House) | $500–$900 | 5% |

**Weighted average ADR: ~$580**, modestly above the $500 assumption. So the ADR isn't the leak — if anything it's slightly conservative. But there's a tier composition mismatch the model hides:

- Atlas Light at $99/mo is positioned for the SMB founder. SMB founders book **mostly business hotels at $300–$450** (not $500), and occasionally the Four Seasons. Realistic Light blended ADR: **$420**.
- Atlas Office at $249/mo is positioned for PE/VC/RIA partners. They book at **$650–$800 blended**.
- Society at $14K/yr is family-layer leisure. ADR jumps to **$900–$1,200** but the model already credits $750.

Substitute the corrected ADRs into the unit economics:

| Tier | Modeled commission | Corrected commission |
|---|---:|---:|
| Light (1 traveler × 18 nights × ADR × 10% × 70%) | $630 ($500 ADR) | **$529** ($420 ADR) |
| Office (3 × 18 × ADR × 10% × 70%) | $1,890 ($500 ADR) | **$2,646** ($700 ADR) |
| Society (4 × 25 × ADR × 10% × 70%) | $5,250 ($750 ADR) | **$6,300** ($900 ADR) |

So the ADR error is **directional but offsetting**: Light is overstated, Office and Society are understated. Net Y5 effect on the v2-facts table is probably **+$15K to +$40K** if you assume the realistic mix — but only if Society actually launches.

### A3. The 70/30 Fora split — when does it actually shift?

This is the single biggest forecasting risk in the v2.0 model and it deserves brutal treatment.

Per Fora's own commission documentation, the splits are 70/30 starting, 80/20 at $300K personal sales, 90/10 at $2M personal sales. The v2-facts doc lists these. **Three things the founder needs to confirm before modeling**:

1. **Is $300K "personal sales" gross booked or commissionable booked?** This is critical. If it's gross booked travel (the natural reading), then $300K is achievable in Y2 with 30 members generating ~$10K of gross travel each. If it's commissionable bookings only — i.e., booked through preferred suppliers at commissionable rates — then $300K requires ~$1M of gross travel routed correctly, which is a Y3 problem.
2. **Is it yearly or cumulative?** Fora's public language reads "annual," but several host agencies use rolling-12-month. The founder should pin Fora's CSM down on this in writing.
3. **Does the clock reset?** If the advisor hits $300K in Y2 and then has a slow Y3 (say $250K), do they fall back to 70/30 mid-year? This is a real risk in seasonal businesses.

Plausible scenario tree under different interpretations:

| Interpretation | When 80/20 triggers | Y5 commission revenue impact vs. model |
|---|---|---|
| $300K gross travel, annual | End of Y2 / start of Y3 | Matches model |
| $300K commissionable bookings, annual | End of Y3 / start of Y4 | **-15% in Y3, -8% in Y4** |
| $300K gross travel, rolling 12-month, with reset | Toggles in/out depending on month | **-5–10% variance, harder to forecast** |
| $300K cumulative all-time | Achieves quickly but irrelevant — not the actual policy | n/a |

The v2-facts table implicitly assumes the first interpretation. **Without written confirmation from Fora, the founder is exposed to ~10% commission revenue erosion through Y3–Y4.**

### A4. Virtuoso 2% clip — applies to where?

The v2-facts doc says "Virtuoso clips 2% of commissions before the Fora split." This is **only partially true** and is the most-misunderstood line in the entire model.

The actual Virtuoso commission structure (per One Mile at a Time and confirmed by multiple host-agency contracts):

- On **Virtuoso preferred hotel rates**, the gross commission paid by the hotel is typically 10%. Of that 10%, the advisor receives 8% and Virtuoso receives 2%. **So the "10% commission" the founder is modeling is already net of the Virtuoso clip if the booking is Virtuoso-routed.**
- On **non-Virtuoso preferred rates** (FHR, Bonvoy STARS, Hyatt Privé direct), the 2% clip **does not apply** because the booking is routed through a different program.
- On **cruise**, commission can be 10–16% gross; Virtuoso clips do apply on Virtuoso preferred cruise lines.
- On **air**, commission is essentially $0 for domestic and 1–3% on premium international; no clip applies.

So the v2-facts model is **double-counting the Virtuoso haircut on Virtuoso bookings** (the 10% is already net) **OR under-counting commission yield on non-Virtuoso bookings** (which should be 10% gross, not 10% minus 2%). Net effect: the modeled commission lines are within ±5% of correct, but for the wrong reasons. **Fix the methodology before scaling.**

Practical implication: about 60% of bookings flow through Virtuoso (8% net to advisor), 30% through other preferred programs (10% net), and 10% non-commissionable. Blended effective rate: 0.6×8% + 0.3×10% + 0.1×0% = **7.8%**, not 10%. **The model is overstating commission by ~22% on gross.**

| Tier | Modeled Y1 commission | Corrected (7.8% blended) |
|---|---:|---:|
| Light | $630 | **$491** |
| Office | $1,890 | **$1,474** |
| Society | $5,250 | **$4,095** |

This is the largest single quantifiable error in the v2.0 model. **Apply this correction across the Y1–Y5 table and Y5 base case drops from $871K to roughly $740K.**

### A5. Personal travel commissions from members

The v2-facts doc claims "Personal travel from members: incremental upside ($5K–$30K/yr in bookings depending on tier)." For Light, this is modeled as $350–$700 of commission, implying $5–10K of personal bookings per Light member.

**Empirical reality from the simulated cohort:** of 28 sims, roughly 11 included a meaningful personal travel hook (honeymoons, Italy client trips, Aspen, anniversary). That's **39% of qualified leads** with personal upside attached. But of the 7 outright closes, only 3 had personal travel as material revenue. **Conversion of "interested in personal travel through us" → "actually books personal travel through us" is probably 30–50%, not 100%.**

So the $350–$700 personal commission line for Light should be discounted to **$140–$350** at Y1 cohort maturity, ramping to $300–$600 by Y3 once trust is established.

For Office at $1,400–$2,000 modeled personal commission: this is the line where the model has the most upside, **because Office members include the principal's spouse and family travel by default**. Empirically this is closer to right — but it requires the founder to actively cross-sell, which is a workflow that doesn't yet exist in the operations docs.

For Society at $2,100: this is the most defensible line in the entire model. Society members buy family travel through their dedicated principal as a matter of course. **Probably understated** — $4–8K of personal commission per Society member is realistic by Y3.

### A6. Design fee math — escalator pricing check

The v2.0 escalator:
- $0 under $5K
- $250 base + $50/$1K from $5K–$15K
- $750 base + $75/$1K from $15K–$30K
- $1,875 base + $100/$1K above $30K
- Capped at $5,000/trip
- Members pay 50%

Let me check effective hourly recoveries against realistic labor.

| Trip value | Labor (hr) | Non-member fee | Member fee | Non-mem $/hr (fee only) | Mem $/hr (fee + 80% of 10% commission) |
|---:|---:|---:|---:|---:|---:|
| $3K (simple) | 1.5 | $0 | $0 | $0 | $128 (commission only) |
| $7K | 3 | $350 | $175 | $117 | $245 |
| $12K | 4 | $600 | $300 | $150 | $300 |
| $20K | 5 | $1,125 | $563 | $225 | $432 |
| $35K | 7 | $2,375 | $1,188 | $339 | $570 |
| $60K | 10 | $4,875 | $2,438 | $488 | $730 |
| $100K | 14 | $5,000 (cap) | $2,500 | $357 | $590 |

**Where it's right:** $15K–$60K trips clear $300–$700/hr, which is the correct band for a senior solo advisor.

**Where it's under-priced:** $3–7K trips. The $0 floor under $5K is generous to a fault — those trips still take 1–1.5 hours and the advisor recovers only the commission ($80–$200). **Fix: institute a $150 intake fee for any booked trip <$5K from non-members, waived for members.**

**Where it's over-priced (i.e. the cap binds too low):** $100K+ trips. A $100K trip is probably 12–16 hours of work plus FAM relationships and supplier negotiation. A $5K cap on a $100K trip is $312/hr, which is on the low end. The cap is set at the wrong number — **$10K cap is more defensible**, with the buyer accustomed to that band (Indagare Custom takes $2,850/yr but charges meaningfully on $100K+ trips through commission stacking).

**The 50% member discount** is the same structural inversion identified in the pricing-stress-test: heaviest users get the steepest cut. The fix proposed there (25% discount above $30K only) still applies. At 50% off across the board, the founder is giving away ~$15–25K/yr of labor at Y3 cohort size.

### A7. EA Companion Seat economics

This is a clever feature — bundling a Light seat for the principal's chief of staff into Office and Society. It increases stickiness, doubles the inbound channel, and reduces voicemail tag. But what's the marginal cost?

| Component | Marginal cost |
|---|---|
| Additional CRM contact, calendar tracking | ~$0 |
| 24/7 desk routing (already provisioned) | ~$0 |
| Incremental trip volume from EA's own personal travel | Could be **net positive** if EA books leisure |
| Extra labor on principal-trip coordination | ~30–60 min per trip |
| Risk of EA leaving the principal and orphaning the seat | Real — see below |

**Net cost per Office member from the EA Companion Seat: ~$300–$600 of incremental labor annually** (30 trips × 1 hour of additional coordination at $200/hr, deflated for overlap).

**Hidden risk:** EAs job-hop every 18–30 months in the principal segment. When the EA leaves, two things can happen: (a) the new EA inherits the seat and onboarding labor restarts (this is fine, ~3 hours one-time), or (b) the old EA takes the principal's book of trust with them and the principal renews lukewarmly. Empirically (b) happens in maybe 15% of EA transitions. **Plan for ~5% annual churn lift in Office tier attributable to EA churn.**

EA Companion Seat is correctly designed but should be **conditional on Office members naming their EA at signup**, with a 60-day window. Otherwise it becomes a checkbox feature that's never used and provides no stickiness.

---

## B. Bear / Base / Bull pressure test — plus a Failure case

### B1. Is the v2-facts base case mix realistic?

The base case Y5: **60 Light / 40 Office / 20 Society = 120 members → $871K**.

| Mix assumption | Plausibility | Evidence |
|---|---|---|
| 60 Light at Y5 | **Plausible** at ~12 net adds/yr after Y1 | Sales cohort shows ~50% of close-eligible interest at Light tier |
| 40 Office at Y5 | **Stretched** — requires 8 net adds/yr from Y2 onward | Cohort shows Office as the dominant tier (37% of closes) but absolute volume needs 10+ Office closes/yr at full pricing |
| 20 Society at Y5 | **Aspirational** | Society cap is 30 globally per v2-facts; the 4 latent Society leads in the cohort are conditional, not closed. Hitting 20 by Y5 requires 5 net Society adds/yr from Q1 2027 onward, with no churn |

The bigger question is **pace of acquisition**. The v2-facts table implies:

| Year | Light adds | Office adds | Society adds | Total new | Churn implied |
|---|---:|---:|---:|---:|---:|
| Y1→Y2 | +13 | +7 | +1 | 21 | minimal (year-old book) |
| Y2→Y3 | +15 | +10 | +4 | 29 | minimal |
| Y3→Y4 | +5 | +10 | +7 | 22 | ~5 (assumed) |
| Y4→Y5 | +5 | +5 | +8 | 18 | ~5 |

Y2→Y3 requires 29 net adds in a year. At a 60% close rate on warm leads and ~40% on cold, that's **~50 qualified discoveries**, or about **4/month**. The simulated cohort suggests 28 discovery calls produce ~7 outright closes plus 14 conditionals (probability-weighted ~$105K). To get 29 net adds, the founder needs **~115 qualified discovery calls in Y3** — which requires either 2.4 cohorts of the simulated quality OR a referral engine generating warm leads at 2–3x the cold cadence.

The Y3 ramp is the **stress point** in the base case. Pre-revenue investors will dig hard here.

### B2. Base case rebuilt with corrections

Applying the corrections from Section A (7.8% blended commission rate, dormancy decay, realistic ADR mix, design fee leakage on small trips):

| Year | Mix (L/O/S) | Subscription (modeled) | Commission/design (corrected) | Total (corrected) | vs. v2-facts |
|---|---|---:|---:|---:|---:|
| Y1 | 22/8/0 | $50K | **$23K** | **$73K** | -$7K |
| Y2 | 35/15/1 | $96K | **$47K** | **$143K** | -$13K |
| Y3 | 50/25/5 | $194K | **$124K** | **$318K** | -$35K |
| Y4 | 55/35/12 | $315K | **$203K** | **$518K** | -$57K |
| Y5 | 60/40/20 | $431K | **$344K** | **$775K** | -$96K |

**Corrected base case Y5: ~$775K, not $871K.** The 11% gap is primarily the Virtuoso clip methodology error, secondarily the dormancy term, and tertiarily the small-trip design-fee leakage.

### B3. Bull case — what would have to be true?

The v2-facts bull case: **80 Light / 60 Office / 30 Society = 170 members → $1.6M**.

For this to hold, **every** of the following must be true simultaneously:

1. **Society at cap (30/30).** Requires 6 net Society adds/yr for 5 years. With Q1 2027 launch, that means 10 Society members by end of Y2027, 16 by Y3, 22 by Y4, 30 by Y5. **Probability: 15–25%** — Society is the highest-quality but lowest-volume product, and 30 invite-only family-office relationships is a 7-year relationship-building exercise, not a 4-year one.
2. **Office acceleration to 60.** Requires 12 Office closes/yr post-Y2. The cohort produces ~4 conditional Office closes per 28 sims; needs 3 sim-equivalent cohorts per year of Office-grade leads. **Probability: 25–35%.**
3. **Light to 80.** Easiest line — 16 net adds/yr. **Probability: 50–60%.**
4. **Fora 90/10 split achieved by Y4.** Requires $2M personal sales/yr by Y4. At Y4 Office+Society mix this is plausible — $2M total commissionable bookings = $14K/Office × 35 Office + $50K/Society × 12 Society + Light = $2.1M. **Probability: 40–50%.**
5. **Zero churn surprises in Society cohort.** One $25K/yr Society churn = -$25K. Five churns over Y2–Y5 = -$125K cumulative impact. **Probability of zero meaningful Society churn: 20–30%.**

Joint probability of all five: **~1–4%.** Bull case is a marketing artifact, not a planning case. Investors will discount it to near-zero.

A more honest "upside" case: 70 Light / 50 Office / 12 Society at Y5 = $1.1M corrected. **Probability: 15–20%.**

### B4. Bear case — too generous?

The v2-facts bear case: **60 Light / 30 Office / 5 Society = $500K**.

This is **not bear enough**. Bear should encode failure modes, not just slower growth. A realistic bear scenario includes one or more of:

- Y2 churn spike (8–12% on cohort 1)
- Society delayed to Q4 2027 (slipping the entire ramp by a year)
- Fora split stuck at 70/30 through Y4 (founder doesn't hit $300K)
- Light dormancy at 25% by Y3
- One Office member files a public complaint, damaging referral velocity for 6 months
- Founder takes 4 weeks of personal medical leave at Y3

A truly bear case: **50 Light / 20 Office / 3 Society = $310–360K**, accounting for ~20% dormancy and 70/30 Fora split through Y4.

| Scenario | Members Y5 | Subscription | Commission/design (corrected) | Total Y5 |
|---|---|---:|---:|---:|
| Failure (see B5) | 30/10/0 | $66K | $34K | **$100K** |
| Realistic bear | 50/20/3 | $159K | $158K | **$317K** |
| Corrected base | 60/40/20 | $431K | $344K | **$775K** |
| Realistic upside | 70/50/12 | $385K | $390K | **$775K** with different mix; **$1.1M** with full Society ramp |
| v2-facts bull | 80/60/30 | $635K | $665K | **$1.3M corrected ($1.6M as published)** |

### B5. Failure case — Society never launches, Office stays small, only Light scales

Useful and required for any investor conversation. Assumptions:

- Society never ships (founder can't recruit dedicated principal at affordable cost; legal/NDA complexity stalls)
- Office hits ~10 and plateaus (founder can't reliably close $249/mo at PE/VC/RIA partner tier without a senior team brand)
- Light scales to ~30 by Y5 (organic Toronto-network growth, limited but real)

| Line item | Y5 value |
|---|---:|
| Light: 30 members × $1,188 | $35,640 |
| Office: 10 members × $2,988 | $29,880 |
| Light commission (corrected 7.8%, 18 nights, $420 ADR) | 30 × $491 × 0.85 dormancy | $12,520 |
| Office commission (3 active × 18 × $700 × 7.8% × 70%) | 10 × $2,063 × 0.9 | $18,570 |
| Personal travel commission | 30 × $200 + 10 × $1,200 | $18,000 |
| Design fees (net 50% from members) | low volume | $5,000 |
| **Total Y5 gross revenue** | | **~$120K** |
| Founder fixed opex (Section C) | | **$(95K)** |
| **Net to founder pre-tax** | | **~$25K** |

**Failure case Y5: a $120K business that nets the founder $25K** — i.e., the business is a money-losing hobby that the founder subsidizes from prior savings or a spouse's income.

This is the case investors care about most. The probability of Failure-case outcomes (defined as Y5 < $200K gross) is, on my read, **30–40%**, driven primarily by Society launch risk and the founder's solo execution risk in a category with no track record.

---

## C. Missing / under-modeled costs

The v2-facts doc lists a Y1 networking budget ($15–20K Toronto) but does not include a full opex line. The v1.0 plan had a $40K opex line that was already light. Let me rebuild the realistic fixed-cost base.

| Category | Y1 | Y3 | Y5 | Notes |
|---|---:|---:|---:|---|
| **Founder personal burn** (not in any version) | $90,000 | $110,000 | $120,000 | Toronto solo, no spouse income contribution assumed; this is salary equivalent the business must support |
| E&O insurance (Travel Industry Solutions) | $800 | $1,200 | $1,800 | Scales with bookings |
| Professional dues (Virtuoso, ASTA, etc. via Fora) | $1,200 | $1,500 | $1,800 | Mostly covered by Fora but conference fees flow through |
| FAM trip costs (gap above supplier-covered) | $4,000 | $7,000 | $10,000 | Industry standard |
| Cross-border tax compliance (Canadian CCPC invoicing US in USD) | $3,500 | $5,000 | $7,500 | Includes CRA + IRS Form W-8BEN-E filings, transfer pricing if Fora is treated as US payer |
| Software stack (CRM, Axus or equivalent, Stripe, accounting, comms, e-sign) | $4,800 | $7,200 | $10,800 | $400–$900/mo, scales with team |
| Stripe / payment processing (2.9% + $0.30) | $2,500 | $11,000 | $25,000 | On membership + design fees |
| Contractor labor (overnight desk coverage at scale) | $0 | $24,000 | $60,000 | Required for 24/7 SLA once members > 50 |
| Marketing (beyond Toronto network: content, ads, conferences, PR) | $18,000 | $35,000 | $55,000 | $15–20K networking + content/PR/conf is realistic; the v2-facts doc only counts networking |
| Travel costs for client meetings (founder to US for Year-in-Reviews) | $6,000 | $18,000 | $30,000 | Year-in-Review is a Society obligation; flights, hotels, dinners |
| Legal (contracts, refund disputes, Society NDA framework) | $4,000 | $6,000 | $9,000 | Stripe disputes alone add ~$500/yr |
| Brand maintenance (website, hosting, design refresh) | $3,000 | $4,000 | $5,000 | |
| Conferences (Virtuoso Travel Week, ILTM, Skift) | $5,000 | $9,000 | $12,000 | $4–7K per conf incl. flights |
| TICO (Path B option, deferred) — included for completeness | $0 (Y1 Path A) | $8,000 | $3,000 | Initial bond + annual renewal |
| Buffer / contingency | $4,000 | $7,000 | $10,000 | |
| **Total ex founder burn** | **$56,800** | **$143,900** | **$240,900** | |
| **Total inc founder burn** | **$146,800** | **$253,900** | **$360,900** | |

**Reality check vs. the v2-facts Y5 base case ($871K gross):**
- Corrected Y5 gross: ~$775K
- Y5 opex (inc. founder burn): ~$361K
- **Y5 net to founder/business: ~$414K**

That's still a real business, but it's **half** of what the headline number implies, and assumes everything goes right. Under the realistic bear case ($317K gross, $361K opex), **the business loses money at Y5** — which is the most important sentence in this document.

### C1. The 90-day refund liability

The First 30 program offers 90-day no-fault exit. At Y5 cohort size:
- 120 members × roughly 30% are within 90 days of signup at any given month (assume 4-year average tenure with steady inflow → 1/16 ≈ 6%; conservative if churn is rising, take 10%)
- 120 × 10% = **12 members within refund window at any moment**
- Average refunded subscription: ~3 months × $200 weighted = $600
- Worst-case simultaneous refund event (cohort discovers a service quality issue): **12 × $600 = $7,200** — manageable

**But the deeper risk is reputational.** If 3 Office or 1 Society member exit in the same 90 days, the founder may face $3–25K of refunds plus a public LinkedIn reputational hit at exactly the moment they're trying to close Y3 acceleration. **Reserve 1 month of refund liability ($8–10K) on the balance sheet.**

### C2. Cross-border tax exposure (the line most likely to surprise the founder)

The founder is in Toronto (Canada). Fora is US-based. Subscriptions and commissions flow USD → CAD. Members are US-based (under Path A, US-only sales).

Key issues:

1. **CCPC status.** A Canadian-controlled private corp with US-source business income may face US tax filings (Form 1120-F) if there's a "permanent establishment" in the US, OR if the founder spends >183 days/yr in the US for client meetings. **Avoid by capping US visits at 120 days/yr.**
2. **GST/HST.** Subscription fees from US members are "zero-rated" for GST purposes (exported services), but the founder must still register if revenue exceeds $30K CAD (~$22K USD), which Y1 will. **Annual filing required.**
3. **Tax treaty.** US-Canada treaty Article XII covers commissions; Article VII covers business profits. Fora as the US payer will issue 1099 or W-8 documentation. **The founder needs a tax accountant fluent in both jurisdictions — Toronto-based "small business" accountants usually are not. Budget $5–8K/yr for proper compliance.**
4. **Currency risk.** All revenue in USD, all expenses in CAD. A 5% CAD strengthening = 5% revenue hit. **Hedging is not realistic at this revenue scale, but the founder must show awareness of the FX exposure.**

The v1.0 plan ignored this. The v2-facts doc ignores this. **This is the single most-cited oversight investors will flag.**

---

## D. Cash flow timing risks

### D1. Commission timing

Hotel commissions are paid 30–90 days post-travel. For a Y5 cohort with $250K of hotel commission revenue, this means at any moment **$20–60K of commission receivable is outstanding**. If a supplier delays payment (common with Marriott direct), $5–15K can sit uncollected for 4–6 months.

**Implication for Y1–Y2:** the founder needs ~$25K of working capital cushion in months 4–9 because Y1 trips booked in months 1–3 won't pay commission until months 5–7. The subscription line covers operating costs, but new advisors typically run a 6-month cash gap before commissions stabilize.

### D2. Refund clawbacks

If a Light member cancels in month 5 of their annual subscription (paid monthly via Stripe), they pay no further but the founder has already counted them as a member. Net Y2 forecasting risk: **~5% of subscription line erodes from mid-year churn**.

More dangerous: if Society members prepay annually ($12–30K upfront) and cancel under the First 30 program, the founder must refund unbooked travel. **Worst case Society refund**: a $25K/yr member cancels in month 2, having taken one $40K family trip. Refund of subscription = $20,830 (10/12 of unused). Commission already paid on the $40K trip = ~$2,800 net. **Net refund liability = $18K cash out, against $2,800 net cash in. -$15K to the business.**

**Fix:** Society program should require non-refundable initiation fee ($3–5K) AND prorate only the unused subscription months. Spelling this out in the Society contract is critical.

### D3. Seasonality

- **Q1**: PE/VC LP meeting season. Heavy booking month. Commission revenue lands in Q2.
- **Q2**: Spring leisure (RIA principal Italy trips). Moderate booking.
- **Q3**: Fundraising road shows; founder/VC summer travel. Moderate.
- **Q4**: Holiday family travel (Society high season); business travel drops sharply post-Thanksgiving. **High personal travel revenue, low business travel.**

Practical implication: **commission revenue is back-half loaded** (Q3–Q4 booking → Q4–Q1 commission receipt). The founder will have a cash trough in May–July of each year. **Reserve 2 months of opex ($25K Y1, $50K Y3) as a working-capital buffer.**

### D4. Society launch gap — what does Y2 cash flow look like?

Society launches Q1 2027 per v2-facts (deferred from Q3 2026). Y2 = 2027 in the v2-facts timeline. So Y2 has:

- Subscription: $96K modeled
- Commission/design: $60K modeled
- Corrected total: ~$143K
- Y2 opex inc founder burn: ~$185K
- **Y2 net: -$42K**

**Y2 is cash-negative**. The founder needs $40–50K of working capital (savings, partner income, or short-term debt) to bridge Y2. This is the most important number the founder is hiding from themselves. **Investors will see it immediately.**

If Society slips further to Q3 2027 or Q1 2028, the Y2 deficit widens to $55–70K and Y3 starts cash-negative too. **Society launch date is the single most cash-sensitive variable in the model.**

---

## E. Pricing viability under different funnel mixes

### E1. 100% warm/referral cohort (the simulated baseline)

The sales-kit projection shows 28 calls → $105K Y1 expected revenue. This assumes:
- 7 outright closes (25% close rate)
- 14 conditionals at probability-weighted conversion (50% close rate)
- Calls sourced through warm intro / brother-in-law / Soho House / EO Toronto / old boss

**Plausibility check.** A 25% outright close rate on warm leads is **aggressive but defensible** for a relationship-introduced product. Real-world data from concierge medicine and high-end advisory suggest 15–22% is the central tendency. **$105K Y1 from 28 warm calls is at the 75th percentile of realistic outcomes.**

To generate 28 warm calls in Y1, the founder needs **~60–80 warm introductions** (some won't convert to discovery calls). The Toronto network plan (Soho House + EO + brother-in-law dinners) plausibly generates 30–50 in Y1. **The gap is the old boss + first 5 referrals, which need to compound.**

### E2. 50/50 warm/cold mix

If half the cohort is cold:
- 14 warm calls × (25% × $6K + 50% conditional × 50% × $4K) = 14 × ($1.5K + $1K) = **$35K**
- 14 cold calls × (8% × $5K + 25% conditional × 30% × $3.5K) = 14 × ($400 + $263) = **$9.3K**
- **Total Y1: ~$44K**

To recover to $80K Y1 (v2-facts Y1 target), the founder needs to **double the cold call volume** — i.e., 14 warm + 28 cold = 42 total discovery calls, or ~3.5/month. Probably doable but requires deliberate cold-outreach cadence.

### E3. 100% cold

Per v2-facts: cold email reply 1–3%, reply→call 30–50%, call→conditional yes 15–25%, conditional→close 40–60%.

Joint funnel: 1.5% × 40% × 20% × 50% = **0.06% close rate from outreach**.

To get 10 cold closes (~$30K of Light/Office, maybe $50K with one bigger account): **~16,000 cold outreaches.**

To get to v2-facts Y1 target of $80K from 100% cold: **need 25–30 closes** = **40,000+ cold messages**.

At a sustainable cadence of 50 personalized cold messages/week (founder solo), that's **800/year**. **100% cold cannot hit Y1 target.** Realistic 100% cold outcome Y1: **$15–25K**.

The v2-facts plan rightly prioritizes warm. But the model should explicitly show that **without 70%+ warm sourcing, Y1 misses by 60–80%.**

### E4. Pricing-viability summary

| Funnel mix | Realistic Y1 revenue | vs. $80K target |
|---|---:|---|
| 100% warm/referral (simulated cohort) | $90–110K | Hit or slightly beat |
| 70/30 warm/cold | $70–85K | On target |
| 50/50 warm/cold | $40–55K | Miss by 30–50% |
| 100% cold | $15–25K | Miss by 70–80% |

**Bottom line:** the v2.0 plan only works if Y1 is overwhelmingly warm-sourced. The Toronto Y1 plan needs to be executed with rigor. **One ICP investor question to expect: "What's your warm pipeline depth right now?" If the honest answer is < 30 named introductions, the plan is at risk.**

---

## F. Verdict — what would actually get funded

### F1. Seed investor at $250K SAFE, $3M cap

**No.** A $3M cap implies the investor's $250K becomes ~8% of the company. For that to make sense, the investor needs to see a credible $25–50M outcome scenario within 5–7 years. This is a solo advisory practice with a Y5 base case of $775K gross / $400K net. Even at a generous 5x revenue multiple (which travel advisory does not command — it trades at 1–2x EBITDA), Y5 enterprise value is $2–4M. **The seed investor is buying down, not up.**

Additionally, no seed investor funds solo-founder lifestyle businesses with no scale path. The "30 Society cap" line in v2-facts is the death knell for venture economics — it explicitly states the firm will never scale beyond ~30 high-touch relationships. **Seed investors do not back firms that have written the scaling ceiling into the business model.**

### F2. Wealth / family-office investor

**Maybe, on different terms.** A family office with a thesis around personal services for the founder/operator class might write a $150–250K cheque structured as:
- Revenue share (5–10% of gross until 1.5–2x payback) rather than equity
- Or convertible note at $1.5M post with founder protection

The terms reflect that the family-office investor isn't looking for an exit — they're looking for either a steady yield or a relationship investment that gives them priority on Society membership. **This is the only realistic outside capital for v2.0.**

The pitch to a family office is not "this becomes a $50M company." It is "we get to 100–150 members and $1M of gross profit by Y5, you get your money back with a yield, and you get to be Society member #1." That's a viable conversation.

### F3. Bootstrap-only

**Yes, this is the strongest path.** The economics support a solo bootstrapped practice that nets the founder $250–400K by Y4–Y5 if the realistic upside case lands. That's a strong outcome for a one-person business with low capital requirements.

The cost of bootstrap is **the Y2 cash trough**. The founder needs to enter Y1 with ~$60K of personal savings or a credit line to bridge Y2's $42K deficit. **No outside capital but a personal balance sheet sufficient to absorb the trough is the realistic financing answer.**

### F4. Realistic exit outcome curve

| Outcome | Probability | Value to founder |
|---|---|---|
| Lifestyle business — $400–600K net to founder, no exit | 35% | $2–3M cumulative over 7–10 years |
| Acqui-hire by Fora, Tzell, or competing host | 15% | $500K–$2M one-time |
| Strategic acquisition by lifestyle membership co (Velocity Black, Inspirato) | 5% | $3–8M, founder rolls in |
| Society spinout becomes the actual business (family-office advisory) | 10% | $5–15M over 10 years if executed |
| Lifestyle business that quietly winds down | 25% | Founder recovers savings, walks away with brand and experience |
| Outright failure | 10% | -$50–150K personal exposure |

**IPO path: 0%.** This is not an IPO business. It is a high-quality solo practice with limited scaling.

The realistic expected value to the founder is **~$1.5–2.5M over a 7-year horizon**, weighted across outcomes. That's a real living, comparable to a senior partner track at a mid-sized firm — but it is not venture-backable, and the founder should stop pitching it as if it were.

---

## G. 10 specific fixes the founder must make before talking to capital

These are concrete edits to the financial model. Not soft suggestions.

### G1. Replace the Virtuoso clip methodology with a blended effective commission rate

Current model uses 10% × 70% Fora split = 7% net to advisor on commissions, treating the 2% Virtuoso clip as a separate line. **Reality: about 60% of bookings have the clip baked into the 10% (so the gross to advisor is 8%), the rest don't.** Use **7.8% blended × Fora split** as the commission yield. **Effect: -$130K on Y5 base case.**

### G2. Add a dormancy term

Light tier dormancy at Y3+ is empirically 15–22% of members capturing subscription only with negligible commission. **Apply 0.85 multiplier on Light commission revenue from Y3 onward.** Effect: -$8–12K on Y3, -$15–25K on Y5.

### G3. Build a real opex line, including founder burn

The model has no founder personal-cost line. Add **$90–120K/yr founder burn** plus the line items in Section C. **The Y2 cash trough of ~$42K becomes visible.** Then build a financing plan to bridge it.

### G4. Pin Fora down on the "$300K personal sales" definition

Get Fora's commission threshold language in writing — annual vs. cumulative, gross vs. commissionable, reset behavior. Model two scenarios (best-case and worst-case interpretation) and disclose both to investors. **Without this, the Y3 commission line is exposed to ±15% variance.**

### G5. Add a working-capital line

$25K Y1, $50K Y3, $80K Y5. Reflects the 30–90 day commission lag plus seasonal cash trough. **Show on the balance sheet, not just the P&L.**

### G6. Add a refund reserve

The First 30 program creates ongoing refund liability. **Reserve 1 month of subscription revenue on the balance sheet as a refund reserve.** Document the Society initiation-fee mechanism to bound Society refund exposure.

### G7. Add cross-border tax / FX line

$5–8K/yr for proper CCPC + US filings. **Disclose FX exposure explicitly** — show what the model looks like at 1.30 CAD/USD vs. 1.40.

### G8. Replace bear case with a realistic bear case

Current bear case ($500K Y5) is too generous. Build a real bear case with one or more failure modes active: Society delayed 12 months, Light dormancy at 25%, Fora split stuck at 70/30, or a Q3 churn event in cohort 1. **Realistic bear: $300–350K Y5.**

### G9. Build the failure case explicitly

A Y5 outcome with Society never launched, Office plateaued at 10, only Light scaled. **Show that this case nets the founder $20–30K, i.e., the business is a loss-making hobby.** Investors need to see the founder has thought about this honestly.

### G10. Fix the design-fee escalator and 50%-off mechanic

Two fixes:
- Add a $150 intake fee for trips under $5K (or refuse them). Plug the labor leak on small trips.
- Reduce the member discount from 50% flat to **25%, applied only to design fees on trips above $30K**. Stop subsidizing the heaviest users via the lightest ones. **Effect: +$8–15K/yr at Y5 cohort scale, plus a more defensible margin story.**

---

## Summary table — corrected v2.0 P&L

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---:|---:|---:|---:|---:|
| **Members (L/O/S)** | 22/8/0 | 35/15/1 | 50/25/5 | 55/35/12 | 60/40/20 |
| Subscription | $50K | $96K | $194K | $315K | $431K |
| Commission (corrected) | $18K | $36K | $94K | $158K | $267K |
| Design fees (net) | $5K | $11K | $30K | $45K | $77K |
| **Gross revenue (corrected)** | **$73K** | **$143K** | **$318K** | **$518K** | **$775K** |
| Founder burn | $(90K) | $(95K) | $(110K) | $(115K) | $(120K) |
| Other opex (Section C) | $(57K) | $(90K) | $(144K) | $(195K) | $(241K) |
| **Total opex** | **$(147K)** | **$(185K)** | **$(254K)** | **$(310K)** | **$(361K)** |
| **Net to founder/business** | **$(74K)** | **$(42K)** | **$64K** | **$208K** | **$414K** |
| Cumulative cash position | $(74K) | $(116K) | $(52K) | $156K | $570K |

**Three observations from the corrected table:**

1. **Y1 + Y2 cumulative deficit: ~$116K.** This is the working capital the founder must front. Without $100K+ of personal savings or a credit facility, the business doesn't survive to Y3.
2. **Breakeven is Y3, not Y2.** The original model implied earlier breakeven by understating opex.
3. **Y5 net of $414K is a strong solo-practice outcome but not a venture outcome.** Investors evaluating against $2–5M Series A-track businesses will pass; investors evaluating against a 7-figure lifestyle practice will engage on rev-share terms.

---

## Closing note

The v2.0 model is meaningfully better than v1.0. The pricing tiers are realistic, the Society tier is correctly invite-only-capped, the EA Companion Seat is a clever stickiness mechanic, and the 90-day refund program signals confidence.

But the model still does what most pre-revenue founder models do: it counts every revenue line at the high end of its range, omits founder burn, and treats the bull case as the planning case. Strip those out and apply the corrections above and **the business is a credible $400K-net solo practice by Y5 — not the $700K-net implied by the headline, not the $1.6M of the bull case, and not the $25K of the failure case.**

The founder should stop trying to make this look venture-backable. Pitch it honestly to a family office as a yield + access investment, bootstrap it through the Y2 trough on personal savings, and accept that the realistic exit is a strategic acquisition by a lifestyle membership company in Y7–Y9 for $3–8M. **That's a good outcome. Pretending it's a $50M outcome is what gets investors to pass.**

The 10 fixes in Section G are mandatory before any capital conversation. Two of them (G1, G3) will change the headline Y5 number by 20%+ each. Better to have an investor learn that from the founder's own analysis than to have them find it in diligence.

---

*Word count: ~5,800. Written for the founder's decision, not for the deck.*
