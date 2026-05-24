# 06 — Operations and Scaling (v3.0 Model B Unlimited)
## Latitude 43 · Operator evaluation · May 2026

**Lens:** What does it actually take to deliver a 60-minute SLA, 24/7, with all design included, from a one-person shop in Toronto routing US sales through Fora? Where does the operating model break first as the book grows from 5 members to 50 to 100? What is missing from the budget, the contracts, and the playbooks that an experienced operator would expect to see before signing the first MSA?

**Verdict (Grade: C+).** The v3.0 plan inherits the strongest operational documentation in the pre-revenue advisor category — a real IROP playbook, a 12-scenario hour-by-hour labor book, a member lifecycle document, a voice guide — and then erodes the credibility of that documentation by promising 24/7 60-minute coverage from a single founder backed by a single PHT VA whose actual hours are not staffed and whose cost is not in the budget. The Model B pivot (all design included) compounds the labor exposure relative to v2.0 by removing the per-trip fee that previously rationed demand. The plan is investable as a $300–500K ARR lifestyle practice with an honest SLA recut. It is not investable as written, because the SLA promise, the staffing plan, and the cost model do not agree with each other on any year between Y1 and Y5.

The findings below split into what is genuinely well thought through, what is questionable under realistic load, what is wrong or missing, and ten ordered fixes.

---

## A. What the plan gets right

### A.1 The IROP playbook is deployable, with caveats

`/operations/irop-playbook.md` is the best operational document in the file. Three things make it deployable rather than aspirational:

1. **The First 15 Minutes protocol is concrete.** Minute 0–2 acknowledgement language, minute 2–5 record open in Notion, minute 5–10 parallel-track sourcing, minute 10–15 two or three priced options to the member. A new advisor can run this from cold reading. The templates (A, B, C) are member-deliverable verbatim. This compares favorably to the actual SOPs in published TMC manuals.
2. **Tier 1 / 2 / 3 classification with explicit thresholds for waking the founder.** Section 7 names the discipline: Tier 2 waits for morning, Tier 3 wakes the founder. That single rule is what makes the 24/7 promise survivable for the founder past month 6. Without it, every overnight delay becomes a phone call and the founder is destroyed inside a quarter.
3. **The supplier hot-line sheet is real.** Air Canada Super Elite desk, United GS, AA ConciergeKey, LH HON, Marriott Bonvoy Ambassador One, Hyatt Globalist concierge, Blacklane priority dispatch, Carey ops. These are the lines an advisor actually calls. Most pre-revenue playbooks list the public 800 number. This one names the elite desks.

Caveats. Section 6 (the 2am Frankfurt scenario) describes "the overnight advisor (Marcus, Berlin time)" and Section 7 names "Berlin-based associate advisor on call" for Shift C. Neither person exists in the Y1 or Y2 hiring plan. The playbook describes a Y3 firm. The Y1 reality is one founder, one PHT VA, and the Fora overnight pool — which is other Fora advisors who happen to be online, not a contracted service.

This is not a fatal flaw. It is a documentation-versus-reality gap that needs to be closed before the first MSA is signed, by either (a) explicitly versioning the playbook ("v1.0 Y1 single-advisor operating mode" with a written §6a that handles the founder-asleep case) or (b) hiring the overnight advisor that the playbook already names.

### A.2 The scenarios book is the most honest labor accounting in the category

`/operations/scenarios-book.md` reports founder-hours per trip archetype, names the break-even scenarios (Sc. 1 NYC turn at 60 min and $130 net), names the loss-leaders (Sc. 6 roadshow at 41 hours), and refuses to use sales-deck math. Scenario 1 explicitly states "We do it because the membership baseline ($50/mo) recurs whether Marcus travels or not, and because nailing the simple trip is what earns the right to charge for the complex ones." That sentence is rare.

For an operator, the value of the scenarios book is not the dollars. It is the per-scenario labor estimate, which lets the founder compute a real load forecast. Under Model B Unlimited, the blended per-member labor numbers from the v2.0 evaluation still apply:

- Atlas Light: 35–55 founder-hours/year/member
- Atlas Office: 90–140 founder-hours/year/member (3 active travelers, shared orchestration overhead)
- Latitude Society: 180–260 founder-hours/year/member

