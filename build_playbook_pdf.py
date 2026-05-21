"""Generate the Preface Playbook PDF — Hormozi-style execution manual."""
from pathlib import Path
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import build_plan_pdf as v1

OUT = Path(__file__).parent / "Preface-Playbook.pdf"

EXTRA_CSS = """
.hormozi-rule {
    background: #0A0A0A; color: #FAFAF8;
    padding: 18px 24px; margin: 0.18in 0;
    font-family: 'Inter', sans-serif; font-size: 11pt;
    border-left: 4px solid #A85C3D;
}
.hormozi-rule .label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt; letter-spacing: 0.18em;
    text-transform: uppercase; color: #A85C3D;
    margin-bottom: 8px; font-weight: 600;
}
.hormozi-rule .rule { font-weight: 500; line-height: 1.45; }
.week-block {
    border: 1px solid #d4d2cc; margin: 0.15in 0;
    page-break-inside: avoid;
}
.week-block .week-head {
    background: #0A0A0A; color: #FAFAF8;
    padding: 14px 24px;
    display: flex; justify-content: space-between; align-items: baseline;
}
.week-block .week-head .w {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10pt; letter-spacing: 0.15em;
    color: #A85C3D; font-weight: 600;
}
.week-block .week-head .title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 16pt; font-weight: 500;
}
.week-block .week-head .target {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt; color: #C4C2BD;
}
.week-block .week-body { padding: 16px 24px; background: #FAFAF8; }
.week-block .week-body ul.check-list { margin: 0; }
.week-block .week-body .deliverable {
    margin-top: 12px; padding-top: 12px;
    border-top: 1px solid #e6e4dd;
    font-size: 9.5pt; color: #4a4a47;
    font-style: italic;
}
.script-box {
    background: #f5f3ec; border: 1px solid #d4d2cc;
    border-left: 4px solid #A85C3D;
    padding: 18px 22px; margin: 0.15in 0;
    font-family: 'Inter', sans-serif; font-size: 10pt;
    line-height: 1.55;
}
.script-box .lab {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt; letter-spacing: 0.15em;
    text-transform: uppercase; color: #A85C3D;
    margin-bottom: 12px; font-weight: 600;
}
.script-box .ctx { font-size: 9pt; color: #6B6B6B; margin-bottom: 12px; font-style: italic; }
.script-box em { color: #8B6F47; font-style: italic; }
.kpi-tile {
    display: inline-block; vertical-align: top;
    width: 32%; padding: 14px 16px;
    background: #f5f3ec; border-left: 3px solid #A85C3D;
    margin: 6px 0.5% 6px 0; box-sizing: border-box;
}
.kpi-tile .lab { font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; letter-spacing: 0.12em; text-transform: uppercase; color: #6B6B6B; }
.kpi-tile .val { font-family: 'Cormorant Garamond', serif; font-size: 18pt; color: #0A0A0A; margin-top: 4px; }
.tool-row {
    display: grid; grid-template-columns: 1.4fr 0.7fr 0.5fr 1.4fr;
    gap: 12px; padding: 10px 0;
    border-bottom: 1px solid #e6e4dd;
    font-size: 9.5pt;
}
.tool-row.header { font-weight: 600; color: #A85C3D; border-bottom: 2px solid #0A0A0A; padding-bottom: 8px; }
.funnel-card {
    page-break-inside: avoid;
    border: 1px solid #d4d2cc;
    margin: 0.2in 0;
}
.funnel-card .head {
    background: #A85C3D; color: #FAFAF8;
    padding: 14px 24px;
    display: flex; justify-content: space-between; align-items: baseline;
}
.funnel-card .head .id {
    font-family: 'JetBrains Mono', monospace; font-size: 10pt;
    letter-spacing: 0.15em; color: #FAFAF8; opacity: 0.7;
}
.funnel-card .head .name {
    font-family: 'Cormorant Garamond', serif; font-size: 20pt;
}
.funnel-card .head .goal {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    color: #FAFAF8; opacity: 0.9;
}
.funnel-card .body { padding: 18px 24px; }
"""


