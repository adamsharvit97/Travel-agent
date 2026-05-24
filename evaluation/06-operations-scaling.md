# 06 — Operations & Scaling Risk
## Latitude 43 · Pre-revenue investor evaluation · May 2026

**Lens:** What breaks operationally as the firm grows from 1 to 120 members? Where do the v2.0 promises (60-min SLA Atlas, 15-min SLA Society, EA Companion Seat, the "named human") collide with the biology of a single founder, the latency of overseas labor, and the failure modes of a Notion-and-Slack stack?

**Ground truth:** `/tmp/v2-facts.md`. Operational artifacts: `/operations/scenarios-book.md`, `/operations/irop-playbook.md`, `/operations/member-lifecycle.md`, `/operations/voice-guide.md`, `/operations/member-portal-mockup.html`, and `/business-plan.md`.

**Posture:** Sharp, not destructive. The IROP playbook and scenarios book are better than most pre-revenue ops documentation. But the stated hiring trajectory (founder solo Y1, PHT VA month 9-12, associate Year 4) is materially out of sync with the operational load implied by the scenarios book and the SLAs implied by the Society tier. That gap is the central risk.

---

## A. Operational breakdown thresholds

The scenarios book gives a granular labor estimate per trip-type. The Y5 base case is **120 paid seats** (60 Light + 40 Office + 20 Society). The question is not whether the founder can build a business at that scale — it's at what member count each constraint binds, given founder-solo Y1 and the deferred hiring plan.

### A.1 Inputs: realistic founder-hour load

From the scenarios book (the most credible labor accounting in the file):

| Trip archetype | Founder hours | Annual frequency per Light/Office member | Annual frequency per Society principal |
|---|---:|---:|---:|
| Simple same-day or 2-day (Sc. 1, 3) | 1.0 | 8–14 | 6–10 |
| Mid-week 4-day (Sc. 2) | 3.8 | 6–10 | 8–14 |
| Multi-pax offsite (Sc. 4, 5) | 13–18 | 0.5–1 | 1–2 |
| Roadshow (Sc. 6) | 41 | 0.2–0.5 | 1–2 |
| Complex international (Sc. 7, 8) | 18–20 | 0.5–1 | 2–4 |
| Hybrid biz/family (Sc. 9) | 11.5 | 0.5 | 1–2 |
| Leisure project (Sc. 10) | 27 | 0 (priced separately) | 1–2 |
| IROP / crisis (Sc. 11, 12) | 2.5 | 1–2 | 3–5 |

Blended **per-member founder-hours/year** by tier (mid-point estimates):

| Tier | Hours/year/member | Source |
|---|---:|---|
| Atlas Light (1 traveler, 18 nights) | 35–55 | Scenarios 1, 2, 3 weighted |
| Atlas Office (~3 active travelers) | 90–140 | Light × 2.5 (not 3x — orchestration shares overhead) |
| Latitude Society (4 family travelers, leisure-heavy) | 180–260 | Higher complexity per scenario, more IROPs, hosting layer |

### A.2 The four-line breakdown chart

A founder doing 60 working hours/week has ~2,800 productive hours/year after factoring in selling, the Journal (52 posts = ~150 hr), FAM trips, admin, taxes, vacation, and the structural overhead of being the only person who exists. **Of that, perhaps 1,800 hours are available for member service.** 80-hour weeks push this to ~2,500 service hours but at a quality cost that compounds.

| Member count (mix per plan) | Implied service hours | Founder solo at 60h/wk (1,800h capacity) | At 80h/wk (2,500h capacity) |
|---|---:|---|---|
| **10 (8L / 2O / 0S)** | ~520 | Comfortable | Comfortable |
| **22 (Y1 plan: 22L / 8O / 0S)** | ~1,890 | **At breaking point** | OK |
| **30 (Y2-ish: 22L / 8O / 0S)** | ~2,100 | **Broken** | Strained |
| **51 (Y2 plan: 35L / 15O / 1S)** | ~3,520 | **Impossible solo** | **Impossible solo** |
| **80 (Y3 plan: 50L / 25O / 5S)** | ~6,150 | Requires 2–3 FTE equivalent | Requires 2–3 FTE equivalent |
| **120 (Y5 plan: 60L / 40O / 20S)** | ~10,750 | Requires 5–6 FTE equivalent | Requires 5–6 FTE equivalent |

**The founder breaks (60-80 hr/week sustained) between member 18 and 25.** This is *during Y1*, not Y2. The plan's milestone of "30 accounts by month 18" sits squarely inside the breakdown band. The PHT VA arriving at "month 9-12" only buys back overnight admin time (per the IROP playbook the VA explicitly does not touch live IROPs), so it shifts the breakage by perhaps 2-3 members, not 20.

### A.3 The 24/7 SLA breaks solo at ~12 members

A 60-min SLA, 24/7/365, is biologically untenable solo. Assume each Atlas member generates one async desk-touch every 36 hours, Poisson-distributed with ~30% concentration in 11pm-7am ET (members in Asia, Europe, or just-landed). At **12 members**, P(at least one overnight message any given night) > 85%. At 20, it's ~100%. **The founder is woken every night.**

