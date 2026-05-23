# Cadence Travel: Forensic Competitive Analysis for Latitude 43

*Prepared for: CEO, Latitude 43. Date: May 2026. Status: Confidential.*

---

## Executive Summary

Cadence (legal name CADENCE Travel; dba `cadencetravel.com`) is a 30-year-old luxury-leaning travel agency headquartered at 7701 Herschel Avenue, La Jolla, CA. Founded in 1995 by **Wendy Burk** (still CEO, in travel since 1977), it operates today as a **branch of Tzell Travel Group**, which sits inside **Global Travel Collection**, which sits inside **Internova Travel Group**, which is **majority-owned by private-equity firm Certares**. Cadence is therefore not founder-controlled in any economic sense; Burk runs it operationally, but the equity capstack is PE.

It runs three businesses under one roof — **Managed Business Travel**, **Meetings & Incentives (M&I)**, and **Cadence Hosting** (host agency for ~200 independent leisure-focused advisors) — plus a **VIP Traveler Program** layered on top of the corporate book. 2024 sales: **$326.5M**; ~50 W-2 employees plus ~150 advisor staff; 200+ ICs. Travel Weekly 2024 Power List rank: #46.

The brand is real, the supplier relationships are real, the Virtuoso status (since 1999) is real. The vulnerabilities are also real: a public-facing 8:30–5:30 PT business-hours signal on the homepage, an opaque VIP program with no pricing, a stitched-together tech stack (TripSuite + Spotnana + third-party SafeToGo + Sabre/Apollo GDS), a "three masters" service model that splits attention between corporate, MICE, and 200 leisure ICs, and persistent customer- and employee-side complaints about service consistency. These are the seams to attack.

---

## 1. Company Structure & Ownership

### History

| Year | Event |
|---|---|
| 1995 | Founded in La Jolla by Wendy Burk with three agents as a **corporate** travel agency |
| 1998 | First business travel reporting tool deployed |
| 1999 | Joins **Virtuoso** (Sept 14, 1999) |
| 2003 | M&I division launched at client request |
| 2012 | Moves to current HQ at 7701 Herschel Ave, La Jolla |
| 2015 | 20-year anniversary; later joins **Tzell Travel Group** as a branch |
| 2020 | Parent reorg: Travel Leaders Group rebrands to **Internova Travel Group** (Certares-owned) |
| 2022 | Highest employee headcount, IC count, and sales in 28-year history |
| 2024 | Sales pass $300M; **TripSuite** (back-office, AI accounting/CRM) launched Oct 7, 2024 |
| 2025 | **Spotnana** front-office partnership announced March 26, 2025; 30-year anniversary |
| 2026 | Independent affiliate advisors named 2026 Virtuoso Cruise Icons |

### Ownership stack

```
Certares (PE)
  └─ Internova Travel Group
       └─ Global Travel Collection
            └─ Tzell Travel Group
                 └─ Cadence (branch)
```

This matters. The "family-owned business" framing in employee reviews and Burk's "we lead with care" copy is brand positioning; the cap table is a PE rollup. Latitude 43 should never let a prospect think Cadence is an independent boutique. It isn't.

### Scale

- 2024 sales: **$326.5M** (Travel Weekly Power List)
- **~50 W-2 employees**
- **200+ independent contractor advisors** (mostly leisure)
- **One office: La Jolla, CA**. No published satellite offices
- Travel Weekly 2024 Power List rank: **#46**

---

## 2. The Full Product/Service Stack

### Homepage hero (verbatim)

> "Unforgettable Leisure Travel / Impactful Meetings & Incentives / Strategic Business Travel"
> "We are a world-renowned travel agency dedicated to the art of taking better care of travelers."
> "Find your Cadence, and experience travel like you've never experienced it before."

Three product lines, equal weight on the hero. This is the **three masters problem** crystallized in their own copy.

### 2.1 Managed Business Travel

- Sells a "managed program" — policy, spend monitoring, reporting, traveler support
- Tech stack disclosed on `/business-travel`: Concur, Deem, Certify (booking); SafeToGo (duty of care); TripCase + TripIt (itinerary); Grasp Reporting; iQCX QC; Marketo; Fare Checker
- Self-claimed metrics: "95% rate service as 'Absolute Perfection'", "30% fewer transactions per agent vs industry," "99% retention," "44% of new accounts from referrals," "$150M+ annual sales" (corp portion only)
- **No pricing, no named clients, no case studies on the page**

