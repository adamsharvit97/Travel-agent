"""Generate the Preface five-year business plan as a branded PDF."""
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

OUT = Path(__file__).parent / "Preface-Business-Plan.pdf"
HTML_OUT = Path(__file__).parent / "_plan.html"

CSS_TEXT = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

@page {
    size: Letter;
    margin: 0.85in 0.85in 1in 0.85in;
    @bottom-center {
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #8B6F47;
    }
    @top-right {
        content: "PREFACE  ·  FIVE-YEAR BUSINESS PLAN";
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        letter-spacing: 0.15em;
        color: #b8a988;
    }
}

@page :first {
    margin: 0;
    @bottom-center { content: none; }
    @top-right { content: none; }
}

@page toc {
    @top-right { content: "TABLE OF CONTENTS"; font-family: 'Inter', sans-serif; font-size: 8pt; letter-spacing: 0.15em; color: #b8a988; }
}

html, body {
    font-family: 'Inter', sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1A1A1A;
    background: #ffffff;
}

/* COVER */
.cover {
    page: cover;
    page-break-after: always;
    background: #F4EDE0;
    height: 100vh;
    padding: 1.5in 1in 1in 1in;
    box-sizing: border-box;
    position: relative;
}
.cover-mark {
    font-family: 'Cormorant Garamond', serif;
    font-size: 28pt;
    font-weight: 500;
    letter-spacing: 0.08em;
    color: #500000;
}
.cover-rule {
    margin-top: 0.4in;
    margin-bottom: 0.4in;
    width: 1.2in;
    height: 2px;
    background: #8B6F47;
}
.cover-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 56pt;
    font-weight: 400;
    line-height: 1.05;
    color: #1A1A1A;
    margin: 0;
}
.cover-subtitle {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 22pt;
    font-weight: 300;
    color: #4a4a47;
    margin-top: 0.3in;
    line-height: 1.3;
}
.cover-meta {
    position: absolute;
    bottom: 1.2in;
    left: 1in;
    right: 1in;
    font-family: 'Inter', sans-serif;
    font-size: 9.5pt;
    color: #4a4a47;
    letter-spacing: 0.05em;
    display: flex;
    justify-content: space-between;
    border-top: 1px solid #b8a988;
    padding-top: 0.25in;
}
.cover-meta .label { display: block; font-size: 7.5pt; letter-spacing: 0.2em; color: #8B6F47; text-transform: uppercase; margin-bottom: 4pt; }
.cover-meta .value { font-size: 10.5pt; color: #1A1A1A; }

/* SECTION HEADERS */
h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 34pt;
    font-weight: 400;
    color: #1A1A1A;
    margin: 0 0 0.05in 0;
    line-height: 1.1;
    page-break-before: always;
    page-break-after: avoid;
}
h1 .num {
    display: block;
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    letter-spacing: 0.25em;
    color: #8B6F47;
    text-transform: uppercase;
    margin-bottom: 10pt;
}
h1::after {
    content: "";
    display: block;
    width: 0.8in;
    height: 2px;
    background: #8B6F47;
    margin-top: 0.15in;
    margin-bottom: 0.25in;
}
h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 20pt;
    font-weight: 500;
    color: #500000;
    margin: 0.35in 0 0.1in 0;
    line-height: 1.2;
    page-break-after: avoid;
}
h3 {
    font-family: 'Inter', sans-serif;
    font-size: 11pt;
    font-weight: 600;
    color: #1A1A1A;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin: 0.22in 0 0.08in 0;
    page-break-after: avoid;
}
h4 {
    font-family: 'Inter', sans-serif;
    font-size: 10pt;
    font-weight: 600;
    color: #500000;
    margin: 0.18in 0 0.05in 0;
    page-break-after: avoid;
}

