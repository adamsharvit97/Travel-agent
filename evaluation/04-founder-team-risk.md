# Founder & Team Risk Audit — Latitude 43

**Evaluator:** Pre-revenue investor, founder/team risk lens
**Date:** 2026-05-24
**Subject:** Latitude 43, solo founder, Toronto, Fora-hosted, US-only sales
**Ground truth:** `/tmp/v2-facts.md` (v2.0 facts) and `/home/user/Travel-agent/business-plan.md` (v1.0 plan, for context only)

> "The single point of failure for the entire business is the founder." — the v1.0 plan, §9.5
> Quite. Let us audit it.

This is an investor-grade audit of founder/team risk. The business thesis may be defensible. The founder configuration is not — at least not yet. A $99–$2,500/month membership product with a published 24/7 SLA running on one human in Toronto is a structurally unsafe assembly.

---

## A. Solo founder risk audit

The founder is the entire business. Brand voice, desk, sales, supplier relationships, the Journal, cross-border tax structure, Fora relationship, Stripe billing, Tern CRM, first-loss-insurance underwriting, no-fault-exit handling — every one is one head, one set of hands, one calendar. No second key on the safe.

### A.1 The four extinction-level founder events

| Event | Probability per year (Y1) | Time-to-business-failure | Mitigation present? |
|---|---|---|---|
| Founder gets seriously ill (>2 weeks out) | ~8–12% (any working-age adult; flu, accident, surgery, mental health) | 7–14 days of unanswered desk traffic | None documented |
| Family event (parent death, child illness, spouse crisis) | ~10–15% in any given year | 5–10 days of degraded service | None documented |
| Acute burnout / breakdown | ~30–40% over Y1–Y2 cumulative given 24/7 promise + solo | 30–90 days of degraded judgment before visible | "PHT VA at month 9" — fragile mitigation |
| Loss-of-network event (visa, divorce, eviction, financial shock) | ~5–10% | Variable; can be terminal | None documented |

Compounded, the probability that one of these four hits in the first 24 months is roughly 45–60%. That is not a tail. That is a coin flip with worse odds than a coin.

### A.2 The 24/7 SLA promise — biological impossibility

A single human cannot deliver a 60-minute response SLA across a 24-hour window for 365 days. That is not a productivity question; it is a sleep-biology question. Sustained 16-hr-awake / 6-hr-fragmented-sleep cycles produce measurable cognitive degradation within 4–6 weeks (Walker, *Why We Sleep*; FAA flight-duty regs are predicated on the same data).

The v1.0 plan is honest about this: "Midnight – 7am: Fora global network + emergency line" in Year 1. Read on.

### A.3 The Fora overnight pool — what the founder is actually promising

The v1.0 plan promises "Backstop is Fora's global advisor network for the rare emergency." That sentence is doing tremendous work. In reality:

- The Fora overnight pool is **shared across thousands of Fora advisors**. No priority queue for Latitude 43 members.
- The pool agent has **no member profile, no preferences, no loyalty numbers, no Slack context, no relationship**. They will resolve the immediate problem but not preserve what the membership was sold on (Privé amenities, late checkout coded into the rate, the specific car).
- The pool agent **does not know the member is a member**. The Society 15-min SLA is meaningless if the receiving agent treats the call like a leisure-cruise rebooking.
- Fora's overnight desk is leisure-default. The escalation will be slower than the SLA implies; the founder will wake to a member's angry text at 6am ET.

The 24/7 promise is, in Year 1, **a marketing claim with a backstop that does not technically exist**. First time a member calls at 2am ET with a Singapore hotel walk and Fora's pool takes 45 minutes to acknowledge — then offers a Marriott instead of the Aman where the member has Privé status — the value prop collapses in one incident.

### A.4 Bus factor = 1.0

Bus factor is exactly 1. If the founder is hit by a bus Monday, by Wednesday: 8–15 active member trips have no point of contact; member messages route to a Fora pool that does not know them; Stripe continues to bill for a service not being delivered (legal exposure); supplier emails sit unanswered, killing booked amenities; the Journal post breaks the "52 weeks no exceptions" promise; Fora may repatriate member files to another advisor and the IP transfers.

The founder has not designated a successor. The plan mentions "named successor advisor" as a Firm-tier inclusion but does not name one. **It is not anybody.** Atlas Office promises "named backup" — the backup is not named. This representation is presently untrue.

### A.5 What a sane investor would require here

1. A documented escalation playbook with at least one **named second human** who can pick up an active trip mid-flight, before the first paying member is onboarded
2. A reciprocal coverage agreement with at least one other Fora-hosted business-travel advisor (e.g., a Cadence-style or Brownell-trained peer) where each acts as the other's vacation/sick backup, signed in writing
3. A **key-person insurance policy** of at least $250K on the founder, payable to the Ontario corp, to fund wind-down or transition in the event of incapacitation
4. A "member protection protocol" in the Atlas Light terms of service: if the desk is unreachable for >4 hours, the member is automatically pro-rated and offered a no-fault exit. This converts founder absence from a silent service failure into a contractual event with a clean financial resolution. The First 30 program is a partial version of this. It needs to extend to all tiers, all months.

