# ALTOUR Forensic Analysis: A Strategic Brief for Latitude 43

**Prepared for:** CEO, Latitude 43
**Date:** May 2026
**Subject:** Deep competitive analysis of ALTOUR, its parent Internova, and structural gaps Latitude 43 can exploit

---

## 1. Corporate Structure, Ownership, and Financial Scale

### 1.1 Lineage

ALTOUR was founded in **1991** in New York by **Alexandre Chemla**, a French-born entrepreneur who built it into one of the largest privately held TMCs in North America. It operated independently until **July 27, 2017**, when Travel Leaders Group and ALTOUR signed a merger agreement creating a combined entity with **nearly $24 billion in annual sales**.

In **2020**, the parent rebranded from Travel Leaders Group to **Internova Travel Group**. In **January 2024**, Internova consolidated Travel Leaders Corporate and ALTOUR under the single ALTOUR brand, naming **Gabe Rizzi** as President.

### 1.2 Ownership chain

| Layer | Entity | Notes |
|---|---|---|
| Top | **Certares Management LLC** | PE firm, majority shareholder of Internova since early 2020 |
| Holding | **Internova Travel Group** | $6B+ in 2024 sales; ~5,500 employees globally |
| Operating | **ALTOUR** | Corporate travel division of Internova; ~$3-4B sales, ~1,300+ travel professionals across 53 offices |
| Sister brands | Global Travel Collection, Tzell, Protravel, Andrew Harper, Nexion, Bonotel, Vacation.com | Roll-up portfolio |

CEO **J.D. O'Hara** was previously a **Senior Partner at Certares** before becoming Internova CEO in January 2020. The PE owner is not arm's-length. The PE firm runs the company.

### 1.3 Financial signals

- Internova 2023 sales: $5.7B (Travel Weekly Power List)
- 2024 sales: ~$6B
- ALTOUR revenue estimates range from $434M to ~$3B+ in transaction volume (gross sales, not net revenue)
- Employee count varies: 1,200-4,200 depending on which subsidiaries are counted

### 1.4 Recent M&A and consolidation signals

Per Travel Weekly's interview with O'Hara: *"When O'Hara took over, he had way too many P&Ls and way too many direct reports with the company's 50 or so brands. Over the years, he's whittled that down."* He has signaled **further brand consolidation** is coming.

O'Hara to Skift: *"This is a business where scale gets rewarded... the more kind of volume that we can buy, but the right kind of volume, not just any volume, is really where we get rewarded."*

**Translation:** Scale and supplier override commissions, not service intimacy, is the explicit profit model.

---

## 2. The Product Stack

| Product | What it does | Buyer | Tech stack |
|---|---|---|---|
| **Core TMC** | Booking, account management, reporting | Mid-to-large enterprise travel managers | Sabre/Apollo GDS + Concur/GetThere/Rearden OBT |
| **ALTOUR Intelligence** | AI suite (Book, Predict, Respond, Transform, Insights, Shield) | Corporate travel managers | **Third-party: 'ello (AI Book) and Lumo (AI Predict)** — not proprietary |
| **ALTOUR Air** | Private aviation/charter | Existing corporate clients | Internal team, ~10 people post-Dyer departure |
| **ALTOUR Vacations** | Leisure crossover for corporate travelers | Same-account leisure spillover | GDS + leisure consortia |
| **YES (Your Event Solutions)** | MICE | Corporate event planners | Merged from 4 sub-brands April 2024 |
| **ALTOUR Capture** | Off-channel booking tracking | Travel managers with leakage problems | Partnership with CapTrav, Prime Numbers Technology, Oversee/Fairfly |
| **ALTOUR Mobile** | Traveler app | Travelers within corporate accounts | **Powered by mTrip** (third party) |

### Critical finding: "ALTOUR Intelligence" is a marketing wrapper, not proprietary AI

ALTOUR's press release explicitly credits:
- **AI Book** is "powered by **'ello**" — a separate Tel Aviv/NY conversational booking startup
- **AI Predict** is "powered by **Lumo**" — a Boston/Boulder PhD-founded ML startup that also licenses to Acai Travel and BizTrip AI

ALTOUR Intelligence is a **branded integration layer** over off-the-shelf vendor tech. Any competitor — including Latitude 43 — can license the same Lumo predictive engine. There is no proprietary AI moat.

---

## 3. Pricing & Deal Structure

ALTOUR's fee structure is **not on their website**. It is buried in client-specific MSAs. The fragments we can verify from public procurement disclosures:

