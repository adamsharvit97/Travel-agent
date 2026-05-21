"""Generate the Preface Content Strategy PDF — segmented channel playbooks."""
from pathlib import Path
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import build_plan_pdf as v1
import build_playbook_pdf as pb

OUT = Path(__file__).parent / "Preface-Content-Strategy.pdf"

EXTRA_CSS = pb.EXTRA_CSS + """
.channel-card {
    border: 1px solid #d4d2cc;
    margin: 0.15in 0;
    page-break-inside: avoid;
}
.channel-card .head {
    background: #0A0A0A; color: #FAFAF8;
    padding: 18px 24px;
    display: flex; justify-content: space-between; align-items: baseline;
}
.channel-card .head .platform {
    font-family: 'Cormorant Garamond', serif; font-size: 22pt;
    font-weight: 400; color: #FAFAF8;
}
.channel-card .head .role {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    letter-spacing: 0.15em; color: #A85C3D; font-weight: 600;
}
.channel-card .body { padding: 18px 24px; background: #fafaf8; }
.channel-card .body p { font-size: 10pt; line-height: 1.55; margin-bottom: 8px; }
.post-template {
    border-left: 3px solid #A85C3D; background: #f5f3ec;
    padding: 14px 20px; margin: 0.1in 0;
    font-size: 10pt; line-height: 1.6;
}
.post-template .lab {
    font-family: 'JetBrains Mono', monospace; font-size: 8.5pt;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: #A85C3D; margin-bottom: 8px; font-weight: 600;
}
.post-template em { color: #8B6F47; font-style: italic; }
.segment-content-block {
    background: #0A0A0A; color: #FAFAF8;
    padding: 32px; margin: 0.2in -0.7in 0.2in -0.7in;
    page-break-after: avoid;
}
.segment-content-block .num {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    letter-spacing: 0.2em; color: #A85C3D; font-weight: 600;
    margin-bottom: 12px;
}
.segment-content-block h1 {
    font-family: 'Cormorant Garamond', serif; font-size: 32pt;
    font-weight: 400; letter-spacing: -0.02em;
    line-height: 1.1; margin-bottom: 12px; color: #FAFAF8;
}
.segment-content-block h1 em { color: #A85C3D; font-style: italic; }
.segment-content-block .sub {
    font-size: 11pt; color: #B8B6B0; max-width: 5.5in;
    line-height: 1.5;
}
.platform-priority {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 12px; margin: 0.15in 0;
}
.platform-priority .pp {
    text-align: center; padding: 16px 12px;
    border: 1px solid #d4d2cc;
}
.platform-priority .pp.tier-1 { background: #A85C3D; color: #FAFAF8; border-color: #A85C3D; }
.platform-priority .pp.tier-2 { background: #f5f3ec; }
.platform-priority .pp.tier-3 { background: #fafaf8; }
.platform-priority .pp .name {
    font-family: 'Cormorant Garamond', serif; font-size: 14pt;
    font-weight: 500;
}
.platform-priority .pp .priority {
    font-family: 'JetBrains Mono', monospace; font-size: 8.5pt;
    letter-spacing: 0.18em; text-transform: uppercase;
    margin-top: 6px;
}
.platform-priority .pp.tier-1 .priority { color: #FAFAF8; }
.platform-priority .pp.tier-2 .priority,
.platform-priority .pp.tier-3 .priority { color: #6B6B6B; }
.platform-priority .pp .why { font-size: 9pt; line-height: 1.45; margin-top: 8px; }
.calendar-week {
    border: 1px solid #d4d2cc; padding: 12px 18px;
    margin: 0.08in 0; page-break-inside: avoid;
}
.calendar-week .week-num {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    letter-spacing: 0.15em; color: #A85C3D; font-weight: 600;
}
.calendar-week .theme {
    font-family: 'Cormorant Garamond', serif; font-size: 14pt;
    margin-bottom: 8px;
}
.calendar-week .grid {
    display: grid; grid-template-columns: repeat(2, 1fr);
    gap: 6px; font-size: 9.5pt;
}
.calendar-week .grid div { padding: 4px 0; }
.calendar-week .grid .lab { color: #A85C3D; font-weight: 600; }
"""