def html_body():
    return r"""
<!-- COVER -->
<div class="cover">
    <div class="cover-mark">Preface</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">The Playbook<br/><span style="font-style: italic; font-weight: 300;">Execution Manual</span></h1>
    <div class="cover-subtitle">A Hormozi-style tactical playbook. What to do, when to do it, exactly how, and how to know it worked.</div>
    <div class="cover-meta">
        <div>
            <span class="label">Companion to</span>
            <span class="value">Preface Business Plan v2</span>
        </div>
        <div>
            <span class="label">Time horizon</span>
            <span class="value">Week 1 &mdash; Month 24</span>
        </div>
        <div>
            <span class="label">Format</span>
            <span class="value">Checklists, scripts, workflows, KPIs</span>
        </div>
    </div>
</div>

<!-- CONTENTS -->
<div class="toc">
    <h1><span class="num">Contents</span>Table of Contents</h1>
    <div class="toc-entry"><span class="num">00</span><span class="title">How to Use This Document</span></div>
    <div class="toc-entry"><span class="num">01</span><span class="title">The Operating Principles (Non-Negotiable)</span></div>
    <div class="toc-entry"><span class="num">02</span><span class="title">The Five Funnels</span></div>
    <div class="toc-subentry"><span>2.1   Warm Network Activation</span></div>
    <div class="toc-subentry"><span>2.2   Partnership Engine</span></div>
    <div class="toc-subentry"><span>2.3   Cold Outreach Engine</span></div>
    <div class="toc-subentry"><span>2.4   Content Inbound</span></div>
    <div class="toc-subentry"><span>2.5   Business Travel</span></div>
    <div class="toc-entry"><span class="num">03</span><span class="title">The 16-Week Launch Sprint</span></div>
    <div class="toc-entry"><span class="num">04</span><span class="title">The 150-Person Warm Network Activation</span></div>
    <div class="toc-entry"><span class="num">05</span><span class="title">The Partnership Playbook</span></div>
    <div class="toc-entry"><span class="num">06</span><span class="title">The Business Travel Playbook</span></div>
    <div class="toc-entry"><span class="num">07</span><span class="title">The Content Engine</span></div>
    <div class="toc-subentry"><span>7.1   Voice &amp; the 50/30/20 Mix</span></div>
    <div class="toc-subentry"><span>7.2   Newsletter Playbook</span></div>
    <div class="toc-subentry"><span>7.3   Instagram Playbook</span></div>
    <div class="toc-subentry"><span>7.4   LinkedIn Playbook</span></div>
    <div class="toc-subentry"><span>7.5   TikTok Playbook</span></div>
    <div class="toc-subentry"><span>7.6   12-Week Editorial Calendar</span></div>
    <div class="toc-entry"><span class="num">08</span><span class="title">The Landing Page Library</span></div>
    <div class="toc-entry"><span class="num">09</span><span class="title">The Workflow Library</span></div>
    <div class="toc-entry"><span class="num">10</span><span class="title">The Sales Conversation Playbook</span></div>
    <div class="toc-entry"><span class="num">11</span><span class="title">The KPI Dashboard</span></div>
    <div class="toc-entry"><span class="num">12</span><span class="title">Tool Stack &amp; Cost Schedule</span></div>
    <div class="toc-entry"><span class="num">13</span><span class="title">Decision Trees &amp; Pivot Triggers</span></div>
    <div class="toc-entry"><span class="num">14</span><span class="title">Month-by-Month Goals (M1&ndash;M24)</span></div>
    <div class="toc-entry"><span class="num">A</span><span class="title">Appendix: Templates, Scripts, &amp; Checklists</span></div>
</div>

<!-- 00 HOW TO USE -->
<section>
<h1><span class="num">Section 00</span>How to Use This Document</h1>
<p class="lead">This is the tactical companion to the strategic plan. The plan tells you <em>what</em> Preface is. This tells you <em>what to do tomorrow.</em></p>

<div class="hormozi-rule">
<div class="label">Rule 00</div>
<div class="rule">If a section doesn't have a checklist, a script, a workflow, or a number you're tracking — it's not a section. It's a vibe. Skip the vibes.</div>
</div>

<h2>The Four Question Test</h2>
<p>Before you start any activity in this playbook, the activity must answer four questions. If it can't, you're wasting time.</p>
<ol>
<li><strong>What's the goal?</strong> Stated as a number with a deadline.</li>
<li><strong>What's the first action?</strong> The thing you do in the next 60 minutes.</li>
<li><strong>What's the KPI?</strong> The number you check at the end of the week.</li>
<li><strong>What's the kill condition?</strong> When do you stop and pivot.</li>
</ol>

<h2>The Single Rule of Sequencing</h2>
<p>Run the funnels in this order. Don't move to the next one until the previous one is producing.</p>
<table>
<thead><tr><th>Sequence</th><th>Funnel</th><th>Move on when</th></tr></thead>
<tbody>
<tr><td>1</td><td>Warm Network (M1)</td><td>5 bookings closed</td></tr>
<tr><td>2</td><td>Partnerships (M2&ndash;3)</td><td>3+ formal partners signed</td></tr>
<tr><td>3</td><td>Cold Outreach (M2&ndash;4)</td><td>1500 emails/day stable, replies routing to VA</td></tr>
<tr><td>4</td><td>Content Inbound (M4 onward)</td><td>Newsletter at 1,000 subs</td></tr>
<tr><td>5</td><td>Business Travel (M5 onward)</td><td>3 corporate accounts signed</td></tr>
</tbody>
</table>
<p>Running everything in parallel before any one is working is the most common founder mistake. Each funnel takes ~3 weeks of focused activation to produce. Don't start a new one until the last one is producing predictably.</p>

<h2>How to Read the Weekly Checklists</h2>
<ul>
<li>Each week has 3&ndash;5 items. Not 15.</li>
<li>Items are written as "Do X" not "Think about Y."</li>
<li>The deliverable line is what you produce by Friday EOW.</li>
<li>If you complete the list, you're on pace. If not, the next week's items don't change &mdash; you compress instead.</li>
</ul>
</section>

<!-- 01 OPERATING PRINCIPLES -->
<section>
<h1><span class="num">Section 01</span>The Operating Principles (Non-Negotiable)</h1>

<div class="hormozi-rule">
<div class="label">Principle 01</div>
<div class="rule"><strong>Volume + iteration &gt; Strategy.</strong> The plan you'll execute is the 80% plan you start with this week, not the 100% plan you'll figure out next month. Send 50 cold emails today, not 5 perfect ones next Monday.</div>
</div>

<div class="hormozi-rule">
<div class="label">Principle 02</div>
<div class="rule"><strong>Build the funnel before you optimize it.</strong> The first version of every funnel will convert poorly. That's fine. You can't optimize what you haven't built. Get to 100 conversations before you A/B test the script.</div>
</div>

<div class="hormozi-rule">
<div class="label">Principle 03</div>
<div class="rule"><strong>Every channel gets 90 days, then a verdict.</strong> If a channel isn't producing measurable output after 90 days of consistent effort, kill it. Don't be sentimental. Sentiment is how you become a content creator who doesn't sell trips.</div>
</div>

<div class="hormozi-rule">
<div class="label">Principle 04</div>
<div class="rule"><strong>Make &gt; Schedule &gt; Reply &gt; Optimize.</strong> In that order, every day. Block your highest-cognitive hour for new outbound (Make), then schedule the calls you booked yesterday (Schedule), then reply to inbound (Reply), then optimize anything (Optimize). Reversed: you'll spend the day in your inbox and ship nothing.</div>
</div>

<div class="hormozi-rule">
<div class="label">Principle 05</div>
<div class="rule"><strong>The dollar-per-hour test.</strong> If a task pays less than $40/hr at your current run-rate, the VA does it. If it pays less than $100/hr, you only do it when no VA can. Below that math, your time is the constraint &mdash; not your money.</div>
</div>

<div class="hormozi-rule">
<div class="label">Principle 06</div>
<div class="rule"><strong>Two-week pivot horizon.</strong> Strategic pivots happen at two-week intervals, not daily. You decide on Day 1 of a sprint what you'll execute. You don't change the plan until Day 14, even if a sexier idea shows up on Day 7. The sexier idea goes in the queue, not the schedule.</div>
</div>

<div class="hormozi-rule">
<div class="label">Principle 07</div>
<div class="rule"><strong>One number per week.</strong> The week is owned by one metric: net commission booked. Not impressions. Not followers. Not partnerships in motion. Booked. Closed. Money-in-mouth. Everything else is a leading indicator and leading indicators lie.</div>
</div>

<h2>What You Will Not Do</h2>
<p>These look productive. They aren't. Avoid:</p>
<ul>
<li><strong>Rebrand work after Week 4.</strong> The brand is the brand. Iterating fonts and palettes is procrastination.</li>
<li><strong>Tool research beyond Week 2.</strong> The tools are picked. Stop browsing alternatives.</li>
<li><strong>Networking events with no specific outcome.</strong> Coffees with named people, yes. "Travel agent meetups," no.</li>
<li><strong>FAM trips that aren't fully comped.</strong> You'll be tempted. Don't. Your CV is already strong enough.</li>
<li><strong>Building a course / e-book / training in Y1.</strong> You'd be teaching what you don't yet know.</li>
<li><strong>Writing replies longer than the inbound message.</strong> Your reply length should be 50&ndash;80% of theirs.</li>
</ul>
</section>

<!-- 02 FIVE FUNNELS -->
<section>
<h1><span class="num">Section 02</span>The Five Funnels</h1>
<p class="section-intro">Every dollar of revenue enters through one of these five funnels. Build them in order. Track each independently.</p>

<div class="funnel-card">
    <div class="head">
        <div>
            <div class="id">FUNNEL A</div>
            <div class="name">Warm Network Activation</div>
        </div>
        <div class="goal">M1&ndash;6 · 50&ndash;80 bookings · 60% of Y1 revenue</div>
    </div>
    <div class="body">
        <p><strong>Mechanic:</strong> Your existing 150-person Toronto/Thornhill network → 1-to-1 messages → coffees → bookings → referrals.</p>
        <p><strong>Stages of the funnel:</strong></p>
        <ol>
            <li>List built (150 names with context) &mdash; <strong>Week 1</strong></li>
            <li>Initial message sent (1-to-1, personal) &mdash; <strong>Week 2&ndash;4</strong></li>
            <li>Coffee/call scheduled &mdash; <strong>Week 3&ndash;6</strong></li>
            <li>Trip context surfaced &mdash; <strong>during coffee/call</strong></li>
            <li>Proposal sent &mdash; <strong>within 48h of call</strong></li>
            <li>Booking closed &mdash; <strong>within 7 days of proposal</strong></li>
            <li>Referral asked (post-trip) &mdash; <strong>3 days after they return</strong></li>
        </ol>
        <p><strong>Conversion targets:</strong> 30% reply rate → 50% of replies become calls → 40% of calls become proposals → 60% of proposals close. End-to-end on a 150-person list = ~5-9 bookings from cold + 15&ndash;25 more across 6 months from warm follow-ups.</p>
        <p><strong>Kill condition:</strong> If end-of-M2 shows &lt;15 reply, you re-do messaging (not list).</p>
    </div>
</div>

<div class="funnel-card">
    <div class="head">
        <div>
            <div class="id">FUNNEL B</div>
            <div class="name">Partnership Engine</div>
        </div>
        <div class="goal">M2&ndash;ongoing · 20+ active partners by Y2 · 25% of Y1 revenue</div>
    </div>
    <div class="body">
        <p><strong>Mechanic:</strong> Wedding planners, real estate agents, mortgage brokers, photographers, jewelers, financial advisors → referral agreements (25% commission share) → repeat referrals.</p>
        <p><strong>Stages:</strong></p>
        <ol>
            <li>Target list of 50 named partners by sector</li>
            <li>Cold message OR warm intro to 20 in M2&ndash;3</li>
            <li>15 coffees scheduled</li>
            <li>5&ndash;8 sign formal agreement</li>
            <li>Each delivers 2&ndash;5 referrals/yr (average)</li>
            <li>Top 20% deliver 80% of partnership volume</li>
        </ol>
        <p><strong>The compounding:</strong> Year 1 = 8 partners × 3 referrals/year = 24 referrals. Year 2 = 18 partners × 4 referrals = 72 referrals. The partnership engine takes 6 months to seed and 12 months to compound.</p>
        <p><strong>Kill condition:</strong> Drop any partner producing &lt;1 referral in 9 months. Keep the relationship; remove from active outreach.</p>
    </div>
</div>

<div class="funnel-card">
    <div class="head">
        <div>
            <div class="id">FUNNEL C</div>
            <div class="name">Cold Outreach Engine</div>
        </div>
        <div class="goal">M3&ndash;ongoing · 1500 emails/day · 5&ndash;10 incremental bookings/month</div>
    </div>
    <div class="body">
        <p><strong>Mechanic:</strong> Apollo lead lists → Instantly multi-domain sender → VA reply triage → calls → bookings.</p>
        <p><strong>Two sequences run in parallel:</strong></p>
        <ul>
            <li><strong>B2B sequence:</strong> US wedding planners, real estate agents, mortgage brokers, photographers. Looking for partnership conversations. (See Funnel B.)</li>
            <li><strong>B2C sequence:</strong> Engaged couples from public engagement announcements + family travel intent signals. Looking for bookings directly.</li>
        </ul>
        <p><strong>Funnel math:</strong> 1,500 emails/day × 22 working days = 33,000 emails/month. ~1.5% reply rate = 495 replies/mo → VA filters to ~50 qualified → 30 calls booked → 8 proposals → 5 bookings.</p>
        <p><strong>Kill condition:</strong> If after 90 days the cold funnel is producing &lt;3 bookings/mo, audit deliverability first (Glock Apps test), copy second, list third. Don't kill until you've fixed all three.</p>
    </div>
</div>

<div class="funnel-card">
    <div class="head">
        <div>
            <div class="id">FUNNEL D</div>
            <div class="name">Content Inbound</div>
        </div>
        <div class="goal">M4&ndash;ongoing · 5K subs Y1 / 50K social Y2 · 15% of Y1 → 30% of Y3 revenue</div>
    </div>
    <div class="body">
        <p><strong>Mechanic:</strong> Voice memos from you → VA produces newsletter + IG + TikTok + LinkedIn → subscribers/followers → DMs/intake form → bookings.</p>
        <p><strong>Channel hierarchy:</strong></p>
        <ol>
            <li><strong>Newsletter</strong> (owned channel, biweekly) &mdash; the primary asset</li>
            <li><strong>Instagram</strong> (reach + visual proof) &mdash; the trust channel</li>
            <li><strong>LinkedIn</strong> (business travel + advisor positioning)</li>
            <li><strong>TikTok</strong> (cold reach, viral upside)</li>
            <li><strong>YouTube Shorts</strong> (repurposed TikTok content, evergreen)</li>
        </ol>
        <p><strong>Funnel math (Y1 target):</strong> 5,000 newsletter subs × 1% trip-intent → 50 leads/mo × 30% close → 15 bookings/mo. By Y2, double that.</p>
        <p><strong>Kill condition:</strong> Any individual social channel that doesn't 2x its followers per quarter for two consecutive quarters gets dropped.</p>
    </div>
</div>

<div class="funnel-card">
    <div class="head">
        <div>
            <div class="id">FUNNEL E</div>
            <div class="name">Business Travel</div>
        </div>
        <div class="goal">M5&ndash;ongoing · 5&ndash;10 corporate accounts by Y1 end · 20% of Y2 revenue</div>
    </div>
    <div class="body">
        <p><strong>Mechanic:</strong> LinkedIn-led outreach to SMB executives + sole-prop founders + sales leaders → onboarding call → booking-on-file relationship → 20&ndash;50 trips/year per account.</p>
        <p><strong>Why business travel is different:</strong></p>
        <ul>
            <li><strong>Frequency:</strong> One corporate account = 20&ndash;50 hotel bookings/year vs 1&ndash;2 leisure trips</li>
            <li><strong>Margin:</strong> Lower per-trip ($40&ndash;120 net) but compounded by volume</li>
            <li><strong>Loyalty:</strong> Once they hand you their card, they stay 3&ndash;5 years</li>
            <li><strong>Sales cycle:</strong> 2&ndash;4 weeks (longer than leisure but with lifetime value 10x)</li>
            <li><strong>Counter-cyclical:</strong> Business travel runs Sun&ndash;Thu; leisure runs Fri&ndash;Sun. They fill each other's calendar gaps.</li>
        </ul>
        <p><strong>Why this is your unfair advantage:</strong> You work in sales. You speak the language. Your daytime network already includes the buyer persona. (See Section 06 for the full playbook.)</p>
        <p><strong>Funnel math:</strong> 200 LinkedIn DMs/mo → 30 conversations → 10 discovery calls → 5 signed accounts × 30 trips/yr × $80 net = $12,000/mo recurring by Y1 end.</p>
        <p><strong>Kill condition:</strong> Per-account volume of &lt;10 trips/yr after 6 months means re-pitching the account or replacing them.</p>
    </div>
</div>
</section>

<!-- 03 16-WEEK SPRINT -->
<section>
<h1><span class="num">Section 03</span>The 16-Week Launch Sprint</h1>
<p class="section-intro">From licensed to $1,500/wk in net commissions. Day 1 through Day 112. Day job continues throughout.</p>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 01</div><div class="title">Foundation</div></div>
        <div class="target">Target: Licensed by Day 21</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Buy TICO Certification Program ($150). Schedule study: 3 evenings/wk, 2 hrs each.</li>
            <li>Submit Fora Canada application ($399 CAD). Confirm Toronto onboarding cohort start date.</li>
            <li>Apply to <strong>The Travel Agent Next Door (TTAND)</strong> as second host for Canadian tour-operator volume (Sunwing/ACV/WestJet Vacations).</li>
            <li>Buy domain: preface.travel (or .ca if taken). Set up Google Workspace ($7/mo).</li>
            <li>Build a 150-person warm-network spreadsheet (Section 04 template).</li>
        </ul>
        <div class="deliverable">Friday deliverable: TICO study started, Fora app submitted, TTAND app submitted, domain live, 150-person list complete with context.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 02</div><div class="title">Platforms</div></div>
        <div class="target">Target: All systems wired</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Deploy preface-homepage-B-hybrid.html as your live site via Netlify or Vercel (free).</li>
            <li>Configure Calendly: 20-min intro call, 45-min discovery call. Connect to Google Calendar.</li>
            <li>Configure Tally intake form. Embed on website.</li>
            <li>Open Beehiiv account (free tier). Set up newsletter brand.</li>
            <li>Secure social handles: @preface.travel on IG, TikTok, LinkedIn business page.</li>
            <li>Hire a contractor on Upwork (4-hour gig, ~$200) to wire up Instantly + Apollo + email-warming. Brief them with exact spec.</li>
        </ul>
        <div class="deliverable">Friday deliverable: Site live. Calendly bookable. Intake form working. Newsletter brand built. Cold-email infrastructure wired (still warming, not sending).</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 03</div><div class="title">License + Network Wave 1</div></div>
        <div class="target">Target: TICO passed. First 50 messages sent.</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Take TICO exam. Pass on first attempt.</li>
            <li>Send personal 1-to-1 message to first 50 people on warm list. (Section 04 template.)</li>
            <li>Schedule 5 in-person coffees with the most-likely-to-refer partners (planners, brokers, agents).</li>
            <li>Record first voice memo for content VA.</li>
        </ul>
        <div class="deliverable">Friday deliverable: TICO certified, 50 personal messages sent, 5 coffees on calendar.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 04</div><div class="title">Network Wave 2 + First Bookings</div></div>
        <div class="target">Target: 1&ndash;2 bookings closed. 50 more messages sent.</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Send personal 1-to-1 message to next 50 people on warm list.</li>
            <li>Run 3&ndash;5 of the scheduled coffees. Each ends with: "Want to start sending people my way? Here's the deal."</li>
            <li>Send first proposal to whichever warm-network lead is closest to booking.</li>
            <li>Close the first booking. Document the workflow.</li>
            <li>Set up CRM: HubSpot Starter ($45/mo) or Notion (free template).</li>
        </ul>
        <div class="deliverable">Friday deliverable: 100 personal messages sent total, 5 coffees done, 3 proposals out, 1&ndash;2 bookings closed.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 05</div><div class="title">Network Wave 3 + Partnership Push</div></div>
        <div class="target">Target: First partnership agreement signed. 3&ndash;5 bookings cumulative.</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Send personal message to final 50 people on warm list (total: 150 contacted).</li>
            <li>Follow up on non-responders from Wave 1 (Week 3) with 2-line nudge.</li>
            <li>Run 5 more partnership coffees. Use Section 05 pitch script.</li>
            <li>Sign first formal partnership agreement (25% commission share, quarterly payout, no quota).</li>
            <li>Publish first newsletter issue (welcome + 3-piece signature content). Section 07.2.</li>
        </ul>
        <div class="deliverable">Friday deliverable: 150 contacted, 1st partnership signed, 1st newsletter out, 3&ndash;5 bookings cumulative.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 06</div><div class="title">Cold Outreach Goes Live</div></div>
        <div class="target">Target: Cold emails sending at 200/day. 7 bookings cumulative.</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Cold email sequences activate at 200 emails/day (will ramp to 1500/day over 6 weeks).</li>
            <li>Hire Filipino VA via OnlineJobs.ph for cold-outreach reply triage ($400&ndash;500/mo, 20 hrs/wk).</li>
            <li>Train VA on reply triage workflow (Section 09). 3 days of supervised training.</li>
            <li>Schedule 5 more partnership coffees.</li>
            <li>Send 2nd newsletter.</li>
        </ul>
        <div class="deliverable">Friday deliverable: Cold emails live, VA hired and trained, 2nd partnership signed, 7 bookings cumulative.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 07</div><div class="title">Content VA + Outsourcing Layer</div></div>
        <div class="target">Target: Content production fully outsourced</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Hire content VA / contractor (Toronto or Buenos Aires) for newsletter + social production ($1,200&ndash;1,500/mo). Use Section 07.1 voice brief.</li>
            <li>Calibrate voice over first 2 weeks of work with line edits.</li>
            <li>Sign 3rd partnership agreement.</li>
            <li>Ramp cold email volume to 400/day.</li>
            <li>Daily KPI dashboard goes live (Section 11).</li>
        </ul>
        <div class="deliverable">Friday deliverable: Content VA producing, 3 partnerships signed, daily KPI dashboard tracking, 9&ndash;10 bookings cumulative.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 08</div><div class="title">Mid-Sprint Review</div></div>
        <div class="target">Target: 8 weeks in, 10&ndash;12 bookings closed, $6&ndash;8K net commission</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Run mid-sprint review. Compare: bookings vs target (10), partnerships vs target (3), newsletter subs vs target (200), cold reply rate vs target (1.5%).</li>
            <li>Identify the funnel that's underperforming. Rebuild only that one. Leave others alone.</li>
            <li>Send 3rd newsletter.</li>
            <li>Cold email ramps to 700/day.</li>
            <li>Schedule 5 more partnership coffees.</li>
        </ul>
        <div class="deliverable">Friday deliverable: Sprint review complete, pivot plan documented, all funnels healthy.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 09</div><div class="title">Business Travel Funnel Begins</div></div>
        <div class="target">Target: First business travel conversations</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Build LinkedIn-targeted list of 200 Toronto-area SMB founders, sales leaders, real estate principals, consulting partners.</li>
            <li>Send 30 personalized LinkedIn DMs using Section 06 script.</li>
            <li>Schedule 3 business-travel discovery calls for Week 10.</li>
            <li>Cold email ramps to 1000/day.</li>
            <li>4th newsletter published.</li>
        </ul>
        <div class="deliverable">Friday deliverable: Business-travel outreach live, 3 calls on calendar, all funnels producing.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 10</div><div class="title">First Business Travel Account</div></div>
        <div class="target">Target: 1 business travel account onboarded</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Run 3 business-travel discovery calls. Convert 1.</li>
            <li>Onboard first BT account: card on file, hotel/airline preferences captured, status accounts linked.</li>
            <li>Send 30 more LinkedIn DMs.</li>
            <li>Cold email at 1500/day (full capacity).</li>
            <li>5th newsletter.</li>
        </ul>
        <div class="deliverable">Friday deliverable: 1 business travel account onboarded, 12&ndash;14 cumulative bookings.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 11&ndash;12</div><div class="title">Optimization Sprint</div></div>
        <div class="target">Target: Conversion rate up 20% on every funnel</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Now that all 5 funnels are running, run conversion-rate optimization on each: cold reply rate, partnership-coffee-to-sign rate, network-message-to-call rate, newsletter open rate, BT call-to-account rate.</li>
            <li>A/B test one variable per funnel per week.</li>
            <li>Sign 4th partnership.</li>
            <li>Hit 50 cumulative warm-network conversations.</li>
            <li>Newsletter at 350+ subs.</li>
            <li>2 business travel accounts active.</li>
        </ul>
        <div class="deliverable">Friday W12 deliverable: All conversion rates documented + improved, 18&ndash;20 cumulative bookings, $1,500/wk avg net commission for past 2 weeks.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 13&ndash;14</div><div class="title">Scale What Works</div></div>
        <div class="target">Target: Best funnel doubles output</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Identify highest ROI funnel from W12 data. Double resource allocation to it.</li>
            <li>If warm network is best: hire VA helper to do email follow-up sequence; you focus on the high-touch closes.</li>
            <li>If partnerships best: book 10 more coffees, build partnership-onboarding doc.</li>
            <li>If cold best: scale to 2,500 emails/day with second sending domain.</li>
            <li>If content best: add a second weekly newsletter edition or daily IG cadence.</li>
            <li>If business travel best: prioritize 60 LinkedIn DMs/wk and add 1 more account.</li>
        </ul>
        <div class="deliverable">Friday W14 deliverable: Best funnel scaled, bookings on track for $2,000/wk avg in W15&ndash;16.</div>
    </div>
</div>

<div class="week-block">
    <div class="week-head">
        <div><div class="w">WEEK 15&ndash;16</div><div class="title">Sprint Close + Q1 Plan</div></div>
        <div class="target">Target: $2,000/wk net commission run-rate, 25&ndash;30 cumulative bookings</div>
    </div>
    <div class="week-body">
        <ul class="check-list">
            <li>Hit $2,000/wk avg for trailing 4 weeks.</li>
            <li>Sprint close: full retrospective. What worked, what didn't, what changes Q2.</li>
            <li>Q2 plan documented (M5&ndash;6): scale-up phase. (See Section 14.)</li>
            <li>Decide on tooling additions for Q2 (CRM upgrade if HubSpot is becoming limiting).</li>
            <li>Document SOPs for first 3 sub-processes that will eventually transfer to a hire.</li>
        </ul>
        <div class="deliverable">Friday W16 deliverable: 16-week sprint complete, $2K/wk locked in, Q2 plan in motion.</div>
    </div>
</div>
</section>

<!-- 04 WARM NETWORK ACTIVATION -->
<section>
<h1><span class="num">Section 04</span>The 150-Person Warm Network Activation</h1>
<p class="section-intro">The single highest-ROI activity in Year 1. Done well, this is 50&ndash;80 bookings in M1&ndash;6.</p>

<h2>Step 1 — Build the List (Day 1, 2 hours)</h2>
<p>Export every contact from: phone, Gmail, Instagram, LinkedIn, WhatsApp, your wedding/engagement guest lists, your sales-pipeline CRM (if relevant), your gym/community/synagogue WhatsApp groups. Goal: 200+ raw names. Filter to ~150 with 7 columns of context.</p>

<div class="callout">
<h4>The 150-Person Sheet Template</h4>
<table>
<thead><tr><th>Name</th><th>How I know them</th><th>Demo</th><th>Likely next trip</th><th>Best channel</th><th>Approach week</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Sarah K</td><td>HS friend</td><td>Engaged, 28</td><td>Honeymoon Sept</td><td>iMessage</td><td>W3</td><td>Not contacted</td></tr>
<tr><td>David C</td><td>Cousin</td><td>Family, 3 kids</td><td>March break</td><td>WhatsApp</td><td>W3</td><td>Not contacted</td></tr>
<tr><td>Maya R</td><td>Family friend</td><td>40s, 3 kids</td><td>Pesach</td><td>iMessage</td><td>W4</td><td>Not contacted</td></tr>
<tr><td>Jordan P</td><td>Real estate agent friend</td><td>35, married</td><td>Likely partnership</td><td>Coffee</td><td>W4</td><td>Not contacted</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
</tbody>
</table>
</div>

<h2>Step 2 — Categorize (Day 1, 30 min)</h2>
<table>
<thead><tr><th>Tier</th><th>Profile</th><th>Approach</th><th>~Volume</th></tr></thead>
<tbody>
<tr><td><strong>Tier 1: Booking Candidates</strong></td><td>Friends/family with trip intent in next 12 months</td><td>Direct: "Here's what I do. Want to chat?"</td><td>40&ndash;60</td></tr>
<tr><td><strong>Tier 2: Referral Sources</strong></td><td>People with strong networks; in-community influencers</td><td>Hybrid: "Here's what I do. If anyone you know is planning..."</td><td>30&ndash;40</td></tr>
<tr><td><strong>Tier 3: Partnership Candidates</strong></td><td>Wedding planners, real estate, mortgage, photographers, jewelers</td><td>Partnership pitch (Section 05)</td><td>20&ndash;30</td></tr>
<tr><td><strong>Tier 4: Awareness</strong></td><td>Acquaintances; community contacts; older peers</td><td>Light: "Hey, wanted to share what I'm doing"</td><td>20&ndash;30</td></tr>
</tbody>
</table>

<h2>Step 3 — The Three Message Templates</h2>

<div class="script-box">
<div class="lab">Template A — Tier 1 (Booking Candidate)</div>
<div class="ctx">1-to-1 personal text or WhatsApp. Voice memo also works for closer friends. Send 5&ndash;10 per evening, not in batch.</div>
Hey [Name] &mdash; quick note. I just got licensed as a travel advisor with Fora (the modern host agency &mdash; not your parents' travel agent kind of thing).

I'm now booking trips for friends and family. The hotel pays the commission, so it costs you nothing &mdash; but you get upgrades, daily breakfast, $100 hotel credits, and a human (me) on WhatsApp if something goes wrong.

Thinking of you because [specific reason: <em>your honeymoon coming up / family March break / 5th anniversary / etc.</em>]. Want to grab a coffee or hop on a call this/next week and chat through it?

No pressure if the timing's off &mdash; would love to be on your list for the next one.
</div>

<div class="script-box">
<div class="lab">Template B — Tier 2 (Referral Source)</div>
<div class="ctx">Same channel as A but framing pivots to network leverage.</div>
Hey [Name] &mdash; wanted to share something new I'm doing. Just got my Fora travel-advisor license. I'm booking trips for friends and family &mdash; the model is the hotel pays the commission, so clients get upgrades, breakfast, and credits at the same price they'd pay direct.

I'm focused on honeymoons, family trips, bach weekends, and milestone travel. <em>(Real specialty: all-inclusives. I've stayed at 20+.)</em>

Reason I'm reaching out: anyone in your circle planning something? Even just a name to put on my radar would be huge. Coffee on me if you want to chat through it.
</div>

<div class="script-box">
<div class="lab">Template C — Tier 3 (Partnership Candidate)</div>
<div class="ctx">More formal. See Section 05 for the full partnership playbook.</div>
Hey [Name] &mdash; been meaning to reach out.

I just got my travel-advisor license and I'm building out Preface (preface.travel). The model: I book honeymoons, family trips, bach weekends, milestone group travel, and corporate travel at properties where my consortia status (Fora is a Virtuoso member + has direct preferred-partner status with Four Seasons, Belmond, Rosewood, Hyatt, etc.) gets clients upgrades, breakfast, resort credits, the works &mdash; at no cost above what Booking.com would charge.

The opportunity for us: anyone you send my way, I send you 25% of my commission. Paid quarterly. No contract, no quota.

Quick 30-min coffee to walk through how the referral mechanic works?
</div>

<h2>Step 4 — The Send Cadence</h2>
<table>
<thead><tr><th>When</th><th>Action</th><th>Volume</th></tr></thead>
<tbody>
<tr><td>Week 3</td><td>Send to Tiers 1+2, batch 1 (top 50 by trip-intent score)</td><td>50 sent</td></tr>
<tr><td>Week 3, Day 5</td><td>Follow-up text to non-responders from batch 1: <em>"Hey &mdash; saw my message didn't go through, did it? :)"</em></td><td>~25 nudges</td></tr>
<tr><td>Week 4</td><td>Send to Tiers 1+2, batch 2 (next 50)</td><td>50 sent</td></tr>
<tr><td>Week 4, Day 5</td><td>Follow-up nudge to batch 2 non-responders</td><td>~25 nudges</td></tr>
<tr><td>Week 5</td><td>Send to Tier 4 + remaining Tier 2 (final 50)</td><td>50 sent</td></tr>
<tr><td>Week 5, Day 5</td><td>Follow-up nudge</td><td>~25 nudges</td></tr>
<tr><td>Week 6</td><td>Final follow-up to all non-responders (30 days post-initial)</td><td>~75 nudges</td></tr>
<tr><td>Week 8</td><td>Stop chasing non-responders. Add to quarterly &ldquo;life update&rdquo; list.</td><td>&mdash;</td></tr>
</tbody>
</table>

<h2>Step 5 — Conversion Workflow (What Happens After They Reply)</h2>
<ol>
<li><strong>They say "tell me more":</strong> Send Calendly link. 20-min intro call. (Section 10 for call structure.)</li>
<li><strong>They say "actually, I have a trip coming up":</strong> Voice-memo back enthusiasm, drop Calendly link immediately, hold the date in your calendar mentally.</li>
<li><strong>They say "I'll keep you in mind":</strong> Reply with one specific value-add ("Just FYI, if you're thinking about [destination they mentioned], the time to book is X weeks before"). Add to 90-day re-touch list.</li>
<li><strong>They don't reply:</strong> One follow-up (above). Then drop into quarterly life-update cadence.</li>
</ol>

<h2>Step 6 — The Referral Ask (Critical and Most Skipped)</h2>
<p>After every closed booking, three specific moments to ask for referrals:</p>
<ul>
<li><strong>At booking confirmation:</strong> "Thanks so much for trusting me on this &mdash; if you know anyone planning a trip in the next 6 months, even just a heads-up before they go to Booking.com is huge."</li>
<li><strong>3 days post-trip:</strong> Welcome-back message + photo request. End with: "If you loved the experience, the highest compliment is sending one friend my way."</li>
<li><strong>Annually:</strong> Birthday or anniversary message that includes: "Anything on the calendar I should help with?"</li>
</ul>

<div class="hormozi-rule">
<div class="label">The number to hit</div>
<div class="rule">From 150 warm-network outreach, expect 30&ndash;50% response rate, 15&ndash;25% conversation rate, 8&ndash;12% booking rate. <strong>That's 12&ndash;18 bookings just from this funnel in M1&ndash;3.</strong> If you're not hitting 30% response rate by W6, rewrite messages. List is rarely the problem.</div>
</div>
</section>

<!-- 05 PARTNERSHIP PLAYBOOK -->
<section>
<h1><span class="num">Section 05</span>The Partnership Playbook</h1>
<p class="section-intro">A signed partnership is worth ~$3K&ndash;15K per year in commission revenue. Get 20 of them. Scale.</p>

<h2>The 50-Partner Target List</h2>
<table>
<thead><tr><th>#</th><th>Partner Type</th><th>Y1 Target</th><th>Volume / partner / yr</th><th>Why they work</th></tr></thead>
<tbody>
<tr><td>1</td><td>Wedding planners (Toronto/Thornhill)</td><td>5&ndash;7</td><td>5&ndash;15 referrals</td><td>Every wedding = honeymoon. Highest density.</td></tr>
<tr><td>2</td><td>Real estate agents (luxury Toronto)</td><td>5&ndash;8</td><td>2&ndash;5 referrals</td><td>Closing a $2M home = client celebrates with a trip.</td></tr>
<tr><td>3</td><td>Mortgage brokers</td><td>3&ndash;5</td><td>2&ndash;4 referrals</td><td>Closing a mortgage = client books vacation home stay.</td></tr>
<tr><td>4</td><td>Wedding photographers</td><td>4&ndash;6</td><td>3&ndash;8 referrals</td><td>Same client overlap as planners; less competitive density.</td></tr>
<tr><td>5</td><td>Bridal stylists / dress shops</td><td>2&ndash;3</td><td>2&ndash;4 referrals</td><td>Captive engaged audience.</td></tr>
<tr><td>6</td><td>Jewelers (engagement rings)</td><td>2&ndash;3</td><td>2&ndash;5 referrals</td><td>Earliest touch-point in honeymoon journey.</td></tr>
<tr><td>7</td><td>Caterers / venues</td><td>3&ndash;4</td><td>3&ndash;6 referrals</td><td>Repeat referrer; talks to engaged couples weekly.</td></tr>
<tr><td>8</td><td>Wealth advisors / financial planners</td><td>3&ndash;5</td><td>1&ndash;3 referrals</td><td>Affluent client base; gift-able commissions (see workaround).</td></tr>
<tr><td>9</td><td>Personal trainers / wellness studios</td><td>2&ndash;3</td><td>1&ndash;3 referrals</td><td>Hot Toronto demographic; high trust.</td></tr>
<tr><td>10</td><td>Concierge medical clinics</td><td>1&ndash;2</td><td>2&ndash;5 referrals</td><td>Captive affluent audience; doctor referrals high trust.</td></tr>
<tr><td>11</td><td>Dental / orthodontic practices (premium)</td><td>1&ndash;2</td><td>1&ndash;2 referrals</td><td>Lower volume but high LTV.</td></tr>
<tr><td>12</td><td>Estate &amp; family lawyers</td><td>1&ndash;2</td><td>1&ndash;3 referrals</td><td>Milestone moments = trips.</td></tr>
<tr><td>13</td><td>Spa / aesthetics clinics</td><td>2&ndash;3</td><td>1&ndash;3 referrals</td><td>Captive female 30+ demographic.</td></tr>
<tr><td>14</td><td>Auto dealerships (luxury)</td><td>1&ndash;2</td><td>1&ndash;2 referrals</td><td>Discretionary spend overlap.</td></tr>
<tr><td>15</td><td>Private school admins / parent-association leads</td><td>1&ndash;2</td><td>2&ndash;5 referrals</td><td>March break + family trip density.</td></tr>
</tbody>
</table>

<h2>The Coffee Pitch (Verbatim, ~3 min)</h2>

<div class="script-box">
<div class="lab">Partnership Coffee Pitch</div>
<div class="ctx">For 30-min coffee. First 3 min is the pitch. Rest is their questions + getting specific about the first referral.</div>
"Thanks for grabbing coffee. Quick context on what I'm doing &mdash; <strong>and the reason I asked is specifically because the best clients in this business come from people like you</strong>, who are in the room when couples and families are making big decisions.

I just got licensed as a travel advisor with Fora &mdash; the modern, millennial-focused host agency. We're a Virtuoso member, we have direct preferred-partner status with Four Seasons, Belmond, Rosewood, Aman, Hyatt (including the Hyatt Inclusive Collection &mdash; Secrets, Dreams, Zoëtry), and most major chains. What that means for clients is: same rate as Booking.com, but they arrive to a room upgrade, daily breakfast, $100&ndash;200 in resort credits, and a human (me) on WhatsApp if something breaks.

The arrangement I'd propose for us: <strong>anyone you send my way who books, I send you 25% of my commission. Paid quarterly. No contract, no quota.</strong> If you send 10 couples in a year that book around $8K each, that's about $1,800&ndash;$2,500 in your pocket. If you send zero, no problem.

The reason this works in our community specifically: you and I know everyone. The same family planning a Pesach trip is planning their daughter's bat mitzvah trip is planning their parents' 60th. <em>One trusted advisor handles all of it. That advisor should be me &mdash; and you should get paid for being the connection.</em>

I'm also <strong>certified specifically on all-inclusives</strong> &mdash; I've personally stayed at 20+ properties (Excellence, Le Blanc, Zoetry, Hyatt Inclusive Collection, Sandals, etc.). So if you're sending clients my way who want a resort trip, they're getting someone with actual receipts, not a generalist.

Want to try it for 90 days, no formal commitment, and see what happens?"
</div>

<h2>The Formal Agreement (1-Page Template)</h2>
<div class="callout">
<h4>Preface Travel — Referral Partnership Agreement (Template)</h4>
<p><strong>Effective:</strong> [Date]</p>
<p><strong>Between:</strong> Preface Travel Co. ("Preface") and [Partner Name / Business] ("Partner")</p>
<p><strong>Term:</strong> 12 months, auto-renewing. Either party may terminate with 30 days notice.</p>
<p><strong>Referral Definition:</strong> A "Referral" is a client introduced to Preface by Partner who books and pays for travel within 12 months of introduction.</p>
<p><strong>Compensation:</strong> Preface will pay Partner 25% of net commission received on each Referral booking, calculated after Fora's 30% host-agency cut and excluding planning fees retained by Preface.</p>
<p><strong>Payment Schedule:</strong> Quarterly, within 30 days of quarter-end, by e-transfer or cheque.</p>
<p><strong>Tracking:</strong> Partner will introduce Referrals via warm email or DM, copying [partner@preface.travel]. Each Referral receives a unique partner-attribution tag in Preface's CRM.</p>
<p><strong>Exclusivity:</strong> Non-exclusive on both sides.</p>
<p><strong>Confidentiality:</strong> Standard mutual.</p>
<p><strong>Signed:</strong> _____________________________ &nbsp; Date: _______</p>
</div>

<h2>The Onboarding Sequence (Partner Side)</h2>
<ol>
<li><strong>Day 0:</strong> Agreement signed (DocuSign or PDF e-signature).</li>
<li><strong>Day 1:</strong> Partner receives Welcome Pack: 2-page brief on how to refer (1-line text template + sample blurb to send their clients).</li>
<li><strong>Day 7:</strong> Check-in: "Just confirming you've got everything &mdash; any first referrals on the radar?"</li>
<li><strong>Day 30:</strong> Monthly partner update email: any commissions paid, any new collateral, one client-friendly content piece.</li>
<li><strong>Day 90:</strong> Quarterly review call (15 min). If 0 referrals: re-onboard. If 1+: thank, share results, ask for testimonial.</li>
</ol>

<h2>Workaround for Financial Advisor Partnerships</h2>
<div class="callout gold">
<p>Most financial advisors can't accept outside commissions due to their broker-dealer's compliance rules. Workaround: <strong>instead of cash, gift dinner / hotel stay / charity donation of equivalent value</strong>. Frame as &ldquo;client-appreciation gift&rdquo;. Same economics for them, no compliance flag.</p>
<p>Specifically: a $1,200 commission share can be paid as a $1,200 hotel stay you book for them, a $1,200 dinner at Donalda Club, or a $1,200 donation in their name to a charity of their choice (often the most-appreciated option).</p>
</div>

<h2>The Top 20% Rule</h2>
<p>By Month 6, ~20% of your partners will be producing ~80% of your partnership volume. Identify them. Treat them like A-list:</p>
<ul>
<li>Monthly check-ins (not quarterly)</li>
<li>Sole-source first FAM trip slots</li>
<li>Featured in newsletter "Partner of the Quarter"</li>
<li>Bumped to 30% commission share after their 5th referral</li>
</ul>

<div class="hormozi-rule">
<div class="label">The number to hit</div>
<div class="rule">8&ndash;10 signed partnerships by end of Month 3. 20 by end of Y1. Each producing average 3 referrals/yr = 60 incremental bookings/yr from the partnership engine alone.</div>
</div>
</section>

<!-- 06 BUSINESS TRAVEL PLAYBOOK -->
<section>
<h1><span class="num">Section 06</span>The Business Travel Playbook</h1>
<p class="section-intro">The funnel most travel advisors ignore. The funnel that produces the most predictable recurring revenue. The funnel that fits your existing sales-led skill set.</p>

<h2>Why This Works (And Why It's a New Funnel for Preface)</h2>
<table>
<thead><tr><th>Dimension</th><th>Leisure Travel</th><th>Business Travel</th></tr></thead>
<tbody>
<tr><td>Trips per client per year</td><td>1&ndash;2</td><td>20&ndash;50</td></tr>
<tr><td>Average trip value</td><td>$4&ndash;15K</td><td>$800&ndash;3K</td></tr>
<tr><td>Avg net commission per trip</td><td>$400&ndash;1,500</td><td>$40&ndash;120</td></tr>
<tr><td>Annual revenue per client</td><td>$500&ndash;3K</td><td>$1,500&ndash;6K</td></tr>
<tr><td>Client lifetime (years)</td><td>1&ndash;2 (trip-driven)</td><td>3&ndash;5+ (relationship-driven)</td></tr>
<tr><td>Sales cycle</td><td>1&ndash;3 weeks</td><td>2&ndash;4 weeks</td></tr>
<tr><td>Seasonal pattern</td><td>Heavy Q1, Q3-Q4</td><td>Sun&ndash;Thu year-round</td></tr>
<tr><td>Buyer persona</td><td>Couples 28&ndash;36 / families</td><td>Founders, partners, sales execs, consultants</td></tr>
<tr><td>Your edge</td><td>Network density, lived AI expertise</td><td><strong>You already work in sales. You speak their language.</strong></td></tr>
</tbody>
</table>

<h2>The Ideal Business Travel Client Profile (ICP)</h2>
<p>Not every executive wants a travel advisor. The ones who do share these traits:</p>
<ol>
<li><strong>Travel 20&ndash;60 nights/year</strong> on business. Less = not worth handing off. More = they have an in-house corporate travel desk already.</li>
<li><strong>Their company has &lt;200 employees</strong> &mdash; bigger has procurement-managed travel via Concur/Egencia. Smaller is where you live.</li>
<li><strong>Status-driven</strong> &mdash; they care about Marriott Titanium, Hilton Diamond, AmEx Platinum. They book based on points and recognition, not just price.</li>
<li><strong>Time-poor</strong> &mdash; their time is worth $300+/hr. Saving 30 min on a booking is the value prop, not saving $50.</li>
<li><strong>Roles:</strong> SaaS founders/CEOs/CROs, real estate principals, M&amp;A lawyers, consultants (independent or partner level), private wealth advisors, healthcare practice owners, agency owners, regional sales VPs.</li>
</ol>

<h2>What You're Actually Selling Them</h2>
<table>
<thead><tr><th>What they think they want</th><th>What you actually sell</th></tr></thead>
<tbody>
<tr><td>Cheaper hotels</td><td>Better hotels at the same price (Hyatt Privé, Marriott STARS, Hilton for Luxury amenities on their work trip)</td></tr>
<tr><td>Convenience</td><td>30 min/week saved &mdash; you book, change, cancel, expense-summarize</td></tr>
<tr><td>Loyalty point optimization</td><td>Yes, you do this too &mdash; layer their points + your Fora consortium benefits</td></tr>
<tr><td>Travel disruption protection</td><td>WhatsApp at 11pm when their flight cancels in Newark</td></tr>
<tr><td>Status without playing the game</td><td>You match their status across brands when possible (Hyatt status match, Hilton, Marriott)</td></tr>
</tbody>
</table>

<h2>The LinkedIn Outreach Sequence (60 days, 5 touches)</h2>

<div class="script-box">
<div class="lab">Touch 1 — Day 0 — Connection Request</div>
<div class="ctx">Add personalized note. Don't pitch.</div>
Hey [Name] &mdash; saw you [recent post / specific company moment / mutual connection]. Building Preface &mdash; corporate travel for founders + sales leaders in Toronto. Curious to connect.
</div>

<div class="script-box">
<div class="lab">Touch 2 — Day 3 (post-acceptance) — Soft Hello</div>
<div class="ctx">Don't pitch yet. Drop value or relate.</div>
Appreciate the connect. Quick context on me: I'm 5 years into [B2B SaaS / fintech / commercial real estate &mdash; whatever your domain is]. Been on the road a lot.

Last year I started Preface, a Toronto-based travel-advisor practice focused on millennial founders + sales leaders. The thesis: most people in our world are leaking 30 minutes / week on Marriott.com when a 2-min Slack to me would handle it.

Not pitching today &mdash; just wanted to connect. If your travel volume's high enough that the friction has occurred to you, happy to chat anytime.
</div>

<div class="script-box">
<div class="lab">Touch 3 — Day 14 — Value Drop</div>
<div class="ctx">Send a useful resource. Build authority.</div>
Quick one [Name] &mdash; in case it's useful, just published a 3-min read on the 5 hotels in Toronto where the loyalty math actually pays off for elite-tier members: [LINK to your newsletter].

If business travel's in your week, the second one (Park Hyatt) is genuinely under-leveraged.
</div>

<div class="script-box">
<div class="lab">Touch 4 — Day 30 — The Specific Ask</div>
<div class="ctx">Now you can pitch.</div>
[Name] &mdash; been a few weeks since we connected. Quick ask:

I'm onboarding 5 founders + sales execs onto Preface this quarter as an "anchor cohort." The deal: I become your bookings desk for hotels + flights, all your existing loyalty programs stay yours (I just book under them), and the hotels pay my fee, so it costs you nothing.

The upside for you: Hyatt Privé / Marriott STARS / Hilton for Luxury benefits on your business stays (upgrade, $50&ndash;100 hotel credit, breakfast) layered on top of your status. Plus you stop logging into Marriott.com.

Want to do a 20-min onboarding call to see if it fits? Calendly: [LINK]
</div>

<div class="script-box">
<div class="lab">Touch 5 — Day 60 — The Closer</div>
<div class="ctx">Final pass. Either close or move on.</div>
Last note from me, [Name] &mdash; circling back on Preface. The anchor-cohort offer expires end of [Month] (after that, I'm priced normally and the pre-bookings credit goes away).

If business travel's not a frequent enough thing for you, totally understand &mdash; happy to be here when it is. If it is, the 20-min call is at [LINK] and the upgrade-package perk alone usually pays for the time.
</div>

<h2>The Onboarding Call (20 minutes)</h2>
<table>
<thead><tr><th>Minute</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>0&ndash;2</td><td>Rapport + agenda. "Goal of this call is to understand your travel pattern + figure out if I can save you time."</td></tr>
<tr><td>2&ndash;6</td><td>Discovery: How many nights/year? Which cities? Which chains/airlines? What's your current loyalty status?</td></tr>
<tr><td>6&ndash;10</td><td>Map the value: For their specific pattern, you'd save them ~X hours/year + capture ~$Y in additional Hyatt Privé/STARS/Impresario amenities.</td></tr>
<tr><td>10&ndash;14</td><td>Walk through the process: Slack/email me the trip, I book, you get confirmation in 30 min, your card on file gets charged direct by the hotel.</td></tr>
<tr><td>14&ndash;17</td><td>Address objections (Section 10).</td></tr>
<tr><td>17&ndash;20</td><td>Close: "If this all makes sense, can we set you up this week? Takes ~15 min for me to load your preferences + card."</td></tr>
</tbody>
</table>

<h2>The Business Travel Onboarding Workflow</h2>
<ol>
<li><strong>Day 0 (post-call):</strong> Send onboarding form (Typeform / Tally). Capture: name, DOB, passport details, hotel loyalty numbers, airline status, dietary/seat preferences, billing card.</li>
<li><strong>Day 1:</strong> Confirm receipt. Set up their profile in your CRM with all preferences. Connect their accounts where you have advisor access (Hyatt Privé linkable, Marriott STARS, Hilton for Luxury, Four Seasons FSPP).</li>
<li><strong>Day 2:</strong> Share their "Travel Profile" PDF (one-pager with everything you'll need to book). They confirm.</li>
<li><strong>Day 3:</strong> Activation. "First trip on the books &mdash; what's coming up?"</li>
<li><strong>Ongoing:</strong> They Slack/email you the trip details (dates, city, conference if relevant). You book within 60 min. Confirmation goes back via same channel.</li>
</ol>

<h2>The Business Travel Pricing Model</h2>
<table>
<thead><tr><th>Tier</th><th>Cost</th><th>What it includes</th></tr></thead>
<tbody>
<tr><td><strong>Standard</strong></td><td>$0/trip (commission-funded)</td><td>Hotel bookings under Fora's Privé/STARS/Virtuoso programs. Client gets upgrade, breakfast, credit at no charge.</td></tr>
<tr><td><strong>Concierge</strong></td><td>$25/trip OR $150/month subscription</td><td>Adds: flight booking, restaurant reservations, car/transfer coordination, disruption recovery, lounge advice.</td></tr>
<tr><td><strong>Executive</strong></td><td>$500/month</td><td>Above + 24/7 WhatsApp + dedicated profile + quarterly travel optimization review + spouse/family leisure trip planning included.</td></tr>
</tbody>
</table>
<p class="small">Most clients land in Standard (free, you make the commission). Tier 2 is for clients with 25+ nights and complex air. Tier 3 is for the top 10% of accounts &mdash; founders / partners who'll spend $30&ndash;60K/yr in total travel.</p>

<h2>The Account Renewal Mechanic</h2>
<p>Business travel clients aren't "renewed" formally &mdash; they're retained by being useful. The retention check-ins:</p>
<ul>
<li><strong>Monthly:</strong> 30-min "trip review" email summarizing booked vs cancelled vs upgraded.</li>
<li><strong>Quarterly:</strong> 20-min call. Review status progress, upcoming travel, leisure-trip cross-sell.</li>
<li><strong>Annually:</strong> Loyalty optimization session. Walk through their Hyatt/Marriott/Hilton spend, recommend status-match opportunities, leverage Privé/STARS for upcoming year.</li>
</ul>

<div class="hormozi-rule">
<div class="label">The number to hit</div>
<div class="rule">5&ndash;10 business travel accounts by end of Y1. Each averaging 25&ndash;35 hotel nights/yr × $60 net commission = <strong>$8&ndash;12K/yr recurring per account</strong>. By Y2 H2: 20 accounts = $160&ndash;240K of recurring revenue independent of leisure seasonality.</div>
</div>
</section>

<!-- 07 CONTENT ENGINE -->
<section>
<h1><span class="num">Section 07</span>The Content Engine</h1>
<p class="section-intro">Content doesn't make sales in Y1. Content makes <em>trust</em> in Y1. Trust closes sales in Y2&ndash;3.</p>

<h2>7.1 — Voice &amp; the 50/30/20 Mix</h2>

<div class="callout">
<h4>Voice Profile (Brief for Content VA)</h4>
<p><strong>Tone:</strong> Smart, opinionated, playful, slightly irreverent. Think: a sharp friend who travels well and tells you the truth.</p>
<p><strong>Vocabulary:</strong> Specific, concrete, brand-name-heavy. Numbers over adjectives. "Excellence Playa Mujeres" not "a top all-inclusive." "$3,460 in upgrade value" not "amazing perks."</p>
<p><strong>Sentence length:</strong> Short. Punchy. Stack short ones until you need a longer one for rhythm. Then a short one again.</p>
<p><strong>Allowed:</strong> Hot takes. Opinions. Self-aware millennial humor. Calling things "mid." Acknowledging trade-offs. Using "lol" sparingly. Memes if they're good.</p>
<p><strong>Forbidden:</strong> "Indulge." "Savor." "Unparalleled luxury." "Embark on a journey." Anything that sounds like a 1996 travel brochure. Emoji overuse. "Wanderlust." "Bucket list" (use only with self-aware framing).</p>
<p><strong>Reference brands:</strong> Mejuri, Away, Glossier (for voice). Aman, Belmond (NOT for voice &mdash; for visual references only).</p>
</div>

<h3>The 50/30/20 Content Mix</h3>
<table>
<thead><tr><th>%</th><th>Type</th><th>Purpose</th><th>Example posts</th></tr></thead>
<tbody>
<tr><td>50%</td><td><strong>Practical / Tactical</strong></td><td>Build authority. Teach something useful. Drive search + saves.</td><td>"How to pick between Excellence Punta Cana vs Playa Mujeres", "What Hyatt Privé actually gets you at a Secrets resort", "The 5 best Toronto hotels for executive travelers"</td></tr>
<tr><td>30%</td><td><strong>Opinionated / Voice</strong></td><td>Differentiation. Build the brand persona.</td><td>"Sandals is mid", "Tulum is performance art", "If you're paying for a butler suite, you should be in Excellence Club"</td></tr>
<tr><td>20%</td><td><strong>Personal / Story</strong></td><td>Trust + humanization. Show the work.</td><td>Client trip recaps, FAM trip notes, behind-the-scenes booking moments, your own travel photos with takes</td></tr>
</tbody>
</table>

<h2>7.2 — Newsletter Playbook</h2>

<h3>Setup (Week 2)</h3>
<ul class="check-list">
<li>Sign up for Beehiiv (free tier, upgrade at 1,000 subs).</li>
<li>Brand colors + logo (use brand from website).</li>
<li>Newsletter name: "<strong>Preface</strong>" (same as brand). Subtitle: "Travel takes, every other Friday."</li>
<li>Welcome email automated. 1 email, ~150 words, 1 link to the homepage.</li>
<li>Embed Beehiiv signup form on homepage + every page footer.</li>
<li>Set publishing cadence: <strong>biweekly Friday 10am ET</strong>.</li>
</ul>

<h3>The Format (Every Issue)</h3>
<table>
<thead><tr><th>Block</th><th>Length</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>1. Subject line (TEST THIS)</td><td>~6 words</td><td>50%+ open rate target. Curiosity, not announcement.</td></tr>
<tr><td>2. One-line opener</td><td>1 sentence</td><td>Sets the mood. Often a hot take.</td></tr>
<tr><td>3. The Take (main piece)</td><td>500&ndash;700 words</td><td>One specific recommendation, comparison, or insider tip. The reason they subscribed.</td></tr>
<tr><td>4. The Receipt</td><td>100&ndash;150 words + image</td><td>Real booking example: what they paid, what they got. Names changed.</td></tr>
<tr><td>5. Three Quick Hits</td><td>~75 words total</td><td>Three one-line tips/takes. Skimmable.</td></tr>
<tr><td>6. CTA</td><td>1 line</td><td>"Got a trip on the calendar? Hit reply." OR "Book a 20-min call: [link]"</td></tr>
<tr><td>7. PS</td><td>1 line</td><td>Optional. A personal note. Builds intimacy.</td></tr>
</tbody>
</table>

<h3>The First 12 Issues (Topics)</h3>
<table>
<thead><tr><th>#</th><th>Title</th><th>Lead Take</th></tr></thead>
<tbody>
<tr><td>01</td><td>Welcome (no take) + What this is</td><td>What you'll get + the manifesto</td></tr>
<tr><td>02</td><td>Excellence Playa Mujeres vs Punta Cana</td><td>I've been to both. Here's the call.</td></tr>
<tr><td>03</td><td>How Hyatt Privé just changed all-inclusive travel</td><td>Now Secrets/Dreams/Zoëtry get real perks.</td></tr>
<tr><td>04</td><td>Sandals is mid. Here are 3 alternatives.</td><td>Excellence, Le Blanc, Royalton Luxury &mdash; same price tier.</td></tr>
<tr><td>05</td><td>The 3 Toronto hotels for executive travel</td><td>Park Hyatt, Ritz, Shangri-La &mdash; ranked.</td></tr>
<tr><td>06</td><td>Why your honeymoon shortlist is wrong</td><td>The 3 mistakes everyone makes at the planning stage.</td></tr>
<tr><td>07</td><td>Sargassum season: where NOT to go May-Oct</td><td>And where to go instead.</td></tr>
<tr><td>08</td><td>The Excellence Club tier upgrade math</td><td>Why the $500/week upgrade is the most undervalued add-on in travel.</td></tr>
<tr><td>09</td><td>Bach weekend logistics 101</td><td>How to plan 10 women, 1 villa, 5 dinners, 1 boat day.</td></tr>
<tr><td>10</td><td>Maldives, ranked.</td><td>The honest hierarchy of 14 resorts I've researched.</td></tr>
<tr><td>11</td><td>Group trips: when to use a TC, when to DIY</td><td>The decision tree.</td></tr>
<tr><td>12</td><td>Best-of: 2026 in receipts</td><td>The 12 most interesting bookings I made this year.</td></tr>
</tbody>
</table>

<h3>Newsletter Growth Tactics</h3>
<ol>
<li><strong>Signup as a default everywhere:</strong> Every IG post, every TikTok caption, every LinkedIn post ends with "newsletter at preface.travel."</li>
<li><strong>Cross-promotion at month 3:</strong> Trade newsletter mentions with 5 other Toronto creators (food, lifestyle, real estate creators).</li>
<li><strong>Lead magnet at month 4:</strong> "The All-Inclusives Decision Guide" &mdash; gated PDF, requires email. Targets to 20% of organic subs.</li>
<li><strong>Referral program at month 6:</strong> Beehiiv has built-in. Reward at 3, 10, 25 referrals.</li>
<li><strong>Paid acquisition at month 12 (only if conversion math works):</strong> Newsletter ad swaps via SparkLoop or Beehiiv Boosts.</li>
</ol>

<h2>7.3 — Instagram Playbook</h2>

<h3>Account Setup</h3>
<ul class="check-list">
<li>Handle: @preface.travel</li>
<li>Bio: "Independent travel advisor (Toronto) · 20+ all-inclusives stayed · Free upgrades + perks at the same prices as Booking.com" + link in bio (Linktree → newsletter, booking, all-inclusives page, about)</li>
<li>Profile photo: clean, modern, on-brand</li>
<li>Highlights: "All-Inclusives" / "Honeymoons" / "Hot Takes" / "Receipts" / "Bookings" / "FAQ"</li>
<li>Verified business account (apply at 1K followers)</li>
</ul>

<h3>Posting Cadence (Weekly)</h3>
<table>
<thead><tr><th>Day</th><th>Format</th><th>Content type</th></tr></thead>
<tbody>
<tr><td>Mon</td><td>Carousel (10 slides)</td><td>Educational / list / ranking</td></tr>
<tr><td>Tue</td><td>Reel (30&ndash;60s)</td><td>Hot take, repurposed from TikTok</td></tr>
<tr><td>Wed</td><td>Single post (image)</td><td>"Receipt" &mdash; real upgrade screenshot</td></tr>
<tr><td>Thu</td><td>Reel (30&ndash;60s)</td><td>Brand showcase: a resort I've been to, 60-sec take</td></tr>
<tr><td>Fri</td><td>Single post (image)</td><td>Newsletter teaser</td></tr>
<tr><td>Mon&ndash;Fri</td><td>Stories (3&ndash;5/day)</td><td>BTS, polls, screenshots, day-in-life</td></tr>
<tr><td>Sat&ndash;Sun</td><td>Stories only (light)</td><td>Personal travel, weekends</td></tr>
</tbody>
</table>

<h3>The 10 Carousel Templates (Reuse Forever)</h3>
<ol>
<li><strong>The Ranking:</strong> "I've been to 12 all-inclusives. Here are the top 4." (slide per resort)</li>
<li><strong>The Comparison:</strong> "Excellence Playa Mujeres vs Punta Cana. The verdict." (head-to-head)</li>
<li><strong>The Decision Tree:</strong> "Honeymoon picker. Answer 4 questions." (interactive feel)</li>
<li><strong>The Receipt:</strong> "What my client paid vs what they got." (math reveal)</li>
<li><strong>The Mistake List:</strong> "5 things people get wrong about booking [topic]."</li>
<li><strong>The Insider:</strong> "5 things the resort website won't tell you."</li>
<li><strong>The Math:</strong> "Same hotel. Same price. Here's what's different through me."</li>
<li><strong>The Hierarchy:</strong> "All-inclusives, tiered by quality."</li>
<li><strong>The Backstory:</strong> "Why I started Preface" (every 3&ndash;4 months)</li>
<li><strong>The Q&amp;A:</strong> "10 questions I get asked daily."</li>
</ol>

<h2>7.4 — LinkedIn Playbook</h2>

<h3>Why LinkedIn Specifically Matters for Preface</h3>
<p>LinkedIn isn't for the leisure-travel audience. It's for the <strong>business travel funnel</strong> and the partnership funnel (financial advisors, real estate principals, lawyers). Treat it as a B2B channel.</p>

<h3>Posting Cadence: 3x/week (Mon, Wed, Fri)</h3>
<table>
<thead><tr><th>Day</th><th>Type</th><th>Topic</th></tr></thead>
<tbody>
<tr><td>Mon</td><td>Insight post (400&ndash;600 words)</td><td>The business travel angle ("How Hyatt Privé status matching works for a Toronto founder")</td></tr>
<tr><td>Wed</td><td>Personal story (200&ndash;400 words)</td><td>Client moment, partnership win, FAM trip note &mdash; framed around an insight</td></tr>
<tr><td>Fri</td><td>Opinion / contrarian post (200&ndash;400 words)</td><td>Industry take ("The travel industry's biggest mistake with founders")</td></tr>
</tbody>
</table>

<h3>The LinkedIn Post Template</h3>
<div class="callout">
<p><strong>Line 1:</strong> Hook. One specific claim or observation. (e.g., "I helped a Toronto founder save 30 minutes a week. He still thinks he hired me for the upgrades.")</p>
<p><strong>Line 2 (blank):</strong></p>
<p><strong>Lines 3&ndash;15:</strong> The story or insight. Short paragraphs (1&ndash;3 lines each). Concrete examples. Numbers.</p>
<p><strong>Line 16 (blank):</strong></p>
<p><strong>Last line:</strong> One-line takeaway OR a soft question.</p>
<p><strong>Optional PS:</strong> "I'm building Preface for founders + sales execs who travel 25+ nights/year. DM me if that's you."</p>
</div>

<h2>7.5 — TikTok Playbook</h2>

<h3>The Honest TikTok Reality</h3>
<p>TikTok is the highest-ceiling, lowest-floor channel. One viral video changes everything. 50 videos with no views might happen first. <strong>Plan for 90 days before judging.</strong></p>

<h3>Setup</h3>
<ul class="check-list">
<li>Handle: @preface.travel</li>
<li>Bio: "20+ all-inclusives stayed. Travel advisor (Toronto). Free hotel perks at the same prices."</li>
<li>Profile photo + linked Instagram</li>
<li>3 anchor videos before launching: an intro, a hot take, a comparison</li>
</ul>

<h3>Posting Cadence</h3>
<p><strong>2 videos / week minimum.</strong> Shot in batches of 6&ndash;8 on a single afternoon. Each 30&ndash;90 seconds.</p>

<h3>The 5 Video Formats (Reuse Forever)</h3>
<ol>
<li><strong>"Should you book X or Y?"</strong> &mdash; head-to-head resort/destination comparisons</li>
<li><strong>"What this $5K booking actually got my client"</strong> &mdash; receipt-style upgrade reveal</li>
<li><strong>"The 3 mistakes you're making at [destination]"</strong> &mdash; list format, fast cuts</li>
<li><strong>"POV: You think you know all-inclusives"</strong> &mdash; storytime / opinion</li>
<li><strong>"Day in the life of a travel advisor"</strong> &mdash; BTS booking moments</li>
</ol>

<h3>TikTok Hook Templates (Copy These)</h3>
<ul>
<li>"This is going to upset some people, but..."</li>
<li>"If you're paying $5K for an all-inclusive, you're doing one of two things wrong."</li>
<li>"I've stayed at 20 all-inclusives. Here's the one I'd never go back to."</li>
<li>"Booking.com is lying to you about resort upgrades."</li>
<li>"POV: your travel agent has never actually been to the resort she's selling you."</li>
</ul>

<h2>7.6 — 12-Week Editorial Calendar</h2>

<table>
<thead><tr><th>Week</th><th>Newsletter</th><th>IG Carousel</th><th>IG Reel</th><th>LinkedIn (3x)</th><th>TikTok (2x)</th></tr></thead>
<tbody>
<tr><td>W1</td><td>&mdash;</td><td>"Why I started Preface"</td><td>Hot take: Sandals is mid</td><td>Launch announcement / why business travel / what I learned in sales</td><td>Intro + Resort take</td></tr>
<tr><td>W2</td><td>&mdash;</td><td>10 all-inclusives ranked</td><td>Excellence Club math</td><td>BT insight / founder story / industry take</td><td>Comparison / Math</td></tr>
<tr><td>W3</td><td>Issue 01 (Welcome)</td><td>Honeymoon decision tree</td><td>Tulum is performance</td><td>Privé deep dive / partner story / contrarian take</td><td>Hot take / Mistake list</td></tr>
<tr><td>W4</td><td>&mdash;</td><td>5 things people get wrong</td><td>Sargassum season warning</td><td>Hotel mathematics / client win / opinion</td><td>BTS / Comparison</td></tr>
<tr><td>W5</td><td>Issue 02 (Excellence vs PC)</td><td>The Excellence Club guide</td><td>Receipt: $3,460 upgrade</td><td>Cost analysis / personal trip / opinion</td><td>Receipt / Day in life</td></tr>
<tr><td>W6</td><td>&mdash;</td><td>Hyatt Privé all-inclusive list</td><td>Le Blanc tour</td><td>Loyalty math / partnership / take</td><td>Comparison / Hot take</td></tr>
<tr><td>W7</td><td>Issue 03 (Hyatt Privé)</td><td>Bach planner guide</td><td>Atelier vs Excellence</td><td>BT cohort / FAM trip / take</td><td>Mistake list / Receipt</td></tr>
<tr><td>W8</td><td>&mdash;</td><td>3 Toronto hotels ranked</td><td>Park Hyatt vs Ritz</td><td>Toronto travel / client win / take</td><td>Comparison / BTS</td></tr>
<tr><td>W9</td><td>Issue 04 (Sandals alternatives)</td><td>Family resort guide</td><td>Hyatt Ziva tour</td><td>Group travel / partner story / take</td><td>Hot take / Day in life</td></tr>
<tr><td>W10</td><td>&mdash;</td><td>Honeymoon mistakes</td><td>Three honeymoon hacks</td><td>Founder travel / case study / take</td><td>Receipt / Comparison</td></tr>
<tr><td>W11</td><td>Issue 05 (Toronto hotels)</td><td>Maldives ranking</td><td>Where NOT to go in May</td><td>Resort review / personal moment / take</td><td>Mistake list / Hot take</td></tr>
<tr><td>W12</td><td>&mdash;</td><td>Q1 best-of</td><td>Tulum take</td><td>Quarter retro / partnership / take</td><td>BTS / Comparison</td></tr>
</tbody>
</table>

<p class="small">After Week 12 the calendar repeats with topic refresh. The mechanics stay identical.</p>

<h3>The Repurposing Stack</h3>
<p>One source → 5 outputs. Don't make content separately for each channel.</p>
<ol>
<li><strong>You record a 5-min voice memo</strong> on the topic of the week.</li>
<li><strong>VA writes the newsletter</strong> from the memo (~600 words).</li>
<li><strong>VA writes one LinkedIn post</strong> derived from a sub-section.</li>
<li><strong>VA writes one IG carousel</strong> (10 slides) from the same topic.</li>
<li><strong>VA writes one TikTok script</strong> from the strongest line.</li>
<li><strong>You record the TikTok</strong> (3 min on Saturday morning).</li>
<li><strong>TikTok becomes IG Reel</strong> with caption rewrite.</li>
</ol>
<p>Total founder time per week: ~90 minutes (voice memo + TikTok shoot + review).</p>
</section>

<!-- 08 LANDING PAGES -->
<section>
<h1><span class="num">Section 08</span>The Landing Page Library</h1>
<p class="section-intro">Eleven pages to build. Three are live. Eight to ship across Q1&ndash;Q3.</p>

<table>
<thead><tr><th>#</th><th>Page</th><th>Purpose</th><th>Priority</th><th>Built</th></tr></thead>
<tbody>
<tr><td>1</td><td>Homepage</td><td>Brand front door + lead capture</td><td>P0</td><td>✓ B-hybrid live</td></tr>
<tr><td>2</td><td>About</td><td>Founder story + trust</td><td>P0</td><td>✓ Live</td></tr>
<tr><td>3</td><td>All-Inclusives</td><td>Specialty SEO + credibility</td><td>P0</td><td>✓ Live</td></tr>
<tr><td>4</td><td>Business Travel</td><td>BT funnel landing page</td><td>P0</td><td>W6&ndash;7 build</td></tr>
<tr><td>5</td><td>Honeymoons</td><td>SEO + conversion for highest-value segment</td><td>P1</td><td>M2 build</td></tr>
<tr><td>6</td><td>Family Trips</td><td>Family segment landing</td><td>P1</td><td>M3 build</td></tr>
<tr><td>7</td><td>Group Trips &amp; Milestones</td><td>Bach + 40th + family trip funnel</td><td>P1</td><td>M3 build</td></tr>
<tr><td>8</td><td>Newsletter signup (gated lead magnet)</td><td>List growth</td><td>P1</td><td>M4 build</td></tr>
<tr><td>9</td><td>Book a Call (intake form)</td><td>Sales funnel</td><td>P0</td><td>W2 build</td></tr>
<tr><td>10</td><td>Partner Program (B2B)</td><td>Partnership funnel</td><td>P2</td><td>M5 build</td></tr>
<tr><td>11</td><td>Hotel Brand Pages (3&ndash;5 SEO plays)</td><td>Long-tail organic traffic</td><td>P2</td><td>M6&ndash;9 build</td></tr>
</tbody>
</table>

<h2>How to Build Each Page (The Skeleton)</h2>

<h3>The Universal Page Structure (Don't Reinvent)</h3>
<p>Every page above the footer follows the same 7-block skeleton. Only content varies.</p>
<ol>
<li><strong>Hero:</strong> One bold statement (h1) + one supporting paragraph + one CTA.</li>
<li><strong>Credibility strip:</strong> Stats bar (20+ AIs, 15+ Caribbean, etc.) OR brand-name strip OR receipt-style trust signal.</li>
<li><strong>Main value prop:</strong> Either "How it works" (4 steps) or "What you get" (4 benefits) or "The math" (table).</li>
<li><strong>Proof:</strong> One real client receipt, testimonial, or specific case study.</li>
<li><strong>Education:</strong> Framework, decision tree, or 4 common mistakes.</li>
<li><strong>FAQ (optional):</strong> 5&ndash;7 specific questions, each 2&ndash;3 sentences.</li>
<li><strong>CTA + Footer:</strong> Clear next step + standard footer.</li>
</ol>

<h2>Page 4 — Business Travel (Build in W6&ndash;7)</h2>
<div class="callout">
<h4>Business Travel Page Specification</h4>
<p><strong>URL:</strong> /business-travel</p>
<p><strong>Hero h1:</strong> "Stop logging into Marriott.com. I'll do it." (or similar)</p>
<p><strong>Hero subhead:</strong> "Travel desk for Toronto founders + sales execs. Hotel + flight bookings, status optimization, disruption recovery. Free at the standard tier; the hotels pay the commission."</p>
<p><strong>Hero CTA:</strong> Book a 20-min onboarding call</p>
<p><strong>Credibility strip:</strong> "20+ hotel partner programs. Fora Privé / Virtuoso member. TICO #XXXXXXX."</p>
<p><strong>How it works (4 steps):</strong> 1) 20-min onboarding call. 2) Profile + preferences captured. 3) Slack/email me trips. 4) Booked within 60 min. Hotel charges your card direct.</p>
<p><strong>Proof:</strong> "Real client receipt — Toronto SaaS founder, 32 hotel nights last quarter, $2,340 in added Hyatt Privé / Marriott STARS amenity value at zero incremental cost."</p>
<p><strong>Tier table:</strong> Standard / Concierge / Executive pricing.</p>
<p><strong>FAQ:</strong> "Do I lose my Marriott points?" (No.) "Can you book through my company's TMS?" (No, this is a personal-account play.) "What if my flight cancels at 2am?" (You text me.) "What's the catch?" (None — Fora pays my commission.)</p>
<p><strong>Final CTA:</strong> 20-min call.</p>
</div>

<h2>Page 5 — Honeymoons (M2 build)</h2>
<div class="callout">
<h4>Honeymoons Page Spec</h4>
<p><strong>URL:</strong> /honeymoons</p>
<p><strong>Hero h1:</strong> "The trip you've been overthinking for 9 months. Let's not screw it up."</p>
<p><strong>Hero CTA:</strong> Book a planning call (free)</p>
<p><strong>Credibility:</strong> "20+ all-inclusives stayed · Maldives, Amalfi, Greek Isles, Caribbean specialist · Avg honeymoon: $12-22K"</p>
<p><strong>The 4 Honeymoon Profiles (interactive decision tree):</strong> Beach &amp; Bali / Multi-city Europe / Adventure + Wind-down / Maldives over-water</p>
<p><strong>Receipt:</strong> Real $14,000 Maldives 7-night booking with full upgrade breakdown</p>
<p><strong>Process timeline:</strong> 12 months out / 9 months / 6 months / 3 months / departure</p>
<p><strong>FAQ:</strong> When do we lock dates? / Do we need both partners on the call? / What about flights? / Can you do destination weddings + honeymoons together?</p>
</div>

<h2>Page 7 — Group Trips &amp; Milestones (M3 build)</h2>
<div class="callout">
<h4>Group Trips Page Spec</h4>
<p><strong>URL:</strong> /groups</p>
<p><strong>Hero h1:</strong> "Twenty people. Five family WhatsApp groups. One trip. We can do this."</p>
<p><strong>Sub-segments:</strong> Bach weekends / 40th birthday groups / Family milestones / Israel pilgrimages / Multi-gen reunions</p>
<p><strong>Process:</strong> Discovery → Group budget alignment → 2-3 destination options → Final pick → Group portal for individual bookings → Day-of coordination</p>
<p><strong>Pricing:</strong> Group planning fee ($1,500-2,500 for 8-15 pax; $3,500-5,000 for 16-30 pax). Refundable through first proposal.</p>
<p><strong>Built on:</strong> Fora Groups platform (launched Oct 2025, $80M+ volume)</p>
</div>

<h2>The Hotel Brand SEO Pages (M6&ndash;9)</h2>
<p>These are pure SEO plays. People search "Excellence Playa Mujeres review" 1,000+ times/month. Build pages targeting those searches.</p>
<table>
<thead><tr><th>Page</th><th>Search target</th><th>Est. monthly searches</th></tr></thead>
<tbody>
<tr><td>/excellence-playa-mujeres-review</td><td>Excellence Playa Mujeres review</td><td>~1,200/mo</td></tr>
<tr><td>/hyatt-prive-all-inclusives</td><td>Hyatt Privé all inclusive</td><td>~400/mo</td></tr>
<tr><td>/le-blanc-spa-cancun-review</td><td>Le Blanc Cancun review</td><td>~600/mo</td></tr>
<tr><td>/sandals-vs-excellence</td><td>Sandals vs Excellence</td><td>~250/mo</td></tr>
<tr><td>/best-all-inclusive-honeymoon-2026</td><td>best all inclusive honeymoon</td><td>~1,800/mo</td></tr>
</tbody>
</table>
<p>Each: 1,500&ndash;2,500 words, your real take, photos, the math, an embedded booking CTA. Long-tail conversion is 3&ndash;8x site average.</p>

<h2>The Deployment Stack</h2>
<table>
<thead><tr><th>Tool</th><th>Use</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>Netlify or Vercel</td><td>Hosting + deployment</td><td>Free up to 100GB bandwidth</td></tr>
<tr><td>Cloudflare</td><td>DNS + caching + analytics</td><td>Free</td></tr>
<tr><td>Beehiiv</td><td>Newsletter + embedded signup forms</td><td>Free → $39/mo at 1K subs</td></tr>
<tr><td>Tally</td><td>Intake forms / lead capture</td><td>Free (up to 10 forms)</td></tr>
<tr><td>Calendly</td><td>Booking calls</td><td>$16/mo</td></tr>
<tr><td>Plausible or PostHog</td><td>Privacy-friendly analytics</td><td>$9&ndash;19/mo</td></tr>
</tbody>
</table>
</section>

<!-- 09 WORKFLOW LIBRARY -->
<section>
<h1><span class="num">Section 09</span>The Workflow Library</h1>
<p class="section-intro">Every repeatable process gets a workflow. Every workflow gets automated where possible. The goal isn't to do less work &mdash; it's to do only the work that requires you.</p>

<h2>9.1 — The Client Journey (Leisure)</h2>
<table>
<thead><tr><th>Stage</th><th>Trigger</th><th>Action</th><th>Owner</th><th>SLA</th></tr></thead>
<tbody>
<tr><td>1. Lead in</td><td>Intake form submitted OR Calendly booked</td><td>Auto-confirm + add to CRM</td><td>Zapier auto</td><td>&lt;1 min</td></tr>
<tr><td>2. Pre-call prep</td><td>Call scheduled</td><td>Review intake answers; pull 2 destination ideas</td><td>You</td><td>15 min day-of</td></tr>
<tr><td>3. Discovery call</td><td>Call time</td><td>Section 10 call structure</td><td>You</td><td>20&ndash;45 min</td></tr>
<tr><td>4. Proposal</td><td>End of call</td><td>1&ndash;3 destination options with hotels + flights + dates</td><td>You + VA</td><td>48 hrs</td></tr>
<tr><td>5. Decision</td><td>Proposal sent</td><td>Follow-up at 24h, 72h, 7d</td><td>You</td><td>7 days</td></tr>
<tr><td>6. Booking</td><td>Client confirms</td><td>Collect planning fee + book</td><td>You</td><td>24 hrs</td></tr>
<tr><td>7. Pre-trip (T-30)</td><td>30 days pre-departure</td><td>Send pre-trip packet: itinerary, weather, packing, restaurant recs</td><td>VA</td><td>&mdash;</td></tr>
<tr><td>8. Departure</td><td>T-2 days</td><td>"Bon voyage" personal message + WhatsApp number</td><td>You</td><td>&mdash;</td></tr>
<tr><td>9. In-trip</td><td>Mid-trip</td><td>Check-in via WhatsApp: "Going OK?"</td><td>You</td><td>&mdash;</td></tr>
<tr><td>10. Return</td><td>T+1 day</td><td>"Welcome back" + photo request + review ask</td><td>You</td><td>24 hrs</td></tr>
<tr><td>11. Referral ask</td><td>T+3 days</td><td>"If you loved it, send one friend"</td><td>You</td><td>&mdash;</td></tr>
<tr><td>12. Annual</td><td>1 yr post</td><td>"Anything on the calendar this year?"</td><td>VA &rarr; You</td><td>&mdash;</td></tr>
</tbody>
</table>

<h2>9.2 — The Business Travel Workflow</h2>
<table>
<thead><tr><th>Trigger</th><th>Action</th><th>SLA</th></tr></thead>
<tbody>
<tr><td>Client texts: "Need NYC Sun&ndash;Wed"</td><td>Reply within 30 min: "On it. Any hotel preference or want me to optimize for points?"</td><td>30 min</td></tr>
<tr><td>Client confirms preference</td><td>Book within 60 min. Confirmation back via same channel.</td><td>60 min</td></tr>
<tr><td>Booking auto-flows to client's Hyatt/Marriott/Hilton account (loyalty number on file)</td><td>Verify amenity package attached (Privé/STARS)</td><td>10 min</td></tr>
<tr><td>Trip 24h out</td><td>Auto-send: "Heads up &mdash; you're booked tomorrow, room confirmed [type], $100 credit on file"</td><td>&mdash;</td></tr>
<tr><td>Trip disruption (flight delay, hotel issue)</td><td>Client texts. You respond within 15 min, fix it.</td><td>15 min</td></tr>
<tr><td>Monthly</td><td>Trip summary email: nights, total spend, perks captured</td><td>&mdash;</td></tr>
</tbody>
</table>

<h2>9.3 — The Cold-Outreach Reply Triage (Daily, VA-owned)</h2>
<p>Cold outreach generates 5&ndash;25 replies per day. VA processes them in three buckets:</p>
<table>
<thead><tr><th>Bucket</th><th>Definition</th><th>Action</th></tr></thead>
<tbody>
<tr><td>A — Hot</td><td>Specific trip intent OR partnership interest with details</td><td>Slack you immediately; you book a call within 24h</td></tr>
<tr><td>B — Warm</td><td>"Tell me more" type replies, no specifics</td><td>VA sends pre-approved follow-up; if engaged, escalate to A</td></tr>
<tr><td>C — Nurture</td><td>"Not now, maybe later"</td><td>Add to 90-day quarterly newsletter list</td></tr>
<tr><td>D — Bounce/Decline</td><td>"Unsubscribe", "Not interested", "Wrong person"</td><td>VA removes from list immediately</td></tr>
</tbody>
</table>

<h2>9.4 — The Content Production Workflow (Weekly)</h2>
<table>
<thead><tr><th>Day</th><th>Step</th><th>Owner</th><th>Output</th></tr></thead>
<tbody>
<tr><td>Mon</td><td>Founder records 5&ndash;8 min voice memo on topic of week</td><td>You</td><td>1 voice memo</td></tr>
<tr><td>Mon</td><td>Forward 1&ndash;2 client photos (anonymized) to VA</td><td>You</td><td>Visuals</td></tr>
<tr><td>Tue</td><td>VA transcribes + drafts: newsletter, 1 LinkedIn post, 1 IG carousel script, 1 TikTok script</td><td>VA</td><td>Drafts</td></tr>
<tr><td>Wed</td><td>VA designs IG carousel in Canva + edits any video</td><td>VA</td><td>Assets ready</td></tr>
<tr><td>Thu</td><td>You review batch (~30 min). Approve or send 1&ndash;2 line edits.</td><td>You</td><td>Approved batch</td></tr>
<tr><td>Fri</td><td>VA publishes newsletter Fri 10am ET, then schedules week's social via Buffer/Later</td><td>VA</td><td>Live + queued</td></tr>
<tr><td>Sat</td><td>You record 2 TikToks (15&ndash;30 min batch)</td><td>You</td><td>Raw clips</td></tr>
<tr><td>Sun</td><td>VA edits TikToks + Reels, schedules for Mon/Wed/Fri</td><td>VA</td><td>Queued</td></tr>
</tbody>
</table>
<p>Total weekly founder time on content: <strong>~90 minutes.</strong></p>

<h2>9.5 — The Partnership Pipeline Workflow</h2>
<ol>
<li><strong>Identify (week 0):</strong> Add to Notion partnership pipeline w/ score (1&ndash;10 on referral-likelihood).</li>
<li><strong>First touch (week 1):</strong> DM or warm intro request. Calendar coffee.</li>
<li><strong>Coffee (week 2):</strong> Section 05 pitch. If interested, send agreement same day.</li>
<li><strong>Sign (week 2&ndash;3):</strong> DocuSign or PDF e-signed. Send Welcome Pack.</li>
<li><strong>First referral check-in (week 7):</strong> "Anyone on the radar?"</li>
<li><strong>Monthly check-in (months 2&ndash;6):</strong> Update on activity + new content.</li>
<li><strong>Quarterly review (month 3, 6, 9, 12):</strong> 15-min call. Performance review + recommit or graceful drop.</li>
</ol>

<h2>9.6 — The Booking Workflow (Inside Fora Portal)</h2>
<ol>
<li>Client confirms booking via Calendly + payment of planning fee.</li>
<li>Fora portal: search hotel, layer Privé/STARS/Virtuoso amenity, confirm rate.</li>
<li>If applicable, book through Fora Reserve / Hyatt Privé / FSPP portal for direct amenity attribution.</li>
<li>Cross-check: rate + room category + amenity package matches proposal.</li>
<li>Confirm booking; send client confirmation with full details + amenity list.</li>
<li>Add to CRM: booking record, expected commission, planning fee captured.</li>
<li>Set 30/14/2-day pre-trip reminders.</li>
</ol>

<h2>9.7 — The Automation Layer (Zapier / Make.com)</h2>
<table>
<thead><tr><th>Zap</th><th>Trigger</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Z1: Lead capture</td><td>Tally form submitted</td><td>Create CRM record + send Slack notif + auto-confirm email</td></tr>
<tr><td>Z2: Call booked</td><td>Calendly confirmed</td><td>Create CRM activity + send prep checklist email</td></tr>
<tr><td>Z3: Newsletter signup</td><td>Beehiiv new subscriber</td><td>Add to CRM "Newsletter list" segment</td></tr>
<tr><td>Z4: Booking confirmed</td><td>Fora booking added (via email parse)</td><td>Create commission tracking row + set follow-up reminders</td></tr>
<tr><td>Z5: Cold reply triage</td><td>Reply email received</td><td>Forward to VA Slack channel for triage</td></tr>
</tbody>
</table>
</section>

<!-- 10 SALES CONVERSATIONS -->
<section>
<h1><span class="num">Section 10</span>The Sales Conversation Playbook</h1>
<p class="section-intro">Closing is just discovery + match + ask. Most travel advisors over-talk and under-listen.</p>

<h2>The 20-Minute Discovery Call (Leisure)</h2>
<table>
<thead><tr><th>Min</th><th>Phase</th><th>What you do / say</th></tr></thead>
<tbody>
<tr><td>0&ndash;2</td><td>Rapport + agenda</td><td>"Thanks for booking. Quick agenda: I'll ask about your trip ideas + budget for ~12 min, then I'll give you 2&ndash;3 recommendations and we'll figure out next steps. Sound good?"</td></tr>
<tr><td>2&ndash;6</td><td>Trip context</td><td>"What's the trip you're thinking about?" Open ended. Let them talk. Note: occasion, destination ideas, dates, who's going.</td></tr>
<tr><td>6&ndash;10</td><td>Budget + priorities</td><td>"What kind of budget are you thinking? Total or per-person?" THEN: "If you had to rank these &mdash; resort experience, location, food, value &mdash; what's most important?"</td></tr>
<tr><td>10&ndash;14</td><td>Surface preferences</td><td>"Have you stayed at all-inclusives before? Which ones?" or "Beach vs. cities?" Calibrate.</td></tr>
<tr><td>14&ndash;17</td><td>Match + recommend</td><td>Recommend 1&ndash;2 properties on the spot. "Based on what you said, I'd be looking at [Hyatt Ziva Cap Cana] for your $4K/pp budget &mdash; here's why."</td></tr>
<tr><td>17&ndash;19</td><td>Next steps</td><td>"Want me to put together a formal proposal with hotel + flight options? Planning fee is $300; refundable through the first revision if it's not right."</td></tr>
<tr><td>19&ndash;20</td><td>Close</td><td>"Sound good? I'll send a Stripe link in 10 min. Once it's in, proposal hits your inbox within 48 hrs."</td></tr>
</tbody>
</table>

<h2>The 10 Most Common Objections (With Verbatim Responses)</h2>

<div class="script-box">
<div class="lab">Objection 1: "Booking.com is cheaper"</div>
"It's the same price, actually &mdash; that's the part most people miss. The hotel publishes one rate; whether you book on Booking, Expedia, or through me, the rate is identical. The difference is what arrives in your room. Through me, you get a confirmed room upgrade, daily breakfast for two, and $100 in resort credits &mdash; all paid by the hotel out of their marketing budget. Booking.com keeps that money for themselves. Want me to send you a side-by-side example?"
</div>

<div class="script-box">
<div class="lab">Objection 2: "I usually just book myself"</div>
"Totally fair &mdash; honestly, for a Holiday Inn in Buffalo I'd say keep doing it yourself. Where I add real value is on the trips you're spending 4 figures or more on, where the upgrade-and-amenity package alone is worth $500&ndash;1,500. Want me to ballpark what your last big trip would have looked like through me, just so you can decide?"
</div>

<div class="script-box">
<div class="lab">Objection 3: "What's your fee?"</div>
"Most of what I do is paid by the hotel commission &mdash; meaning free to you. For more complex trips (multi-stop, custom planning), I charge a planning fee that ranges from $300 for a simple honeymoon to $2,500 for a 20-person family pilgrimage. The fee covers the planning work &mdash; the actual bookings are still at zero markup. Let me know roughly what you're thinking and I'll tell you upfront."
</div>

<div class="script-box">
<div class="lab">Objection 4: "Can you get me a deal?"</div>
"Honest answer: not on the rate. Hotels enforce rate parity &mdash; I can't price under what they publish. What I CAN do is layer real upgrade value on top: a $400 room becomes a $700 room, you get $200 in credit and breakfast, and a human in your corner if something breaks. On a $5K trip, that's usually about $1,000&ndash;1,500 of upside at zero extra cost. That's the real 'deal.'"
</div>

<div class="script-box">
<div class="lab">Objection 5: "Sunwing has this trip for $3K/pp"</div>
"That's a packaged charter deal &mdash; Sunwing buys the flights and rooms in bulk and bundles them. I literally can't match it because it's not the same product. For mass-market all-inclusives, Sunwing wins on price &mdash; full stop. Where I beat them is at the next tier up: Hyatt Privé properties (Secrets/Dreams/Zoëtry), Excellence, Le Blanc &mdash; resorts where Sunwing doesn't have an inventory deal but I have a Privé amenity package. Often it's $300&ndash;500/pp more, but you arrive to a club-level suite with $200 in resort credits. Want me to spec one out as a comparison?"
</div>

<div class="script-box">
<div class="lab">Objection 6: "I need to think about it / check with my partner"</div>
"Of course. Two things to make that easier: I'll send a 1-page summary by EOD with the 2&ndash;3 options + amenities + total cost so you both can review. And I'll hold the planning slot for 5 business days &mdash; after that, the proposal slot moves to the next client in queue. Sound fair?"
</div>

<div class="script-box">
<div class="lab">Objection 7: "We were thinking of doing it through [destination wedding planner]"</div>
"Great planner. Quick thing: travel-advisor work and wedding-planning work are different scopes. Wedding planners do the venue, decor, ceremony logistics &mdash; I do the hotel bookings, room blocks, flights, and guest-side logistics. They actually work great together. Want me to coordinate directly with your planner so we're not doubling up?"
</div>

<div class="script-box">
<div class="lab">Objection 8: "Are you certified? How long have you been doing this?"</div>
"Yes &mdash; TICO-certified [#XXXX], independent advisor with Fora (Virtuoso member, FSPP, Hyatt Privé, etc.). I started in [Month/Year]. What I bring that some longer-tenured advisors don't: I've personally stayed at 20+ all-inclusives, so when you ask me about Excellence Playa Mujeres I'm not reading a brochure. That's the unfair advantage I lean on."
</div>

<div class="script-box">
<div class="lab">Objection 9: "Can you do this for less than [budget]?"</div>
"I can show you options at $X, $Y, and $Z so you can see the trade-offs &mdash; and tell you which one I'd pick if it were my honeymoon. Sometimes the answer is: you'd be better off going a tier up because the amenity package closes the gap. Sometimes it's: you'd be better off going a different week. Let me put two options together and you can decide."
</div>

<div class="script-box">
<div class="lab">Objection 10: "When do I need to decide by?"</div>
"For [destination] in [month], the smart-book window is [X weeks] out for best rates + room category. After that, you start losing inventory at the better resorts. If you can decide in the next 10 days, we're in great shape. Beyond 4 weeks from now, we'll start seeing higher prices."
</div>

<h2>The Three Closing Moves</h2>
<ol>
<li><strong>Soft close:</strong> "Want me to put a hold on those dates while you think?" (No commitment from them. Gives you sales momentum.)</li>
<li><strong>Medium close:</strong> "If I send you a proposal by [Friday], are you in a position to make a decision next week?" (Reveals their actual readiness.)</li>
<li><strong>Hard close:</strong> "We've covered the options. Want to go with [Option B] and I'll get it booked tomorrow morning?" (Direct ask. Used when the buying signals are strong.)</li>
</ol>
</section>

<!-- 11 KPI DASHBOARD -->
<section>
<h1><span class="num">Section 11</span>The KPI Dashboard</h1>
<p class="section-intro">What you measure is what you manage. What you don't measure dies in silence.</p>

<h2>The Single Number: Net Commission Booked (Weekly)</h2>
<div class="hormozi-rule">
<div class="label">North Star</div>
<div class="rule">One number rules them all: <strong>Net Commission Booked This Week</strong>. Computed every Friday at 5pm. Year 1 target: ramp from $0 to $2,500/wk by Day 300. If this number is flat for 3 consecutive weeks, you have a problem. If it's growing, the rest of the dashboard is leading-indicator noise.</div>
</div>

<h2>Daily KPIs (Track in 5 minutes)</h2>
<table>
<thead><tr><th>Metric</th><th>Target (M3+)</th><th>How to track</th></tr></thead>
<tbody>
<tr><td>Outbound activity (cold + warm)</td><td>50&ndash;100/day</td><td>Instantly + manual log</td></tr>
<tr><td>Replies received</td><td>10&ndash;30/day</td><td>Inbox + VA report</td></tr>
<tr><td>Calls booked</td><td>2&ndash;4/day</td><td>Calendly</td></tr>
<tr><td>Proposals sent</td><td>1&ndash;3/day</td><td>CRM</td></tr>
<tr><td>Bookings closed</td><td>0.5&ndash;1.5/day (M3+)</td><td>Fora + CRM</td></tr>
</tbody>
</table>

<h2>Weekly KPIs (Friday 5pm review, 30 min)</h2>
<table>
<thead><tr><th>Metric</th><th>M1&ndash;3 target</th><th>M4&ndash;6 target</th><th>M7&ndash;12 target</th></tr></thead>
<tbody>
<tr><td>Net Commission Booked</td><td>$1,000&ndash;1,500</td><td>$1,500&ndash;2,000</td><td>$2,500+</td></tr>
<tr><td>New leads added (all funnels)</td><td>20&ndash;40</td><td>40&ndash;80</td><td>80&ndash;150</td></tr>
<tr><td>New calls booked</td><td>5&ndash;10</td><td>10&ndash;15</td><td>15&ndash;25</td></tr>
<tr><td>Bookings closed</td><td>3&ndash;5</td><td>5&ndash;7</td><td>7&ndash;12</td></tr>
<tr><td>Win rate (proposal → booking)</td><td>40%</td><td>50%</td><td>60%</td></tr>
<tr><td>Avg booking size (gross)</td><td>$4K</td><td>$5K</td><td>$6K</td></tr>
<tr><td>Newsletter subs added</td><td>10&ndash;30</td><td>50&ndash;100</td><td>100&ndash;200</td></tr>
<tr><td>Social followers added (IG+TikTok+LI)</td><td>20&ndash;50</td><td>100&ndash;300</td><td>300&ndash;800</td></tr>
</tbody>
</table>

<h2>Monthly KPIs (Last Friday, 60 min)</h2>
<table>
<thead><tr><th>Metric</th><th>M1&ndash;3</th><th>M4&ndash;6</th><th>M7&ndash;12</th></tr></thead>
<tbody>
<tr><td>Gross commission revenue</td><td>$3&ndash;7K</td><td>$8&ndash;13K</td><td>$14&ndash;22K</td></tr>
<tr><td>Net commission (after Fora 30%)</td><td>$2&ndash;5K</td><td>$5.5&ndash;9K</td><td>$10&ndash;15K</td></tr>
<tr><td>Planning fees collected</td><td>$0.5&ndash;2K</td><td>$1&ndash;3K</td><td>$2&ndash;5K</td></tr>
<tr><td>Total revenue</td><td>$2.5&ndash;7K</td><td>$6.5&ndash;12K</td><td>$12&ndash;20K</td></tr>
<tr><td>Active partnerships</td><td>1&ndash;3</td><td>5&ndash;8</td><td>10&ndash;15</td></tr>
<tr><td>Business travel accounts</td><td>0</td><td>1&ndash;2</td><td>4&ndash;8</td></tr>
<tr><td>Newsletter subs (cumulative)</td><td>50&ndash;200</td><td>500&ndash;1,200</td><td>2,500&ndash;5,000</td></tr>
<tr><td>Cost of operation</td><td>~$1K</td><td>~$2K</td><td>~$3K</td></tr>
</tbody>
</table>

<h2>Quarterly Review (Day 1 of Q2, Q3, Q4)</h2>
<ol>
<li><strong>Compare actuals vs plan.</strong> Identify the biggest variance (positive or negative).</li>
<li><strong>Funnel ROI:</strong> Which channel produced the most $/hour of effort? Which the least?</li>
<li><strong>Kill candidates:</strong> Any channel below 1.5x time-cost-to-revenue gets a 30-day notice.</li>
<li><strong>Scale candidates:</strong> Channel above 3x time-cost-to-revenue gets doubled resource.</li>
<li><strong>Next-quarter priorities:</strong> 3 things, no more.</li>
</ol>

<h2>The Dashboard Itself (Build It)</h2>
<p>Build a Notion or Google Sheets dashboard that auto-updates from your tools:</p>
<table>
<thead><tr><th>Tile</th><th>Source</th><th>Update cadence</th></tr></thead>
<tbody>
<tr><td>Weekly Net Commission</td><td>Manual from Fora + CRM</td><td>Friday 5pm</td></tr>
<tr><td>Pipeline value (forecast)</td><td>CRM sum of open proposals × win rate</td><td>Live</td></tr>
<tr><td>Newsletter subs</td><td>Beehiiv API</td><td>Daily</td></tr>
<tr><td>Cold-email reply rate</td><td>Instantly dashboard</td><td>Daily</td></tr>
<tr><td>Partner referral count</td><td>CRM</td><td>Weekly</td></tr>
<tr><td>BT trips this month</td><td>Manual from BT log</td><td>Weekly</td></tr>
</tbody>
</table>
</section>

<!-- 12 TOOL STACK -->
<section>
<h1><span class="num">Section 12</span>Tool Stack &amp; Cost Schedule</h1>
<p class="section-intro">Every tool. Every cost. Every link. Buy them in this order.</p>

<h2>Month 1 — Foundation Stack (~$200 setup)</h2>
<div class="tool-row header">
    <div>Tool</div><div>Purpose</div><div>Cost/mo</div><div>Link / signup notes</div>
</div>
<div class="tool-row"><div>TICO Certification</div><div>Required ON license</div><div>$150 one-time</div><div>tico.ca (study course)</div></div>
<div class="tool-row"><div>Fora Travel</div><div>Primary host agency</div><div>$399/yr ($33/mo)</div><div>foratravel.com/join &mdash; Canada cohort</div></div>
<div class="tool-row"><div>TTAND</div><div>Secondary host (Cdn tour ops)</div><div>$50&ndash;100/mo</div><div>thetravelagentnextdoor.com</div></div>
<div class="tool-row"><div>Domain (preface.travel)</div><div>Site URL</div><div>$40/yr</div><div>Cloudflare or Namecheap</div></div>
<div class="tool-row"><div>Google Workspace</div><div>Email + Drive</div><div>$7/mo</div><div>workspace.google.com</div></div>
<div class="tool-row"><div>Calendly</div><div>Call booking</div><div>$16/mo</div><div>calendly.com</div></div>
<div class="tool-row"><div>Tally</div><div>Intake forms</div><div>Free</div><div>tally.so</div></div>
<div class="tool-row"><div>Beehiiv</div><div>Newsletter</div><div>Free → $39/mo at 1K subs</div><div>beehiiv.com</div></div>
<div class="tool-row"><div>Notion</div><div>CRM + ops + SOPs</div><div>Free (personal)</div><div>notion.so</div></div>
<div class="tool-row"><div>Canva Pro</div><div>Design (carousels, decks)</div><div>$13/mo</div><div>canva.com</div></div>
<div class="tool-row"><div>Netlify or Vercel</div><div>Site hosting</div><div>Free</div><div>netlify.com or vercel.com</div></div>

<h2>Month 2&ndash;3 — Outreach Stack (+$200/mo)</h2>
<div class="tool-row header">
    <div>Tool</div><div>Purpose</div><div>Cost/mo</div><div>Link / signup notes</div>
</div>
<div class="tool-row"><div>Instantly</div><div>Cold email at scale</div><div>$97/mo</div><div>instantly.ai &mdash; growth plan</div></div>
<div class="tool-row"><div>Apollo</div><div>Lead lists + enrichment</div><div>$79/mo</div><div>apollo.io &mdash; basic plan</div></div>
<div class="tool-row"><div>Second sending domain (preface-co.com etc.)</div><div>Deliverability isolation</div><div>$15/yr × 2 = $30/yr</div><div>Cloudflare</div></div>
<div class="tool-row"><div>VA (Filipino, outreach/admin)</div><div>Reply triage + admin</div><div>$400&ndash;600/mo</div><div>OnlineJobs.ph</div></div>

<h2>Month 4&ndash;6 — Content Stack (+$1,500/mo)</h2>
<div class="tool-row header">
    <div>Tool</div><div>Purpose</div><div>Cost/mo</div><div>Link / signup notes</div>
</div>
<div class="tool-row"><div>Content VA / Contractor</div><div>Newsletter + social production</div><div>$1,200&ndash;1,800/mo</div><div>Upwork (Toronto/Buenos Aires) or OnlineJobs.ph</div></div>
<div class="tool-row"><div>Toronto editor (top 5 posts/mo)</div><div>Voice calibration</div><div>$300&ndash;500/mo</div><div>Twitter / Ryerson grads</div></div>
<div class="tool-row"><div>Buffer or Later</div><div>Social scheduling</div><div>$15/mo</div><div>buffer.com</div></div>
<div class="tool-row"><div>CapCut Pro</div><div>Video editing</div><div>$8/mo</div><div>capcut.com</div></div>
<div class="tool-row"><div>ChatGPT Plus / Claude Pro</div><div>Content + comms drafting</div><div>$20/mo</div><div>openai.com or claude.ai</div></div>
<div class="tool-row"><div>Plausible Analytics</div><div>Privacy-friendly site analytics</div><div>$9/mo</div><div>plausible.io</div></div>

<h2>Month 6+ — CRM &amp; Automation (+$200/mo)</h2>
<div class="tool-row header">
    <div>Tool</div><div>Purpose</div><div>Cost/mo</div><div>Link / signup notes</div>
</div>
<div class="tool-row"><div>HubSpot Starter (CRM)</div><div>Pipeline + email tracking</div><div>$45/mo</div><div>hubspot.com (or stay on Notion)</div></div>
<div class="tool-row"><div>Zapier</div><div>Automation glue</div><div>$29/mo (starter)</div><div>zapier.com</div></div>
<div class="tool-row"><div>DocuSign Personal</div><div>Partnership agreements</div><div>$15/mo</div><div>docusign.com</div></div>
<div class="tool-row"><div>QuickBooks Self-Employed</div><div>Bookkeeping + tax</div><div>$15/mo</div><div>intuit.com</div></div>
<div class="tool-row"><div>E&amp;O Insurance (Errors &amp; Omissions)</div><div>Required for advisor practice</div><div>$80&ndash;120/mo</div><div>via TICO directory</div></div>

<h2>Year 2 Add-ons (per growth)</h2>
<table>
<thead><tr><th>Tool</th><th>When</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>Slack (with team)</td><td>When first sub-advisor onboards</td><td>$10/user/mo</td></tr>
<tr><td>Loom Pro (video proposals)</td><td>Once proposals get complex</td><td>$15/mo</td></tr>
<tr><td>SparkLoop (newsletter cross-promo)</td><td>At 2K+ newsletter subs</td><td>$59/mo</td></tr>
<tr><td>Beehiiv Boosts</td><td>Paid newsletter growth</td><td>Pay-per-sub ($1&ndash;3 ea)</td></tr>
<tr><td>HubSpot Pro</td><td>When CRM is &gt;1,500 contacts</td><td>$450/mo</td></tr>
</tbody>
</table>

<h2>Total Cost by Phase</h2>
<table>
<thead><tr><th>Phase</th><th>Monthly run-rate</th><th>Annualized</th></tr></thead>
<tbody>
<tr><td>M1</td><td>~$200</td><td>$2,400</td></tr>
<tr><td>M2&ndash;3</td><td>~$700</td><td>$8,400</td></tr>
<tr><td>M4&ndash;6</td><td>~$2,200</td><td>$26,400</td></tr>
<tr><td>M7&ndash;12</td><td>~$2,800</td><td>$33,600</td></tr>
<tr><td>Y2 steady</td><td>~$5,000</td><td>$60,000</td></tr>
</tbody>
</table>
<p>At Y1 net commission of ~$100K, total opex ($25K) is 25% &mdash; healthy. At Y2 steady-state of $250K+ net commission, opex of $60K is 24%. Same ratio. The math holds.</p>
</section>

<!-- 13 DECISION TREES -->
<section>
<h1><span class="num">Section 13</span>Decision Trees &amp; Pivot Triggers</h1>

<h2>When to Hire</h2>
<table>
<thead><tr><th>Role</th><th>Hire when...</th><th>Approx month</th></tr></thead>
<tbody>
<tr><td>Outreach VA (reply triage + admin)</td><td>You spend &gt;5 hrs/wk on admin OR cold replies are above 20/day</td><td>M2&ndash;3</td></tr>
<tr><td>Content VA</td><td>Content production becomes a bottleneck OR you skip 2+ newsletters in a row</td><td>M3&ndash;4</td></tr>
<tr><td>Toronto editor / content lead</td><td>Voice-drift in content is becoming a problem (you're rewriting too much)</td><td>M5&ndash;6</td></tr>
<tr><td>First sub-advisor</td><td>You're turning away &gt;3 leads/month for capacity reasons</td><td>M18&ndash;24</td></tr>
<tr><td>Ops / client services lead</td><td>You're spending &gt;10 hrs/wk on booking ops (not closing)</td><td>M24&ndash;30</td></tr>
<tr><td>FT content producer</td><td>Personal income passes Target ($30K/mo)</td><td>M30+</td></tr>
</tbody>
</table>

<h2>When to Quit the Day Job</h2>
<div class="callout warn">
<h4>Dual-Trigger Required (Both)</h4>
<ol>
<li><strong>Business condition:</strong> Net commission averaging $2,500/wk for 8 consecutive weeks AND</li>
<li><strong>Runway condition:</strong> $30K savings buffer (6 months of $5K/mo personal burn) accumulated separately</li>
</ol>
<p>Expected trigger window: <strong>Month 13&ndash;18</strong>. Earlier than 13 is reckless (no buffer). Later than 18 means the business is under-performing and you should rethink.</p>
</div>

<h2>When to Drop a Channel</h2>
<table>
<thead><tr><th>Channel</th><th>Kill trigger</th></tr></thead>
<tbody>
<tr><td>Cold email</td><td>&lt;3 bookings/mo after 90 days at full volume, after copy/deliverability/list iteration</td></tr>
<tr><td>A partnership</td><td>0 referrals after 9 months OR partner stops responding to monthly check-in</td></tr>
<tr><td>A social channel</td><td>Doesn't 2x followers in a quarter for 2 consecutive quarters</td></tr>
<tr><td>Newsletter</td><td>Never. Newsletter is your owned channel. Adjust the format if open rate drops below 25%, but don't kill.</td></tr>
<tr><td>A booking segment</td><td>If you're handling &gt;3 bookings/mo in a segment that nets &lt;$200/booking, charge a higher planning fee or refer out</td></tr>
</tbody>
</table>

<h2>When to Pivot the Brand</h2>
<p><strong>Don't.</strong> Brand pivots in Y1 are usually procrastination. The brand is set. The only pivot worth making in Y1 is the <strong>segment mix</strong>: if your bookings are 70%+ from one type (e.g., bach trips), tilt outreach to balance. The brand stays.</p>

<h2>The Six Risk Triggers (Watch Weekly)</h2>
<table>
<thead><tr><th>Signal</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Net commission flat for 3 weeks</td><td>Run the funnel-by-funnel audit. Find the broken one.</td></tr>
<tr><td>Cold reply rate drops below 1%</td><td>Audit deliverability first (Glock Apps test), then copy, then list.</td></tr>
<tr><td>Partner referral pipeline drying up</td><td>Re-book 5 coffees. Onboard 3 new partners.</td></tr>
<tr><td>Newsletter open rate drops below 30%</td><td>Audit subject lines + sender reputation. Re-engage cold subs with a "Hey, still want this?" email.</td></tr>
<tr><td>Day-job interfering with business consistently (3+ weeks of missed targets)</td><td>Negotiate reduced hours OR start exit planning.</td></tr>
<tr><td>Personal energy depleted (3+ weeks of 60+ hr weeks with no progress)</td><td>Take a full weekend off. Drop the lowest-ROI activity. Reassess capacity.</td></tr>
</tbody>
</table>
</section>

<!-- 14 MONTH BY MONTH -->
<section>
<h1><span class="num">Section 14</span>Month-by-Month Goals (M1&ndash;M24)</h1>

<h2>Phase 1 — Foundation (M1&ndash;3)</h2>
<table>
<thead><tr><th>Month</th><th>Primary goal</th><th>Bookings (cum.)</th><th>Net revenue (cum.)</th><th>Key milestones</th></tr></thead>
<tbody>
<tr><td>M1</td><td>Licensed, launched, warm network activated (Wave 1&ndash;2)</td><td>5&ndash;8</td><td>$3&ndash;6K</td><td>TICO + Fora live, 100/150 warm contacted, 1 partnership signed</td></tr>
<tr><td>M2</td><td>Cold outreach live, 3 partnerships, content rhythm</td><td>13&ndash;17</td><td>$10&ndash;15K</td><td>1500 emails/day, VA hired, 3 newsletters out, 1st content VA</td></tr>
<tr><td>M3</td><td>All 5 funnels in motion</td><td>22&ndash;30</td><td>$18&ndash;25K</td><td>5 partnerships, content engine 90% outsourced, BT outreach starts</td></tr>
</tbody>
</table>

<h2>Phase 2 — Scale (M4&ndash;6)</h2>
<table>
<thead><tr><th>Month</th><th>Primary goal</th><th>Bookings (cum.)</th><th>Net revenue (cum.)</th><th>Key milestones</th></tr></thead>
<tbody>
<tr><td>M4</td><td>$1,500/wk avg net commission stable, 1st BT account</td><td>35&ndash;45</td><td>$30&ndash;40K</td><td>Newsletter at 600 subs, 1 BT account onboarded, all 5 funnels producing</td></tr>
<tr><td>M5</td><td>Optimize the highest-ROI funnel</td><td>50&ndash;62</td><td>$45&ndash;55K</td><td>2&ndash;3 BT accounts, 8 partnerships, IG at 2,500 followers</td></tr>
<tr><td>M6</td><td>$2,000/wk avg, content compounding</td><td>67&ndash;80</td><td>$60&ndash;75K</td><td>3 BT accounts, 10 partnerships, newsletter at 1,200 subs</td></tr>
</tbody>
</table>

<h2>Phase 3 — Compound (M7&ndash;12)</h2>
<table>
<thead><tr><th>Month</th><th>Primary goal</th><th>Bookings (cum.)</th><th>Net revenue (cum.)</th><th>Key milestones</th></tr></thead>
<tbody>
<tr><td>M7&ndash;8</td><td>Day-job-exit window opens (Happy tier $15K/mo)</td><td>95&ndash;115</td><td>$80&ndash;100K</td><td>$2,000&ndash;2,500/wk, 5 BT accounts, 12 partnerships, IG 5K</td></tr>
<tr><td>M9&ndash;10</td><td>Hit Pro tier at Fora ($100K commissionable cumulative)</td><td>130&ndash;160</td><td>$110&ndash;140K</td><td>Pro tier unlocks (Virtuoso login + IATA + CLIA + flights desk)</td></tr>
<tr><td>M11&ndash;12</td><td>$2,500/wk locked, day-job exit if dual trigger met</td><td>180&ndash;200</td><td>$155&ndash;180K</td><td>5&ndash;8 BT accounts, 15 partnerships, newsletter at 2,500 subs, IG 8K, TikTok 5K</td></tr>
</tbody>
</table>

<h2>Phase 4 — Solo Peak (M13&ndash;18)</h2>
<table>
<thead><tr><th>Month</th><th>Primary goal</th><th>Bookings (cum.)</th><th>Net revenue (cum.)</th><th>Key milestones</th></tr></thead>
<tbody>
<tr><td>M13&ndash;14</td><td>Day job exited (assuming trigger met), full-time on Preface</td><td>220&ndash;250</td><td>$200&ndash;230K</td><td>Capacity doubles. Funnels scale.</td></tr>
<tr><td>M15&ndash;16</td><td>Approaching Satisfied tier ($20K/mo); first sub-advisor identified</td><td>275&ndash;310</td><td>$250&ndash;290K</td><td>10 BT accounts, 18 partnerships, IG 15K</td></tr>
<tr><td>M17&ndash;18</td><td>First sub-advisor onboarded (Fora team-leader role)</td><td>340&ndash;380</td><td>$320&ndash;360K</td><td>First override revenue starts. Personal capacity preserved.</td></tr>
</tbody>
</table>

<h2>Phase 5 — Team Build (M19&ndash;24)</h2>
<table>
<thead><tr><th>Month</th><th>Primary goal</th><th>Bookings (cum.)</th><th>Net revenue (cum.)</th><th>Key milestones</th></tr></thead>
<tbody>
<tr><td>M19&ndash;20</td><td>Sub-advisor #1 producing; you maintain solo flow</td><td>420&ndash;470</td><td>$390&ndash;440K</td><td>Brand pulling inbound. Cold less critical.</td></tr>
<tr><td>M21&ndash;22</td><td>Sub-advisor #2 onboarded; ops process documented</td><td>510&ndash;570</td><td>$470&ndash;530K</td><td>15 BT accounts, 25 partnerships</td></tr>
<tr><td>M23&ndash;24</td><td>Target tier ($30K/mo) hit; 3-person practice operating</td><td>610&ndash;680</td><td>$560&ndash;640K</td><td>Y3 enters with team-driven growth, BT recurring base $200K+/yr</td></tr>
</tbody>
</table>
</section>

<!-- APPENDIX -->
<section>
<h1><span class="num">Appendix A</span>Templates, Scripts &amp; Checklists</h1>

<h2>A.1 — The 90-Day Launch Checklist (Print This)</h2>

<h3>Week 1</h3>
<ul class="check-list">
<li>TICO course bought + study schedule blocked</li>
<li>Fora Canada application submitted</li>
<li>TTAND application submitted</li>
<li>Domain bought (preface.travel) + Google Workspace set up</li>
<li>150-person warm network sheet built</li>
</ul>

<h3>Week 2</h3>
<ul class="check-list">
<li>Website live (B-hybrid deployed via Netlify)</li>
<li>Calendly + Tally configured</li>
<li>Social handles claimed (IG, TikTok, LinkedIn)</li>
<li>Beehiiv newsletter brand built</li>
<li>Cold-email infrastructure wired by contractor (Instantly + Apollo)</li>
</ul>

<h3>Week 3</h3>
<ul class="check-list">
<li>TICO exam passed</li>
<li>First 50 warm-network messages sent</li>
<li>5 partnership coffees scheduled</li>
<li>First content voice memo recorded</li>
</ul>

<h3>Week 4</h3>
<ul class="check-list">
<li>Next 50 warm-network messages sent (cum: 100)</li>
<li>3+ coffees completed</li>
<li>First proposal sent</li>
<li>First booking closed</li>
<li>CRM set up (HubSpot Starter or Notion)</li>
</ul>

<h3>Week 5</h3>
<ul class="check-list">
<li>Final 50 warm-network messages sent (cum: 150)</li>
<li>First partnership agreement signed</li>
<li>First newsletter published</li>
<li>3&ndash;5 bookings cumulative</li>
</ul>

<h3>Week 6</h3>
<ul class="check-list">
<li>Cold email live at 200/day</li>
<li>Outreach VA hired + trained</li>
<li>2nd partnership signed</li>
<li>2nd newsletter</li>
<li>7 bookings cumulative</li>
</ul>

<h3>Week 7</h3>
<ul class="check-list">
<li>Content VA hired (Toronto/BA)</li>
<li>3rd partnership signed</li>
<li>Cold email at 400/day</li>
<li>Daily KPI dashboard live</li>
</ul>

<h3>Week 8&mdash;12 — Continue (see Section 03)</h3>

<h2>A.2 — Email Templates Quick Reference</h2>
<table>
<thead><tr><th>Template</th><th>Use case</th><th>Section</th></tr></thead>
<tbody>
<tr><td>A: Tier 1 warm network</td><td>Friends/family with trip intent</td><td>04</td></tr>
<tr><td>B: Tier 2 warm network</td><td>Referral sources</td><td>04</td></tr>
<tr><td>C: Tier 3 warm network</td><td>Partnership candidates</td><td>04</td></tr>
<tr><td>D: Partnership coffee pitch</td><td>3-min coffee pitch</td><td>05</td></tr>
<tr><td>E: BT LinkedIn touch 1</td><td>Connection request</td><td>06</td></tr>
<tr><td>F: BT LinkedIn touch 2</td><td>Soft hello post-acceptance</td><td>06</td></tr>
<tr><td>G: BT LinkedIn touch 3</td><td>Value drop</td><td>06</td></tr>
<tr><td>H: BT LinkedIn touch 4</td><td>The specific ask</td><td>06</td></tr>
<tr><td>I: BT LinkedIn touch 5</td><td>The closer</td><td>06</td></tr>
<tr><td>J: Pre-trip packet (T-30)</td><td>30 days pre-departure</td><td>09</td></tr>
<tr><td>K: Welcome back + photo + review ask</td><td>T+1 day return</td><td>09</td></tr>
<tr><td>L: Referral ask</td><td>T+3 days return</td><td>04</td></tr>
<tr><td>M: Annual re-touch</td><td>1 year post booking</td><td>09</td></tr>
</tbody>
</table>

<h2>A.3 — The One-Page Founder Schedule (Day Job + Business)</h2>
<table>
<thead><tr><th>Time block</th><th>Activity</th><th>Channel</th></tr></thead>
<tbody>
<tr><td>6:30&ndash;7:30am</td><td>Outbound block (50 cold emails / 5 LinkedIn DMs)</td><td>Cold + BT</td></tr>
<tr><td>7:30&ndash;9am</td><td>Personal: workout, breakfast</td><td>&mdash;</td></tr>
<tr><td>9am&ndash;5pm</td><td>Day job</td><td>&mdash;</td></tr>
<tr><td>Day job &ldquo;lull&rdquo; (30&ndash;90 min)</td><td>Reply triage, content review, partnership messages</td><td>All</td></tr>
<tr><td>5&ndash;6pm</td><td>Personal / dinner</td><td>&mdash;</td></tr>
<tr><td>6&ndash;8pm</td><td>2&ndash;3 client/partner calls</td><td>Sales</td></tr>
<tr><td>8&ndash;9pm</td><td>Booking work (proposals, confirmations)</td><td>Ops</td></tr>
<tr><td>9&ndash;10pm</td><td>Personal / wind down</td><td>&mdash;</td></tr>
<tr><td>Saturday 9am&ndash;1pm</td><td>3&ndash;4 intake calls + content batch (TikTok shoot)</td><td>Sales + content</td></tr>
<tr><td>Sunday</td><td>OFF (truly)</td><td>&mdash;</td></tr>
</tbody>
</table>
<p>~15 hours/wk on business steady-state alongside day job. Sustainable. Compresses to 25 hrs/wk during seasonal pushes.</p>

<div class="divider">&middot; &middot; &middot;</div>
<p style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 13pt; font-style: italic; color: #4a4a47;">End of Playbook v1</p>
<p style="text-align: center; font-size: 9pt; color: #8B6F47;">This playbook is the tactical companion to Preface Business Plan v2. The plan tells you what. This tells you how.</p>
</section>
"""


def main():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Preface — The Playbook</title>
<style>{v1.CSS_TEXT}{EXTRA_CSS}</style>
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
