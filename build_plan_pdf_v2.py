"""Generate the Preface v2 business plan — rewritten with founder-specific signal."""
from pathlib import Path
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

# Import the CSS framework from v1
import build_plan_pdf as v1

OUT = Path(__file__).parent / "Preface-Business-Plan-v2.pdf"


def html_body():
    return r"""
<!-- COVER -->
<div class="cover">
    <div class="cover-mark">Preface</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">The Business Plan<br/><span style="font-style: italic; font-weight: 300;">v2</span></h1>
    <div class="cover-subtitle">Personalized to who you actually are, what you actually want, and the network you actually have.</div>
    <div class="cover-meta">
        <div>
            <span class="label">Prepared for</span>
            <span class="value">Founder — Preface</span>
        </div>
        <div>
            <span class="label">Date</span>
            <span class="value">May 21, 2026</span>
        </div>
        <div>
            <span class="label">Revision</span>
            <span class="value">v2 — Post-Founder-Intake</span>
        </div>
    </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="toc">
    <h1><span class="num">Contents</span>Table of Contents</h1>
    <div class="toc-entry"><span class="num">01</span><span class="title">What Changed in V2</span></div>
    <div class="toc-entry"><span class="num">02</span><span class="title">Executive Summary</span></div>
    <div class="toc-entry"><span class="num">03</span><span class="title">Founder Profile (Distilled)</span></div>
    <div class="toc-entry"><span class="num">04</span><span class="title">Unit Economics &amp; Math</span></div>
    <div class="toc-entry"><span class="num">05</span><span class="title">Market Position — The Thornhill Wedge</span></div>
    <div class="toc-entry"><span class="num">06</span><span class="title">The Six-Horizon Plan</span></div>
    <div class="toc-subentry"><span>6.1   Month 1 — Foundation (Day-Job Continues)</span></div>
    <div class="toc-subentry"><span>6.2   Months 2–3 — Activate the Network</span></div>
    <div class="toc-subentry"><span>6.3   Months 4–6 — Outsource &amp; Automate</span></div>
    <div class="toc-subentry"><span>6.4   Year 1 — Hit $2,500/wk by Day 300 (Day Job Stays)</span></div>
    <div class="toc-subentry"><span>6.5   Year 3 — Amplification, Not Replacement</span></div>
    <div class="toc-subentry"><span>6.6   Year 5 — Two Paths Surface</span></div>
    <div class="toc-entry"><span class="num">07</span><span class="title">The Network-First Growth Engine</span></div>
    <div class="toc-entry"><span class="num">08</span><span class="title">The Outsourced Content Strategy</span></div>
    <div class="toc-entry"><span class="num">09</span><span class="title">Financial Projections (Your Income Tiers)</span></div>
    <div class="toc-entry"><span class="num">10</span><span class="title">Capital &amp; Tooling</span></div>
    <div class="toc-entry"><span class="num">11</span><span class="title">Risk Register</span></div>
    <div class="toc-entry"><span class="num">12</span><span class="title">Decision Gates</span></div>
    <div class="toc-entry"><span class="num">13</span><span class="title">Weekly Operating Rhythm (Ambivert-Friendly)</span></div>
    <div class="toc-entry"><span class="num">14</span><span class="title">The Two-Path Exit Math</span></div>
    <div class="toc-entry"><span class="num">A</span><span class="title">Appendix — Updated Templates &amp; Scripts</span></div>
</div>

<!-- 01 WHAT CHANGED -->
<section>
<h1><span class="num">Section 01</span>What Changed in V2</h1>
<p class="lead">V1 was a strong generic plan for an unknown founder. V2 is a specific plan for you. Here's what moved.</p>

<table>
<thead><tr><th>Dimension</th><th>V1 Assumption</th><th>V2 Reality</th></tr></thead>
<tbody>
<tr><td><strong>Wedge market</strong></td><td>Generic 28&ndash;36 Toronto millennials</td><td>Thornhill / Toronto Jewish community network &mdash; dense, family-oriented, segment-aligned</td></tr>
<tr><td><strong>Growth engine</strong></td><td>Cold outreach machine drives funnel; partnerships secondary</td><td>Partnership network is primary; cold outreach is a set-and-forget background process</td></tr>
<tr><td><strong>Day-job timing</strong></td><td>Quit at month 6 if business hits $1K/wk</td><td><strong>Day job stays through month 15&ndash;18 minimum.</strong> Under-3-months runway makes earlier exit financially unsafe</td></tr>
<tr><td><strong>Content strategy</strong></td><td>Founder produces 12+ posts/wk personally</td><td>Founder records voice memos + sends client takeaways; VA produces content from month 4</td></tr>
<tr><td><strong>Hire philosophy</strong></td><td>Hire to free yourself from sales work</td><td>Hire to amplify the operator-in-chief; founder stays in the action through Y5</td></tr>
<tr><td><strong>End-state</strong></td><td>Build to sell</td><td>Build to own, with exit optionality preserved &mdash; founder loves the operator role</td></tr>
<tr><td><strong>Income arcs</strong></td><td>Single $400&ndash;600K Y5 midpoint</td><td>Five-tier ladder modeled: $15K / $25K / $35K / $80K / $250K monthly &mdash; each with specific gates</td></tr>
<tr><td><strong>Brand direction</strong></td><td>Refined warm-classic (Cormorant Garamond, cream/burgundy)</td><td>Cool modern minimal visuals + playful, irreverent voice &mdash; Mejuri / Away / Glossier reference points (see separate brand deliverable)</td></tr>
<tr><td><strong>FAM trips</strong></td><td>Pursue actively in Y1</td><td>Only if fully comped &mdash; founder prefers personal travel investment</td></tr>
<tr><td><strong>Sales motion</strong></td><td>Cold-led hunter</td><td>Relationship-led closer with partnership infrastructure</td></tr>
</tbody>
</table>

<div class="callout gold">
    <h4>The Strategic Reframe</h4>
    <p>V1 treated this as a sales-and-marketing scale challenge. V2 treats it as a <strong>network-monetization business</strong> with an automation layer underneath. The Thornhill Jewish community is your unfair advantage; the broader millennial brand is your TAM expansion in Year 2 onward.</p>
</div>
</section>

<!-- 02 EXECUTIVE SUMMARY -->
<section>
<h1><span class="num">Section 02</span>Executive Summary</h1>
<p class="lead">Preface is a Toronto millennial travel agency that grows from a dense, affluent referral network into a broader brand. Built by a relationship-led operator who loves running the room.</p>

<h2>The Thesis</h2>
<p>You're not a content creator who happens to sell travel. You're a relationship-led closer with a dense, segment-perfect network in the Toronto/Thornhill Jewish community &mdash; affluent families with predictable spend on bach trips, honeymoons, Israel pilgrimages, milestone celebrations, and multi-generational holidays. That network is your wedge. Activate it first; expand to broader millennials in Y2&ndash;Y3.</p>

<p>The path: <strong>day job stays through month 15&ndash;18</strong> because your runway requires it. Inside that window, you license up (TICO + Fora), activate your warm network, build referral partnerships with planners and brokers you already know, and ship a set-and-forget cold-outreach engine for US partners. Content gets outsourced from month 4 to a VA who turns your voice memos into newsletter posts and Reels. By day 300, the practice is producing $2,500/wk in commissions; by month 18, you can quit the day job safely. By Year 5, you're either a $500K+ lifestyle operator or a $3&ndash;16M exit candidate.</p>

<h2>The Five-Tier Income Ladder</h2>
<div class="exec-stats">
    <div>
        <div class="label">Tier 1 &mdash; Comfortable</div>
        <div class="stat">$15K/mo</div>
        <div class="note">Reachable in Y1 Q4; replaces day-job net</div>
    </div>
    <div>
        <div class="label">Tier 2 &mdash; Wanted</div>
        <div class="stat">$25K/mo</div>
        <div class="note">Y2 with consistent partnership volume</div>
    </div>
    <div>
        <div class="label">Tier 3 &mdash; Target</div>
        <div class="stat">$35K/mo</div>
        <div class="note">Y3 with 2&ndash;3 sub-advisors producing</div>
    </div>
    <div>
        <div class="label">Tier 4 &mdash; Goal</div>
        <div class="stat">$80K/mo</div>
        <div class="note">Y5&ndash;Y6 with full team + brand pull</div>
    </div>
</div>
<p class="small" style="margin-top: -0.1in;">A fifth tier &mdash; <strong>$250K/mo ($3M/yr)</strong> &mdash; is the Y7&ndash;Y10 picture. It requires either an exit producing $15M+ (annualizable returns) or a 20+ advisor team at scale. Real, but not bookable to a five-year plan.</p>

<h2>Why You Win</h2>
<ul>
<li><strong>Network density.</strong> 100+ peers in target demo, plus existing planner / mortgage broker / real-estate connections feeding leads.</li>
<li><strong>Sales-led temperament.</strong> Relationship-builder, not a content creator. Plan respects that.</li>
<li><strong>No competitive constraints.</strong> Day-job contract is clean &mdash; can operate openly.</li>
<li><strong>Low burn.</strong> $5K/mo personal expenses means a faster break-even than typical founders.</li>
<li><strong>Caribbean + Europe + LatAm fluency.</strong> Your travel CV aligns with honeymoon, family all-inclusive, and bach segments &mdash; exactly your demo.</li>
</ul>

<h2>The Constraints That Shape Everything</h2>
<ul>
<li><strong>Under 3 months runway.</strong> Day job continues through month 15&ndash;18 minimum.</li>
<li><strong>Content is a weakness.</strong> Outsourced from month 4.</li>
<li><strong>Ambivert energy budget.</strong> Cap client calls at 5/day. Protect solo blocks.</li>
<li><strong>Functional (not strong) tech.</strong> Buy the stack; one-time contractor wires it up.</li>
<li><strong>No fully-comped FAM acceptance unless deeply comped.</strong> Site visits funded selectively.</li>
</ul>

<h2>The Tension To Watch</h2>
<div class="callout warn">
    <h4>Operator vs. Exit</h4>
    <p>You said &ldquo;build something I own&rdquo; (favors exit) AND &ldquo;high-touch operator &mdash; busy and important&rdquo; (favors lifestyle). These are in tension. Operators who love running the room rarely sell &mdash; acquirers buy businesses that run <em>without</em> the founder. V2 surfaces both paths. The hybrid decision at year 4 stays open, but if you want to preserve real exit optionality, Y3 must include a deliberate transition plan: documented SOPs, a recognizable advisor team, and a brand strong enough to outlive your daily presence.</p>
</div>
</section>

<!-- 03 FOUNDER PROFILE -->
<section>
<h1><span class="num">Section 03</span>Founder Profile (Distilled)</h1>
<p class="section-intro">The compressed read on who you are, used as input to every other decision in this plan.</p>

<h2>How You Operate</h2>
<table>
<tbody>
<tr><td><strong>Top skill</strong></td><td>Building relationships, networking, long-game trust</td></tr>
<tr><td><strong>Weakest skill</strong></td><td>Content creation &mdash; doesn't come naturally, will outsource</td></tr>
<tr><td><strong>Energy profile</strong></td><td>Ambivert &mdash; people-time is enjoyed but draining; needs recovery</td></tr>
<tr><td><strong>Tech fluency</strong></td><td>Functional &mdash; can follow setup guides, won't build from scratch</td></tr>
<tr><td><strong>Sales motion</strong></td><td>Relationship-led closer (not a cold hunter); partnership-fed</td></tr>
<tr><td><strong>Network density</strong></td><td>Strong in Thornhill/Toronto Jewish community; planners, brokers, real estate already in network</td></tr>
<tr><td><strong>Comfort with public profile</strong></td><td>Will be on camera if revenue requires; prefers behind-the-scenes</td></tr>
</tbody>
</table>

<h2>What You Want</h2>
<table>
<tbody>
<tr><td><strong>Real motivation</strong></td><td>Build something I own. Ownership of an asset matters more than the income from it.</td></tr>
<tr><td><strong>End-state preference</strong></td><td>Hybrid &mdash; decide at Y4 based on circumstances</td></tr>
<tr><td><strong>Y5 lifestyle picture</strong></td><td>High-touch operator &mdash; busy, in-demand, running the room</td></tr>
<tr><td><strong>Team appetite</strong></td><td>Open, depends on people &mdash; not forced, opportunistic</td></tr>
<tr><td><strong>Brand framing</strong></td><td>Personal first, transition to agency brand by Y3</td></tr>
<tr><td><strong>Geographic intent</strong></td><td>Toronto if partnered (likely); nomadic if not</td></tr>
<tr><td><strong>Family timing</strong></td><td>3&ndash;5 years out &mdash; full grind window through Y3</td></tr>
</tbody>
</table>

<h2>The Constraints You Carry</h2>
<table>
<tbody>
<tr><td><strong>Day job</strong></td><td>$100K base + $50K commission = $150K total this year</td></tr>
<tr><td><strong>Day-job contract</strong></td><td>Clean &mdash; no non-compete, no moonlighting restriction</td></tr>
<tr><td><strong>Personal burn</strong></td><td>~$5K/mo</td></tr>
<tr><td><strong>Savings runway</strong></td><td>Under 3 months &mdash; the binding financial constraint</td></tr>
<tr><td><strong>Travel CV</strong></td><td>Caribbean (deep), Europe (moderate), Buenos Aires extended stay incoming</td></tr>
<tr><td><strong>Luxury positioning</strong></td><td>Accessible-luxury weighted ($3&ndash;8K), with capacity for higher tiers</td></tr>
</tbody>
</table>

<h2>The Brand You Want</h2>
<div class="callout">
<p><strong>Voice:</strong> Playful, irreverent. Self-aware millennial. Memes allowed. Closest references: Mejuri, Away, Glossier. <em>Not</em> Aman, Belmond, Brownell.</p>
<p><strong>Visual:</strong> Cool modern minimal. Gallery whites, sharp blacks, restrained palette. <em>Not</em> the current Preface site direction (warm classic Cormorant Garamond / cream / burgundy).</p>
<p><strong>Specialty edge:</strong> <strong>All-inclusives.</strong> Personally stayed at 20+ properties across the Caribbean and Mexico &mdash; the strongest credential in your demographic. Generalist for everything else; the deep knowledge gets featured as a credibility marker, not as the brand identity (don't want to be pigeonholed into resort-only bookings).</p>
</div>
</section>

<!-- 04 UNIT ECONOMICS -->
<section>
<h1><span class="num">Section 04</span>Unit Economics &amp; The Math</h1>
<p class="section-intro">Same math as v1, restated with your blended mix.</p>

<h2>Per-Booking Revenue</h2>
<table>
<thead>
<tr><th>Trip Type</th><th class="num">Avg Booking</th><th class="num">Commission %</th><th class="num">After Fora 30%</th><th class="num">Planning Fee</th><th class="num">Net to You</th></tr>
</thead>
<tbody>
<tr><td>Couples weekend</td><td class="num">$4,500</td><td class="num">11%</td><td class="num">$347</td><td class="num">$100</td><td class="num">$447</td></tr>
<tr><td>Family all-inclusive</td><td class="num">$7,000</td><td class="num">13%</td><td class="num">$637</td><td class="num">$150</td><td class="num">$787</td></tr>
<tr><td>Honeymoon (2-stop)</td><td class="num">$12,000</td><td class="num">12%</td><td class="num">$1,008</td><td class="num">$500</td><td class="num">$1,508</td></tr>
<tr><td>Bach weekend (10 pax)</td><td class="num">$14,000</td><td class="num">12%</td><td class="num">$1,176</td><td class="num">$500</td><td class="num">$1,676</td></tr>
<tr><td>Israel trip (family, 7 pax)</td><td class="num">$22,000</td><td class="num">10%</td><td class="num">$1,540</td><td class="num">$750</td><td class="num">$2,290</td></tr>
<tr><td>Bar/Bat mitzvah trip (12 pax)</td><td class="num">$35,000</td><td class="num">11%</td><td class="num">$2,695</td><td class="num">$1,500</td><td class="num">$4,195</td></tr>
<tr><td>Milestone group (15 pax)</td><td class="num">$60,000</td><td class="num">12%</td><td class="num">$5,040</td><td class="num">$2,500</td><td class="num">$7,540</td></tr>
<tr><td><strong>Blended Average (V2 Mix)</strong></td><td class="num"></td><td class="num"></td><td class="num"></td><td class="num"></td><td class="num"><strong>$820</strong></td></tr>
</tbody>
</table>
<p class="small">V2 blended average is higher than V1 ($820 vs $700) because the Thornhill wedge produces a meaningfully higher share of Israel trips, bar/bat mitzvahs, and milestone groups &mdash; all high-value bookings. Y1 mix expectation: 25% couples / 18% family / 15% honeymoon / 15% bach / 12% Jewish-community-specific (Israel + bar/bat mitzvah) / 5% milestone / 10% adjacent (babymoon, anniversary, etc).</p>

<h2>Income Ladder &mdash; Bookings Required</h2>
<table>
<thead><tr><th>Tier</th><th class="num">Monthly Net</th><th class="num">Bookings/mo</th><th class="num">Bookings/wk</th><th>Phase Hit</th></tr></thead>
<tbody>
<tr><td>Comfortable</td><td class="num">$15K</td><td class="num">~18</td><td class="num">~4.5</td><td>Y1 Q4</td></tr>
<tr><td>Wanted</td><td class="num">$25K</td><td class="num">~30</td><td class="num">~7.5</td><td>Y2 H2</td></tr>
<tr><td>Target</td><td class="num">$35K</td><td class="num">~43</td><td class="num">~11</td><td>Y3 with team</td></tr>
<tr><td>Goal</td><td class="num">$80K</td><td class="num">~98</td><td class="num">~24</td><td>Y5&ndash;Y6 with full team</td></tr>
<tr><td>Ultimate</td><td class="num">$250K</td><td class="num">~305</td><td class="num">~76</td><td>Y8&ndash;Y10 OR exit equivalent</td></tr>
</tbody>
</table>
<p>At ~10 bookings/wk you're at solo capacity. Anything beyond requires sub-advisors.</p>
</section>

<!-- 05 MARKET POSITION -->
<section>
<h1><span class="num">Section 05</span>Market Position &mdash; The Thornhill Wedge</h1>
<p class="section-intro">Where you start, how you expand, and what makes the trajectory defensible.</p>

<h2>The Wedge: Toronto/Thornhill Jewish Community</h2>
<p>This is your unfair advantage. The Thornhill Jewish community is:</p>
<ul>
<li><strong>Dense.</strong> Tight social network &mdash; everyone knows everyone within 1&ndash;2 degrees. Word of mouth moves fast.</li>
<li><strong>Affluent.</strong> One of the highest-income postal-code clusters in Canada. Discretionary travel spend is normal, not luxury.</li>
<li><strong>Family-oriented.</strong> Multi-generational trip planning is cultural baseline.</li>
<li><strong>Segment-perfect.</strong> Annual family vacations, bar/bat mitzvah travel, Israel pilgrimages, milestone celebrations, bach trips for engaged peers &mdash; all in your wheelhouse.</li>
<li><strong>Underserved.</strong> No advisor practice currently owns this community at the millennial level.</li>
</ul>

<h2>The Strategic Frame: Wedge, Not Brand</h2>
<p>Brand publicly as <strong>&ldquo;Preface &mdash; the millennial travel agency.&rdquo;</strong> Operate Y1&ndash;Y2 from the Thornhill community network. Don't brand around Jewish identity &mdash; that limits TAM &mdash; but don't ignore the unfair advantage either. The pattern works across consumer businesses:</p>
<table>
<thead><tr><th>Brand</th><th>Wedge</th><th>Final Position</th></tr></thead>
<tbody>
<tr><td>Casper</td><td>NYC tech early adopters</td><td>National DTC mattress brand</td></tr>
<tr><td>Allbirds</td><td>SF tech bros (2016&ndash;17)</td><td>Global sustainable footwear</td></tr>
<tr><td>Mejuri</td><td>Toronto millennial women</td><td>Global fine jewelry DTC</td></tr>
<tr><td>Liquid Death</td><td>Metal / skater community</td><td>National lifestyle beverage</td></tr>
<tr><td>Preface (you)</td><td>Toronto Jewish millennial community</td><td>National millennial travel agency</td></tr>
</tbody>
</table>

<h2>Expansion Sequence</h2>
<ol>
<li><strong>Y1.</strong> Thornhill / Toronto Jewish community + their first-degree connections. ~50&ndash;100 clients.</li>
<li><strong>Y2.</strong> Broader Toronto millennials + first US clients via referral and content. ~200 clients.</li>
<li><strong>Y3.</strong> National (Canada-wide) + select US metros via partnerships. ~400 clients across team.</li>
<li><strong>Y4&ndash;Y5.</strong> Brand recognition crosses tipping point; inbound becomes meaningful share of volume.</li>
</ol>

<h2>The Five Segments + Thornhill Add-Ons</h2>
<table>
<thead><tr><th>Segment</th><th>Trigger</th><th class="num">Avg Booking</th><th class="num">Thornhill Boost?</th></tr></thead>
<tbody>
<tr><td>Couples annual</td><td>Planning January window</td><td class="num">$4,500</td><td class="num">Baseline</td></tr>
<tr><td>Family school-break</td><td>Spring / Pesach / winter break</td><td class="num">$7,000</td><td class="num">+30% (Pesach trips)</td></tr>
<tr><td>Honeymoon</td><td>Engagement</td><td class="num">$12,000</td><td class="num">Baseline</td></tr>
<tr><td>Bach / Bachelorette</td><td>Engagement &rarr; 4&ndash;8 mo out</td><td class="num">$14,000 group</td><td class="num">+40% (frequency)</td></tr>
<tr><td>Milestone group</td><td>40th / 50th / parents' anniversary</td><td class="num">$60,000 group</td><td class="num">+50% (Israel + family)</td></tr>
<tr><td><strong>Israel pilgrimage / family</strong></td><td>Bar/bat mitzvah, milestones, holidays</td><td class="num">$22,000</td><td class="num"><strong>Wedge-specific</strong></td></tr>
<tr><td><strong>Bar/Bat mitzvah travel</strong></td><td>Age 12&ndash;13 milestone</td><td class="num">$35,000</td><td class="num"><strong>Wedge-specific</strong></td></tr>
<tr><td>Babymoon / anniversary / reunion</td><td>Life moments</td><td class="num">$4&ndash;8K</td><td class="num">Baseline</td></tr>
</tbody>
</table>

<div class="callout gold">
    <h4>The Calendar Edge</h4>
    <p>The Thornhill wedge gives you a predictable annual calendar your competitors don't have visibility into: Pesach (March&ndash;April) family trips, bar/bat mitzvah season (October&ndash;June), summer Israel travel, High Holiday adjacencies. Build content + outreach campaigns around this calendar from Y1.</p>
</div>
</section>

<!-- 06 SIX HORIZON PLAN -->
<section>
<h1><span class="num">Section 06</span>The Six-Horizon Plan</h1>
<p class="section-intro">Same six horizons as v1, rebuilt around the network-first thesis and the day-job constraint.</p>

<!-- 6.1 -->
<div class="phase-banner">
    <div class="phase-num">Phase 6.1  ·  Month 1</div>
    <div class="phase-title">Foundation</div>
    <div class="phase-sub">Get licensed, get launched, tap your warm network. Day job continues.</div>
</div>

<h3>Objective</h3>
<p>Be legally able to sell travel by week 3. Close 5&ndash;8 bookings from your warm network. Day job continues at full intensity &mdash; this is supplemental.</p>

<h3>Hard Deliverables</h3>
<ul class="check-list">
<li>TICO Certification Program purchased ($150) &mdash; week 1</li>
<li>Fora Canada application submitted &mdash; week 1</li>
<li>TICO exam passed &mdash; by week 3</li>
<li>Business domain + Google Workspace email (yourname@preface.travel)</li>
<li>Calendly + Tally intake form configured</li>
<li>Social handles secured (@preface.travel)</li>
<li>Site live by week 3 (existing v2 mockups deployed; brand rework comes later)</li>
<li>Warm-network list built: <strong>not 50, but 150</strong> &mdash; everyone in your phone in the 28&ndash;45 demo + parents' generation peers + planner/broker/agent contacts</li>
<li>5&ndash;8 bookings closed by end of month from this list</li>
</ul>

<h3>Month 1 KPIs</h3>
<div class="kpi-row">
    <div class="kpi"><div class="lab">Licensed</div><div class="val">Yes</div><div class="sub">TICO + Fora</div></div>
    <div class="kpi"><div class="lab">Bookings</div><div class="val">5&ndash;8</div><div class="sub">Warm network</div></div>
    <div class="kpi"><div class="lab">Revenue</div><div class="val">$3&ndash;6K</div><div class="sub">Net commission</div></div>
    <div class="kpi"><div class="lab">Day job</div><div class="val">Full</div><div class="sub">No reduction</div></div>
</div>

<div class="callout warn">
    <h4>The Failure Mode</h4>
    <p>TICO study deprioritized OR network outreach done as group blast instead of 1-to-1 messages. The dense network expects personal contact. Generic announcements convert poorly.</p>
</div>

<!-- 6.2 -->
<div class="phase-banner">
    <div class="phase-num">Phase 6.2  ·  Months 2&ndash;3</div>
    <div class="phase-title">Activate the Network</div>
    <div class="phase-sub">In-person coffees, partnership formalization, the Thornhill wedge in motion.</div>
</div>

<h3>Objective</h3>
<p>Convert your existing relational density into a referral engine. Sign 3&ndash;5 partnership agreements. Lay the technical groundwork for a cold-outreach engine that will run in the background from month 4.</p>

<h3>Hard Deliverables</h3>
<ul class="check-list">
<li><strong>20 in-person coffees</strong> with people in your network &mdash; wedding planners, real estate agents, mortgage brokers, photographers, venue managers, hotel reps, anyone influential</li>
<li>3&ndash;5 partnership agreements signed: 25% commission share, paid quarterly, no quota</li>
<li>Cold outreach infrastructure built (Instantly + Apollo) &mdash; <strong>contractor wires it up</strong>, you don't</li>
<li>Sequences drafted (US-only): wedding planners, real estate agents</li>
<li>Soft launch: 200 emails/day going out, hands-off</li>
<li>VA hire begins recruitment (Philippines or LatAm, $10&ndash;15/hr)</li>
<li>Newsletter live on Beehiiv; biweekly cadence (not weekly &mdash; sustainable for ambivert)</li>
<li>Continuing 20&ndash;30 client conversations from M1 warm-network leads</li>
</ul>

<h3>Month 3 KPIs</h3>
<div class="kpi-row">
    <div class="kpi"><div class="lab">Lifetime Clients</div><div class="val">25&ndash;35</div><div class="sub">Mostly Thornhill</div></div>
    <div class="kpi"><div class="lab">Monthly Revenue</div><div class="val">$6&ndash;9K</div><div class="sub">Net</div></div>
    <div class="kpi"><div class="lab">Partnerships</div><div class="val">3&ndash;5</div><div class="sub">Formal agreements</div></div>
    <div class="kpi"><div class="lab">VA Hired</div><div class="val">Yes</div><div class="sub">Onboarded by week 11</li></div></div>
</div>

<!-- 6.3 -->
<div class="phase-banner">
    <div class="phase-num">Phase 6.3  ·  Months 4&ndash;6</div>
    <div class="phase-title">Outsource &amp; Automate</div>
    <div class="phase-sub">Content production handed off. Cold engine runs in background. You focus on close + partnerships.</div>
</div>

<h3>Objective</h3>
<p>Hit <strong>consistent $1,500/wk net commissions</strong> by week 24. Hand off all repeatable work to VAs/contractors so your hours focus on what only you can do: closing calls and partnership relationships.</p>

<h3>The Outsourcing Architecture</h3>
<table>
<thead><tr><th>Function</th><th>Owner</th><th>Cost/mo</th><th>Your Time</th></tr></thead>
<tbody>
<tr><td>Cold outreach reply triage</td><td>VA (Philippines)</td><td>$300</td><td>0 hrs</td></tr>
<tr><td>Lead list cleaning + enrichment</td><td>VA</td><td>(included)</td><td>0 hrs</td></tr>
<tr><td>Newsletter writing + scheduling</td><td>Content VA (Toronto / Buenos Aires)</td><td>$1,200</td><td>30 min/wk dictation</td></tr>
<tr><td>Social posts (IG / TikTok / LinkedIn)</td><td>Content VA</td><td>(included)</td><td>30 min/wk dictation</td></tr>
<tr><td>Reels / TikTok editing</td><td>Content VA</td><td>(included)</td><td>You record raw clips weekly</td></tr>
<tr><td>Bookkeeping</td><td>Accountant + bookkeeper</td><td>$200</td><td>0 hrs</td></tr>
<tr><td>Admin / scheduling / inbox</td><td>Same VA as outreach</td><td>(included)</td><td>0.5 hr/day review</td></tr>
<tr><td><strong>Your time stays on</strong></td><td colspan="3">Client calls, partnership meetings, supplier relationships, strategic direction</td></tr>
</tbody>
</table>

<h3>The Day-Job-Continues Reality</h3>
<p>You're still working the day job through this entire phase. Day job stays through month 15&ndash;18 minimum because of the runway constraint. This phase optimizes your business activity to fit inside ~25 hrs/wk of extracted time.</p>

<h3>Month 6 KPIs</h3>
<div class="kpi-row">
    <div class="kpi"><div class="lab">Monthly Revenue</div><div class="val">$7&ndash;11K</div><div class="sub">Net</div></div>
    <div class="kpi"><div class="lab">Weekly Average</div><div class="val">$1.5K+</div><div class="sub">Consistent</div></div>
    <div class="kpi"><div class="lab">Partnerships</div><div class="val">8&ndash;10</div><div class="sub">Active sources</div></div>
    <div class="kpi"><div class="lab">VA Cost</div><div class="val">$1,500/mo</div><div class="sub">Producing leverage</div></div>
</div>

<!-- 6.4 -->
<div class="phase-banner">
    <div class="phase-num">Phase 6.4  ·  Months 7&ndash;12</div>
    <div class="phase-title">Year 1 &mdash; Hit $2,500/wk by Day 300</div>
    <div class="phase-sub">Day job stays. Business compounds. Runway builds.</div>
</div>

<h3>Objective</h3>
<p>Average <strong>$2,500/wk</strong> by week 43 (day 300). End Y1 with $100K+ commission revenue + accumulated runway. Quit only when both conditions are met: business consistent at target AND 6 months of savings stored.</p>

<h3>The Dual Quit Trigger</h3>
<div class="callout">
<h4>Required for quitting day job</h4>
<ol>
<li><strong>Business condition:</strong> $2,500/wk net commissions for 8 consecutive weeks</li>
<li><strong>Runway condition:</strong> 6 months of personal expenses ($30K) saved separately</li>
</ol>
<p>BOTH conditions, not either. The runway exists because Y1 business income is volatile &mdash; a slow quarter can take you back to $1K/wk for 6&ndash;8 weeks. The savings absorb that. Without them, you'd be forced back into job-hunting at exactly the wrong moment.</p>
</div>

<h3>Y1 Financial Picture (Day-Job-Continues Scenario)</h3>
<table>
<thead><tr><th>Line item</th><th class="num">Annual</th></tr></thead>
<tbody>
<tr><td>Day-job income (full year)</td><td class="num">$150K</td></tr>
<tr><td>Business gross commission</td><td class="num">$90&ndash;130K</td></tr>
<tr><td>Less: Fora 30% cut</td><td class="num">($27&ndash;39K)</td></tr>
<tr><td>Plus: planning fees</td><td class="num">$18&ndash;25K</td></tr>
<tr><td>Business net before tax</td><td class="num">$81&ndash;116K</td></tr>
<tr><td>Less: opex (tools, VAs, content)</td><td class="num">($15&ndash;20K)</td></tr>
<tr><td><strong>Total household pre-tax income</strong></td><td class="num"><strong>$216&ndash;246K</strong></td></tr>
<tr><td><strong>After-tax (incorporated, optimized)</strong></td><td class="num"><strong>~$155&ndash;175K take-home</strong></td></tr>
<tr><td><strong>Savings buildup (above $5K/mo burn)</strong></td><td class="num"><strong>~$95&ndash;115K saved by Y1 end</strong></td></tr>
</tbody>
</table>

<p>This is the math that makes V2 so much better than V1. <strong>You don't have to choose between &ldquo;quit early and run lean&rdquo; vs &ldquo;stay forever.&rdquo;</strong> Day job + business in parallel for 12&ndash;18 months produces ~$100K of pure savings while the business proves itself. Quit when both signals are green.</p>

<h3>Quarterly Pacing</h3>
<table>
<thead><tr><th>Quarter</th><th>Months</th><th class="num">Target Revenue</th><th>Defining Activity</th></tr></thead>
<tbody>
<tr><td>Q1</td><td>1&ndash;3</td><td class="num">$8&ndash;18K</td><td>Foundation + warm-network activation</td></tr>
<tr><td>Q2</td><td>4&ndash;6</td><td class="num">$20&ndash;30K</td><td>VA-supported scale; first content compounding</td></tr>
<tr><td>Q3</td><td>7&ndash;9</td><td class="num">$28&ndash;42K</td><td>Acceleration; $2K&ndash;$2.5K/wk run-rate</td></tr>
<tr><td>Q4</td><td>10&ndash;12</td><td class="num">$35&ndash;55K</td><td>$2,500/wk locked in by day 300</td></tr>
</tbody>
</table>

<!-- 6.5 -->
<div class="phase-banner">
    <div class="phase-num">Phase 6.5  ·  Year 3</div>
    <div class="phase-title">Amplification, Not Replacement</div>
    <div class="phase-sub">Hire to extend your reach, not to step back from the room.</div>
</div>

<h3>The Reframed Y3 Picture</h3>
<p>Standard playbook says: hire so you can do less. <strong>Your playbook says: hire so you can do more, but at higher leverage.</strong> You stay client-facing and partnership-facing &mdash; the work you love. Sub-advisors take the lower-touch trips (couples weekends, smaller honeymoons) so your time goes to the high-trust, high-revenue work (Israel family pilgrimages, multi-gen milestones, bar/bat mitzvah travel).</p>

<h3>The Y3 Team Shape</h3>
<table>
<thead><tr><th>Role</th><th>Hired By</th><th>Type</th><th>Override / Cost</th></tr></thead>
<tbody>
<tr><td>Junior advisor #1</td><td>Month 18&ndash;20</td><td>Fora team-leader sub</td><td>25% override on her bookings</td></tr>
<tr><td>Junior advisor #2</td><td>Month 24&ndash;28</td><td>Fora team-leader sub</td><td>25% override</td></tr>
<tr><td>Operations / client services lead</td><td>Month 30</td><td>FTE or 0.8 FTE contractor</td><td>$60&ndash;80K/yr</td></tr>
<tr><td>Content lead (replacing VA)</td><td>Month 30</td><td>0.5 FTE contractor</td><td>$30&ndash;40K/yr</td></tr>
<tr><td>Junior advisor #3 (optional)</td><td>Month 32&ndash;36</td><td>Fora team-leader sub</td><td>25% override</td></tr>
</tbody>
</table>

<h3>Y3 Financial Picture</h3>
<table>
<tbody>
<tr><td>Your personal bookings (capped at solo capacity)</td><td class="num">$300K commission</td></tr>
<tr><td>Team commissions (2&ndash;3 sub-advisors)</td><td class="num">$300&ndash;500K</td></tr>
<tr><td>Your override (25% of team)</td><td class="num">$75&ndash;125K</td></tr>
<tr><td>Total revenue across team</td><td class="num">$600&ndash;800K</td></tr>
<tr><td><strong>Your personal income (incorporated)</strong></td><td class="num"><strong>$280&ndash;350K take-home</strong></td></tr>
</tbody>
</table>
<p>This hits Tier 3 (target = $35K/mo = $420K/yr gross &asymp; $280K take-home incorporated).</p>

<!-- 6.6 -->
<div class="phase-banner">
    <div class="phase-num">Phase 6.6  ·  Year 5</div>
    <div class="phase-title">Two Paths Surface</div>
    <div class="phase-sub">Operator lifestyle or exit candidate. You don't have to decide yet, but you do have to know.</div>
</div>

<h3>Path A &mdash; Operator Lifestyle (your stated preference)</h3>
<ul>
<li>5&ndash;8 sub-advisors</li>
<li>$1.5&ndash;3M total agency commission revenue</li>
<li><strong>Personal income: $400&ndash;650K/yr</strong> (your bookings + team override)</li>
<li>You stay in the action: client closes, partnership meetings, supplier relationships</li>
<li>35&ndash;45 hour weeks (matches the &ldquo;busy and important&rdquo; lifestyle picture)</li>
<li>No exit; recurring income for as long as you want to run it</li>
<li>Real wealth comes from compounding personal income across 10+ years</li>
</ul>

<h3>Path B &mdash; Exit Candidate (your &ldquo;build something I own&rdquo; motivation)</h3>
<ul>
<li>12&ndash;20 advisors</li>
<li>$4&ndash;8M total agency revenue</li>
<li><strong>Personal income (pre-exit): $300&ndash;500K/yr</strong></li>
<li>EBITDA margin: 25&ndash;35% &rarr; $1&ndash;2.8M</li>
<li>Multiple: 3&ndash;6x &rarr; <strong>$3&ndash;16M sale value</strong></li>
<li>Likely acquirers: Internova (Travel Edge in Canada), Virtuoso member firms, PE roll-up funds</li>
<li>Requires founder to step back &mdash; brand strong enough to run without you</li>
</ul>

<h3>The Hard Trade-Off</h3>
<div class="callout warn">
<h4>What Path B Requires That You Said You Don't Want</h4>
<p>You said Y5 lifestyle = &ldquo;high-touch operator, busy and important.&rdquo; Path B requires the opposite: founder steps back, business runs without you, acquirer trusts the team and the brand. Path B preserves the option to be busy and important <em>after</em> the sale &mdash; you can stay on as CEO of the acquired business for 2&ndash;3 years of earnout &mdash; but during years 3&ndash;5 you have to deliberately reduce founder centrality. That's the cost of optionality.</p>
<p><strong>The honest read:</strong> based on your answers, Path A is the natural fit. Path B is achievable but requires real discipline in years 3&ndash;5 to scaffold the business away from you. Decide at year 4.</p>
</div>
</section>

<!-- 07 NETWORK-FIRST GROWTH -->
<section>
<h1><span class="num">Section 07</span>The Network-First Growth Engine</h1>
<p class="section-intro">Cold outreach matters, but it's the second engine. Your existing network is the first.</p>

<h2>The Three Lead Sources, Weighted For You</h2>
<table>
<thead><tr><th>Source</th><th>Y1 Share</th><th>Y3 Share</th><th>Your Time</th></tr></thead>
<tbody>
<tr><td>Warm network + referrals (Thornhill density)</td><td class="num">60%</td><td class="num">35%</td><td>Heavy &mdash; the work you love</td></tr>
<tr><td>Cold outreach (US partnerships + B2C)</td><td class="num">25%</td><td class="num">35%</td><td>Minimal &mdash; runs in background</td></tr>
<tr><td>Content + inbound</td><td class="num">15%</td><td class="num">30%</td><td>30 min/wk dictation</td></tr>
</tbody>
</table>

<h2>Network Activation Sequence (Months 1&ndash;3)</h2>
<h3>Step 1: Map the 150</h3>
<p>Not the standard 50. Build a 150-person sheet covering:</p>
<ul>
<li>Friends 28&ndash;45 (your peers, partnered, traveling)</li>
<li>Family / parents' peer cohort (40&ndash;65, milestone trip planners)</li>
<li>Service providers you know: wedding planners, real estate agents, mortgage brokers, photographers, venues, caterers, jewelers, dress shops</li>
<li>Community leaders: rabbis, school directors, charity board members</li>
<li>Anyone you'd trust to vouch for you</li>
</ul>

<h3>Step 2: The Sequence</h3>
<ol>
<li><strong>Week 1:</strong> Personal 1-to-1 text to first 50 (you, voice memo or short message)</li>
<li><strong>Week 2:</strong> Next 50</li>
<li><strong>Week 3:</strong> Final 50</li>
<li><strong>Week 4:</strong> Follow up with non-responders (~50% of total)</li>
</ol>
<p>Expected output from a 150-person list with a dense Toronto community: 8&ndash;15 bookings in first 60 days + 5&ndash;10 partnership conversations opened.</p>

<h2>The Sample Network Message</h2>
<div class="email-template">
<div class="meta">CONTEXT: 1-TO-1 PERSONAL TEXT, NOT EMAIL BLAST</div>
<div class="body">Hey [Name] &mdash; just wanted to share something I'm doing on the side. I got my travel-advisor license through Fora (the millennial-focused agency) &mdash; I'm now booking trips for friends and family, with the supplier paying the commission, so it doesn't cost you anything but you get upgrades, breakfast, hotel credits, the stuff you can't get on Expedia.

I'm focused on honeymoons, bach trips, family vacations, and Israel/milestone group travel. Thought of you because [specific reason &mdash; their upcoming trip, engagement, family situation].

No pressure &mdash; if you've already got a trip planned this year, I'd love to be on your list for the next one. If something's brewing, want to grab a coffee?</div>
</div>

<h2>The Partnership Activation Plan (Toronto)</h2>
<p>Schedule 20 coffees with the planners, brokers, and agents in your network in months 2&ndash;3.</p>

<table>
<thead><tr><th>Partner Type</th><th>Density in Your Network</th><th>Target Coffees</th></tr></thead>
<tbody>
<tr><td>Wedding planners (Jewish weddings, kosher catering, etc)</td><td>High</td><td class="num">5&ndash;6</td></tr>
<tr><td>Real estate agents (Thornhill / Forest Hill / Bayview)</td><td>High</td><td class="num">4&ndash;5</td></tr>
<tr><td>Mortgage brokers</td><td>Medium-high</td><td class="num">3</td></tr>
<tr><td>Photographers (engagement + wedding)</td><td>Medium</td><td class="num">3</td></tr>
<tr><td>Caterers / event venues</td><td>Medium</td><td class="num">2</td></tr>
<tr><td>Jewelry / bridal stylists</td><td>Low</td><td class="num">2</td></tr>
<tr><td><strong>Total in months 2&ndash;3</strong></td><td></td><td class="num"><strong>~20</strong></td></tr>
</tbody>
</table>

<h2>The Cold Outreach Engine (Background, US-Only)</h2>
<p>The full cold-outreach playbook from V1 still runs, but it's a <strong>set-and-forget background system</strong>, not your primary activity. A contractor wires it up in month 2; VA handles reply triage from month 4.</p>
<ul>
<li>Volume by month 6: 1,500 emails/day to US wedding planners + real estate + B2C engaged couples</li>
<li>Sequences from V1 stay (Sections 7.1&ndash;7.3 in V1)</li>
<li><strong>Your time on cold:</strong> 0 hrs/wk after initial setup</li>
<li><strong>Expected output:</strong> 5&ndash;8 incremental bookings/month by Y1 end, +20% to total revenue</li>
</ul>

<div class="callout gold">
    <h4>On Paying Referral Fees to Financial Advisors</h4>
    <p>You asked: can you pay financial advisors a commission for referrals? <strong>Travel-advisor referral fees are not securities-regulated</strong> &mdash; legally fine. The practical catch: most FAs' compliance departments forbid them from accepting outside compensation. <strong>Workaround:</strong> instead of cash, gift dinner at Donalda, a Marriott hotel stay, or a charity donation in their name. Same economic value. No compliance flag for them. Frame it as "client-appreciation gifting" rather than "referral fee." This is how the wealth-advisor channel actually works in practice.</p>
</div>
</section>

<!-- 08 CONTENT STRATEGY -->
<section>
<h1><span class="num">Section 08</span>The Outsourced Content Strategy</h1>
<p class="section-intro">You're not a content creator. You're a person who has interesting client conversations. The VA turns those into content.</p>

<h2>The Production Model</h2>
<table>
<thead><tr><th>Step</th><th>Owner</th><th>Time</th></tr></thead>
<tbody>
<tr><td>1. You finish a client call and record a 3-min voice memo on what was interesting</td><td>You</td><td>3 min</td></tr>
<tr><td>2. You forward 1&ndash;2 client photos (after trip) with 1-line context</td><td>You</td><td>1 min</td></tr>
<tr><td>3. VA transcribes voice memo, identifies content angle, drafts post</td><td>Content VA</td><td>~45 min</td></tr>
<tr><td>4. VA writes 1 newsletter post + 2 IG posts + 1 TikTok script + 1 LinkedIn post (from your voice memo content)</td><td>Content VA</td><td>~3 hrs</td></tr>
<tr><td>5. You review weekly batch (Friday), make 5&ndash;10 word edits, approve</td><td>You</td><td>30 min/wk</td></tr>
<tr><td>6. VA schedules and publishes</td><td>Content VA</td><td>~1 hr</td></tr>
<tr><td><strong>Your total weekly content time</strong></td><td colspan="2"><strong>~45 min</strong></td></tr>
</tbody>
</table>

<h2>The Voice You Want vs. the Reality of Outsourcing</h2>
<p>You said: <em>&ldquo;Playful / irreverent.&rdquo;</em> Most content VAs default to generic corporate-friendly travel agency tone. To get the playful voice, you need to either:</p>
<ol>
<li><strong>Pay more for a Toronto-based content contractor</strong> ($1,500&ndash;2,500/mo) who can write in your voice after a few weeks of calibration; or</li>
<li><strong>Use a cheaper Philippines VA for production + a Toronto editor</strong> at $50&ndash;75/post to inject voice into the top 5&ndash;6 posts per month that matter most.</li>
</ol>
<p><strong>Recommendation for V2:</strong> Option 2 from M4&ndash;M9. Option 1 from M10 onward if Y1 is hitting targets.</p>

<h2>The Five Content Pillars (Voice-Adjusted)</h2>
<table>
<thead><tr><th>Pillar</th><th>Voice-Right Hook</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Math</strong></td><td>&ldquo;Here's what your $8K Expedia booking cost you in upgrades you didn't get&rdquo;</td><td>1x/wk LinkedIn + IG</td></tr>
<tr><td><strong>The Receipt</strong></td><td>Screenshot of an actual upgrade with caption: &ldquo;She paid $5K. They gave her the $12K suite. This is what we do.&rdquo;</td><td>2x/wk IG story</td></tr>
<tr><td><strong>The Hot Take</strong></td><td>&ldquo;Sandals is mid. Here are 3 all-inclusives that aren't.&rdquo;</td><td>1x/wk TikTok</td></tr>
<tr><td><strong>The Insider</strong></td><td>&ldquo;The Aman Tokyo room they don't show on the website&rdquo;</td><td>1x/wk newsletter</td></tr>
<tr><td><strong>The Story</strong></td><td>Client trip recap (real names with permission)</td><td>1x/biweekly newsletter</td></tr>
</tbody>
</table>

<h2>Newsletter as the Primary Content Asset</h2>
<p>Biweekly (not weekly &mdash; sustainable). 1,200&ndash;1,500 words. Format: one insider tip + one client story + one travel deal. Build to 5K subs by Y2 end. Paid tier ($10/mo) launches at 5K subs &mdash; templates, exclusive deals, monthly Q&amp;A call. Target 2% paid conversion = $1K/mo MRR by Y2 H2.</p>
</section>

<!-- 09 FINANCIAL PROJECTIONS -->
<section>
<h1><span class="num">Section 09</span>Financial Projections (Your Income Tiers)</h1>
<p class="section-intro">Projection paths to each of your stated income tiers.</p>

<h2>Year 1 &mdash; Monthly P&amp;L (Day-Job-Continues Scenario)</h2>
<table>
<thead><tr><th>Month</th><th class="num">Bookings</th><th class="num">Gross</th><th class="num">Net After Fora</th><th class="num">Fees</th><th class="num">Opex</th><th class="num">Business Net</th><th class="num">Day Job Net</th><th class="num">Total Take-Home</th></tr></thead>
<tbody>
<tr><td>M1</td><td class="num">6</td><td class="num">$3.2K</td><td class="num">$2.2K</td><td class="num">$600</td><td class="num">($1.0K)</td><td class="num">$1.8K</td><td class="num">$8.7K</td><td class="num">$10.5K</td></tr>
<tr><td>M2</td><td class="num">9</td><td class="num">$5.1K</td><td class="num">$3.6K</td><td class="num">$900</td><td class="num">($0.3K)</td><td class="num">$4.2K</td><td class="num">$8.7K</td><td class="num">$12.9K</td></tr>
<tr><td>M3</td><td class="num">11</td><td class="num">$6.5K</td><td class="num">$4.6K</td><td class="num">$1.1K</td><td class="num">($0.3K)</td><td class="num">$5.4K</td><td class="num">$8.7K</td><td class="num">$14.1K</td></tr>
<tr><td>M4</td><td class="num">13</td><td class="num">$8.0K</td><td class="num">$5.6K</td><td class="num">$1.4K</td><td class="num">($1.5K)</td><td class="num">$5.5K</td><td class="num">$8.7K</td><td class="num">$14.2K</td></tr>
<tr><td>M5</td><td class="num">15</td><td class="num">$9.3K</td><td class="num">$6.5K</td><td class="num">$1.6K</td><td class="num">($1.7K)</td><td class="num">$6.4K</td><td class="num">$8.7K</td><td class="num">$15.1K</td></tr>
<tr><td>M6</td><td class="num">17</td><td class="num">$10.8K</td><td class="num">$7.6K</td><td class="num">$1.8K</td><td class="num">($1.7K)</td><td class="num">$7.7K</td><td class="num">$8.7K</td><td class="num">$16.4K</td></tr>
<tr><td>M7</td><td class="num">18</td><td class="num">$12.1K</td><td class="num">$8.5K</td><td class="num">$2.0K</td><td class="num">($1.8K)</td><td class="num">$8.7K</td><td class="num">$8.7K</td><td class="num">$17.4K</td></tr>
<tr><td>M8</td><td class="num">19</td><td class="num">$13.5K</td><td class="num">$9.5K</td><td class="num">$2.2K</td><td class="num">($1.8K)</td><td class="num">$9.9K</td><td class="num">$8.7K</td><td class="num">$18.6K</td></tr>
<tr><td>M9</td><td class="num">20</td><td class="num">$14.8K</td><td class="num">$10.4K</td><td class="num">$2.4K</td><td class="num">($1.8K)</td><td class="num">$11.0K</td><td class="num">$8.7K</td><td class="num">$19.7K</td></tr>
<tr><td>M10</td><td class="num">22</td><td class="num">$16.3K</td><td class="num">$11.4K</td><td class="num">$2.6K</td><td class="num">($1.9K)</td><td class="num">$12.1K</td><td class="num">$8.7K</td><td class="num">$20.8K</td></tr>
<tr><td>M11</td><td class="num">23</td><td class="num">$17.7K</td><td class="num">$12.4K</td><td class="num">$2.9K</td><td class="num">($1.9K)</td><td class="num">$13.4K</td><td class="num">$8.7K</td><td class="num">$22.1K</td></tr>
<tr><td>M12</td><td class="num">25</td><td class="num">$19.2K</td><td class="num">$13.4K</td><td class="num">$3.1K</td><td class="num">($1.9K)</td><td class="num">$14.6K</td><td class="num">$8.7K</td><td class="num">$23.3K</td></tr>
<tr><td><strong>Y1</strong></td><td class="num"><strong>198</strong></td><td class="num"><strong>$136K</strong></td><td class="num"><strong>$95K</strong></td><td class="num"><strong>$23K</strong></td><td class="num"><strong>($16K)</strong></td><td class="num"><strong>$100K</strong></td><td class="num"><strong>$105K</strong></td><td class="num"><strong>$205K</strong></td></tr>
</tbody>
</table>

<p class="small">Day-job net assumed $105K take-home from $150K gross. With $5K/mo personal burn ($60K/yr), Y1 leaves <strong>~$145K of accumulated savings</strong> &mdash; enough to fund a safe day-job exit at month 13&ndash;15.</p>

<h2>Income Tier Achievement Timeline</h2>
<table>
<thead><tr><th>Tier</th><th class="num">Monthly Income</th><th class="num">Y/M Hit (Business Only)</th><th class="num">Combined w/ Day Job</th></tr></thead>
<tbody>
<tr><td>Tier 1 &mdash; Comfortable</td><td class="num">$15K</td><td class="num">Y2 M3</td><td class="num">Y1 M3 (with day job)</td></tr>
<tr><td>Tier 2 &mdash; Wanted</td><td class="num">$25K</td><td class="num">Y2 M9</td><td class="num">Y1 M6</td></tr>
<tr><td>Tier 3 &mdash; Target</td><td class="num">$35K</td><td class="num">Y3 (with team)</td><td class="num">Y2 (without team if day job continues)</td></tr>
<tr><td>Tier 4 &mdash; Goal</td><td class="num">$80K</td><td class="num">Y5 (full team)</td><td class="num">Y4 (with team + day-job-replacement-level commissions)</td></tr>
<tr><td>Tier 5 &mdash; Ultimate</td><td class="num">$250K</td><td class="num">Y7&ndash;Y10 OR exit-equivalent</td><td class="num">n/a</td></tr>
</tbody>
</table>

<h2>Years 2&ndash;5 Trajectory (Post-Day-Job)</h2>
<table>
<thead><tr><th></th><th class="num">Y2</th><th class="num">Y3</th><th class="num">Y4</th><th class="num">Y5</th></tr></thead>
<tbody>
<tr><td>Personal bookings</td><td class="num">320</td><td class="num">380</td><td class="num">380</td><td class="num">380</td></tr>
<tr><td>Team bookings</td><td class="num">0</td><td class="num">450</td><td class="num">1,100</td><td class="num">2,200</td></tr>
<tr><td>Personal gross commission</td><td class="num">$295K</td><td class="num">$370K</td><td class="num">$395K</td><td class="num">$415K</td></tr>
<tr><td>Team gross commission</td><td class="num">$0</td><td class="num">$420K</td><td class="num">$1.05M</td><td class="num">$2.1M</td></tr>
<tr><td>Your team override (25%)</td><td class="num">$0</td><td class="num">$105K</td><td class="num">$262K</td><td class="num">$525K</td></tr>
<tr><td>Planning fees + newsletter MRR</td><td class="num">$45K</td><td class="num">$80K</td><td class="num">$140K</td><td class="num">$220K</td></tr>
<tr><td>Less opex (team + tools + content + ops)</td><td class="num">($45K)</td><td class="num">($120K)</td><td class="num">($250K)</td><td class="num">($420K)</td></tr>
<tr><td><strong>Personal take-home (incorporated)</strong></td><td class="num"><strong>$185K</strong></td><td class="num"><strong>$295K</strong></td><td class="num"><strong>$410K</strong></td><td class="num"><strong>$540K</strong></td></tr>
<tr><td><strong>Monthly equivalent</strong></td><td class="num"><strong>$15K/mo</strong></td><td class="num"><strong>$25K/mo</strong></td><td class="num"><strong>$34K/mo</strong></td><td class="num"><strong>$45K/mo</strong></td></tr>
</tbody>
</table>

<p>Y5 personal take-home of $45K/mo gets you between Tier 3 ($35K target) and Tier 4 ($80K goal). Reaching the full Tier 4 requires either: (a) extending the team to 6&ndash;8 advisors (Y6&ndash;Y7) or (b) an exit producing equivalent annualized returns.</p>
</section>

<!-- 10 CAPITAL & TOOLING -->
<section>
<h1><span class="num">Section 10</span>Capital &amp; Tooling Plan</h1>
<p class="section-intro">Updated for VA-heavy content production and the contractor-built tech stack.</p>

<h2>Month 1 Setup Costs</h2>
<table>
<thead><tr><th>Item</th><th class="num">CAD</th></tr></thead>
<tbody>
<tr><td>TICO certification</td><td class="num">$150</td></tr>
<tr><td>Fora (1 yr)</td><td class="num">$410</td></tr>
<tr><td>Domain + Google Workspace (12 mo)</td><td class="num">$110</td></tr>
<tr><td>Website (existing v2 design deployed)</td><td class="num">$200</td></tr>
<tr><td>Ontario business name registration</td><td class="num">$60</td></tr>
<tr><td>Canva Pro (annual)</td><td class="num">$130</td></tr>
<tr><td>One-time tech setup contractor (cold email + Apollo + Beehiiv wiring)</td><td class="num">$800</td></tr>
<tr><td><strong>Total Month 1</strong></td><td class="num"><strong>~$1,860</strong></td></tr>
</tbody>
</table>

<h2>Recurring Opex by Phase (CAD)</h2>
<table>
<thead><tr><th>Tool / Function</th><th class="num">M2&ndash;M3</th><th class="num">M4&ndash;M6</th><th class="num">M7&ndash;M12</th><th class="num">Y2</th></tr></thead>
<tbody>
<tr><td>Cold email engine (Instantly)</td><td class="num">$100</td><td class="num">$140</td><td class="num">$200</td><td class="num">$300</td></tr>
<tr><td>Lead enrichment (Apollo)</td><td class="num">$80</td><td class="num">$100</td><td class="num">$130</td><td class="num">$200</td></tr>
<tr><td>Calendly Pro</td><td class="num">$16</td><td class="num">$16</td><td class="num">$16</td><td class="num">$16</td></tr>
<tr><td>Beehiiv</td><td class="num">$0</td><td class="num">$50</td><td class="num">$100</td><td class="num">$200</td></tr>
<tr><td>Canva Pro</td><td class="num">$13</td><td class="num">$13</td><td class="num">$13</td><td class="num">$13</td></tr>
<tr><td>VA (admin + reply triage)</td><td class="num">$0</td><td class="num">$400</td><td class="num">$650</td><td class="num">$1,500</td></tr>
<tr><td><strong>Content VA / contractor</strong></td><td class="num">$0</td><td class="num">$800</td><td class="num">$1,200</td><td class="num">$2,000</td></tr>
<tr><td>Toronto content editor (top posts)</td><td class="num">$0</td><td class="num">$250</td><td class="num">$400</td><td class="num">$600</td></tr>
<tr><td>Second sending domain</td><td class="num">$0</td><td class="num">$50</td><td class="num">$100</td><td class="num">$200</td></tr>
<tr><td>CRM (HubSpot Starter)</td><td class="num">$0</td><td class="num">$0</td><td class="num">$60</td><td class="num">$200</td></tr>
<tr><td>Bookkeeping</td><td class="num">$0</td><td class="num">$200</td><td class="num">$300</td><td class="num">$500</td></tr>
<tr><td>E&amp;O insurance</td><td class="num">$0</td><td class="num">$0</td><td class="num">$80</td><td class="num">$80</td></tr>
<tr><td><strong>Monthly Total</strong></td><td class="num"><strong>$209</strong></td><td class="num"><strong>$2,019</strong></td><td class="num"><strong>$3,249</strong></td><td class="num"><strong>$5,809</strong></td></tr>
</tbody>
</table>

<p>Y2 opex of ~$70K/yr is justified against $295K+ in commission revenue (~24% opex ratio). Industry-healthy.</p>
</section>

<!-- 11 RISK REGISTER -->
<section>
<h1><span class="num">Section 11</span>Risk Register</h1>
<p class="section-intro">V1's 12 risks remain. Three new ones surface from your specific profile.</p>

<table>
<thead><tr><th>#</th><th>Risk</th><th>Watch For</th><th>Mitigation</th></tr></thead>
<tbody>
<tr><td>1</td><td>TICO study slips past month 1</td><td>Week 2 with &lt;5 hrs studied</td><td>Block 3 evenings/wk, no exceptions</td></tr>
<tr><td>2</td><td>Warm network underperforms expectations</td><td>End of M1 with &lt;3 bookings from 150-person list</td><td>Outreach was group-blast. Re-do 1-to-1 with voice memos</td></tr>
<tr><td>3</td><td>Cold email deliverability tanks</td><td>Spam-folder rate &gt;40%</td><td>Add second domain, reduce volume, vary subject lines</td></tr>
<tr><td>4</td><td>Day-job lull time disappears</td><td>Workload spike kills your daytime extracted hours</td><td>Pre-commit to 6&ndash;9pm + Saturday morning blocks</td></tr>
<tr><td>5</td><td>Burnout at month 9</td><td>Working day job + business 70+ hrs, no inflection</td><td>Drop the 2 worst-performing segments; take a long weekend</td></tr>
<tr><td>6</td><td>VA quality is below expectation</td><td>Content drafts unusable; admin errors compounding</td><td>Replace within 6 weeks. Quality VAs exist; first hire often isn't right</td></tr>
<tr><td>7</td><td><strong>NEW: Content voice drift</strong></td><td>VA-produced content sounds corporate; you hate it</td><td>Toronto editor reviewing top 5 posts/mo with voice calibration sessions</td></tr>
<tr><td>8</td><td>Wrong segment dominates</td><td>80% bach parties; you hate it</td><td>Tilt outreach away; brand is flexible</td></tr>
<tr><td>9</td><td>HST registration missed</td><td>Cross $30K in 4 rolling quarters unregistered</td><td>Register voluntarily at month 4&ndash;5</td></tr>
<tr><td>10</td><td><strong>NEW: Operator-vs-exit drift</strong></td><td>Y3 you can't step back; exit path closes</td><td>Decide at Y4. Plan stays for Path A unless you reverse</td></tr>
<tr><td>11</td><td>Fora policy changes hurt economics</td><td>Commission split shifts</td><td>Independent brand built; ready to leave for own host agency</td></tr>
<tr><td>12</td><td>Supplier commission compression</td><td>Industry-wide cuts</td><td>Diversify supplier mix; lean into FIT independents</td></tr>
<tr><td>13</td><td>Recession Y2&ndash;Y3</td><td>Discretionary travel drops 20%+</td><td>Shift mix to family + milestone (less elastic) away from bach</td></tr>
<tr><td>14</td><td><strong>NEW: Network exhaustion</strong></td><td>Y2 H2 with warm-network referrals slowing dramatically</td><td>Cold outreach + content must be producing real volume by Y2 to bridge</td></tr>
</tbody>
</table>
</section>

<!-- 12 DECISION GATES -->
<section>
<h1><span class="num">Section 12</span>Decision Gates</h1>

<h2>Gate 1 &mdash; Month 6: Day-Job Continuation</h2>
<p>Reaffirmed: <strong>day job stays.</strong> Under-3-months runway makes earlier exit financially unsafe regardless of business performance.</p>

<h2>Gate 2 &mdash; Month 12: Incorporation</h2>
<p>If business net &gt; $60K Y1, incorporate as CCPC. Defer tax at 12.2% small-business rate; eligible for LCGE on Y5 exit.</p>

<h2>Gate 3 &mdash; Month 13&ndash;15: Day-Job Exit</h2>
<p>Dual trigger required:</p>
<ol>
<li>Business at $2,500/wk net for 8 consecutive weeks</li>
<li>$30K savings buffer (6 months of $5K/mo burn) accumulated</li>
</ol>

<h2>Gate 4 &mdash; Month 18&ndash;20: First Sub-Advisor</h2>
<p>Hire when: leads exceed capacity AND SOPs documented AND $30K+ override pool fundable AND specific person identified.</p>

<h2>Gate 5 &mdash; Year 3: Host Agency Independence</h2>
<p>Leave Fora when team override revenue exceeds $80K/yr.</p>

<h2>Gate 6 &mdash; Year 4: Path A vs Path B</h2>
<p>If revenue and team are trending: choose lifestyle (Path A) or exit-prep (Path B). Path B requires deliberate Y3&ndash;Y5 founder-step-back which conflicts with stated &ldquo;high-touch operator&rdquo; preference. Default expected: <strong>Path A.</strong></p>
</section>

<!-- 13 WEEKLY RHYTHM -->
<section>
<h1><span class="num">Section 13</span>Weekly Operating Rhythm (Ambivert-Friendly)</h1>
<p class="section-intro">Caps protect against burnout. The schedule respects that talking to people, while energizing, is costly.</p>

<h2>Hard Rules</h2>
<ul>
<li><strong>Max 5 client calls per day.</strong> Beyond that, quality drops.</li>
<li><strong>Two protected solo blocks per week:</strong> Monday morning (planning), Friday afternoon (review). No calls.</li>
<li><strong>One full off-day weekly</strong> (Saturday or Sunday) &mdash; no business activity.</li>
<li><strong>Partnership coffees &mdash; max 3/week in-person.</strong> Higher cost than client calls.</li>
</ul>

<h2>Steady-State Week (M6+, Day Job + Business)</h2>
<table>
<thead><tr><th>Day</th><th>Day-Job (8am&ndash;5pm)</th><th>Business (Lull + Evening)</th><th>Business Hrs</th></tr></thead>
<tbody>
<tr><td><strong>Monday</strong></td><td>Day job; lull time: outreach review (45 min)</td><td>Evening: 2 client calls + weekly planning (90 min)</td><td>2.25</td></tr>
<tr><td><strong>Tuesday</strong></td><td>Day job; lull: VA briefing (30 min)</td><td>Evening: 2 client calls + 1 partnership call (90 min)</td><td>2.0</td></tr>
<tr><td><strong>Wednesday</strong></td><td>Day job; lull: voice memos for content (30 min)</td><td>Evening: 3 client calls (90 min)</td><td>2.0</td></tr>
<tr><td><strong>Thursday</strong></td><td>Day job; lull: bookings work (45 min)</td><td>Evening: in-person partner coffee + 1 client (2 hrs)</td><td>2.75</td></tr>
<tr><td><strong>Friday</strong></td><td>Day job; lull: review + close week (30 min)</td><td>Evening: bookings work (90 min)</td><td>2.0</td></tr>
<tr><td><strong>Saturday</strong></td><td>OFF or content review (45 min)</td><td>3&ndash;4 client calls (intake heavy)</td><td>4.0</td></tr>
<tr><td><strong>Sunday</strong></td><td>OFF</td><td>OFF</td><td>0</td></tr>
<tr><td><strong>Total</strong></td><td></td><td></td><td><strong>~15 hrs/wk on top of day job</strong></td></tr>
</tbody>
</table>

<p>15 hrs/wk is the realistic steady-state alongside the day job. Peaks to 25 hrs/wk during seasonal pushes (January planning, October winter-break planning).</p>

<h2>Post-Day-Job Schedule (M15+)</h2>
<p>Once day job exits, capacity doubles. ~30 hrs/wk steady-state on business, 8 hrs personal time gain. Use the gain for: physical training, dating, longer personal travel, the things that disappeared in Y1.</p>
</section>

<!-- 14 EXIT MATH -->
<section>
<h1><span class="num">Section 14</span>The Two-Path Exit Math</h1>
<p class="section-intro">Both paths produce serious wealth. They differ on whether you're running the business in year 6 or holding the proceeds.</p>

<h2>Path A &mdash; Operator Lifestyle</h2>
<table>
<thead><tr><th>Year</th><th class="num">Personal Income</th><th class="num">Cumulative</th></tr></thead>
<tbody>
<tr><td>Y1</td><td class="num">$100K (business) + $105K (day job) = $205K</td><td class="num">$205K</td></tr>
<tr><td>Y2</td><td class="num">$185K</td><td class="num">$390K</td></tr>
<tr><td>Y3</td><td class="num">$295K</td><td class="num">$685K</td></tr>
<tr><td>Y4</td><td class="num">$410K</td><td class="num">$1.1M</td></tr>
<tr><td>Y5</td><td class="num">$540K</td><td class="num">$1.6M</td></tr>
<tr><td>Y6&ndash;Y10 (continued)</td><td class="num">$550&ndash;700K/yr</td><td class="num">$5&ndash;6M by Y10</td></tr>
</tbody>
</table>

<h2>Path B &mdash; Build to Exit</h2>
<table>
<tbody>
<tr><td>Cumulative income Y1&ndash;Y5 (slightly lower than Path A; founder-cost is recouped via equity)</td><td class="num">$1.4M</td></tr>
<tr><td>Y5 sale at midpoint multiple (4.5x EBITDA on $5M revenue, 28% margin)</td><td class="num">$6.3M EV</td></tr>
<tr><td>Founder equity retained at sale (85%)</td><td class="num">$5.3M</td></tr>
<tr><td>2-3 year earnout (acquirer typical)</td><td class="num">$1.5M</td></tr>
<tr><td><strong>Y5 founder total take</strong></td><td class="num"><strong>~$8.2M</strong></td></tr>
<tr><td>Post-sale: continue as Acquired CEO for 2&ndash;3 yrs at $400K/yr salary</td><td class="num">$1&ndash;1.2M</td></tr>
<tr><td><strong>Total by Y8</strong></td><td class="num"><strong>~$10.5M</strong></td></tr>
</tbody>
</table>

<h2>Side-by-Side</h2>
<table>
<thead><tr><th></th><th class="num">Path A (Lifestyle)</th><th class="num">Path B (Exit)</th></tr></thead>
<tbody>
<tr><td>Y5 wealth</td><td class="num">$1.6M cumulative</td><td class="num">$8.2M lump + accumulated</td></tr>
<tr><td>Y10 wealth</td><td class="num">$5&ndash;6M</td><td class="num">$11&ndash;15M (assuming reinvested)</td></tr>
<tr><td>Y5 lifestyle</td><td class="num">Busy operator, &ldquo;in the room&rdquo;</td><td class="num">Stepped back, prepared for sale</td></tr>
<tr><td>Y6&ndash;Y10 lifestyle</td><td class="num">Continue operating</td><td class="num">Sold; CEO of acquired entity OR free</td></tr>
<tr><td>Risk</td><td class="num">Industry compression; you have to keep working</td><td class="num">Valuation drops; founder-dependency penalty</td></tr>
<tr><td>Family fit (3&ndash;5 yr kids window)</td><td class="num">Compatible; you control hours</td><td class="num">Compatible; less day-to-day pressure post-sale</td></tr>
</tbody>
</table>

<div class="callout gold">
    <h4>The Honest Answer</h4>
    <p>Your stated preferences point to Path A. Path A still produces $5&ndash;6M of cumulative income by Y10 &mdash; not generational wealth but real wealth, sustained by an operating asset you fully control. Path B produces a much larger lump sum but requires founder-step-back behavior you said you don't want. Default to Path A; preserve Path B optionality by maintaining clean books and a distinct brand starting Y3.</p>
</div>
</section>

<!-- APPENDIX -->
<section>
<h1><span class="num">Appendix A</span>Updated Templates &amp; Scripts</h1>

<h2>A.1 &mdash; The 150-Person Warm Network Mapping Sheet (Template)</h2>
<table>
<thead><tr><th>Name</th><th>Relationship</th><th>Demo</th><th>Next Likely Trip</th><th>Approach Date</th><th>Status</th></tr></thead>
<tbody>
<tr><td>[Name]</td><td>HS friend</td><td>Married, 28</td><td>1st anniversary trip Aug</td><td>M1 W1</td><td>Not yet contacted</td></tr>
<tr><td>[Name]</td><td>Cousin</td><td>Engaged</td><td>Honeymoon Sept</td><td>M1 W1</td><td>Not yet contacted</td></tr>
<tr><td>[Name]</td><td>Family friend</td><td>40s, 3 kids</td><td>Pesach family trip</td><td>M1 W2</td><td>Not yet contacted</td></tr>
<tr><td>[etc &times; 147]</td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

<h2>A.2 &mdash; The Network Coffee Pitch Script</h2>
<div class="callout">
<p><em>&ldquo;Thanks for grabbing coffee. Quick context: I just got my travel-advisor license through Fora Travel. It's the millennial-focused agency &mdash; we book the same hotels you'd see on Expedia, except suppliers pay us a commission AND give your clients upgrades, breakfast, credits, the stuff you can't get direct.</em></p>
<p><em>The reason I wanted to meet: the best clients in this business come from people like you &mdash; a planner / agent / broker who's in the room when couples and families are making big decisions. The arrangement: anyone you send my way, I send you 25% of my commission. Paid quarterly. No contract, no quota. If you send me ten couples, you make a few thousand dollars passive income. If you send me zero, no problem.</em></p>
<p><em>The reason this works in our community specifically: you and I know everyone. The same family that's planning a Pesach trip is planning their daughter's bat mitzvah trip is planning their parents' 60th. One trusted advisor handles all of it. That advisor should be me &mdash; and you should get paid for it.</em></p>
<p><em>Want to try it for 90 days, no formal commitment?&rdquo;</em></p>
</div>

<h2>A.3 &mdash; The VA Hiring Brief (Content Producer)</h2>
<div class="callout">
<p><strong>Role:</strong> Content Producer, Travel Agency</p>
<p><strong>Location:</strong> Toronto preferred / remote acceptable</p>
<p><strong>Hours:</strong> 15&ndash;20 hrs/wk, flexible</p>
<p><strong>Compensation:</strong> $1,500&ndash;2,000 CAD/mo</p>
<p><strong>Responsibilities:</strong></p>
<ul>
<li>Transcribe weekly voice memos from founder (3&ndash;5/wk)</li>
<li>Produce 4 IG posts, 2 TikTok scripts, 2 LinkedIn posts, 1 biweekly newsletter from those memos</li>
<li>Schedule + publish all content</li>
<li>Engage with comments / DMs (escalate trip inquiries to founder via Slack)</li>
<li>Track content performance, report weekly</li>
</ul>
<p><strong>Voice profile:</strong> Playful, irreverent, smart-friend energy. Reference brands: Mejuri, Away, Glossier. Avoid corporate travel-agency tone.</p>
<p><strong>Where to source:</strong> OnlineJobs.ph (Philippines), Upwork (Toronto/LatAm), Twitter referrals (millennial copywriters), local university (Toronto Met / Ryerson / York English/journalism programs).</p>
</div>

<div class="divider">&middot; &middot; &middot;</div>
<p style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 13pt; font-style: italic; color: #4a4a47;">End of v2 Business Plan</p>
<p style="text-align: center; font-size: 9pt; color: #8B6F47;">Brand direction deliverable to follow separately.</p>
</section>
"""


def main():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Preface — V2 Business Plan</title>
<style>{v1.CSS_TEXT}</style>
</head>
<body>
{html_body()}
</body>
</html>
"""
    font_config = FontConfiguration()
    HTML(string=html_doc).write_pdf(str(OUT), font_config=font_config)
    print(f"Written: {OUT}")


if __name__ == "__main__":
    main()