### 2.2 Meetings & Incentives

- "Full-Service Program Management," hotel sourcing, attendee management, "Group air management through parent company Tzell," on-site staffing, SMM
- Uses Cvent for registration, SafeToGo for safety, and now **Spotnana** for corporate travel modernization
- Tagline: "our people are our product"
- **No pricing, no named clients, no case studies**

### 2.3 Cadence Hosting

- **200+ ICs**, mostly leisure focused
- Per HostAgencyReviews: $0 franchise/start-up fee; commission split, monthly fee, ticketing fee — **all undisclosed publicly**; USA agents only; experienced agents only
- Operates the annual **Cadence Connects** supplier–advisor event (May 7–10, 2025 at Hotel del Coronado, 10th anniversary)

### 2.4 VIP Traveler Program

- Lives at `/vip`. Marketed as "an exclusive service tier reserved for the top business travelers of your company"
- Benefits: expedited response, additional QC, "waivers + favors extended to VIPs first," surprise-and-delight, proactive monitoring, complimentary leisure planning
- **Dedicated VIP line: 858.551.3060 (24/7) and `vip@cadencetravel.com`**
- **No tier names. No pricing. No eligibility threshold. No application process.** Employer-designated, not user-purchasable.

### 2.5 SafeToGo

- This is **not proprietary**. SafeToGo is a third-party duty-of-care platform owned by **Magnatech** (UK-based travel management solutions vendor). Multiple TMCs license it
- Cadence's marketing implies SafeToGo is a branded feature. Their `/business-travel` page describes it as part of their stack, not their IP

### 2.6 Tech stack — true picture

| Layer | Reality |
|---|---|
| GDS | Sabre + Apollo |
| Front-office TMC tool | **Spotnana** (March 2025 partnership) |
| Online booking | Concur, Deem, Certify |
| Mid/back-office | **TripSuite** (Oct 2024) — AI-powered CRM, commission tracking, accounting |
| Duty of care | SafeToGo (Magnatech, licensed) |
| Itinerary | TripCase + TripIt (Concur) |
| Reporting | Grasp Reporting |
| QC | iQCX |
| Event registration | Cvent |

**Headline:** Cadence does not own its tech. It is a systems integrator stitching Spotnana, TripSuite, SafeToGo, Concur, Cvent, and Sabre. Every piece is rentable; none of it is a moat.

---

## 3. Pricing & Deal Structure

- **Managed corporate**: not disclosed publicly. Industry-standard TMC pricing is per-transaction (PNR) plus management fee plus per-traveler license fees for SafeToGo/Concur — Cadence does not disclose its breakdown
- **MICE**: bespoke; à-la-carte sourcing fees common in industry
- **Host agency**: $0 start-up; commission split undisclosed; monthly/annual fees undisclosed
- **VIP program**: no pricing surfaced — it is a service tier inside a corporate contract
- **Minimum spend / client size**: undisclosed publicly

**Net**: zero price transparency anywhere on the site. Every engagement requires a sales conversation.

---

## 4. The Actual Client Experience

### 4.1 Trustpilot (client-side)

The single most damning piece of public client review:

> "We did not experience the 'world class white glove care' advertised. Our agent forgot to remind us to book airline seats… other passengers on the cruise got ship credits, free beverage packages, and gift baskets in their rooms. We received nothing. We were told several things that were untrue, including an incorrect check-in time for a river cruise. We gained nothing by using a travel agent and do not recommend Cadence."

### 4.2 Yahoo / Google reviews

Local Yahoo review describes the front-of-house staff as **"full of attitude"** with the suggestion to "try another place that would treat customers nicely."

### 4.3 Glassdoor — Cadence (CA)

Headline pros: benefits (health, 401K, dental, vision), described in some reviews as "the BEST family-owned business"

Headline cons:

> "Lots of employee turnover and very low employee morale. The company is extremely disorganized with no clear direction from upper management and constantly changing policies."
>
> "Cadence used to be great but has declined. Typical workdays involve confusion, stress, and bad attitudes with no clear guidance or direction and constantly changing procedures."
>
> "Entry-level job salaries aren't very high considering the cost of living in California."

**The same reviews praising Burk's accessibility describe the operating layer beneath her as chaotic, under-paid, and high-turnover. That is the layer that touches your client every day.**

### 4.4 Internal red flag