The Y1 backstop ("Fora global network + emergency line") is unspecified. The IROP playbook itself assumes a "Berlin-based associate advisor on call" — not in the Y1 hiring plan, not in the Y1 cost line. **There is a backstop in the SOP that is not in the budget.**

### A.4 EA Companion Seat onboarding goes from feature to operational tax

The EA Companion Seat creates a second profile per Office/Society member — second loyalty set, second preferences, second consent-to-act flag, second human who can open the desk in the principal's name. Onboarding takes ~2 hours per profile per the lifecycle doc.

| Office + Society members | EA seats | Annual onboarding hours | Annual maintenance (profile refresh, password resets, EA turnover) |
|---:|---:|---:|---:|
| 8 (Y1) | 8 | 16 | 16 |
| 16 (Y2) | 16 | 32 | 32 |
| 30 (Y3) | 30 | 60 | 60 |
| 60 (Y5) | 60 | 120 | 120 |

**EA turnover is the silent multiplier.** EA tenure at Series A-C startups is ~14-18 months; at family offices ~3 years. Across 60 Office+Society seats by Y5, expect **20-30 EA churn events/year** — each a re-onboarding, fresh consent, fresh trust-build. **Unmanageable by month 30 without dedicated profile-management infrastructure and ≥0.25 FTE of ops support.**

### A.5 The Society 15-min SLA is unholdable solo at ~3 members

15-min SLA is 4x tighter than Atlas. Combined with "dedicated principal," it means the founder personally is on the hook 15-min, 24/7, per Society member.

N=1: founder lives on the phone — manageable. N=3: cannot reliably sleep, eat dinner, or be in a meeting without a phone-down policy. N=5: mathematically violable any night the founder sleeps >4 consecutive hours. **Solo-feasible at N=1, marginal at N=2, fictional at N=3+** — the Y5 plan calls for 20.

A 15-min SLA cannot be met by a Manila VA who is not licensed to make sub-$10K commitments on behalf of a Society principal mid-crisis. The VA pool is an answering service, not a substitute.

### A.6 Fora host infrastructure constraints

- **Commission split tiered on personal sales.** 90/10 only at $2M GBV. The Y5 base case has the founder still at 80/20.
- **Fora is consumer-leisure-first.** Tern, Axus, Notion are bolted on — two of three core SaaS layers (CRM, itinerary, portal) are *outside* Fora's stack and unsupported.
- **Sabre access is via Fora.** Host agency GDS contracts get renegotiated routinely. "Migrate within 90 days" understates the cost: every profile, PNR history, and commission record lives in Fora.
- **Fora's E&O umbrella covers "activities performed in the Fora system."** The membership product, advisory work, Notion portal, Slack channels — none of that is. The independent $2M E&O is needed from Day 1, not Y2.

If Fora hits a product or commercial wall in 2027-2028, every advisor on the platform shares the wall.

---

## B. Scaling the desk

### B.1 The "named human" promise vs. operational reality

The lifecycle doc promises a **lead advisor** plus a **named successor advisor**. In Y1, the founder is both. **The named-successor promise is broken on day one and only becomes true at month 24+.** Members who join in months 1-24 were sold a structural promise the firm cannot yet deliver.

Recoverable, but the plan needs (a) explicit Y1 disclosure ("your lead is the founder; named backup appointed by Q3 2027") and (b) honesty that Light/Office members will get a structurally less-personal experience starting in Y3 when associates take over day-to-day.

### B.2 When does the desk become a pod (and break the promise)?

The promise — one name, one phone, one inbox — survives until two operational events:

| Event | When | Why it breaks the promise |
|---|---|---|
| First non-founder takes a member's call | Month 12–18 (PHT VA hire) | The VA is not "Sarah K." The member learns the desk is multi-person |
| First lead-advisor handoff (member changes lead) | Month 30–36 | The member explicitly notices that their "named human" was a placeholder |
| First trip executed entirely by associate, founder absent | Month 36–48 | The founder's relational equity stops being the product |

The member who closed on "the founder is your desk" feels something else when an associate emails them. The repeat-member NPS gap between "founder-served" and "associate-served" in boutique advisories is consistently 15-25 points. **The pod transition is a churn event, not a feature.**

### B.3 The Society 1:6 ratio at 30, 60, 100 members

Industry benchmarks for UHNW concierge: Quintessentially ~1:8, Knightsbridge Circle ~1:5, Société Anonyme ~1:6. At 1:6, each advisor carries ~1,400-1,800 saturating hours/year.

Applied to the Society cap of 30 (Y5 plan: 20 active):

| Society members | Required dedicated advisors at 1:6 | Burden on founder if no advisor hired | All-in cost of advisor team |
|---:|---:|---|---:|
| 5 (Y3) | 1 (the founder) | 1,200 hrs/yr — half the founder | $0 (sunk) |
| 12 (Y4) | 2 | Impossible solo | $180–240K |
| 20 (Y5 base) | 3–4 | Impossible solo | $360–480K |
| 30 (cap) | 5 | n/a | $600–750K |