def html_body():
    return r"""
<!-- COVER -->
<div class="cover">
    <div class="cover-mark">Preface</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">Content<br/>Strategy<br/><span style="font-style: italic; font-weight: 300;">v1</span></h1>
    <div class="cover-subtitle">Segment-specific content playbooks. Channel priorities. Templates. The 52-week calendar.</div>
    <div class="cover-meta">
        <div><span class="label">Companion to</span><span class="value">Brand Guide + Playbook</span></div>
        <div><span class="label">Audience</span><span class="value">Content VA + Founder</span></div>
        <div><span class="label">Cadence</span><span class="value">Bi-weekly review</span></div>
    </div>
</div>

<!-- TOC -->
<div class="toc">
    <h1><span class="num">Contents</span>Table of Contents</h1>
    <div class="toc-entry"><span class="num">00</span><span class="title">The Strategic Framework</span></div>
    <div class="toc-entry"><span class="num">01</span><span class="title">Channel Selection — Where Content Actually Lives</span></div>
    <div class="toc-entry"><span class="num">02</span><span class="title">Segment 1: All-Inclusives (Specialty / Cross-Platform)</span></div>
    <div class="toc-entry"><span class="num">03</span><span class="title">Segment 2: Honeymoon (Visual / Aspirational)</span></div>
    <div class="toc-entry"><span class="num">04</span><span class="title">Segment 3: Bach Weekend (IG / TikTok)</span></div>
    <div class="toc-entry"><span class="num">05</span><span class="title">Segment 4: Business Travel (LinkedIn Primary)</span></div>
    <div class="toc-entry"><span class="num">06</span><span class="title">Segment 5: Family Travel (Newsletter Primary)</span></div>
    <div class="toc-entry"><span class="num">07</span><span class="title">Newsletter Deep Dive (The Owned Asset)</span></div>
    <div class="toc-entry"><span class="num">08</span><span class="title">The Repurposing System</span></div>
    <div class="toc-entry"><span class="num">09</span><span class="title">52-Week Master Calendar</span></div>
    <div class="toc-entry"><span class="num">10</span><span class="title">Analytics &amp; Optimization</span></div>
</div>

<!-- 00 FRAMEWORK -->
<section>
<h1><span class="num">Section 00</span>The Strategic Framework</h1>
<p class="lead">Content for a travel-advisor practice has one job: build trust at scale. Conversion happens 1:1. Trust happens 1:many.</p>

<h2>What Content Is For (And Isn't)</h2>
<table>
<thead><tr><th>Content IS</th><th>Content ISN'T</th></tr></thead>
<tbody>
<tr><td>Building trust before someone needs to book</td><td>A direct-response sales channel</td></tr>
<tr><td>The proof layer ("here's a real receipt")</td><td>Brand-awareness for everyone (it's for under-40 affluent specifically)</td></tr>
<tr><td>The voice rehearsal that calibrates the brand</td><td>A vanity exercise around follower counts</td></tr>
<tr><td>The asset that compounds over 24 months</td><td>The thing that pays this month's bills</td></tr>
<tr><td>The mechanism that turns a 5-min call into trust earned in advance</td><td>Substitute for the warm-network and partnership funnels</td></tr>
</tbody>
</table>

<h2>The North Star Metric (Content)</h2>
<div class="hormozi-rule">
<div class="label">Content KPI</div>
<div class="rule"><strong>"Inbound DMs / inquiries per month that mention specific content."</strong> Not impressions. Not followers. Not engagement rate. The single test: when a new lead shows up, can they reference a piece of your content? At M12, target = 30% of new leads have content attribution. At M24, target = 50%.</div>
</div>

<h2>The 50/30/20 Mix (Recap)</h2>
<table>
<thead><tr><th>%</th><th>Type</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>50%</td><td>Practical / Tactical</td><td>Authority + SEO + saves. Rankings, comparisons, decision frameworks.</td></tr>
<tr><td>30%</td><td>Opinionated / Voice</td><td>Differentiation. Hot takes. The brand persona showing up.</td></tr>
<tr><td>20%</td><td>Personal / Story</td><td>Trust + humanization. Client trips, behind-the-scenes, your own travel.</td></tr>
</tbody>
</table>

<h2>The Distribution Pyramid</h2>
<ol>
<li><strong>Newsletter (owned)</strong> — biweekly. The asset. Highest-trust audience. Newsletter is the only channel that survives algorithm changes.</li>
<li><strong>Instagram (rented, visual primary)</strong> — daily. Where the broadest demo lives.</li>
<li><strong>LinkedIn (rented, B2B primary)</strong> — 3x/week. Business travel funnel + partnership credibility.</li>
<li><strong>TikTok (rented, reach upside)</strong> — 2x/week. Cold-reach + viral potential. Plan for 90 days before judging.</li>
<li><strong>YouTube Shorts (rented, evergreen)</strong> — TikTok repurposed. Adds search-traffic upside.</li>
</ol>
</section>

<!-- 01 CHANNEL SELECTION -->
<section>
<h1><span class="num">Section 01</span>Channel Selection — Where Content Actually Lives</h1>
<p class="section-intro">Not every segment deserves the same content investment. Match the segment to where its audience actually consumes content.</p>

<h2>The Segment × Channel Matrix</h2>
<table>
<thead><tr><th>Segment</th><th>Newsletter</th><th>Instagram</th><th>LinkedIn</th><th>TikTok</th></tr></thead>
<tbody>
<tr><td><strong>All-Inclusives (specialty)</strong></td><td>High</td><td>High</td><td>Low</td><td>High</td></tr>
<tr><td><strong>Honeymoon</strong></td><td>Medium</td><td>High</td><td>Low</td><td>Medium</td></tr>
<tr><td><strong>Bach Weekend</strong></td><td>Low</td><td>High</td><td>None</td><td>High</td></tr>
<tr><td><strong>Family Travel</strong></td><td>High</td><td>Medium</td><td>Low</td><td>Low</td></tr>
<tr><td><strong>Business Travel</strong></td><td>Medium</td><td>Low</td><td>High</td><td>None</td></tr>
<tr><td><strong>Milestone Group</strong></td><td>Low (newsletter via Family)</td><td>Low</td><td>Low</td><td>None</td></tr>
</tbody>
</table>

<h2>What This Means for Production</h2>
<ul>
<li><strong>Newsletter focuses on:</strong> All-Inclusives takes + Family vacation planning + Business travel insights + Honeymoon long-reads. (Milestone Group doesn't need content; it gets referrals.)</li>
<li><strong>Instagram focuses on:</strong> All-Inclusive ranks + receipts + honeymoon visuals + bach destinations.</li>
<li><strong>LinkedIn focuses on:</strong> Business travel + partnership credibility + founder lessons.</li>
<li><strong>TikTok focuses on:</strong> All-Inclusives hot takes + bach vibes + honeymoon comparisons.</li>
</ul>

<h2>Production Capacity Allocation</h2>
<p>You're not producing content for all 6 segments at equal weight. The split:</p>
<table>
<thead><tr><th>Segment</th><th>% of weekly content output</th></tr></thead>
<tbody>
<tr><td>All-Inclusives (specialty, cross-cuts)</td><td>40%</td></tr>
<tr><td>Honeymoon</td><td>20%</td></tr>
<tr><td>Business Travel</td><td>15%</td></tr>
<tr><td>Family Travel</td><td>15%</td></tr>
<tr><td>Bach Weekend</td><td>5%</td></tr>
<tr><td>Brand / Founder / Off-Topic (Toronto, FAM trips, hot takes)</td><td>5%</td></tr>
</tbody>
</table>
<p>All-Inclusives over-indexes because: (a) it's the specialty edge, (b) the content cross-cuts honeymoon + family + bach segments, (c) SEO upside is highest there.</p>
</section>

<!-- 02 ALL-INCLUSIVES -->
<section>
<div class="segment-content-block">
    <div class="num">— CONTENT FOR SEGMENT 01</div>
    <h1>All-Inclusives <em>Content</em></h1>
    <div class="sub">The specialty. The credibility engine. The brand differentiator. 40% of content output goes here because it cross-cuts every leisure segment AND establishes the unfair advantage no algorithm can replicate.</div>
</div>

<h2>Channel Priority</h2>
<div class="platform-priority">
    <div class="pp tier-1">
        <div class="name">Instagram</div>
        <div class="priority">— Tier 1</div>
        <div class="why">Visual proof. Carousel rankings travel well. Real-resort photography is the entire brand.</div>
    </div>
    <div class="pp tier-1">
        <div class="name">TikTok</div>
        <div class="priority">— Tier 1</div>
        <div class="why">Comparison videos, hot takes, mistake-list content perform best here.</div>
    </div>
    <div class="pp tier-1">
        <div class="name">Newsletter</div>
        <div class="priority">— Tier 1</div>
        <div class="why">Long-form rankings, deep comparisons, "the verdict" pieces all live here.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">LinkedIn</div>
        <div class="priority">— Tier 3</div>
        <div class="why">Occasional, not primary. Frame as advisor-industry takes.</div>
    </div>
</div>

<h2>The Five Content Pillars (All-Inclusives Specific)</h2>
<table>
<thead><tr><th>Pillar</th><th>What it is</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Ranking</strong></td><td>Specific properties ranked by category. "5 best adults-only AIs in Mexico." "The Hyatt Inclusive Collection, ranked."</td><td>1x/wk</td></tr>
<tr><td><strong>The Comparison</strong></td><td>Head-to-head: Excellence Playa Mujeres vs Punta Cana. Le Blanc vs. Atelier. Sandals vs. Excellence.</td><td>1x/wk</td></tr>
<tr><td><strong>The Receipt</strong></td><td>Real client booking math: room category, amenity package, total added value.</td><td>2x/wk</td></tr>
<tr><td><strong>The Mistake</strong></td><td>"5 mistakes people make booking Riviera Maya." "Why you shouldn't book base room at Excellence."</td><td>1x/wk</td></tr>
<tr><td><strong>The Hot Take</strong></td><td>"Sandals is mid." "Maldives in August is a scam." "Tulum is performance art."</td><td>1x/wk</td></tr>
</tbody>
</table>

<h2>Instagram Content Templates — All-Inclusives</h2>

<div class="post-template">
<div class="lab">Carousel Template 1 — The Ranking</div>
<strong>Slide 1 (hook):</strong> "I've stayed at 20+ all-inclusives. Here are the 5 I'd actually recommend." [Photo: a hotel beach]<br/>
<strong>Slides 2-6:</strong> One property per slide. Photo + name + 2-line take. Color-coded verdict tag (Recommend / Conditional / Skip).<br/>
<strong>Slide 7:</strong> "What I left out: the 15 that aren't on this list."<br/>
<strong>Slide 8 (CTA):</strong> "Newsletter has the full list with my honest takes. preface.travel."<br/>
<em>Save rate: this format hits 8-15% save rate consistently. Saves matter more than likes.</em>
</div>

<div class="post-template">
<div class="lab">Carousel Template 2 — The Head-to-Head</div>
<strong>Slide 1:</strong> "Excellence Playa Mujeres vs. Excellence Punta Cana. I've been to both."<br/>
<strong>Slide 2:</strong> "The 4-line summary." (Best for: PM. Best for: PC. The verdict: PM. Why most people pick PC anyway:.)<br/>
<strong>Slides 3-6:</strong> Side-by-side on 4 dimensions: food / rooms / beach / vibe.<br/>
<strong>Slide 7:</strong> "I'd pick Playa Mujeres. Even if it costs $400 more."<br/>
<strong>Slide 8:</strong> CTA — "Book a 20-min call: preface.travel."
</div>

<div class="post-template">
<div class="lab">Single Post Template — The Receipt</div>
<strong>Image:</strong> Hotel folio screenshot or photo of upgraded room (anonymized).<br/>
<strong>Caption:</strong> "Last week's booking. $5,500 Excellence Playa Mujeres, 7 nights.<br/><br/>
What they booked: Junior Suite Pool View.<br/>
What they arrived to: Excellence Club Two-Story Rooftop Suite.<br/><br/>
Plus: $200 resort credit, breakfast at all restaurants, butler service.<br/><br/>
Cost over Booking.com: $0.<br/><br/>
This is the entire pitch."<br/>
<em>Hashtags: keep to 5-8. Mix specific (#excellenceplayamujeres) and category (#caribbeantravel).</em>
</div>

<h2>TikTok Templates — All-Inclusives</h2>

<div class="post-template">
<div class="lab">TikTok Template 1 — The Hot Take Open</div>
<strong>Opening 3 sec (hook):</strong> "Sandals is mid. I'll tell you why."<br/>
<strong>3-15 sec:</strong> "I've stayed at 20+ all-inclusives, including 4 Sandals properties. They're fine. They're not better than Excellence, Le Blanc, or Royalton Luxury at the same price point — and the marketing is doing a lot of work."<br/>
<strong>15-30 sec:</strong> Specific comparison. Sandals Royal Caribbean Jamaica $4,200/pp vs Excellence Playa Mujeres $4,300/pp.<br/>
<strong>30-45 sec:</strong> Specific differences (room category, food, beach).<br/>
<strong>Final 5 sec:</strong> "Newsletter has the full hierarchy."<br/>
<em>Caption: 1 line, no hashtags above 3.</em>
</div>

<div class="post-template">
<div class="lab">TikTok Template 2 — The Mistake</div>
<strong>Opening hook:</strong> "Three things you're doing wrong when booking an all-inclusive."<br/>
<strong>Mistake 1 (3-15 sec):</strong> "Booking on Booking.com. You don't save anything. You just lose the upgrades."<br/>
<strong>Mistake 2 (15-30 sec):</strong> "Booking the base room. Bait pricing. The actual product is the Club tier."<br/>
<strong>Mistake 3 (30-45 sec):</strong> "Booking Riviera Maya June through September. Sargassum will end you."<br/>
<strong>Close:</strong> "Bonus: you should be at Excellence Playa Mujeres, not Sandals. But that's a different video."
</div>

<h2>Newsletter Content — All-Inclusives</h2>
<p>The newsletter is where all-inclusive content goes deep. Format:</p>
<ul>
<li><strong>Lead piece (500-700 words):</strong> A single ranking, comparison, or insider piece. "Excellence Playa Mujeres vs Punta Cana — the verdict." "The 4 Hyatt Inclusive Collection properties worth booking."</li>
<li><strong>Receipt block:</strong> One real booking with full upgrade math.</li>
<li><strong>Three quick takes:</strong> One AI hot take + one industry observation + one calendar tip.</li>
</ul>

<h2>The 30 All-Inclusive Content Ideas (Stock Bank)</h2>
<ol>
<li>Excellence Playa Mujeres vs Excellence Punta Cana (the verdict)</li>
<li>The Hyatt Inclusive Collection ranked (Secrets / Dreams / Zoëtry / Breathless / Ziva / Zilara)</li>
<li>Why Hyatt Privé changed all-inclusive booking</li>
<li>Sandals: which 2 properties are actually good (everything else is mid)</li>
<li>The 5 mistakes people make booking Riviera Maya</li>
<li>Sargassum season: where to go and where to skip May-Oct</li>
<li>Excellence Club tier: the math</li>
<li>Le Blanc Cancun vs Atelier Playa Mujeres</li>
<li>The 3 best family all-inclusives in the Caribbean</li>
<li>The 3 best adults-only all-inclusives in Mexico</li>
<li>Why I'd never book Royalton CHIC (and who should)</li>
<li>Booking.com vs. Preface: the actual difference on a $5K resort booking</li>
<li>The 3 hotels you should stay at vs the 3 you think you should</li>
<li>Rosewood Mayakoba: not an all-inclusive but functions like one (the meal plan trick)</li>
<li>Christmas week pricing: how to think about it</li>
<li>Beach quality matrix: Turks vs Riviera Maya vs DR</li>
<li>Why your honeymoon shortlist is wrong (3 reasons)</li>
<li>The Beaches Turks family verdict</li>
<li>What to pack for an all-inclusive that's NOT in any packing list</li>
<li>The restaurant reservation strategy at Excellence (it's not what they tell you)</li>
<li>Why the Maldives in August is a scam</li>
<li>The Pacific Mexico vs Riviera Maya debate (Cabo / Cancun / PV)</li>
<li>How to read an all-inclusive review without being misled</li>
<li>The "Club" tier across brands (Excellence Club / Privé / Preferred / Atelier Inspira)</li>
<li>Hyatt Inclusive vs traditional Hyatt resort: the difference</li>
<li>The 2 honeymoon properties no one books that they should</li>
<li>The bach weekend resort verdict (3 picks, ranked)</li>
<li>What makes Zoetry Agua Punta Cana the calmest AI in the Caribbean</li>
<li>Tour-operator packages vs hotel-direct: when each wins (Sunwing math vs Privé math)</li>
<li>My biggest all-inclusive booking regret</li>
</ol>
</section>

<!-- 03 HONEYMOON CONTENT -->
<section>
<div class="segment-content-block">
    <div class="num">— CONTENT FOR SEGMENT 02</div>
    <h1>Honeymoon <em>Content</em></h1>
    <div class="sub">Aspirational + visual. Less hot-take, more "here's the trip you want." Honeymoon content is the strongest IG segment because the demographic spends hours saving honeymoon posts.</div>
</div>

<h2>Channel Priority</h2>
<div class="platform-priority">
    <div class="pp tier-1">
        <div class="name">Instagram</div>
        <div class="priority">— Tier 1</div>
        <div class="why">Pinterest-style saving behavior is real. Carousels of honeymoon properties hit 10x baseline reach.</div>
    </div>
    <div class="pp tier-2">
        <div class="name">TikTok</div>
        <div class="priority">— Tier 2</div>
        <div class="why">"Honeymoon ideas you haven't thought of" format performs well.</div>
    </div>
    <div class="pp tier-2">
        <div class="name">Newsletter</div>
        <div class="priority">— Tier 2</div>
        <div class="why">Honeymoon deep-reads (Maldives ranked, Bali vs Bora Bora, Italy itineraries).</div>
    </div>
    <div class="pp tier-3">
        <div class="name">LinkedIn</div>
        <div class="priority">— Tier 3</div>
        <div class="why">Mostly skip. Use only for "lessons from planning 50 honeymoons" founder posts.</div>
    </div>
</div>

<h2>The Four Honeymoon Content Pillars</h2>
<table>
<thead><tr><th>Pillar</th><th>What it is</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Profile</strong></td><td>"The 4 honeymoon profiles (which one are you)" — quiz/framework format. Beach &amp; lie down / Multi-city Europe / Adventure + recover / Maldives over-water.</td><td>Monthly</td></tr>
<tr><td><strong>The Destination Deep Dive</strong></td><td>One destination, one carousel/long-read. "Maldives ranked." "Why Greek Islands beat Amalfi for honeymoons." "Bali by region."</td><td>2x/mo</td></tr>
<tr><td><strong>The Property Spotlight</strong></td><td>One hotel, photo essay + commentary. Why it works for honeymooners specifically.</td><td>2x/mo</td></tr>
<tr><td><strong>The Common Mistake</strong></td><td>"3 honeymoon planning mistakes." "Why your shortlist is wrong."</td><td>Monthly</td></tr>
</tbody>
</table>

<h2>Instagram Templates — Honeymoon</h2>

<div class="post-template">
<div class="lab">Carousel — The Profile Quiz</div>
<strong>Slide 1:</strong> "Honeymoon planning is paralyzing. Here's the framework I use."<br/>
<strong>Slide 2:</strong> "Question 1: Sit-on-the-beach-for-a-week, or move every 3 days?"<br/>
<strong>Slide 3:</strong> "Question 2: Activity-packed, or actively-doing-nothing?"<br/>
<strong>Slide 4:</strong> "Question 3: Comfort food / familiar / restaurant menus, or local + adventurous?"<br/>
<strong>Slide 5:</strong> "Question 4: $10K budget, $15K, $20K, $25K+?"<br/>
<strong>Slides 6-9:</strong> 4 profile cards. Each: title, 1-sentence summary, 2 destination recommendations.<br/>
<strong>Slide 10:</strong> CTA — "Book a 20-min call. preface.travel."<br/>
<em>This format gets shared in honeymoon-planning DMs. High save rate.</em>
</div>

<div class="post-template">
<div class="lab">Single Post — The Property Spotlight</div>
<strong>Image:</strong> One stunning hotel photo (real, not stock).<br/>
<strong>Caption:</strong> "Six Senses Bhutan is the most underrated honeymoon property right now.<br/><br/>
$1,200/night sounds high. It includes everything: meals, activities, transfers between five Six Senses lodges spread across the country.<br/><br/>
For couples who want 'somewhere your friends haven't been' — this is the answer.<br/><br/>
On a 9-night itinerary I just booked: $11,000/pp all-in including flights. Honestly, that's not crazy for what you get."<br/>
<em>Hook is the destination, not the brand. Property name is the credibility.</em>
</div>

<h2>TikTok Templates — Honeymoon</h2>

<div class="post-template">
<div class="lab">TikTok — "POV: You're planning a honeymoon"</div>
<strong>Opening:</strong> "POV: you're planning a honeymoon and you've narrowed it down to 5 places. They all look the same on Instagram."<br/>
<strong>15-30 sec:</strong> "I'll save you 3 hours. Pick based on these 3 questions."<br/>
<strong>30-45 sec:</strong> "Beach-and-don't-move OR move-every-3-days? / Tropical OR seasonal? / $15K range OR $25K+ range?"<br/>
<strong>45-60 sec:</strong> "Beach-tropical-$15K = Riviera Maya 5-star or Maldives shoulder season. Beach-seasonal-$15K = Greek Islands. Multi-stop-tropical-$25K = Bali + Singapore."<br/>
<strong>Close:</strong> "Book a call and I'll narrow it from 5 to 1."
</div>

<h2>Newsletter — Honeymoon</h2>
<p>Quarterly deep-dive issues focused on honeymoon-specific topics:</p>
<ul>
<li><strong>Issue:</strong> "Maldives, ranked. The 14 resorts I'd consider."</li>
<li><strong>Issue:</strong> "Bali by region: which one for which couple."</li>
<li><strong>Issue:</strong> "Greek Islands vs. Amalfi: honest verdict."</li>
<li><strong>Issue:</strong> "South Africa + Mauritius: the 14-day itinerary."</li>
<li><strong>Issue:</strong> "Why honeymoons cost what they cost (the math)."</li>
</ul>

<h2>The 20 Honeymoon Content Ideas (Stock Bank)</h2>
<ol>
<li>The 4 honeymoon profiles framework</li>
<li>Maldives, ranked</li>
<li>Bali by region (Ubud vs. Seminyak vs. Nusa Dua vs. Uluwatu)</li>
<li>Greek Islands honeymoon: Santorini vs. Mykonos vs. Crete vs. Milos</li>
<li>South Africa + Mauritius: the 14-day itinerary</li>
<li>Bora Bora vs. Maldives: the verdict</li>
<li>Why your honeymoon shortlist is wrong (3 reasons)</li>
<li>The 3 honeymoon properties you've never heard of</li>
<li>Best honeymoon time of year by destination (the calendar)</li>
<li>How to honeymoon for under $10K (with full perks)</li>
<li>Bali + Singapore + Tokyo: the 14-day adventure honeymoon</li>
<li>Multi-stop vs. one-place: how to choose</li>
<li>Italy honeymoon: Amalfi or Lake Como or Tuscany</li>
<li>The Six Senses honeymoon list (top 5)</li>
<li>How long should a honeymoon actually be?</li>
<li>The post-wedding 3-night vs. 14-night decision</li>
<li>Honeymoon registries: do they work?</li>
<li>Aman vs. Belmond vs. Six Senses: the comparison</li>
<li>The 5 most-overrated honeymoon destinations</li>
<li>How to honeymoon planning timeline (12-9-6-3-month checkpoints)</li>
</ol>
</section>

<!-- 04 BACH CONTENT -->
<section>
<div class="segment-content-block">
    <div class="num">— CONTENT FOR SEGMENT 03</div>
    <h1>Bach Weekend <em>Content</em></h1>
    <div class="sub">The demographic that scrolls IG and TikTok hardest. Smaller content investment, but highest conversion rate from content to inquiry. 8-15 women planning together = high-share content goes viral within the group.</div>
</div>

<h2>Channel Priority</h2>
<div class="platform-priority">
    <div class="pp tier-1">
        <div class="name">Instagram</div>
        <div class="priority">— Tier 1</div>
        <div class="why">The maid-of-honor is on IG. Carousel destinations + villa tours convert.</div>
    </div>
    <div class="pp tier-1">
        <div class="name">TikTok</div>
        <div class="priority">— Tier 1</div>
        <div class="why">"Bach destination ideas" videos blow up. Demographic is exactly here.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">Newsletter</div>
        <div class="priority">— Tier 3</div>
        <div class="why">Light coverage. One bach-specific newsletter per quarter.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">LinkedIn</div>
        <div class="priority">— Skip</div>
        <div class="why">Not where the buyer hangs out.</div>
    </div>
</div>

<h2>Three Bach Content Pillars</h2>
<table>
<thead><tr><th>Pillar</th><th>What it is</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Destination List</strong></td><td>"5 underrated bach destinations." "Mykonos vs Mexico City vs Lisbon: which one for your group."</td><td>Monthly</td></tr>
<tr><td><strong>The Logistics Post</strong></td><td>"How to actually plan a 10-person bach without ending friendships." "The MOH guide to villa rentals."</td><td>Bi-monthly</td></tr>
<tr><td><strong>The Vibe Show</strong></td><td>Real client trip highlights. Specific villas, specific dinners, specific bach moments.</td><td>2x/mo</td></tr>
</tbody>
</table>

<h2>IG Templates — Bach</h2>

<div class="post-template">
<div class="lab">Carousel — "5 underrated bach destinations"</div>
<strong>Slide 1:</strong> "Mykonos is overdone. Tulum is sold out. Here are 5 bach destinations no one in your group has already booked."<br/>
<strong>Slides 2-6:</strong> One destination per slide. Photo + name + key benefits + estimated per-person cost.<br/>
- Mexico City (~$1,500/pp, food + speakeasies + spa)<br/>
- Lisbon (~$1,800/pp, beach + tile + nightlife)<br/>
- Nashville (~$1,500/pp, no passport + brunch + music)<br/>
- Cabo (~$2,000/pp, beach + clubs + private villas)<br/>
- Bermuda (~$2,400/pp, 2-hr flight + pink sand + civilized)<br/>
<strong>Slide 7:</strong> CTA — "Need help planning? Book a call: preface.travel."
</div>

<div class="post-template">
<div class="lab">Reel — "MOH POV"</div>
<strong>Open:</strong> "POV: you're the MOH and you have 8 group texts."<br/>
<strong>Cut to:</strong> "Here's how I plan it without losing my mind."<br/>
<strong>15-45 sec:</strong> 3-step framework: 1) Lock dates first. 2) Lock budget per person. 3) Pick one destination + one anchor activity. Everything else flexes.<br/>
<strong>Close:</strong> "Or DM me. I do this for a living."
</div>

<h2>The 12 Bach Content Ideas (Stock Bank)</h2>
<ol>
<li>5 underrated bach destinations</li>
<li>How to plan a 10-person bach without ending friendships</li>
<li>Mykonos vs. Tulum vs. Lisbon — which one for your group?</li>
<li>Villa vs. resort vs. boutique hotel: the bach decision</li>
<li>How to handle the budget-conscious member of the group</li>
<li>The 3-day vs. 4-day vs. 5-day bach: real economics</li>
<li>Nashville bach: actually fine. Here's the play.</li>
<li>Cabo: the 3 specific resorts/villas to consider</li>
<li>How to pre-book restaurants at every bach destination (the actual list)</li>
<li>The Bermuda bach pitch (no passport, civilized)</li>
<li>Mexico City bach 4-day itinerary</li>
<li>The bride's vote isn't more important. Here's how to actually decide as a group.</li>
</ol>
</section>

<!-- 05 BUSINESS TRAVEL CONTENT -->
<section>
<div class="segment-content-block">
    <div class="num">— CONTENT FOR SEGMENT 04</div>
    <h1>Business Travel <em>Content</em></h1>
    <div class="sub">LinkedIn-led. Different audience, different tone. The buyer is a founder or sales exec, not a couple planning a honeymoon. Voice is the same — opinionated, specific — but the substance shifts from "where to vacation" to "how to optimize the travel you're already doing."</div>
</div>

<h2>Channel Priority</h2>
<div class="platform-priority">
    <div class="pp tier-1">
        <div class="name">LinkedIn</div>
        <div class="priority">— Tier 1</div>
        <div class="why">The buyer lives here. Founders + sales leaders + consulting partners read LinkedIn daily.</div>
    </div>
    <div class="pp tier-2">
        <div class="name">Newsletter</div>
        <div class="priority">— Tier 2</div>
        <div class="why">Once a month: BT-focused issue. Hotel ranks for execs, loyalty math, travel optimization.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">Instagram</div>
        <div class="priority">— Skip</div>
        <div class="why">Wrong demographic for this funnel.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">TikTok</div>
        <div class="priority">— Skip</div>
        <div class="why">Same as IG. Founders aren't here for travel advice.</div>
    </div>
</div>

<h2>Four BT Content Pillars</h2>
<table>
<thead><tr><th>Pillar</th><th>What it is</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Loyalty Math</strong></td><td>Hyatt Globalist vs Marriott Titanium vs Hilton Diamond — when each pays off. Status match strategies.</td><td>2x/mo</td></tr>
<tr><td><strong>The Hotel Pick</strong></td><td>"3 Toronto hotels for execs." "Best Marriott in Manhattan for late check-in." "Where to stay in Austin for SXSW."</td><td>2x/mo</td></tr>
<tr><td><strong>The Optimization Insight</strong></td><td>How Privé / STARS / Impresario actually layers onto a business trip. The 15 minutes a week you're losing on Marriott.com.</td><td>2x/mo</td></tr>
<tr><td><strong>The Founder Lesson</strong></td><td>Story-led posts. "Last week I rebooked a flight for a client at 11pm on a Sunday from Lisbon." Drives credibility + trust.</td><td>2x/mo</td></tr>
</tbody>
</table>

<h2>LinkedIn Post Templates — BT</h2>

<div class="post-template">
<div class="lab">Insight Post — The Loyalty Math</div>
<strong>Hook line:</strong> "If you travel for work 40+ nights/year, you're picking the wrong hotel chain."<br/><br/>
<strong>Body:</strong> "Most founders default to whichever chain they started with (Marriott if their first job had Bonvoy, Hilton if SPG was discontinued).<br/><br/>
But the loyalty math diverges sharply at the 40-night mark:<br/><br/>
&mdash; Hyatt Globalist (60 nights or 100K base points): suite upgrades on every paid stay, free breakfast, late check-out. The cleanest deal of the three.<br/><br/>
&mdash; Marriott Titanium (75 nights): suite upgrades on cash stays only, 50% bonus points, free breakfast at most brands. Largest network but stingiest perks.<br/><br/>
&mdash; Hilton Diamond (60 nights or 100K points): breakfast, room upgrades (rare), executive lounge. Lowest threshold but lightest amenities.<br/><br/>
At 40+ nights/year, Hyatt is the math. At 75+ nights, you go Marriott for the footprint."<br/><br/>
<strong>Closer:</strong> "I help founders + sales execs in Toronto pick which chain and stop wasting status. DM if you're under-optimized."
</div>

<div class="post-template">
<div class="lab">Story Post — The Disruption Save</div>
<strong>Hook:</strong> "Got a text at 11pm Sunday. Client's flight from Lisbon back to YYZ cancelled. He had a 9am Monday board meeting."<br/><br/>
<strong>Body:</strong> "Standard travel-disruption playbook:<br/><br/>
1. Check next-available alternatives (3 options in 5 minutes via Fora flights desk).<br/>
2. Re-book on TAP via FRA, arrives YYZ 7am Monday.<br/>
3. Alert hotel of late check-in.<br/>
4. Text client: 'Done. Here's your new itinerary. Sleep.'<br/><br/>
He made the board meeting. He texted thanks. He didn't have to spend 2 hours on hold with the airline at 3am from a Lisbon hotel."<br/><br/>
<strong>Closer:</strong> "This is the actual value-prop of a travel desk. The Marriott points stay yours. The 11pm scramble doesn't."
</div>

<h2>Newsletter (LinkedIn-Adjacent BT Issues)</h2>
<p>Monthly BT-focused issue subjects:</p>
<ul>
<li>"The 5 Toronto hotels for executive travelers, ranked"</li>
<li>"Hyatt Globalist math: when it pays off"</li>
<li>"The 3 Marriott STARS properties I'd recommend in Manhattan"</li>
<li>"How to status-match across Marriott, Hyatt, Hilton in one week"</li>
<li>"The exec travel anti-patterns that cost you 30 min/wk"</li>
</ul>

<h2>The 18 BT Content Ideas (Stock Bank)</h2>
<ol>
<li>5 Toronto hotels for executive travelers (ranked)</li>
<li>Hyatt Globalist vs Marriott Titanium math</li>
<li>How status-matching actually works (Marriott / Hyatt / Hilton)</li>
<li>The 3 best Marriott STARS properties in Manhattan</li>
<li>Why most founders are using the wrong hotel chain</li>
<li>The 15 minutes a week you're losing on Marriott.com</li>
<li>What Hyatt Privé actually does for a business traveler</li>
<li>Hilton Impresario vs. Marriott STARS: the verdict</li>
<li>Executive travel: when to fly biz vs eco vs premium eco</li>
<li>The disruption-recovery playbook (real client story)</li>
<li>Earning miles for status vs cash for upgrades: the trade-off</li>
<li>The 5 hotels I'd avoid in [city]</li>
<li>How I helped a founder save 30 minutes a week</li>
<li>The most underrated chain for business travel (it's Hyatt)</li>
<li>Late check-in: the policy by chain</li>
<li>The points-vs-cash decision: a framework</li>
<li>How to handle business + personal travel on the same card</li>
<li>The 3 Toronto hotels for in-person client meetings</li>
</ol>
</section>

<!-- 06 FAMILY CONTENT -->
<section>
<div class="segment-content-block">
    <div class="num">— CONTENT FOR SEGMENT 05</div>
    <h1>Family Travel <em>Content</em></h1>
    <div class="sub">Newsletter-led. Parents read newsletters more than they scroll TikTok. Less visual emphasis, more practical-utility content. The audience overlaps heavily with All-Inclusives, so much of the content cross-pollinates.</div>
</div>

<h2>Channel Priority</h2>
<div class="platform-priority">
    <div class="pp tier-1">
        <div class="name">Newsletter</div>
        <div class="priority">— Tier 1</div>
        <div class="why">Parents read in the morning, after kids are in school. Family content gets 50%+ open rates here.</div>
    </div>
    <div class="pp tier-2">
        <div class="name">Instagram</div>
        <div class="priority">— Tier 2</div>
        <div class="why">Carousels (kid-friendly resort guides). Less Reels-heavy than honeymoon.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">LinkedIn</div>
        <div class="priority">— Tier 3</div>
        <div class="why">Occasional family-travel posts. Often when planning around a school break.</div>
    </div>
    <div class="pp tier-3">
        <div class="name">TikTok</div>
        <div class="priority">— Skip</div>
        <div class="why">Demographic doesn't consume primary travel content here.</div>
    </div>
</div>

<h2>Four Family Content Pillars</h2>
<table>
<thead><tr><th>Pillar</th><th>What it is</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td><strong>The Calendar Plan</strong></td><td>"March break planning starts now." "Summer family travel: where to go." Seasonally-anchored content.</td><td>Quarterly + leading edges</td></tr>
<tr><td><strong>The Resort Family-Verdict</strong></td><td>Specific resort reviews for families. Hyatt Ziva, Beaches Turks, Excellence (yes, kids welcome), Princess family.</td><td>Monthly</td></tr>
<tr><td><strong>The Practical Guide</strong></td><td>"What to pack." "How to book flights with kids." "Restaurant strategies at all-inclusives." Utility-heavy.</td><td>Monthly</td></tr>
<tr><td><strong>The Multi-Gen Trip</strong></td><td>3-generation family travel. Cross-pollinates with Milestone Group segment.</td><td>Quarterly</td></tr>
</tbody>
</table>

<h2>Newsletter Templates — Family</h2>

<div class="post-template">
<div class="lab">Newsletter Issue: "March Break Planning Starts Now"</div>
<strong>Lead piece (500 words):</strong> Why March break booking starts in October, not February. Specific properties booking out: Beaches Turks (sold out by Dec), Hyatt Ziva (Dec). Sunwing inventory model. The flexible-dates trick.<br/>
<strong>Receipt:</strong> "Last week I booked a family of 4 to Beaches Turks for March break. Total cost: $11,200. Through me vs. direct: $1,840 in added value (suite upgrade + breakfast for 4 + $250 resort credit + waterpark passes)."<br/>
<strong>Three quick takes:</strong> Mexico vs. DR for kids / The Hyatt Inclusive Collection family verdict / Why you shouldn't book the connecting room (book the suite instead)
</div>

<div class="post-template">
<div class="lab">Newsletter Issue: "The 4 Hyatt Inclusive Resorts For Families"</div>
<strong>Lead piece:</strong> Detailed take on Hyatt Ziva Cap Cana, Hyatt Ziva Rose Hall, Hyatt Ziva Riviera Cancun, Hyatt Ziva Cabo. For each: kids' programming, adult zones, beach quality, restaurant variety, my honest take.<br/>
<strong>Verdict:</strong> "Cap Cana for kids 7+. Rose Hall for adventure. Cabo for older families. Riviera Cancun for the multi-gen play."
</div>

<h2>Instagram — Family</h2>
<p>Less aggressive than honeymoon/all-inclusive. 2 posts/week:</p>
<ul>
<li>1 carousel/week: family-focused resort comparison or seasonal planner</li>
<li>1 reel/week (optional): "What to actually pack for a kids' all-inclusive" / "The restaurant strategy"</li>
</ul>

<h2>The 15 Family Content Ideas (Stock Bank)</h2>
<ol>
<li>March break planning starts now: where + when</li>
<li>The 4 Hyatt Inclusive resorts for families (ranked)</li>
<li>Mexico vs. DR for family travel: the verdict</li>
<li>Why Beaches Turks is worth the premium</li>
<li>The all-inclusive restaurant strategy with kids</li>
<li>How to pack for a kids' all-inclusive (the real list)</li>
<li>Summer family travel: where to go, where to skip</li>
<li>Multi-gen family trips: where they actually work</li>
<li>The connecting room vs. suite decision</li>
<li>Best kids' clubs in the Caribbean</li>
<li>How to book flights with kids (the seat-selection hack)</li>
<li>Why Sunwing is fine — when it's fine</li>
<li>The 3 resorts I'd never take kids to</li>
<li>Best family-friendly Mexico Pacific resorts</li>
<li>March break vs. winter holiday: cost comparison</li>
</ol>
</section>

<!-- 07 NEWSLETTER DEEP DIVE -->
<section>
<h1><span class="num">Section 07</span>Newsletter Deep Dive (The Owned Asset)</h1>
<p class="section-intro">Newsletter is the only channel that survives algorithm changes. It's also the highest-trust audience. Treat it accordingly.</p>

<h2>The Goal Trajectory</h2>
<table>
<thead><tr><th>Milestone</th><th>Target subs</th><th>What it enables</th></tr></thead>
<tbody>
<tr><td>M3</td><td>200</td><td>Validates the format. Word-of-mouth growth starts.</td></tr>
<tr><td>M6</td><td>1,000</td><td>Beehiiv paid tier unlocks. Cross-promotion starts.</td></tr>
<tr><td>M9</td><td>2,500</td><td>Newsletter referral program live.</td></tr>
<tr><td>M12</td><td>5,000</td><td>Sponsor/swap deals viable.</td></tr>
<tr><td>M18</td><td>10,000+</td><td>Paid tier launches. Material revenue.</td></tr>
<tr><td>M24</td><td>20,000+</td><td>Cohort of brand-defining readers. Newsletter alone drives 30%+ of inbound.</td></tr>
</tbody>
</table>

<h2>The Issue Format (Every Other Friday, 10am ET)</h2>
<table>
<thead><tr><th>Block</th><th>Length</th><th>Voice notes</th></tr></thead>
<tbody>
<tr><td><strong>Subject line</strong></td><td>~6 words</td><td>Curiosity over announcement. "Excellence vs. Excellence." "Sandals: the verdict."</td></tr>
<tr><td><strong>One-line opener</strong></td><td>1 sentence</td><td>Often a take. Sets tone. "Booking.com is lying to you about resort upgrades."</td></tr>
<tr><td><strong>The Take (lead piece)</strong></td><td>500&ndash;700 words</td><td>One destination, one comparison, or one insider tip. Be specific.</td></tr>
<tr><td><strong>The Receipt</strong></td><td>100&ndash;150 words</td><td>Real anonymized booking math. Hotel, room, upgrade, total value.</td></tr>
<tr><td><strong>Three Quick Hits</strong></td><td>~75 words total</td><td>One opinion + one insider tip + one seasonal calendar note.</td></tr>
<tr><td><strong>The CTA</strong></td><td>1 line</td><td>"Trip on the calendar? Hit reply." OR "Book a 20-min call." Vary monthly.</td></tr>
<tr><td><strong>The P.S.</strong></td><td>1 line</td><td>Optional. Personal moment. Builds intimacy. "P.S. Just booked a family of 4 to Beaches Turks. They were genuinely surprised by how good it is."</td></tr>
</tbody>
</table>

<h2>The Subject Line Library (Use These, Don't Invent New Ones Until You've Used These)</h2>
<table>
<thead><tr><th>Pattern</th><th>Example</th></tr></thead>
<tbody>
<tr><td>[Brand] vs. [Brand]</td><td>"Excellence vs. Excellence (the verdict)"</td></tr>
<tr><td>The [Number] [Things]</td><td>"The 3 honeymoon properties no one books"</td></tr>
<tr><td>[Brand] is [opinion]</td><td>"Sandals is mid"</td></tr>
<tr><td>Why [counterintuitive claim]</td><td>"Why your honeymoon shortlist is wrong"</td></tr>
<tr><td>The [adjective] [thing]</td><td>"The honest Maldives ranking"</td></tr>
<tr><td>How to [achieve outcome] without [common mistake]</td><td>"How to plan a 10-pax bach without ending friendships"</td></tr>
<tr><td>What [hotel/brand] [does/doesn't tell you]</td><td>"What Excellence doesn't tell you about Club tier"</td></tr>
<tr><td>The [time period] best/worst</td><td>"Q1's most-booked resorts (with verdicts)"</td></tr>
</tbody>
</table>

<h2>Newsletter Growth Tactics (In Order)</h2>
<ol>
<li><strong>Default everywhere (M1 onwards):</strong> Every IG, TikTok, LinkedIn post ends with "newsletter at preface.travel."</li>
<li><strong>Welcome sequence (M2):</strong> 3-email welcome on signup. (Email 1 = welcome. Email 2 = the all-inclusives starter guide. Email 3 = "want a 20-min call?")</li>
<li><strong>Cross-promotion swaps (M4):</strong> Trade newsletter mentions with 5-10 other Toronto creators (food, lifestyle, real estate, wedding) at 500&ndash;1,000 subs.</li>
<li><strong>Lead magnet (M5):</strong> "The All-Inclusives Decision Guide" gated PDF. Email-gated download. Promote on IG.</li>
<li><strong>Beehiiv Referral Program (M6):</strong> Built-in mechanic. Rewards at 3/10/25 referrals. (Reward: exclusive content, then a 1-on-1 call, then a $200 credit toward planning fee.)</li>
<li><strong>SparkLoop or Beehiiv Boosts (M12+):</strong> Pay for newsletter subs. Cost: $1&ndash;3/sub. Only when conversion math justifies.</li>
<li><strong>Paid newsletter tier (M18+):</strong> $10/mo. Templates, exclusive resort intel, monthly Q&amp;A call. Aim for 1&ndash;2% paid conversion.</li>
</ol>
</section>

<!-- 08 REPURPOSING -->
<section>
<h1><span class="num">Section 08</span>The Repurposing System</h1>
<p class="section-intro">One source → 5 outputs. Don't make content separately for each channel. The repurposing waterfall is the only way to ship at the cadence required.</p>

<h2>The Weekly Cycle</h2>
<table>
<thead><tr><th>Day</th><th>Action</th><th>Owner</th><th>Output</th></tr></thead>
<tbody>
<tr><td>Sunday</td><td>Founder picks topic from stock bank</td><td>You</td><td>Topic + angle</td></tr>
<tr><td>Monday</td><td>Founder records 5-8 min voice memo</td><td>You</td><td>1 raw voice memo</td></tr>
<tr><td>Tuesday</td><td>VA transcribes + drafts newsletter</td><td>VA</td><td>Newsletter draft</td></tr>
<tr><td>Wednesday</td><td>VA extracts derivatives: 1 LinkedIn post + 1 IG carousel + 1 IG reel script + 1 TikTok script + 1 LinkedIn carousel (PDF)</td><td>VA</td><td>5 derivative drafts</td></tr>
<tr><td>Thursday</td><td>VA designs IG carousel in Canva + edits all videos</td><td>VA</td><td>Visual assets ready</td></tr>
<tr><td>Thursday PM</td><td>Founder reviews batch (30 min)</td><td>You</td><td>Approved content</td></tr>
<tr><td>Friday 10am</td><td>Newsletter publishes</td><td>VA</td><td>Live</td></tr>
<tr><td>Friday-Sunday</td><td>VA schedules week's social via Buffer</td><td>VA</td><td>Queued</td></tr>
<tr><td>Saturday</td><td>Founder records 2 TikToks (batch, 15&ndash;30 min)</td><td>You</td><td>2 raw clips</td></tr>
<tr><td>Sunday</td><td>VA edits TikToks → schedule for Mon/Wed</td><td>VA</td><td>Queued</td></tr>
</tbody>
</table>

<h2>The Five Outputs From One Topic</h2>
<table>
<thead><tr><th>Output</th><th>From source</th><th>Time</th></tr></thead>
<tbody>
<tr><td>Newsletter issue (~600 words)</td><td>Voice memo transcript, edited + structured</td><td>~45 min VA</td></tr>
<tr><td>LinkedIn post (300&ndash;400 words)</td><td>Strongest insight from voice memo, reframed for biz/professional audience</td><td>~20 min VA</td></tr>
<tr><td>IG carousel (10 slides)</td><td>The newsletter's structure, broken into one-slide-per-point</td><td>~60 min VA (incl. Canva design)</td></tr>
<tr><td>IG reel + TikTok (60&ndash;90 sec)</td><td>The hottest take from the voice memo, scripted for video</td><td>~30 min script + 15 min you record</td></tr>
<tr><td>LinkedIn carousel PDF</td><td>The IG carousel, re-styled for LinkedIn (longer slides, more text)</td><td>~30 min VA</td></tr>
</tbody>
</table>

<h2>The Quarterly Best-Of Repurpose</h2>
<p>Every 3 months, the highest-performing newsletter pieces get re-bundled:</p>
<ul>
<li>Top 3 issues → gated PDF lead magnet</li>
<li>Top 5 hot takes → LinkedIn carousel + IG carousel</li>
<li>Top resort reviews → updates to the All-Inclusives website page</li>
<li>Top client stories → new Receipts section on homepage</li>
</ul>
</section>

<!-- 09 52-WEEK CALENDAR -->
<section>
<h1><span class="num">Section 09</span>52-Week Master Calendar</h1>
<p class="section-intro">The full year of content themes. Map your voice memos to these. Repeat the cycle Y2 with refreshed angles.</p>

<h2>Q1 — January-March</h2>

<div class="calendar-week"><div class="week-num">— W1 (Jan, first week)</div><div class="theme">"The Travel Year Ahead — what to book now"</div><div class="grid"><div><span class="lab">Newsletter:</span> Forecasting trip planning for the year</div><div><span class="lab">Social:</span> Resort rankings carousel</div></div></div>

<div class="calendar-week"><div class="week-num">— W2</div><div class="theme">"March break planning is now"</div><div class="grid"><div><span class="lab">Newsletter:</span> March break specific (Family)</div><div><span class="lab">Social:</span> Family resort comparison</div></div></div>

<div class="calendar-week"><div class="week-num">— W3</div><div class="theme">"Excellence Playa Mujeres vs Punta Cana"</div><div class="grid"><div><span class="lab">Newsletter:</span> The verdict (All-Inclusives)</div><div><span class="lab">Social:</span> Side-by-side carousel + reel</div></div></div>

<div class="calendar-week"><div class="week-num">— W4</div><div class="theme">"Honeymoon math: planning timeline"</div><div class="grid"><div><span class="lab">Newsletter:</span> 12-9-6-3 timeline (Honeymoon)</div><div><span class="lab">Social:</span> The 4 honeymoon profiles carousel</div></div></div>

<div class="calendar-week"><div class="week-num">— W5</div><div class="theme">"Sandals is mid"</div><div class="grid"><div><span class="lab">Newsletter:</span> The verdict (All-Inclusives)</div><div><span class="lab">Social:</span> Hot take reel + carousel ranking</div></div></div>

<div class="calendar-week"><div class="week-num">— W6</div><div class="theme">"The 5 Toronto hotels for executive travel"</div><div class="grid"><div><span class="lab">Newsletter:</span> Toronto hotel ranking (BT)</div><div><span class="lab">LinkedIn:</span> Status math + ranking</div></div></div>

<div class="calendar-week"><div class="week-num">— W7</div><div class="theme">"Hyatt Privé changes all-inclusive booking"</div><div class="grid"><div><span class="lab">Newsletter:</span> The Inclusive Collection deep-dive</div><div><span class="lab">Social:</span> IG carousel + TikTok</div></div></div>

<div class="calendar-week"><div class="week-num">— W8</div><div class="theme">"Maldives, ranked"</div><div class="grid"><div><span class="lab">Newsletter:</span> The 14 resorts (Honeymoon)</div><div><span class="lab">Social:</span> Carousel + IG reel tour of 1 property</div></div></div>

<div class="calendar-week"><div class="week-num">— W9-12</div><div class="theme">Bach destinations + Spring break wrap + March-break receipts + Hyatt Globalist math</div><div class="grid"><div><span class="lab">Newsletter:</span> Q1 best-of issue (W12)</div><div><span class="lab">Social:</span> Spring break content + bach destinations</div></div></div>

<h2>Q2 — April-June</h2>

<div class="calendar-week"><div class="week-num">— W13-16</div><div class="theme">"Honeymoon season opens" / Greek Islands ranked / Bali by region / The 3 Hyatt Inclusive family resorts</div><div class="grid"><div><span class="lab">Newsletter:</span> Honeymoon focus (W14)</div><div><span class="lab">Social:</span> Bali carousel + Maldives reel</div></div></div>

<div class="calendar-week"><div class="week-num">— W17-20</div><div class="theme">Le Blanc vs Atelier / Sargassum season warning / Summer family planning / Bach Mexico City + Lisbon</div><div class="grid"><div><span class="lab">Newsletter:</span> Sargassum issue (W19)</div><div><span class="lab">Social:</span> Bach carousel + Le Blanc tour reel</div></div></div>

<div class="calendar-week"><div class="week-num">— W21-26</div><div class="theme">Summer travel hot takes + Tulum truth + Cabo bach guide + 3 underrated honeymoons</div><div class="grid"><div><span class="lab">Newsletter:</span> Q2 best-of (W26)</div><div><span class="lab">Social:</span> Bach reels + Tulum take</div></div></div>

<h2>Q3 — July-September</h2>

<div class="calendar-week"><div class="week-num">— W27-32</div><div class="theme">Italy honeymoons / The Toronto hotel ranking / Why Sunwing is fine (and when) / Bermuda bach / Multi-gen group play</div><div class="grid"><div><span class="lab">Newsletter:</span> Italy honeymoon issue (W29)</div><div><span class="lab">Social:</span> Italy carousel + bach reels</div></div></div>

<div class="calendar-week"><div class="week-num">— W33-39</div><div class="theme">Winter break planning / Hyatt status year-end push / Bach destinations recap / 5 mistakes when booking December resorts</div><div class="grid"><div><span class="lab">Newsletter:</span> Winter planning (W36)</div><div><span class="lab">Social:</span> Year-end status push (LinkedIn)</div></div></div>

<h2>Q4 — October-December</h2>

<div class="calendar-week"><div class="week-num">— W40-43</div><div class="theme">Christmas booking deadline approaches / New Year planning / Best holiday resorts / Status-match year-end</div><div class="grid"><div><span class="lab">Newsletter:</span> Holiday booking (W41)</div><div><span class="lab">Social:</span> Family resort recommendations</div></div></div>

<div class="calendar-week"><div class="week-num">— W44-48</div><div class="theme">2027 trip planning / Best-of-year posts / FAM trip recaps / Honeymoon trends</div><div class="grid"><div><span class="lab">Newsletter:</span> Year-end best-of (W48)</div><div><span class="lab">Social:</span> Year-recap carousels + reels</div></div></div>

<div class="calendar-week"><div class="week-num">— W49-52</div><div class="theme">Holiday season / Christmas-week receipt / 2027 forecast / Personal year-end reflection</div><div class="grid"><div><span class="lab">Newsletter:</span> "The 2026 trips that worked" (W52)</div><div><span class="lab">Social:</span> Personal year-end posts</div></div></div>
</section>

<!-- 10 ANALYTICS -->
<section>
<h1><span class="num">Section 10</span>Analytics &amp; Optimization</h1>
<p class="section-intro">Track the leading and lagging indicators separately. The leading indicators tell you if it's working; the lagging tell you if it mattered.</p>

<h2>Weekly Analytics Review (Friday 5pm, 15 min)</h2>
<table>
<thead><tr><th>Metric</th><th>Where</th><th>What's normal</th></tr></thead>
<tbody>
<tr><td>Newsletter open rate</td><td>Beehiiv</td><td>40&ndash;55%</td></tr>
<tr><td>Newsletter click rate</td><td>Beehiiv</td><td>3&ndash;7%</td></tr>
<tr><td>Newsletter new subs (this week)</td><td>Beehiiv</td><td>10&ndash;100, scaling</td></tr>
<tr><td>IG reach this week</td><td>IG Insights</td><td>10K&ndash;100K, scaling</td></tr>
<tr><td>IG saves rate (top posts)</td><td>IG Insights</td><td>3&ndash;8%</td></tr>
<tr><td>LinkedIn impressions</td><td>LinkedIn</td><td>3K&ndash;30K/wk</td></tr>
<tr><td>TikTok views (top post)</td><td>TikTok Analytics</td><td>1K&ndash;100K, volatile</td></tr>
<tr><td>DMs received this week</td><td>Manual count</td><td>2&ndash;15 scaling</td></tr>
</tbody>
</table>

<h2>Monthly Deep Dive (Last Friday, 60 min)</h2>
<ol>
<li><strong>Inquiries with content attribution:</strong> Of new leads this month, how many referenced a specific post / newsletter / channel? Target: 30%+ by M12.</li>
<li><strong>Top 3 posts (by saves or shares):</strong> What's the pattern? Topic, format, hook? Repeat the pattern.</li>
<li><strong>Bottom 3 posts:</strong> What didn't work? Topic mismatch? Hook too soft? Visual problem?</li>
<li><strong>Channel performance ratio:</strong> Hours invested / inquiries generated. Cut the bottom channel if it's been bottom for 2 consecutive months.</li>
<li><strong>Newsletter cohort behavior:</strong> Open rate by signup vintage. If newer subs open less, the recent acquisition source is wrong.</li>
</ol>

<h2>The Kill / Scale Decision (Quarterly)</h2>
<table>
<thead><tr><th>Signal</th><th>Decision</th></tr></thead>
<tbody>
<tr><td>Channel produces &lt;2 inquiries / quarter after 90 days</td><td>Kill or reduce to 1 post/week</td></tr>
<tr><td>Channel produces &gt;15 inquiries / quarter</td><td>Double cadence; consider paid acquisition</td></tr>
<tr><td>Pillar performs 3x baseline</td><td>Increase that pillar to 40% of output</td></tr>
<tr><td>Pillar underperforms 50% of baseline 2 quarters in a row</td><td>Drop the pillar; reallocate</td></tr>
</tbody>
</table>

<div class="divider">&middot; &middot; &middot;</div>
<p style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 13pt; font-style: italic; color: #4a4a47;">End of Content Strategy v1</p>
</section>
"""


def main():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Preface — Content Strategy</title>
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