| Source | Fee structure |
|---|---|
| **Dartmouth College** | **$26 per agent-assisted transaction**, charged only when ticket purchased |
| **Purdue Fort Wayne** | Fee schedule referenced, not published; references "Low Fare Guarantee" |
| **Industry benchmark (BTN)** | TMC agent-assisted fees range **$25-$35 for domestic, higher for international**; online bookings $7-$15 |

**Typical ALTOUR contract structure** (inferred from procurement docs and industry standard):
- Per-transaction agent fee (~$26-35 domestic, $50+ international)
- Online booking tool fee (~$7-15)
- Implementation fee (one-time)
- Possible management fee or volume rebate sharing
- After-hours service fees per call
- Pass-through of GDS segment fees on certain contracts

**Minimum effective floor:** ALTOUR's stated positioning targets enterprises. Industry rule of thumb: a TMC will not profitably service a company below ~$250K-$500K in annual T&E. **A solo founder spending $80K is below the cost-of-service floor for any direct ALTOUR relationship.**

---

## 4. Client Experience: Praise and Pain

### Yelp (3.5/59 reviews)
- **Praise:** Individual advisors named — "Charlene Fuentes," "Rae," "Stephanie" — for going above and beyond
- **Complaints:** *"Completely incompetent... refused to make a simple phone call"*; reservations not going through and being rebooked at higher rates; responses *"without signatures so customers cannot contact them in ways other than a generic info email address"*

### Glassdoor / Indeed (employees)
- **Overall:** 3.5/5 (Glassdoor 65 reviews), 3.4/5 (Indeed 32 reviews)
- **Recent verbatim, Oct 14, 2025 (Corporate Travel Specialist):** *"Heavily micromanaged"* and *"Favoritism is rampant"*
- **Aug 7, 2024 (Technical Support):** *"Pay structure does not keep up with inflation"; "Where you are is where you stay in the IT department"*
- **Sept 14, 2023:** *"upper management has no loyalty"; "Insurance is so expensive for a family"*
- **UK office:** *"The UK management team mean well but all decisions are overruled by US management who are incompetent and have zero regard for their employees"*
- **COVID:** *"Terrible handling of Covid 19 impact on people, making people redundant with little regard for employee contribution"*
- **Internova rating:** 3.6/5 across 34 reviews; described in some as *"dishonest"* with *"hard-to-cancel memberships"* and culture *"like a pyramid scheme"*

### The defining client-experience signal: micromanagement is degrading agent productivity

From Glassdoor: agents report that *"new systems that are supposed to help not actually helping agents and making simple phone calls and emails become multi-step wastes of time,"* reducing calls handled from *"many per hour to about 3 due to data entry requirements."*

This is the smoking gun. Internova's data/reporting tooling — the thing they sell to travel managers — is **actively making frontline service slower** for the traveler.

---

## 5. Leadership & Culture

| Name | Role | Tenure | Note |
|---|---|---|---|
| **J.D. O'Hara** | CEO, Internova | CEO since Jan 2020; with company since 2018 | Ex-Certares Senior Partner. Lehman alum. The PE owner's man. |
| **Gabe Rizzi** | President, ALTOUR | Since Jan 2024 (with Internova since 2016) | Ran Travel Leaders Corporate before consolidation |
| **Alexandre Chemla** | Founder, former CEO | Departed Dec 2023 | Stated he *"decided that the time had come to complete the integration with Internova Travel Group"* |
| **Mary Sue Leathers** | President, ALTOUR Meetings & Incentives | Continuing | |
| **Wynona Dyer** | Co-founder, ALTOUR Air | **Retired July 31, 2025** | Internova took full ownership |
| **Matthew Jones** | VP Product Management | New, Feb 2026 | From Travelport/BCD |
| **Bill Lemmon** | VP Global Sales, MICE | New, Feb 2026 | From MCI |
| **Brett Lindsey** | Sr Director of Sales | New, Feb 2026 | **Focus: midmarket segment expansion** |
| **Chantal Wulf** | VP Partner Management | New, Feb 2026 | |

### The two structural signals to read

1. **The founder is gone.** Chemla left at end of 2023. The Co-founder of ALTOUR Air retired July 2025. **The boutique DNA has departed.** What remains is a PE-installed operator (Rizzi) running a consolidated brand from a Certares portfolio company.