The plan budgets one associate advisor at $85K all-in in Y4 and a second + ops manager in Y5 at $140K incremental — total advisor-tier headcount ~$225K. **The Y5 budget covers roughly half the advisor team the Society SLA actually requires.** This is the single largest cost-line understatement in the operating plan.

Two paths out: (a) re-cut Society economics so the per-member fee fully covers a dedicated advisor (which would push Society pricing toward $4-6K/mo, not $1-2.5K/mo — i.e. closer to Knightsbridge Circle), or (b) cap Society at 6-8 members across Y3-Y5 and accept that it is a brand line, not a revenue line.

### B.4 What does a 24/7 desk that actually scales cost?

A true 24/7 staffed desk — three 8-hour shifts, 7 days/week, with backup capacity for vacation and sick days — requires a minimum of **3.5 FTE-equivalents per "named-human" line**. At reasonable all-in costs:

| Role | Coverage | All-in/year | At what member count is it required? |
|---|---|---:|---|
| Founder (always there) | 0700–2200 ET, 5 days, with on-call | $0 (sunk) | 0 |
| PHT VA, 5×8 overnight | 2300–0700 ET, M–F | $18–24K | ~15 |
| PHT VA, 7×8 overnight | 7-day cover | $30–40K | ~30 |
| Associate advisor, US-based | Full-time, business hours US backup | $85–120K | ~40 |
| Lead advisor (second senior) | Pod model, business hours | $130–160K | ~80 |
| Operations manager | Profile mgmt, IROP log review, billing | $90–120K | ~80 |
| EU/UK overnight advisor (Berlin) | Live IROP capable in NA night | $100–140K | ~50 (or Society launch) |
| Asia-Pacific overnight (Singapore) | Live IROP capable | $80–110K | ~100 (or with first Asia-heavy Society principal) |

**Realistic fully-staffed desk by Y5 (120 members):** $580–760K/year in labor before benefits, technology, supervision overhead. **The plan budgets $225K of advisor headcount in Y5 (associate + second associate or PHT lead + ops manager).** The gap is 2-3x.

This is the single most consequential financial finding in this evaluation. The business is sellable, but it must be sold as a firm that absorbs a much larger labor cost in Y4-Y5 than the current model assumes — *or* the SLA must come down (60-min → 4-hour outside business hours, 15-min Society → 30-min business hours / 60-min overnight). Either the cost goes up or the promise comes down. Both are recoverable; pretending neither is necessary is not.

---

## C. Failure modes per scenario

The scenarios book is unusually candid — it admits Scenario 6 (the roadshow) loses money on labor, and that Scenarios 11/12 (IROPs) lose money by design. The investor question is which of these failure modes get worse, not better, at scale.

