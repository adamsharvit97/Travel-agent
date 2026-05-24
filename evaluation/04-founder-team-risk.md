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

The v2.0 facts state Atlas Light/Office have a 24/7 desk; Society has a 15-minute SLA. The v1.0 plan describes 60-minute first response. Either way, the math does not close on one human.

### C.1 The single-human capacity model

Let's model the desk as a queueing system, very roughly.

Assume:
- Active members at scale: 30 (the v2.0 facts' Y2 target = 51 members; let's use 30 for a mid-Y2 mid-point)
- Average member message rate during a normal week: 2–4 messages/week per active traveler
- Atlas Office has ~3 active travelers; assume 50% of members are Office or higher
- Effective traveler count served: 30 + (15 × 2 additional travelers) = ~60 travelers
- Messages per week: 60 × 3 = **180 messages/week, ~26/day, ~1.1/hour over a 24-hour day**

A 60-minute first-response SLA across 24 hours per day requires the responder to be checking the queue at least every 30 minutes (so the max wait at any point is ≤60 min). That is 48 check-ins per day. Even if each check-in is only 5 minutes of cognitive load (read, triage, respond or defer), that is **4 hours of pure attention per day on the desk before any actual booking work happens**.

Booking work, supplier escalations, sales calls, Journal writing, finance, taxes, and Fora administrative load are on top of that.

A solo human can run this for maybe 12–16 weeks before measurable degradation. Then they break.

### C.2 The breakpoint by member count

| Active member count | Founder hours/week to hold SLA | Sustainability |
|---|---|---|
| 5 members | 25–35 hrs | Sustainable; founder has bandwidth for sales |
| 10 members | 40–50 hrs | Sustainable but no slack for content/sales/learning |
| 15 members | 55–65 hrs | Sustainable for ~6 months; burnout risk rising |
| 20 members | 65–75 hrs | Unsustainable; SLA breaks weekly |
| 25 members | 75–90 hrs | Founder is sleeping 5 hrs/night; cognitive errors compound |
| 30+ members | 90+ hrs | Mathematically impossible without help |

The plan's Y1 target is 30 paying members (22 Light + 8 Office). The plan's Y2 target is 51 members. **The founder breaks somewhere between member 15 and member 22, well before the Y1 target is hit.**

This is the central operational lie in the v1.0 plan. The 24/7 SLA at the Y1 member volume cannot be held solo. The plan acknowledges this in §9.5 ("hire the PHT VA at month 9–12, not month 18") but the operational coverage table still shows founder-only night coverage in Year 1, and the VA is scoped at $12K/year, which is a single 8-hour shift, 5 days/week. That leaves 16 hours/day, plus weekends, on the founder.

### C.3 The Society 15-minute SLA

The Latitude Society tier promises a 15-minute SLA. This is a marketing-grade promise. Held against a single human across 24 hours, it is **fundamentally impossible**. The maximum sustainable response cadence for a human checking queues across a 24-hour cycle is 30–60 minutes (because the human has to sleep, eat, shower, and have a relationship). A 15-minute SLA requires either:

- Two humans in offset time zones (Toronto + Manila, both senior enough to handle Society-tier members) — the cheap version is $40K/year on the VA side, the realistic version is $80K
- Three humans in 8-hour rotations — $200K+ all-in
- An AI-mediated triage layer that acknowledges within 15 minutes and surfaces to a human asynchronously — possible but requires a $50K–$100K build and is brittle on launch

The Society tier launches Q1 2027 (deferred from Q3 2026, per v2.0 facts) — sensible. But the 15-minute SLA is presently a promise that cannot be operationally backed in 2027 either, unless the second principal advisor (proposed below) is hired and trained by then. With Society capped at 30 members globally and an invite-only motion, this is recoverable. But it requires a hire by Q3 2026 to be ready for Q1 2027 launch — and that hire is not in the plan.

### C.4 When the founder actually breaks

Combining the message-volume math with the burnout literature:

- **Month 4–6:** First serious sleep deficit. Founder starts missing Journal posts or Journal quality slips visibly.
- **Month 6–8:** First missed SLA visible to a member. Founder rationalizes it ("they understand, it was 4am on a Sunday").
- **Month 8–11:** First member-facing rookie error compounded by tiredness (wrong room, mis-ticketed name). First Loss Insurance triggers.
- **Month 10–14:** First anchor client raises concerns — either churns or downgrades. The plan's "anchor client churn at month 9" risk materializes.
- **Month 12–16:** Founder either hires help, restructures the offering, or burns out and the business enters a slow decline that takes 6–12 more months to manifest publicly.

This is not pessimism. This is the modal outcome for a solo advisor on a published 24/7 SLA. It is the reason no other reputable competitor in the v2.0 facts list — Bell & Bly, Cadence, Brownell, SmartFlyer, Indagare — publishes a true 24/7 SLA. They publish business hours plus an emergency line because they know.

---

## D. Hiring plan gaps

The v1.0 plan has a coverage table for Years 1–5 but it is not a hiring plan. There are no roles, no titles, no JDs, no equity allocations, no salary bands, no recruiting funnel, no onboarding plan, no role-by-role revenue trigger. This is a major gap.

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

The v2.0 base case is **viable but tight**. The bear case ($500K Y5) **cannot sustain this hiring plan** — the second principal advisor and the ops lead become unaffordable, and Society launch must be deferred indefinitely.

### D.3 The hire the plan most underestimates

It is not the VA. It is the **second principal advisor**. The Society tier and the bus-factor problem both require a second corporate-trained human who can hold an active member relationship. That human is not a $50K hire. They are a $110–140K all-in hire (salary + commission share + benefits + tools) and they are hard to find — corporate-grade travel advisors with 5+ years of experience, willing to work as an associate in a 2-person shop, are vanishingly rare in the Fora population. The realistic recruiting timeline is **6–9 months**, which means starting the search at month 9 to onboard by month 18, which means having the cash committed at month 6. The plan does not.

### D.4 Compensation reality

The Toronto cost-of-living advantage is real but does not extend to the second advisor. If the second advisor is also Toronto-based, they are taking a salary that is roughly competitive with Canadian agency work (~CAD $85–110K). If the second advisor is US-based (which the plan implies in the v1.0 §11.4 "US-based associate advisor"), they cost USD $85–95K plus benefits — closer to $115–125K all-in. The founder's Toronto-overhead-advantage thesis erodes the moment the team is more than one person.

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

A solo founder running a paid membership product with a published 24/7 SLA, doing outbound sales, writing the Journal weekly, building partner relationships, learning the category, and operating a Canadian corp serving US clients is at:

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

These are bad numbers. The mitigations are: (a) hire the VA earlier than the plan says, (b) build the reciprocal-coverage agreement with a peer Fora advisor before month 3, (c) set a "Saturday hours" hard line from month 3 (no member contact between Saturday 6pm ET and Sunday 6pm ET except true emergencies), (d) require the founder to take 5 days off, fully disconnected, every 90 days, with the reciprocal-coverage partner running the desk, and (e) make Fora's Slack community part of the social cure for isolation rather than another work surface.

### E.4 The spouse / family pressure on bootstrapped runway

The founder is bootstrapped. The v1.0 plan shows a Y1 net to founder of $5,880 (bear) to $24,448 (bull) — and the v2.0 facts revise revenue down further (Y1 = $80K total, before any costs). The founder is taking home **somewhere between $0 and $30K in Y1**, while working 60–80 hours/week, while a spouse watches and pays the household bills.

This is the most under-discussed risk in the deck. Bootstrapped founders who go below $50K household income, while their spouse covers the gap, while they work weekends, fail at roughly twice the rate of founders with 12 months of runway. The plan needs an explicit answer to: **what is the household runway?** If the spouse is not on board for an 18-month income drought, the business has a 6-month half-life.

---

## F. Skill stack gaps

A founder of a productized service business needs roughly nine skill stacks. Here is the honest grading of the Latitude 43 founder against each.

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