2. **The NousTravel defection.** In February 2025, Internova sued former ALTOUR exec **Anthony Lee Thomas** and **Barry Noskeau** for starting **NousTravel**, alleging Thomas took *"trade secrets"* and that *"seven senior employees have resigned since NousTravel's founding."* Internova paid Thomas a **$193,427.78** non-compete consideration, which they are now trying to claw back.

Seven senior ALTOUR employees resigning to follow two execs out the door is a culture statement. Senior people don't leave a healthy boutique to start a competitor. They leave because the PE-owned roll-up isn't the place they signed up for.

---

## 6. ICP — Who ALTOUR Actually Serves

**Stated ICP:** Mid-to-large enterprises with global travel programs. Trade press positioning calls them *"one of the largest travel management companies in the world."*

**Actual book of business (verifiable):**
- **Dartmouth College**
- **Purdue Fort Wayne / Purdue University system**
- **Ohio University**
- **OMNIA Partners** (group purchasing co-op channel to mid-market)
- Historically strong in **fashion, entertainment, finance, media**

**Floor of profitability:** Industry-standard cost-of-service floor for a full-service TMC with named-agent service is $250-500K T&E. The Brett Lindsey hire (Feb 2026) for *"midmarket segment expansion"* is itself the proof — ALTOUR is now intentionally trying to reach down-market because the upper enterprise market is mature/saturated. Even their definition of "midmarket" is companies with $1M+ programs, not individuals.

**The gap:** Anyone with $50K-$500K of personal/professional travel spend is invisible to ALTOUR. They are too small for a named account team and too big for OMNIA's transactional pass-through.

---

## 7. Technology Reality

| Layer | What ALTOUR claims | What it actually is |
|---|---|---|
| AI Book | "Conversational booking, VIP consultant in your pocket" | Licensed integration of 'ello |
| AI Predict | "Predicts disruption before airlines" | Licensed integration of Lumo |
| AI Insights | "Natural language portal" | NLP wrapper over GDS + Concur reporting |
| AI Transform | "AI video for policy training" | Synthesia-class avatar tool wrapper |
| AI Shield | "Real-time risk alerts, crisis comms" | Resold risk intelligence feed |
| Mobile app | Branded ALTOUR app | Powered by **mTrip** (third party) |
| OBT | Branded "online booking" | **SAP Concur, GetThere, Rearden** — not proprietary |
| GDS | — | Sabre/Apollo |

**Net:** ALTOUR has built an integration layer, not a product. Their tech is **rented**. The whole "AI suite" is a press-release veneer over best-of-breed vendor relationships any competitor could replicate in 60 days.

The platform is also built for the **travel manager**, not the traveler. The dashboards optimize for spend reporting, leakage capture, and policy compliance — buyer's tools, not flier's tools. ALTOUR Intelligence answers the procurement officer's questions. It does not answer the founder's question: *"Where am I sleeping tonight in São Paulo?"*

---

## 8. Service Promise vs. Reality

### The 24/7 desk
ALTOUR markets a 24/7 emergency desk routed *"to ALTOUR agents, not a secondary service."* Public sources do not confirm staffing geography. Industry norm: large TMCs operate hybrid hubs across US, UK, India (Bangalore/Pune), and Philippines. Internova has UK and Mexico operations explicitly. The absence of any "based in the US" claim on their after-hours page is itself the signal — if it were US-only, marketing would say so.

### Named human continuity
Dartmouth's procurement contract names "dedicated agents assigned to Dartmouth" — but agents are pooled per account, not per traveler. Multiple Yelp and Glassdoor reviews reference *"responses without signatures so customers cannot contact them"* — this is the **pod model** in practice. The contract names a team; the traveler gets whoever's on shift.

### IROPs (Irregular Operations)
The whole pitch of AI Predict is "we'll catch it before it happens." But when the Glassdoor agents are doing *"3 calls per hour because of data entry,"* the human side of IROPs handling is structurally throttled by the very system management installed to track productivity.

---

## 9. Marketing & GTM

- **Sales motion:** RFP-driven enterprise sales (procurement-led), supplemented by **GBTA Convention** sponsorship, GBTA regional chapters (Michigan, Denver), industry trade press
- **Content:** Blog "View from 36K" / "ALTOUR Insider" newsletter. Topics: duty of care, compliance, policy enforcement, AI rollout. **Every piece is written for the travel manager**, not the traveler
- **Press:** Heavy presence in Business Travel News, Travel Weekly, Skift, PhocusWire
- **Website funnel:** *"Let's Connect"* CTA → form → enterprise sales call. No self-serve pricing, no individual signup, no consumer pathway
- **Who they want to look like:** Amex GBT and BCD — the global TMC giants