| # | Scenario | Failure at member 20 | Failure at member 50 | Failure at member 100 | Where quality degrades | Where mistakes get expensive |
|---|---|---|---|---|---|---|
| 1 | NYC 2-day | None — founder still loves these | Trip itself fine; founder skips proactive touches | Trip is rushed; pre-arrival emails to Whitby stop happening | Pre-arrival relationship-building drops | One bad GM interaction → upgrade stops happening → member notices |
| 2 | SF 4-day VC | None | Daily morning brief becomes templated | Brief is wrong on weather / gate; member texts a correction | Personalization erodes | LP-host dinner with wrong wine flagged → relational damage to *the member*, not us |
| 3 | Same-day turn | None | Standby car coordination breaks (no one watching the calendar between flights) | Member texts mid-meeting "can car come now"; nobody picks up for 18 min | Real-time responsiveness | The whole point of the trip — making hockey practice — gets blown |
| 4 | Miami offsite | Some sub-itinerary errors (wrong dietary, room mismatch) | One of five rooms not upgraded; partner notices | One of nine PNRs ticketed wrong; partner missed a flight | Multi-pax coordination | $50K of E&O exposure if a partner missed a portco closing |
| 5 | re:Invent 10pax | Manageable | Conference housing block deadline slips; one engineer ends up at the Linq | Accessible room (Sam's) not actually confirmed; he arrives to a non-accessible room | Edge-case detail follow-through | Disability access failure → ADA-adjacent press story |
| 6 | Roadshow 18 mtgs | Founder takes 40+ hrs but holds it | Founder cannot — must delegate live war-room ops to associate who doesn't know LPs | War room is hours behind; the 5am DCA-CHO recovery doesn't happen | Real-time recovery quality | Anna's Fund III roadshow miss → "Latitude 43 cost me $20M of LP commits" story |
| 7 | NYC-LDN-GVA-ZRH | Founder still doing this personally | Pre-arrival emails to three GMs become one generic templated note | At least one upgrade misses because relationship outreach was perfunctory | GM relationships go cold | David's diligence trip → wrong room, wrong amenity, *complaints to other PE peers* |
| 8 | Asia + IROP | IROP recovery still founder-led; lift OK | Founder asleep during Asia day; VA takes the typhoon call but is not authorized to spend $45K on private jet | Wrong call gets made on a Tier 2/3 split; LP meeting missed | IROP judgment under fatigue | Priya's typhoon → meeting lost → reputational damage |
| 9 | Schwab + Aspen (hybrid) | Spousal channel ("text Lisa direct") is clean | Texting Lisa happens during the founder's only family weekend; Lisa gets a 9-hour-late reply on the meltdown | Lisa stops trusting the desk for the kid stuff; Robert hears about it | Family-side trust erodes | One bad ski-school morning becomes the "they're not for families" story |
| 10 | Italy anniversary | Founder personally invested | Junior associate builds the trip; Caroline notices the rooms aren't quite right | Anniversary trip is fine but feels like *any* travel agency could have done it | The orchestration polish drops | Le Sirenuse room mismatch → "I paid a premium for the same trip my friend booked herself" |
| 11 | FRA 2am IROP | Founder is alive at 2am, takes the call | Founder is asleep; PHT VA cannot reach Cathay HON desk because the relationship is the founder's, not the VA's | Founder cannot answer because Society principal in Aspen has a 15-min SLA at the same moment | Concurrency under crisis | Devin loses the BOM meeting → $4M of optionality at risk → very public rage |
| 12 | SAO visa | Same as 11 | Same | Same — plus the consulate trade-attaché relationship is the founder's; nobody else can call it | Edge-case relationship capital is non-transferable | Sarah's $80K Brazil deal blows up → testimonial reverses |

**The pattern:** quality degrades first in the *pre-arrival relationship layer* (the GM emails, the named driver, the maître d' phone call). This is invisible to the member for 2-3 trips, then suddenly visible all at once when a stack of small misses compound into a "this isn't what I signed up for" moment. The lifecycle doc anticipates this with the 90-day check-in and the renewal conversation, but neither mechanism catches the slow erosion across months 6-18.

**The expensive mistakes** (E&O exposure, refund liability, bad press) cluster in Scenarios 4, 5, 6, 11. These are the trips that should carry the highest service oversight and the most pre-trip review. The current model treats them as routine workload.

---

## D. The IROP playbook stress test

The IROP playbook is the best operational document in the file. It is also written for a firm that does not yet exist.

### D.1 The 2am Frankfurt scenario — does it hold solo?

Playbook §6: *"The overnight advisor (Marcus, Berlin time) receives the cancellation alert within 90 seconds."* In `/tmp/v2-facts.md`: the founder is solo, in Toronto, with no Berlin advisor and no Y1 hiring budget for one. **The playbook describes a Y3 firm.**

In Y1, FRA 02:00 = ET 20:00 — founder still awake, fine. The hard case is concurrent: Devin's FRA cancellation while the founder has a Society principal mid-IROP in Aspen and a roadshow member needing a 05:00 brief in London. Three Tier 2s, one human, one hour.

The playbook does not handle concurrency. Tier classification assumes serial incidents. **Concurrent Tier 2s break the playbook above ~15 members** because P(simultaneous IROPs) scales with the square of trips-in-flight.

### D.2 Fora's overnight pool — what's the real handoff quality?

"Fora global network + emergency line" is **other Fora advisors who happen to be online** — not a contracted service. No knowledge of the member's profile, no authority to spend, no relational equity (they call Cathay MPC Diamond as themselves, not as the founder), variable competence (Fora is leisure-skewed). Handoff quality is **2/5 at best.** The playbook implicitly acknowledges this — every template names a Latitude 43 person, not a Fora overnight. **The Y1 24/7 promise is fiction, gracefully papered over.**

### D.3 The 15-min Society SLA on overnight calls — biologically impossible solo

This deserves its own emphasis. A 15-minute response SLA, 24/7/365, requires that the responsible human is **awake, sober, near their phone, and in a position to act** every 15-minute window for the entire year. There are 35,040 such windows per year. A single human cannot occupy more than ~70% of them (sleep, dinner, the dentist, a flight, a workout, the rest of life).

Even with the most generous staffing — founder + Berlin advisor + Singapore advisor + PHT VA — overlapping 15-min coverage costs roughly $400-500K of full-time labor. The Society tier at Y5 base case (20 members × $14K avg) generates $280K of subscription. The 15-min SLA, taken literally, is mathematically a loss leader **unless** Society members generate $25-40K of commission/design revenue each (per `/tmp/v2-facts.md`, this is plausible at $26-46K/yr — but only if every Society member is at the upper end of the booking range).

The unit economics on Society can work, but only if the firm is honest that the 15-min SLA is a **business-hours commitment with a "founder-on-call" overnight policy**, not a literal 24/7 promise. Selling it as literal will produce churn the first time a 2am text goes 28 minutes.

---

## E. Technology stack risks

### E.1 Tern vs. Travefy vs. Axus

The plan splits the tooling cleanly: **Tern for CRM** (member relationships, trip tracking), **Travefy for base itineraries** (included with Fora), **Axus for the Firm/Society tier itineraries**. This is the right structural choice — none of the three handles all three jobs well.

| Tool | Scales to | Breaks at |
|---|---|---|
| Tern | ~200 active members per advisor with discipline | Above 200; or when team grows past 3 advisors needing shared visibility — Tern's multi-user model is weak |
| Travefy | Effectively unlimited (itinerary tool, not workflow tool) | Doesn't scale into operations; it ends at PDF delivery |
| Axus | ~500 trips/year per firm | Quality-of-life issues above 500 — sync delays, template bloat |

**The real platform risk is none of the above scaling — it is the integration debt between them.** Tern, Travefy, Axus, Fora's portal, Sabre, the Notion member-portal, Slack channels, WhatsApp Business, SMS — these are eight systems that share no native integration. Every member touch lives in 2-4 of them. The cost of keeping them in sync is paid in founder time (Y1) and operations-manager time (Y3+).

**By Y3 the firm needs either a custom integration layer or a dedicated ops manager.** The plan budgets the ops manager at Y5 ($140K-ish, bundled with the second advisor). Y3 is where it breaks; Y5 is where the plan hires. **24-month gap.**

### E.2 Slack, WhatsApp, SMS — at what count does the founder lose the thread?

The voice guide says text-first, email-for-records, Slack for Firm tier shops. The scenarios book is mostly text-led. The 76% messaging-over-phone buyer preference (from `/tmp/v2-facts.md`) reinforces text.

Asynchronous text threads scale like inboxes: linearly with member count, but cognitive load on the person managing them is **super-linear** because each new thread carries its own context, its own member voice, its own thread of relationships. Industry rule-of-thumb from EA-network research (NYCEA, IAAP — the same networks the plan targets): a single high-context EA can hold ~8-12 active text threads. A founder with member depth and history can stretch to ~20.

**At 20 members the founder loses the conversation thread.** Specifics start drifting: the wrong restaurant gets a follow-up text, the wrong member gets the weather flag, a confirmation goes to the spouse instead of the principal. The voice guide ("names over nouns") becomes harder to maintain when names blur.

Mitigations the plan should add:
- Pre-canned context retrieval from Tern on every inbound (e.g., "Diane texted — last trip was SF, she's on AA Plat Pro, current open thread is SFO trip closing Friday")
- A "thread freshness" SLA — no thread goes >24 hours without a status touch
- Aggressive use of EA-as-buffer for Office tier (the Companion Seat as a load-balancer, not a feature)

### E.3 GDS access (Sabre/Amadeus via Fora) — limitations at scale

Sabre is a 1970s-era system with a modern frontend. Limitations relevant at scale:

- **NDC content gap** — 30% of bookable premium fare inventory is now outside the GDS (acknowledged in the plan, §3 competitor analysis). At scale, this means every international Premium booking requires checking 2-3 channels: Sabre, the airline direct site, and consolidator inventory. Each additional channel adds 4-8 minutes of search time per booking.
- **Multi-user concurrency** in Sabre is permissioned through Fora; once two advisors are on the same member's PNR, Sabre locks one out. Trivial at N=1, painful at N=4.
- **Sabre training** for any new advisor is 80-120 hours. The associate advisor hire (Y4) cannot start producing for 2-3 months.

The plan correctly identifies NDC as the structural reason "the human is the product." Operationally, this same NDC fragmentation **costs the firm 15-20% more labor per international booking** than a pre-NDC equivalent firm. It's a real cost, not just a competitive advantage.

### E.4 Notion-based portal — when does it break?

The member portal mockup is HTML (a static prototype). The actual operating portal per the plan is Notion-based. Notion scales to:

- ~50 members before sync latency and page-load issues become a daily annoyance for the operator
- ~150 members before Notion's permission model (page-level sharing) becomes a security risk — accidental exposure of one member's profile to another is a real failure mode
- ~250 members before Notion stops being viable at all

**The Notion portal is a Y1-Y2 expedient that needs to be replaced by Y3.** The replacement is either: (a) a custom build (~$60-120K), (b) a tenant on a member-portal SaaS (Common Room, Circle, Tribe — none purpose-built for this; ~$2-5K/mo with adaptation), or (c) the Fora portal (which the plan explicitly says is inadequate for the business-travel use case). None of these is in the Y3 budget.

The IROP log lives in the same Notion database. The seven-year retention requirement for Tier 3 IROP files (per the playbook) is a legal compliance question that **Notion is not the right system for**. By the time the first Tier 3 case happens, the firm will wish it had built the IROP log in a system with audit trails.

---

## F. Cash flow / operations interaction

### F.1 Commission lag

Hotel commissions pay 30-90 days after guest checkout. Air commissions pay weekly via ARC. The mix per the plan is 70% hotel / 30% air. Effective DSO on commission revenue: ~60 days.

| Year | Commission revenue (base case) | 60-day receivables float | Working capital strain |
|---|---:|---:|---|
| Y1 | $30K | $5K | Trivial |
| Y2 | $60K | $10K | Minor |
| Y3 | $159K | $26K | Noticeable |
| Y4 | $260K | $43K | Material if labor costs accelerate |
| Y5 | $440K | $73K | Material; corresponds to ~1 month of associate payroll |

The membership subscription (100% retained, Stripe monthly billing) covers the labor float in Y1-Y2. By Y4-Y5, the receivables on commission are large enough that **a quarter-over-quarter dip in commission timing (e.g., post-Q1 LP season, hotels paying slowly) can create a payroll pinch**. The plan should carry 60-90 days of operating cash by Y3.

### F.2 Refund liability under the First 30 (90-day no-fault exit)

The First 30 program allows members a 90-day no-fault exit with monthly Stripe billing. Refund liability at any point in time:

- Max liability per member: 3 months × subscription = $297 (Light), $747 (Office), $3-7.5K (Society)
- Max aggregate liability at Y5 (assuming worst-case all members are 0-90 days in): $63K (60 Light × $297 + 40 Office × $747 + 20 Society × $4.5K avg) = **~$167K**

In practice, the population in the 0-90 day window at any moment is ~20-25% of the book. So **real-world maximum refund liability is ~$33-42K** — manageable, but **all of it would land in Q1** (the cohort that signed Q4-Q1 churning at month 2-3).

**The cash-flow trap:** if Q1 churn hits 30% on the new-sign cohort (plausible — the LP-season busy period creates regret-buy dynamics in finance), the firm could owe $50K of refunds against a Q1 commission base that hasn't yet paid out. **Y3-Y5 needs a refund reserve line on the balance sheet, ~$50-80K.** Not in the plan.

### F.3 Seasonality

The plan acknowledges Q1 LP season and Q4 holidays. The operational implications:

| Quarter | Demand pattern | Operational stress | Cash pattern |
|---|---|---|---|
| Q1 | LP season + roadshow heavy | Highest founder-hour quarter | Subscription strong; commission lag drags |
| Q2 | Steady business travel + conference season | Moderate | Commission catches up from Q1 |
| Q3 | Summer slow + August dead zone | Lowest | Cash dip; subscriptions still bill |
| Q4 | Family + ski + offsite-heavy | Hybrid biz/leisure spike | Strong commission earn; pays in Q1 next year |

The Q3 cash dip plus Q4 founder-burnout-cycle is the predictable annual stress point. The plan does not seasonally adjust for this. **Y3+ probably needs a Q3 hiring or PR push specifically to keep the funnel from going cold while the operating quarter is light.**

---

## G. The hiring plan that's needed but missing

This is the section that should drive the largest single revision to the business plan.

### G.1 What the plan says vs. what the operations require

| Hire | Plan timing | Plan cost | Operations-required timing | Operations-required cost | Gap |
|---|---|---:|---|---:|---|
| PHT VA (overnight admin) | Month 9–12 | $18K/yr | **Month 4–6** | $18–24K/yr | Hire 5 months earlier |
| PHT VA, 7×8 (full overnight cover) | Month 18 | $22K/yr | Month 12–15 | $30–40K/yr | Hire 6 months earlier; cost is 30-50% higher than budgeted |
| Associate advisor, US-based (Sabre-trained, IROP-capable) | Year 4 | $85K/yr | **Month 12–18** | $80–120K/yr | Hire 24+ months earlier |
| Lead/senior advisor (second senior) | Year 5 | (bundled $140K) | Month 30–36 | $130–160K/yr | Hire 24 months earlier |
| Operations manager (profile mgmt, IROP log, billing) | Year 5 | (bundled $140K) | Month 24–30 | $90–120K/yr | Hire 24 months earlier |
| EU/UK overnight advisor (Berlin) | Not in plan | n/a | Month 30–36 (with Society launch) | $100–140K/yr | **Missing entirely** |
| APAC overnight advisor (Singapore) | Not in plan | n/a | Year 4–5 | $80–110K/yr | **Missing entirely** |
| Director of operations | Not in plan | n/a | Month 30 | $150K/yr | Missing; partly overlaps with ops manager |

### G.2 Does the math work?

**The honest answer: it does not work at the v2.0 SLAs as written.** At Y5 (120 members, base case $871K revenue), the operations-required labor cost is $580–760K — roughly 65-87% of total revenue. That leaves nothing for founder compensation, taxes, technology, marketing, or profit.

Three paths reconcile this:

**Path 1: Reduce the SLAs.** Move Atlas to 4-hour SLA outside business hours (still industry-leading). Move Society to 30-min business hours / 60-min overnight. This drops the labor requirement to ~$320-400K and the math works.

**Path 2: Reduce the headcount.** Accept that "named human" is a Y1-Y2 brand, replaced by "the desk" as the firm grows. Use AI-assisted triage to reduce per-incident labor by 30-40%. Get to a $400K labor base by Y5. The brand softens.

**Path 3: Raise the prices.** Atlas Light to $129, Office to $329, Society floor at $24K/yr. This adds ~$240K of subscription revenue at the Y5 base case. Combined with a moderate SLA recut, the math closes.

The plan should pick one explicitly, model it, and own the tradeoff. Today the plan reads as if all three of "named-human SLA," "Y5 hiring plan as written," and "the math works" are simultaneously true. They are not.

---

## H. Quality assurance and brand risk

### H.1 The one bad early experience

The buyer cohort — partners at PE firms, founders, principals at RIAs — is a small, networked, vocal world. Per `/tmp/v2-facts.md`, 42% of consumers have no opinion of travel agents; among the target cohort that percentage is materially lower because the cohort *talks*. One LinkedIn post — "I left Latitude 43" — from a credible buyer is worth more brand damage than 50 sales-deck Journals.

The shape of the post that kills the business:

> *"I was a Latitude 43 member for 8 months. The first 3 trips were great — Avshalom himself handled everything. The next 5 trips were... different. The associate who replaced him on my account didn't know my preferences, missed an upgrade I'd been promised, and worst of all, when my flight cancelled in Frankfurt at 2am I got an auto-text from someone in Manila who didn't know my name. The $99/mo felt like a deal at month 1 and an embarrassment by month 8."*

**The structural risk is the pod transition** (per §B.2). It is also the moment when the brand promise (named human, 24/7) gets stress-tested most directly. The lifecycle doc handles this at the level of process; the operational reality of one founder splitting attention across 50+ relationships is what breaks it.

### H.2 The "LinkedIn-savvy buyer" post

Higher-probability than the founder may want to admit. Mitigations the plan has not codified:

1. **An at-risk-member protocol.** Any member who hasn't booked in 90 days, or whose last quarterly review surfaced friction, gets a personal founder touch — not a templated check-in. This is in the lifecycle doc as the "first 90 days" mechanism but stops after month 3.
2. **A founder-led "service recovery" tier.** When a service failure happens (and it will), the founder personally calls the member within 24 hours, owns it, and offers a tangible recovery (credit, gesture, upgrade). The IROP playbook handles incidents *to* the member; it doesn't handle failures *by* the firm.
3. **A graceful exit protocol** that retains the relationship after departure. The "door we leave open" line is right; the operational execution (a quarterly "still thinking of you" touch for 36 months) is what makes it real and not just rhetoric.

### H.3 Recovery cost

The advisor-industry rule: recovery from a bad-experience post is 10x acquisition cost. The plan models warm-network CAC at near-zero (referrals + Journal). A LinkedIn-post recovery would require **paid acquisition, PR remediation, and a likely founder-led campaign of 1:1 outreach to the cohort that read the post** — call it $25-50K in soft cost per major incident.

The acceptable per-year frequency: 0. The realistic per-year frequency at Y3+: 0.5-1. **Budget $30K/yr from Y3 as brand-defense reserve.**

---

## I. Verdict

### I.1 Can this firm operationally hold its promises at $1M ARR?

At $1M ARR (roughly the Y5 base case + 15%), the firm has ~130 members. **At the SLAs as written, no — not without 3.5x the budgeted headcount.** At a recut SLA (4-hr outside business hours for Atlas; 30-min business hours for Society), **yes, with the recommended earlier hiring trajectory.** The realistic operating model:

- 1 founder, principal/Society lead
- 1 senior advisor (US, Sabre-trained, IROP-capable)
- 1 junior advisor (US or remote)
- 1 ops manager
- 2-3 VAs (PHT + APAC overnight) for triage and admin
- Total labor: ~$450K
- Margin available for founder, taxes, marketing, technology: ~$550K

This is a healthy boutique advisory at $1M ARR. It is not the firm the v2.0 deck describes.

### I.2 Can this firm hold at $5M ARR?

$5M ARR implies ~400 Atlas seats and 30 Society principals (the cap). This requires:

- 2-3 lead advisors (pod model)
- 4-6 associates
- 2 ops managers
- 4-6 VAs across timezones
- Total labor: ~$1.4-1.8M
- Significant technology spend ($150-250K/year on platforms + custom)

Operationally feasible. **The brand promise of "named human" is fully gone by this point** — the firm operates as pods, with members assigned to a lead advisor, escalation paths to senior, founder personally serves only the top 5-8 Society principals. This is a real firm; it is also a different firm than the one being launched in 2026.

### I.3 At $20M ARR?

$20M ARR implies institutional scale: 1,500+ seats, multiple offices or remote pods, a head of operations, a head of advisory, a CTO. The model is feasible (Knightsbridge Circle, Quintessentially operate at this scale) but the founder transitions from "the desk" to "the chairman." The Society cap (30) has to be revisited or supplemented with a sister-tier. The Journal becomes a content team. The voice guide is enforced by an editor.

Operationally, $20M is a 7-10 year build with at least one capital raise to absorb the labor-cost-curve in years 4-6. The plan today is positioned for $1-2M as a sole-proprietor practice. **The bridge to $20M is not modeled and would require a meaningfully different cap structure and team.**

### I.4 Realistic operating model by scale

| Scale | Member count | Headcount | Founder role | What the promise actually means |
|---|---:|---|---|---|
| $250K ARR (Y1-Y2) | 25–40 | 1 founder + 1 PHT VA | Lead advisor for every member | The 24/7 SLA is honor-bound, with quiet exceptions overnight |
| $1M ARR (Y4-Y5) | 100–130 | 1 founder + 2 advisors + 1 ops + 2 VAs | Lead for top tier; oversight for rest | Named human for Society; "the desk" for Atlas |
| $5M ARR (Y7-Y8) | 350–450 | 1 founder + 8-10 advisors + 3 ops + 4-6 VAs | Chairman; selective member work | Pods; the founder is brand, not desk |
| $20M ARR (Y10+) | 1,500+ | Founder + 30-40 staff | CEO | A firm in the Knightsbridge Circle category |

---

## J. Ten specific operational fixes / additions

The recommendations below are ordered by urgency, not by size.

### 1. Re-cut the Atlas SLA before the first member signs.

**Today's promise:** 60-minute first response, 24/7.
**Honest promise:** 60-minute first response during 0700-2200 ET, 7 days; 4-hour first response 2200-0700 ET, automated triage for non-emergencies; "open desk" emergency line for true emergencies, 90-minute response 24/7.

This is still industry-leading. It is also defensible without lying.

### 2. Hire the PHT VA at month 4, not month 9-12.

The Y1 plan has the founder doing 60-80 hour weeks. The VA at month 4 buys back ~12-15 founder hours/week of admin (billing, calendar, profile updates, IROP log maintenance, basic Sabre lookups). The cost is $18-24K — affordable from month 4 subscription revenue if the Y1 close-rate hits even half the plan.

### 3. Defer Society launch to Q3 2027 and cap at 6 members through Y4.

The 15-min SLA is genuinely impossible solo. Six Society members is the maximum a solo founder can hold to a true dedicated-principal standard. The deferred launch buys the time to hire an associate first.

### 4. Hire the first associate advisor at month 14-18, not Year 4.

This is the single largest plan revision. Cost: $85-120K/yr. Funded by: subscription revenue at the Y2 sign-rate ($96K subscription in the base case), which is short of the full cost — but the alternative is founder burnout, which is catastrophic per the plan's own §14 risk register. **The associate is not a "Year 4 luxury." It is a Y2 survival measure.**

### 5. Build the "named successor" promise into the website language, not just the lifecycle doc.

Either: (a) make the named successor real by month 18 (requires the associate hire above), or (b) soften the language to "your lead advisor with deep operational backup," which is honest in Y1. The current ambiguity is a churn risk.

### 6. Move the IROP log out of Notion to an audit-trail system by month 18.

Options: Linear, Jira Service Management, or a custom build on Postgres. Cost: $5-15K to migrate. The seven-year retention requirement for Tier 3 IROP files is a real legal exposure that Notion cannot defensibly meet.

### 7. Add a refund reserve line of $30K to the balance sheet from Y2.

The First 30 program is a brand-building feature with a real Q1 cash flow tail. Carrying the reserve quietly is operationally clean; not carrying it is a Q1 surprise risk.

### 8. Codify the "concurrent IROP" protocol in the playbook.

The current playbook handles serial incidents. Add a section on: who takes priority when two Tier 2s arrive simultaneously, who calls the second member to set expectations, when to invoke the Fora pool, and at what member count the protocol gets revised (suggest: every 20 members).

### 9. Carry an independent $2M E&O policy from Day 1, not Year 2.

The Fora umbrella covers booking activities; it does not cover the advisory layer the firm sells (the membership, the Reports, the Journal advice, the IROP recovery). $1,800-2,400/year is trivial; the first claim without coverage is existential. Pull the Y2 hire forward to Y1.

### 10. Set up the "service recovery" protocol explicitly, before the first failure.

When the firm fails a member (not when the airline fails the member), there is a specific protocol: founder calls within 24 hours, written acknowledgment of what went wrong, tangible recovery (credit, upgrade, gesture), and a written debrief filed in the member's record. This is missing from the lifecycle doc and the IROP playbook. Add a one-page SOP. The first incident that uses it is the one that saves the LinkedIn post from being written.

---

## Closing investor note

The operational discipline visible in this firm — the scenarios book, the IROP playbook, the voice guide, the lifecycle doc — is **materially above average for a pre-revenue advisory practice.** The founder has thought harder about the operating model than most of their direct competitors (Cadence, Embark, Bell & Bly) appear to have.

The risk is not that the operational thinking is weak. The risk is that **the operational thinking has not yet been reconciled with the budget and the SLA promises**. Today the firm is selling a Knightsbridge Circle-grade service standard at an Indagare-grade price point on an Embark-grade headcount budget. Two of those three numbers have to change.

The most consequential decision in the next 90 days is the one made about hiring velocity. The plan's "founder alone through Year 3" model fails on the math of the SLAs as written. The earlier the firm hires the first associate and the first overnight VA, the higher the probability that the brand promise survives contact with the operational reality.

If those hires happen — and if the Atlas and Society SLAs are honestly recut to reflect what a small team can deliver — this becomes a real $1-2M ARR boutique advisory by Y5, with a defensible bridge to $5M by Y7-Y8. If they don't, the firm will hit ~30 members and either break the founder or break the promise. Both outcomes are LinkedIn posts the firm cannot afford.

**One-line verdict for the investment committee:** A high-quality operating thesis with a credible founder, undermined by a hiring trajectory that has not been priced against the SLAs the firm is selling. Investable conditional on (a) earlier associate hire, (b) honest SLA recut, (c) Society cap discipline through Y4. Pass without those three.

---

*End of evaluation.*