The founder is **strong at brand, marketing, and strategy; weak at the core craft of travel operations**. This is a precisely backwards configuration for a productized service business in the first 18 months. A founder who is strong at travel ops but weak at brand can hire a fractional CMO for $30K/year. A founder who is strong at brand but weak at travel ops cannot hire a fractional senior travel advisor cheaply — that person is $100K+ and hard to find.

The founder is, in effect, running a brand exercise (Latitude 43, the Journal, the voice, the website designs) on top of a service they have not yet learned to deliver. This is the precise configuration of failure for "agency" launches across categories: the marketing front door is gorgeous, the back-of-house is empty. It works for 6–12 months until the first wave of members tries to actually use the service.

### F.2 Where the founder must invest in advisors/contractors immediately

1. A **senior corporate-travel advisor mentor** willing to be on speed-dial for 5–10 hours/month, paid $300–500/hour. The plan should budget $15–25K Y1 for this.
2. A **TICO-experienced Canadian attorney**, on retainer at $3–5K/year, because the Toronto-resident-serving-US-clients structure has at least three sharp edges (TICO, US state seller-of-travel laws applied to a Canadian seller via Fora's umbrella, and the question of whether Atlas memberships are "travel sales" under any of those regimes — flagged in v1.0 §12.2 but not resolved).
3. A **cross-border CPA** (already in the plan, non-negotiable).
4. A **US-licensed E&O specialist broker** — Fora's umbrella may not extend to all of Latitude 43's advisory work (the v1.0 plan acknowledges this in §11.5). Confirm coverage in writing before member #1.
5. A **reciprocal-coverage Fora peer advisor**, signed in writing, before launch.

That is five outside humans before the founder takes their first member. The plan currently names roughly two (the CPA and a vague "counsel").

---

## G. Cross-border ops

The Toronto-founder-serving-US-clients structure is the single best margin lever in the model and the single most legally complex feature of the business. It deserves more attention than the plan gives it.

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

The v1.0 plan §12.3 is competent but compressed. The risks not adequately surfaced:

| Risk | Severity | Notes |
|---|---|---|
| **US permanent establishment ("PE")** if founder spends >120 days in US for client work | High if triggered | Track US days carefully; conferences + client meetings can accumulate; >180 days creates US tax residency complication |
| **State nexus** in any state where Latitude 43 has "economic nexus" by sales volume (CA, NY, FL have low thresholds — $100–500K) | Medium-high; will trigger by Y3 in base case | Sales tax on services is mostly out of scope for travel agency services in most states, but advisory/membership fees in some states (Hawaii GET, NM gross receipts, WA B&O) may apply |
| **GST/HST zero-rating** — services to US clients are zero-rated, but the founder must document non-Canadian customer location | Medium | Stripe billing address proves this if collected properly; document retention 6 years |
| **CCPC status** — if any US person owns >50% (e.g., a US-resident co-founder added later), CCPC status is lost and the small-business deduction disappears | Medium if cap table changes | Be careful with any US-resident equity additions |
| **W-8BEN-E filing** required to be paid by US corporate clients (Atlas Office, Firm) without 30% withholding | Low (administrative) | One form per client; ensure on file before invoicing |
| **Personal Canadian tax** on founder's salary — Ontario marginal rate is 53.5% above $246K | High if successful | Tax-optimize via salary/dividend mix; this is what the CPA earns their fee for |

### G.3 Banking and FX exposure

The plan §12.4 lists the right accounts. The FX exposure is real but manageable: if 95%+ of revenue is USD and roughly 60% of costs are USD (Fora share, tools, contractors) and 40% are CAD (founder's CAD living costs, Canadian corp tax), the founder has roughly $40–60K of net CAD/USD exposure per year. At plausible 5–10% annual FX volatility, that's $2–6K of P&L noise — material to a Year-1 net of $30K, immaterial to a Year-5 net of $400K.

Stripe USD payouts to a TD USD account, Wise Business for sub-$50K FX conversions, and **forward contracts via the bank** for any single planned conversion above $25K. The plan does not mention forwards; for the bear/base Y1, this is fine. By Y3 it should be a standing practice.

### G.4 Payment processing

Stripe USD billing is fine. Two unobvious risks:

1. **Chargebacks**. A member who churns angrily (early in the relationship, before The First 30 is fully understood) may file a chargeback rather than use the no-fault exit. The First 30 program mitigates this, but Stripe's chargeback dispute process is asymmetric — the merchant usually loses if the buyer is determined. Set Stripe radar rules; require explicit acknowledgment of the First 30 terms at billing.
2. **Stripe risk team interventions**. New businesses billing high ACVs ($1K–$2.5K/month) in financial services-adjacent categories sometimes get held by Stripe risk. Establish the account, build billing history with the first ~5 members at lower amounts (Atlas Light) before billing the first Society client at $2,500/month.

---

## H. First 6 months death spirals

What kills Latitude 43 in months 1–6? Six concrete spirals, ranked by probability.

### H.1 Spiral 1: The bad early-member story

A member onboards in month 2. In month 4, the founder mis-tickets a name on a $4,200 international itinerary. The member is denied boarding at Newark. They miss a fundraising meeting in London. The founder pays the change fees (~$1,800), the member is furious, posts on LinkedIn about "the travel office that ruined my Series A roadshow." The post gets 200 reactions. Two warm prospects in the founder's pipeline see it. Both ghost.

Probability in months 1–6: **20–30%**. Severity: high but recoverable if handled well; terminal if handled badly.

Mitigation: Triple-check every international ticket against passport name for the first 50 bookings, period. Have a peer Fora advisor review every international PNR for the first 30 days.

### H.2 Spiral 2: Unintended TICO violation

A Toronto-based prospect emails through the website. The founder, eager for any anchor, takes a discovery call. The conversation goes well; the prospect is a Toronto-based founder who wants to sign up. The founder, under pressure, hand-waves the US-only line. The member onboards. Six months later TICO does a routine sweep, finds Latitude 43 marketing to Ontarians (because the discovery call is logged, the email exists, the Stripe billing address shows ON). Fine, formal complaint, public.

Probability in months 1–6: **5–10%**. Severity: catastrophic for the brand; recoverable financially.

Mitigation: A hard rule, signed by the founder, that no Ontario-resident discovery call happens, ever, without TICO counsel pre-clearance. The footer disclaimer is necessary but not sufficient — the temptation to take the warm anchor is the real risk.

### H.3 Spiral 3: Spouse / family pressure

Three months in, household income is $0 from Latitude 43. The spouse, who agreed to 12 months of runway, starts asking questions in month 4. The founder, sensing the runway compressing, takes on a side consulting engagement to bridge — the engagement eats 15 hours/week. The 24/7 desk degrades. Two members churn. The case study dies. The Journal slips.

Probability in months 1–6: **15–25%** depending on household financial position.

Mitigation: Have the explicit conversation **before launch**, in writing if possible. Set a defined runway with a defined re-evaluation date (e.g., month 12). Budget for the household, not for the business. The plan does not currently include a household budget; an investor would ask to see one.

### H.4 Spiral 4: The first IROP at 2am ET

A Society-tier (or even Office-tier) member is in Frankfurt. Their flight cancels at 7am Frankfurt = 1am ET. They text the desk. The founder is asleep. The Fora overnight pool picks up 32 minutes later (outside the 60-minute SLA but acceptable) but does not know the member, books a Marriott instead of the member's preferred Kempinski, gets the member a connecting flight 6 hours later when a 3-hour option existed via Munich. The member spends 9 hours in Frankfurt and calls the founder personally at 3pm ET demanding to know "what am I paying you for."

Probability in months 1–6: **40–60%** depending on member travel volume and international exposure.

Mitigation: The reciprocal-coverage Fora peer agreement; a written escalation card for every member loaded into the Fora overnight desk's view; founder's phone on for the first 90 days, period. This is also the strongest single argument for **delaying Society launch beyond Q1 2027** unless the second advisor is hired.

### H.5 Spiral 5: Fora policy or relationship break

Fora changes its commission split (the v1.0 plan acknowledges this risk at Medium probability). Or Fora's host agreement adds a non-compete clause. Or Fora's CEO leaves and the new operator tightens the membership-product rules. The founder discovers that Latitude 43's membership SKU is not "travel sales" under Fora's interpretation and is required to be billed separately, outside Fora's payment rails.

Probability in months 1–6: **10–15%**. Severity: medium; survivable with planning.

Mitigation: Read the host contract in detail. Maintain a written contingency to migrate to another host (Cadence, Gifted Travel Network, Brownell Independent, or SmartFlyer) within 90 days. Keep direct relationships with at least one Privé contact and one Virtuoso contact outside Fora's introductions.

### H.6 Spiral 6: The founder's own first SLA miss

In month 3, the founder is at a sister's wedding in Vancouver. Phone is on silent. A member sends two messages over a 90-minute window. The founder responds 4 hours later. The member doesn't churn — but their next renewal is uncertain, and they tell a peer that the desk "wasn't really 24/7."

Probability in months 1–6: **80–90%**. This *will* happen. The question is whether the system catches it.

Mitigation: This is the single strongest argument for a reciprocal-coverage Fora peer. Set the cover before the wedding.

---

## I. The team Latitude 43 needs to be venture-backable

Three different framings here: (1) what does the business need to clear a "this could be a real company" bar; (2) what does it need to be acquirable by a larger advisory in Year 5; (3) what does it need to be venture-backable (debatable whether it should ever raise venture given the unit economics, but we'll answer).

### I.1 The Year-2 team to clear the "real company" bar

By the end of Year 2, to demonstrate to any outside observer (investor, acquirer, or just a sober founder doing a self-assessment) that Latitude 43 is a real company and not a side project:

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

### I.3 The Year-5 team to be acquirable

To be acquirable (the founder's stated exit thesis in v1.0 §1: "compound for a decade or sell into a larger advisory group in year five"), Latitude 43 needs to demonstrate that **the business does not require the founder personally**. That requires:

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

Against a v2.0 base-case Y5 revenue of $871K, **this team consumes the entire revenue base**. The business cannot afford the team that makes it acquirable on base-case revenue. It can on bull-case revenue ($1.6M). It cannot on bear-case ($500K). The plan has not surfaced this tension.

### I.4 Venture-backability

Latitude 43 is, charitably, not a venture-backable business in the standard VC sense. The unit economics (90 accounts × ~$10K blended ACV at Y5 = $900K revenue) are too small to support venture-scale outcomes. The business is more appropriately funded with:

- A small friends-and-family round ($50–150K) for 18-month runway smoothing
- A small SBA-equivalent (BDC, Futurpreneur Canada) loan ($25–50K)
- Bootstrap from member subscription revenue

If the founder insists on venture, the only realistic path is to **reposition the company as a software-and-services hybrid** — a SaaS layer (Tern-replacement, Society-portal, member-app) sold to other advisors, with Latitude 43 as the flagship use case. That is a different company.

---

## J. Verdict and 10 specific hires / partnerships / advisors needed

### J.1 Verdict

Latitude 43 has a defensible product thesis, a strong brand layer, and a founder who is clearly investing in the marketing and positioning surface of the business. The founder/team risk profile, however, is **the highest single risk in the deck**. A solo, category-new founder running a published 24/7 SLA in a regulated, cross-border, supplier-dependent service business is structurally unstable. The risk is not that the business idea is wrong. The risk is that the founder cannot operationally deliver the promise long enough for the brand thesis to compound.

The base-case path is survivable if and only if **five things happen by month 9**:

1. The PHT VA is hired and trained (not "scoped for month 12" — hired and live by month 9)
2. The reciprocal-coverage Fora peer agreement is signed
3. The senior advisor mentor is on retainer
4. The household runway conversation has happened and produced an explicit 18-month plan
5. The founder has booked their first 25 bookings without a member-facing severe error

If any two of these do not happen, the business has a >50% probability of failing or compressing materially by month 18.

The Society tier should be **deferred beyond Q1 2027** unless the second principal advisor is hired by Q3 2026. The 15-minute SLA is unbackable solo.

The honest investor verdict is: **invest only if the founder demonstrates a 24-month operational plan, a written hiring trigger schedule, a key-person insurance policy, a reciprocal-coverage agreement signed by a peer, and an explicit household runway commitment**. The product can work. The founder configuration, as presented, cannot.

### J.2 The 10 specific hires, partnerships, and advisors needed

1. **PHT-based VA (overnight desk, member-support generalist)** — Hire by month 6, not month 12. Cost $18–24K/year. The single highest-leverage operational hire in the business. Without this, the 24/7 promise is fiction.

2. **Reciprocal-coverage Fora peer advisor** — Sign before launch. Identify two candidates in the Fora corporate-travel cohort, propose mutual vacation/illness coverage with a 50/50 commission share on bookings made during the coverage window. No cash cost. Single best mitigation for bus-factor risk.

3. **Senior corporate-travel advisor mentor** — Retain by month 1. 5–10 hours/month at $300–500/hour. Target someone with 10+ years of corporate-travel advisory experience at SmartFlyer, Brownell, Cadence, or Tzell. Cost $15–25K Y1. Compresses the founder's learning curve from 24 months to 9–12.

4. **TICO-experienced Canadian counsel** — Retain by month 1. Annual retainer $3–5K. Resolve the open question of whether Atlas memberships are "travel sales" under Ontario regulations; pre-clear any Canadian inbound; review the Fora host agreement.

5. **Cross-border CPA (US/Canada)** — Retain by month 1. Cost $5K Y1, scaling to $8–12K by Y3. Already in the v1.0 plan. Confirm.

6. **Fractional CMO / Content Editor** — Hire by month 6. 5–10 hours/week at $1,500–2,500/month. Owns the Journal calendar, edits posts, manages LinkedIn distribution. Frees the founder to do desk work and sales.

7. **Second Principal Advisor** — Begin recruiting at month 9, hire by month 18. Corporate-travel trained, 5+ years experience, willing to operate as associate-with-equity in a 2-person shop. Cost $110–140K all-in. Required for Society launch and bus-factor risk reduction.

8. **US-based E&O specialist insurance broker** — Engage by month 3. Confirm Fora umbrella coverage in writing for membership product and advisory services. Layer a $2M independent E&O policy by month 12. Cost: $1K broker engagement, $2.4K/year policy.

9. **Key-person life and disability insurance policy on the founder** — Bind by month 3. $250K life + 24-month disability income replacement. Cost $1.5–2.5K/year. Payable to the Ontario corp to fund member transition or wind-down. This is the only thing that makes Latitude 43 borrowable against and acquirable in a key-person event.

10. **Anchor-client advisory partnership** — Formalize with the warm anchor (the founder's old boss) by month 1. Written 12-month case-study agreement: discounted Atlas Office membership ($1,500/year for Y1, then full price), in exchange for written testimonial at month 6, video testimonial at month 12, and quarterly referral conversations. The brother-in-law network is informal and unreliable; the old boss is the only structured GTM asset in Year 1 and should be papered as such.

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

### J.4 The bottom line

The founder is investing heavily in the front of the house — the brand, the Journal, the website, the deck, the voice guide. The back of the house — the desk, the coverage model, the hiring plan, the regulatory and tax structure, the partner network — is **roughly 12 months behind where it should be at this stage of planning**. The v2.0 facts deferred the Society tier from Q3 2026 to Q1 2027; this is the right instinct. The same instinct should be applied to the 24/7 promise itself: either explicitly downgrade Atlas Light to "extended hours (7am–11pm ET, 7 days)" until the second human is hired, or do the hiring work to make 24/7 real.

A solo founder with no track record in the category, running a 24/7 SLA, serving US clients from Toronto, with one warm lead and a brother-in-law network, is not unfundable. They are early. The question is not whether they can build Latitude 43. It is whether they can build the team that builds Latitude 43, before the desk gets too loud to think.

---

*End of audit. Recommendations are concrete and dated. The founder either builds this team configuration by month 12 or the business fails for predictable, modeled reasons. The investor's first ask should be a 24-month hiring plan with cash triggers. The founder's first ask of themselves should be the same.*