---

## 10. Structural Weaknesses to Attack

### A. The "size of company" gap
ALTOUR's named-agent service requires ~$250K+ T&E minimum to be profitable; their actual sales team targets $1M+. Below that, you are routed through OMNIA, an online tool, or you simply don't get served. **A $50K-$500K solo founder/RIA/VC partner is in the dead zone.**

### B. The Internova absorption risk
ALTOUR is now one of three Internova divisions. JD O'Hara has explicitly said *"there will be a further whittling down of brands."* The brand is a sales channel, not a stewarded boutique. The founder is gone. The ALTOUR Air co-founder is gone. The Chemla-era ALTOUR no longer exists.

### C. The "named human" problem
Pooled agents on shift. Multiple verbatim reviews complain of unsigned emails and generic inboxes. The advisor named on the MSA is not necessarily the advisor servicing your trip.

### D. After-hours reality
ALTOUR will not publicly state where their after-hours desk is staffed. The geographic gap is real.

### E. Tech vs. service positioning dilution
By pivoting hard into "ALTOUR Intelligence" — competing on the Navan/TravelPerk axis — ALTOUR is **diluting its high-touch positioning**. They now have to be a tech platform AND a boutique service AND a global TMC. Trying to be all three simultaneously is a classic mid-market squeeze.

### F. PE compression
Certares is a private equity firm. PE math demands margin expansion. Internova's response: brand consolidation (cost out), micromanagement systems (productivity metrics), outsourcing (labor arbitrage). The Glassdoor signal — *"3 calls per hour"* — is the leading indicator of service-quality decay. The NousTravel defection (seven senior people out the door) is the lagging indicator.

---

## 11. Latitude 43 Attack Vectors

| # | ALTOUR reality | Latitude 43 counter |
|---|---|---|
| 1 | **Built for companies.** RFP-driven enterprise sales. No self-serve. | **Built for the individual.** A founder, GP, partner, or RIA principal signs up directly. No procurement department required. |
| 2 | **Floor: ~$250K-$1M T&E.** Mid-market hire confirms they're reaching DOWN; OMNIA channel confirms they don't service SMB directly. | **Floor: $50K personal T&E.** We are profitable on the exact buyer ALTOUR can't touch. |
| 3 | **Pod model.** Verbatim Yelp reviews: *"responses without signatures."* Glassdoor: *"3 calls per hour due to data entry."* | **One named advisor. 15 clients maximum.** The human on your contract is the human who picks up. |
| 4 | **24/7 desk geography opaque.** | **Founder's mobile number.** Pacific to Asia coverage published, named humans on the schedule. |
| 5 | **Fees buried in MSA.** No public pricing. Dartmouth pays $26/transaction. | **Atlas membership pricing on the website.** All-in. Unlimited tickets included. No surprises. |
| 6 | **"ALTOUR Intelligence" is for travel managers.** Dashboards measure leakage and policy compliance. | **Latitude 43 platform is for the traveler.** The screen answers "where am I, what's next, what do I need now?" |
| 7 | **$26-$35 per ticket on top of management fees.** | **Unlimited transactions inside Atlas membership.** |
| 8 | **Tech is licensed.** AI Book = 'ello. AI Predict = Lumo. Mobile = mTrip. | **Same best-of-breed integrations, but built around the traveler's day.** We don't pretend we invented the AI. |
| 9 | **Founder Chemla gone Dec 2023. Co-founder Dyer retired Jul 2025. NousTravel defection with 7 senior departures.** | **Founder-led, single-partner accountability.** The strategist's name and email is on the contract. |
| 10 | **Owned by Certares PE.** Brand consolidation explicit. O'Hara: *"scale gets rewarded."* | **Owned by its operator.** Optimized for client lifetime quality, not LBO return math. |
| 11 | **Pivoting toward Navan.** "ALTOUR Intelligence" positions them against tech platforms. | **Doubling down on advisor.** We are not a platform. We are the strategist who uses platforms on your behalf. |
| 12 | **Glassdoor: *"Heavily micromanaged. Favoritism is rampant"* (Oct 2025).** | **Built from a blank sheet in 2026.** No legacy systems, no PE quarter, no pod model to dismantle. |

---

## 12. The 250-Word Pitch — Verbatim