At the Y5 base case (60 Light, 40 Office, 20 Society) that is roughly 10,750 service-hours/year — 5 to 6 FTE-equivalents at industry productivity. The Y5 budget covers approximately 2 FTE-equivalents (founder + 1 advisor + 1 VA, if the VA staffing is even doubled to cover overnight 7 days, which is not in the plan).

### A.3 Standing instructions and the supplier-data layer

The standing-instructions concept (room preferences, dietary, allergies, seat preferences, status numbers, card numbers, named drivers) is correctly stored once and applied every trip. The lifecycle document captures this at the orientation call in Day 5–7. The scenarios book demonstrates it in every scenario — Diane's Park Hyatt 3601 corner suite request to GM Marco by name, Marcus's high-floor-away-from-elevator note at the Whitby through front-office manager Jamie.

Operationally, the right place for this layer is not Notion (which is the current home per `/operations/member-portal-mockup.html`). It is a structured profile system with field-level audit trails and a per-supplier integration layer (Tern, Travefy, or Axus depending on tier). The plan partly acknowledges this in v2.0's operations annex but does not budget the migration. For Y1 with under 25 members, Notion holds. Past 50 members, Notion starts leaking — page-level permissions become a security risk, sync latency annoys the operator, and EA-turnover events (a multiplier the plan still underprices) compound the maintenance load.

### A.4 The text/SMS-as-primary-channel decision is correct

Members at the target ICP do not download apps and do not log into portals for routine requests. The 76% messaging-over-phone preference cited in `/tmp/v2-facts.md` matches what every EA-network survey reports. SMS-first with email-for-records is the right choice and matches the operational voice in `/operations/voice-guide.md`.

The implementation question — Twilio reliability, A2P 10DLC registration for US-bound SMS from a Canadian entity, member phone-number changes mid-trip — is treated as solved in the plan. It is not. See §C.3 below.

### A.5 The First 30 / 90-day no-fault exit, monthly Stripe billing

Monthly Stripe with a 90-day no-fault exit is the right billing posture. It eliminates the multi-year-contract objection in the sales call, aligns the firm's cash with the member's experience, and lets the firm off-board labor-negative members without legal friction. The aggregate refund liability is bounded (see lens 1 unit economics), and the 30-day Stripe accounting matches the operating cadence in `/operations/member-lifecycle.md`. This is structurally correct.

### A.6 The "all design included" promise — the buyer side works

The Model B pivot eliminates the unanswerable "what is the all-in?" question that killed Model A in the R6+R7 sims. From the buyer's perspective, this is a real improvement. From the operations side, it is also a simplification — the desk no longer has to track, quote, invoice, and collect per-trip fees on top of running the trip. That removes roughly 15–20 minutes of admin per trip across the desk surface, which at Office volumes (22 trips/member/year × 3 active travelers) is 5–7 hours/member/year of recovered labor. Modest, but real.

What this section does not address is the cost side of removing the rationing mechanism. That is the rest of the evaluation.

---

## B. What is questionable under load

### B.1 The single-PHT-VA staffing model does not cover the stated hours

The plan says PHT VA covers 11pm–7am ET. That is 8 hours/night × 7 nights = 56 hours/week of overnight coverage. **A single VA cannot legally or sustainably cover 56 hours/week.** The PHT employment norm is 40 hours/week (5 days × 8 hours), with overtime above. To actually cover 11pm–7am ET seven days a week the firm needs:

- Either 2 VAs working overlapping 5-day schedules (5 + 5 = 10 day-shifts, 7 of which are needed)
- Or 1 VA at 40 hours covering 5 nights and the founder absorbing the other 2 nights (which violates the founder's 7am–11pm coverage commitment on those days unless the founder breaks for 7 hours of sleep before 7am ET, which collides with the 7am Toronto start)

The honest staffing model is 2 PHT VAs at roughly $1,500–2,500/month all-in each ($18–30K/year each), so $36–60K/year of overnight VA cost. The plan's §14.2 operating cost line of "$4–6K/yr" for tools captures none of this. **The single largest cost-line omission in the plan is the second PHT VA.** It is $30–40K/year of structural cost that has to land somewhere.

Two paths reconcile this:

1. **Run founder-only 24/7 for the first 6 months** with an MSA flex clause ("60-minute target SLA on inbounds 7am–11pm ET; 90-minute target overnight; emergencies via voice line, sub-60 minutes always"). This is honest, defensible, and matches what the founder can actually deliver alone in Y1.
2. **Budget 2 PHT VAs from month 4** at $36–60K/year and re-cut the Y1 operating cost line accordingly. The founder draw stays at $0; the additional cost is paid out of subscription as it accrues. At month 4 the firm has roughly 5 members and $1,300/month of subscription, which does not cover even one VA. The realistic month-of-first-hire is month 8 with 12–15 members.

The plan should pick one path explicitly. Today it picks neither and quietly assumes a single VA covers 56 hours, which is not a real labor model.

### B.2 Founder coverage 7am–11pm ET, 7 days, is a 112-hour week before any selling

The founder's stated coverage is 16 hours/day × 7 days = 112 hours/week of desk-availability. Even if 70% of those hours are passive (waiting for a text) and 30% are active service work, that is 33 hours of active desk work per week. Add the 100/day cold email program (~3 hours/day × 5 days = 15 hours/week), the newsletter cadence (Desk Diary 2x/week + 43rd Parallel monthly = roughly 8 hours/week), monthly Latitude Reports digests for every member, quarterly trip-pattern reviews, Society quarterly Year-in-Review hosting, FAM trips, taxes, and the Renmac primary income — and the founder is structurally over capacity from member #12.

The biology of the 24/7 SLA solo is straightforward. Assume one Atlas member generates one async desk-touch every 36 hours with ~30% concentration in 11pm–7am ET. At 12 Atlas members, the probability of at least one overnight inbound any given night is over 85%. At 20 members it is functionally 100%. The founder is woken every night the PHT VA does not catch the inbound.

The plan's risk register R10 (founder primary income falls) and R1 (single-founder bus risk) acknowledge the fragility but do not specify the operating limits. **Specify them.** A defensible written SLA reads:

- 60-min first response, 7am–11pm ET, 7 days, on inbound text to the desk line
- 90-min first response, 11pm–7am ET, on inbound text
- Sub-60 min always on the emergency voice line for declared emergencies
- The desk closes for 4 documented weeks/year (e.g., 1 week in March, 1 in August, 1 in October, 1 between Christmas and New Year); during those weeks the backup principal at Fora carries the line at the same SLA

That is industry-leading and survivable. The current language ("60-minute SLA, 24/7, founder 7am–11pm, PHT VA 11pm–7am") is industry-leading and not survivable.

### B.3 Labor-negative member risk under Unlimited

Model A's per-trip design fee was a rationing mechanism. Model B removes it. The plan acknowledges the risk in §5.3 and proposes three protections: the 3-active-traveler cap on Office, the PHT VA hire, and the quarterly trip-pattern review. Each is partly load-bearing and partly aspirational.

Run the threshold math. An Atlas Office member at $349/mo generates $4,188 in annual subscription. Founder labor at a fully loaded $125/hour (which is conservative for a billable advisor) breaks even at 33.5 hours of design work per year per Office member. The unit economics imply 22 trips/year × 3 active travelers = 66 trip-events, and the scenarios book reports a weighted average of 4–6 founder-hours per Office-style trip when orchestration overhead is shared. **The mid-case Office member consumes 90–140 hours/year against a $4,188 subscription. The break-even threshold is 33 hours. The mid-case Office member is already labor-negative on subscription alone before commission revenue arrives.**

Commission revenue rescues this. Office mid-case commission is $2,250–2,800/year at 7.8% effective on $30K of hotel spend, plus personal-travel commission. Total Y1 economics per the plan are $7,844–$8,894. At $125/hour fully loaded, the break-even labor band is roughly 62–71 hours/year. Mid-case load is 90–140. **Most Office members run 1.3x to 2x labor-negative on a fully loaded basis** before the firm captures any indirect value from referrals, retention, or upgrade to Society.

This is not a fatal finding. Two correctives:

1. **The 3-active-traveler cap is the binding mechanic** and has to be enforced in the MSA, in the welcome packet, in the orientation call, and in the trip-tracking system. The plan mentions it once. It needs to be load-bearing across the entire onboarding stack.
2. **The quarterly trip-pattern review is engineered, not vibes.** Specify a triggered review: any Office member exceeding 50 founder-hours in a single quarter, or 150 founder-hours trailing four quarters, triggers a documented conversation with three outcomes — (a) Society upgrade, (b) scope reset with the member at the existing fee, (c) friendly off-board at next anniversary. Without that mechanic, the quarterly review is a vibe and the labor exposure compounds.

The break threshold on trip count per Office member is roughly 12–14 designed trips/year per active traveler before the member becomes labor-negative in a serious way. A heavy-using PE operating partner pulling 28 trips/year on a single Office seat with two designated travelers running 18 each is the failure mode. The plan needs to name it and price for it.

### B.4 Quarterly trip-pattern review — engineered or vibes?

Today it is vibes. The plan describes a "15-minute call to flag overspend, under-utilization, or rotation issues." There is no trigger threshold, no escalation tree, no template, no script, no documented outcome path. Compare to the IROP playbook, which has all of those.

The engineered version needs three things: (a) a quantitative trigger (hours, trips, IROP frequency, or spend), (b) a documented conversation with three named outcomes, (c) a logged decision in the member's relationship record. The lifecycle document provides the framework at the renewal conversation. It does not provide it at the quarterly. Build the quarterly review template before the first Office member onboards.

### B.5 The 3-active-traveler cap on Office — enforcement infrastructure missing

The cap appears once in the plan body and once in the table. It does not appear in:

- The MSA language (which does not exist in the repo yet)
- The welcome packet or onboarding script (`/operations/onboarding-kit.md` referenced but the cap is not visibly drafted into it)
- The trip-tracking system (Notion-based per the mockup, no field for "active traveler count")
- The quarterly review template (does not exist)
- The sales-call playbook (`/sales-kit/discovery-playbook.md`, referenced)

For the cap to be load-bearing, it has to be in all five places. Without enforcement infrastructure, the cap is what a litigator would call illusory — promised but unenforceable.

### B.6 Founder vacation, illness, family — no real continuity plan

The plan's risk register R1 cites "Backup principal pre-staged at Fora; documented SOPs; member SLA flex clause in MSA." None of those three deliverables exist in the repo. There is no named backup principal, no signed agreement with another Fora advisor for coverage, no SLA flex clause in any MSA draft, and no rehearsed handoff. The Fora overnight pool is not a contracted service.

The honest continuity plan needs four elements:

1. **Named backup principal at Fora** with a signed reciprocal coverage agreement, paid retainer (~$500–1,000/month), and 4 paid weeks/year of full desk coverage.
2. **Documented handoff packet** — every active trip, every standing-instruction profile, every supplier hot-line, every IROP-in-progress — accessible to the backup in a secure shared system. Not Notion, because Notion's page-level permissions leak.
3. **Two scheduled founder-off weeks per year minimum** with full backup coverage, marketed to members in advance ("the desk is on rotating coverage March 14–21, your lead advisor for that week is [Name]").
4. **Illness / emergency protocol** — a triggered text-cascade that informs members within 4 hours when the founder is offline for >24 hours.

None of those four exist in the v3.0 plan. Each is a 1-week build. None of them is in the cost model. The backup principal retainer alone is $6–12K/year.

---

## C. What is wrong or missing

### C.1 Twilio / SMS reliability and the cross-border phone-number problem

Text/SMS as the primary channel works only if the SMS layer is reliable, compliant, and resilient to member phone changes mid-trip. The plan treats this as solved. It is not.

Specifically:

- **A2P 10DLC registration** for US-bound SMS from a Canadian operating entity (Latitude 43 Inc., Ontario CCPC) requires US carrier campaign approval, brand vetting, and use-case registration. Without it, throughput is throttled to ~30 SMS/day to US carriers and message delivery is unreliable. Setup time: 4–8 weeks. Cost: $200–500/year plus per-message fees. Not in the budget.
- **Twilio reliability** is 99.95% nominally but the failure modes that matter are not platform-wide outages — they are individual delivery failures (carrier filtering, recipient handset issues, roaming gateway problems). For an SLA product, the firm needs a fallback channel that triggers when an outbound message is not delivered within X minutes. Twilio supports delivery receipts but the operational discipline of acting on them is not in the playbook.
- **Member phone changes mid-trip.** A member who swaps SIMs on landing in Europe, or whose corporate IT pushes a new device mid-trip, breaks the SMS thread. The IROP playbook does not address this case. The fix is an enrolled secondary contact (email + a documented voice line) and a check on the orientation call that the member's roaming behavior is known.
- **WhatsApp Business** is the international-traveler standard and the plan does not specify whether it is the primary or backup. For a member traveling in Asia, SMS is functionally dead; WhatsApp is the channel.

Recommend: WhatsApp Business as primary for international itineraries, SMS as primary for US-domestic, email as redundancy on both, voice line as last resort. Documented in `/operations/communication-protocol.md` (does not exist; create it).

### C.2 Tools stack — actual monthly cost is not $4–6K/yr

The plan §14.2 says "$4–6K/yr operating" for Fora monthly fee, Stripe, Apollo, Smartlead, Notion, Substack, Honeybook. Let me total this honestly:

| Tool | Monthly | Annual |
|---|---:|---:|
| Fora platform fee (advisor) | $100 | $1,200 |
| Stripe (no monthly fee, 2.9% + 30 cents per txn) | $0 | ~$2,400 in fees on $80K subscription Y1 |
| Apollo (sales eng) | $99 | $1,188 |
| Smartlead (cold email) | $94 | $1,128 |
| Notion (team) | $20 | $240 |
| Substack (Pro tier optional) | $0 / $50 | $0 / $600 |
| Honeybook | $39 | $468 |
| Twilio (SMS A2P) | $30 | $360 |
| WhatsApp Business API (via BSP) | $50 | $600 |
| LinkedIn Sales Navigator | $99 | $1,188 |
| Calendar / scheduling (Calendly or similar) | $15 | $180 |
| E&O insurance (independent $2M) | $200 | $2,400 |
| Email / domain / hosting | $25 | $300 |
| Tern CRM (if adopted) | $99 | $1,188 |
| **Subtotal tools** | | **~$11–13K/yr** |

Plus payment processing fees on subscription ($2,400 on Y1, scaling to $20K+ by Y5), plus the missing PHT VA cost ($36–60K/year for 2 VAs), plus the backup principal retainer ($6–12K/year), plus E&O premium independent of Fora ($2K+/year from day one because the membership product is not covered under Fora's umbrella).

**Realistic Y1 operating cost: $55–80K, not $4–6K.** This is an order-of-magnitude error in the plan. It does not change the lifestyle-business thesis (the founder's primary income from Renmac absorbs it), but it changes the founder-draw math and the time-to-positive-cash-from-Latitude meaningfully.

### C.3 Scaling thresholds — what breaks first

Walking the book from 5 to 50 to 100 members, the binding constraints in order of arrival:

**At 5 members.** Nothing breaks. Founder runs everything from a phone. Notion holds. The IROP playbook is honored on adrenaline.

**At 12 members.** The 24/7 SLA breaks the founder. P(overnight inbound) exceeds 85%. The PHT VA hire becomes urgent regardless of the budget. The founder's sleep degrades. Cold email cadence drops because the founder is recovering. This is month 6–9 in the plan's Y1 trajectory.

**At 20 members.** The text-thread cognitive load exceeds what one person can hold. Members start getting the wrong context in replies. The voice guide's "names over nouns" becomes harder to maintain. Quality erodes invisibly — the member notices the third miss, not the first or second. The labor-negative Office members (10–15% of the book per the v2 evaluation) start consuming disproportionate time.

**At 30 members.** Notion's page-level permissions become a real security risk. Some EA at one Office account sees a snippet of another member's standing instructions. The founder has not built a profile-management system because the founder has been running trips. The first off-board happens for a reason that is not the member's fault. The retention conversation in the lifecycle document is invoked but not yet rehearsed.

**At 50 members.** The plan's PHT VA staffing is exposed as undersized. The IROP playbook's "Berlin associate" is exposed as fictional. The quarterly trip-pattern review is exposed as a vibe. The founder is doing 70-hour weeks and the primary income is at risk. The "named human" promise has been quietly redefined into "the desk" without telling the early members. The first LinkedIn post from a departed member becomes a non-trivial possibility.

**At 80 members.** This is where the plan claims to operate at Y3. Without 2–3 advisors and a dedicated ops manager, it does not operate. The realistic load is 5,000–6,000 service hours/year against 1,800–2,500 founder-available hours.

**At 100 members.** Outside the realistic founder-only universe by a factor of 3. The Y4 plan budgets a single $85K associate. The operating reality requires a 4–5 person team.

### C.4 Hire #2 — when, role, cost

The plan budgets one associate in Y4. The operating reality says hire #2 should happen at month 18–24 (member count 35–50), not month 36+. The role is **senior advisor**, US-based, Sabre-trained, IROP-capable, all-in cost $85–120K. Funded by Y2 subscription run-rate plus founder forgoing draw through Y2.

Hire #3 — the operations manager — is needed by month 30 at member count 60+. Profile management, IROP log audit, billing reconciliation, EA-turnover re-onboarding, Tern/Notion migration. All-in $90–120K.

Hire #4 — the second senior advisor — is needed only if the Society tier launches at scale (>8 members). If Society is capped at 6 members through Y4 (which is the right call given the 15-min SLA math), hire #4 deferred to Y5 or Y6.

**Total Y3 labor cost in the honest model:** $200–250K. Plan budgets ~$80K. **Gap: $120–170K.** That gap is the most consequential financial finding from the operations lens and it has not changed between v2.0 and v3.0.

### C.5 IROP playbook deployability score

Section-by-section deployability for Y1 operations:

| Section | Y1 deployable? | Notes |
|---|---|---|
| §1 IROP definition | Yes | Cleanly written |
| §2 First 15 Minutes | Yes | Templates and named systems |
| §3 First Hour + supplier hot-lines | Yes, with caveat | Hot-lines need contact verification before first IROP; some are aspirational |
| §4 Tier 1/2/3 decision tree | Yes | Explicit thresholds |
| §5 Communication templates | Yes | A and B verbatim deployable; C needs voice protocol |
| §6 2am Frankfurt scenario | **No** | Names "Marcus, Berlin advisor" who does not exist |
| §7 Handoff protocol | **No** | Three shifts assumes three advisors; Y1 has one |
| §8 Post-IROP debrief | Yes | Cleanly written |
| §9 IROP log | Partial | Notion is wrong system for 7-year retention of Tier 3 cases |

Overall: deployable for Tier 1 and most Tier 2 incidents under solo operation. Not deployable for Tier 3 concurrent or overnight incidents without (a) the named Berlin advisor that does not exist, or (b) an honest documented fallback (founder is paged, member is voice-called from Toronto regardless of hour, Fora pool is reserved for triage acknowledgement only).

**Recommend a v1.1 of the playbook with a §6a "Solo-mode operating overlay" that names the actual Y1 fallback.**

### C.6 Quarterly trip-pattern review — template not in repo

The plan promises the mechanic. The mechanic does not exist in the operations folder. Build it before the first Office member onboards. One-page template: trigger thresholds, three-outcome decision tree, member-facing script, internal log entry. 2-hour build. Single largest operational lever for managing labor-negative members.

### C.7 EA Companion Seat — operational tax not modeled

Each Office member brings an EA. EA tenure at Series A–C startups is 14–18 months. Across 40 Office seats by Y5, expect 25–30 EA turnover events per year, each requiring a re-onboarding (~2 hours), fresh consent-to-act, fresh trust-build. That is 50–60 hours/year of founder time on EA churn alone — roughly 3 weeks of full-time work hidden in "maintenance."

The plan does not budget this. The lifecycle document covers initial onboarding well; it does not address EA replacement. Add an EA-turnover SOP and budget the labor.

---

## D. Ten recommendations, prioritized

1. **Re-cut the SLA to honest language before MSA #1 is signed.** 60-min 7am–11pm ET, 90-min 11pm–7am ET, sub-60-min on emergency voice line at all hours, desk closed 4 documented weeks/year with backup principal coverage. Industry-leading and survivable.

2. **Budget 2 PHT VAs from month 8, not 1 from month 4.** $36–60K/year. Adjust the operating cost line in §14.2 from "$4–6K" to "$55–80K." This does not break the lifestyle thesis but it does change the founder-draw math.

3. **Sign a backup principal at Fora with reciprocal coverage MSA.** $500–1,000/month retainer, 4 paid weeks/year of full coverage, named in every onboarding packet. Build the handoff packet before the first vacation.

4. **Pull hire #2 (senior advisor) forward to month 18–24.** $85–120K all-in. Funded by Y2 subscription plus deferred founder draw. This is the single largest plan revision and the operationally non-negotiable one.

5. **Build the quarterly trip-pattern review template before the first Office member onboards.** Quantitative triggers (50 founder-hours/quarter, 150 trailing four quarters), three named outcomes, member-facing script, internal log. One-page SOP.

6. **Enforce the 3-active-traveler cap across MSA, onboarding kit, trip-tracking, quarterly review, and sales playbook.** Five places. Each is a 1-hour build. Without all five, the cap is illusory.

7. **Pick the communication channel stack explicitly.** WhatsApp Business primary for international itineraries, SMS primary for US-domestic, email redundancy, voice line on emergency. A2P 10DLC registration started day 1 (4–8 week lead time). Document in `/operations/communication-protocol.md`.

8. **Migrate IROP log out of Notion to an audit-trail system by month 18.** Linear, Jira Service Management, or a custom Postgres build. 7-year retention on Tier 3 cases is a legal exposure Notion does not defensibly cover. $5–15K migration cost.

9. **Carry independent $2M E&O from day 1.** $1,800–2,400/year. The Fora umbrella covers booking activity; it does not cover the membership product, the advisory layer, the Journal, or the IROP recovery itself. First claim without coverage is existential.

10. **Write a v1.1 of the IROP playbook with a Solo-mode overlay.** Name the actual Y1 fallback for §6 (2am Frankfurt with no Berlin advisor) and §7 (three-shift handoff with one advisor). Honest documentation today protects the brand tomorrow.

---

## E. Closing operator note

The v3.0 plan is selling a Knightsbridge Circle service standard on a Bell & Bly footprint with an Embark headcount budget. Two of those three numbers have to move.

The Model B Unlimited pivot is the right strategic call. It also raises the operational bar by removing the per-trip fee that previously rationed demand. The plan acknowledges the labor-margin risk in §5.3 but does not engineer the controls (the cap, the quarterly review, the off-board mechanic) tightly enough for the controls to actually bind.

The IROP playbook, the scenarios book, the lifecycle document, and the voice guide together form the strongest pre-revenue operational artifact set in the category. They describe a Y3 firm. The Y1 firm — solo founder, 1 PHT VA at month 4, no backup principal, no independent E&O, Notion as the system of record, no quarterly review template, no MSA in the repo — is two work-weeks away from being operationally honest.

The lifestyle thesis survives all of this. The investability of the plan as a $500–800K ARR Y5 practice survives all of this. What does not survive without the ten fixes above is the brand promise of "the named human, 60 minutes, 24/7, all design included" at the moment that promise is stress-tested — which the plan's own scenarios book shows happens roughly twice in the first 90 days of any member relationship.

The right answer is not to soften the promise. The right answer is to staff and document it honestly. The plan today does neither. The fixes are small. The cost of not making them is one LinkedIn post from a credible buyer in Y2.

**Grade: C+.** Investable conditional on (1) earlier and larger VA staffing, (2) earlier senior-advisor hire, (3) honest SLA recut, (4) the seven operational documents listed above written and in the repo before MSA #1 is signed, (5) the backup principal contract signed and the handoff packet built. Without those five, the operating model breaks somewhere between member 20 and member 35, which is inside Y2 of the plan's own trajectory.

---

*End of operations evaluation.*
