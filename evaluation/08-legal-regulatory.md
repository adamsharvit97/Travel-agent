# 08 — Legal, Regulatory & Cross-Border Risk

**Evaluator stance:** Pre-revenue investor with cross-border specialty. Toronto-based solo founder, hosted under Fora Travel (US-registered), targeting US clients, occasionally serving Canadian-resident referrals. I am looking for the landmines that will cost real money or kill the company in months 6–24.

**Verdict up front:** The legal posture in the v1.0 plan reads competently but is dangerously casual on five issues: (1) the actual operational definition of "US-only" under TICO, (2) whether Fora's seller-of-travel coverage extends to a Canadian advisor invoicing a separate membership product in their own brand, (3) HST treatment of the membership SKU vs. zero-rated commission, (4) the IP/regulatory exposure of the phrase "First Loss Insurance," and (5) the Fora termination/portability risk that sits underneath the entire revenue model. None are fatal. All are foreseeable. Four can be solved for under $10,000 in legal spend before launch.

---

## A. TICO three-path framework — pressure-test

The plan defaults to **Path A (US-only, defer TICO)**. That is the correct Y1 choice on cash terms but the plan understates how narrow the safe operational corridor actually is.

### A.1 What "US-only" actually means under the Ontario Travel Industry Act, 2002

TICO's jurisdiction triggers on **"selling travel services to consumers in Ontario."** The statute and Reg. 26/05 are activity-based, not residency-based in the way US sales tax nexus is. The factors that determine whether a transaction is "in Ontario":

| Factor | TICO will likely treat as Ontario-touching | Plan's exposure |
|---|---|---|
| Consumer is physically present in Ontario at point of sale | Yes — Ontario sale | High if any US client signs up from a hotel in Toronto |
| Consumer is an Ontario tax resident, even if abroad | Yes — Ontario consumer | High if a Canadian friend-of-founder signs up |
| Travel originates in Ontario (Pearson, Billy Bishop) | Yes — Ontario sale | Medium — most US clients won't book YYZ origin |
| Marketing accessible from Ontario via the open internet | Grey — registration not triggered by passive web presence, **but advertising rules apply** | High — see Section G |
| Payment processed via Stripe to a CCPC bank account | Mostly irrelevant for trigger; relevant for evidence | Medium — creates a paper trail |

**Bottom line on Path A operational rules:**

1. **No Canadian-resident sales.** Full stop. The "polite decline" language in §12.1 of the plan is correct but must be a documented intake control, not an aspiration. Recommend: hard-coded Stripe + Tern intake fields — country of residence, tax residency, country of origin for first booking — with a refusal workflow and a logged record of the decline (date, name, source). If Canadian residents end up in the funnel and slip through, TICO's complaint-driven enforcement will eventually find one.