> ALTOUR is genuinely good at what they were built for: managing the corporate travel program of a 2,000-person company with a procurement officer and a travel manager. They have global supplier reach, a real 24/7 desk, and three decades of operating muscle. If you run travel for a Fortune 1000, they belong on your RFP shortlist.
>
> But that's not you. You're a founder, a GP, a partner. Your "travel program" is *you*, plus your two co-founders, plus your EA on a good day. You don't have a procurement department. You don't fit on an enterprise MSA. ALTOUR's direct sales team won't return your call below about $500,000 a year in spend, and if they do, you'll be routed to a pooled agent team where the human who answers an email is not the human who answers the next one.
>
> ALTOUR's founder Alexandre Chemla left at the end of 2023. The private equity owner, Certares, has been consolidating brands ever since. Seven senior people walked out the door in 2024 to start a competitor. The boutique they sell you is not the boutique that exists.
>
> Latitude 43 is built for you, specifically. One named advisor — me, or someone I personally hired — with no more than 15 clients on their book, ever. Atlas membership pricing published on our website. Unlimited tickets. My mobile number when you're stuck in Frankfurt at 2 a.m.
>
> They scaled until they're owned by spreadsheets. We're not going to. That's the whole thesis.

---

## Sources

- Internova History — https://internova.com/history/
- Travel Leaders Group and ALTOUR Announce Merger (2017) — https://internova.com/travel-leaders-group-and-altour-announce-merger/
- Internova Rebrands Travel Leaders Corporate as ALTOUR — https://www.travelmarketreport.com/retail-strategies/articles/internova-rebrands-travel-leaders-corporate-as-altour
- Internova consolidates corporate travel under Altour brand — Travel Weekly — https://www.travelweekly.com/Travel-News/Travel-Agent-Issues/Internova-consolidates-corporate-travel-under-Altour-brand
- Certares' Internova strategy for luxury travel — Skift — https://skift.com/2023/10/27/certares-internova-behind-its-strategy-for-luxury-travel-agencies/
- Internova CEO plans further brand consolidation — Travel Weekly — https://www.travelweekly.com/Travel-News/Travel-Agent-Issues/Internova-CEO-plans-more-brand-consolidation
- JD O'Hara bio — Internova — https://internova.com/leadership-jd-ohara/
- ALTOUR — What We Do — https://altour.com/what-we-do/
- ALTOUR Intelligence — https://altour.com/altour-intelligence/
- PRNewswire: ALTOUR Unveils AI-Powered Solutions — https://www.prnewswire.com/news-releases/altour-unveils-ai-powered-business-travel-solutions-set-to-revolutionize-corporate-travel-management-302202965.html
- 'ello and ALTOUR conversational booking — https://sayello.co/blog/ello-and-altour-to-showcase-converssational-travel-booking-at-innovation-faceoff-london-2025
- Lumo (thinklumo.com) — https://www.thinklumo.com/
- ALTOUR Air co-founder Dyer retires; Internova full ownership — https://www.travelmarketreport.com/air/articles/altour-air-cofounder-to-step-down-giving-internova-full-ownership
- SAP Concur partner page for ALTOUR — https://www.concur.com/partners/altour
- mTrip powers ALTOUR mobile app — https://www.mtrip.com/altour-mobile-app/
- Dartmouth procurement — ALTOUR contract — https://www.dartmouth.edu/finance/purchasing/business_travel/travel/
- Purdue Fort Wayne — ALTOUR contract — https://www.pfw.edu/offices/accounting/travel/altour.html
- BTN: TMC Fee Models Primer — https://www.businesstravelnews.com/SME/Primers/TMC-Fee-Models-Topline-Review
- Altour Reviews — Glassdoor — https://www.glassdoor.com/Reviews/Altour-Reviews-E33653.htm
- Altour customer reviews — Yelp — https://www.yelp.com/brands/altour
- Alexandre Chemla leaving ALTOUR — Travel Weekly — https://www.travelweekly.com/Travel-News/Travel-Agent-Issues/Alexandre-Chemla-leaving-Altour
- Internova sues former ALTOUR employees — Travel Weekly — https://www.travelweekly.com/Travel-News/Travel-Agent-Issues/Internova-sues-former-Altour-employees
- ALTOUR Strengthens Leadership Team (Feb 2026) — https://altour.com/altour-strengthens-leadership-team-to-advance-growth-and-industry-excellence/
- Gabe Rizzi — BTN 25 Most Influential — https://www.businesstravelnews.com/Most-Influential/2025/Gabe-Rizzi