Cadence advertises a 2025 footprint of only **27 Yelp reviews** total over its lifetime in La Jolla. For a 30-year, $326M-revenue firm, that's a deliberately low public review footprint — meaning their reputation is largely managed in private channels rather than open web.

---

## 5. Leadership & Culture

### Executive team

| Name | Title |
|---|---|
| Wendy Burk | Founder & CEO |
| Harold Frysh | Chairman |
| Eitan Geft | President |
| Gina Jackson | VP, Finance |
| Jenn Mitchell | VP, Operations |
| John Knob | Senior Director of Culture |
| Chardell Robinson | VP, Corporate Sales & Account Management |

**Observation**: Cadence has a Chairman (Frysh) and a President (Geft) layered above Burk operationally. That is uncommon for a 50-person founder-led shop and is a structural signal of Tzell/Internova oversight.

### Sales motion

- **Inbound + referral-led.** Burk's interviews stress: "44% of new accounts from client referrals"
- **Cadence Connects** (their own annual event, 10 years running) is the primary GTM motion for the host side
- No evidence of GBTA/ACTE booth presence in 2024–2026 search results, suggesting **weak presence at the corporate travel buyer's conferences** despite their corporate-travel claim

### Culture signals

- 7 consecutive years on San Diego "Best Places to Work" list
- But Glassdoor cons: "extremely disorganized," "no clear direction," "constantly changing policies," "low morale" — coexisting with the awards
- Award-bait culture programming (John Knob's "Senior Director of Culture" title) over operational discipline is one read

---

## 6. ICP — Who They Actually Serve

### Stated targets

- **Corporate**: managed-program clients
- **MICE**: Spotnana announcement explicitly names "small to mid-sized businesses and meeting planners"
- **Leisure**: ultra-high-net-worth retail clients sourced through the 200 ICs and the Virtuoso channel

### Actual book

- No publicly named corporate clients. Supplier-side testimonials (Hyatt's Raffaela Tasca, Four Seasons' Victoria Uslaner) dominate the public references — they reference **how nice Cadence is to work with**, not **what client outcomes they delivered**

### Where the cracks are

- **Founders/VC partners/PE deal teams with $50K–$2M T&E spend**: too small to be a meaningful "managed program" client. These spenders fall into a **no-man's-land** between Cadence's corporate desk and the host-agency leisure ICs
- **Solo professionals / RIAs**: same gap. They want a single named human for both work and personal travel; Cadence routes work travel to the corporate desk and personal travel to a separate leisure advisor

**This is Latitude 43's lane.**

---

## 7. Technology Reality

| Claim | Reality |
|---|---|
| "SafeToGo Software" (corporate page) | Licensed third-party from Magnatech. Not proprietary |
| Spotnana partnership (Mar 2025) | Front-end TaaS booking platform. SMB-focused |
| TripSuite (Oct 2024) | Third-party AI back-office — early-stage startup ($5M seed from F-Prime, 2024) |
| Traveler app | TripCase / TripIt (both Concur properties). No Cadence-branded app |
| Reporting | Grasp Reporting (third-party) |
| GDS | Sabre + Apollo |

**Verdict**: Cadence's "technology" page is a list of vendors. Their stack in 2025 is **two new partnerships (Spotnana + TripSuite) bolted onto a Sabre/Apollo + Concur backbone with SafeToGo licensed in.**

---

## 8. The Service Promise vs. Reality

### The hours problem

**Homepage** (`cadencetravel.com`): "Monday–Friday: 8:30am to 5:30pm" — the only hours visible on the front door.

**Travel Support page** (`/travel-support`): three different desks with three different hours:

| Desk | Hours | Channel |
|---|---|---|
| Agent (main) | 6:00am – 5:00pm PT, Mon–Fri | corpres@cadencetravel.com / 858.551.3000 |
| After-hours emergency | 5:00pm – 6:00am PT Mon–Fri; **24h Sat–Sun** | emergency@cadencetravel.com / 858.551.3041 (**code: SV23G**) |
| Online booking tool support | 7:00am – 5:00pm PT, Mon–Fri | onlinehelp@cadencetravel.com |
| VIP line | 24/7 | vip@cadencetravel.com / 858.551.3060 |

**Findings**:

1. They **do** have an after-hours desk. But it's a different number, requires a **call-in code (SV23G)** which is friction in an actual disruption, and the homepage doesn't surface it — a prospect scanning the front door sees "8:30–5:30, M–F" and walks
2. The VIP line is the only 24/7 main channel, and access to it is **employer-controlled** and undefined
3. There is no disclosure of whether the after-hours desk is in-house or outsourced. Industry convention: 5pm–6am after-hours coverage at agencies the size of Cadence is **outsourced to consortium-shared call centers**
4. The "code SV23G" reads like a Sabre/Tzell queue-routing code that has lived in their copy for years. That's a brand staleness tell

### Response-time commitments

- **No SLA disclosed anywhere on the site**

### Account manager continuity

- Not addressed in public materials. Multiple "Account Director" titles, suggesting a **pod or assignment model**

---

## 9. Marketing & GTM

### Content

The blog has **substantially more than 3 articles** — current snapshot shows ~20 posts in 11 weeks, ~2/week. Topics are nearly all **leisure-skewed supplier features**: Auberge in Mexico, Rocco Forte suites, Four Seasons yachts, AmaWaterways, Crystal Cruises.

**Implication**: the editorial engine serves the host-agency / leisure side. Corporate buyers visiting the blog see hotel features, not procurement insights, RFP guides, T&E benchmarking, or duty-of-care analyses. The content strategy is **inconsistent with their stated corporate positioning**.

### Brand staleness

- Visual: the site uses photographic hero cards with simple text overlays, three-up service blocks, and a "EXPLORE" CTA pattern that was design-fashion ~2014–2017
- The press-release voice ("art of taking better care of travelers," "find your Cadence") reads as same-era luxury-agency cliché
- The "code SV23G" buried in the after-hours flow has not been re-thought in years

---

## 10. Structural Weaknesses to Attack

### A. The "business hours problem"

The homepage publishes **Mon–Fri 8:30–5:30 PT** as the company's hours. They have an after-hours emergency desk, but:
1. It's invisible from the front door
2. It requires a code (SV23G)
3. It's likely outsourced to a Tzell/Internova shared after-hours pool
4. There is **no first-response SLA** committed publicly

For a founder traveling at 2am ET who misses a connection, the brand experience starts with "they're closed."

### B. The "three masters" problem

Hero-equal billing for Leisure / M&I / Business Travel. The blog is 90% leisure. The biggest sales/PE wins (Spotnana, TripSuite) are for the corporate/M&I side. The 200 ICs are leisure. **Cadence's center of gravity is leisure host-agency; corporate is the second child.**

### C. The "dated brand" issue

Stagnant voice, stagnant UX patterns, stagnant operational artifacts (the SV23G code). The 30-year anniversary press release in 2025 is the most recent flagship — backward-looking framing.

### D. The "regional concentration"

- One office, La Jolla
- One time zone (Pacific) for primary hours
- No East-Coast presence for clients in NY/Boston/Miami finance hubs

### E. The "Top Traveler VIP Program" mystery

The VIP page exists but contains no tier names, no pricing, no eligibility threshold, no application path for individuals. It is employer-designated only.

### F. The "host agency vs. corporate" tension

200 leisure-focused ICs versus a corporate-managed-program desk under one roof, one brand, one supplier-relations team. The leisure side gets the Virtuoso amenities, the Cadence Connects spotlight, the blog real estate, and the board seats.

### G. The "named human" problem

Multiple Account Director titles, pod-and-rotation likely default for sub-VIP corporate accounts.

---

## 11. The Latitude 43 Attack Vectors

### A. Hours and SLA

**Cadence:** Public homepage hours are "Monday–Friday: 8:30am to 5:30pm" PT. The after-hours line requires a code SV23G. No public response-time SLA.

**Latitude 43:** Publish **24/7/365** on the homepage. Commit to a **60-minute first-response SLA**. Single phone number, no code.

### B. Specialization vs. three masters

**Cadence:** Hero copy splits Leisure / M&I / Business Travel equally. Center of gravity is leisure-host.

**Latitude 43:** One business: **luxury business travel advisory for founders, VC partners, PE deal teams, RIAs, and solo professionals.** No MICE side hustle. No host agency.

### C. Price transparency

**Cadence:** Zero pricing on any product line.

**Latitude 43:** Three named **Latitude Atlas** tiers with **public annual prices on the homepage.**

### D. Named human

**Cadence:** Pod-model implied. Glassdoor cites "constantly changing policies" and turnover.

**Latitude 43:** Founder/principal handles the relationship until book size forces a hire — and even then, the principal stays on the contract.

### E. VIP transparency

**Cadence:** The VIP Traveler Program has no tier names, no pricing, no eligibility threshold, no self-serve signup.

**Latitude 43:** **Latitude Atlas** — three named tiers, public eligibility criteria (annual T&E spend bands), public annual price list.

### F. Content commitment

**Cadence:** Blog is ~90% leisure supplier features; almost no corporate-buyer-grade content.

**Latitude 43:** **Latitude Journal** commits to 52 weeks of content per year, **operator-grade**: founder T&E benchmarks, post-mortems of real disruptions.

### G. Brand register

**Cadence:** Voice is 2014-era luxury-agency cliché.

**Latitude 43:** Launching in 2026 with an **operator-luxe register** — built for buyers who came up on Stripe, Linear, Ramp, and Mercury.

### H. Tech narrative

**Cadence:** Stitches Spotnana (front), TripSuite (back), SafeToGo (licensed). "SafeToGo Software" is not proprietary.

**Latitude 43:** Don't try to out-tech them on TMC plumbing. Compete on **service-layer software**: a public client portal showing every trip, every disruption, every dollar saved.

### I. Independence of voice

**Cadence:** PE-owned (Certares → Internova → GTC → Tzell → Cadence).

**Latitude 43:** Boutique under Fora as host. Aligned incentives. No PE clock.

### J. Geography & time zone

**Cadence:** One Pacific-time office in La Jolla.

**Latitude 43:** Toronto-based principal sits **3 hours closer to NY/Boston** than La Jolla.

---

## 12. The Pitch (250 words, deliverable verbatim)

> Cadence Travel has earned its 30 years. Founded by Wendy Burk in 1995, they did $326 million in 2024, they've been a Virtuoso member since the Clinton administration, and their relationships with Four Seasons, Ritz-Carlton, Rosewood, and the major cruise lines are real. They host 200 luxury advisors, they run their own annual supplier event, and they recently signed Spotnana and TripSuite to modernize the stack. If you are a 500-person SMB with a corporate-card program, a managed-travel policy, a Concur instance, and a meeting-planner on staff — Cadence is built for you.
>
> But that's not you. You're a founder, a VC partner, a deal lead, an advisor with a book. Your T&E is between fifty thousand and two million dollars. You are simultaneously your CFO, your traveler, your CEO, and your spouse's plus-one in Lisbon next month. Cadence's homepage publishes Monday-to-Friday, 8:30-to-5:30 Pacific hours. Their VIP program is unpriced and employer-designated. Their book of business sits behind one office in La Jolla and 200 leisure independents.
>
> Latitude 43 is built for you. We do one thing: luxury business travel advisory for operators who treat work travel and personal travel as one life. Twenty-four-seven, sixty-minute first response in writing. Three named price tiers on our homepage. A founder who answers the phone. Toronto-based, eastern-time-first. Launching in 2026 with the operator-luxe register the category has needed for ten years.
>
> Same supplier amenities. Same Virtuoso access. A different decade of brand.

---

## Appendix: Sources

- Cadence homepage (`cadencetravel.com`)
- `/about-us`, `/our-team-bios`, `/business-travel`, `/meetings-incentives`, `/hostagency`, `/vip`, `/travel-support`, `/press`, `/travel-blog`
- Travel Weekly 2024 Power List entry
- PR Newswire — "Cadence Marks 30 Years of Excellence in Luxury Travel" (Jan 2025)
- PR Newswire — "Cadence Partners with Spotnana" (Mar 26, 2025)
- PR Newswire — "Cadence Ushers in New Era of Travel Technology" / TripSuite (Oct 7, 2024)
- Business Travel News — "TMC Cadence Taps Spotnana as Tech Partner"
- HostAgencyReviews — `hostagencyreviews.com/hosts/cadence`
- Trustpilot — `trustpilot.com/review/cadencetravel.com`
- Yelp — `yelp.com/biz/cadence-travel-la-jolla`
- Glassdoor — `glassdoor.com/Reviews/Cadence-CA-Reviews-E1471950.htm`
- Authority Magazine / Medium — Women of the C-Suite interview with Wendy Burk
- Skift — "Certares' Internova: Behind Its Strategy for Luxury Travel Agencies" (Oct 27, 2023)
- Magnatech — `magnatech.com/traveller-tracking/` (SafeToGo ownership)
- Virtuoso — `virtuoso.com/agencies/1152/cadence`