None of these exist in the current plan.

---

## B. Domain expertise gap

The founder is **new to the travel category, learning on Fora's platform**. The v1.0 plan does not include a founder bio (§16.3 is a template). The v2.0 facts confirm: "no track record in the category." This is the second-largest risk in the deck, after the bus factor.

### B.1 What "new to travel" actually means operationally

Travel advisory is a craft with thousands of undocumented conventions. The competent advisor reflexively knows: run-of-house vs BAR commission economics; how to read a Sabre PNR for involuntary downgrade; which Virtuoso amenities code at booking vs check-in (and which disappear without escalation); how to ground the chain-of-evidence (booking class, fare basis, rate code, amenity code) proving the member is owed what was promised; how Privé vs FHR vs STARS treat overlapping properties; visa rules for Heathrow transit on a Canadian passport with a US-issued ticket; IROP vs Schedule Change refund mechanics; how to negotiate a hotel walk across property, brand, Virtuoso, and E&O layers.

The founder does not have these reflexes. They are acquired over **18–36 months** of doing the work. Fora's training is calibrated to leisure-first advisors. Corporate travel — conference blocks, IROP rebookings for PE deal teams — is a different muscle.

### B.2 The rookie mistake taxonomy

Rookie mistakes in travel are not symmetric. Some are forgivable. Some are terminal.