/* TEXT */
p { margin: 0 0 0.1in 0; }
em { color: #4a4a47; }
strong { color: #1A1A1A; font-weight: 600; }
.lead {
    font-family: 'Cormorant Garamond', serif;
    font-size: 14pt;
    font-style: italic;
    color: #4a4a47;
    line-height: 1.45;
    margin: 0.1in 0 0.25in 0;
}

ul, ol { margin: 0.05in 0 0.15in 0.25in; padding: 0; }
li { margin-bottom: 4pt; }
ul li::marker { color: #8B6F47; }

/* TABLES */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.12in 0 0.2in 0;
    font-size: 9pt;
    page-break-inside: avoid;
}
thead th {
    background: #EBE1CC;
    color: #500000;
    text-align: left;
    padding: 7pt 8pt;
    font-weight: 600;
    font-size: 8.5pt;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border-bottom: 2px solid #8B6F47;
}
tbody td {
    padding: 6pt 8pt;
    border-bottom: 1px solid #EBE1CC;
    vertical-align: top;
}
tbody tr:nth-child(even) td { background: #faf6ed; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }

/* CALLOUTS */
.callout {
    background: #F4EDE0;
    border-left: 3px solid #500000;
    padding: 12pt 16pt;
    margin: 0.18in 0;
    font-size: 9.5pt;
    line-height: 1.5;
    page-break-inside: avoid;
}
.callout h4 { margin-top: 0; }
.callout.warn { border-left-color: #b85c00; background: #fbf3e6; }
.callout.gold { border-left-color: #8B6F47; }

/* EXECUTIVE SUMMARY BOX */
.exec-stats {
    display: flex;
    gap: 14pt;
    margin: 0.25in 0;
    page-break-inside: avoid;
}
.exec-stats > div {
    flex: 1;
    background: #F4EDE0;
    padding: 14pt;
    border-top: 2px solid #500000;
}
.exec-stats .label {
    font-size: 7.5pt;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #8B6F47;
}
.exec-stats .stat {
    font-family: 'Cormorant Garamond', serif;
    font-size: 26pt;
    font-weight: 500;
    color: #500000;
    line-height: 1.05;
    margin: 6pt 0 4pt 0;
}
.exec-stats .note { font-size: 8.5pt; color: #4a4a47; line-height: 1.3; }

/* TOC */
.toc { page: toc; }
.toc-entry {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dotted #d8cdb3;
    padding: 6pt 0;
    font-size: 10.5pt;
}
.toc-entry .num {
    font-family: 'Inter', sans-serif;
    color: #8B6F47;
    font-weight: 500;
    width: 30pt;
}
.toc-entry .title { flex: 1; color: #1A1A1A; font-family: 'Cormorant Garamond', serif; font-size: 13pt; }
.toc-entry .page { color: #500000; font-weight: 600; font-size: 9.5pt; font-family: 'Inter', sans-serif; }
.toc-subentry {
    padding: 3pt 0 3pt 35pt;
    font-size: 9.5pt;
    color: #4a4a47;
    display: flex;
    justify-content: space-between;
}

/* CODE / TEMPLATES */
.email-template {
    background: #faf6ed;
    border: 1px solid #d8cdb3;
    padding: 14pt 16pt;
    margin: 0.12in 0;
    font-size: 9pt;
    line-height: 1.55;
    page-break-inside: avoid;
}
.email-template .meta {
    font-family: 'Inter', sans-serif;
    font-size: 8pt;
    color: #8B6F47;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 6pt;
}
.email-template .subject { font-weight: 600; margin-bottom: 8pt; color: #1A1A1A; }
.email-template .body { font-family: 'Inter', sans-serif; white-space: pre-wrap; }

/* PHASE BANNERS */
.phase-banner {
    background: linear-gradient(135deg, #500000 0%, #6b1414 100%);
    color: #F4EDE0;
    padding: 18pt 22pt;
    margin: 0.1in 0 0.2in 0;
    page-break-inside: avoid;
}
.phase-banner .phase-num {
    font-family: 'Inter', sans-serif;
    font-size: 8pt;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #d8cdb3;
}
.phase-banner .phase-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 24pt;
    margin: 6pt 0 4pt 0;
    line-height: 1.1;
}
.phase-banner .phase-sub {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 13pt;
    color: #EBE1CC;
}

/* KPI ROW */
.kpi-row {
    display: flex;
    gap: 10pt;
    margin: 0.15in 0;
    page-break-inside: avoid;
}
.kpi {
    flex: 1;
    border: 1px solid #d8cdb3;
    padding: 10pt;
    background: #fdfaf3;
}
.kpi .lab { font-size: 7.5pt; letter-spacing: 0.18em; text-transform: uppercase; color: #8B6F47; }
.kpi .val { font-family: 'Cormorant Garamond', serif; font-size: 19pt; color: #500000; margin: 3pt 0 0 0; line-height: 1.1; }
.kpi .sub { font-size: 8pt; color: #4a4a47; }

/* CHECKLIST */
.check-list { list-style: none; padding-left: 0; }
.check-list li {
    padding-left: 22pt;
    text-indent: -22pt;
    margin-bottom: 6pt;
}
.check-list li::before {
    content: "▢  ";
    color: #8B6F47;
    font-weight: 600;
}

/* TWO-COLUMN */
.two-col { column-count: 2; column-gap: 0.3in; column-rule: 1px solid #EBE1CC; }

/* DIVIDER */
.divider {
    text-align: center;
    margin: 0.3in 0;
    color: #b8a988;
    letter-spacing: 0.5em;
    font-size: 10pt;
}

.small { font-size: 8.5pt; color: #4a4a47; }
.tag {
    display: inline-block;
    background: #EBE1CC;
    color: #500000;
    font-size: 7.5pt;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 2pt 8pt;
    border-radius: 2pt;
    font-weight: 600;
    margin-right: 4pt;
}

.section-intro { color: #4a4a47; font-style: italic; margin-bottom: 0.15in; font-size: 10.5pt; font-family: 'Cormorant Garamond', serif; }
"""


def html_body():
    return r"""
<!-- COVER -->
<div class="cover">
    <div class="cover-mark">Preface</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">The Five-Year<br/>Business Plan</h1>
    <div class="cover-subtitle">From licensed-day-one to exit-ready.<br/>A complete operating roadmap for an independent travel advisor practice.</div>
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
            <span class="label">Horizon</span>
            <span class="value">1 mo · 3 mo · 6 mo · 1 yr · 3 yr · 5 yr</span>
        </div>
    </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="toc">
    <h1><span class="num">Contents</span>Table of Contents</h1>
    <div class="toc-entry"><span class="num">01</span><span class="title">Executive Summary</span></div>
    <div class="toc-entry"><span class="num">02</span><span class="title">Founder Situation &amp; Capacity</span></div>
    <div class="toc-entry"><span class="num">03</span><span class="title">Unit Economics &amp; The Math</span></div>
    <div class="toc-entry"><span class="num">04</span><span class="title">Market Position &amp; Segments</span></div>
    <div class="toc-entry"><span class="num">05</span><span class="title">The Six-Horizon Plan</span></div>
    <div class="toc-subentry"><span>5.1   Month 1 — Foundation</span></div>
    <div class="toc-subentry"><span>5.2   Months 2–3 — Early Traction</span></div>
    <div class="toc-subentry"><span>5.3   Months 4–6 — Machine Running</span></div>
    <div class="toc-subentry"><span>5.4   Year 1 — Scaling</span></div>
    <div class="toc-subentry"><span>5.5   Year 3 — Team &amp; Brand</span></div>
    <div class="toc-subentry"><span>5.6   Year 5 — Exit-Ready</span></div>
    <div class="toc-entry"><span class="num">06</span><span class="title">The Cold Outreach Playbook</span></div>
    <div class="toc-entry"><span class="num">07</span><span class="title">The Content Engine</span></div>
    <div class="toc-entry"><span class="num">08</span><span class="title">The Partnership Playbook</span></div>
    <div class="toc-entry"><span class="num">09</span><span class="title">Financial Projections</span></div>
    <div class="toc-entry"><span class="num">10</span><span class="title">Capital &amp; Tooling Plan</span></div>
    <div class="toc-entry"><span class="num">11</span><span class="title">Risk Register</span></div>
    <div class="toc-entry"><span class="num">12</span><span class="title">Decision Gates</span></div>
    <div class="toc-entry"><span class="num">13</span><span class="title">Weekly Operating Rhythm</span></div>
    <div class="toc-entry"><span class="num">14</span><span class="title">The Exit Math</span></div>
    <div class="toc-entry"><span class="num">A</span><span class="title">Appendix — Templates &amp; Checklists</span></div>
</div>

<!-- 01 EXECUTIVE SUMMARY -->
<section>
<h1><span class="num">Section 01</span>Executive Summary</h1>
<p class="lead">Preface is a Toronto-based independent travel advisor practice serving the underserved 28–36 demographic — the &ldquo;HENRY&rdquo; cohort with luxury aspirations, real disposable income, and zero existing travel-advisor relationships. The opportunity is to be first.</p>

<h2>The Thesis</h2>
<p>The traditional travel-advisor industry has aged with its clientele. Virtuoso, Brownell, and Brilliant Travels skew 55+. Meanwhile, an entire generation of HENRYs — engaged couples, new parents, milestone-trip planners, friend groups doing annual ski weeks — books $5,000+ vacations on Expedia without realizing that the same hotel rooms, at identical rates, come with breakfast, upgrades, and credits when booked through a TICO-certified advisor.</p>

<p>The path: become licensed (TICO + Fora) in month 1, build a cold-outreach machine and content engine through months 2–6, hit a consistent <strong>$2,500/wk in commissions by day 300</strong>, and use Year 1's $100K+ revenue to fund team expansion in Year 2–3. By Year 5, Preface is either a $400–600K/yr lifestyle agency or a $3–16M acquisition target.</p>

<h2>The Numbers</h2>
<div class="exec-stats">
    <div>
        <div class="label">Day 300</div>
        <div class="stat">$2,500/wk</div>
        <div class="note">Average weekly commission run-rate</div>
    </div>
    <div>
        <div class="label">Year 1</div>
        <div class="stat">$80–135K</div>
        <div class="note">Total commission revenue</div>
    </div>
    <div>
        <div class="label">Year 3</div>
        <div class="stat">$250–400K</div>
        <div class="note">Personal income inc. team override</div>
    </div>
    <div>
        <div class="label">Year 5</div>
        <div class="stat">$3–16M</div>
        <div class="note">Modeled exit value at sale</div>
    </div>
</div>

<h2>Why This Works Now</h2>
<ul>
    <li><strong>Demographic gap.</strong> No serious advisor practice targets HENRYs under 40 in Canada. Existing advisors don't speak the language; existing online tools don't unlock luxury rates.</li>
    <li><strong>Distribution arbitrage.</strong> Fora Travel provides the back-office (supplier contracts, commission tracking, training, brand support) for $410/yr + 30% commission split. That's cheap infrastructure.</li>
    <li><strong>Cold-outreach asymmetry.</strong> Wedding planners and real estate agents in the US are accessible (CAN-SPAM applies, not CASL). 500 emails/day with a 2% reply rate yields 10+ partnership conversations/wk.</li>
    <li><strong>Content compounds.</strong> One viral TikTok in months 4–6 (statistically near-certain at 12+ posts/wk for 24 weeks) produces a multi-year inbound trickle.</li>
    <li><strong>Founder fit.</strong> Sales-trained, full-time job with steal-able lull time during business hours, scaling to full grind mode within 6 months.</li>
</ul>

<h2>Key Risks</h2>
<ul>
    <li>TICO certification deprioritized → entire timeline slips.</li>
    <li>Burnout at month 9 before run-rate hits target.</li>
    <li>Day-job conflict surfaced too early, forcing a premature quit without runway.</li>
    <li>Founder cannot delegate at year 2–3, preventing team scale and locking practice into solo plateau.</li>
</ul>

<h2>Critical Decisions Ahead</h2>
<ol>
    <li><strong>Month 6:</strong> Day-job — stay, reduce, or quit.</li>
    <li><strong>Month 12:</strong> Incorporate (CCPC) for tax deferral and future LCGE eligibility.</li>
    <li><strong>Month 18:</strong> First sub-advisor hire under Fora team structure.</li>
    <li><strong>Year 3:</strong> Stay on Fora vs. become independent TICO host agency.</li>
    <li><strong>Year 4–5:</strong> Sell (acquisition) vs. operate (lifestyle income forever).</li>
</ol>
</section>

<!-- 02 FOUNDER SITUATION -->
<section>
<h1><span class="num">Section 02</span>Founder Situation &amp; Capacity</h1>
<p class="section-intro">An honest accounting of what's available, what's constrained, and what changes when.</p>

<h2>Current State (Month 0)</h2>
<table>
<tbody>
<tr><td><strong>Age</strong></td><td>29</td></tr>
<tr><td><strong>Location</strong></td><td>Toronto, Canada</td></tr>
<tr><td><strong>Primary Income</strong></td><td>Full-time sales role (covers personal overhead)</td></tr>
<tr><td><strong>Available Hours (current)</strong></td><td>~30–35 hrs/wk — workday lull (2–3 hrs) + evenings (3–5 hrs) + weekends</td></tr>
<tr><td><strong>Available Hours (post-move)</strong></td><td>60–80 hrs/wk — &ldquo;absolute grind mode&rdquo;</td></tr>
<tr><td><strong>Network</strong></td><td>~50 warm-network individuals appropriate for initial outreach (friends, family, ex-colleagues, peer engaged couples)</td></tr>
<tr><td><strong>Skills</strong></td><td>Sales (primary), customer-facing, writing; willing to learn content production</td></tr>
<tr><td><strong>Capital Available</strong></td><td>Sufficient for ~$1K month-1 setup + $200/mo opex through year 1</td></tr>
<tr><td><strong>Runway</strong></td><td>Day job income still primary — business is supplemental until month 6+</td></tr>
</tbody>
</table>

<h2>Capacity Curve by Phase</h2>
<table>
<thead><tr><th>Phase</th><th>Months</th><th>Hours/wk on business</th><th>Day-job state</th></tr></thead>
<tbody>
<tr><td>Foundation</td><td>0–1</td><td>20–25</td><td>Full-time</td></tr>
<tr><td>Early Traction</td><td>2–3</td><td>30–35</td><td>Full-time</td></tr>
<tr><td>Machine Running</td><td>4–6</td><td>40–50</td><td>Full-time, decision pending</td></tr>
<tr><td>Scaling</td><td>7–12</td><td>50–60</td><td>Reduced or phased out</td></tr>
<tr><td>Team Build</td><td>13–36</td><td>40–50</td><td>Quit</td></tr>
<tr><td>Operator Mode</td><td>37–60</td><td>30–40</td><td>n/a</td></tr>
</tbody>
</table>

<h2>Constraints to Plan Around</h2>
<div class="callout warn">
    <h4>Day-Job IP &amp; Non-Compete</h4>
    <p>Operate this business exclusively from personal devices, personal email, personal Calendly, personal accounts. Do not store client data on company laptops. Do not use company-paid Zoom, Slack, or productivity tools. Do not work on this during clearly-tracked sales-team time blocks. If a non-compete or non-solicit exists in your employment contract, have an employment lawyer review it before launch ($300 well spent).</p>
</div>

<div class="callout">
    <h4>CASL Compliance (Canada)</h4>
    <p>Canadian Anti-Spam Legislation restricts cold electronic outreach to Canadian recipients without express or implied consent. <strong>All cold email is targeted at US recipients</strong> (CAN-SPAM, much looser). Canadian outreach happens in-person, by referral, or to industry peers under implied-consent provisions.</p>
</div>

<div class="callout gold">
    <h4>TICO Certification Is The Critical Path</h4>
    <p>You cannot legally sell travel from Ontario without TICO certification. The certification process is ~$150 plus an exam. Block 3 evenings/week for study. <strong>No bookings happen until this is passed.</strong></p>
</div>
</section>

<!-- 03 UNIT ECONOMICS -->
<section>
<h1><span class="num">Section 03</span>Unit Economics &amp; The Math</h1>
<p class="section-intro">Every income target back-solves to a specific number of bookings, calls, and outreach touches. Here is the math.</p>

<h2>Per-Booking Revenue</h2>
<p>The Fora model: you collect the trip price from the client, the supplier (hotel, cruise line, tour operator) pays a commission to Fora directly, Fora retains 30% and remits 70% to you. You separately invoice a planning fee from the client for complex trips.</p>

<table>
<thead>
<tr><th>Trip Type</th><th class="num">Avg Booking</th><th class="num">Commission %</th><th class="num">After Fora 30%</th><th class="num">Planning Fee</th><th class="num">Net to You</th></tr>
</thead>
<tbody>
<tr><td>Couples weekend</td><td class="num">$4,500</td><td class="num">11%</td><td class="num">$347</td><td class="num">$100</td><td class="num">$447</td></tr>
<tr><td>Family all-inclusive</td><td class="num">$7,000</td><td class="num">13%</td><td class="num">$637</td><td class="num">$150</td><td class="num">$787</td></tr>
<tr><td>Honeymoon (2-stop)</td><td class="num">$12,000</td><td class="num">12%</td><td class="num">$1,008</td><td class="num">$500</td><td class="num">$1,508</td></tr>
<tr><td>Bach weekend (10 pax)</td><td class="num">$14,000</td><td class="num">12%</td><td class="num">$1,176</td><td class="num">$500</td><td class="num">$1,676</td></tr>
<tr><td>Milestone group (15 pax)</td><td class="num">$60,000</td><td class="num">12%</td><td class="num">$5,040</td><td class="num">$2,500</td><td class="num">$7,540</td></tr>
<tr><td><strong>Blended Average</strong></td><td class="num"></td><td class="num"></td><td class="num"></td><td class="num"></td><td class="num"><strong>$700</strong></td></tr>
</tbody>
</table>
<p class="small">Blended average weighted to expected Y1 mix: 30% couples, 20% family, 18% honeymoon, 18% bach, 4% milestone, 10% other.</p>

<h2>Income Targets Back-Solved</h2>
<table>
<thead><tr><th>Income Tier</th><th class="num">$/wk Net</th><th class="num">Bookings/wk</th><th class="num">Bookings/yr</th><th>Phase</th></tr></thead>
<tbody>
<tr><td>Y1 Minimum Floor</td><td class="num">$1,000</td><td class="num">1.5</td><td class="num">75</td><td>Months 4–6</td></tr>
<tr><td>Day 300 Target</td><td class="num">$2,500</td><td class="num">3.5</td><td class="num">180</td><td>Month 10</td></tr>
<tr><td>Y2 Stable Run-Rate</td><td class="num">$3,500</td><td class="num">5</td><td class="num">260</td><td>Year 2</td></tr>
<tr><td>Solo Ceiling</td><td class="num">$5,000</td><td class="num">7</td><td class="num">365</td><td>Year 3</td></tr>
</tbody>
</table>

<h2>Activity Back-Solved (Day 300 Target)</h2>
<p>At day 300 you need 3.5 bookings/wk. Conversion math:</p>
<table>
<thead><tr><th>Funnel Stage</th><th class="num">Volume/wk</th><th class="num">Conv. %</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Cold emails sent (US)</td><td class="num">7,500</td><td class="num">—</td><td>1,500/day × 5 days, across 2–3 sending domains</td></tr>
<tr><td>Replies</td><td class="num">75</td><td class="num">1.0%</td><td>B2C engaged + B2B planners blended</td></tr>
<tr><td>Discovery calls booked</td><td class="num">22</td><td class="num">30%</td><td>Calendly link in second reply</td></tr>
<tr><td>Intake calls held</td><td class="num">18</td><td class="num">80%</td><td>20% no-show / reschedule</td></tr>
<tr><td>Proposals sent</td><td class="num">12</td><td class="num">65%</td><td>Skip prospects who aren't ready</td></tr>
<tr><td>Bookings closed</td><td class="num">3.5</td><td class="num">30%</td><td>Industry-normal close rate</td></tr>
</tbody>
</table>
<p>Plus partnership-sourced leads (15–25/wk from 5+ active partners by month 9) and content-sourced inbound (5–10/wk by month 9) — these have 2–3x higher close rates because trust is pre-built. The cold-email funnel is the engine; partnerships and content are the multipliers.</p>

<h2>Lifetime Client Economics</h2>
<p>A first-time honeymoon client at age 30 is worth more than just the honeymoon. Modeled lifetime journey:</p>
<table>
<thead><tr><th>Year</th><th>Trip</th><th class="num">Booking</th><th class="num">Net to You</th></tr></thead>
<tbody>
<tr><td>Y0</td><td>Bachelor / Bachelorette weekend</td><td class="num">$1,400/pp × group</td><td class="num">$1,675</td></tr>
<tr><td>Y0</td><td>Honeymoon</td><td class="num">$12,000</td><td class="num">$1,508</td></tr>
<tr><td>Y1</td><td>First anniversary</td><td class="num">$6,000</td><td class="num">$640</td></tr>
<tr><td>Y2</td><td>Babymoon</td><td class="num">$4,500</td><td class="num">$450</td></tr>
<tr><td>Y3</td><td>First-baby trip</td><td class="num">$5,500</td><td class="num">$530</td></tr>
<tr><td>Y4–Y8</td><td>Annual family week × 5</td><td class="num">$7,000 each</td><td class="num">$3,935</td></tr>
<tr><td>Y9</td><td>Friend-group ski trip</td><td class="num">$3,500/pp × 4</td><td class="num">$840</td></tr>
<tr><td>Y10</td><td>Milestone 40th birthday trip</td><td class="num">$25,000</td><td class="num">$2,650</td></tr>
<tr><td><strong>10-Year LTV</strong></td><td></td><td class="num"></td><td class="num"><strong>~$12,228</strong></td></tr>
</tbody>
</table>

<div class="callout gold">
    <h4>The Strategic Takeaway</h4>
    <p>A booked client isn't a transaction — it's the start of a 10-year, $12K+ revenue stream, with referrals stacked on top. This is why customer-acquisition costs of $200–400 per booked client are sustainable. It's also why every client must get a 5-star experience: a single negative reference at month 18 doesn't just lose one trip, it loses a decade of compounding.</p>
</div>
</section>

<!-- 04 MARKET POSITION -->
<section>
<h1><span class="num">Section 04</span>Market Position &amp; Segments</h1>
<p class="section-intro">Where Preface fits in a crowded but mis-targeted market.</p>

<h2>Competitive Landscape</h2>
<table>
<thead><tr><th>Competitor Type</th><th>Examples</th><th>Audience</th><th>Why You Win</th></tr></thead>
<tbody>
<tr><td>Legacy Luxury Agencies</td><td>Virtuoso member firms, Brownell, Brilliant Travels</td><td>55+ HNWI</td><td>Don't speak millennial language; advisors retire faster than they replace; client base aging out</td></tr>
<tr><td>OTAs</td><td>Expedia, Booking.com, Hotels.com</td><td>Everyone</td><td>No upgrades, no credits, no human; same rate but worse experience</td></tr>
<tr><td>DIY Booking</td><td>Direct-to-hotel</td><td>Self-directed</td><td>Most clients don't know suppliers give better rates to advisors than direct</td></tr>
<tr><td>Other Fora Advisors</td><td>~12,000 Fora advisors globally</td><td>Fragmented</td><td>Most are part-time hobbyists with no brand, no system, no segmentation</td></tr>
<tr><td>Bach-Trip Specialists</td><td>Bach Weekend, Bachelorette.com</td><td>Bach only</td><td>Single-segment; you own the same client across 10 years of trips</td></tr>
</tbody>
</table>

<h2>The Five Primary Segments</h2>
<table>
<thead><tr><th>Segment</th><th>Trigger</th><th class="num">Avg Booking</th><th class="num">Y1 Mix</th></tr></thead>
<tbody>
<tr><td><strong>Couples Annual Trip</strong></td><td>Planning January window</td><td class="num">$4,500</td><td class="num">30%</td></tr>
<tr><td><strong>Family School-Break</strong></td><td>Spring break / winter break</td><td class="num">$7,000</td><td class="num">20%</td></tr>
<tr><td><strong>Honeymoon</strong></td><td>Engagement → 8–14 mo out</td><td class="num">$12,000</td><td class="num">18%</td></tr>
<tr><td><strong>Bach / Bachelorette</strong></td><td>Engagement → 4–8 mo out</td><td class="num">$14,000 (group)</td><td class="num">18%</td></tr>
<tr><td><strong>Milestone Group</strong></td><td>40th / 50th / parents' anniversary</td><td class="num">$60,000 (group)</td><td class="num">4%</td></tr>
</tbody>
</table>

<h2>Six Additional Segments to Layer In</h2>
<table>
<thead><tr><th>Segment</th><th>Trigger</th><th class="num">Avg Trip</th><th>Strategic Value</th></tr></thead>
<tbody>
<tr><td><strong>Babymoon</strong></td><td>2nd–3rd trimester announcement</td><td class="num">$3–6K</td><td>Highly seasonal; stacks onto honeymoon clients</td></tr>
<tr><td><strong>First Anniversary</strong></td><td>11 months post-wedding</td><td class="num">$4–8K</td><td>CRM-triggered; near-100% conversion of honeymoon clients</td></tr>
<tr><td><strong>Friend-Group Annual</strong></td><td>Sept planning for following ski/golf season</td><td class="num">$2–3K/pp</td><td>Subscription-like; 5–10 year repeat</td></tr>
<tr><td><strong>Reunion Trip</strong></td><td>10-yr college reunion math</td><td class="num">$2–4K/pp</td><td>Predictable annual cohort; alumni network density</td></tr>
<tr><td><strong>Graduation</strong></td><td>MBA, residency, law school May–June</td><td class="num">$5–15K</td><td>High-spend; dense peer-referral pool</td></tr>
<tr><td><strong>Sabbatical / Reset</strong></td><td>Burnout, career break</td><td class="num">$8–25K</td><td>Story-rich content; high per-trip revenue</td></tr>
</tbody>
</table>

<h2>The Demographic Insight</h2>
<p>The strategic edge isn't a particular segment — it's the <strong>relationship-holder</strong>. In a 28–36 cohort, the adult child plans for the family. The 35-year-old daughter is the one who books her parents' 40th anniversary trip, her own honeymoon, her brother's bach weekend, the family Christmas vacation, and her own kid's first international trip. <strong>One trusted advisor relationship = 5–8 trips per year across the family system.</strong></p>
<p>This is why segmenting feels expansive: you're not chasing five audiences, you're serving one audience across many life moments.</p>

<div class="callout">
    <h4>Parents &amp; Grandparents — A Note On Scope</h4>
    <p>Avoid direct outreach to the 60+ demographic. That's the entrenched legacy lane (Virtuoso, Brownell) and they have decades of relationship capital you can't out-compete. Your edge is serving them <em>through their adult child</em> via the Milestone Group segment. Don't dilute the brand by targeting their generation directly.</p>
</div>
</section>

<!-- 05 SIX HORIZON PLAN -->
<section>
<h1><span class="num">Section 05</span>The Six-Horizon Plan</h1>
<p class="section-intro">Each phase has hard deliverables, KPIs, and a single failure mode that must be watched.</p>

<!-- 5.1 -->
<div class="phase-banner">
    <div class="phase-num">Phase 5.1  ·  Month 1</div>
    <div class="phase-title">Foundation</div>
    <div class="phase-sub">Get licensed, get launched, get the first five.</div>
</div>

<h3>Objective</h3>
<p>Be legally able to sell travel, technically able to book a trip, and personally credible by week 4. Close 3–5 bookings from existing network.</p>

<h3>Hard Deliverables</h3>
<ul class="check-list">
<li>TICO Certification Program purchased ($150) — week 1</li>
<li>Fora Canada application submitted — week 1</li>
<li>TICO exam passed — by week 3</li>
<li>Fora onboarding training started in parallel</li>
<li>Business domain + Google Workspace email — week 1</li>
<li>Calendly link configured — week 1</li>
<li>Tally/Typeform intake form — week 1</li>
<li>Website live (v2 mockups deployed) — week 3</li>
<li>Social handles secured (IG, TikTok, LinkedIn) — week 1</li>
<li>50-person warm-network list with &ldquo;next trip&rdquo; status — week 2</li>
</ul>

<h3>Month 1 KPIs</h3>
<div class="kpi-row">
    <div class="kpi"><div class="lab">Licensed</div><div class="val">Yes</div><div class="sub">TICO + Fora</div></div>
    <div class="kpi"><div class="lab">Bookings</div><div class="val">3–5</div><div class="sub">From warm network</div></div>
    <div class="kpi"><div class="lab">Revenue</div><div class="val">$1–3K</div><div class="sub">Commission</div></div>
    <div class="kpi"><div class="lab">Site Live</div><div class="val">Yes</div><div class="sub">3 testimonials staged</div></div>
</div>

<h3>Explicitly NOT Doing This Month</h3>
<ul>
<li>No paid ads</li>
<li>No cold outreach</li>
<li>No production content (just placeholder posts so profiles aren't empty)</li>
<li>No partnership outreach</li>
<li>No premium tooling</li>
</ul>

<div class="callout warn">
    <h4>The Failure Mode</h4>
    <p>TICO study gets deprioritized. The exam is the only gate with a true timeline lock. Block 3 evenings/wk and finish before week 4. If month 1 ends without TICO passed, the entire timeline slips.</p>
</div>

<!-- 5.2 -->
<div class="phase-banner">
    <div class="phase-num">Phase 5.2  ·  Months 2–3</div>
    <div class="phase-title">Early Traction</div>
    <div class="phase-sub">Build the machine, book the first twenty, look like a real business.</div>
</div>

<h3>Objective</h3>
<p>Move from &ldquo;friend with a license&rdquo; to operator with momentum. Cold outreach soft-launched. Content cadence locked. First wedding planner partnership.</p>

<h3>Hard Deliverables</h3>
<ul class="check-list">
<li>Cold email infrastructure live: Instantly.ai or Smartlead — week 5</li>
<li>Lead lists purchased: Apollo or Seamless.AI — week 5</li>
<li>Cold outbound: 500 emails/day (200 B2B planners + 300 B2C engaged) — week 7</li>
<li>Content cadence locked: IG 4×, TikTok 3×, LinkedIn 3× per week</li>
<li>Newsletter launched on Beehiiv or Substack — week 6</li>
<li>1–2 wedding planner partnerships signed with 25%-of-commission referral fee — by week 12</li>
<li>Toronto in-person coffee circuit: 10 meetings with wedding planners, photographers, venues</li>
</ul>

<h3>Month 3 KPIs</h3>
<div class="kpi-row">
    <div class="kpi"><div class="lab">Lifetime Clients</div><div class="val">15–25</div><div class="sub">Cumulative</div></div>
    <div class="kpi"><div class="lab">Monthly Revenue</div><div class="val">$4–6K</div><div class="sub">Commissions</div></div>
    <div class="kpi"><div class="lab">Partnerships</div><div class="val">1–2</div><div class="sub">Sending leads</div></div>
    <div class="kpi"><div class="lab">IG Followers</div><div class="val">~2K</div><div class="sub">Engaged audience</div></div>
</div>

<h3>The Cold Email Volume Logic</h3>
<p>Two sending domains (yourname@preface.travel + a secondary like yourname@gopreface.com) keeps deliverability healthy. 250 emails/day per inbox × 2 inboxes per domain × 2 domains = 1,000/day max safe volume. Start at 500/day in week 5, ramp to 1,000/day by week 8.</p>

<div class="callout warn">
    <h4>The Failure Mode</h4>
    <p>Cold outreach quality, not quantity, is the issue if month 3 ends with fewer than 15 clients. Re-read your sequences — if they read like every other cold email, they convert like every other cold email. Specificity beats polish: name a planner by their actual market and reference a trip type they actually deal with.</p>
</div>

<!-- 5.3 -->
<div class="phase-banner">
    <div class="phase-num">Phase 5.3  ·  Months 4–6</div>
    <div class="phase-title">Machine Running</div>
    <div class="phase-sub">Hit the floor. Cold + content + referrals all producing.</div>
</div>

<h3>Objective</h3>
<p>Hit minimum <strong>$1,000/wk commissions consistently</strong> by week 24. Decide on the day-job at month 6.</p>

<h3>Hard Deliverables</h3>
<ul class="check-list">
<li>Cold email scaled to 1,500–2,500/day across two sending domains</li>
<li>3–5 active partnerships sending warm leads weekly</li>
<li>5K+ Instagram, 5K+ TikTok, 500+ newsletter subscribers</li>
<li>At least one social post hits 100K+ views (statistically near-certain at this cadence)</li>
<li>Case-study page live: 3 real client trip recaps with photos</li>
<li>VA hired for 15–25 hrs/wk: lead-list cleaning, reply triage, scheduling</li>
<li>Lifetime clients: 40–60</li>
</ul>

<h3>Month 6 KPIs</h3>
<div class="kpi-row">
    <div class="kpi"><div class="lab">Monthly Revenue</div><div class="val">$5–8K</div><div class="sub">Commissions</div></div>
    <div class="kpi"><div class="lab">Weekly Average</div><div class="val">$1K+</div><div class="sub">Floor hit</div></div>
    <div class="kpi"><div class="lab">Partnerships</div><div class="val">5</div><div class="sub">Active sources</div></div>
    <div class="kpi"><div class="lab">Newsletter</div><div class="val">500+</div><div class="sub">Engaged subscribers</div></div>
</div>

<h3>The Day-Job Decision</h3>
<p>At end of month 6, choose one:</p>
<table>
<thead><tr><th>Option</th><th>Trigger Conditions</th><th>Outcome</th></tr></thead>
<tbody>
<tr><td><strong>Stay full-time</strong></td><td>Business &lt; $1K/wk OR runway &lt; 4 months</td><td>Extend Y1 target by 3–6 months</td></tr>
<tr><td><strong>Reduce to part-time</strong></td><td>If your employer offers 60% schedule</td><td>Cleaner ramp, lower stress</td></tr>
<tr><td><strong>Quit</strong></td><td>$1K+/wk for 8 consecutive weeks AND 4+ months runway saved</td><td>Required to hit $2,500/wk by day 300</td></tr>
</tbody>
</table>

<div class="callout warn">
    <h4>The Failure Mode</h4>
    <p>Quitting too early. The math of the day-300 target requires full-time effort starting around month 7, but only if foundations are working. Don't conflate &ldquo;I want to quit&rdquo; with &ldquo;the business says I should quit.&rdquo; The 8-consecutive-weeks rule is the test.</p>
</div>

<!-- 5.4 -->
<div class="phase-banner">
    <div class="phase-num">Phase 5.4  ·  Months 7–12</div>
    <div class="phase-title">Year 1 — Scaling</div>
    <div class="phase-sub">Hit $2,500/wk by day 300. Become a real business.</div>
</div>

<h3>Objective</h3>
<p>Average <strong>$2,500/wk</strong> by week 43 (day 300). End Y1 with $100K+ in commission revenue. Build systems that prevent burnout.</p>

<h3>Hard Deliverables</h3>
<ul class="check-list">
<li>$2,500/wk run-rate by week 43</li>
<li>150+ lifetime clients by month 12</li>
<li>10–15 active partnerships</li>
<li>10K+ combined social following</li>
<li>2,000–5,000 newsletter subscribers</li>
<li>First newsletter-only client conversion (someone who never met you in person)</li>
<li>VA at 20–25 hrs/wk handling all repeatable admin</li>
<li>Day-job phased out by month 9</li>
</ul>

<h3>Year 1 Financial Picture</h3>
<table>
<thead><tr><th>Line Item</th><th class="num">Annual</th></tr></thead>
<tbody>
<tr><td>Gross commission revenue</td><td class="num">$80–135K</td></tr>
<tr><td>Less: Fora 30% cut</td><td class="num">($24–40K)</td></tr>
<tr><td>Plus: planning fees</td><td class="num">$15–25K</td></tr>
<tr><td><strong>Net business revenue</strong></td><td class="num"><strong>$71–120K</strong></td></tr>
<tr><td>Less: opex (tools, VA, domain, email)</td><td class="num">($8–12K)</td></tr>
<tr><td><strong>Take-home before tax</strong></td><td class="num"><strong>$63–108K</strong></td></tr>
</tbody>
</table>

<h3>Quarterly Pacing</h3>
<table>
<thead><tr><th>Quarter</th><th>Months</th><th class="num">Target Revenue</th><th>Defining Activity</th></tr></thead>
<tbody>
<tr><td>Q1</td><td>1–3</td><td class="num">$5–15K</td><td>Foundation + early traction</td></tr>
<tr><td>Q2</td><td>4–6</td><td class="num">$15–25K</td><td>Machine running + day-job decision</td></tr>
<tr><td>Q3</td><td>7–9</td><td class="num">$25–40K</td><td>Acceleration</td></tr>
<tr><td>Q4</td><td>10–12</td><td class="num">$35–55K</td><td>$2,500/wk locked in</td></tr>
</tbody>
</table>

<div class="callout warn">
    <h4>The Failure Mode</h4>
    <p>Burnout at month 9. You're working harder than ever and the line doesn't yet show the inflection. Two responses are wrong: (a) quit, or (b) push harder on the same activity. The right response is to drop the two segments performing worst and double down on the three that work — and to take a real long weekend off.</p>
</div>

<!-- 5.5 -->
<div class="phase-banner">
    <div class="phase-num">Phase 5.5  ·  Year 3</div>
    <div class="phase-title">Team &amp; Brand</div>
    <div class="phase-sub">You hit max solo throughput. Choose: cap and run, or build.</div>
</div>

<h3>The Fork</h3>
<p>Year 3 forces a choice. Solo, you'll plateau at $200–280K personal commissions + fees. To go higher, you build a team.</p>

<h3>Path A — Solo Lifestyle</h3>
<ul>
<li>$200–300K commissions, $150–220K take-home</li>
<li>35-hour weeks, premium clients only</li>
<li>No team override revenue</li>
<li>Plateau forever; limited sale value</li>
</ul>

<h3>Path B — Build to Sell</h3>
<ul>
<li>2–4 advisors under Preface (Fora Team structure or independent host)</li>
<li>Personal $200K commissions + $50–100K team override = $250–300K total</li>
<li>$400K–1M total team commission revenue</li>
<li>Brand recognized in Toronto for the 28–36 demographic</li>
<li>Newsletter at 10–25K subscribers</li>
<li>25–40 partnership relationships, top 10 sending consistent volume</li>
</ul>

<h3>How to Find &amp; Pay Advisors</h3>
<p>The Fora Team Leader model lets you bring on advisors under your tier. You provide leads + training; you keep 20–30% override on their commissions. Talent pools:</p>
<ul>
<li><strong>Peer network</strong> — friends in PR, hospitality, sales who want side income</li>
<li><strong>Wedding planners' employees</strong> — adjacent skills, hate their hours</li>
<li><strong>Flameout Fora advisors</strong> — already licensed; lack leads; you have leads</li>
</ul>

<p>Typical first hire: sales-aptitude friend who sells ~$300–500K/yr in trips. Their commission ~$36–60K. Your override: $11–18K. With 3 such advisors, that's <strong>$40–55K passive override</strong> stacked on top of your personal output.</p>

<h3>Hire Trigger Conditions</h3>
<ol>
<li>Lead volume exceeds capacity (turning away or going cold)</li>
<li>Brand has gravitational pull (advisors apply to you)</li>
<li>Process is documented (intake, booking, follow-up SOPs)</li>
<li>You can pay them ($30K+ override pool available)</li>
</ol>
<p>Realistic earliest: month 18. Plan Y3 for 2–4.</p>

<h3>The Independent Host Decision</h3>
<p>Around Year 2–3 you'll evaluate leaving Fora for your own TICO-registered host agency.</p>
<table>
<thead><tr><th>Lever</th><th>Stay on Fora</th><th>Independent Host</th></tr></thead>
<tbody>
<tr><td>Commission split</td><td>70/30 to advisor</td><td>100% to you</td></tr>
<tr><td>Capital needed</td><td>$410/yr</td><td>$10K TCF deposit + setup</td></tr>
<tr><td>Back-office burden</td><td>Fora handles all</td><td>Your problem: commissions, E&amp;O, TICO compliance</td></tr>
<tr><td>Brand control</td><td>Partial — under Fora umbrella</td><td>Full</td></tr>
<tr><td>Sellability</td><td>Limited (Fora owns infrastructure)</td><td>High (clean asset)</td></tr>
<tr><td>Right time to switch</td><td>—</td><td>When override revenue alone is $80K+/yr</td></tr>
</tbody>
</table>

<!-- 5.6 -->
<div class="phase-banner">
    <div class="phase-num">Phase 5.6  ·  Year 5</div>
    <div class="phase-title">Exit-Ready</div>
    <div class="phase-sub">$200K isn't enough for a family. The exit is.</div>
</div>

<h3>Two End States</h3>
<table>
<thead><tr><th></th><th>Lifestyle Agency</th><th>Acquisition Target</th></tr></thead>
<tbody>
<tr><td>Team size</td><td>5–8 advisors</td><td>12–20 advisors</td></tr>
<tr><td>Revenue</td><td>$1.5–3M/yr</td><td>$4–8M/yr</td></tr>
<tr><td>Personal income</td><td>$400–600K/yr</td><td>$300–500K/yr pre-exit</td></tr>
<tr><td>Time investment</td><td>30–40 hrs/wk</td><td>50–60 hrs/wk Y3–Y5</td></tr>
<tr><td>Exit value</td><td>None (lifestyle)</td><td>$3–16M sale + 2–8M earnout</td></tr>
<tr><td>Best for</td><td>Income + family time</td><td>Generational wealth</td></tr>
</tbody>
</table>

<h3>Likely Acquirers</h3>
<ul>
<li><strong>Internova Travel Group</strong> — owns Travel Leaders, Altour, Protravel, Frosch, Tzell. Most active consolidator.</li>
<li><strong>Travel Edge</strong> — Internova's Canadian arm; most natural buyer for a Toronto-based agency.</li>
<li><strong>Virtuoso member firms</strong> — looking to expand into younger demographics.</li>
<li><strong>PE roll-up funds</strong> — increasingly active in travel advisory.</li>
</ul>

<h3>Positioning for Scenario 2 (Exit)</h3>
<ol>
<li><strong>Own brand distinct from Fora.</strong> Acquirers buy brands, customer lists, and books — not &ldquo;a high-volume Fora advisor.&rdquo;</li>
<li><strong>Document by Y3.</strong> SOPs, training, supplier relationships in writing.</li>
<li><strong>Defensible niche.</strong> &ldquo;The agency for millennials with luxury budgets&rdquo; commands a premium multiple.</li>
<li><strong>Repeatable revenue.</strong> Subscription elements (paid newsletter tier, corporate retainers) push valuation higher.</li>
<li><strong>Clean books.</strong> Incorporate Y2 at latest. Get a real accountant. Pay yourself a structured salary.</li>
<li><strong>Founder ego in check.</strong> Many advisor businesses fail to scale because the founder can't stop being the salesperson. The buyer needs to know the business runs without you.</li>
</ol>
</section>

<!-- 06 COLD OUTREACH PLAYBOOK -->
<section>
<h1><span class="num">Section 06</span>The Cold Outreach Playbook</h1>
<p class="section-intro">Specific volume, tools, sequences. Read this section before sending a single email.</p>

<h2>Volume &amp; Infrastructure</h2>
<table>
<thead><tr><th>Phase</th><th class="num">Daily Volume</th><th class="num">Inboxes</th><th class="num">Domains</th><th>Reply Target</th></tr></thead>
<tbody>
<tr><td>Months 2–3</td><td class="num">500</td><td class="num">2</td><td class="num">1</td><td>5/day</td></tr>
<tr><td>Months 4–6</td><td class="num">1,500</td><td class="num">4</td><td class="num">2</td><td>15/day</td></tr>
<tr><td>Months 7–12</td><td class="num">3,000–5,000</td><td class="num">8–12</td><td class="num">3–4</td><td>30–50/day</td></tr>
</tbody>
</table>

<h2>Tool Stack</h2>
<ul>
<li><strong>Cold email engine:</strong> Instantly.ai ($60–$100/mo) or Smartlead ($60/mo). Both handle multiple sending inboxes, warmup, deliverability.</li>
<li><strong>Lead enrichment:</strong> Apollo ($60/mo) or Seamless.AI ($100/mo). Apollo is friendlier UX; Seamless has more contacts.</li>
<li><strong>Inbox warmup:</strong> Mailwarm or built-in via Instantly. Run warmup for 2 weeks before sending volume.</li>
<li><strong>Reply triage:</strong> Done by VA from week 10 onward. Categorize: interested / not now / not a fit / unsubscribe.</li>
<li><strong>Scheduling:</strong> Calendly. Always include link in second touch.</li>
</ul>

<h2>Sequence 1 — Wedding Planners (B2B)</h2>

<div class="email-template">
<div class="meta">TOUCH 1  ·  DAY 0</div>
<div class="subject">Subject: Honeymoon referrals for {{Company}}</div>
<div class="body">Hi {{First Name}},

I run an independent travel advisor practice (Fora Travel, TICO-certified) focused on millennial couples — bachelorettes, honeymoons, and milestone trips.

I'm reaching out to wedding planners in {{City}} because most couples we book come from a planner referral. The arrangement: you send couples my way, I plan their honeymoon, and you earn 25% of my commission on every booking — paid quarterly. Average referral: ~$400 to your business per couple.

Worth a 15-min call to walk through it?

— {{Your Name}}
Preface · TICO #XXXXXXX
{{Calendly link}}</div>
</div>

<div class="email-template">
<div class="meta">TOUCH 2  ·  DAY 4</div>
<div class="subject">Subject: Re: Honeymoon referrals for {{Company}}</div>
<div class="body">Hi {{First Name}},

Quick follow-up on this. I closed three honeymoons in the last 30 days and could have placed two more if I'd had planner partners in {{City}}.

If 25% of commission isn't the right structure for {{Company}}, I'm flexible — happy to discuss flat per-referral fees or a marketing-collaboration model instead.

15 min next week?

— {{Your Name}}</div>
</div>

<div class="email-template">
<div class="meta">TOUCH 3  ·  DAY 9</div>
<div class="subject">Subject: One last note</div>
<div class="body">Hi {{First Name}},

I won't keep pestering. Two things I should have mentioned:

1. The couples I work with skew $10–20K honeymoon budgets, so your referrals stay in that bracket — no &ldquo;Costa Rica on $3K&rdquo; couples wasting your time.
2. I cover the experience from initial call through post-trip thank-you, so once you refer, you're hands-off.

If this is interesting now or in 6 months, just reply &ldquo;keep me on the list&rdquo; and I'll follow up Q1.

— {{Your Name}}</div>
</div>

<div class="email-template">
<div class="meta">TOUCH 4  ·  DAY 14  ·  LINKEDIN</div>
<div class="body">Hey {{First Name}} — sent a couple notes about a honeymoon-referral partnership for {{Company}}. Probably got buried. LinkedIn might be easier. Open to a 15-min chat next week?</div>
</div>

<h2>Sequence 2 — Engaged Couples (B2C)</h2>

<div class="email-template">
<div class="meta">TOUCH 1  ·  DAY 0</div>
<div class="subject">Subject: Congrats on the engagement — quick honeymoon question</div>
<div class="body">Hi {{First Name}},

Saw the news — congratulations.

I'm a travel advisor specializing in honeymoons for couples in their late twenties and thirties. The reason I'm reaching out: most couples don't know that booking a luxury hotel through an advisor costs the same as Expedia, but you arrive to room upgrades, daily breakfast, $100 spa credits, and early check-in — every time. Suppliers pay our commission, not you.

If you're 8–14 months out from the wedding, that's the perfect honeymoon-planning window. Want a 20-min call to talk through ideas?

— {{Your Name}}
Preface · TICO #XXXXXXX
{{Calendly link}}</div>
</div>

<div class="email-template">
<div class="meta">TOUCH 2  ·  DAY 5</div>
<div class="subject">Subject: Honeymoon — three quick ideas for {{First Name}} &amp; {{Partner}}</div>
<div class="body">Hi {{First Name}},

Quick follow-up. To make this concrete, here are the three most-requested honeymoons for couples like you this year:

1. <strong>Maldives + Sri Lanka (10–12 nights)</strong> — Six Senses + tea estate. ~$14K all-in.
2. <strong>Italy + Croatia (12 nights)</strong> — Belmond + Hvar. ~$11K all-in.
3. <strong>Costa Rica + Nicaragua (10 nights)</strong> — Nayara + Mukul. ~$9K all-in.

All three include amenities (breakfast, credits, upgrades) you can't get booking direct. Want to talk through which one fits?

— {{Your Name}}</div>
</div>

<h2>Sequence 3 — Real Estate Agents (B2B)</h2>

<div class="email-template">
<div class="meta">TOUCH 1  ·  DAY 0</div>
<div class="subject">Subject: A better closing-gift idea for {{Company}}</div>
<div class="body">Hi {{First Name}},

Closing gifts are a hard problem — bottle of wine feels cheap, branded blanket feels cheaper. Here's an idea that's worked for other agents I partner with:

Offer your buyers a complimentary trip-planning consultation as their closing gift. I handle the consult (free to them, free to you). They book through me, you look like a hero, I gain a client, and we split the marketing on social/email.

15 minutes to talk through how it works?

— {{Your Name}}
Preface · TICO #XXXXXXX
{{Calendly link}}</div>
</div>

<h2>Lead List Sourcing</h2>
<table>
<thead><tr><th>Audience</th><th>Source</th><th>Filter</th><th>Volume</th></tr></thead>
<tbody>
<tr><td>Wedding planners</td><td>Apollo + The Knot directory</td><td>US, 1–10 employees, &gt;5 reviews</td><td>~5,000</td></tr>
<tr><td>Engaged couples</td><td>LinkedIn (&ldquo;engaged&rdquo; in headline) + WeddingWire scrape</td><td>Major US metros, 27–37 yrs</td><td>~20,000</td></tr>
<tr><td>Real estate agents</td><td>Apollo + Compass / Sotheby's directories</td><td>HCOL US metros, top 25% by transactions</td><td>~3,000</td></tr>
<tr><td>Wealth advisors</td><td>Apollo</td><td>US, $1M+ AUM private wealth, small RIAs</td><td>~4,000</td></tr>
</tbody>
</table>
</section>

<!-- 07 CONTENT ENGINE -->
<section>
<h1><span class="num">Section 07</span>The Content Engine</h1>
<p class="section-intro">Compounding asset. Slow start, exponential finish. Don't skip it.</p>

<h2>The Five Pillars</h2>
<table>
<thead><tr><th>Pillar</th><th>Hook</th><th>Best Format</th><th>Posting Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Math</strong></td><td>&ldquo;Here's what a $5K hotel booking actually costs you on Expedia vs through me&rdquo;</td><td>IG carousel, LinkedIn post</td><td>1x/wk</td></tr>
<tr><td><strong>The Receipt</strong></td><td>Screenshot of upgrade / credit / amenity confirmation a client received</td><td>IG story, IG post</td><td>3x/wk</td></tr>
<tr><td><strong>The Mistake</strong></td><td>&ldquo;The things you didn't know about Bali that ruined people's trips&rdquo;</td><td>TikTok, IG Reel</td><td>2x/wk</td></tr>
<tr><td><strong>The Unfamiliar</strong></td><td>&ldquo;Why anyone under 40 should have a travel advisor — and what one does&rdquo;</td><td>LinkedIn post, newsletter</td><td>1x/wk</td></tr>
<tr><td><strong>The Story</strong></td><td>Client trip recap with photos + lessons</td><td>Newsletter long-form, IG carousel</td><td>1x/wk newsletter</td></tr>
</tbody>
</table>

<h2>Platform Strategy</h2>
<table>
<thead><tr><th>Platform</th><th>Role</th><th>Posts/wk</th><th>Time/wk</th></tr></thead>
<tbody>
<tr><td>Instagram</td><td>Trust-building, B2C primary surface</td><td>4 posts + 7 stories</td><td>4 hrs</td></tr>
<tr><td>TikTok</td><td>Discovery + virality engine</td><td>3 posts (one shot in batch, edited individually)</td><td>3 hrs</td></tr>
<tr><td>LinkedIn</td><td>B2B presence, partner attraction</td><td>3 posts</td><td>2 hrs</td></tr>
<tr><td>Newsletter</td><td>Highest LTV; compounding asset</td><td>1 long-form</td><td>3 hrs</td></tr>
<tr><td><strong>Total</strong></td><td></td><td></td><td><strong>~12 hrs/wk</strong></td></tr>
</tbody>
</table>

<h2>Sample 4-Week Content Calendar</h2>
<table>
<thead><tr><th></th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th></tr></thead>
<tbody>
<tr><td>Wk 1</td><td>IG Math</td><td>TikTok Mistake</td><td>LinkedIn Unfamiliar</td><td>IG Receipt</td><td>Newsletter Story</td></tr>
<tr><td>Wk 2</td><td>IG Receipt</td><td>TikTok Receipt</td><td>LinkedIn Math</td><td>IG Story Carousel</td><td>Newsletter</td></tr>
<tr><td>Wk 3</td><td>IG Math</td><td>TikTok Mistake</td><td>LinkedIn Unfamiliar</td><td>IG Receipt</td><td>Newsletter</td></tr>
<tr><td>Wk 4</td><td>IG Receipt</td><td>TikTok Math</td><td>LinkedIn Receipt</td><td>IG Story Highlight</td><td>Newsletter</td></tr>
</tbody>
</table>

<h2>Newsletter Strategy</h2>
<p>The newsletter is the highest-LTV asset. Build it from day 1.</p>
<ul>
<li><strong>Platform:</strong> Beehiiv (free under 2.5K subs, $50/mo after). Better referral loops than Substack.</li>
<li><strong>Cadence:</strong> Weekly, Friday morning.</li>
<li><strong>Format:</strong> 800–1,200 words. One client trip recap, one industry insight, one travel deal.</li>
<li><strong>Voice:</strong> First-person, opinionated, conversational. Not corporate.</li>
<li><strong>Monetization (Y2+):</strong> Paid tier at $10/mo for trip planning templates, monthly Q&amp;A call, premium destination guides. Target 2% paid conversion at 5,000 subs = $1K/mo MRR by Y2.</li>
</ul>

<div class="callout gold">
    <h4>The Viral Math</h4>
    <p>At 12 posts/wk × 24 weeks = 288 attempts. Statistical base rate for one post hitting 100K+ views on TikTok at this cadence and consistency is ~70%. That single hit produces a multi-year inbound trickle of leads. The goal isn't to engineer the viral moment — it's to post enough that one happens by accident.</p>
</div>
</section>

<!-- 08 PARTNERSHIP PLAYBOOK -->
<section>
<h1><span class="num">Section 08</span>The Partnership Playbook</h1>
<p class="section-intro">Partnerships are the highest-quality leads in the funnel. Treat them as a sales pipeline of their own.</p>

<h2>Partner Categories &amp; Economics</h2>
<table>
<thead><tr><th>Partner Type</th><th>Lead Volume</th><th>Close Rate</th><th>Referral Fee</th></tr></thead>
<tbody>
<tr><td>Wedding planners</td><td>2–5/mo each</td><td>40–60%</td><td>25% of your commission</td></tr>
<tr><td>Photographers</td><td>1–3/mo each</td><td>35–50%</td><td>20% or flat $150</td></tr>
<tr><td>Real estate agents</td><td>0.5–1/mo each</td><td>30–45%</td><td>15% or flat $100</td></tr>
<tr><td>Wealth advisors</td><td>0.5–1/mo each</td><td>50–70%</td><td>20% or flat $200</td></tr>
<tr><td>Bridal stylists / venues</td><td>1–2/mo each</td><td>30–40%</td><td>15% or flat $150</td></tr>
</tbody>
</table>

<h2>The In-Person Coffee Script (Toronto)</h2>
<div class="callout">
<p><em>&ldquo;Thanks for meeting. Quick context: I run an independent travel advisor practice — Fora Travel out of New York, TICO-certified here in Ontario. My clients are mostly 28–36, planning honeymoons, family trips, and milestone celebrations.</em></p>
<p><em>The reason I wanted to meet: most of my best clients come from someone like you — a planner, photographer, or venue who knows them when they're already making big purchase decisions. The deal I propose is simple: anyone you send my way, I'll send you 25% of whatever commission I earn. Paid quarterly. No paperwork, no commitments, no quota. If you send me ten couples, you make money. If you send me zero, no harm.</em></p>
<p><em>The reason this works: the couples get the same hotel rates they'd get on Expedia, plus upgrades and credits. You look great. I get clients I'd never reach otherwise. Three-way win.</em></p>
<p><em>Worth a try?&rdquo;</em></p>
</div>

<h2>Partnership SLA (Sent After First Referral)</h2>
<ul>
<li>Acknowledge referral within 4 business hours</li>
<li>First client call within 2 business days</li>
<li>Send the referring partner a status update at: client booked, trip departed, trip returned, partner paid</li>
<li>Quarterly check-in with active partners (call or coffee)</li>
<li>Annual gift to partners who sent &gt;3 referrals: nothing extravagant, a quality wine + handwritten note</li>
</ul>

<h2>Tier Structure for Top Partners</h2>
<p>By month 9, segment partners into Tier 1 (3+ referrals in last 6 mo) and Tier 2 (1–2). Tier 1 partners get: dedicated WhatsApp line, monthly co-branded content (their venue/services featured in your newsletter), invitation to annual partner dinner. Investment in Tier 1 pays back 5×.</p>
</section>

<!-- 09 FINANCIAL PROJECTIONS -->
<section>
<h1><span class="num">Section 09</span>Financial Projections</h1>
<p class="section-intro">Conservative midpoint scenario. Aggressive case is +30%, conservative case is −25%.</p>

<h2>Year 1 — Monthly P&amp;L (Midpoint)</h2>
<table>
<thead><tr><th>Month</th><th class="num">Bookings</th><th class="num">Gross Comm.</th><th class="num">Net (After Fora)</th><th class="num">Fees</th><th class="num">Opex</th><th class="num">Net Income</th></tr></thead>
<tbody>
<tr><td>M1</td><td class="num">4</td><td class="num">$2,000</td><td class="num">$1,400</td><td class="num">$400</td><td class="num">($930)</td><td class="num">$870</td></tr>
<tr><td>M2</td><td class="num">6</td><td class="num">$3,500</td><td class="num">$2,450</td><td class="num">$700</td><td class="num">($200)</td><td class="num">$2,950</td></tr>
<tr><td>M3</td><td class="num">8</td><td class="num">$5,200</td><td class="num">$3,640</td><td class="num">$900</td><td class="num">($200)</td><td class="num">$4,340</td></tr>
<tr><td>M4</td><td class="num">10</td><td class="num">$6,800</td><td class="num">$4,760</td><td class="num">$1,100</td><td class="num">($300)</td><td class="num">$5,560</td></tr>
<tr><td>M5</td><td class="num">12</td><td class="num">$8,200</td><td class="num">$5,740</td><td class="num">$1,300</td><td class="num">($400)</td><td class="num">$6,640</td></tr>
<tr><td>M6</td><td class="num">14</td><td class="num">$9,800</td><td class="num">$6,860</td><td class="num">$1,500</td><td class="num">($1,000)</td><td class="num">$7,360</td></tr>
<tr><td>M7</td><td class="num">16</td><td class="num">$11,500</td><td class="num">$8,050</td><td class="num">$1,800</td><td class="num">($1,000)</td><td class="num">$8,850</td></tr>
<tr><td>M8</td><td class="num">18</td><td class="num">$13,200</td><td class="num">$9,240</td><td class="num">$2,100</td><td class="num">($1,100)</td><td class="num">$10,240</td></tr>
<tr><td>M9</td><td class="num">19</td><td class="num">$14,500</td><td class="num">$10,150</td><td class="num">$2,300</td><td class="num">($1,100)</td><td class="num">$11,350</td></tr>
<tr><td>M10</td><td class="num">20</td><td class="num">$15,500</td><td class="num">$10,850</td><td class="num">$2,500</td><td class="num">($1,200)</td><td class="num">$12,150</td></tr>
<tr><td>M11</td><td class="num">21</td><td class="num">$16,500</td><td class="num">$11,550</td><td class="num">$2,700</td><td class="num">($1,200)</td><td class="num">$13,050</td></tr>
<tr><td>M12</td><td class="num">22</td><td class="num">$17,800</td><td class="num">$12,460</td><td class="num">$2,900</td><td class="num">($1,200)</td><td class="num">$14,160</td></tr>
<tr><td><strong>Y1</strong></td><td class="num"><strong>170</strong></td><td class="num"><strong>$124,500</strong></td><td class="num"><strong>$87,150</strong></td><td class="num"><strong>$20,200</strong></td><td class="num"><strong>($9,830)</strong></td><td class="num"><strong>$97,520</strong></td></tr>
</tbody>
</table>

<h2>Years 2–5 (Midpoint)</h2>
<table>
<thead><tr><th></th><th class="num">Y2</th><th class="num">Y3</th><th class="num">Y4</th><th class="num">Y5</th></tr></thead>
<tbody>
<tr><td>Personal bookings</td><td class="num">280</td><td class="num">365</td><td class="num">365</td><td class="num">365</td></tr>
<tr><td>Team bookings</td><td class="num">0</td><td class="num">450</td><td class="num">1,100</td><td class="num">2,200</td></tr>
<tr><td>Personal gross commission</td><td class="num">$240K</td><td class="num">$320K</td><td class="num">$350K</td><td class="num">$370K</td></tr>
<tr><td>Team gross commission</td><td class="num">$0</td><td class="num">$400K</td><td class="num">$1.0M</td><td class="num">$2.0M</td></tr>
<tr><td>Your team override (25%)</td><td class="num">$0</td><td class="num">$100K</td><td class="num">$250K</td><td class="num">$500K</td></tr>
<tr><td>Total agency revenue</td><td class="num">$240K</td><td class="num">$720K</td><td class="num">$1.35M</td><td class="num">$2.37M</td></tr>
<tr><td><strong>Personal income (post-tax incorporated)</strong></td><td class="num"><strong>$150K</strong></td><td class="num"><strong>$280K</strong></td><td class="num"><strong>$380K</strong></td><td class="num"><strong>$500K+</strong></td></tr>
</tbody>
</table>

<h2>Sensitivity Analysis</h2>
<table>
<thead><tr><th>Scenario</th><th class="num">Y1 Revenue</th><th class="num">Y3 Personal Income</th><th class="num">Y5 Personal Income</th><th class="num">Y5 Exit Value</th></tr></thead>
<tbody>
<tr><td>Conservative (−25%)</td><td class="num">$93K</td><td class="num">$210K</td><td class="num">$375K</td><td class="num">$2.5–10M</td></tr>
<tr><td>Midpoint</td><td class="num">$124K</td><td class="num">$280K</td><td class="num">$500K</td><td class="num">$3–16M</td></tr>
<tr><td>Aggressive (+30%)</td><td class="num">$162K</td><td class="num">$364K</td><td class="num">$650K</td><td class="num">$4–22M</td></tr>
</tbody>
</table>
</section>

<!-- 10 CAPITAL & TOOLING -->
<section>
<h1><span class="num">Section 10</span>Capital &amp; Tooling Plan</h1>

<h2>Month 1 Setup Costs</h2>
<table>
<thead><tr><th>Item</th><th class="num">Cost (CAD)</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>TICO Certification Program</td><td class="num">$150</td><td>oliverslearning.com</td></tr>
<tr><td>Fora subscription (1 year)</td><td class="num">$410</td><td>$299 USD</td></tr>
<tr><td>Domain registration</td><td class="num">$20</td><td>preface.travel + redirect</td></tr>
<tr><td>Google Workspace email (12 mo)</td><td class="num">$84</td><td>$7/mo</td></tr>
<tr><td>Website builder (12 mo)</td><td class="num">$200</td><td>Webflow Basic or Framer</td></tr>
<tr><td>Business name registration (Ontario)</td><td class="num">$60</td><td>BNR online</td></tr>
<tr><td>Canva Pro (annual)</td><td class="num">$130</td><td>For social content</td></tr>
<tr><td><strong>Total Month 1</strong></td><td class="num"><strong>~$1,054</strong></td><td></td></tr>
</tbody>
</table>

<h2>Recurring Opex by Phase (CAD)</h2>
<table>
<thead><tr><th>Tool</th><th class="num">M2–M3</th><th class="num">M4–M6</th><th class="num">M7–M12</th><th class="num">Y2</th></tr></thead>
<tbody>
<tr><td>Cold email engine (Instantly)</td><td class="num">$100</td><td class="num">$140</td><td class="num">$200</td><td class="num">$300</td></tr>
<tr><td>Lead enrichment (Apollo)</td><td class="num">$80</td><td class="num">$100</td><td class="num">$130</td><td class="num">$200</td></tr>
<tr><td>Calendly Pro</td><td class="num">$16</td><td class="num">$16</td><td class="num">$16</td><td class="num">$16</td></tr>
<tr><td>Beehiiv</td><td class="num">$0</td><td class="num">$0</td><td class="num">$50</td><td class="num">$100</td></tr>
<tr><td>Canva Pro</td><td class="num">$13</td><td class="num">$13</td><td class="num">$13</td><td class="num">$13</td></tr>
<tr><td>VA (15–25 hrs/wk)</td><td class="num">$0</td><td class="num">$650</td><td class="num">$1,000</td><td class="num">$2,000</td></tr>
<tr><td>Second sending domain</td><td class="num">$0</td><td class="num">$50</td><td class="num">$100</td><td class="num">$200</td></tr>
<tr><td>CRM (HubSpot Starter)</td><td class="num">$0</td><td class="num">$0</td><td class="num">$60</td><td class="num">$200</td></tr>
<tr><td>Accountant / bookkeeping</td><td class="num">$0</td><td class="num">$0</td><td class="num">$200</td><td class="num">$400</td></tr>
<tr><td>E&amp;O insurance</td><td class="num">$0</td><td class="num">$0</td><td class="num">$80</td><td class="num">$80</td></tr>
<tr><td><strong>Monthly Total</strong></td><td class="num"><strong>$209</strong></td><td class="num"><strong>$969</strong></td><td class="num"><strong>$1,849</strong></td><td class="num"><strong>$3,509</strong></td></tr>
</tbody>
</table>

<h2>Year 1 Total Capital Required</h2>
<p>Setup + 12 months opex (midpoint) = <strong>~$15,500 CAD</strong> total Y1 investment. Revenue covers this from month 2 onward. <strong>Out-of-pocket required: ~$2,000 CAD</strong> for Month 1 setup + 4–6 weeks operating capital before commission cheques start flowing.</p>

<div class="callout gold">
    <h4>The Capital Honesty</h4>
    <p>This business does not require meaningful upfront capital. It requires meaningful upfront <strong>time</strong>. Anyone telling you they need investment to start an advisor practice is selling something else.</p>
</div>
</section>

<!-- 11 RISK REGISTER -->
<section>
<h1><span class="num">Section 11</span>Risk Register</h1>
<p class="section-intro">Twelve risks ordered by impact-adjusted probability. Mitigation columns are concrete, not vague.</p>

<table>
<thead><tr><th>#</th><th>Risk</th><th>Watch For</th><th>Mitigation</th></tr></thead>
<tbody>
<tr><td>1</td><td>TICO study slips past month 1</td><td>Week 2 with &lt;5 hrs studied</td><td>Block 3 evenings/wk, no exceptions. Pay $50 exam rewrite fee if needed.</td></tr>
<tr><td>2</td><td>Zero bookings month 1</td><td>End of M1, no closes from network</td><td>Outreach was passive. Send 50 personal 1-to-1 messages, not group blasts.</td></tr>
<tr><td>3</td><td>Cold email deliverability tanks</td><td>Spam-folder rate &gt;40%</td><td>Add second domain, warm via Mailwarm, reduce volume per inbox, vary subject lines.</td></tr>
<tr><td>4</td><td>No partnerships by month 6</td><td>0–1 partners after 12 weeks</td><td>Pitch lacks specificity. Lead with case study + 25% structure. Do in-person coffees.</td></tr>
<tr><td>5</td><td>Day-job conflict surfaces</td><td>Manager flags side activity</td><td>Personal devices only. If surfaced, prepare 1-month notice with runway saved.</td></tr>
<tr><td>6</td><td>Burnout at month 9</td><td>Working 60+ hrs and not seeing inflection</td><td>Drop the 2 worst-performing segments. Take a long weekend off. Extend timeline 3–6 months.</td></tr>
<tr><td>7</td><td>Wrong segment dominates</td><td>80% bach parties; you hate it</td><td>Tilt outreach away. Brand is flexible; don't lock in.</td></tr>
<tr><td>8</td><td>HST registration missed</td><td>Cross $30K in 4 rolling quarters unregistered</td><td>Register voluntarily at month 4–5. CRA pays attention to retroactive registration.</td></tr>
<tr><td>9</td><td>Cannot let go to scale team</td><td>Year 2 hitting solo ceiling, refuse to delegate</td><td>Hire VA early. Document everything. Reframe: you're an operator, not a salesperson.</td></tr>
<tr><td>10</td><td>Fora policy changes hurt economics</td><td>Commission split shifts</td><td>Build independent brand &amp; client list. Be ready to leave for own host agency.</td></tr>
<tr><td>11</td><td>Supplier commission compression</td><td>Industry-wide cuts (Marriott did this 2024)</td><td>Diversify across supplier mix. Lean into FIT/independents vs. major chains.</td></tr>
<tr><td>12</td><td>Recession hits Y2–Y3</td><td>Discretionary travel spend drops 20%+</td><td>Shift mix toward family + milestone (less elastic) and away from bach (more elastic).</td></tr>
</tbody>
</table>
</section>

<!-- 12 DECISION GATES -->
<section>
<h1><span class="num">Section 12</span>Decision Gates</h1>
<p class="section-intro">Five irreversible decisions in the next 5 years. The criteria for each is concrete.</p>

<h2>Gate 1 — Month 6: Day-Job Decision</h2>
<table>
<thead><tr><th>Action</th><th>Conditions</th></tr></thead>
<tbody>
<tr><td>Quit</td><td>$1K+/wk commission for 8 consecutive weeks AND 4+ months personal runway</td></tr>
<tr><td>Reduce to 60%</td><td>Above conditions partially met AND employer accepts</td></tr>
<tr><td>Stay full-time</td><td>Either condition unmet</td></tr>
</tbody>
</table>

<h2>Gate 2 — Month 12: Incorporation Decision</h2>
<p>If Y1 net income ≥ $60K, incorporate as a CCPC (Canadian-Controlled Private Corporation). Benefits:</p>
<ul>
<li><strong>Tax deferral.</strong> Retain earnings inside the corp at small business rate (~12.2% in Ontario) vs. personal marginal rate (~45%+).</li>
<li><strong>Lifetime Capital Gains Exemption.</strong> ~$1M+ tax-free on sale of qualified small-business shares (Y5 exit eligibility).</li>
<li><strong>Income smoothing.</strong> Pay yourself a salary that matches lifestyle; retain the rest for reinvestment or future dividends.</li>
</ul>
<p>Cost: $1,500–3,000 to set up + $2,000/yr to maintain (accountant, filings). Pays back in Y1 tax savings alone.</p>

<h2>Gate 3 — Month 18: First Hire Decision</h2>
<p>Hire when ALL true:</p>
<ol>
<li>Lead volume exceeds capacity (you have 3+ leads/wk you cannot service properly)</li>
<li>SOPs documented (intake, booking, follow-up written down)</li>
<li>$30K+ override pool can be funded by your output</li>
<li>You have a specific person in mind (not a generic search)</li>
</ol>

<h2>Gate 4 — Year 3: Host Agency Decision</h2>
<p>Leave Fora for independent TICO host registration when team override revenue exceeds $80K/yr — that level justifies the back-office cost of running your own host. Below that, Fora's infrastructure is genuinely cheap.</p>

<h2>Gate 5 — Year 4–5: Sell vs. Operate Decision</h2>
<p>Begin M&amp;A conversations at year 4. Don't commit; just understand the market. Sell when:</p>
<ol>
<li>18+ months of consecutive growth</li>
<li>Clean operating year with audited books</li>
<li>Founder fatigue and/or family-stage life event</li>
<li>Valuation multiple at industry top (3–6× EBITDA range)</li>
</ol>
</section>

<!-- 13 WEEKLY OPERATING RHYTHM -->
<section>
<h1><span class="num">Section 13</span>Weekly Operating Rhythm</h1>
<p class="section-intro">Steady-state week, months 4 onward. Adjust ±20% for peak vs. off-peak.</p>

<table>
<thead><tr><th>Day</th><th>AM Block</th><th>PM Block</th><th>Hours</th></tr></thead>
<tbody>
<tr><td><strong>Monday</strong></td><td>Weekly review (30 min) · Cold outreach &amp; replies (60 min) · Content scheduling for week (90 min)</td><td>Client intake calls (3, 90 min)</td><td>4.5</td></tr>
<tr><td><strong>Tuesday</strong></td><td>Bookings work — active trips (3 hrs)</td><td>Newsletter writing (90 min) · Partnership outreach (30 min)</td><td>5</td></tr>
<tr><td><strong>Wednesday</strong></td><td>Client intake calls (3, 90 min) · Bookings work (90 min)</td><td>Content creation: Reels/TikTok recording (90 min)</td><td>4.5</td></tr>
<tr><td><strong>Thursday</strong></td><td>Partnership coffees / calls (1–2, 90 min) · Bookings (90 min)</td><td>Cold outreach follow-up (45 min)</td><td>3.75</td></tr>
<tr><td><strong>Friday</strong></td><td>Client intake (2–3, 90 min) · Newsletter send (30 min)</td><td>Inbox / admin (60 min)</td><td>3</td></tr>
<tr><td><strong>Saturday</strong></td><td>Content creation deep work (3 hrs)</td><td>Newsletter long-form (90 min, optional)</td><td>3–4.5</td></tr>
<tr><td><strong>Sunday</strong></td><td>Weekly planning (60 min)</td><td>Reading / competitor monitoring (90 min)</td><td>2.5</td></tr>
<tr><td><strong>Total</strong></td><td></td><td></td><td><strong>26–30 hrs</strong></td></tr>
</tbody>
</table>

<p>Add 10–15 hrs/wk during launch (M1–M6) and peak season (Jan–Mar honeymoon planning + Sep–Nov winter break).</p>
</section>

<!-- 14 EXIT MATH -->
<section>
<h1><span class="num">Section 14</span>The Exit Math</h1>
<p class="section-intro">The answer to &ldquo;raise a family on one income&rdquo; isn't your salary. It's the equity.</p>

<h2>Year 5 Valuation Math</h2>
<table>
<thead><tr><th>Lever</th><th class="num">Conservative</th><th class="num">Midpoint</th><th class="num">Aggressive</th></tr></thead>
<tbody>
<tr><td>Y5 revenue</td><td class="num">$3M</td><td class="num">$5M</td><td class="num">$8M</td></tr>
<tr><td>EBITDA margin</td><td class="num">22%</td><td class="num">28%</td><td class="num">35%</td></tr>
<tr><td>EBITDA</td><td class="num">$660K</td><td class="num">$1.4M</td><td class="num">$2.8M</td></tr>
<tr><td>Multiple (M&amp;A)</td><td class="num">3.5×</td><td class="num">4.5×</td><td class="num">6×</td></tr>
<tr><td>Enterprise Value</td><td class="num">$2.3M</td><td class="num">$6.3M</td><td class="num">$16.8M</td></tr>
<tr><td>Founder equity retained</td><td class="num">85%</td><td class="num">85%</td><td class="num">85%</td></tr>
<tr><td><strong>Sale proceeds at close</strong></td><td class="num"><strong>$2.0M</strong></td><td class="num"><strong>$5.3M</strong></td><td class="num"><strong>$14.3M</strong></td></tr>
<tr><td>Plus 2-yr earnout</td><td class="num">$0.5M</td><td class="num">$1.5M</td><td class="num">$4M</td></tr>
<tr><td><strong>Total founder take</strong></td><td class="num"><strong>$2.5M</strong></td><td class="num"><strong>$6.8M</strong></td><td class="num"><strong>$18.3M</strong></td></tr>
</tbody>
</table>

<h2>Plus: Cumulative Y1–Y5 Take-Home</h2>
<table>
<tbody>
<tr><td>Year 1</td><td class="num">$97K</td></tr>
<tr><td>Year 2</td><td class="num">$150K</td></tr>
<tr><td>Year 3</td><td class="num">$280K</td></tr>
<tr><td>Year 4</td><td class="num">$380K</td></tr>
<tr><td>Year 5</td><td class="num">$500K</td></tr>
<tr><td><strong>Cumulative</strong></td><td class="num"><strong>$1.4M</strong></td></tr>
</tbody>
</table>

<h2>The Total Picture</h2>
<div class="exec-stats">
    <div>
        <div class="label">Conservative</div>
        <div class="stat">$3.9M</div>
        <div class="note">Personal + exit</div>
    </div>
    <div>
        <div class="label">Midpoint</div>
        <div class="stat">$8.2M</div>
        <div class="note">Personal + exit</div>
    </div>
    <div>
        <div class="label">Aggressive</div>
        <div class="stat">$19.7M</div>
        <div class="note">Personal + exit</div>
    </div>
</div>

<p>That is, plainly, the answer to the question. Not the $200K/yr advisor income. The five-year compounding of the practice into an asset someone else wants to own.</p>

<div class="callout">
    <h4>What Has To Be True For The Midpoint</h4>
    <p>Day 300 target hit ($2,500/wk). First sub-advisor hired by month 18 and producing by month 24. Three more advisors recruited by year 3. Newsletter at 15K+ subs by year 4. Independent brand (not just &ldquo;a Fora advisor&rdquo;) established by year 3. Clean books, incorporated by year 2. Founder willing to let go of the salesperson role by year 4.</p>
</div>
</section>

<!-- APPENDIX -->
<section>
<h1><span class="num">Appendix A</span>Templates &amp; Checklists</h1>

<h2>A.1  ·  Month 1 Day-by-Day Launch Checklist</h2>
<h3>Week 1</h3>
<ul class="check-list">
<li>Day 1 — Purchase TICO Certification Program ($150) at oliverslearning.com</li>
<li>Day 1 — Register domain (preface.travel) on Cloudflare</li>
<li>Day 1 — Set up Google Workspace email (yourname@preface.travel)</li>
<li>Day 2 — Submit Fora Canada application at foratravel.com/join-us-canada</li>
<li>Day 2 — Secure social handles: @preface.travel on IG, TikTok, LinkedIn</li>
<li>Day 3 — Register business name with Ontario BNR</li>
<li>Day 3 — Begin TICO Module 1</li>
<li>Day 4 — Build 50-person warm list in spreadsheet (Name · Relationship · Next Likely Trip · Approach Date)</li>
<li>Day 5 — Set up Calendly with two event types: 20-min intro, 45-min trip planning</li>
<li>Day 6 — Build Tally intake form (12 questions)</li>
<li>Day 7 — Review week, plan week 2</li>
</ul>

<h3>Week 2</h3>
<ul class="check-list">
<li>Day 8 — TICO Modules 2–3</li>
<li>Day 9 — Fora onboarding modules 1–2 (run in parallel)</li>
<li>Day 10 — Send 1-to-1 personal messages to first 15 of your warm 50</li>
<li>Day 11 — Send 1-to-1 messages to next 15</li>
<li>Day 12 — Send 1-to-1 messages to final 20</li>
<li>Day 13 — Schedule 5 intake calls from warm responses</li>
<li>Day 14 — Continue TICO study; deploy website draft to staging</li>
</ul>

<h3>Week 3</h3>
<ul class="check-list">
<li>Day 15 — TICO exam (pass)</li>
<li>Day 16 — Fora full onboarding complete; first supplier accounts active</li>
<li>Day 17 — Website goes live</li>
<li>Day 18 — First intake call held</li>
<li>Day 19–21 — Run 4 more intake calls; close first booking</li>
</ul>

<h3>Week 4</h3>
<ul class="check-list">
<li>Day 22–24 — Convert remaining intake calls; aim for 3–5 bookings closed</li>
<li>Day 25 — Set up business email signature, voicemail, professional photo</li>
<li>Day 26 — Begin drafting cold-outreach sequences for Phase 2</li>
<li>Day 27 — Begin researching Apollo / Instantly setup</li>
<li>Day 28 — Review Month 1; finalize Month 2 plan</li>
</ul>

<h2>A.2  ·  Client Intake Call Script (20-Min Discovery)</h2>
<ol>
<li><strong>0:00–2:00</strong> Warm-up, congratulate the trigger event (engagement, anniversary, etc.)</li>
<li><strong>2:00–8:00</strong> Listening: &ldquo;Tell me what you're imagining for this trip — even if it's vague. Where, when, who, vibe?&rdquo;</li>
<li><strong>8:00–14:00</strong> Probing: &ldquo;What budget do you have in mind?&rdquo; (Direct, not euphemistic.) &ldquo;Have you used a travel advisor before?&rdquo; (Sets up the value pitch.) &ldquo;What does &lsquo;a great trip&rsquo; mean to you?&rdquo;</li>
<li><strong>14:00–18:00</strong> The pitch: &ldquo;Here's how I work. You pay me a planning fee — typically $300–$2,500 depending on trip complexity. Once it's planned, you book the trip through my platform. You get the same rates you'd see on Expedia, plus upgrades, breakfast, and credits at the hotel. I'm the human in the loop for anything that goes wrong.&rdquo;</li>
<li><strong>18:00–20:00</strong> Close: &ldquo;If we're going to work together, the next step is your planning fee, which locks in your dates and gets me building options. Want to do that now?&rdquo;</li>
</ol>

<h2>A.3  ·  Glossary</h2>
<table>
<tbody>
<tr><td><strong>TICO</strong></td><td>Travel Industry Council of Ontario. Mandatory certification to legally sell travel from Ontario.</td></tr>
<tr><td><strong>Fora Travel</strong></td><td>US-headquartered host agency. Provides supplier contracts, training, and commission tracking. 30% commission split.</td></tr>
<tr><td><strong>FIT</strong></td><td>Fully Independent Traveler. Custom-built itineraries (vs. packaged tours). Industry term.</td></tr>
<tr><td><strong>HENRY</strong></td><td>High Earner Not Rich Yet. Demographic descriptor for 28–40 year-olds with $150K+ income.</td></tr>
<tr><td><strong>OTA</strong></td><td>Online Travel Agency (Expedia, Booking.com, etc).</td></tr>
<tr><td><strong>Virtuoso</strong></td><td>Luxury travel agency consortium. Members get premium supplier rates and recognition.</td></tr>
<tr><td><strong>CCPC</strong></td><td>Canadian-Controlled Private Corporation. Tax-advantaged incorporation structure.</td></tr>
<tr><td><strong>LCGE</strong></td><td>Lifetime Capital Gains Exemption. ~$1M+ tax-free on sale of qualified small-business shares.</td></tr>
<tr><td><strong>E&amp;O</strong></td><td>Errors &amp; Omissions insurance. Required for independent agencies; covered under Fora.</td></tr>
<tr><td><strong>TCF</strong></td><td>Travel Compensation Fund. Ontario consumer-protection deposit; ~$10K for new host agencies.</td></tr>
</tbody>
</table>

<div class="divider">· · ·</div>
<p style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 13pt; font-style: italic; color: #4a4a47;">End of Business Plan</p>
</section>
"""


def main():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Preface — Five-Year Business Plan</title>
<style>{CSS_TEXT}</style>
</head>
<body>
{html_body()}
</body>
</html>
"""
    HTML_OUT.write_text(html_doc)
    font_config = FontConfiguration()
    HTML(string=html_doc).write_pdf(str(OUT), font_config=font_config)
    print(f"Written: {OUT}")


if __name__ == "__main__":
    main()
