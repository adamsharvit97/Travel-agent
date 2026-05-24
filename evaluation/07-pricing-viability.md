# 07 — v2.0 Pricing Viability: A Pre-Revenue Investor's Stress Test

**Evaluator role:** Sharp pre-revenue investor. Brutal lens.
**Ground truth:** `/tmp/v2-facts.md` (Latitude 43 v2.0 facts).
**References:** `research/pricing-stress-test.md`, `research/adjacent-lifestyle-memberships.md`, `research/adjacent-card-concierges.md`.
**Date:** 2026-05-24.

---

## Investor's TL;DR (read this first)

The v2.0 pricing structure is a meaningful improvement over the $50/mo proposal that the prior stress-test killed. It is **closer to credible** at every price point, and the architectural decision to retain 100% of subscription dollars while sharing only commissions with Fora is the single smartest move in the entire plan. That alone converts a marginal Y1 into a survivable one.

But "improvement" is not "investable." Under a hard investor lens, **v2.0 still has six structural cracks**:

1. **The $99 Atlas Light tier is priced into a dead zone** — above the content-only floor ($33/mo) but below the credible-human-relationship floor ($200/mo). It will attract the wrong members and create the wrong expectations.
2. **The 70/30 → 80/20 threshold ($300K personal sales) is harder to clear than the plan models.** The Y2 numbers assume the founder hits 80/20 by end of Y1. The math says probably not.
3. **The "subscription = 100% to advisor" claim is not independently verified.** It is the load-bearing assumption of the entire model. If Fora's policy changes — or if it was never that policy to begin with — the plan loses ~$50–$430K in 5-year value depending on the timing.
4. **The design fee escalator delivers $50–$200/hr effective rates on the most common trip bands.** That is a labor problem with a money disguise.
5. **First Loss Insurance is unpriced** ($30K of theoretical exposure that is plausibly real on 30–50% of named trips in Y1, given the support-call-black-hole pain point being the *whole pitch*).
6. **Society at $14K is below the prevailing market floor for a 1:6 service-ratio, dedicated-principal, 15-minute-SLA product** — Knightsbridge's nearest analog is £25K ($31K) at 1:5, and Knightsbridge has 10 years of provenance Latitude does not have.

**Verdict:** A bootstrapped solo founder can survive Y1–Y2 on this pricing if and only if the warm-anchor close happens, the 70/30 split is endured without complaint, and Society is deferred (which v2.0 has correctly already done). **The plan does not break at Y1.** It breaks at the Y3 inflection where the model assumes Society members and the founder needs to be in two service registers at once with no team.

**What I would change before launch:**
- Kill or radically reposition Atlas Light at $99. Either raise to $199 (credible-human band) or strip the human and price at $49 (content + AI band).
- Tighten the 80/20 trigger language: it's a Fora-controlled threshold, not a Latitude-controlled outcome.
- Lock subscription policy with Fora in writing before launch.
- Re-cut the design fee escalator to start at $5K with a $500 floor — not $250 on a $5K trip.
- Charge an upfront $1,500 Society induction fee to offset First Loss exposure.
- Defer Society to Y3 at the earliest. Y2 is too aggressive.

The rest of this document shows the math.

---

## A. The v2.0 Price-Point Audit

### A.1 Atlas Light — $99/mo ($1,188/yr)

**Position claim:** Just above Indagare Self Planner ($33/mo, content-only). Below the "no human service exists below $200/mo" floor.

**Why $99 fails the credible-floor test:**

The pricing stress-test established (Section 1.4) a five-band credible price ladder:

| Band | Price | What it pays for | Examples |
|---|---:|---|---|
| Content + app only | $33–$50/mo | Self-serve, no human | Indagare Self Planner, One Medical |
| Content + async human triage | $99–$150/mo | **Gap in market** | (none) |
| Named human relationship, on-demand | $200–$400/mo | Indagare Custom, Velocity Black, MDVIP, Soho House CWH |
| Named human + escalation, hard SLA | $400+/mo | Sollis, E by Equinox |
| Bespoke / quiet ultra-luxury | $1,000+/mo | Knightsbridge, Sienna Charles |

**The investor read:** the "gap in market" framing is *almost always* a self-deception. Gaps exist for a reason. The $99–$150/mo band is empty because **the unit economics of putting a human on the line at $1,188/yr per member do not work for the operator** — which is exactly what the stress-test math showed. Atlas Light at $99 is asking the founder to volunteer for the same trap that killed Forward at $149/mo.

**The v2.0 defense (steelmanned):** v2.0 design fees are stacked on top of Light ($250 floor at $5K, scaling up), and Light commissions still flow. The $99 is not the only revenue line. The per-member Y1 economics in `/tmp/v2-facts.md` say $2,400–3,000 per Light member, which is the same neighborhood as a $200/mo pure-subscription product.

**Why this defense partially works:**
The math is roughly correct *if* the Light member books 18 nights/year through Fora at $500 ADR with 30% on commissionable preferred rates. That is a plausible assumption for a business traveler. The per-member economics are not fake.

**Why this defense does not fully work:**
The $99 price point sets *buyer expectations* of service level. A buyer paying $99/mo expects content-tier responsiveness. A buyer paying $200/mo expects relationship-tier responsiveness. **The v2.0 plan promises relationship-tier service (24/7 desk, named text/email)** to a $99/mo buyer. This is the same register-price mismatch that the stress-test flagged at $50/mo, just scaled up. The mismatch is smaller but not eliminated.