2. **The "US person in Toronto on the day they sign up" case is the most operationally awkward.** A US-resident anchor client who happens to be at the Shangri-La Toronto when they apply is **not** an Ontario consumer for residency purposes — but the point-of-sale is arguably in Ontario. The conservative read is: the residency test dominates if you can document it. Practical fix: collect a US billing address, US tax residency declaration, and proof-of-residency document (driver's license, US W-9 or ITIN-equivalent) at onboarding. If you have that file, you can defend the transaction.

3. **The "referral from Toronto network" mechanic in the GTM plan is the real risk surface.** Soho House Toronto, EO Toronto, the brother-in-law dinners — every one of these produces Ontario-resident leads. The plan says you decline them. In practice, you will be tempted at month nine when your runway is tight and an EO member with a $200K T&E budget asks to join. That is the moment you accidentally become a TICO registrant after the fact. Build a written policy now ("Ontario inquiries are declined and referred"), get the referral-partner relationship in place **before launch** so the decline is graceful, and put it in your CRM as a hard gate.

4. **Brother-in-law / family network exception.** Travel booked for non-paying friends and family under your personal Fora advisor account, with no consideration, is arguably not "selling travel services" and may sit outside TICO scope. But the moment any consideration (even a thank-you commission split, a meal, a referral fee) flows from an Ontario resident, you are in scope. Document the family-only bookings as gifts, not commercial activity.

### A.2 Path B — Get TICO registered

| Item | Realistic figure | Source |
|---|---|---|
| Initial registration fee | $3,000 one-time | TICO fee schedule |
| Annual renewal | ~$200–$2,500 sliding by sales | TICO |
| Working capital test | Positive working capital, audited or notice-to-reader financials | TICO Reg. 26/05 |
| Trust account | Required for client funds in advance of supplier payment | Reg. 26/05 s. 27 |
| Security deposit / bonding | Generally **not** required at the small-registrant tier unless working capital fails, but ~$10K letter-of-credit common for new registrants | TICO discretion |
| Compensation Fund contribution | $0.05 per $1,000 of sales (immaterial) | TICO |
| Education / TICO exam | Founder must pass the TICO Travel Counsellor exam; supervisor must pass Travel Industry Supervisor exam — founder can hold both | TICO |
| Designated supervisor | Must be named, must be on premises, must hold supervisor cert | Reg. 26/05 |
| Legal setup | $5K–$10K with a TICO-experienced lawyer | Market |
| Realistic timeline | **3–5 months** from engagement to certificate | TICO standard |
| **All-in Y1 cost** | **$15K–$25K** | — |

**Is Fora compatible with a TICO-registered Canadian entity?** Almost certainly no, in the simple form. Fora is an IATA/ARC-accredited US host. A TICO registrant must be the merchant of record for Ontario consumer sales, must hold a trust account, must issue receipts under its own TICO number, and must answer to Ontario consumer-protection law. Fora's system is built to be the merchant of record. You cannot easily be both — Fora-hosted for US bookings and TICO-registered for Ontario bookings — without a structurally separate Canadian entity, a separate booking workflow, and a separate set of supplier relationships for the TICO side.

**The realistic Path B architecture, if you ever pursue it:**

- Latitude 43 Inc. (CCPC, Ontario) — TICO-registered, holds Ontario consumer relationships, sells via direct supplier contracts or via a Canadian host (TPI, Travel Edge, Vision Travel)
- Latitude 43 USA LLC or a US d/b/a operating under Fora — holds US consumer relationships
- Cross-licensing of brand IP between the two
- Two sets of E&O, two sets of registrations, two ledgers

That is a Year 3+ structure if and only if the Ontario book grows large enough to justify it (probably $250K+ in Ontario commission). It is not a Year 1 problem.

### A.3 Path C — Partner with a TICO-licensed Canadian agency

Realistic Canadian host partners for Ontario referral overflow:

| Partner | Pros | Cons |
|---|---|---|
| **Travel Edge** (Internova) | Best brand fit, Virtuoso | Same parent as Brownell/ALTOUR — your competition |
| **Vision Travel** (Direct Travel) | Strong corporate infra | Brand mismatch |
| **TPI** | Easy onboarding, established | Generalist brand |
| **Nexion Canada** (CWT/AmEx) | Good systems | AmEx affiliation awkward given competitive positioning |
| **The Travel Agent Next Door** | Easy onboarding | Mass-market drag |
| **Boutique TICO holder** | Cleanest control | Hardest to find and vet |

**Fair split:** 25% of net commission if they book and own the client; 10–15% finder's fee if you do the work and they provide the umbrella; 20–30% for full white-label (their TICO number, your brand on the receipt).

**Liability cross-overs:** TICO holder owns consumer-protection obligation for bookings they process; you retain reputational and membership-contract liability. The whipsaw risk: client sues you for service failure, your defense ("we didn't book it") is undermined by your membership contract. Resolve via explicit pass-through language, a written referral agreement with mutual indemnity, and a single point-of-contact protocol.

### A.4 Recommendation on framework

Stay on Path A through Y2. Pre-stage Path C by signing a referral MOU with one TICO partner in Q1 2026 so that "we politely decline" becomes "we politely refer." Plan Path B as a Y3+ decision conditional on Ontario book exceeding $250K commission or $1M GBV. Do not pretend Path B is a Y1 option; the cash, time, and structural conflict with Fora make it implausible.

---

## B. Cross-border tax structure

The plan's tax section (§12.3) is directionally right and mechanically incomplete.

### B.1 What's defensible in the current plan

- CCPC + small business deduction: combined federal-Ontario rate of ~12.2% on the first $500K active business income is **correct** for 2026 if active business income (ABI) qualifies.
- GST/HST zero-rating on export of services: **correct** under the Excise Tax Act s. 7 of Part V Schedule VI, **conditional on** the recipient being a non-resident, not being in Canada at the time the service is performed, and not consuming the service primarily in Canada.
- ITIN for W-9: correct posture; some corporate clients will require it.
- No US permanent establishment expected: correct under the Canada-US Tax Treaty Article V if the founder is not physically present in the US for substantial periods and has no US office.

### B.2 What the plan misses or papers over

**Membership fees vs. commission income — different tax characterizations.**

| Revenue stream | Canadian tax treatment | HST treatment | US source? |
|---|---|---|---|
| Membership subscription billed to US-resident individual | ABI of CCPC; small business deduction available; ~12.2% combined to $500K | **Zero-rated** as export of service if recipient is non-resident, not in Canada when service is delivered, and service is not consumed in Canada | No, generally; service performed in Canada by Canadian entity |
| Membership subscription billed to US company (Atlas Office/Firm) | ABI; small business deduction available | **Zero-rated** — non-resident corporate recipient | No US source if no PE |
| Commission from Fora (US merchant of record) on US travel | ABI; small business deduction available | **Zero-rated** — Fora is non-resident; service consumed outside Canada | No |
| Design fees (trip-planning fees) | ABI | **Zero-rated** if US client; **taxable HST at 13%** if Canadian client | No |
| Per-trip receipts (Latitude Reports successor) | ABI | Same as design fees | No |

**The GST/HST trap that the plan misses:** If you accept **any** Canadian-resident client, even one, on any product (including a friend-of-founder for a single trip), your zero-rating analysis becomes case-by-case rather than blanket. Once a single domestic supply happens, you have to track HST on every invoice and remit. The clean answer: do not accept any Canadian-resident paid client in Y1. Period.

**Worldwide income on the Canadian return:**
- The CCPC reports worldwide income; T2 schedules 21, 91, 97 may apply depending on foreign affiliate / partnership structure.
- T1135 Foreign Income Verification Statement is required for the founder personally if specified foreign property (US bank accounts, US brokerage, US LLC interests over CAD$100K cost base) is held. The Fora relationship does not by itself trigger T1135. A USD bank account at TD does not trigger T1135 (Canadian bank). A USD bank account at an actual US bank would.
- If commission flows from Fora to the CCPC, no T1135 from that source. If Fora pays the founder personally, T1135 may apply.

**US tax surfaces the plan understates:**

1. **Form W-8BEN-E, not W-9**, filed with Fora. A CCPC is a foreign entity. W-8BEN-E with treaty position under Article VII (business profits) zeroes US withholding on commission. W-9 signals US tax residency and risks 30% withholding plus IRS filings. Correct the plan.
2. **Form 1042-S** is what Fora issues to the CCPC. Form 1120-F required only with US trade-or-business and effectively connected income. Solo Canadian advisor with no US presence: no 1120-F. Atlas Firm embedded engagements flip the math.
3. **State seller-of-travel registrations** — see Section D.
4. **State sales tax on the membership product** — WA, HI, NM have broad service-sales-tax regimes. Hawaii GET at 4.5% can apply to non-resident providers with sufficient nexus. One HI client unlikely; ten worth a memo.

### B.3 Permanent establishment risk if founder visits US client offices

This is the single most underappreciated tax risk in the plan. Under Canada-US Tax Treaty Article V:

- A PE arises if the founder has "a fixed place of business" in the US through which business is conducted.
- A PE also arises under the **services PE rule** (Article V(9)) if the founder is physically present in the US providing services for **more than 183 days** in any 12-month period, **or** if more than 50% of the gross active business revenue is derived from US services performed during periods totaling 183+ days.

The "more than 50% of gross active business revenue from US services" test is the dangerous one for Latitude 43. 100% of revenue is US-sourced. The 183-day test is the saving grace.

**Practical guidance:**
- Track US travel days obsessively from Day 1. Use a calendar app, dump it monthly, retain for seven years.
- Cap founder US days at **120 per calendar year, 150 per 12-month rolling window.** This gives a 33-day safety buffer.
- Atlas Firm "embedded" service models (founder spends 2 days/week in NYC client office) are the exposure point. If a single client wants this, structure it as multiple short visits, hard cap at 120 days, and get a memo from cross-border tax counsel **before** signing.
- A PE finding would create US federal income tax on US-attributable profit, state tax in the state(s) of physical presence, payroll tax obligations if you hire anyone US-side, and a 1120-F filing burden.

### B.4 Founder personal tax

Salary/dividend mix solved in conjunction with RRSP room, CPP, marginal rate; bias dividend early to preserve SBD; HSA inside CCPC for family medical; cross-border CPA from Month 1 (~$4–6K Y1, $3–5K thereafter).

---

## C. Fora contractual relationship

The plan treats Fora as background infrastructure. From an investor's view, Fora is **the single largest concentration risk in the company.** If Fora terms change, the business model changes. If Fora is acquired (likely within 36 months — they've raised at unicorn-adjacent valuations and need an exit), terms will change.

