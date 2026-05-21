"""Generate the Preface Segment Workflows PDF — operational playbook per target market."""
from pathlib import Path
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import build_plan_pdf as v1
import build_playbook_pdf as pb

OUT = Path(__file__).parent / "Preface-Segment-Workflows.pdf"

EXTRA_CSS = pb.EXTRA_CSS + """
.segment-cover {
    background: #0A0A0A; color: #FAFAF8;
    padding: 40px 32px; margin: 0.2in -0.7in 0.2in -0.7in;
    page-break-after: avoid;
}
.segment-cover .num {
    font-family: 'JetBrains Mono', monospace; font-size: 10pt;
    letter-spacing: 0.2em; color: #A85C3D; font-weight: 600;
    margin-bottom: 12px;
}
.segment-cover h1 {
    font-family: 'Cormorant Garamond', serif; font-size: 38pt;
    font-weight: 400; letter-spacing: -0.02em;
    line-height: 1.05; margin-bottom: 14px; color: #FAFAF8;
}
.segment-cover h1 em { color: #A85C3D; font-style: italic; }
.segment-cover .meta {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 24px; margin-top: 28px;
    padding-top: 24px; border-top: 1px solid #2A2A2A;
}
.segment-cover .meta-item .label {
    font-family: 'JetBrains Mono', monospace; font-size: 8pt;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: #6B6B6B; margin-bottom: 6px; font-weight: 600;
}
.segment-cover .meta-item .value {
    font-family: 'Cormorant Garamond', serif;
    font-size: 14pt; color: #FAFAF8;
}
.flow-stage {
    border: 1px solid #d4d2cc; margin: 0.12in 0;
    page-break-inside: avoid;
}
.flow-stage .head {
    background: #f5f3ec;
    padding: 12px 20px;
    display: flex; justify-content: space-between; align-items: baseline;
    border-bottom: 1px solid #d4d2cc;
}
.flow-stage .head .step {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    letter-spacing: 0.15em; color: #A85C3D; font-weight: 600;
}
.flow-stage .head .title {
    font-family: 'Cormorant Garamond', serif; font-size: 15pt;
    font-weight: 500;
}
.flow-stage .head .timing {
    font-family: 'JetBrains Mono', monospace; font-size: 8.5pt;
    color: #6B6B6B; letter-spacing: 0.1em;
}
.flow-stage .body { padding: 14px 20px; background: #fafaf8; }
.flow-stage .body p { font-size: 10pt; line-height: 1.55; margin-bottom: 8px; }
.flow-stage .body ul { font-size: 10pt; line-height: 1.55; margin-left: 0.2in; }
.discovery-block {
    background: #f5f3ec; border-left: 4px solid #A85C3D;
    padding: 16px 22px; margin: 0.12in 0;
}
.discovery-block .lab {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: #A85C3D; margin-bottom: 10px; font-weight: 600;
}
.discovery-block ol { font-size: 10pt; line-height: 1.6; }
.discovery-block ol li { margin-bottom: 8px; }
.discovery-block ol li em { color: #6B6B6B; font-style: italic; }
"""