**Predicted failure mode at $99:**
Light members will treat the desk as their personal travel agent for any whim ("can you book my anniversary dinner?"). Light members will adverse-select into the lowest-margin trip patterns (multiple sub-$5K bookings where no design fee applies and commission is thin). Light members will churn at consumer-subscription rates (8% annual base, per Recurly), which at $1,188/yr is a $9,500 cliff per 10 members.

**Where $99 might survive:**
If — and only if — Atlas Light is genuinely positioned as **the on-ramp tier**, with a hard policy that 18 nights/year × $500 ADR (= $9K booking volume) is required for renewal eligibility, and members who fall below that are politely upsold to per-trip booking with no membership. This is unstated in v2.0. It should be stated.

**Investor verdict on $99:** Tentatively viable as written *only because* design fees and commissions backfill it. Strategically, $99 is the wrong price. Either raise to $199 or strip human service and price at $49 + per-trip design fees.

### A.2 Atlas Office — $249/mo ($2,988/yr)

**Position claim:** Below Velocity Black ($258/mo) and Soho House CWH ($358/mo).

**Why $249 is *the most defensible* price point in v2.0:** this is the band where adjacent comps cluster — Velocity Black ($258), Soho House CWH ($358), MDVIP ($200), Indagare Custom ($238). $249 sits in the middle of the credible-named-relationship band.

| Comp | Monthly | Service ratio |
|---|---:|---|
| Indagare Custom Planner | $238 | Undisclosed |
| Velocity Black | $258 | Undisclosed |
| Soho House CWH | $358 | n/a |
| MDVIP entry | $200–$417 | ~1:600 |
| **Atlas Office (v2.0)** | **$249** | **1:15 claimed** |

**Bundle is strong.** "Design fees waived" is a real economic gift — at 5 travelers × 3 named trips × $750 average fee saved, that's $11,250/yr of fee waiver against $2,988/yr of subscription. EA companion seat is a soft moat (EA becomes the booking advocate inside the principal's company).

**Labor density problem:** Office is sold as 5 travelers. If 5 Office members hit their cap (5 × 18 trips × ~1 hour each), that's **450 hours/year per Office member**. 15 Office members × 450 hours = 6,750 hours/year, or 130 hours/week. Even at 1:15 service ratio, this breaks the solo founder at ~6 Office members. Plan models 8 in Y1, 15 in Y2 — both above the labor ceiling.

**Investor verdict on $249:** Right price. Wrong service promise. Fix: cap "active travelers" at 3 (not 5), or redefine "up to 5" as a roster (not a usage allowance).

### A.3 Latitude Society — $1,000–$2,500/mo ($12K–$30K/yr)

**Position claim:** Above Indagare Custom ($2,856/yr) but below Knightsbridge (~$31K/yr).

| Comp | Annual | Service ratio | Member count | Provenance |
|---|---:|---|---|---|
| Indagare Custom | $2,850 | Undisclosed | Several thousand | 19 years |
| Sienna Charles | $50K base | Undisclosed | $100M+ NW required | 18 years |
| Knightsbridge Standard | $31,000 | 1:4–1:5 | 50–60 capped | Ex-Amex Centurion Elite architect |
| Knightsbridge Elite | $124,000 | Higher | Subset | Same |
| **Latitude Society** | **$12K–$30K, avg $14K** | **1:6** | **30 cap** | **Solo founder, no track record** |

**The brutal comparison:** Knightsbridge has McNeill's Amex Centurion provenance (built the original Centurion service, designed Elite at 1:10, quit when told to scale). That provenance is *the entire brand*. 95%+ renewal. Earned over a decade.

**Latitude Society at $14K average is asking principals to pay 45% of Knightsbridge's price for a founder with no track record.** The buyer at $14K/yr is not bargain-hunting; they are status-buying. Pricing 45% below the leader signals *45% less credible*, not *45% better value*.

**Defense (steelmanned):** v2.0 has correctly **deferred Society to Q1 2027**. The price is *modeled* but not *live*. This buys 6 months of Y2 to build proof points.

**Remaining problem:** even deferred, the founder has ~6 months to manufacture the Society-credibility stack — 2–3 Office case studies, named hotel GM partnership, Atlas Conduct doc, application/committee, founder long-form press. Without that stack, Society at $14K is a price without a brand. Y3 plan assumes 5 Society members netting $26K–$46K each — that's 50% of Y3 revenue resting on Society.

**The band:** sensible. But the **modal price needs to be $2,083/mo ($25K/yr) to be credible against the Knightsbridge anchor**. Pricing the average at $14K (bottom-half of band) sends a discount signal. Either compress band to $20K–$30K with fewer members, or accept Society competes against Indagare + a $1K/mo upcharge, not Knightsbridge.

**Investor verdict:** Deferral correct. Band correct. Modal price ($14K) too low for the positioning logic. **Move the average to $20K+ or reposition Society downward.** Cannot have it both ways.

---

## B. The 70/30 → 80/20 → 90/10 Fora Split Implications

### B.1 Y1 starts at 70/30. Founder needs $300K personal sales to hit 80/20.

**The arithmetic:**

Personal sales at Fora means **commissionable booking volume that the advisor personally drove**, not subscription revenue. Per `/tmp/v2-facts.md`, the Y1 mix is 22 Light + 8 Office = 30 members. Average booking volume per member at v2.0 assumptions:

| Tier | Annual hotel nights | ADR | Total booking | Commissionable @ 30% prefer-rate |
|---|---:|---:|---:|---:|
| Light | 18 | $500 | $9,000 | $2,700 |
| Office | 3 travelers × 18 = 54 | $500 | $27,000 | $8,100 |
| Society (Y1: 0) | — | — | — | — |