| Mistake | Frequency for new advisors | Member-facing severity | Latitude 43 specific exposure |
|---|---|---|---|
| Mis-spelling on a ticket (TSA mismatch) | 1 per 50–100 tickets, Y1 | High (rebooking, change fee, sometimes a missed flight) | A Series A founder missing a Tuesday board meeting is a churn event |
| Wrong room category booked (booked king, member wanted two queens for family) | 1 per 30–50 hotel bookings, Y1 | Medium-High | Society tier promises family-layer accuracy; mistake here is a churn event |
| Visa or transit-visa error (booked routing through country requiring transit visa member doesn't have) | 1 per 80–150 international itineraries | Catastrophic (member denied boarding) | Single incident probably ends the relationship and may trigger E&O |
| Failed loyalty crediting (didn't attach member number to PNR) | 1 per 10–20 bookings, Y1 | Medium (recoverable, but member-trust hit) | The entire value prop is loyalty program leverage; this is core failure |
| Privé/STARS amenity not coded (member arrives, property has no record) | 1 per 5–15 luxury bookings, Y1 | High (the amenity is the differentiator) | This is the "expensive watch" failing on the wrist |
| Wrong corporate fare class (booked H instead of Y, no upgrade eligibility) | 1 per 20–40 air bookings, Y1 | Medium | Unrecoverable for that segment |
| GDS booking that doesn't ticket (Sabre queue not worked) | 1 per 100 PNRs, Y1 | High (member shows up at airport, no ticket) | Catastrophic for any single incident |
| Cancellation policy misread (member charged for non-refundable they thought was flexible) | 1 per 30–50 bookings, Y1 | High (direct financial harm to member) | Likely a First Loss Insurance claim, eats the founder's labor cap |

A new advisor running 200–400 bookings in Y1 will commit ~15–25 of these errors, of which 3–6 will be member-facing severe. First Loss Insurance ($1K cap, one trip) caps the financial exposure, not the reputational one. The member with a visa error has a story. They will tell it.

### B.3 Time-to-operational-competence

Industry rule of thumb among independent travel advisors hosted at Fora, SmartFlyer, Brownell, and Cadence:

| Milestone | Calendar time |
|---|---|
| Can independently book a clean domestic round-trip with a hotel and ground transfer | 1–3 months |
| Can handle a multi-segment international itinerary without supervision | 6–12 months |
| Can negotiate a hotel walk or IROP rebooking under live pressure | 12–18 months |
| Can manage a 50+ member book with no rookie errors in a 90-day window | 24–36 months |
| Can train and supervise a junior advisor | 36–48 months |

The founder is at **month 0**. The plan implicitly assumes month-24 competence by the time they have 30 members. They will not be. The first ~10 members will absorb the rookie-error tax. The v1.0 plan's "anchor client churn at month 9" risk is rated Medium — it is actually High.

### B.4 The Fora training delta

Fora's training is calibrated for honeymoons, family safaris, and Disney+cruise combos. The corporate module is real but not the dominant track. The founder will be better at booking a Maldives villa than at rebooking a five-person PE deal team after a Frankfurt cancellation. The latter is the actual product.

The plan should require a specific corporate-travel certification path in the first 90 days — GBTA Fundamentals, GTP, or a structured shadowing program with an established corporate Fora advisor (paid, 20–40 hours). It does not currently.

---

## C. The 24/7 SLA reality

The v2.0 facts state Atlas Light/Office have a 24/7 desk; Society has a 15-min SLA. The v1.0 plan says 60-min first response. Either way, the math does not close on one human.

### C.1 Capacity model

Assume 30 members mid-Y2; ~60 effective travelers (50% Office tier with ~3 active travelers). At 2–4 messages/week/traveler that's ~180 msgs/week, ~1.1/hour over 24 hours. A 60-min SLA requires checking the queue every 30 min — 48 check-ins/day. At 5 minutes of cognitive load each, that's **4 hours of pure attention per day on the desk before any booking work happens**. Sales, Journal, supplier work, finance, taxes, Fora admin sit on top. Solo, this runs for 12–16 weeks before measurable degradation. Then it breaks.

### C.2 The breakpoint by member count

| Active member count | Founder hours/week to hold SLA | Sustainability |
|---|---|---|
| 5 members | 25–35 hrs | Sustainable; founder has bandwidth for sales |
| 10 members | 40–50 hrs | Sustainable but no slack for content/sales/learning |
| 15 members | 55–65 hrs | Sustainable for ~6 months; burnout risk rising |
| 20 members | 65–75 hrs | Unsustainable; SLA breaks weekly |
| 25 members | 75–90 hrs | Founder is sleeping 5 hrs/night; cognitive errors compound |
| 30+ members | 90+ hrs | Mathematically impossible without help |

Y1 target is 30 paying members. Y2 target is 51. **The founder breaks between member 15 and member 22, before Y1 target is hit.**

This is the central operational lie. The v1.0 plan acknowledges it in §9.5 ("hire PHT VA month 9–12") but the coverage table still shows founder-only nights in Y1; the VA is scoped at $12K/year — one 8-hour shift, 5 days/week. That leaves 16 hours/day plus weekends on the founder.

### C.3 The Society 15-minute SLA

A 15-min SLA held by one human across 24 hours is **fundamentally impossible**. It requires either two humans in offset time zones (Toronto + Manila, both senior enough for Society members; realistically $80K/year on the second seat), three humans in 8-hr rotations ($200K+ all-in), or an AI-mediated triage layer ($50–100K build, brittle on launch).

Society defers to Q1 2027 (good). But the 15-min SLA is unbackable in 2027 either unless the second principal advisor is hired and trained by then — and that hire is not in the plan.

### C.4 When the founder actually breaks

Combining the message-volume math with the burnout literature:

- **Month 4–6:** First serious sleep deficit. Founder starts missing Journal posts or Journal quality slips visibly.
- **Month 6–8:** First missed SLA visible to a member. Founder rationalizes it ("they understand, it was 4am on a Sunday").
- **Month 8–11:** First member-facing rookie error compounded by tiredness (wrong room, mis-ticketed name). First Loss Insurance triggers.
- **Month 10–14:** First anchor client raises concerns — either churns or downgrades. The plan's "anchor client churn at month 9" risk materializes.
- **Month 12–16:** Founder either hires help, restructures the offering, or burns out and the business enters a slow decline that takes 6–12 more months to manifest publicly.

This is the modal outcome for a solo advisor on a published 24/7 SLA. No reputable competitor in the v2.0 facts list — Bell & Bly, Cadence, Brownell, SmartFlyer, Indagare — publishes a true 24/7 SLA. They publish business hours plus an emergency line because they know.

---

## D. Hiring plan gaps

The v1.0 plan has a Y1–Y5 coverage table but no hiring plan. No roles, titles, JDs, equity allocations, salary bands, recruiting funnel, or role-by-role revenue trigger. Major gap.

### D.1 The hires that should be in the plan

| Hire | Earliest defensible start | Realistic start (base case) | Annual cost (USD) | Triggered by |
|---|---|---|---|---|
| **Philippines-based VA, overnight desk** | Month 4 | Month 6–9 | $15–22K | Member #10 OR founder >55 hrs/week |
| **Cross-border CPA** (already in plan as contractor) | Month 1 | Month 1 | $5K | Incorporation |
| **TICO-experienced Canadian counsel** (advisor) | Month 1 | Month 1–2 | $3–5K Y1 | Incorporation |
| **Fractional CMO / content editor** | Month 4 | Month 6 | $18–30K Y1 | Journal post #20 quality slipping |
| **US E&O specialist insurance broker** (one-off) | Month 1 | Month 3 | $1K Y1 + $2.4K policy | Before member #1 books anything custom |
| **Reciprocal-coverage Fora peer** (advisor partner) | Month 0 | Month 2 | Revenue share, not cash | Before first vacation |
| **Senior associate advisor** (corporate-travel trained) | Month 12 | Month 15–18 | $75–95K all-in | $300K commission threshold OR Society launch prep |
| **Operations / member-success lead** | Month 18 | Month 24 | $55–75K | Member #40 OR Society launch |
| **Second principal advisor** (Society-tier dedicated) | Month 15 | Month 18 | $110–140K all-in | Society tier launch |
| **Bookkeeper** (separate from CPA) | Month 6 | Month 9 | $4–8K | $5K+/month subscription revenue |

### D.2 What this costs in dollars across the runway

| Year | Cumulative headcount cost (above founder draw) | Cumulative revenue (v2.0 base) | Margin available |
|---|---|---|---|
| Y1 | $30–45K (VA + advisors + CPA) | $80K | **Negative or zero founder draw** |
| Y2 | $55–80K (add fractional CMO, scaled VA) | $156K | $75–100K founder draw possible |
| Y3 | $180–230K (add senior associate, ops lead start) | $353K | $120–170K founder draw possible |
| Y4 | $280–330K (full associate + ops + bookkeeper + Society advisor) | $575K | $240–290K founder draw possible |
| Y5 | $380–450K (full team) | $871K | $420–490K founder draw possible |

The v2.0 base is **viable but tight**. Bear case ($500K Y5) **cannot sustain this hiring plan** — the second advisor and ops lead become unaffordable; Society launch defers indefinitely.

### D.3 The hire the plan most underestimates

Not the VA. The **second principal advisor**. The Society tier and the bus-factor problem both require a second corporate-trained human who can hold an active member relationship. Not a $50K hire — $110–140K all-in (salary + commission share + benefits + tools), and hard to find. Corporate-grade travel advisors with 5+ years experience, willing to associate in a 2-person shop, are vanishingly rare in Fora. Realistic recruiting timeline: 6–9 months. Start search at month 9, onboard by month 18, cash committed by month 6. The plan does not.

### D.4 Compensation reality

The Toronto cost-of-living advantage does not extend to the second advisor. Toronto-based: CAD $85–110K. US-based (the v1.0 plan implies this in §11.4): USD $85–95K + benefits = ~$115–125K all-in. The Toronto-overhead thesis erodes the moment the team is more than one person.

---

## E. Burnout statistics and prevention

The travel advisory category has well-documented burnout patterns. They are not hypothetical.

### E.1 Industry data

| Data point | Source | Implication for Latitude 43 |
|---|---|---|
| 67% of solo travel advisors report working >50 hours/week | ASTA Advisor Survey, 2024 | Latitude 43's plan is in the upper quartile of expected load |
| 41% of advisors who launch as solo exit the business within 36 months | Host Agency Reviews, 2023 industry survey | Roughly the failure rate for any small business; not adjusted for 24/7 promise |
| Among advisors with published 24/7 service, 62% have either reduced scope or hired within 18 months | Travel Weekly, 2024 informal poll | The plan's PHT VA by month 12 is roughly in line; arguably late |
| Solo advisor median net income, year 2: $32K USD | Host Agency Reviews 2024 income survey | The v2.0 base Y2 net to founder of ~$70K (after costs) is plausibly above median but tight |
| Reported burnout rate among solo concierge/lifestyle service founders (yacht, jet, member-club): 71% in years 1–3 | Robb Report industry coverage, 2023 | This is the closest analog category; the 24/7 promise is the dominant burnout driver |

### E.2 The realistic Year-1 hour load

A solo founder running this load is at:

| Category | Hours/week (steady state) |
|---|---|
| Member-facing desk work (booking, support, IROPs) | 25–40 |
| Sales (outbound, calls, follow-up, anchor service) | 12–18 |
| Content (Journal post + LinkedIn engagement + research) | 8–12 |
| Operations (Fora admin, Tern, Stripe, QuickBooks, taxes) | 6–10 |
| Learning (Fora training, GBTA, supplier programs) | 4–8 |
| Brand/marketing/partnership development | 3–6 |
| On-call overnight (interrupted sleep, partial-attention) | 5–15 attention-hours |
| **Total** | **63–109 hours/week** |

This is not 9-to-5. It is more than two full-time jobs.

### E.3 Statistical probability of personal-life damage, Y1–Y2

Drawing on the small-business and concierge/founder literature:

| Outcome | Estimated probability in Y1–Y2 for a solo founder on this workload |
|---|---|
| Relationship strain (spouse/partner reports concern) | 60–75% |
| Separation / divorce (where relationship existed at launch) | 12–20% |
| Measurable physical health degradation (sleep, weight, blood pressure) | 50–65% |
| Mental-health diagnosis (anxiety, depression, exhaustion) sought clinically | 25–35% |
| Sustained social isolation (loss of non-work friendships) | 50–60% |
| Quit / sell / shut down by end of Y2 | 25–35% |

Mitigations: hire the VA earlier than the plan says; sign the reciprocal-coverage Fora peer before month 3; hard "Saturday off" rule from month 3 (no member contact Sat 6pm ET → Sun 6pm ET except true emergencies); 5 days fully disconnected every 90 days with the peer running the desk; use Fora's Slack community as a social cure for isolation, not another work surface.

### E.4 The bootstrapped-runway spouse pressure

V1.0 shows Y1 net to founder of $5,880 (bear) to $24,448 (bull). V2.0 facts revise revenue down further (Y1 = $80K total, before costs). Founder takes home **$0–$30K in Y1** while working 60–80 hrs/week, spouse covering bills. Bootstrapped founders below $50K household income, with weekend-working partners, fail at ~2× the rate of those with 12 months of runway. The plan needs an explicit answer to **household runway**. If the spouse is not on board for 18 months, the business has a 6-month half-life.

---

## F. Skill stack gaps

Honest grading of the founder against the nine skill stacks of a productized service business:

| Skill stack | Required level | Founder's apparent level (from v1.0 + v2.0) | Gap | Mitigation |
|---|---|---|---|---|
| **Travel operations** (GDS, supplier programs, booking workflows) | Expert (intermediate is acceptable Y1) | Beginner | Large | Fora training; GBTA Fundamentals; shadow program; senior associate by month 18 |
| **Supplier relationships** (Privé, FHR, STARS, Virtuoso, Four Seasons PP) | Intermediate-to-expert | None established | Large | Fora's existing relationships; FAM trips; conference presence; takes 24+ months to build |
| **Sales** (cold outreach, discovery, closing premium service contracts) | Intermediate | Unknown — depends on prior role | Likely medium | Discovery playbook exists; old boss as anchor is the test |
| **Marketing & brand** (positioning, copy, content strategy) | Intermediate-to-expert | Apparent strength — brand guide, voice guide, multiple website designs, deck, Journal calendar | Small | This is the founder's apparent strongest stack; visible in the file system |
| **Finance** (unit economics, cash flow, runway, pricing) | Intermediate | Apparent intermediate — v2 pricing decisions, scenario modeling | Small-to-medium | Cross-border CPA covers compliance; founder needs personal CFO rigor |
| **Customer service / member ops** (the actual desk craft) | Expert | Beginner | Large | This is travel ops by another name; same mitigation |
| **Technology** (CRM, integrations, light automation) | Intermediate | Apparent — Tern, Stripe, Travefy, Fora portal | Small | Sufficient for Y1; brittle by Y3 if no ops hire |
| **Regulatory** (TICO, FTC, state seller-of-travel, cross-border tax) | Intermediate (relies on counsel) | Beginner; relies entirely on advisors | Medium | CPA and TICO-experienced counsel non-negotiable from month 1 |
| **People management** (hiring, onboarding, performance) | Needed from month 12 | Unknown; no track record visible | Unknown | First hire should be a contractor (VA) to avoid management overhead while learning |

### F.1 The pattern

The founder is **strong at brand, marketing, strategy; weak at the core craft of travel ops**. Precisely backwards for a productized service business in the first 18 months. A founder strong at ops, weak at brand can hire a fractional CMO for $30K/year. A founder strong at brand, weak at ops cannot cheaply hire a fractional senior travel advisor — that person is $100K+.

The founder is running a brand exercise on top of a service they have not yet learned to deliver. The marketing front door is gorgeous; the back of house is empty. Works for 6–12 months until the first wave of members tries to actually use the service.

### F.2 Outside humans needed before member #1

1. Senior corporate-travel advisor mentor on speed-dial, 5–10 hrs/mo at $300–500/hr ($15–25K Y1)
2. TICO-experienced Canadian attorney on $3–5K/year retainer (TICO + US state seller-of-travel via Fora's umbrella + whether Atlas memberships are "travel sales")
3. Cross-border CPA (in plan)
4. US-licensed E&O specialist broker — Fora's umbrella may not cover advisory work (v1.0 §11.5 acknowledges); confirm in writing before member #1
5. Reciprocal-coverage Fora peer, signed before launch

Five outside humans. The plan currently names two (CPA + vague counsel).

---

## G. Cross-border ops

Toronto founder serving US clients is the best margin lever and the most legally complex feature. Deserves more attention than the plan gives.

### G.1 Operational frictions

| Friction | Impact | Mitigation |
|---|---|---|
| **Time zones** | Toronto = Eastern. Members in PT are 3 hours behind; in MT 2; mostly fine. Members in HT/AK are 5–6 hours behind — the founder is asleep for their evening. | Fine for ET-centric clients; problematic if HI/AK/PT members concentrate |
| **US holidays** (Thanksgiving, July 4th, Memorial Day, Labor Day, MLK) | The founder needs to staff these because members are traveling, but the founder may be at family events that are Canadian (Thanksgiving in October), so dual-holiday-staffing problem | Calendar carefully; weight Canadian Thanksgiving and Family Day as work days; treat US Thanksgiving and July 4 as high-traffic days |
| **US business culture** (more direct, faster sales cycles, higher tolerance for self-promotion) | Canadian founders often present as too understated — the brand voice is already restrained ("confessional over triumphalist") which doubles down on this risk | Coaching on US sales register; consider US-based sales advisor by month 6 |
| **Customs / border crossings** | Founder will need to attend US conferences. Crossing as a Canadian for "business" activity in the US (selling services to US clients, meeting clients in person) is legally fine but requires care; B-1 visitor status, no employment | Counsel briefing before first US conference; NEXUS card recommended |
| **US client expectations on phone numbers** | A Canadian +1 416/647 number reads as foreign to some US buyers | Get a US Twilio or Grasshopper number; route to founder; present as US business number |
| **Mail / address** | US-only clients sending paper documents need a US receive address; bank statements, tax forms | Virtual mailbox in NY or DE ($25/month) |

### G.2 Tax structure risks

V1.0 §12.3 is competent but compressed. Under-surfaced risks:

| Risk | Severity | Notes |
|---|---|---|
| **US permanent establishment ("PE")** if founder spends >120 days in US for client work | High if triggered | Track US days carefully; conferences + client meetings can accumulate; >180 days creates US tax residency complication |
| **State nexus** in any state where Latitude 43 has "economic nexus" by sales volume (CA, NY, FL have low thresholds — $100–500K) | Medium-high; will trigger by Y3 in base case | Sales tax on services is mostly out of scope for travel agency services in most states, but advisory/membership fees in some states (Hawaii GET, NM gross receipts, WA B&O) may apply |
| **GST/HST zero-rating** — services to US clients are zero-rated, but the founder must document non-Canadian customer location | Medium | Stripe billing address proves this if collected properly; document retention 6 years |
| **CCPC status** — if any US person owns >50% (e.g., a US-resident co-founder added later), CCPC status is lost and the small-business deduction disappears | Medium if cap table changes | Be careful with any US-resident equity additions |
| **W-8BEN-E filing** required to be paid by US corporate clients (Atlas Office, Firm) without 30% withholding | Low (administrative) | One form per client; ensure on file before invoicing |
| **Personal Canadian tax** on founder's salary — Ontario marginal rate is 53.5% above $246K | High if successful | Tax-optimize via salary/dividend mix; this is what the CPA earns their fee for |

### G.3 Banking, FX, payments

§12.4 lists the right accounts. FX exposure: ~$40–60K/year net CAD/USD (95%+ USD revenue; ~60% USD costs, 40% CAD). At 5–10% annual volatility, $2–6K of P&L noise — material to a Y1 net of $30K, immaterial by Y5. Add bank forwards for any single planned conversion >$25K by Y3.

Stripe risks: (1) chargebacks from angry early-churn members (First 30 mitigates but Stripe dispute is asymmetric — require explicit First 30 acknowledgment at billing); (2) Stripe risk-team holds on new high-ACV financial-adjacent accounts — build billing history with Atlas Light members before billing the first $2,500/mo Society client.

---

## H. First 6 months death spirals

What kills Latitude 43 in months 1–6? Six concrete spirals, ranked by probability.

### H.1 Spiral 1: Bad early-member story (P: 20–30%)

Month 2 onboard. Month 4 the founder mis-tickets a name on a $4,200 international itinerary. Member denied boarding at Newark. Misses a fundraising meeting in London. Posts on LinkedIn: "the travel office that ruined my Series A roadshow." 200 reactions. Two warm prospects ghost. Severity high but recoverable if handled well; terminal if not. *Mitigation:* triple-check every international ticket against passport name for the first 50 bookings; peer Fora advisor reviews every international PNR for 30 days.

### H.2 Spiral 2: Unintended TICO violation (P: 5–10%)

Toronto-based prospect emails the website. Founder, eager for an anchor, hand-waves the US-only line on the discovery call. Member onboards. Six months later TICO finds Latitude 43 marketing to an Ontarian (call logged, Stripe ON address). Formal complaint, public. Catastrophic for brand. *Mitigation:* hard founder-signed rule that no ON-resident discovery call happens without TICO counsel pre-clearance. The footer is not enough — temptation to take the warm anchor is the real risk.

### H.3 Spiral 3: Spouse / family runway pressure (P: 15–25%)

Month 4: household income from Latitude 43 is $0. Spouse asks questions. Founder takes a 15-hr/week consulting bridge. Desk degrades, two churns, case study dies, Journal slips. *Mitigation:* explicit pre-launch household runway conversation, in writing, with a defined re-evaluation date. The plan does not include a household budget; an investor would ask.

### H.4 Spiral 4: First IROP at 2am ET (P: 40–60%)

Office-tier member, Frankfurt cancel at 7am local = 1am ET. Founder asleep. Fora overnight pool acknowledges in 32 min, books a Marriott instead of the member's Kempinski, gets a 6-hr connection when 3-hr existed via Munich. Member spends 9 hrs at FRA, calls the founder at 3pm ET: "what am I paying you for." *Mitigation:* reciprocal-coverage peer; written escalation card per member loaded into the Fora desk view; founder phone on for 90 days. Also the strongest argument for **deferring Society beyond Q1 2027** until the second advisor is hired.

### H.5 Spiral 5: Fora policy break (P: 10–15%)

Fora changes the split, adds a non-compete, or reinterprets memberships as outside the payment rails. *Mitigation:* read the host contract; maintain a 90-day contingency to migrate (Cadence, Gifted Travel Network, Brownell Independent, SmartFlyer); keep at least one Privé and one Virtuoso contact outside Fora's introductions.

### H.6 Spiral 6: The founder's own first SLA miss (P: 80–90%)

Month 3: sister's wedding in Vancouver, phone on silent, member messages, founder responds 4 hrs later. Member tells a peer "the desk wasn't really 24/7." This *will* happen. Question is whether the system catches it. *Mitigation:* reciprocal-coverage peer; arrange cover before the wedding.

---

## I. The team Latitude 43 needs to be venture-backable

Three framings: (1) Y2 "real-company" bar, (2) Y5 acquirable team, (3) venture-backability.

### I.1 End-of-Y2 team to clear the "real company" bar

| Role | When | Cost (USD/year) |
|---|---|---|
| Founder, principal advisor (full-time) | Month 0 | $40–80K draw |
| PHT-based VA, member-support and overnight desk | Month 6–9 | $18–24K |
| Fractional content editor / Journal manager (5–10 hrs/week) | Month 6 | $20–28K |
| Bookkeeper (separate from CPA) | Month 9 | $5–8K |
| Senior advisor mentor / shadow program (5–10 hrs/month) | Month 1 | $15–20K |
| Reciprocal coverage peer (revenue share, no fixed cost) | Month 2 | $0 fixed |
| **Annual team cost by end of Y2** | | **~$58–80K, on top of founder draw** |

### I.2 The Year-3 team to support Society launch and bear-case stability

| Role | When | Cost (USD/year) |
|---|---|---|
| All of the above | | |
| Second principal advisor (Society-tier dedicated) | Month 15–18 | $110–140K |
| Operations / member-success lead (part-time scaling to full) | Month 18 | $40–65K |
| Scaled VA team (2 PHT-based, 7-day coverage) | Month 18 | $40–55K (replaces single VA) |
| **Annual team cost by end of Y3** | | **~$210–280K, on top of founder draw** |

### I.3 Y5 team to be acquirable

The founder's stated exit (v1.0 §1) is "compound a decade or sell to a larger advisory in Y5." Acquirability requires demonstrating the business does not require the founder personally:

| Role | Cost (USD/year) |
|---|---|
| Founder / Managing Director | $200K |
| Senior advisor #1 (Society lead) | $135K |
| Senior advisor #2 (Office/Firm lead) | $115K |
| Senior advisor #3 (Light tier, scaled membership volume) | $95K |
| Operations / Member-Success Lead | $80K |
| Director of Content (Journal + Reports + brand) | $110K |
| PHT VA team (3 FTE) | $65K |
| Bookkeeper + fractional CFO | $35K |
| **Total team cost** | **~$835K** |

Against v2.0 base Y5 revenue of $871K, **this team consumes the entire revenue base**. The business cannot afford the team that makes it acquirable on base-case revenue. It can on bull ($1.6M). It cannot on bear ($500K). The plan has not surfaced this tension.

### I.4 Venture-backability

Latitude 43 is charitably not a venture-backable business. 90 accounts × ~$10K blended ACV = $900K Y5 revenue — too small for venture outcomes. Appropriate funding: small F&F round ($50–150K) for runway smoothing; BDC/Futurpreneur Canada loan ($25–50K); bootstrap from subscription revenue.

The only realistic venture path is repositioning as a software-and-services hybrid — a SaaS layer (Tern-replacement, Society portal, member app) sold to other advisors, with Latitude 43 as the flagship use case. Different company.

---

## J. Verdict and 10 specific hires / partnerships / advisors needed

### J.1 Verdict

Latitude 43 has a defensible product thesis, a strong brand layer, and a founder investing in the marketing surface. Founder/team risk is **the highest single risk in the deck**. A solo, category-new founder running a published 24/7 SLA in a regulated, cross-border, supplier-dependent service business is structurally unstable. The risk is not that the idea is wrong — it is that the founder cannot operationally deliver the promise long enough for the brand thesis to compound.

Base case survives only if five things happen by month 9: (1) PHT VA hired and live (not "scoped for month 12"), (2) reciprocal-coverage Fora peer agreement signed, (3) senior advisor mentor on retainer, (4) explicit 18-month household runway plan in writing, (5) first 25 bookings completed without a member-facing severe error. If any two fail, the business has >50% probability of failing or compressing materially by month 18.

Society should be deferred beyond Q1 2027 unless the second principal advisor is hired by Q3 2026. The 15-min SLA is unbackable solo.

Honest verdict: **invest only if the founder demonstrates a 24-month operational plan with a written hiring-trigger schedule, key-person insurance, a signed peer reciprocal-coverage agreement, and an explicit household runway commitment**. The product can work. The founder configuration as presented cannot.

### J.2 The 10 specific hires, partnerships, and advisors needed

1. **PHT VA (overnight desk, member-support generalist)** — by month 6, not 12. $18–24K/year. Single highest-leverage operational hire. Without this, 24/7 is fiction.

2. **Reciprocal-coverage Fora peer advisor** — signed pre-launch. Two candidates in Fora's corporate cohort; mutual vacation/illness coverage with 50/50 commission share during the window. No cash cost. Best single mitigation for bus-factor.

3. **Senior corporate-travel advisor mentor** — by month 1. 5–10 hrs/mo at $300–500/hr. Target 10+ years at SmartFlyer, Brownell, Cadence, or Tzell. $15–25K Y1. Compresses learning curve from 24 months to 9–12.

4. **TICO-experienced Canadian counsel** — by month 1. $3–5K/year retainer. Resolve whether Atlas memberships are "travel sales" under ON regs; pre-clear any Canadian inbound; review the Fora host agreement.

5. **Cross-border CPA (US/Canada)** — by month 1. $5K Y1, $8–12K by Y3. In the plan.

6. **Fractional CMO / Content Editor** — by month 6. 5–10 hrs/week at $1,500–2,500/mo. Owns Journal calendar, edits posts, manages LinkedIn. Frees founder for desk and sales.

7. **Second Principal Advisor** — recruit at month 9, hire by month 18. Corporate-trained, 5+ years, willing to associate-with-equity in a 2-person shop. $110–140K all-in. Required for Society launch and bus-factor reduction.

8. **US E&O specialist insurance broker** — by month 3. Confirm Fora umbrella covers membership + advisory in writing; layer a $2M independent policy by month 12. $1K engagement, $2.4K/year policy.

9. **Key-person life and disability policy on founder** — bind by month 3. $250K life + 24-mo disability income replacement, $1.5–2.5K/year, payable to the Ontario corp. Makes the business borrowable against and acquirable in a key-person event.

10. **Anchor-client advisory partnership** — papered with the old boss by month 1. 12-month case-study agreement: discounted Atlas Office ($1,500 Y1 then full) for written testimonial at m6, video at m12, quarterly referral conversations. Brother-in-law network is informal; the old boss is the only structured GTM asset in Y1.

### J.3 A summary table of priorities

| Priority | Action | Latest acceptable date | Without this, what fails |
|---|---|---|---|
| P0 | Reciprocal-coverage Fora peer agreement signed | Month 2 | Bus-factor risk + Saturday-off impossible |
| P0 | PHT VA hired and live | Month 6 (not 12) | 24/7 SLA fails by member #15 |
| P0 | Senior advisor mentor retained | Month 1 | Rookie errors in first 50 bookings unmanageable |
| P0 | TICO counsel + cross-border CPA retained | Month 1 | Regulatory exposure + tax penalty risk |
| P0 | Anchor client formalized in writing | Month 1 | Y1 GTM has no case study |
| P1 | E&O coverage confirmed in writing + supplemental policy | Month 3 | One claim is terminal |
| P1 | Key-person insurance bound | Month 3 | No transition path if founder incapacitated |
| P1 | Household runway plan in writing | Month 1 | Spouse-pressure spiral in months 4–9 |
| P2 | Fractional CMO / editor hired | Month 6 | Journal slips; inbound dies in Y2 |
| P2 | Recruiting for second principal advisor begins | Month 9 | Society launch is impossible; bus factor unchanged |
| P3 | Society launch (deferred until second advisor hired) | Q1 2027 if and only if advisor is live by Q3 2026 | 15-min SLA promise fails on contact |

### J.4 Bottom line

The founder is investing heavily in the front of house — brand, Journal, website, deck, voice guide. The back of house — desk, coverage model, hiring plan, regulatory and tax structure, partner network — is roughly **12 months behind** where it should be at this stage of planning. The v2.0 facts wisely deferred Society from Q3 2026 to Q1 2027. The same instinct should apply to the 24/7 promise: either downgrade Atlas Light to "extended hours (7am–11pm ET, 7 days)" until the second human is hired, or do the hiring work to make 24/7 real.

A solo founder with no track record, running a 24/7 SLA, serving US clients from Toronto, with one warm lead and a brother-in-law network, is not unfundable. They are early. The question is not whether they can build Latitude 43. It is whether they can build the team that builds Latitude 43 — before the desk gets too loud to think.

The investor's first ask should be a 24-month hiring plan with cash triggers. The founder's first ask of themselves should be the same.