### C.1 What Fora's IC agreement actually says (typical Fora advisor agreement, 2025 vintage)

I have not read your specific signed copy. Based on the publicly available terms and what other Fora advisors have shared:

| Clause | Typical Fora position | Latitude 43 exposure |
|---|---|---|
| Independent contractor status | Affirmed; advisor is not an employee | Low |
| Brand use — Fora marks | Advisor may identify as a "Fora Advisor" with restrictions; cannot misrepresent | Medium — see below |
| Advisor's own brand/d/b/a | **Permitted** in current Fora terms (this is a Fora differentiator vs. legacy hosts); advisor may operate under a personal brand and route bookings through Fora | Medium |
| Exclusivity | **Non-exclusive** — advisor may have other business activity, but bookings must go through Fora when using Fora's accreditation | Medium |
| Commission split | Tiered, as documented (70/30 → 80/20 at $300K → 90/10 at $2M) | High concentration risk |
| Client ownership | **Disputed area.** Fora generally claims a relationship with the client (newsletter list, app); advisor claims the booking relationship. Termination clauses often allow Fora to retain client data | **High — see C.5** |
| Termination | Generally 30–60 days either side; Fora retains booking records | Medium |
| Change of terms | Fora can modify split tiers and policies on notice (typically 30 days) | High |
| Non-compete post-termination | Usually limited; Fora generally does not enforce non-competes | Low |
| Assignment | Fora may assign in M&A; advisor may not assign without consent | High in M&A scenario |

### C.2 Can the founder operate under a separate brand (Latitude 43) without Fora's permission?

Yes, in the current Fora model — this is exactly what Fora markets ("build your own brand"). But three constraints:

1. The booking transaction must clearly show Fora as the merchant of record (legal requirement under ARC/IATA and state SOT laws).
2. Advisor cannot represent Latitude 43 as IATA-accredited or as a travel agency in its own right; the accreditation belongs to Fora.
3. Fora's marketing terms may require attribution ("In partnership with Fora" or similar). This conflicts with the brand's positioning and should be checked **before launch**. The Latitude 43 website should plan for a Fora attribution footer.

### C.3 What if Fora changes terms

Plausible Fora term changes in the next 36 months:

| Change | Probability | Impact on Latitude 43 |
|---|---|---|
| Split structure tightening (e.g., 60/40 default, higher tier thresholds) | Medium-High — common in host-agency consolidation | Direct hit to commission line; ~10–20% revenue impact at Y3+ |
| Membership fee revenue share | Medium — Fora may eventually argue membership rides on their platform | Existential to the 100%-retained-subscription model. Negotiate now. |
| Required use of Fora tooling (Tern displacement) | Medium | Operational disruption |
| Exclusivity on supplier relationships | Low-Medium | Locks out Virtuoso optionality |
| Pricing-floor or pricing-ceiling rules on advisor membership products | Low | Existential to pricing model |

**Mitigation:** Read the agreement now with travel-industry counsel. Document the split-tier and membership-fee positions in writing with Fora **before** Latitude 43 starts billing. A side letter is cheap insurance.

### C.4 What if Fora is acquired or shuts down

Fora has raised significant capital (Series B+ from Heartcore, Forerunner, Insight). Three likely exits:

1. **Strategic acquisition by a legacy host** (Internova, Virtuoso parent, Travel Leaders). Likely re-papering of advisor agreements. Likely tighter commission splits.
2. **Acquisition by an OTA / hospitality platform** (Airbnb, Booking). Existential model change.
3. **Wind-down** (low probability but real for a growth-stage company). 30–60 day notice; commission tail paid out or not.

**Portability plan:**
- Maintain a clean, exportable client database **outside Fora's system** (Tern is your primary CRM — keep it that way).
- Document every supplier relationship by direct contact, not Fora-portal-only.
- Maintain Virtuoso member relationships via the host but understand that Virtuoso membership rides on the host. A Fora exit may sever Virtuoso unless the receiving host also holds Virtuoso.
- Pre-identify two backup hosts: **Gifted Travel Network** (luxury-leaning, smaller, founder-led — closest cultural fit), **Cadence** (despite competitive overlap, structurally similar), **Brownell** (legacy, harder cultural fit).
- 90-day migration plan written and shelved.

### C.5 Client ownership in termination

This is the contract clause to read three times. In a Fora termination, the typical pattern is:
- Advisor retains the right to contact clients they brought in.
- Fora retains a copy of the booking history and may continue to market to those clients via the Fora consumer app.
- The advisor must re-paper supplier relationships at the new host.

**The membership-relationship is yours**, assuming the membership contract is between Latitude 43 Inc. and the client (not between Fora and the client). **Make sure the contract is structured this way from Day 1.** If Stripe billing is on a Fora-controlled account, you have a problem. If billing is on Latitude 43 Inc.'s Stripe account, you are fine.

---

## D. State seller-of-travel laws

Five states have active seller-of-travel statutes that affect Latitude 43. The plan's §12.2 lists them and says Fora covers them. That's directionally true but worth pressure-testing.