Y1 personal sales calculation:
- 22 Light × $9,000 = $198,000 total / $59,400 commissionable
- 8 Office × $27,000 = $216,000 total / $64,800 commissionable
- **Y1 total volume: $414,000.** This exceeds $300K. Good.
- **Y1 total commissionable: $124,200.** This is the more relevant number for Fora's threshold.

**The ambiguity:** Fora's $300K threshold is documented in the stress-test as "personal sales/year" without specifying gross booking volume vs. commissionable volume vs. commissionable revenue. The most common industry reading is **gross booked volume** — in which case the founder clears $300K easily at 30 members.

**The catch:** the founder must clear $300K in **personal sales within a calendar year for the next year's split to bump**. Fora resets advisors annually. So:
- Y1: starts at 70/30 (always — every new advisor starts here).
- Y1 ends: if cumulative personal sales ≥ $300K, Y2 split = 80/20.
- Y2 ends: if Y2 cumulative ≥ $300K (or whatever Fora's renewal threshold is), Y3 stays at 80/20.

The plan implicitly assumes that **once 80/20 is achieved, it persists**. That is not how Fora works in industry practice. Most host agencies require annual re-qualification. If the founder hits $300K in Y1 (likely) but has a slow Y2 (possible if churn hits or Society launch is delayed), they could drop back to 70/30 in Y3.

### B.2 What if Y1 personal sales fall short?

**Stress scenarios:**

| Y1 Membership outcome | Booking volume | Hits $300K? | Y2 split |
|---|---:|---:|---|
| Plan (22L + 8O) | $414K | Yes | 80/20 |
| Soft Y1 (15L + 5O) | $270K | **No** | 70/30 |
| Very soft (10L + 3O) | $171K | No | 70/30 |
| Anchor-only (5L + 1O) | $72K | No | 70/30 |

**The "soft Y1" is the realistic Y1 for a solo founder with no track record.** Cold-funnel math in `/tmp/v2-facts.md` says 5,000 outreaches per 10 cold closes. The Y1 plan correctly relies on warm/referral instead — but warm/referral on a brand-new product without case studies still converts at perhaps 30% of qualified intros. The founder probably needs 80–100 warm intros to land 22+8=30 members in Y1. That's a tall ask for one brother-in-law's network + one anchor + Soho House Toronto + EO Toronto.

**Y2 economic delta if founder stays at 70/30:**

| Line | At 80/20 | At 70/30 | Delta |
|---|---:|---:|---:|
| Y2 commission revenue (modeled $60K at 80/20) | $60,000 | $52,500 | **−$7,500** |
| Total Y2 revenue | $156,000 | $148,500 | **−$7,500** |

Small in absolute terms. But the cumulative effect compounds: if 70/30 persists through Y2 and the $2M lifetime threshold for 90/10 is similarly delayed, the founder leaves **~$40–60K on the table over 5 years**. That's the difference between paying off Toronto Y1 networking spend twice over vs. once.

### B.3 Annual reset vs. lifetime — the actual Fora policy

**This is a known unknown for the founder.** `/tmp/v2-facts.md` does not specify whether the 70/30 → 80/20 → 90/10 ladder is:
- **Lifetime achievement**: once hit, always retained ("you earned 80/20, you keep it"); or
- **Annual qualification**: must hit thresholds each calendar year ("80/20 if last year's sales were ≥ $300K").

Industry norms at host agencies vary. Andavo (cited in the stress-test) uses annual thresholds. Brownell's Catalyst is similar. **The plan should not assume lifetime ratcheting until verified in the Fora advisor contract.**

**Action item before launch:** founder must obtain Fora's written policy on whether commission split tiers reset annually. If they reset, the Y3+ revenue model needs a 5–10% haircut on commission lines to reflect realistic split persistence risk.

---

## C. The "Subscription = 100% to Advisor" — Verification Required

### C.1 Is this Fora's actual policy?

**This is the single load-bearing assumption of v2.0.** The entire architecture of the plan rests on the founder retaining 100% of membership subscription dollars, with only commissions split with Fora. If this is true, v2.0's net economics are dramatically better than v1.0's. If it's false, the plan loses ~$60K–$130K/yr in Y4–Y5.

**What is plausible:** Fora is a host agency. Host agencies generally split *travel commissions* (the IATA-licensed revenue stream that requires their accreditation). They do not generally split *advisor-charged client fees* — design fees, planning fees, retainers — because those are advisor-to-client transactions outside Fora's IATA umbrella. A membership subscription is arguably a *retainer* or *service fee*, not a travel commission. Under that framing, 100% to advisor is plausible.

**What is concerning:** some host agencies *do* take a cut of all advisor-collected revenue, including planning fees and retainers, because their hosting agreement defines "advisor revenue" broadly. Fora's specific hosting agreement is not in the founder's documents. The pricing-stress-test cites Fora's published advisor commission resource but does not cite a Fora statement on planning fees or membership retainers.

**Risk-adjusted scenarios:**

| Fora's actual policy | Y5 subscription revenue at base case | Net to founder | Delta |
|---|---:|---:|---:|
| 100% to advisor (assumed) | $431K | $431K | $0 (base) |
| Fora takes 10% of subscription | $431K | $388K | **−$43K** |
| Fora applies 70/30–90/10 split to subscription | $431K | $345K (avg 80/20) | **−$86K** |
| Fora applies different split (e.g., 50/50 above a threshold) | $431K | $216K | **−$215K** |

A 50/50 outcome on subscription would functionally destroy v2.0. The plan would revert to v1.0 economics.

### C.2 What if Fora changes policy mid-engagement?

**This is the existential risk.** Fora is a venture-backed business (raised in 2022, growth-mode). It changes terms. Hosts have historically changed splits, introduced platform fees, restricted advisor-charged services, or "harmonized" pricing across their advisor base. The founder is not Fora's only advisor charging a membership. Fora has product-strategy reasons to want a piece of any membership a hosted advisor builds.

**Exit cost if Fora changes:** the founder cannot simply walk. Fora holds the IATA accreditation, the supplier relationships, the Virtuoso seat, and (critically) the booking history. Moving the book to another host (Brownell Catalyst $2,500 tuition, Andavo, Embark Beyond) means:
- 30–90 days of disruption
- Member-side re-onboarding (new booking platform, new email signatures, possibly new advisor-of-record paperwork)
- Loss of Fora's specific supplier amenity packages on in-flight bookings
- Possible non-compete or no-solicit terms in the Fora hosting agreement

**Founder must verify before launch:**
1. Fora's written stance on advisor-collected membership fees (100% to advisor, or shared).
2. The contractual term (1-year auto-renew, 3-year, evergreen?).
3. Termination clauses (notice period, book-portability rules).
4. Any "platform fee" or "tech fee" Fora reserves the right to assess on advisor businesses above $X in revenue.
5. Whether Fora restricts the advisor from operating under their own brand (Latitude 43 vs. "X at Fora").

### C.3 Investor recommendation

**Get this in writing within 30 days of launch.** A short LOI-style email from Fora's advisor success team — "We confirm that membership subscription fees collected by [Founder] from Latitude 43 members are not subject to the standard advisor/host commission split" — is the cheapest possible insurance. Without it, every dollar of subscription is at risk of being reclaimed.

If Fora declines to confirm in writing, **the founder has a binary decision**: stay at Fora and accept that subscription policy is undefined (and assume Fora will eventually claim its cut), or move to a host that confirms it in writing. Brownell Catalyst, Andavo, and Embark are reasonable alternatives to evaluate.

---

## D. Design Fee Escalator — Is It Priced Right?

### D.1 Effective hourly rate by trip band

Restating the v2.0 escalator from `/tmp/v2-facts.md`:
- $0 under $5K
- $250 base + $50/$1K from $5K–$15K
- $750 base + $75/$1K from $15K–$30K
- $1,875 base + $100/$1K above $30K
- Capped at $5,000/trip
- Members pay 50%

**Hour assumptions for a complex trip (intake + research + book + reconfirm + IROP handling):**
- $5K trip: simple — 2.5–4 hours
- $10K trip: moderate — 4–6 hours
- $20K trip: complex international — 8–12 hours
- $30K trip: multi-leg with experiences — 12–18 hours
- $50K trip: family with private elements — 18–25 hours
- $100K trip: ultra-complex — 30–40 hours

**Effective hourly rate, non-member, at midpoint hour estimate:**

| Trip value | Design fee | Hours (midpoint) | $/hr |
|---:|---:|---:|---:|
| $5,000 | $250 | 3 | **$83** |
| $7,500 | $375 | 4 | **$94** |
| $10,000 | $500 | 5 | **$100** |
| $15,000 | $750 | 7 | **$107** |
| $20,000 | $1,125 | 10 | **$113** |
| $30,000 | $1,875 | 15 | **$125** |
| $50,000 | $3,875 | 22 | **$176** |
| $75,000 | $5,000 (capped) | 30 | **$167** |
| $100,000 | $5,000 (capped) | 35 | **$143** |

**Effective hourly rate, member (50% off):**

| Trip value | Design fee (member) | Hours | $/hr |
|---:|---:|---:|---:|
| $5,000 | $125 | 3 | **$42** |
| $10,000 | $250 | 5 | **$50** |
| $15,000 | $375 | 7 | **$54** |
| $30,000 | $938 | 15 | **$63** |
| $50,000 | $1,938 | 22 | **$88** |

### D.2 Comparison to adjacent benchmarks

| Comp | Floor | Effective $/hr at similar trip |
|---|---:|---:|
| SmartFlyer | $500 floor | $125–$167 at $5K trip (3–4 hrs) |
| Bell & Bly | $800/week | $200/hr at 4-hr-per-day pace |
| Fora typical advisor | ~$350/week-of-travel | $87/hr at 4-hr days |
| Independent advisor avg (industry) | varies | $150–$300/hr aspirational |
| Fractional CFO / Chief of Staff | n/a retainer | $200–$400/hr loaded |
| **v2.0 non-member rates** | **$250 at $5K** | **$83–$176** |
| **v2.0 member rates** | **$125 at $5K** | **$42–$88** |

**The brutal finding:**
- v2.0 non-member rates underprice the $5K–$15K band relative to SmartFlyer's $500 floor.
- v2.0 member rates are *labor-losses* on every trip under $30K. Member trips between $5K and $30K (the *bulk* of business travel) earn the founder $42–$63/hr — barely above Toronto minimum wage when fully loaded.
- The $5K cap on a $100K trip means the founder is effectively giving a volume discount to the largest, highest-status trips. That is the wrong direction. The high-end buyer is the *least* price-sensitive; capping the fee at $5K leaves $5K–$10K of recoverable design revenue on the table at the $75K–$100K trip band.

### D.3 The cap problem

A capped escalator at $5K means:
- $40K trip → $2,875 fee
- $60K trip → $4,875 fee
- $80K trip → $5,000 (cap hit)
- $100K trip → $5,000 (cap)
- $200K trip → $5,000 (cap)

**The cap is a 12% effective fee at $40K and a 2.5% effective fee at $200K.** For a buyer at the $200K trip band, paying 2.5% to a travel advisor *is normal* (Indagare-style firms charge similar). The cap is therefore not protecting the buyer from "feeling overcharged" — it is simply leaving founder revenue on the floor.

### D.4 Investor recommendation on design fees

1. **Move the $5K floor up.** Non-members pay $500 minimum starting at $5K, scaling to $750 at $10K. This puts v2.0 in line with SmartFlyer.
2. **Drop the 50% member discount to 25%.** Members at 50% off are creating the structurally inverted incentive flagged by the stress-test — heaviest users generate lowest per-trip revenue.
3. **Remove the cap above $75K.** Above that band, the design fee is a non-issue to the buyer and meaningful to the founder.
4. **Add a $1,500 design fee floor for "rush" work** (under 14 days from departure). This is industry standard (Bell & Bly's 50% rush surcharge precedent) and prices in the actual scarcity cost of last-minute work.

---

## E. First Loss Insurance — Economic Exposure

### E.1 The exposure math

Stated policy (`/tmp/v2-facts.md`):
- $1K labor cap per incident
- One named trip per member per membership year
- Declared on sales call

**Worst-case math:**

| Membership tier | Y1 members | Named trips eligible | Cap/incident | Total exposure |
|---|---:|---:|---:|---:|
| Atlas Light | 22 | 22 | $1,000 | $22,000 |
| Atlas Office | 8 | 8 | $1,000 | $8,000 |
| Society (Y1: 0) | 0 | 0 | — | $0 |
| **Y1 total** | **30** | **30** | — | **$30,000** |

If all 30 Y1 members invoke First Loss Insurance on their named trip, exposure is $30K — roughly **38% of Y1 revenue**.

### E.2 Probability of invocation

This is where v2.0's positioning works *against* the founder's First Loss exposure.

`/tmp/v2-facts.md` lines 128–131 identify "the support-call black hole" as **the dominant pain point** in buyer research. The whole pitch is built around the proposition that travel breaks, and Latitude is the firm that catches it. Buyer research says **89% of business travelers were disrupted in 2025, losing 4h45m and $1,726 per disrupted trip**.

If 89% of business travelers are disrupted, and First Loss Insurance triggers on a "labor-intensive recovery" (interpreted loosely), then the actual invocation rate on the *named trip* could be **30–50%, not 5%**.

**Revised exposure under realistic invocation:**

| Invocation rate | Y1 incidents | Total cost |
|---|---:|---:|
| 5% (optimistic) | 1.5 | $1,500 |
| 15% (sober) | 4.5 | $4,500 |
| 30% (realistic given buyer research) | 9 | $9,000 |
| 50% (pessimistic) | 15 | $15,000 |
| 100% (worst case) | 30 | $30,000 |

A more honest central case: **$5K–$10K of First Loss exposure in Y1**, or 6–13% of Y1 revenue.

### E.3 Is it priced into the membership fee?

**It is not, explicitly.** The v2.0 per-member economics in `/tmp/v2-facts.md` list:
- Subscription (100%)
- Hotel commission
- Personal travel commission
- Design fees (member rate)

No line for "First Loss accrual" or "loss provision." This means the labor cost of First Loss is *implicit* in the founder's time — every hour the founder spends recovering a member's botched trip under First Loss is an hour not earning commission elsewhere. At the founder's blended hourly rate of ~$150–$200/hr (estimated), a $1K labor cap is 5–7 hours of work — which is a lot of compensation-free hours per incident.

### E.4 Investor recommendation on First Loss

1. **Cap the policy at 1 incident per member per *lifetime of membership*, not per year.** "Named trip declared on sales call" is good. Re-declaring it every year is a slow bleed.
2. **Add a $250 deductible / co-pay.** Symbolic but reduces frivolous invocation.
3. **Price-in a First Loss accrual** of $50/member/year explicitly into the Light tier and $100/member/year into Office. That's $1,100 + $800 = $1,900 in Y1 to fund expected losses. (This effectively raises the Light price by $4/mo and Office by $8/mo — undetectable to the buyer.)
4. **Publish the conditions narrowly.** "Labor-intensive recovery of a documented IROP" is different from "the hotel was disappointing." Define the trigger to avoid scope creep.

---

## F. The First 30 Program — Refund Exposure

### F.1 90-day no-fault refund on annual prorated

**Stated policy:** Monthly Stripe billing, 90-day no-fault exit (`/tmp/v2-facts.md` line 85).

**Industry refund-rate benchmarks:**
- Consumer subscriptions in early days: 15–30% cancel within 90 days (Recurly + general SaaS data).
- B2B SaaS: 5–15% cancel within trial windows.
- Premium memberships (Soho House, Velocity Black): churn is concentrated at *renewal*, not within the trial.

**Y1 refund exposure scenarios:**

If 30 members sign in Y1 and 20% cancel within 90 days:
- 6 members cancel
- Average refund liability: if cancellation happens at day 60 of a 90-day window, founder has collected 2 months of billing
- Refund exposure on Light: 6 cancellations × ~$200 (2 months at $99) = effectively zero refund liability since monthly Stripe billing means **the founder only collected what was already earned**

**This is the key insight:** v2.0's monthly Stripe billing structurally limits refund exposure. The "90-day no-fault" reads dangerous on paper but is mostly a *churn risk*, not a *refund risk*. The founder loses *future* revenue, not *collected* revenue.

### F.2 The actual exposure: revenue cliff, not refund

| Scenario | Y1 close rate | 90-day cancellation rate | Members at end of Y1 |
|---|---:|---:|---:|
| Plan | 30 closes | 0% | 30 |
| Sober | 30 closes | 15% | 25.5 |
| Realistic | 30 closes | 25% | 22.5 |
| Pessimistic | 30 closes | 40% | 18 |

At 25% 90-day cancellation:
- 22 Light × $1,188 + 8 Office × $2,988 = $26,136 + $23,904 = **$50,040 of modeled subscription** → reduced to $37,530
- **~$12,500 revenue evaporation** vs. plan in Y1 subscription line.

**Cash flow implication:** Y1's plan is ~$80K total. Losing $12.5K of subscription is a 15% revenue haircut. Manageable. But it compounds:
- Year 2 starts with 22.5 members, not 30
- The Y2 model needs to ADD 13–18 new closes just to reach the modeled 35+15+1 = 51 members
- Each lost early-Y1 member is a lost referral source for Y2

### F.3 Investor recommendation on First 30

1. **Keep the 90-day no-fault.** It is genuinely a sales accelerator (removes the buyer's "what if I hate it" objection) and the structural refund risk is minimal under monthly billing.
2. **Track 90-day churn as a leading indicator**. If 90-day cancellations exceed 20%, the product-market fit is weaker than the plan assumes, and Y2 forecasts need adjustment.
3. **Add a "honest reason for leaving" exit interview** — not for retention but for product learning. Refunds should be voluntary information transactions.

---

## G. Society Tier Launch Economics

### G.1 Restated unit economics at scale

`/tmp/v2-facts.md` models Y5 base case at 60 Light + 40 Office + 20 Society. Let's stress the Society line specifically at the modeled 20 members, $14K average:

| Line | Annual per Society member | × 20 |
|---|---:|---:|
| Subscription (100%, avg) | $14,000 | $280,000 |
| Hotel commission (4 travelers × 25 nights × $750 × 10% × 70%) | $5,250 | $105,000 |
| Personal/leisure commission | $2,100 | $42,000 |
| Event design fees (mid-range $15K) | $15,000 | $300,000 |
| **Per-member Y5 revenue** | **$36,350** | **$727,000** |

The 30-member full-launch scenario from the brief:
- 30 × $14K = $420K subscription
- Plus design + commission of approximately +$360K
- **Total Society contribution at 30 members: ~$780K**

### G.2 The 1:6 service ratio cost

If Society runs at 1:6 advisor-to-member as v2.0 specifies, **30 members require 5 advisors**. Per the lifestyle-memberships research, a Knightsbridge-grade dedicated personal manager costs $80K–$120K loaded (US/Canada salary + benefits + tools). Five advisors = **$400K–$600K in labor**.

**Net Society contribution at 30 members and 5 advisors:**

| Line | $ |
|---|---:|
| Society revenue | $780,000 |
| 5 advisor salaries (loaded, avg $90K) | $(450,000) |
| Society-specific marketing/events | $(50,000) |
| Hotel GM partnerships and amenity buy-ups | $(30,000) |
| Founder time (allocated 30% to Society oversight) | $(60,000) |
| **Net Society contribution at 30 members** | **~$190,000** |

This is materially worse than the prompt's $380K estimate. The reason: the 1:6 service ratio at the price band Latitude is targeting is **structurally unprofitable** unless the average Society price is $20K+ (not $14K).

### G.3 Alternative Society configurations

| Config | Avg price | Members | Service ratio | Advisors | Net contribution |
|---|---:|---:|---:|---:|---:|
| As planned | $14K | 30 | 1:6 | 5 | ~$190K |
| Higher price | $20K | 30 | 1:6 | 5 | ~$370K |
| Tighter cap | $14K | 18 | 1:6 | 3 | ~$210K |
| Knightsbridge-grade | $25K | 12 | 1:4 | 3 | ~$235K |

**The Knightsbridge-grade configuration is the most defensible:** 12 members at $25K with a 1:4 ratio is a true private-relationship product. It generates similar net contribution at *less than half the service-delivery burden*. v2.0's plan of 20 Society members at $14K average is a worst-of-both-worlds choice: priced like a mid-tier product, marketed like a top-tier product.

### G.4 Investor recommendation on Society

1. **Cap Society at 12–15 members in Y5, not 20.** Smaller is the brand promise. 30 was always aspirational.
2. **Raise the modal price to $20K** (band: $1,500–$2,500/mo). The current $14K average is below the credible band.
3. **Defer the Society launch to Y3 (mid-2027), not Q1 2027.** Y2 should be spent building the case-study stack from Office members.
4. **Hire one advisor by Y3, two by Y4, not five.** Society must scale with proven members, not modeled ones.

---

## H. Pricing Under Different ICP Scenarios

### H.1 100% Atlas Light at $99 — does the model work?

**Math:** 200 members × $1,188 = $237,600 subscription.

Per-member commission/design revenue from `/tmp/v2-facts.md` Y3+ economics: ~$1,500/member. So 200 × $1,500 = $300K commission/design.

**Total: $537K revenue.**

Labor: 200 members × ~25 hours/year (avg, including support) = 5,000 hours = 100 hours/week. **Impossible solo.** Requires 2 FTE coordinators at $75K loaded = $150K opex.

**Net: $537K − $150K − $60K other opex = $327K to founder.**

This is *not bad*. But it requires the founder to hire and manage two coordinators by Y3. That's a real operational pivot from "solo practice" to "small team."

**Risk:** The $99 product attracts the worst adverse-selection profile (heavy travelers who get half-off design fees on every trip). At 200 Light members, churn alone (8% annual) means losing 16 members/year = $19K cliff, requiring constant net-new acquisition.

### H.2 100% UHNW principals at Society — does the model work?

**Math:** 30 members × $20K (raising the average from $14K to a credible level) = $600K subscription.

Per-member commission/design: ~$15K. So 30 × $15K = $450K.

**Total: $1.05M revenue.**

Labor: 1:5 service ratio = 6 advisors. 6 × $100K loaded = $600K opex.

**Net: $1.05M − $600K − $100K other opex = $350K to founder.**

Comparable net to the 100% Light scenario at far higher revenue and much more brand prestige. The downside is fragility: losing 3 of 30 members is 10% revenue loss in one event.

**Risk:** Y1 sales cycle to get 30 Society members is impossible. Even at 1 close per quarter (aggressive for a $20K product with no track record), reaching 30 takes 7.5 years.

### H.3 Mixed Atlas + Society — the actual realistic mix

This is what the v2.0 plan models. Restated at Y5 base:

| Tier | Members | Revenue/member | Total |
|---|---:|---:|---:|
| Light | 60 | $3,100 | $186,000 |
| Office | 40 | $7,600 | $304,000 |
| Society | 20 | $36,350 | $727,000 |
| **Total** | **120** | — | **~$1,217K (revenue)** |

(Note: v2.0 models Y5 at $871K total. The $1.2M above implies the v2.0 model may be conservative — or the Society modeling at $20K average is more generous than v2.0 actually plans.)

**Labor:** Light + Office at 100 members ≈ 50–60 hours/week solo founder (still over-capacity). Add 1 coordinator. Society needs 3–4 advisors. Total opex from labor: $300K–$400K.

**Net: $1.2M − $400K labor − $100K other opex = $700K to founder.**

This is the bull case. The base case ($871K total revenue per v2.0) implies ~$400–500K net, which is the right number for a 5-year-mature solo founder business with one coordinator and 2–3 contract advisors.

### H.4 The ICP-mix verdict

The mixed Atlas + Society model is the right answer **provided Society is deferred to Y3 and the mix doesn't depend on Society to clear Y1–Y2**. The v2.0 plan's Y2 numbers (35L + 15O + 1S) are sensible — Society stays at 0 or 1 in Y2. Where the plan strains is Y3 (50L + 25O + 5S) — that's the year where the founder needs Society credibility, which means Y2 needs to be spent building the case studies that justify $20K+ pricing in Y3.

---

## I. Verdict — Is v2.0 Pricing Sustainable for a Solo Founder Y1–Y3?

### I.1 Y1 (2026)

**Yes, viable.** The founder needs 30 members to hit ~$80K. The membership mix (22L + 8O) is achievable through warm/referral if the brother-in-law network + Soho House Toronto + EO + the anchor close all deliver.

The $99 Light price is wrong but not fatal in Y1 — the absolute member count is small enough that the founder can compensate for adverse selection through personal triage.

The 70/30 split is endured but the $300K personal sales threshold is plausibly met if the mix lands.

**Y1 break risk: missing the close on the warm anchor.** Without the anchor's Office account, the Y1 plan loses ~$8K of subscription and ~$10K of commission. Now revenue is $60K. That's tight but survivable.

### I.2 Y2 (2027)

**Marginally viable.** The plan adds 13–20 net new members (depending on Y1 churn). Cold outreach is starting to pay because Y1 produced 2–3 case studies. The 80/20 split has kicked in.

Society at 1 member is the right call. The deferred launch is the right call.

**Y2 break risk: Atlas Light churn.** If Light churn hits 25–35% (consumer subscription baseline), the founder is constantly running a treadmill of acquisition just to stay flat. This is the year where the $99 price becomes a tax: the wrong members are easier to acquire but harder to retain.

### I.3 Y3 (2028) — the inflection point

**This is where v2.0 breaks first.**

Y3 plan: 50L + 25O + 5S = 80 members. Revenue ~$353K.

Three things must simultaneously be true for Y3 to land:
1. Light churn must be ≤15% (better than industry baseline).
2. Office must double from 15 to 25 — requires sales beyond the founder's warm network.
3. Society at 5 members must launch and close — requires brand credibility the founder may or may not have built.

The founder is also at labor saturation. 80 members × varying loads = ~80–100 hours/week of trip execution + sales + content. **The plan needs the first coordinator hire in Y3.** That's $75K loaded, eating $75K of the $353K revenue and revealing the founder netting closer to $150K, not the implied $250K.

**Y3 break risk: founder labor + Society credibility, simultaneously.** This is the year where the plan most plausibly fails as written.

### I.4 Where does v2.0 break first?

In order of likelihood:

1. **Y3 founder-labor ceiling** — the math says 80 members at the v2.0 service promise is more than one person can deliver, full stop.
2. **Society launch credibility** — the founder needs to manufacture in Y2 the brand equity Knightsbridge built over a decade. Probable failure mode: Society launches but closes only 1–2 members in Y3, not 5.
3. **Light tier adverse selection** — the $99 price attracts the wrong members and the design-fee escalator can't fully backfill the labor.
4. **Fora subscription policy change** — the load-bearing 100% assumption gets challenged, and the founder discovers the membership fee is split.
5. **First Loss Insurance invocation rate** — higher than the founder modeled because the whole pitch is "we catch disruption."

### I.5 What should the founder change before launch?

The 10 specific fixes are in Section J. The headline three:
1. **Reprice or reposition Atlas Light.** Either lift to $199 or strip it to content + AI + per-trip booking.
2. **Lock the Fora subscription policy in writing.** Pre-launch. No exceptions.
3. **Defer Society to Y3+ explicitly in the plan.** Y2 is too aggressive.

---

## J. 10 Specific Pricing Fixes

### Fix 1 — Reprice Atlas Light from $99 to $149 or $199

Move out of the dead zone ($99–$150 has no comp). $149 lands in Indagare Custom's neighborhood ($238). $199 sits at the floor of the credible-human-relationship band. Either signals seriousness. $99 signals "I'm cheaper than Soho House because I'm not Soho House."

### Fix 2 — Drop the member design-fee discount from 50% to 25%

The 50% discount actively destroys the most-monetizable users. 25% is plenty of psychological gift and protects margin on the heaviest trippers.

### Fix 3 — Raise the design-fee floor from $5K to $7.5K with a $500 minimum

A $250 design fee at a $5K trip is $83/hr — below labor cost. Raise the floor to $500 minimum and start the escalator at $7.5K trip value. SmartFlyer's $500 floor is the right anchor.

### Fix 4 — Remove the $5K design-fee cap above $75K trip value

Cap to $5K up to $75K. Above $75K, charge $50/$1K incrementally. A $100K trip should pay $6,250, not $5,000. The buyer doesn't care; the founder pays rent.

### Fix 5 — Reposition Atlas Office travelers as "up to 3 active, 5 named roster"

The "up to 5 travelers" promise is unbounded labor risk. Reframe as: up to 5 named travelers on the account, of whom no more than 3 may have active booking authority at any time. This caps labor.

### Fix 6 — Raise Society's modal price to $20K and shrink cap to 15

$14K average is below the credible Society band. $20K with a 15-member cap is a stronger brand promise and a better unit economic. 12–15 members at 1:4 ratio is achievable solo + one contract advisor by Y4.

### Fix 7 — Charge a $1,500 Society induction fee at launch

Knightsbridge has no induction; Soho House does (~50% of annual). The induction fee both funds the first-90-days onboarding labor and signals price seriousness. Refundable in the first 30 days; non-refundable after.

### Fix 8 — Lock the Fora subscription policy in writing within 30 days

Single highest-leverage action. Without it, every subscription dollar is at risk. Email Fora's advisor success team. Get the policy in writing. File it.

### Fix 9 — Defer Latitude Society to Y3 (H2 2027), not Q1 2027

Y2 should be dedicated to Office expansion and case-study production. Society launches when the founder has 3 named Office case studies, one published founder long-form interview, and two named hotel GM partnerships. Not before.

### Fix 10 — Add a $50/member/year First Loss accrual into Light pricing and $100/member/year into Office

This costs the buyer $4/mo (Light) or $8/mo (Office). It is undetectable but accumulates a $2K–$3K loss reserve in Y1. Without it, every First Loss invocation comes directly out of founder hours.

---

## Appendix — Side-by-side: v2.0 as written vs. v2.0 with the 10 fixes

| Variable | v2.0 as written | v2.0 with fixes |
|---|---|---|
| Atlas Light price | $99/mo | $149/mo or $199/mo |
| Member design discount | 50% | 25% |
| Design fee floor | $250 at $5K | $500 at $7.5K |
| Design fee cap | $5K | $5K to $75K, then $50/$1K |
| Office active-traveler cap | "Up to 5" (unbounded) | "Up to 3 active, 5 named" |
| Society average price | $14K | $20K |
| Society member cap | 30 | 15 |
| Society induction fee | $0 | $1,500 |
| Fora subscription policy | Assumed 100% | Confirmed in writing |
| Society launch | Q1 2027 | H2 2027 (Y3) |
| First Loss funding | Implicit | $50/Light, $100/Office accrual |

**Estimated impact on Y5 economics:**

| Metric | v2.0 base case | v2.0 with fixes |
|---|---:|---:|
| Y5 total revenue | $871K | ~$950K–$1.05M |
| Y5 net to founder | ~$450K (implied) | ~$550K–$650K |
| Y3 break risk | Moderate–high | Moderate |
| Society launch year | 2027 | 2028 |
| Founder labor saturation year | Y3 | Y4 |

The fixes raise net by approximately $100–200K at Y5, delay Society by 12 months (which protects the brand), and meaningfully reduce the risk that v2.0 breaks at the Y3 inflection.

---

## Final Investor Note

The v2.0 pricing model is what most founders propose after their first stress-test: visibly improved, marginally more defensible, but still carrying the original instincts toward under-pricing that the stress-test was supposed to correct. The Atlas Light $99 price is the tell — it is the founder's discomfort with charging more, dressed up with a new tier name.

**The good news**: the v2.0 structure (100% subscription retention, tiered Fora commission, deferred Society) is architecturally sound. With the 10 fixes above, this is a survivable, possibly thriving solo practice that can clear $500K+ net by Y5.

**The bad news**: every fix listed requires the founder to charge more and promise less. The pre-launch test of whether v2.0 will succeed is not whether the plan works on paper. It is whether the founder, sitting across from a real prospect in a real Toronto coffee shop in Q3 2026, can quote $199/mo with a straight face. If they can, the business has a chance. If they reflexively quote $99 because "$199 feels like a lot to ask," v2.0 will end up exactly where v1.0 ended — a structurally underpriced service whose founder works too many hours for too little money.

Price is the founder's first and most honest signal of what they think their work is worth. v2.0 underprices in two of three tiers. Fix that, and there is a business here.

---

*Document length: approximately 6,200 words. Sources: `/tmp/v2-facts.md`, `research/pricing-stress-test.md`, `research/adjacent-lifestyle-memberships.md`, `research/adjacent-card-concierges.md`.*