def html_body():
    return r"""
<!-- COVER -->
<div class="cover">
    <div class="cover-mark">Preface</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">Segment<br/>Workflows<br/><span style="font-style: italic; font-weight: 300;">v1</span></h1>
    <div class="cover-subtitle">Six target markets. Six different workflows. End-to-end operational playbooks for the highest-value segments.</div>
    <div class="cover-meta">
        <div><span class="label">Companion to</span><span class="value">Plan v2 + Playbook</span></div>
        <div><span class="label">Use for</span><span class="value">Per-segment SOPs</span></div>
        <div><span class="label">Format</span><span class="value">Stage-by-stage workflows</span></div>
    </div>
</div>

<!-- TOC -->
<div class="toc">
    <h1><span class="num">Contents</span>Table of Contents</h1>
    <div class="toc-entry"><span class="num">00</span><span class="title">The Six Segments at a Glance</span></div>
    <div class="toc-entry"><span class="num">01</span><span class="title">Honeymoon Workflow</span></div>
    <div class="toc-entry"><span class="num">02</span><span class="title">Family Vacation Workflow</span></div>
    <div class="toc-entry"><span class="num">03</span><span class="title">Bach Weekend Workflow</span></div>
    <div class="toc-entry"><span class="num">04</span><span class="title">Milestone Group Workflow</span></div>
    <div class="toc-entry"><span class="num">05</span><span class="title">Business Travel Workflow (Deep Dive)</span></div>
    <div class="toc-entry"><span class="num">06</span><span class="title">All-Inclusive Specialty Workflow</span></div>
    <div class="toc-entry"><span class="num">07</span><span class="title">Cross-Segment Operations</span></div>
</div>

<!-- 00 OVERVIEW -->
<section>
<h1><span class="num">Section 00</span>The Six Segments at a Glance</h1>
<p class="lead">Six distinct buying patterns. Each requires different discovery, sales cadence, and operational flow. The brand is one. The workflows are not.</p>

<h2>The Segment Matrix</h2>
<table>
<thead><tr><th>Segment</th><th>Avg Booking</th><th>Sales Cycle</th><th>Y1 Mix</th><th>Primary Channel</th><th>Net / Booking</th></tr></thead>
<tbody>
<tr><td><strong>Honeymoon</strong></td><td>$12K&ndash;$22K</td><td>2&ndash;6 weeks</td><td>25%</td><td>Network referral + content</td><td>$1,200&ndash;2,400</td></tr>
<tr><td><strong>Family Vacation</strong></td><td>$5K&ndash;$15K</td><td>3&ndash;5 weeks</td><td>22%</td><td>Network referral + partnerships</td><td>$500&ndash;1,500</td></tr>
<tr><td><strong>Bach Weekend</strong></td><td>$1.5K&ndash;3K / pp · 8&ndash;15 pax</td><td>2&ndash;4 weeks</td><td>14%</td><td>Network + IG</td><td>$1,500&ndash;3,000 / group</td></tr>
<tr><td><strong>Milestone Group</strong></td><td>$25K&ndash;80K total</td><td>3&ndash;6 months</td><td>10%</td><td>Network referral + family lifecycle</td><td>$4,000&ndash;8,000</td></tr>
<tr><td><strong>Business Travel</strong></td><td>$2K&ndash;3K / trip · 20&ndash;50 trips/yr/account</td><td>2&ndash;4 weeks per account</td><td>15% (Y2 ramp to 25%)</td><td>LinkedIn outbound</td><td>$60&ndash;120 / trip</td></tr>
<tr><td><strong>All-Inclusive (specialty)</strong></td><td>$4K&ndash;$15K</td><td>1&ndash;3 weeks</td><td>14% (cross-cuts other segments)</td><td>SEO + content + referrals</td><td>$500&ndash;1,800</td></tr>
</tbody>
</table>

<h2>The Operational Difference</h2>
<table>
<thead><tr><th>Dimension</th><th>Highest-touch</th><th>Lowest-touch</th></tr></thead>
<tbody>
<tr><td>Pre-call work</td><td>Milestone Group (research / family logistics)</td><td>Business Travel (just a Slack)</td></tr>
<tr><td>Calls per booking</td><td>Milestone Group (3&ndash;5)</td><td>Business Travel (1 onboarding then async)</td></tr>
<tr><td>Hours per booking</td><td>Milestone Group (12&ndash;25 hrs)</td><td>Business Travel (10&ndash;30 min/trip)</td></tr>
<tr><td>Repeat probability</td><td>Business Travel (90%+)</td><td>Bach Weekend (one-time event)</td></tr>
<tr><td>Referral probability</td><td>Bach Weekend (8&ndash;15 friends = 8&ndash;15 leads)</td><td>Business Travel (B2B, slower)</td></tr>
<tr><td>Margin / hour</td><td>Honeymoon (high $)</td><td>Bach Weekend (high if you batch)</td></tr>
</tbody>
</table>

<h2>Capacity Math (Solo, M6&ndash;12)</h2>
<table>
<thead><tr><th>Segment</th><th>Hours / booking</th><th>Max / month (solo)</th></tr></thead>
<tbody>
<tr><td>Honeymoon</td><td>8&ndash;12</td><td>~6&ndash;8</td></tr>
<tr><td>Family Vacation</td><td>5&ndash;8</td><td>~10</td></tr>
<tr><td>Bach Weekend</td><td>6&ndash;10</td><td>~5</td></tr>
<tr><td>Milestone Group</td><td>12&ndash;25</td><td>~2&ndash;3</td></tr>
<tr><td>Business Travel</td><td>~20&ndash;30 min / trip × 30 trips = 10&ndash;15 hrs / account</td><td>~5&ndash;8 accounts</td></tr>
</tbody>
</table>
<p class="small">Total monthly capacity at full mix: ~25&ndash;30 leisure bookings + 5&ndash;8 active BT accounts. Beyond that → first sub-advisor.</p>
</section>

<!-- 01 HONEYMOON -->
<section>
<div class="segment-cover">
    <div class="num">— SEGMENT 01</div>
    <h1>Honeymoon <em>Workflow</em></h1>
    <div class="meta">
        <div class="meta-item"><div class="label">Avg Booking</div><div class="value">$12&ndash;22K</div></div>
        <div class="meta-item"><div class="label">Net / Booking</div><div class="value">$1,200&ndash;2,400</div></div>
        <div class="meta-item"><div class="label">Sales Cycle</div><div class="value">2&ndash;6 weeks</div></div>
        <div class="meta-item"><div class="label">Planning Fee</div><div class="value">$500&ndash;1,000</div></div>
    </div>
</div>

<h2>ICP — Who's the Buyer</h2>
<p>Couples 27&ndash;34, recently engaged (typically 9&ndash;14 months before wedding). One partner does the research; the other has opinions about budget. They've already googled. They've already saved IG posts. They're shortlisting, not just exploring. Affluent enough to spend $10&ndash;25K on a single trip without flinching but still price-aware. Almost always a major life event (the trip after the wedding) so emotional stakes are high.</p>

<h2>Discovery Questions (Use the Exact Order)</h2>
<div class="discovery-block">
<div class="lab">15-min honeymoon discovery</div>
<ol>
<li><strong>When's the wedding, and when are you thinking the trip will be?</strong> <em>Looking for: wedding date + how soon after (immediately / 6 mo / 1 year).</em></li>
<li><strong>Have you started a shortlist?</strong> <em>Looking for: their assumed answer, then we can challenge it.</em></li>
<li><strong>What kind of trip do you imagine &mdash; one place and don't move, or multi-stop?</strong> <em>Reveals whether they're a beach-and-don't-move couple or an adventure-then-recover couple.</em></li>
<li><strong>What does "this trip would be perfect" look like in your head?</strong> <em>Open-ended. Lets them describe in their own words. Listen for vibes vs. specific properties.</em></li>
<li><strong>Budget &mdash; what total cost would feel right, including flights?</strong> <em>Per-couple total. Not "per person." If they hesitate, give a range: "Most of my couples spend $12&ndash;25K total."</em></li>
<li><strong>Anything you're not willing to do?</strong> <em>Long flights, mosquitos, cold water, super-active, super-quiet. Eliminates 30% of the world fast.</em></li>
<li><strong>Have either of you been to [destination they mentioned]?</strong> <em>If yes, ask what they liked / didn't. If no, you have your hook.</em></li>
<li><strong>How are you splitting the planning &mdash; mostly one of you, or together?</strong> <em>Pinpoints decision-maker. The "researcher" partner is your primary contact.</em></li>
</ol>
</div>

<h2>The Workflow — Stage by Stage</h2>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 01</div><div class="title">Lead In</div></div><div class="timing">Day 0</div></div>
<div class="body">
<p><strong>Source:</strong> Network referral (highest) / IG DM / partnership intro / cold reply.</p>
<p><strong>Action:</strong> Auto-reply within 1 hour: "Congrats &mdash; happy to walk through ideas. Want to book a 20-min call? My Calendly: [link]."</p>
<p><strong>Key signal:</strong> "Engagement," "honeymoon," "September wedding" in the original message = qualified.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 02</div><div class="title">Pre-Call Prep</div></div><div class="timing">15 min before call</div></div>
<div class="body">
<p>Review intake form (if used). Glance their IG to gauge aesthetic. Have 3 destination ideas ready in different price bands ($10K / $16K / $22K). Open Fora portal in another tab.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 03</div><div class="title">Discovery Call</div></div><div class="timing">20&ndash;30 min</div></div>
<div class="body">
<p>Run the 8 discovery questions above. Resist the urge to recommend until min 14&ndash;15. Listen for: who's the decision-maker, what's the actual budget (not the stated one), what's the unspoken expectation (Instagram-worthy vs. private vs. activity-packed).</p>
<p><strong>End with:</strong> "I'll put together 2&ndash;3 options that match what you described. Planning fee is $500&mdash;refundable through the first revision if it's not right. Want me to send the link?"</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 04</div><div class="title">Planning Fee Collected</div></div><div class="timing">Same day to 3 days post-call</div></div>
<div class="body">
<p>Stripe link sent. Auto-confirmation email + Slack notif when paid. 48-hour proposal SLA starts. If they don't pay within 5 business days, send one follow-up: "Heads up &mdash; holding your spot in the queue until Friday."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 05</div><div class="title">Proposal Build</div></div><div class="timing">24&ndash;48 hours</div></div>
<div class="body">
<p>2&ndash;3 destination options. For each: 1 hotel (or 2 if multi-stop), flight routing, dates, total cost, what's included via Fora's preferred-partner programs (specific amenities by property), why this beats their original shortlist if applicable.</p>
<p><strong>Format:</strong> 3-page Notion doc OR Canva PDF (whichever the client prefers). Always include: a clear "I'd pick option B because X" recommendation at the bottom. Never present all options as equal.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 06</div><div class="title">Proposal Review Call</div></div><div class="timing">3&ndash;7 days after proposal sent</div></div>
<div class="body">
<p>30-min call. Walk through the proposal. Answer questions. Make 1&ndash;2 substitutions if needed. Lock the destination + property.</p>
<p>If they need more time: "Take a couple days. I'll hold the dates till Friday." Don't let it go past 10 days without re-engaging &mdash; rates and availability shift.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 07</div><div class="title">Booking</div></div><div class="timing">Within 48h of confirmation</div></div>
<div class="body">
<p>Book hotel through Fora portal (verify preferred-partner amenity package). Book flights through Fora Flights Desk if Pro tier, or guide them to book direct on a deal you've vetted. Collect deposit if applicable (most all-inclusives are full prepaid; many luxury hotels are 50% at booking).</p>
<p>Send confirmation email with: booking ref numbers, hotel direct phone, flight info, amenity package summary, what's prepaid vs. balance, what to do at check-in.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 08</div><div class="title">Pre-Trip — T-30 Days</div></div><div class="timing">30 days out</div></div>
<div class="body">
<p>Pre-trip packet email (VA-produced): destination weather, what to pack, restaurant reservations recommended (book if needed), excursions to consider, tipping norms, currency, transit from airport.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 09</div><div class="title">Pre-Trip — T-7 Days</div></div><div class="timing">1 week out</div></div>
<div class="body">
<p>Personal message from you: "Hey &mdash; you're 7 days out from [destination]. Anything come up I should help with? Last call for restaurant reservations / spa bookings."</p>
<p>Re-confirm flight times. Send WhatsApp number with: "Save my number. Use it 24/7 if anything goes sideways."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 10</div><div class="title">In-Trip</div></div><div class="timing">Days 1, 4, 7</div></div>
<div class="body">
<p><strong>Day 1:</strong> "Land safe? Room good?" Quick WhatsApp.</p>
<p><strong>Day 4:</strong> "How's it going? Anything you wish you'd booked I can still try to grab?"</p>
<p><strong>Day 7 / Last day:</strong> "Travel home safe. Welcome-back message coming tomorrow."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 11</div><div class="title">Post-Trip — T+1 Day</div></div><div class="timing">Day after return</div></div>
<div class="body">
<p>Welcome-back message + photo request: "Welcome back! Anything you want to send my way photo-wise (with permission to repost) would be awesome. And if you have 60 seconds, a Google review means the world." Include the review link.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 12</div><div class="title">Referral Ask + 1-Year Loop</div></div><div class="timing">T+3 days, T+90 days, annually</div></div>
<div class="body">
<p><strong>T+3 days:</strong> "If you loved the trip, the highest compliment is sending one friend my way." Specific. Not a generic "let me know if you know anyone."</p>
<p><strong>T+90 days:</strong> "Quick one &mdash; how's married life? Any travel coming up?" (Babymoon teaser.)</p>
<p><strong>T+1 year (anniversary):</strong> Personal anniversary message. Often triggers an anniversary-trip booking. Cycle continues.</p>
</div>
</div>

<h2>Honeymoon-Specific Objections</h2>
<table>
<thead><tr><th>Objection</th><th>Verbatim response</th></tr></thead>
<tbody>
<tr><td>"We were thinking of doing this through our wedding planner"</td><td>"Great planner. Wedding planner does venue/decor/ceremony. I do hotels/flights/multi-stop logistics. We work great together &mdash; want me to coordinate directly with them?"</td></tr>
<tr><td>"Can we use our IHG / Marriott points?"</td><td>"You can &mdash; just not for both elements. Decision: use points on hotel (you lose the FSPP/Privé amenity package and the bookable upgrade) OR pay cash for the hotel through me (you keep the points for status earning + get the amenity package). For honeymoons, paying cash usually wins &mdash; the cash value of the upgrade + breakfast + credits typically exceeds the value of the points redemption."</td></tr>
<tr><td>"It's so far out, why book now?"</td><td>"Two reasons. One: the better resorts sell out at peak honeymoon dates (Sept/Oct, March break, holiday weeks). Two: deposit-and-cancel policies on most properties are 60&ndash;90 days flexible. You're not really locked in; you're just reserving."</td></tr>
</tbody>
</table>

<h2>Honeymoon KPIs</h2>
<table>
<thead><tr><th>Metric</th><th>Target</th></tr></thead>
<tbody>
<tr><td>Discovery call → planning fee</td><td>60%</td></tr>
<tr><td>Planning fee → booking</td><td>85%</td></tr>
<tr><td>Avg booking size</td><td>$14K</td></tr>
<tr><td>Days from discovery → booking</td><td>14&ndash;21</td></tr>
<tr><td>Post-trip referral rate</td><td>20% (1 in 5 sends a friend)</td></tr>
<tr><td>1-year repeat (anniversary trip)</td><td>15%</td></tr>
</tbody>
</table>
</section>

<!-- 02 FAMILY -->
<section>
<div class="segment-cover">
    <div class="num">— SEGMENT 02</div>
    <h1>Family Vacation <em>Workflow</em></h1>
    <div class="meta">
        <div class="meta-item"><div class="label">Avg Booking</div><div class="value">$5&ndash;15K</div></div>
        <div class="meta-item"><div class="label">Net / Booking</div><div class="value">$500&ndash;1,500</div></div>
        <div class="meta-item"><div class="label">Sales Cycle</div><div class="value">3&ndash;5 weeks</div></div>
        <div class="meta-item"><div class="label">Planning Fee</div><div class="value">$200&ndash;500</div></div>
    </div>
</div>

<h2>ICP</h2>
<p>Parents 32&ndash;45 with 1&ndash;3 kids (ages 0&ndash;14). Affluent suburban (Thornhill, Forest Hill, Bayview). Annual trip pattern (March break, summer, December). All-inclusive weighted, with 30% European city/multi-stop in the mix. Decision-maker is typically one parent (often, but not always, the mom). High repeat probability &mdash; once they trust you, they book every year for 5+ years.</p>

<h2>Discovery Questions</h2>
<div class="discovery-block">
<div class="lab">20-min family discovery</div>
<ol>
<li><strong>When are you traveling, and how flexible are the dates?</strong> <em>School calendar is the constraint. Identify if locked.</em></li>
<li><strong>Ages of kids?</strong> <em>Critical for property selection. Under 4 = certain pools, 4&ndash;10 = kids' club, 11+ = teen amenities.</em></li>
<li><strong>What kind of trip works for your family &mdash; relaxed beach, adventure, multi-city, theme park?</strong></li>
<li><strong>Budget total or per-person?</strong> <em>Most parents think in total. Get them to confirm including flights.</em></li>
<li><strong>Have you stayed at resorts before? Which ones? What worked, what didn't?</strong> <em>Calibration question. "We did Sandals" tells you a lot.</em></li>
<li><strong>Adults-only sections matter to you?</strong> <em>Almost always yes if kids are 7+. Almost always no if kids are 2&ndash;4.</em></li>
<li><strong>Flight tolerance?</strong> <em>5 hrs / 8 hrs / 12 hrs. With small kids, this is real.</em></li>
<li><strong>Any dietary / accessibility / medical things to plan around?</strong> <em>Critical. Often surfaces only when asked.</em></li>
</ol>
</div>

<h2>The Workflow</h2>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 01</div><div class="title">Lead In + Pre-Call Filter</div></div><div class="timing">Day 0&ndash;2</div></div>
<div class="body">
<p>Most family-vacation leads start with low specificity ("we're thinking somewhere warm in March"). Reply with a friendly nudge to book a call + a quick question to filter: "What ages are the kids? And were you thinking all-inclusive / hotel / cruise?"</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 02</div><div class="title">Discovery Call</div></div><div class="timing">20&ndash;30 min</div></div>
<div class="body">
<p>Run the 8 questions. Pay special attention to: prior resort experience (their reference points), school dates (constraints), and dietary/accessibility needs (often surface late).</p>
<p>Recommend 1&ndash;2 on the spot if confident. Family travel is more about narrowing fast than exploring widely &mdash; parents want decisions, not options.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 03</div><div class="title">Planning Fee</div></div><div class="timing">Same day</div></div>
<div class="body">
<p>Lower than honeymoon: $200 standard, $500 if multi-stop or 2-week itinerary. Family clients tend to book annually &mdash; the long-term LTV justifies a lower entry fee.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 04</div><div class="title">Proposal</div></div><div class="timing">48 hours</div></div>
<div class="body">
<p>Format matters: families want a 1-page summary they can email to the other parent. Don't send a 3-page Notion doc. Send a clean PDF: 1 destination recommendation + 2 backup options, each with: property name + room type + dates + flights + total cost + amenity package.</p>
<p>Always include kids' programming details if available (kids' club hours, age requirements, supervised activities).</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 05</div><div class="title">Decision Call (Optional)</div></div><div class="timing">5&ndash;10 days</div></div>
<div class="body">
<p>Families often want to make the decision asynchronously (both parents need to review). Don't push for a second call unless they ask. Follow up via email or text after 5 business days with a yes/no nudge.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 06</div><div class="title">Booking</div></div><div class="timing">24h post-confirmation</div></div>
<div class="body">
<p>Often involves multiple rooms (adults + kids in adjoining or connecting). Verify room configuration matches family size. For all-inclusives, confirm meal plan tier (Standard / Club / etc).</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 07</div><div class="title">Pre-Trip — Family-Specific</div></div><div class="timing">T-30, T-14, T-7</div></div>
<div class="body">
<p><strong>T-30:</strong> Family-specific pre-trip packet (more detailed than honeymoon): kids' club schedule, what to pack for kids, restaurant booking strategy (many resorts require advance reservation), pool depths if relevant, beach safety, child passports + ETA reminder.</p>
<p><strong>T-14:</strong> Re-confirm flight times. Check on any health/medical needs.</p>
<p><strong>T-7:</strong> Final pre-trip note + WhatsApp number.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 08</div><div class="title">In-Trip</div></div><div class="timing">Day 1, Day 4</div></div>
<div class="body">
<p><strong>Day 1:</strong> "Hope the flights with the kids were okay. Settled in?"</p>
<p><strong>Day 4:</strong> Light check-in.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 09</div><div class="title">Post-Trip + Annual Loop</div></div><div class="timing">T+1, then annual</div></div>
<div class="body">
<p>Welcome back + review ask. Schedule the next-year touch: <strong>October (winter break planning) and January (March break planning).</strong> This is the highest-retention segment if you nail the annual rhythm.</p>
</div>
</div>

<h2>Family Travel KPIs</h2>
<table>
<thead><tr><th>Metric</th><th>Target</th></tr></thead>
<tbody>
<tr><td>Discovery → planning fee</td><td>50%</td></tr>
<tr><td>Planning fee → booking</td><td>80%</td></tr>
<tr><td>Avg booking size</td><td>$8K</td></tr>
<tr><td>Year-over-year repeat rate</td><td>60%+</td></tr>
<tr><td>Referrals (parent network is dense)</td><td>30% within 18 months</td></tr>
</tbody>
</table>
</section>

<!-- 03 BACH -->
<section>
<div class="segment-cover">
    <div class="num">— SEGMENT 03</div>
    <h1>Bach Weekend <em>Workflow</em></h1>
    <div class="meta">
        <div class="meta-item"><div class="label">Avg Group Spend</div><div class="value">$1.5&ndash;3K / pp · $15&ndash;30K total</div></div>
        <div class="meta-item"><div class="label">Group Size</div><div class="value">8&ndash;15 people</div></div>
        <div class="meta-item"><div class="label">Sales Cycle</div><div class="value">2&ndash;4 weeks</div></div>
        <div class="meta-item"><div class="label">Planning Fee</div><div class="value">$500&ndash;1,500</div></div>
    </div>
</div>

<h2>ICP</h2>
<p>Maid of Honor / Bride organizing for 8&ndash;15 women, ages 26&ndash;34. Wedding is 4&ndash;8 months out. They've already settled on a destination concept (Mykonos / Tulum / Lisbon / Nashville / Miami / Mexico City) but haven't done logistics. Decision-maker is the MOH (or sometimes the bride directly). High group-text energy: 8&ndash;15 women in a WhatsApp means coordination overhead is real.</p>

<h2>Discovery Questions</h2>
<div class="discovery-block">
<div class="lab">25-min bach discovery</div>
<ol>
<li><strong>How many people, and what's the role of the person I'm talking to (MOH, bride, etc.)?</strong></li>
<li><strong>What dates, and how locked are they?</strong> <em>4-day weekends are most common (Thu&ndash;Sun or Fri&ndash;Mon).</em></li>
<li><strong>Destination ideas?</strong> <em>If they say "we're thinking Mykonos or Tulum," respect it. Don't pivot unless there's a structural problem.</em></li>
<li><strong>Per-person budget &mdash; what's everyone comfortable spending?</strong> <em>Critical. There's always a budget-conscious member.</em></li>
<li><strong>What kind of vibe &mdash; private villa / boutique hotel / all-inclusive / Airbnb-with-amenities?</strong></li>
<li><strong>How many of the group know each other well?</strong> <em>Reveals risk of sub-group drama.</em></li>
<li><strong>Are there any specific activities the bride wants (boat day, club bottle service, spa, photography)?</strong></li>
<li><strong>What's the realistic decision timeline?</strong> <em>How fast can they commit, given they need group consensus.</em></li>
</ol>
</div>

<h2>The Workflow</h2>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 01</div><div class="title">Lead In</div></div><div class="timing">Day 0</div></div>
<div class="body">
<p>Source: typically IG referral or friend-of-friend. Often: "Hey, my friend just got engaged and we're trying to figure out her bach &mdash; can we chat?"</p>
<p>Auto-reply within 1 hour. The MOH is typically in flight planning mode and responsive.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 02</div><div class="title">Group Briefing Call</div></div><div class="timing">25&ndash;30 min</div></div>
<div class="body">
<p>Almost always with the MOH alone (rarely with the bride or the full group). Run the discovery questions. Bach groups always have an in-group budget tension &mdash; surface it directly: "What's the highest someone in the group can spend per person, and what's the lowest? Plan for the lowest."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 03</div><div class="title">Planning Fee</div></div><div class="timing">Same day</div></div>
<div class="body">
<p>Higher fee than family ($500 base; $1,000 if international with complex air; $1,500 for villa + multiple restaurants + boat day). Justify it: bach groups are 8&ndash;15 individual bookings, often with separate flights from different cities. You're doing 3&ndash;5x the work of a couple's trip.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 04</div><div class="title">Proposal</div></div><div class="timing">3&ndash;5 days</div></div>
<div class="body">
<p>1 strong recommendation (don't give 3 options &mdash; group can't decide between options). Include: property + per-pp cost + group activities + day-by-day rough plan + flight cost ranges from common cities.</p>
<p>Send as a shareable Notion page or PDF that the MOH can drop in the group WhatsApp.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 05</div><div class="title">Group Consensus Phase</div></div><div class="timing">5&ndash;14 days</div></div>
<div class="body">
<p>This is the longest stage. Group WhatsApp goes wild. Be patient. Don't push. Check in once at day 5: "Group feeling good about it?"</p>
<p>If the group has objections, gather them all at once via MOH, then issue ONE revised proposal addressing all. Avoid death-by-revision.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 06</div><div class="title">Booking — The Hard Part</div></div><div class="timing">7&ndash;14 days</div></div>
<div class="body">
<p>Two booking models:</p>
<ul>
<li><strong>Group room block:</strong> Hotel/villa holds rooms; you collect deposits from individuals; one master folio. Better economics but more logistics.</li>
<li><strong>Individual bookings under a shared resort:</strong> Each person books under their own card; you book all of them through Fora. Cleaner but more transaction volume.</li>
</ul>
<p>For 10+ pax villa: use the group block. For all-inclusive resort: individual bookings.</p>
<p>Set deadlines: "Everyone needs to confirm their dates and payment method by [Friday]. Names not in by then go to waitlist."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 07</div><div class="title">Pre-Trip Coordination</div></div><div class="timing">T-30, T-7</div></div>
<div class="body">
<p><strong>T-30:</strong> Group itinerary PDF: hotel info, restaurant reservations (book them yourself), boat day details, spa day if booked, transport from airport.</p>
<p><strong>T-7:</strong> WhatsApp message to MOH: "Last call for any restaurant or activity additions. Otherwise &mdash; have an incredible weekend."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 08</div><div class="title">In-Trip + Post</div></div><div class="timing">Mid-trip + T+1</div></div>
<div class="body">
<p>Light-touch check-in mid-trip. Post-trip: <strong>this is where bach trips pay back massively in referrals.</strong> 8&ndash;15 women now think of you as "the travel agent who planned my friend's bach." Send each one a follow-up: "If you have a trip coming up, would love to help."</p>
</div>
</div>

<h2>The Bach Multiplier</h2>
<div class="hormozi-rule">
<div class="label">The compounding move</div>
<div class="rule">Every bach trip = 8&ndash;15 new people in your network who just experienced your work firsthand. <strong>Of those 8&ndash;15, statistically 2&ndash;4 are engaged or planning a wedding within 2 years.</strong> The bach itself nets ~$2K&ndash;3K; the downstream honeymoon and wedding-guest-travel bookings net $5K&ndash;15K. This is the highest-LTV-per-acquisition segment in the practice.</div>
</div>
</section>

<!-- 04 MILESTONE GROUP -->
<section>
<div class="segment-cover">
    <div class="num">— SEGMENT 04</div>
    <h1>Milestone Group <em>Workflow</em></h1>
    <div class="meta">
        <div class="meta-item"><div class="label">Total Spend</div><div class="value">$25&ndash;80K</div></div>
        <div class="meta-item"><div class="label">Group Size</div><div class="value">12&ndash;30 people</div></div>
        <div class="meta-item"><div class="label">Sales Cycle</div><div class="value">3&ndash;6 months</div></div>
        <div class="meta-item"><div class="label">Planning Fee</div><div class="value">$2,500&ndash;5,000</div></div>
    </div>
</div>

<h2>ICP</h2>
<p>Multi-generational family or extended-friends group. Occasion: 40th / 50th / 60th birthday, parents' anniversary, family reunion, bar/bat mitzvah trip abroad, post-wedding extended celebration. Decision-maker is typically one organizer (often the host or one of the adult children). Budget is sizable but allocated across many travelers, so per-person economics still matter.</p>

<h2>Discovery Questions</h2>
<div class="discovery-block">
<div class="lab">45-min milestone discovery (longer than other segments)</div>
<ol>
<li><strong>What's the occasion, and whose celebration is it?</strong> <em>Whose preferences drive decisions?</em></li>
<li><strong>How many people, ranging in age from what to what?</strong> <em>Multi-gen logistics get specific.</em></li>
<li><strong>Date range &mdash; how locked?</strong></li>
<li><strong>Destination ideas &mdash; or are you open?</strong> <em>Milestone groups often have a "vibe" (Israel pilgrimage, Italian villa, Caribbean reunion) before destination.</em></li>
<li><strong>What's the budget &mdash; who's paying and how does it split?</strong> <em>Critical. Host pays all? Each family pays own? Mix?</em></li>
<li><strong>Mobility / dietary / health considerations across the group?</strong></li>
<li><strong>Activity vs. relaxation balance?</strong> <em>Older generations often prefer fewer activities; younger generations want more.</em></li>
<li><strong>Single-property or multi-stop?</strong></li>
<li><strong>Are people flying from different cities?</strong></li>
<li><strong>Is there a specific "moment" the trip is built around (dinner, ceremony, event)?</strong></li>
</ol>
</div>

<h2>The Workflow</h2>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 01</div><div class="title">Initial Brief</div></div><div class="timing">Day 0</div></div>
<div class="body">
<p>Source: typically warm network referral or partnership intro (family lawyer, financial advisor, wedding planner who's worked with the family before).</p>
<p>Schedule 60-min discovery call. These don't get done in 20 minutes.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 02</div><div class="title">Discovery Call</div></div><div class="timing">45&ndash;60 min</div></div>
<div class="body">
<p>Run the 10 questions. Take detailed notes. Identify the constraint set: dates, budget, accessibility, dietary, geographic preferences. Ask: "If I came back to you with a perfect proposal that included everything except [one constraint], which one are you willing to flex on?"</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 03</div><div class="title">Planning Fee</div></div><div class="timing">Same day or 1 day after</div></div>
<div class="body">
<p>$2,500 base. $3,500 for 20+ pax or complex multi-stop. $5,000 if it includes event coordination (private dinner, milestone ceremony, etc).</p>
<p>This isn't optional &mdash; the planning workload is enormous. Set expectations: "I'll spend 15&ndash;25 hours building this proposal. The planning fee covers that work and is refundable through the first revision if it's not what you wanted."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 04</div><div class="title">Proposal Build</div></div><div class="timing">5&ndash;10 days</div></div>
<div class="body">
<p>Significantly more detailed than honeymoon or family proposals. Include:</p>
<ul>
<li>Single recommendation (one strong option, not three)</li>
<li>Property + room allocation (who stays where) + room types</li>
<li>Day-by-day group itinerary outline</li>
<li>Per-person cost breakdown</li>
<li>Cost-by-traveler-segment (kids, adults, seniors if rates differ)</li>
<li>Flight options from each origin city</li>
<li>Group activities (private dinners, excursions, transportation)</li>
<li>Backup if specific dates / properties have issues</li>
</ul>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 05</div><div class="title">Family Decision Process</div></div><div class="timing">2&ndash;6 weeks</div></div>
<div class="body">
<p>Multi-stakeholder decision. Patient is required. Expect: a) the host approves but needs sibling buy-in, b) one family has dietary/dates concerns, c) someone wants a cheaper room option. Issue revised proposals at most 2x. Past that, structural issues exist and you need a re-discovery call.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 06</div><div class="title">Group Booking Process</div></div><div class="timing">2&ndash;4 weeks</div></div>
<div class="body">
<p>Use Fora Groups platform (built for exactly this, $80M+ volume since Oct 2025). It provides:</p>
<ul>
<li>Group portal each guest can use to confirm + pay</li>
<li>Master booking sheet visible to you</li>
<li>Payment collection across multiple travelers</li>
<li>Group amenity blocks (concierge access, welcome amenity, group dinner)</li>
</ul>
<p>Set clear deadlines and a payment schedule. Most milestone groups need: 25% deposit at confirm, 50% at 90 days out, balance at 30 days out.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 07</div><div class="title">Pre-Trip Coordination (Heavy)</div></div><div class="timing">T-60 / T-30 / T-7</div></div>
<div class="body">
<p><strong>T-60:</strong> Confirm all room types, dietary needs, group activities, transportation.</p>
<p><strong>T-30:</strong> Group itinerary PDF. Restaurant reservations confirmed. Private group activities booked. Transfers arranged.</p>
<p><strong>T-7:</strong> Final logistics email to all travelers (with permission via host). Your WhatsApp number shared with the host.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 08</div><div class="title">In-Trip Presence</div></div><div class="timing">Daily</div></div>
<div class="body">
<p>For milestone groups, daily WhatsApp check-ins with the host are normal. Things will come up: a guest has a complaint, a restaurant changed plans, weather issue. You triage from afar. This is where Fora's hotel-direct relationships matter &mdash; when you call the GM with the host's issue, doors open faster than if the host called directly.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 09</div><div class="title">Post-Trip + Family Lifecycle</div></div><div class="timing">T+1, then 6-month touch</div></div>
<div class="body">
<p>Welcome back + review ask. The big play: the milestone group has 12&ndash;30 people who now know you. <strong>Add each of them to the newsletter (with permission via the host).</strong> Within 18 months, 3&ndash;5 of those people will have their own trip-worthy event &mdash; engagement, family vacation, birthday.</p>
</div>
</div>

<h2>Milestone Group KPIs</h2>
<table>
<thead><tr><th>Metric</th><th>Target</th></tr></thead>
<tbody>
<tr><td>Discovery → planning fee</td><td>70% (high commitment from the start)</td></tr>
<tr><td>Planning fee → booking</td><td>90%+ (sunk cost is real)</td></tr>
<tr><td>Avg total spend</td><td>$45K</td></tr>
<tr><td>Avg net commission</td><td>$5,500</td></tr>
<tr><td>Hours per booking</td><td>15&ndash;25</td></tr>
<tr><td>Downstream bookings within 18 months</td><td>3&ndash;5 from same group</td></tr>
</tbody>
</table>
</section>

<!-- 05 BUSINESS TRAVEL -->
<section>
<div class="segment-cover">
    <div class="num">— SEGMENT 05</div>
    <h1>Business Travel <em>Workflow</em></h1>
    <div class="meta">
        <div class="meta-item"><div class="label">Avg Trip Spend</div><div class="value">$800&ndash;3K</div></div>
        <div class="meta-item"><div class="label">Trips / Yr / Account</div><div class="value">20&ndash;50</div></div>
        <div class="meta-item"><div class="label">Sales Cycle</div><div class="value">2&ndash;4 weeks (account)</div></div>
        <div class="meta-item"><div class="label">Pricing</div><div class="value">Free / $150&ndash;500 mo</div></div>
    </div>
</div>

<h2>The Difference</h2>
<p>This workflow is the opposite of leisure travel. Leisure is high-touch low-frequency. Business travel is low-touch high-frequency. Optimize accordingly: front-load the onboarding work, then move to async transactional booking. <em>See Playbook Section 06 for the full ICP, outreach sequence, and onboarding details. This document covers the operational workflow after onboarding.</em></p>

<h2>The Booking Workflow (Per-Trip)</h2>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 01</div><div class="title">Request In</div></div><div class="timing">T-0</div></div>
<div class="body">
<p>Client texts/Slacks: "Need NYC Sun&ndash;Wed, 4-star, near Midtown, under $400/night."</p>
<p>Your reply (within 30 min): "On it. Any hotel preference, or want me to optimize for Hyatt Privé / Marriott STARS perks?"</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 02</div><div class="title">Search + Confirm Preference</div></div><div class="timing">T+15&ndash;30 min</div></div>
<div class="body">
<p>Pull 2&ndash;3 options from Fora portal that match preferred-partner amenity programs. Send back: "Three options &mdash; Park Hyatt $385 (Privé: upgrade + $100 F&amp;B + breakfast), Edition $420 (STARS: upgrade + $100 + breakfast), Conrad $360 (Impresario: $100 + breakfast). I'd pick Park Hyatt &mdash; the rate's lower than Marriott rack and Privé gives you the biggest perks package. OK to book?"</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 03</div><div class="title">Book</div></div><div class="timing">T+30&ndash;60 min</div></div>
<div class="body">
<p>Book through Fora portal under their loyalty number. Confirm preferred-partner amenity attribution. Verify card on file is correctly charged.</p>
<p>Send confirmation: "Booked. Confirmation #XYZ. Privé upgrade should be in your folio at check-in. $100 F&amp;B credit + breakfast for 4. Have a good trip."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 04</div><div class="title">Pre-Trip Reminder</div></div><div class="timing">T-1 day automated</div></div>
<div class="body">
<p>Auto-email: "Heads up &mdash; you're checking in tomorrow at Park Hyatt NYC. Address: 153 W 57th. Suite upgrade confirmed in folio. $100 F&amp;B credit on file. Late check-out by 2pm noted. Text me if anything goes sideways."</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 05</div><div class="title">Disruption Recovery</div></div><div class="timing">As needed</div></div>
<div class="body">
<p>Flight cancelled, hotel overbooked, missed connection. Client texts. You respond within 15 min and fix. This is the WhatsApp value-prop. Common moves:</p>
<ul>
<li>Hotel overbooked at check-in → call GM, use Privé status to claim upgrade or move to same-tier sister property</li>
<li>Flight cancelled → re-book on next available, alert hotel of late check-in</li>
<li>Client added meeting requires city change → re-route everything in 30 min</li>
</ul>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 06</div><div class="title">Monthly Account Review</div></div><div class="timing">Monthly</div></div>
<div class="body">
<p>1-page summary email: trips booked, total spend, perks captured (upgrades + credits + breakfast values), points/miles earned, any disruption recoveries handled. This is the retention mechanic &mdash; clients forget the value you're providing if you don't show them.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 07</div><div class="title">Quarterly Optimization Call</div></div><div class="timing">Quarterly</div></div>
<div class="body">
<p>20-min call. Review: pace toward next status tier (Hyatt Globalist, Marriott Titanium, Hilton Diamond), opportunities for status match across brands, leisure trip cross-sell (their spouse's anniversary trip, family vacation next year).</p>
<p>This is also when you ask: "Anyone in your network who travels similarly to you?"</p>
</div>
</div>
</section>

<!-- 06 ALL-INCLUSIVE -->
<section>
<div class="segment-cover">
    <div class="num">— SEGMENT 06</div>
    <h1>All-Inclusive <em>Specialty</em> Workflow</h1>
    <div class="meta">
        <div class="meta-item"><div class="label">Avg Booking</div><div class="value">$4&ndash;15K</div></div>
        <div class="meta-item"><div class="label">Net / Booking</div><div class="value">$500&ndash;1,800</div></div>
        <div class="meta-item"><div class="label">Sales Cycle</div><div class="value">1&ndash;3 weeks (shortest)</div></div>
        <div class="meta-item"><div class="label">Planning Fee</div><div class="value">$0&ndash;300</div></div>
    </div>
</div>

<h2>The Strategic Note</h2>
<p>All-inclusive is a specialty positioning that cross-cuts the other segments. Most all-inclusive bookings happen <em>through</em> one of the leisure segments above (honeymoon at Excellence, family at Hyatt Ziva, bach at Royalton). But the all-inclusive expertise also generates a meaningful flow of <strong>standalone all-inclusive inquiries</strong> — couples or solo travelers booking a 5-7 night resort trip without the "occasion" framing. This is the workflow for those.</p>

<h2>The Dual-Host Decision Tree</h2>
<div class="callout warn">
<h4>Critical: Which Host Books the Trip?</h4>
<p>All-inclusive bookings split between two host paths:</p>
<ul>
<li><strong>Through Fora:</strong> Luxury and upmarket all-inclusives where Fora has Hyatt Privé / Virtuoso amenity packages (Excellence, Le Blanc, Zoetry, Secrets, Dreams, Atelier, Hyatt Ziva, Grand Velas, Rosewood Mayakoba). Amenity package usually beats packaged-tour pricing.</li>
<li><strong>Through TTAND / TPI (secondary host):</strong> Mass-market all-inclusives where tour-operator packaged pricing wins (Sunwing, Air Canada Vacations, WestJet Vacations, Transat). Bahia Principe, Iberostar non-Grand, Riu, Royalton non-Luxury, Barceló, mid-tier Princess.</li>
</ul>
<p>The first 5 minutes of the discovery call determine which path. Asking budget + brand preference + travel dates pinpoints which host owns the booking.</p>
</div>

<h2>Discovery Questions</h2>
<div class="discovery-block">
<div class="lab">15-min all-inclusive discovery</div>
<ol>
<li><strong>When are you traveling, and from where?</strong> <em>YYZ→PUJ peak December = packaged charter terrain. YUL→Cancun off-peak = Fora-direct terrain.</em></li>
<li><strong>How many people, and ages?</strong></li>
<li><strong>Have you stayed at all-inclusives before? Which ones?</strong> <em>Calibration. "We always do Sandals" tells you the tier.</em></li>
<li><strong>What did you like / not like about the last one?</strong> <em>Specific feedback to anchor recommendation.</em></li>
<li><strong>Adults-only or family?</strong></li>
<li><strong>Budget total or per-person, including flights?</strong> <em>$3K/pp/week packaged → tour operator. $5K+/pp/week + open to longer stays → Fora.</em></li>
<li><strong>Vibe &mdash; quiet, lively, active, sleepy?</strong></li>
<li><strong>Food important? Beach important? Pool important?</strong> <em>One of these matters more than the others, always.</em></li>
</ol>
</div>

<h2>The Workflow</h2>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 01</div><div class="title">Lead In (Often High Intent)</div></div><div class="timing">Day 0</div></div>
<div class="body">
<p>Source: SEO from the All-Inclusives page + IG referral + word-of-mouth from previous all-inclusive clients. These leads tend to be highest-intent &mdash; they specifically want resort travel.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 02</div><div class="title">Quick Discovery</div></div><div class="timing">15&ndash;20 min</div></div>
<div class="body">
<p>Shorter than other segments because the buying intent is clearer. The 8 questions above. Within 10 minutes you know: which host path, which property tier, which destinations to recommend.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 03</div><div class="title">On-the-Spot Recommendation</div></div><div class="timing">During the call</div></div>
<div class="body">
<p>Unlike honeymoon (where you build a polished proposal), all-inclusive bookings often close from the call directly. "For your $4K/pp/week January in DR &mdash; I'd put you at Excellence Punta Cana, Club tier. About $4,200/pp. Privé gives you breakfast at all restaurants, $200 spa credit, and butler service. Want me to send a 1-page summary and get this booked this week?"</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 04</div><div class="title">Planning Fee (Often Waived)</div></div><div class="timing">Same day</div></div>
<div class="body">
<p>Often no planning fee for straightforward all-inclusive bookings. The Fora commission is enough. Reserve the $200&ndash;300 planning fee for: multi-stop AI trips, group AI bookings, custom requests beyond standard packaging.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 05</div><div class="title">Booking</div></div><div class="timing">24&ndash;72 hours</div></div>
<div class="body">
<p>If Fora: standard Fora portal flow with Privé / Virtuoso amenity attribution.</p>
<p>If TTAND: standard tour operator portal flow (Sunwing dashboard, ACV portal). Note: amenity perks don't apply on packaged bookings.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 06</div><div class="title">All-Inclusive-Specific Pre-Trip</div></div><div class="timing">T-21, T-7</div></div>
<div class="body">
<p><strong>T-21:</strong> Resort-specific guide: restaurant reservation strategy (many resorts require day-of advance booking), excursion recommendations, spa appointment booking, what tipping looks like at all-inclusives.</p>
<p><strong>T-7:</strong> Final note + WhatsApp.</p>
</div>
</div>

<div class="flow-stage">
<div class="head"><div><div class="step">STAGE 07</div><div class="title">Post-Trip + Specific Review Ask</div></div><div class="timing">T+1, T+3</div></div>
<div class="body">
<p>"Welcome back. Quick favor: I'm collecting honest property reviews for the All-Inclusives page. Would you be willing to share a 2-3 sentence take I could feature (anonymized or with name attribution, your call)?" Real client reviews on the All-Inclusives page strengthen the specialty positioning enormously.</p>
</div>
</div>

<h2>All-Inclusive Specialty KPIs</h2>
<table>
<thead><tr><th>Metric</th><th>Target</th></tr></thead>
<tbody>
<tr><td>Discovery → booking</td><td>70% (highest in the practice)</td></tr>
<tr><td>Time to booking</td><td>5&ndash;10 days</td></tr>
<tr><td>Avg booking size</td><td>$7K</td></tr>
<tr><td>Avg net (Fora-routed)</td><td>$800&ndash;1,500</td></tr>
<tr><td>Avg net (TTAND-routed)</td><td>$300&ndash;500</td></tr>
<tr><td>SEO contribution to leads</td><td>30% by M9</td></tr>
</tbody>
</table>
</section>

<!-- 07 CROSS-SEGMENT -->
<section>
<h1><span class="num">Section 07</span>Cross-Segment Operations</h1>
<p class="section-intro">Things that apply across every segment workflow. Don't rebuild these for each.</p>

<h2>The Universal Intake Form (Use for All Segments)</h2>
<p>Single Tally form. Adaptive questions based on segment selected. Fields:</p>
<ul>
<li>Name + Email + Phone (required)</li>
<li>Segment: Honeymoon / Family / Bach / Milestone / Business Travel / Resort (Other)</li>
<li>Number of travelers</li>
<li>Approximate date range</li>
<li>Approximate budget (range options, not free-text)</li>
<li>Origin city / How you heard about Preface</li>
<li>One-sentence "anything I should know"</li>
</ul>
<p>Form submission → auto-routes to your Slack with segment-specific labeling.</p>

<h2>The Universal CRM Stages</h2>
<table>
<thead><tr><th>Stage</th><th>Definition</th></tr></thead>
<tbody>
<tr><td>1. New Lead</td><td>Inquiry received, not yet contacted</td></tr>
<tr><td>2. Outreached</td><td>Initial reply sent, awaiting response</td></tr>
<tr><td>3. Call Scheduled</td><td>Discovery call on calendar</td></tr>
<tr><td>4. Discovery Done</td><td>Call complete, awaiting planning fee or proposal</td></tr>
<tr><td>5. Planning Fee Paid</td><td>Active proposal build</td></tr>
<tr><td>6. Proposal Sent</td><td>Awaiting client decision</td></tr>
<tr><td>7. Booked</td><td>Trip booked + commission tracked</td></tr>
<tr><td>8. In-Trip</td><td>Client traveling</td></tr>
<tr><td>9. Completed</td><td>Returned + post-trip messaging done</td></tr>
<tr><td>10. Nurture</td><td>1-year referral / repeat loop</td></tr>
<tr><td>X. Lost</td><td>Closed without booking; reason logged</td></tr>
</tbody>
</table>

<h2>The Pre-Trip Packet Template (One Template, Three Versions)</h2>
<p>Same skeleton across segments. Vary the depth.</p>
<ol>
<li><strong>Quick context:</strong> Your trip, dates, headcount</li>
<li><strong>Booking confirmation block:</strong> Property name + confirmation number + check-in time + room types</li>
<li><strong>What to expect at check-in:</strong> Amenity package, upgrade status, special requests</li>
<li><strong>Recommendations (segment-specific):</strong>
    <ul>
    <li>Honeymoon: restaurant reservations, spa, sunset moments, photographer if relevant</li>
    <li>Family: kids' programming, restaurant strategy, beach safety</li>
    <li>Bach: dinner reservations, boat day, club access, group activities</li>
    <li>Milestone Group: group activities, restaurant blocks, transportation, special events</li>
    <li>BT: room number once available, hotel direct phone, transport from airport</li>
    </ul>
</li>
<li><strong>Practical:</strong> Weather, currency, tipping, transit, passport/visa, time zone</li>
<li><strong>Disruption protocol:</strong> Your WhatsApp number + a quick "if X then text me"</li>
</ol>

<h2>The Welcome-Back / Review Ask Template</h2>
<div class="callout">
<p style="font-family: 'Inter', sans-serif; font-size: 11pt; line-height: 1.6;">
<strong>Subject:</strong> Welcome back &mdash; quick favor?<br/><br/>

Hey [Name] &mdash;<br/><br/>

Hope the trip was as good as the photos look. Glad to have helped.<br/><br/>

Two quick things:<br/><br/>

1. <strong>If you have 60 seconds,</strong> would you be willing to leave a quick Google review? Even one line helps people deciding whether to work with me: <a href="#" style="color: #A85C3D;">[review link]</a>.<br/><br/>

2. <strong>If the trip was meaningfully better</strong> than you expected, the highest compliment is sending one friend my way. Forward this email or just drop my Calendly link: <a href="#" style="color: #A85C3D;">[link]</a>.<br/><br/>

Thanks for trusting me on this. Hit me up anytime there's a next trip on the horizon.<br/><br/>

&mdash; [Name]
</p>
</div>

<h2>The Annual Re-Engagement Loop</h2>
<table>
<thead><tr><th>Trigger</th><th>Message</th></tr></thead>
<tbody>
<tr><td>Anniversary of trip</td><td>"Quick one &mdash; happy [X-year] since [trip]. Any travel coming up?"</td></tr>
<tr><td>Honeymoon: 1 year</td><td>"Happy anniversary! Any plans to mark it? I'd love to help plan something."</td></tr>
<tr><td>Family: October &amp; January</td><td>October: "Winter break thoughts forming?" January: "March break ideas yet?"</td></tr>
<tr><td>Bach: After the wedding</td><td>"Honeymoon thoughts? If you didn't book it yet, I'd love to help."</td></tr>
<tr><td>Milestone: Annual</td><td>"Any milestone moments coming up I should help with?"</td></tr>
<tr><td>BT: Quarterly</td><td>Built into the workflow (Section 05)</td></tr>
</tbody>
</table>

<div class="divider">&middot; &middot; &middot;</div>
<p style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 13pt; font-style: italic; color: #4a4a47;">End of Segment Workflows v1</p>
</section>
"""


def main():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Preface — Segment Workflows</title>
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