| State | Trigger | Bond/Trust | Annual fee | Fora coverage? | Latitude 43 separate need? |
|---|---|---|---|---|---|
| **California** (CST) | Selling travel to CA residents OR from a CA location | $1M bond or trust account, or CA Travel Consumer Restitution Fund participation | $100 + restitution fund | **Yes, via Fora's CST registration** — Fora will likely require disclosure of its CST number on all CA-resident-facing materials | **Likely no**, IF Fora confirms in writing that the membership product is covered. Get written confirmation. |
| **Florida** | Selling travel to FL residents OR from FL | $50K bond (waivable with 3 years' clean operation and AOR with ARC/IATA host) | $300 | **Yes, via Fora** | **No**, with written confirmation |
| **Washington** | Selling travel to WA residents | $10K trust account; surety bond option | $222 | **Yes, via Fora** | **No**, with written confirmation |
| **Hawaii** | Selling travel to HI residents OR from HI | Client trust account | $130 | **Yes, via Fora** | **No**, with written confirmation |
| **Iowa** | Selling travel to IA residents | $10K bond or trust | $400 | **Yes, via Fora** | **No**, with written confirmation |

**The non-obvious problem: the membership product.**

Seller-of-travel statutes were written for booking transactions. A $99/month membership that delivers no specific travel service is a grey area:

- **California's read:** broad. CST defines "seller of travel" as anyone who arranges for compensation a vacation certificate, travel package, or transportation. A membership that includes "design fees waived on members' trips" and "24/7 desk for travel arrangement" is reasonably arguable as a seller-of-travel activity. CA AG enforcement is active.
- **Florida:** narrower; a pure membership without trip-specific obligation may not trigger.
- **Washington:** similar to FL.

**The Fora coverage question:** Fora's registrations cover bookings made through Fora's merchant of record. A membership fee billed to a Latitude 43 Stripe account, on a Latitude 43 contract, with no immediate travel deliverable, **may not be within scope of Fora's SOT registrations.**

**Action:** Get a written legal opinion (one memo, $3–5K from a CA-licensed travel-industry firm — Krooth & Altman, Baker Hostetler travel practice, or a specialist like Maggio + Kattar) on whether the Latitude 43 membership product is a "sale of travel" in CA. If yes, register Latitude 43 separately in CA. If no, paper the file and move on.

Without that memo, you are running on assumption. CA enforcement is via consumer complaint and AG investigation; one complaint from a disgruntled Atlas Light member in San Francisco who reads the SOT statute creates a six-figure problem.

---

## E. Privacy and data

This is where founder optimism meets regulatory reality.

### E.1 Regimes that apply

| Regime | Triggered by | Posture for Latitude 43 |
|---|---|---|
| **PIPEDA** (Canada) | Any commercial activity in Canada — applies because the CCPC is in Canada | Full applicability; the simplest framework, lowest bar |
| **Law 25** (Quebec) | Personal info of Quebec residents | Applies only if Quebec residents are clients (you said no Canadian residents — so no) |
| **GDPR** (EU) | Offering goods/services to EU residents, or monitoring EU residents | Triggered if a single Italian-resident client signs up. Probable within 24 months. |
| **UK GDPR** | UK residents | Same |
| **CCPA / CPRA** (California) | $25M gross revenue OR 100K+ CA consumers OR 50% of revenue from selling CA personal info | **Not triggered Y1** by revenue threshold; **likely not** triggered by consumer count at 60–100 members; **monitor at Y3+** |
| **Other state privacy laws** (CO, CT, VA, UT, OR, TX) | Various revenue/consumer thresholds, generally higher than CCPA | Not triggered Y1; monitor |
| **HIPAA** | Covered entity / business associate status | **Not triggered** — Latitude 43 is not a covered entity. **But:** voluntary collection of dietary, allergy, medical-condition data creates non-HIPAA but real privacy obligations under PIPEDA / GDPR / CCPA |
| **PCI DSS** | Card data | Handled by Stripe; do not store PAN/CVV; SAQ-A applies (lowest tier) |

### E.2 The data you collect that creates real exposure

From §17 of the plan (the intake form):

- Passport number and expiry — **sensitive personal information under PIPEDA**; require encryption at rest, access logging, retention policy
- Known traveler numbers (TSA Pre, Global Entry, Nexus, CLEAR) — government identifiers, same treatment as passport
- Credit cards on file — **do not store directly**; use Stripe's vault and reference by token only
- Loyalty numbers — lower sensitivity but commercially valuable; same protection
- Dietary, allergy, medical info — sensitive; explicit opt-in consent required under PIPEDA Schedule 1 Principle 4.3 and GDPR Art. 9
- Travel companion data (spouses, children) — third-party data; consent of the data subject required if practical

**Practical fixes:**

1. **DPA in the membership agreement** — explicit, plain-English data processing terms.
2. **Tern CRM data architecture** — confirm Tern is SOC 2 Type II; confirm data residency (likely US-based). PIPEDA permits cross-border transfer with notice; GDPR requires SCCs and a transfer impact assessment if EU subjects.
3. **Encrypted document storage** for passport scans — not email, not Slack. Notion is not acceptable for passport storage; use Onedrive/Sharepoint with BitLocker, or a purpose-built tool (TripSuite, Travefy's secure vault, or a dedicated encrypted folder service).
4. **Retention policy:** purge passport copies on expiry + 1 year. Purge dietary/medical on member off-boarding.
5. **Breach notification** — PIPEDA requires notification to the OPC and affected individuals for breaches of security safeguards that pose "real risk of significant harm." Have an incident-response runbook from launch.
6. **Privacy policy on the website** — written specifically for cross-border, not a generic template. Budget $2K with a privacy lawyer.
7. **DPIA (Data Protection Impact Assessment)** — formal under GDPR if EU subjects; informal under PIPEDA. Do it once at launch, refresh annually.

### E.3 Cross-border data flow — Toronto to US

- PIPEDA permits transfer to US processors with notice and equivalent protection (contractual).
- US Cloud Act exposure exists for any data stored on US-resident servers. Inform members.
- Schrems II-style concerns for any EU data routed through US — mitigated by SCCs in Tern's DPA and any sub-processor's DPA.

**Risk level:** Low if you adopt the above practices. Medium-High if you cowboy it.

---

## F. Insurance and liability

The plan's §11.5 is one paragraph. It's the right outline; here is the full picture.

### F.1 Coverage map

| Policy | Carrier path | Covers | Y1 cost | Necessary? |
|---|---|---|---|---|
| **E&O (Fora umbrella)** | Through Fora | Bookings made via Fora system; advisor errors in routing, ticketing, etc. | Included | Yes (in place) |
| **Independent E&O — $2M** | Berkshire Hathaway, Hiscox, RPS Berkley, or travel-specialist (Berkshire Travel) | Advisory work outside Fora (custom reporting, advisory calls, membership product disputes), gap coverage | $1,800–2,400 | **Yes from Y1, not Y2** — the plan's defer to Y2 is too aggressive given the membership product sits outside Fora |
| **General liability — $2M** | Generic broker (Zensurance, ALIGNED, Westland) | Bodily injury / property damage at in-person events (Year-in-Reviews, dinners) | $600–1,000 | **Yes from when first in-person event occurs** |
| **Cyber liability — $1M** | Coalition, At-Bay, Beazley, Chubb | Data breach response, ransomware, business interruption from cyber | $1,200–1,800 | **Yes from launch** — you handle passport data |
| **Director & Officer (D&O)** | Chubb, AIG, Travelers | Director liability — relevant if you raise outside capital | $1,500–3,000 | **Defer** until first outside investor |
| **Commercial property** | Generic | Office contents, equipment | $400–600 | Optional — depends on home office vs. coworking |
| **Personal umbrella** | Personal lines | Personal liability protection | $400–800 | Recommended |

**Total recommended Y1 insurance spend: $4,000–5,800.** Plan understates by ~$2K.

### F.2 Corporate veil

CCPC limited liability holds only with corporate formalities (minute book, resolutions), no commingling (top veil-piercing factor), adequate capitalization, and no unnecessary personal guarantees. Expect to personally guarantee corporate credit cards, any commercial lease, occasionally Stripe, and possibly Fora. Keep separate bank account, credit card, and email infrastructure.

### F.3 Two liability scenarios to model

1. **Villa walk** — member's family arrives at a double-booked villa. $20–50K exposure. Fora E&O likely responds for the booking; independent E&O covers the advisory-promise framing. Both policies matter.
2. **Cyber breach** — passport scans exfiltrated from email. PIPEDA notification, 60 members, possible class threat. $50–200K in response cost alone. Cyber policy non-negotiable.

---

## G. Marketing and advertising restrictions

### G.1 TICO advertising rules

Ontario Reg. 26/05 ss. 30–39 govern travel advertising. Section 30 prohibits providing (including advertising) travel services without registration; section 32 sets disclosure requirements. Passive websites accessible from Ontario are generally not "ads to Ontario consumers," but North American sites including Ontario sit in a grey zone.

**Skift / press article problem:** a Toronto resident reads a profile, visits the site, inquires. Technically arguable as Ontario marketing; practically, TICO does not pursue passive-website cases without evidence of active Ontario targeting.

**Defensive posture:** footer notice ("We are a U.S.-market travel office. Not registered with TICO. Do not sell to Ontario residents"); inquiry form requires country of residence with automated decline-and-refer for Ontario; no Ontario geo-targeted ads anywhere; treat US trade press (Skift, Travel Weekly) as US marketing despite Ontario accessibility.

### G.2 FTC and US marketing rules

| Rule | Source | Posture |
|---|---|---|
| **Endorsement disclosure (FTC 16 CFR Part 255)** | Updated 2023 | Material connections disclosed; all paid testimonials labeled; member referral bonus disclosed |
| **Testimonials** | FTC | Genuine testimonials only; results not atypical of typical experience |
| **CAN-SPAM** | 15 USC §7701 | Unsubscribe, physical address, no misleading subject lines — all email marketing must comply |
| **TCPA** | 47 USC §227 | SMS to US numbers requires prior express written consent; this is critical because the plan leans on SMS |
| **State little-FTCs** (CA, NY) | Various | Same posture as FTC; CA has CCPA-adjacent ad rules |

**The TCPA issue is material.** Latitude 43 leans on SMS as a service channel. Inbound, member-initiated SMS is fine. Outbound marketing SMS to non-members requires prior express written consent. Outbound service SMS to members is fine if covered by the membership agreement's consent language. **Build SMS consent into the membership agreement explicitly.**

### G.3 LinkedIn ad targeting

LinkedIn permits geographic exclusion. Practical settings:

- Include: United States.
- Exclude: Canada (all provinces). Exclude EU (until you have a GDPR posture).
- Targeting: founder/owner/principal titles, $5M+ revenue companies, specific industries (financial services, tech, professional services).

### G.4 Founder personal LinkedIn

This is the gray zone. A Toronto-based founder posting personal LinkedIn content about travel reaches a global audience including Ontario. If the content is opinion/journalism (e.g., the Latitude Journal), TICO has no jurisdiction. If it includes an inquiry CTA, it becomes ad-adjacent. Solution: in personal posts, do not include direct "apply" CTAs; route via the website which has the Ontario decline notice.

---

## H. Member contract terms

### H.1 Drafting principles

The membership agreement is the single most important contract in the business. Must be drafted by a lawyer with travel-industry experience. Budget $4–8K for a thorough draft.

### H.2 Cross-border enforceability — key clauses

| Clause | Recommendation | Why |
|---|---|---|
| **Governing law** | New York or Delaware law for the membership; alternatively Ontario | NY law is well-understood, courts are sophisticated, US clients are comfortable; Delaware is a fine alternative. Ontario adds friction for US clients. |
| **Forum/venue** | New York County or Wilmington; or, AAA arbitration in NY | Convenient for US clients; avoids Ontario forum questions |
| **Dispute resolution** | **Mandatory arbitration with AAA Consumer Rules; small-claims carve-out** | Avoids class actions; faster, lower cost; aligns with US consumer norms |
| **Class action waiver** | Yes, with severability | Standard US consumer contract |
| **Limitation of liability** | Cap at 12 months of fees paid; exclude consequential damages | Standard; survives most jurisdictions |
| **Indemnification** | Mutual, narrow | Avoid one-sided indemnity that won't survive in court |
| **The 90-day no-fault refund** | Plain English; pro-rated refund of unused subscription; commission booked is not refunded | Aligns with "First 30" / 90-day program; the language of "no questions asked" should mean what it says |
| **Auto-renewal** | Required disclosures under California Automatic Renewal Law (Bus & Prof Code §17600 et seq.) and similar state laws — clear cancellation method, advance notice, "click to cancel" | **Critical** — CA, NY, OR all have ARL statutes with private rights of action |
| **Modification** | Latitude 43 may modify on 30-day notice; member may terminate without penalty if material change | Fair; defensible |
| **Communication consent** | Email, SMS, phone — all opted-in via the agreement | Solves TCPA |
| **Travel-related disclaimers** | Latitude 43 is an advisor, not a travel insurance company, not a guarantor of supplier performance, not responsible for force majeure | Standard travel-industry language |
| **"First Loss Insurance" clause** | See Section I — must be carefully drafted | Disambiguate from regulated insurance |
| **Data processing** | DPA incorporated by reference | Privacy regimes |
| **Severability, integration, no third-party beneficiaries** | Standard | Standard |

### H.3 Chargeback risk

The 90-day no-fault refund is a chargeback-mitigation tool. If a member can get a refund without friction in the first 90 days, they have no reason to chargeback through their card issuer. Beyond 90 days, chargeback exposure on monthly subscriptions is real but limited:

- Stripe's chargeback rate threshold is 0.9% (warning) and 1.0% (penalty program).
- At 60 members billing monthly = 720 transactions/year, the threshold is 7 disputes/year before warning territory.
- Realistic exposure: 1–2 chargebacks/year, well within tolerance.

**Membership-fee chargebacks** are easier to defend than booking chargebacks (clear contract, documented service). **Booking chargebacks** flow through Fora as merchant of record and are Fora's first-line problem.

### H.4 The Atlas Family Office NDA

The plan mentions "pre-signed NDA" at Society and Family Office tiers. The NDA is one-directional (member's information confidential to Latitude 43) plus a tightly-drafted mutual carve-out. The Family Office "opt-out marketing clause" needs to be drafted as a separate, signed addendum, not buried in the membership agreement.

---

## I. Intellectual property

### I.1 Trademark — "Latitude 43"

| Jurisdiction | Status (estimated) | Action |
|---|---|---|
| Canada (CIPO) | Likely available; common phrase but not in travel category | File ITU application in Class 39 (travel arrangement) and Class 41 (publishing — for Latitude Journal). $336 CAD base + $108/class. Budget $1,500 with counsel. |
| United States (USPTO) | Likely available; verify with full search | File 1(b) ITU application in same classes. $350/class. Budget $2,500 with counsel. |
| EU (EUIPO) | Defer | Not needed until EU clients |
| UK (UKIPO) | Defer | Same |

**Risk if you don't file:** Someone else does. "Latitude 43" is geographically descriptive (43°N runs through Toronto, Boston, Marseilles), which actually weakens the mark — geographic descriptors are harder to register and harder to enforce. Counsel may recommend adding a stylized logo or a distinctive secondary phrase ("Latitude 43 Travel Office," "Latitude 43 Atlas") to strengthen the application.

**Search before file:** USPTO TESS and CIPO database search at minimum. Common-law search (Google, Travel Weekly archives) for unregistered users in the travel industry. Reasonably likely to find no blockers, but verify.

### I.2 Brand assets — Cormorant Garamond, Inter, navy/ivory palette

- **Cormorant Garamond** — SIL Open Font License, free for commercial use. No risk.
- **Inter** — SIL OFL, free for commercial use. No risk.
- **Color palette** — colors are not protectable except in very narrow trade-dress contexts.
- **Logo design** — if commissioned, ensure work-for-hire or assignment of copyright in the contract. If founder-designed, no issue.
- **Photography on website** — every image must be licensed (Unsplash with commercial license terms verified, Getty/Adobe Stock with extended commercial license, original photography with model and property releases). Stock photography of identifiable people requires model release; common gap. Stock photography of identifiable private property (a specific hotel exterior) may require property release.

### I.3 "First Loss Insurance" — the biggest IP/regulatory risk in the plan

Operationally clever, regulatorily dangerous. "Insurance" is regulated under the Ontario Insurance Act and every US state. Using it in a product name when the product is not an insurance contract risks: (1) UDAP/consumer protection enforcement for misleading naming, (2) insurance regulator inquiry (FSRA, state DOIs), (3) weaker trademark, (4) courts construing the "insurance" promise broadly against the drafter.

**Mitigation: rename.** Candidates: "First Trip Guarantee," "First Loss Credit," "First Trip Promise," "Founder's Guarantee — First Trip." Structure unchanged: service-level guarantee with $1K labor cap, named trip only, specific failure events, service credit not cash, disclaimer that it is not insurance and does not replace travel insurance. The v2 voice work already bans "luxury, bespoke, curated" — drop "insurance" too.

### I.4 "Latitude Atlas," "Latitude Desk," "Latitude Journal," "Latitude Society"

If "Latitude 43" is registered as the house mark, these are likely defensible as sub-brand extensions without separate registration. Defer separate filings.

---

## J. Verdict and 10 specific legal/regulatory actions before launch

### J.1 Verdict

**Pre-launch legal risk: Moderate-Manageable.** No fatal flaw. Five issues are foreseeable, fixable with $15–25K of legal spend in the first 90 days, and four are time-critical (must be done before any member is billed):

1. The Fora contractual relationship is the single largest concentration risk; it is fixable with a side letter and a portability plan but cannot be ignored.
2. The "First Loss Insurance" naming is a regulatory landmine that costs nothing to defuse but everything to ignore.
3. The CA seller-of-travel coverage of the membership product needs a legal opinion before billing CA residents.
4. The TICO operational discipline must be documented as policy, not assumed.
5. Cyber/E&O insurance gap from Day 1, not Y2.

The plan is competently aware of these issues. The execution gap is between awareness and operational discipline.

### J.2 The 10 actions, prioritized and budgeted

| # | Action | When | Cost | Why |
|---|---|---|---|---|
| 1 | **Engage cross-border travel-industry counsel for a one-time pre-launch memo** covering: TICO scope confirmation, CA SOT coverage of the membership product, Fora IC contract review, "First Loss Insurance" renaming, membership agreement draft | Pre-launch, Weeks 1–6 | $12–18K all-in | Single biggest risk-reduction lever; all five Y1 fatalities sit in this memo |
| 2 | **Re-paper the membership product agreement** — NY governing law, AAA arbitration, ARL-compliant auto-renewal, data processing addendum, TCPA SMS consent, refund mechanics, "guarantee" not "insurance" | Pre-launch, Week 4–8 | Included in #1 | Member contracts are the document a plaintiff's lawyer reads first |
| 3 | **Get written confirmation from Fora that:** (a) Latitude 43 may operate under its own brand, (b) state SOT registrations cover Latitude 43 membership product, (c) Latitude 43 owns the membership-client relationship and Stripe account, (d) commission split tiers and membership fee retention are committed | Pre-launch, Week 1–3 | $0 (negotiation only) | If Fora says no to any of these, your plan needs to change before launch |
| 4 | **Incorporate Latitude 43 Inc. (Ontario CCPC)**, open Stripe under Latitude 43, open USD bank account (TD or RBC US$ commercial), engage cross-border CPA, register for HST voluntarily, register for BN, file W-8BEN-E with Fora | Pre-launch, Weeks 1–2 | $2–3K | Foundation; the plan has this but should add W-8BEN-E correction |
| 5 | **Build the intake control architecture:** Tern field for country of residence, Stripe customer field for country of residence, hard refusal workflow for Ontario residents, audit log of declines, written referral relationship with a TICO-licensed Canadian partner | Pre-launch, Week 3–6 | $1–2K | Defends the TICO posture; provides a graceful "no" for Ontario referrals |
| 6 | **Insurance package live from Day 1:** Independent E&O $2M, cyber liability $1M, general liability $2M, personal umbrella. Plan understates by $2K and defers wrongly to Y2 | Pre-launch, Week 4–8 | $4–5.5K Y1 | Membership product sits outside Fora E&O; cyber cannot be deferred given passport data |
| 7 | **File trademark applications** for "Latitude 43" in CIPO Class 39+41 and USPTO Class 39+41; conduct full clearance search; reserve domains and handles | Pre-launch, Week 2–6 | $4–5K | One-time IP foundation; cheap insurance |
| 8 | **Privacy stack:** PIPEDA-compliant privacy policy on website, encrypted document storage for passports (not email/Slack), Tern DPA on file, incident response runbook, retention policy, member consent language for sensitive data (dietary, medical) | Pre-launch, Week 4–8 | $2–3K | Required by PIPEDA; reduces breach exposure |
| 9 | **PE tracking and US-day cap policy:** calendar log of US days, $120-day annual cap, $150-day rolling cap, written approval workflow for any planned Atlas Firm on-site engagement; cross-border tax memo on file | Pre-launch, ongoing | $1–2K (memo + tool) | Avoids the single largest tax-restructuring trigger |
| 10 | **Fora portability plan written and shelved:** clean Tern export procedure, supplier relationship contact list independent of Fora, pre-identified backup hosts (Gifted Travel Network, Cadence, Brownell), 90-day migration runbook | Pre-launch, Week 6–10 | $0 (founder time) | If Fora terms shift or M&A happens, you execute the runbook rather than scramble |

**Total pre-launch legal/regulatory cost: $26–38K.** This is real money against an $80K Y1 revenue plan. It is also non-negotiable for any pre-revenue investor — the alternative is a six-figure surprise in Y2 or Y3 that wipes out two quarters of runway.

### J.3 Things to monitor quarterly post-launch

- Fora IC agreement changes (read every revision, push back via the advisor community)
- CA SOT enforcement actions against host-agency advisors (Travel Weekly, ASTA briefings)
- CCPA / state privacy law applicability as revenue and headcount grow
- Ontario inquiry decline log — if Ontario demand is consistently strong, Path B becomes a real decision rather than a theoretical one
- US-day count for the founder (PE tracking)
- Any move into EU consumer space (triggers GDPR readiness work)

### J.4 The investor's bottom line

The legal posture is not a deal-breaker. It is a deal-shaper. A pre-revenue investor wants to see, in the data room:

1. A signed cross-border counsel engagement letter
2. The Fora side letter (or written email trail) confirming the four items in Action #3
3. The legal memo on CA SOT coverage of the membership product
4. The fully-papered membership agreement, not a template
5. The "First Loss Insurance" renamed to "First Trip Guarantee" or equivalent
6. An insurance binder showing E&O, cyber, GL, umbrella in force
7. Trademark filings in flight
8. A privacy policy on the website that is not a Termly template
9. A US-day-tracking calendar
10. A Fora portability runbook

Show that, and the legal section of the diligence is closed in one conversation. Skip it, and the investor will spend $5–10K of their own legal budget asking the same questions, and you will look like the founder who hadn't thought about it. Pre-revenue companies die from looking like that.

---

**End of evaluation.**
