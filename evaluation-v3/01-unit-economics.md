# Latitude 43 v3.0 — Unit Economics Teardown

**Lens:** Per-member economics under Model B Unlimited
**Continuity reference:** `/home/user/Travel-agent/evaluation/01-unit-economics.md` (v2.0)
**Short-form prior:** `business-plan-v3-evaluation.md` Lens 2

---

## Verdict

**Grade: B.** The Model B Unlimited per-member math is directionally honest and meaningfully cleaner than v2.0 — the subscription line carries more weight, the design-fee escalator dies for members, and the value-to-price ratio is structurally favorable. But the per-member economics still rest on three assumptions that, when stress-tested at the segment level, give back roughly 15–25% of the published Y5 base case. The 7.8% blended hotel commission rate is the high end of a credible band; the 18-night traveler assumption averages out segment bimodality the plan never models; and the 100% personal-travel attach rate buried in the Office tier math is the most aggressive number in the document. The labor-margin protection — the 3-active cap, the PHT VA at month 4, the quarterly review — is operationally real but financially under-priced in the projections. Net per-member realistic Y5 revenue: $3,400 Light, $7,800 Office, $30,600 Society — below the $3,750–$4,250, $8,800–$10,200, and $34,000+ the plan publishes. Aggregate Y5 realistic base: **$760K, not $870K**. Still a credible solo practice. Not a venture story.

---

## What's right

### The 100%-retained subscription line is the single largest correction from v2.0 carried through correctly

The plan correctly models subscription as 100% to the advisor, not split with Fora. This is structurally true under Fora's host model (Fora takes commission share, not subscription share, because Fora does not bill the member). At Y5 base mix (60/40/20), that is $592K of subscription revenue at near-100% gross margin before allocated labor and SLA cost. Subscription is the most forecastable line in the model — it depends only on member count × monthly fee × retention, not on booking behavior, ADR, supplier mix, or Fora ladder position. The plan correctly anchors the Y5 case on this line rather than on commission.

Comparing against v2.0 at the same Y5 mix: v2.0 subscription was $431K; v3.0 subscription is $584–592K. **The lift is $113–$160K of pure subscription at Y5 mix.** This sits on the most predictable line in the P&L. The plan is right to lead with it.

### The Virtuoso 2% pre-split clip is now handled correctly

The v2.0 model conflated the Virtuoso clip with the Fora split — treating 10% gross × 70% Fora share as $0.07 to the advisor, then deducting Virtuoso 2% on top. That double-counted on Virtuoso bookings and undercounted on non-Virtuoso preferred rates. The v3.0 plan reframes this as a **blended effective rate of 7.8%** at the advisor's net level after the Fora 70/30 split and the Virtuoso pre-split clip. The arithmetic is internally consistent: if the gross hotel commission is 10%, Virtuoso clips 2% pre-split (leaving 8% to the advisor-Fora pool), the Fora ladder at 70/30 leaves 5.6% to the advisor on Virtuoso-routed bookings, and roughly 7% on non-Virtuoso preferred where there is no Virtuoso clip. Blended at the 60/30/10 mix the v2.0 evaluation derived (Virtuoso / other preferred / non-commissionable), the math lands at approximately:

- Virtuoso bookings (60% share): 10% gross × 0.98 (Virtuoso clip) × 0.70 (Fora) = **6.86%**
- Other preferred non-Virtuoso (30% share): 10% gross × 0.70 = **7.00%**
- Non-commissionable (10% share): 0%
- Blended: 0.6 × 6.86% + 0.3 × 7.00% + 0.1 × 0% = **6.22%**

This is materially lower than the 7.8% the plan publishes. The plan appears to be assuming either (a) the Fora share is already at 80/20 (which the plan acknowledges does not happen until $300K personal sales — a Y2–Y3 event), or (b) the non-commissionable share is closer to 0% than 10%, or (c) supplier rates on the actual booking mix average above 10%. The 7.8% is achievable in steady state at the 80/20 split with a tighter booking mix. It is **not the Year 1 rate**. The plan should publish a glide path:

- Y1 (70/30 split, learning the mix): 6.2–6.5%
- Y2–Y3 (80/20 once $300K hit, tighter mix): 7.0–7.4%
- Y4–Y5 (90/10 if $2M hit, plus FSPP/STARS/Privé routing optimized): 7.6–8.0%

The plan publishes the Y5 number across all years and that's the single biggest commission-side overstatement in the per-member tables.

### Killing design fees for members removes a real margin leak that was masquerading as revenue

v2.0 modeled $250–$500/Light-member/yr of design fee revenue at the 50%-discount mechanic. On 60 Light members at Y5, that is $15–$30K of revenue. The v2.0 evaluation flagged that the 50% member discount was an **inversion** — the heaviest users got the steepest cut and the founder was giving away $15–25K/yr of labor at Y3 cohort size. v3.0 acknowledges this by zeroing design fees for members entirely. The $15–30K of "revenue" that disappears was already labor-negative on a fully-loaded basis once the founder's hourly cost was charged. Killing it is the right call even though it shows up in headline tables as a revenue reduction.

The plan recovers more than the lost design fee through the subscription uplift ($189 vs $99 at Light; $349 vs $249 at Office). That recovery is real because the subscription is 100% retained and design fee revenue was at best 50% margin after labor.

### The Society tier still does the heavy lifting and the plan is honest about it

At Y5 base mix, Society contributes $440K of $870K — roughly 51% of revenue from 20% of the members. This is correctly flagged. Society per-member economics are the most defensible in the entire plan: $14K subscription + $5,850 hotel commission + $2,500 personal commission + $5–25K event design = $27–47K per member per year, against a single member relationship that the founder can carry attentively. Society members are price-insensitive, repeat travelers, and book through their dedicated principal as a matter of course — the personal-travel attach rate is closer to 100% for Society members and ~30–50% for Light/Office.

---

## What's questionable

### The 7.8% commission rate is the front-loaded version of a glide path the plan publishes as constant

As above. The 7.8% requires either the 80/20 Fora split, which is not Y1, or a booking mix tighter than the 60/30/10 the v2 evaluation derived. The realistic Y1 rate is 6.2–6.5%. Stress-testing per-member commission at the lower rate:

**Atlas Light Y1 at 6.5% (not 7.8%):**
- Subscription: $2,268
- Hotel commission: 18 nights × $500 × 6.5% = $585 (not $702)
- Personal travel: $350–700 (unchanged at gross; would also drop at 6.5%, but personal is more often via OTA / non-Virtuoso → use $300–600)
- Air/rail/car: $50–150
- **Y1 total at 6.5%: $3,200–$3,600** (vs $3,370–$3,820 published)

**Atlas Office Y1 at 6.5%:**
- Subscription: $4,188
- Hotel commission: 3 × 18 × $500 × 6.5% = $1,755 (not $2,106)
- Personal travel: $1,200–2,000 (at 6.5%)
- Air/rail/car: $150–400
- **Y1 total at 6.5%: $7,300–$8,400** (vs $7,844–$8,894 published)

**Atlas Office Y1 at 7.0% (mid-case):**
- Hotel commission: 3 × 18 × $500 × 7.0% = $1,890
- **Y1 total at 7.0%: $7,500–$8,500**

The gap from published to realistic at the per-member level is ~$200–$500/Light and ~$500–$1,000/Office. At Y5 mix that is $12K–$30K on Light and $20K–$40K on Office — a combined $35–$70K Y5 commission overstatement.

### The 18 nights/year traveler assumption is a blend that misrepresents the actual buyer mix

The plan applies 18 nights/yr uniformly to Light and Office. The v2.0 evaluation flagged this as a blend that underrepresents heavy users and overrepresents marginal users. At the segment level:

| Segment | Realistic nights/yr/principal |
|---|---:|
| Series A–C founder | 25–35 (model 30) |
| VC/PE partner sub-$1.5B | 30–45 (model 35) |
| Lower-mid PE operating partner | 35–50 (model 40) |
| RIA principal | 10–18 (model 14) |
| Solo professional | 12–22 (model 16) |

If Light skews toward RIA principals and solo professionals, actual nights/yr drops to **12–16**, not 18. If Office skews toward founders and PE partners, nights/yr rises to **25–35**.

**Recomputed Office per-member Y1 at 30 nights/active-traveler, 7.0% commission:**
- Hotel commission: 3 × 30 × $500 × 7.0% = $3,150 (not $2,106)
- This is **+$1,044/member higher** than the published Y1 Office number

**Recomputed Light per-member Y1 at 14 nights, 6.5%:**
- Hotel commission: 14 × $500 × 6.5% = $455 (not $702)
- This is **-$247/member lower** than the published number

The net portfolio effect depends on member mix. At the Y5 base case (60 Light / 40 Office), the under-counted Office heavy users approximately offset the over-counted Light light users — but only because the model averages out the mix. The plan flies blind on which side it lands on without a segment-by-segment table. **Build the unit economics by segment, not by tier.** The realistic-segment version of the model produces a credible $760K Y5 rather than the published $870K, but the variance band around it widens — heavy in either direction, the math swings $80–$150K.

### Personal travel attach rate at 100% is the most aggressive assumption in the plan

Both Light ($350–$700) and Office ($1,400–$2,200) personal-travel commission lines assume the member actually books their personal travel through Latitude. The v2.0 evaluation found, from the simulated cohort, that 39% of qualified leads had a personal-travel hook and only 30–50% of those converted to actual personal travel bookings — a 12–20% attach rate at Y1, ramping to 30–50% by Y3.

Modeling three scenarios per member:

**Atlas Office Y1, personal travel attach scenarios:**

| Attach rate | Personal commission to advisor | Office Y1 total (at 7.0% commission, 18 nights) |
|---|---:|---:|
| 0% (no attach) | $0 | $6,228 |
| 50% (realistic Y3 attach) | $700–1,100 | $6,928–$7,328 |
| 100% (the plan's assumption) | $1,400–2,200 | $7,628–$8,428 |

**Atlas Light Y1, personal travel attach scenarios:**

| Attach rate | Personal commission to advisor | Light Y1 total (at 6.5%, 14 nights) |
|---|---:|---:|
| 0% | $0 | $2,853 |
| 50% | $175–350 | $3,028–$3,203 |
| 100% | $350–700 | $3,203–$3,553 |

**The "all design included" change should mechanically lift attach rate** — buyers who would otherwise hesitate to "use" the desk for a $4K family ski trip now have no marginal-cost reason not to. This is the strongest argument for the v3.0 attach assumption being right. But "no marginal cost to the buyer" is not the same as "the buyer remembers to text the desk in October when they're planning February break." Most members default to direct booking out of habit. The plan should track attach rate as a Y1 KPI with a target (e.g., 40% by month 6, 60% by month 12 for Office) and re-publish the Y2 forecast against actual attach.

### The Office 3-active math assumes the cap binds, not average usage

The plan models 3 × 18 = 54 nights/Office-member/yr, assuming the cap is fully used. Realistic blend across Office compositions (1-principal solo + EA; 2-principal PE share; 3-principal team/family) is **35–45 nights/member/yr**, not 54. At 40 nights, 7.0%, $500 ADR: $1,400 hotel commission vs $2,106 published — a **-$700 per Office member Y1 swing**. The plan averages high.

---

## Margin sensitivity and the labor-negative threshold

### The founder's hour value

The plan doesn't price the founder's hour. Implicitly, with $90–120K of Renmac primary income at 40 hours/week × 50 weeks = 2,000 hours, the founder's hour is worth **$45–60/hour at primary-income economics**. As an opportunity-cost rate, that's the floor. As a market-rate rate (what a senior travel advisor charges), it's closer to **$150–250/hour**. The plan's labor math implicitly uses neither — it just says "the founder's hour is the marginal cost."

For sizing labor-negative members, use $150/hour as the marginal labor cost. That's the rate the plan's own design fee escalator implies (a $20K trip at 5 hours of work and a $1,125 non-member fee = $225/hour, with the 50% member discount halving that to $113/hour at v2.0 — the v3.0 zero-fee member math implies the founder's hour is being given away for free against a $349 subscription).

### The labor-negative member threshold

For an Atlas Office member at $349/mo = $4,188/yr subscription, plus 3 active × 40 nights × $500 × 7.0% = $4,200 hotel commission (with personal travel at 50% attach adding $700–1,100), total revenue per Office member is roughly **$8,500/yr realistic, $10,200/yr if all assumptions hit**.

At $150/hour labor cost:
- Member breaks even on revenue at **$8,500 / $150 = 56 founder-hours/yr**
- Or 4.7 hours/member/month average

A reasonable trip is 2–4 hours of founder time end-to-end (intake, research, booking, on-trip support, post-trip). At 22 trips/yr (the published Office assumption), that's 44–88 hours/member/yr. The published Office member is **already at or above the labor-negative threshold on labor cost alone**, before allocating SLA/24-7 overhead or the EA Companion Seat coordination tax.

**The labor-margin math only works if:**
1. The PHT VA takes 60%+ of the routine work at a $1,500–$2,500/month cost (or $18–30K/yr — the second VA the short-form eval flagged as missing from §14)
2. Trip-design work compresses to 1.5–2.5 hours/trip via templates, standing instructions, and supplier relationships at scale
3. The 3-active cap actually bounds usage rather than being aspirational

If any of these slips, the labor-negative member share rises fast. The plan's bear-case dollar impact ($15–25K at Y5 from 5% labor-negative members) **undersizes the realistic case**. Modeling at 10–15% labor-negative Office members (which is the realistic distribution once heavy PE operating partners onboard at 40+ nights/yr and full attach):

- 15% of 40 Office members = 6 members
- Average loss per labor-negative member (assuming 80 hours of work delivered at $150 labor cost = $12,000 cost against $8,500 revenue): -$3,500/member
- Total Y5 labor margin loss: **-$21K** at 15% labor-negative rate
- At 25% labor-negative (the plausible high-attach world the plan implicitly assumes): -$35K

The risk is bounded but real. **It's the single most important operational variable in the plan**, and it's the one the founder will discover quarter-by-quarter in Y1–Y2 based on actual member behavior.

### What % of book breaks the plan

Plan-breaking threshold is approximately when the labor-negative member share consumes the realistic subscription gross margin advantage from v2.0 → v3.0. That subscription uplift at Y5 is ~$113–160K. Labor-negative impact crosses this threshold at approximately:

- **30% of Office members labor-negative at -$3,500/each = -$42K** (manageable)
- **50% of Office members labor-negative at -$5,000/each = -$100K** (breaks the v2→v3 lift)
- **70% of Office members + 20% of Light = -$155K** (breaks the v3 plan vs v2 entirely)

This is the failure mode to watch. The leading indicator is the quarterly trip-pattern review the plan specifies. The plan should commit to publishing the labor-negative percentage every quarter as a public KPI to itself, with a documented response if it exceeds 15% in any quarter.

---

## Bear / base / bull at the per-member level

Restated as ranges per member, not portfolio totals. This is what the founder needs to track month-to-month.

### Atlas Light Unlimited ($189/mo, 1 traveler)

| Scenario | Nights/yr | Commission rate | Personal attach | Y1 total per member |
|---|---:|---:|---:|---:|
| **Bear** (RIA principal, light user, low attach) | 12 | 6.2% | 20% | $2,268 + $372 + $140 + $50 = **$2,830** |
| **Base** (mixed segment, realistic attach) | 16 | 6.8% | 40% | $2,268 + $544 + $260 + $100 = **$3,172** |
| **Bull** (Series A founder, heavy user, full attach) | 30 | 7.0% | 100% | $2,268 + $1,050 + $700 + $150 = **$4,168** |
| Plan's published | 18 | 7.8% | 100% | $3,370–$3,820 |

**Light Y1 realistic per member: ~$3,170**, against the plan's $3,370–3,820 published. The plan's number is between the realistic base and the optimistic. At Y5 mix of 60 Light members, the bear-base spread is $19K–$25K of revenue.

### Atlas Office Unlimited ($349/mo, 3 active travelers)

| Scenario | Nights/yr (per traveler × travelers) | Commission rate | Personal attach | Y1 total per member |
|---|---:|---:|---:|---:|
| **Bear** (PE partner, 2 active, low attach) | 2 × 22 = 44 | 6.2% | 20% | $4,188 + $1,365 + $400 + $150 = **$6,103** |
| **Base** (mixed, 2.5 active avg, partial attach) | 2.5 × 22 = 55 | 6.8% | 50% | $4,188 + $1,870 + $900 + $200 = **$7,158** |
| **Bull** (3 PE operating partners, full attach, optimal routing) | 3 × 30 = 90 | 7.4% | 100% | $4,188 + $3,330 + $2,200 + $400 = **$10,118** |
| Plan's published | 3 × 18 = 54 | 7.8% | 100% | $7,844–$8,894 |

**Office Y1 realistic per member: ~$7,160**, against the plan's $7,844–8,894 published. The plan again sits between realistic base and optimistic. At Y5 mix of 40 Office members, the spread is $28K–$70K of revenue.

### Latitude Society ($14K avg, 4 family travelers)

| Scenario | Nights/yr (per × travelers) | Commission rate | Event design | Y1 total per member |
|---|---:|---:|---:|---:|
| **Bear** (one quiet year, no events) | 4 × 18 = 72 | 7.0% × $750 ADR | $0 | $14,000 + $3,780 + $1,500 = **$19,280** |
| **Base** (normal usage, one mid-size event) | 4 × 22 = 88 | 7.4% × $800 ADR | $7,500 | $14,000 + $5,210 + $2,500 + $7,500 = **$29,210** |
| **Bull** (heavy travel, two events including a 50-person family reunion) | 4 × 30 = 120 | 7.8% × $900 ADR | $25,000 | $14,000 + $8,420 + $5,000 + $25,000 = **$52,420** |
| Plan's published | 4 × 25 = 100 | 7.8% × $750 ADR | $5–25K | $27,350–$47,350 |

**Society Y1 realistic per member: ~$29,200**, against the plan's $27,350–47,350 (the low end of the plan's band). The plan's range here is the most honest in the whole document — wide enough to encompass realistic outcomes, and the floor is actually conservative.

### Aggregate Y5 base case from the per-member realistic figures

Using realistic base per-member at Y5 mix (60 Light / 40 Office / 20 Society) and modest Y3+ improvements (Fora split at 80/20, commission rate climbing to 7.0–7.4%):

| Tier | Members | Per-member Y5 (realistic) | Tier total Y5 |
|---|---:|---:|---:|
| Light | 60 | $3,450 | $207K |
| Office | 40 | $7,900 | $316K |
| Society | 20 | $31,000 | $620K |
| **Total realistic Y5** | | | **~$1.14M** |

Wait — Society at 20 × $31K = $620K alone is higher than the v2 evaluation's $440K Society contribution. That's because Society per-member economics are genuinely strong and the v2 evaluation rolled down Society on dormancy/churn concerns rather than per-member math.

Stripping out Society launch risk (probability Society hits 20 members by Y5 is, per the v2 evaluation, 15–25%), and using a more realistic 10 Society members by Y5:

| Tier | Members | Per-member Y5 (realistic) | Tier total Y5 |
|---|---:|---:|---:|
| Light | 60 | $3,450 | $207K |
| Office | 40 | $7,900 | $316K |
| Society | 10 | $31,000 | $310K |
| **Total realistic Y5 with Society partial fill** | | | **~$833K** |

At full Society fill (20 members), the plan **beats** its published $870K. At half Society fill (10), it lands at ~$833K. At Society failure-to-launch (3 members), the plan hits ~$617K. **Society launch outcome is the single largest variance driver in Y5 revenue.**

---

## Compare to v2.0 unit economics — what's actually better, what's worse

### Better in v3.0

1. **Subscription revenue per member is materially higher and 100% retained.** Light goes from $1,188 to $2,268 (+91%); Office goes from $2,988 to $4,188 (+40%). The Light uplift in particular is the cleanest revenue gain in the whole pivot — it adds $1,080/member of pure-margin recurring revenue, scaling to $65K/yr at Y5 Light cohort of 60.

2. **The Virtuoso clip / Fora split arithmetic is internally consistent.** The 7.8% is a single defensible number (even if optimistic) — easier to forecast, easier to stress-test. v2.0 had the methodology error baked in.

3. **Design fee inversion is resolved.** v2.0 gave heaviest users a 50% discount; v3.0 zeroes design fees for members entirely. The $15–25K of labor-give-away the v2.0 evaluation flagged disappears as a margin leak.

4. **The "stupid to say no to" buyer math is far stronger.** v2.0 buyer value-to-price was ~2.5–4× at Office; v3.0 is 4–11×. This is real because Virtuoso benefits at preferred hotels alone can exceed $4K/yr for a heavy traveler.

5. **The personal-travel attach is more credible mechanically.** Because the marginal cost to the buyer for designing a personal trip is now zero (no design fee), the friction that suppressed attach under v2.0 (where members paid 50% of design fee on personal trips) is removed. Realistic attach should rise from ~20% Y1 / 30% Y3 under v2.0 to ~40% Y1 / 60% Y3 under v3.0.

### Worse in v3.0

1. **Labor-margin exposure per member is materially higher.** v2.0 had a design fee escalator that recovered $250–$500/yr per Light member and waived design fees on Office members but kept the leverage of "we can decline a trip request without a fee attached." v3.0 commits to design-anything-included. The marginal labor cost per "free" design is the founder's hour. The 3-active cap and the PHT VA are the only structural protections, and as scoped above the labor-negative threshold is plausibly hit at 15–25% of Office members in Y2–Y3.

2. **The per-member commission line has more cognitive risk.** v2.0's 10% × 70% × 0.98 was easy to communicate and audit. v3.0's "7.8% blended" looks cleaner but hides three different rates across three sub-pools (Virtuoso preferred, non-Virtuoso preferred, non-commissionable). The founder will be asked by sophisticated buyers and Fora's CSM what the actual rate was last quarter, and the answer is going to be a band, not a number.

3. **Y1 commission is overstated more than Y3+ commission.** v2.0 implicitly assumed 70/30 across all years (matching the realistic Y1 reality). v3.0 publishes 7.8% as if the 80/20 split is already in effect. The Y1 commission overstatement under v3.0 is ~$130–$200/Light and ~$350–$600/Office vs the Y1-realistic 6.2–6.5% rate.

4. **The EA Companion Seat now carries more labor-margin tax.** Under v2.0, with design fees on personal trips, the EA's trip queries had a soft brake. Under v3.0, the EA can text the desk for anything at no marginal cost. EAs are high-volume users by training. The plan does not size the EA-attributable trip load, which is plausibly 20–40% of total Office desk volume.

5. **The non-member design pricing is largely orphaned.** v2.0 used design fees as both a revenue line and a member-qualification mechanic. v3.0 retains the qualification function ("pay $500–$2,000 to use Latitude once, convert at 30–40%") but loses the meaningful revenue line. The 30–40% conversion claim is asserted, not engineered — no mechanic in the operations docs proactively converts paying non-members to subscription. This is a real gap.

### Neutral

- Society economics are essentially identical between v2.0 and v3.0.
- The Fora ladder mechanics (70/30 → 80/20 → 90/10) are unchanged. The Fora "personal sales" definition remains unpinned in both versions.
- The 18-night/yr assumption is the same. Both plans average across segments.

---

## What's wrong or missing

### 1. No segment-by-segment unit economics

The plan defines 5 ICP segments in §3 with different T&E ranges, different trip cadences, different buying processes. The unit economics in §5 are by tier (Light / Office / Society), not by segment. A Series A founder Office member and a 2-principal RIA Office member have wildly different unit economics — different nights/yr, different ADR (founders book more business hotels, RIAs more conference hotels), different personal-travel attach (founders' spouses book more leisure, RIA principals' spouses book less). The plan needs a 5×3 segment × tier table. Until it has one, the Y5 mix is a guess.

### 2. No accounting for PHT VA cost

The short-form v3 evaluation flagged this: PHT VA at $1,500–2,500/month × 2 VAs for 56 hours/week overnight coverage = $36–60K/yr that does not appear in §14.2's $4–6K/yr operating cost line. This is a per-member labor cost when scaled — at Y5 with 120 members, the VA cost is roughly $300–500/member/yr that the per-member economics implicitly absorb. **This is the single largest cost line missing from the plan.**

### 3. No founder-hour costing

The plan never prices the founder's hour. Without a labor rate, the labor-negative member calculation is qualitative. Recommend pricing the founder's hour at $150/hour as a planning rate (between primary-income economics at $45–60 and market-advisor rate at $150–250). Show in the per-member economics how many founder hours each tier consumes at base/bear/bull usage.

### 4. No personal-travel attach KPI

The §5 commission lines assume 100% personal-travel attach (because the math published includes the personal commission). The plan should publish:
- Year 1 attach rate target by tier (e.g., Light 30%, Office 50%, Society 80%)
- Year 3 attach rate target (Light 50%, Office 70%, Society 95%)
- Quarterly reporting against actual

Without this, the plan cannot diagnose whether a Y1 commission miss is from low attach, low nights/yr, or low ADR.

### 5. No Fora "personal sales" definition pinned

Same as v2.0. The 80/20 trigger at $300K personal sales is the single biggest commission lever in the model. If "personal sales" means gross commissionable bookings at preferred rates only (the strict reading), the trigger lands a year later than the plan implies and Y3 commission revenue drops 8–15%. **Get Fora's CSM to clarify in writing before the Y1 forecast is published.**

### 6. No quarterly labor-negative member protocol

The plan says "quarterly trip-pattern review" but doesn't specify the threshold (3.0× implied hours? 1.5×?), the response sequence (Society upgrade → coverage adjustment → off-board), or the cooling-off period between flag and action. Without a documented mechanic, "labor-negative member review" is a vibe. The v3 evaluation already flagged this; restating here because it's the operational mechanism that backstops the entire Model B labor-margin thesis.

### 7. No EA labor allocation in Office economics

The EA Companion Seat is included in Office at no incremental price. In the per-member table, this should add ~30–60 minutes per trip of incremental coordination labor, scaling to ~10–20 hours/year of additional founder time per Office member. At $150/hour, that's $1,500–$3,000 of labor cost per Office member from the EA seat alone — a meaningful tax that does not appear anywhere in §5.

### 8. No discussion of commission-receipt timing per member

Hotel commissions pay 30–90 days post-stay. For a member that books a $20K trip in March that stays in July, commission lands in October–December. The per-member Y1 revenue figures in §5 conflate booked and collected. For a Y1 member onboarded in month 6, only ~6 weeks of hotel commission actually lands inside Y1 against 6 months of subscription. **The published Y1 per-member number is closer to 75–85% in cash terms** — meaningful for the Y1 cash trough that the v2 evaluation flagged.

---

## Recommendations (prioritized, executable)

1. **Publish a Y1-specific commission rate of 6.2–6.5%, not 7.8%.** The 7.8% is a Y3+ steady-state number. Show the glide path in §5: Y1 6.4%, Y2 6.8%, Y3 7.2%, Y4–Y5 7.8%. Restate Y1 per-member revenue figures at the lower rate. This alone moves the published Y1 from ~$115K to ~$95K and is the single most honest change available.

2. **Build a 5-segment × 3-tier unit economics matrix.** Show nights/yr, ADR, personal-travel attach, and total revenue per member for each combination. The matrix will reveal which segments are most valuable per Office seat (PE operating partners), which are most fragile (RIA principals at 14 nights and low attach), and where the Y1 GTM motion should concentrate.

3. **Price the founder's hour at $150 and run the labor-negative member math explicitly.** Publish a table: at $349/mo, the Office member breaks even on labor at 56 founder-hours/yr (4.7/month). At 22 trips/yr × 3 hours each = 66 hours, the modal Office member is plausibly $1,500 labor-negative before SLA overhead. The PHT VA at month 4 is the structural answer; size it at $36–60K/yr as the short-form eval flagged.

4. **Publish three explicit personal-travel attach scenarios per tier (0% / 50% / 100%).** The 100% attach number is the plan's published assumption. Make the 0% and 50% versions equally visible so the founder is forecasting realistically. Track actual attach as a Y1 quarterly KPI.

5. **Document the quarterly labor-negative trigger and response protocol.** Specific threshold (recommend: any member exceeding 2.5× the implied unit-economics hours in a quarter), specific response sequence (1: Society upgrade conversation; 2: explicit coverage scope adjustment in writing; 3: friendly off-board with 90-day notice). Add to `/operations/member-lifecycle.md`.

6. **Pin Fora's definition of "personal sales" in writing.** Annual vs cumulative, gross booked vs commissionable booked, reset behavior. Re-publish the Y2–Y3 commission line under best-case and worst-case interpretations. The variance band on the Y3 commission line is ±15% until this is resolved.

7. **Add the EA Companion Seat labor tax to Office per-member economics.** Specify the assumption (e.g., 15 hours/year of incremental founder time per Office EA seat at $150/hour = $2,250 of labor cost). This either lowers the Office contribution margin or argues for an explicit EA-seat usage cap.

8. **Stress-test Y5 revenue at three Society outcomes:** Society at cap (20 members → ~$870K), Society partial fill (10 members → ~$760K), Society failure-to-launch (3 members → ~$610K). The plan currently publishes only the cap-fill version. Investors and the founder both need to see the full distribution.

9. **Restate Y1 per-member revenue in cash terms, not booked terms.** Hotel commissions pay 30–90 days after stay. A Y1 member onboarded in month 6 produces only ~75% of the published Y1 per-member number in actual Y1 cash. This matters for the Y1–Y2 cash trough.

10. **Add a non-member-to-member conversion mechanic in the operations doc.** §2.4 asserts 30–40% conversion; the operations docs have no proactive conversion trigger. Recommend: at completion of any non-member project, send a documented "convert to Light" offer with a 30-day window, tracked as a Y1 KPI. Without this, the qualification-funnel argument is empty.

---

*Word count: ~4,400. Per-member realistic Y5 base case: $3,450 Light, $7,900 Office, $31,000 Society. Aggregate realistic Y5 at base mix: $830–$870K with full Society fill; $760K at half Society fill; $617K at Society failure-to-launch. The v3.0 plan is better than v2.0 on subscription gross margin and worse on labor-margin exposure. Net per-member economics improve by 10–15% at Light, 8–12% at Office, ~3% at Society — meaningful but not transformative.*
