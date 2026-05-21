"""Generate the Preface Brand Guide PDF — voice, mission, identity."""
from pathlib import Path
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import build_plan_pdf as v1

OUT = Path(__file__).parent / "Preface-Brand-Guide.pdf"

EXTRA_CSS = """
.manifesto-page {
    background: #0A0A0A; color: #FAFAF8;
    padding: 0.5in 0.7in; margin: -0.2in -0.7in 0.3in -0.7in;
    page-break-inside: avoid;
}
.manifesto-page .eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt; letter-spacing: 0.2em;
    text-transform: uppercase; color: #A85C3D;
    margin-bottom: 16pt; font-weight: 600;
}
.manifesto-page .statement {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22pt; font-weight: 400; line-height: 1.3;
    letter-spacing: -0.01em; color: #FAFAF8;
}
.manifesto-page .statement em { font-style: italic; color: #A85C3D; }
.dodont {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 0; margin: 0.15in 0;
    border: 1px solid #d4d2cc;
    page-break-inside: avoid;
}
.dodont .col { padding: 18px 22px; }
.dodont .col.do { border-right: 1px solid #d4d2cc; background: #f5f3ec; }
.dodont .col.dont { background: #fafaf8; }
.dodont .col .lab {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5pt; letter-spacing: 0.18em;
    text-transform: uppercase; font-weight: 600;
    margin-bottom: 10px;
}
.dodont .col.do .lab { color: #A85C3D; }
.dodont .col.dont .lab { color: #6B6B6B; }
.dodont .col .ex {
    font-size: 10pt; line-height: 1.5;
    color: #2A2A2A; margin-top: 8px;
}
.dodont .col .ex strong { color: #0A0A0A; }
.swatch-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 12px; margin: 0.2in 0;
}
.swatch {
    border: 1px solid #d4d2cc;
    page-break-inside: avoid;
}
.swatch .color {
    height: 1.2in; display: block;
}
.swatch .meta { padding: 10px 12px; background: #fafaf8; }
.swatch .name { font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.1em; font-weight: 600; color: #0A0A0A; }
.swatch .hex { font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; color: #6B6B6B; margin-top: 4px; }
.swatch .use { font-size: 8.5pt; color: #6B6B6B; margin-top: 6px; line-height: 1.4; }
.type-spec {
    border: 1px solid #d4d2cc; padding: 24px 28px;
    margin: 0.12in 0; page-break-inside: avoid;
}
.type-spec .role {
    font-family: 'JetBrains Mono', monospace; font-size: 9.5pt;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: #A85C3D; margin-bottom: 6px; font-weight: 600;
}
.type-spec .name {
    font-family: 'Cormorant Garamond', serif; font-size: 16pt;
    margin-bottom: 4px;
}
.type-spec .usage { font-size: 9.5pt; color: #6B6B6B; margin-bottom: 18px; line-height: 1.5; }
.type-spec .sample-display {
    font-family: 'Cormorant Garamond', serif;
    font-size: 38pt; line-height: 1.05;
    letter-spacing: -0.015em; color: #0A0A0A;
    margin: 10px 0;
}
.type-spec .sample-body {
    font-family: 'Inter', sans-serif; font-size: 11pt;
    line-height: 1.55; color: #2A2A2A;
    margin: 10px 0; max-width: 5in;
}
.type-spec .sample-mono {
    font-family: 'JetBrains Mono', monospace; font-size: 10pt;
    letter-spacing: 0.05em; color: #0A0A0A;
}
.pitch-card {
    border-left: 4px solid #A85C3D; background: #fafaf8;
    padding: 22px 26px; margin: 0.15in 0;
    page-break-inside: avoid;
}
.pitch-card .timer {
    font-family: 'JetBrains Mono', monospace; font-size: 9.5pt;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: #A85C3D; margin-bottom: 12px; font-weight: 600;
}
.pitch-card .pitch {
    font-family: 'Inter', sans-serif; font-size: 11pt;
    line-height: 1.6; color: #0A0A0A;
}
.pitch-card .pitch em { color: #8B6F47; font-style: italic; }
.tagline-grid {
    display: grid; grid-template-columns: repeat(2, 1fr);
    gap: 12px; margin: 0.15in 0;
}
.tagline {
    border: 1px solid #d4d2cc;
    padding: 24px;
}
.tagline .text {
    font-family: 'Cormorant Garamond', serif;
    font-size: 18pt; font-weight: 500;
    line-height: 1.2; letter-spacing: -0.01em;
    color: #0A0A0A; margin-bottom: 14px;
}
.tagline .text em { color: #A85C3D; font-style: italic; }
.tagline .when {
    font-family: 'JetBrains Mono', monospace; font-size: 9pt;
    letter-spacing: 0.12em; color: #6B6B6B;
    text-transform: uppercase;
}
.values-grid {
    margin: 0.15in 0;
}
.value-row {
    display: grid; grid-template-columns: 90px 1fr;
    gap: 24px; padding: 22px 0;
    border-bottom: 1px solid #e6e4dd;
    page-break-inside: avoid;
}
.value-row:last-child { border-bottom: 0; }
.value-row .num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 36pt; font-weight: 300;
    color: #A85C3D; line-height: 1;
}
.value-row .val .name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 18pt; font-weight: 500;
    margin-bottom: 8px; letter-spacing: -0.01em;
}
.value-row .val .desc {
    font-size: 10pt; color: #2A2A2A; line-height: 1.6;
    margin-bottom: 8px; max-width: 5.5in;
}
.value-row .val .manifests {
    font-size: 9pt; color: #6B6B6B; font-style: italic;
    line-height: 1.5;
}
"""


def html_body():
    return r"""
<!-- COVER -->
<div class="cover">
    <div class="cover-mark">Preface</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">Brand Guide<br/><span style="font-style: italic; font-weight: 300;">v1</span></h1>
    <div class="cover-subtitle">Mission. Voice. Visual identity. Everything that makes Preface sound like Preface — and not like another travel agency.</div>
    <div class="cover-meta">
        <div>
            <span class="label">Companion to</span>
            <span class="value">Business Plan v2 + Playbook</span>
        </div>
        <div>
            <span class="label">Use for</span>
            <span class="value">Voice calibration, design, copy</span>
        </div>
        <div>
            <span class="label">Lock date</span>
            <span class="value">M3 (then quarterly review)</span>
        </div>
    </div>
</div>

<!-- TOC -->
<div class="toc">
    <h1><span class="num">Contents</span>Table of Contents</h1>
    <div class="toc-entry"><span class="num">01</span><span class="title">The Brief — What Preface Is, in 60 Seconds</span></div>
    <div class="toc-entry"><span class="num">02</span><span class="title">Mission, Vision, &amp; What We Believe</span></div>
    <div class="toc-entry"><span class="num">03</span><span class="title">The Five Values (Non-Negotiable)</span></div>
    <div class="toc-entry"><span class="num">04</span><span class="title">Brand Personality</span></div>
    <div class="toc-entry"><span class="num">05</span><span class="title">The Voice — Principles &amp; Profile</span></div>
    <div class="toc-entry"><span class="num">06</span><span class="title">Voice Do's &amp; Don'ts (50 Examples)</span></div>
    <div class="toc-entry"><span class="num">07</span><span class="title">Positioning Statement</span></div>
    <div class="toc-entry"><span class="num">08</span><span class="title">Elevator Pitches (10s / 30s / 120s)</span></div>
    <div class="toc-entry"><span class="num">09</span><span class="title">Taglines &amp; Headline Library</span></div>
    <div class="toc-entry"><span class="num">10</span><span class="title">Visual Identity — Palette</span></div>
    <div class="toc-entry"><span class="num">11</span><span class="title">Visual Identity — Typography</span></div>
    <div class="toc-entry"><span class="num">12</span><span class="title">Visual Identity — Layout &amp; Photography Principles</span></div>
    <div class="toc-entry"><span class="num">13</span><span class="title">Brand Application Examples</span></div>
    <div class="toc-entry"><span class="num">14</span><span class="title">Reference Brands &amp; Anti-References</span></div>
</section>
</div>

<!-- 01 THE BRIEF -->
<section>
<h1><span class="num">Section 01</span>The Brief — What Preface Is, in 60 Seconds</h1>

<div class="manifesto-page">
    <div class="eyebrow">— The 60-second read</div>
    <div class="statement">Preface is a Toronto-based travel-advisor practice for under-40s who travel often, spend well, and have figured out that <em>Expedia is leaving thousands of dollars on the table</em> &mdash; in upgrades, breakfast, hotel credits, and the kind of human help you can't outsource to a chatbot. We book what we've slept in. We have opinions, and we share them. We charge what the hotel pays us, which means the better trip costs you nothing extra. <em>That's the entire pitch.</em></div>
</div>

<h2>The Reductive Version (For When You Forget)</h2>
<table>
<tbody>
<tr><td><strong>Who</strong></td><td>A modern travel advisor for under-40 professionals + their families</td></tr>
<tr><td><strong>Where</strong></td><td>Toronto-based, serving Canada-wide + US</td></tr>
<tr><td><strong>What we sell</strong></td><td>Hotel + resort + flight bookings with consortium amenities (upgrades, breakfast, credits) layered on top, at zero markup</td></tr>
<tr><td><strong>How we differ</strong></td><td>Lived expertise (20+ all-inclusives), opinions you can quote, a brand that doesn't sound like 1996</td></tr>
<tr><td><strong>Specialty edge</strong></td><td>All-inclusives (visible credibility, not the brand identity)</td></tr>
<tr><td><strong>Anti-positioning</strong></td><td>Not your parents' travel agent. Not a luxury concierge club. Not a points-hacking website. Not an OTA.</td></tr>
</tbody>
</table>
</section>

<!-- 02 MISSION VISION -->
<section>
<h1><span class="num">Section 02</span>Mission, Vision, &amp; What We Believe</h1>

<h2>Mission</h2>
<div class="manifesto-page">
    <div class="eyebrow">— Why Preface exists</div>
    <div class="statement">To give the under-40 generation the kind of travel experience their parents' generation had access to &mdash; <em>updated for how they actually book, communicate, and trust.</em></div>
</div>

<p>What this means in practice:</p>
<ul>
<li>Make the travel-advisor relationship something a 30-year-old recommends to their friend without irony</li>
<li>Strip out the gatekeeping ("members only," "$50K minimum") that made advisors feel inaccessible</li>
<li>Replace brochure language with honest, opinionated guidance</li>
<li>Bring the consortium-amenity economics (upgrades, credits, breakfast) to people who didn't know they qualified</li>
</ul>

<h2>Vision (Y5)</h2>
<div class="manifesto-page">
    <div class="eyebrow">— Where we're going</div>
    <div class="statement">By 2030, Preface is the default travel advisor for affluent millennial Toronto. When someone in our demographic is planning a honeymoon, a milestone family trip, or onboarding their business travel, our name comes up <em>without anyone needing to explain what a travel advisor is.</em></div>
</div>

<p>Concrete vision metrics by Y5:</p>
<ul>
<li>3,000+ active clients (booked at least one trip with us)</li>
<li>50K newsletter subs, 100K combined social following</li>
<li>20+ active business-travel accounts</li>
<li>5&ndash;8 sub-advisors operating under the Preface brand</li>
<li>Name-recognition in the Toronto under-40 affluent segment &mdash; you say "Preface" and they say "the travel agency, right?"</li>
</ul>

<h2>What We Believe (Manifesto)</h2>
<p>The seven beliefs that everything else flows from:</p>

<ol>
<li><strong>Travel advisors aren't dead.</strong> The old ones are just hard to find under 60. The industry needed a brand that didn't make under-40s feel like they wandered into the wrong store.</li>

<li><strong>Same price. Better arrival.</strong> The hotel pays our commission. The rate is identical to Booking.com. The difference is what's waiting in your room. Everyone who books direct is leaving the same dollars on the table; we just decided to pick them up.</li>

<li><strong>Lived experience &gt; google-able expertise.</strong> You can't write a useful review of a resort you've never visited. We sleep where we sell. When we don't know a property, we say so.</li>

<li><strong>Opinions, not brochures.</strong> The industry got addicted to vague aspirational language ("indulge in unparalleled luxury"). We write in normal sentences. We rank things. We tell you Sandals is mid and explain why.</li>

<li><strong>The relationship is the product.</strong> One trip is the start. Ten years of trips is the actual business. We're the advisor you stay with from honeymoon to babymoon to milestone family pilgrimage.</li>

<li><strong>The hotel is half the trip.</strong> The other half is the human in the loop &mdash; the WhatsApp message at 11pm when a flight gets cancelled. That part isn't on Booking.com's product roadmap.</li>

<li><strong>No minimum. No membership. No gatekeeping.</strong> A $3,000 bach weekend and a $50,000 family milestone get the same care. Our economics work either way.</li>
</ol>
</section>

<!-- 03 VALUES -->
<section>
<h1><span class="num">Section 03</span>The Five Values (Non-Negotiable)</h1>
<p class="section-intro">Every operating decision &mdash; what to write, who to hire, when to say no &mdash; should map to one of these five.</p>

<div class="values-grid">
    <div class="value-row">
        <div class="num">01</div>
        <div class="val">
            <div class="name">Honesty over polish.</div>
            <div class="desc">If a resort has a problem (sargassum, loud DJs, mediocre food), we say so. If a client's shortlist is wrong for their priorities, we tell them &mdash; even if it costs us the booking. Trust accrues over time and is the entire long-term moat.</div>
            <div class="manifests"><strong>Manifests as:</strong> hot takes that name names; "I wouldn't recommend that property" being a normal sentence; redirecting a client to TTAND/Sunwing if their budget can't support Privé economics.</div>
        </div>
    </div>

    <div class="value-row">
        <div class="num">02</div>
        <div class="val">
            <div class="name">Receipts over promises.</div>
            <div class="desc">We show real numbers. Real upgrade values. Real client outcomes (anonymized). Real properties we've stayed at. Marketing language without proof is a fast way to look like every other agency.</div>
            <div class="manifests"><strong>Manifests as:</strong> the "Receipt" homepage section; carousel posts showing real upgrade math; the 20+ all-inclusives list page with property-by-property takes; never using stock photos for hotels we haven't been to.</div>
        </div>
    </div>

    <div class="value-row">
        <div class="num">03</div>
        <div class="val">
            <div class="name">Specifically opinionated.</div>
            <div class="desc">"Great honeymoon resort" tells you nothing. "Excellence Playa Mujeres if Mexico, Six Senses if Asia, Royal Mansour if North Africa, and never the Maldives in August" is useful. Specificity is the brand.</div>
            <div class="manifests"><strong>Manifests as:</strong> rankings; head-to-head comparisons; calling out specific months / brands / room categories; the "Hot Takes" section of the newsletter.</div>
        </div>
    </div>

    <div class="value-row">
        <div class="num">04</div>
        <div class="val">
            <div class="name">Modern, not formal.</div>
            <div class="desc">We don't write "Dear Mr. Smith." We don't have a contact form titled "Inquiries." We don't use words like "boutique" or "bespoke" unless mocking them. The voice is the friend, not the front-desk clerk.</div>
            <div class="manifests"><strong>Manifests as:</strong> first-name everything; iMessage/WhatsApp as primary channels; calling things "mid" when they're mid; using emoji selectively, not performatively.</div>
        </div>
    </div>

    <div class="value-row">
        <div class="num">05</div>
        <div class="val">
            <div class="name">Inclusive at the entry point.</div>
            <div class="desc">$3K bach weekend gets the same care as $50K family pilgrimage. The economics work because the commission is the commission. We don't gate access by spend &mdash; we let the client self-select up over time.</div>
            <div class="manifests"><strong>Manifests as:</strong> no trip-minimums; pricing transparency (Standard tier free); welcoming first-timers without making them feel like first-timers; never using the word "exclusive" as a virtue.</div>
        </div>
    </div>
</div>
</section>

<!-- 04 PERSONALITY -->
<section>
<h1><span class="num">Section 04</span>Brand Personality</h1>
<p class="section-intro">If Preface were a person, here's who you'd be sitting across from.</p>

<table>
<thead><tr><th>Trait</th><th>What it means</th><th>What it isn't</th></tr></thead>
<tbody>
<tr><td><strong>Smart friend</strong></td><td>You're not the authority figure. You're the friend who happens to know this stuff cold.</td><td>Not the concierge. Not the expert speaking down. Not the influencer.</td></tr>
<tr><td><strong>Opinionated</strong></td><td>You have takes. You defend them. You're willing to say "I'd skip that."</td><td>Not contrarian for sport. Not edgy without substance. Not refusing to take a side to seem balanced.</td></tr>
<tr><td><strong>Specific</strong></td><td>Property names. Room categories. Dollar amounts. Months. Decade-old context.</td><td>Not vague. Not "amazing." Not "incredible." Not "transformative."</td></tr>
<tr><td><strong>Playful</strong></td><td>Self-aware. Memes if they're good. Sentences that land.</td><td>Not silly. Not Twitter-brain. Not over-emoji-ed. Not trying too hard.</td></tr>
<tr><td><strong>Honest</strong></td><td>Names problems. Tells clients when they're wrong. Won't oversell.</td><td>Not cynical. Not negative. Not blunt to the point of rude.</td></tr>
<tr><td><strong>Modern</strong></td><td>Built for how the under-40 demographic actually books and communicates.</td><td>Not retro-aesthetic. Not deliberately edgy. Not "young" in a pandering way.</td></tr>
<tr><td><strong>Confident, low-status</strong></td><td>You know your stuff. You don't need to remind people that you do.</td><td>Not arrogant. Not chest-pounding. Not trying to project authority you haven't earned.</td></tr>
</tbody>
</table>

<h2>The Two-Sentence Personality Test</h2>
<p>If a piece of content sounds like it could be written by either Mejuri's brand team or Aman's brand team, it's wrong for Preface. We sit between them: <strong>Mejuri-style voice with Aman-level credibility.</strong></p>
<p>If it sounds like it could be written by Sandals or Expedia, it's also wrong. Those brands talk down. We talk across.</p>
</section>

<!-- 05 VOICE PRINCIPLES -->
<section>
<h1><span class="num">Section 05</span>The Voice — Principles &amp; Profile</h1>

<h2>The Six Voice Principles</h2>

<div class="hormozi-rule" style="background: #0A0A0A; color: #FAFAF8; padding: 18px 24px; margin: 0.18in 0; border-left: 4px solid #A85C3D;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #A85C3D; margin-bottom: 8px; font-weight: 600;">Voice Principle 01</div>
<div style="font-weight: 500; line-height: 1.45;"><strong>One sentence at a time.</strong> Short sentences. Stack them. Use a longer one when the rhythm needs it. Then go short again.</div>
</div>

<div class="hormozi-rule" style="background: #0A0A0A; color: #FAFAF8; padding: 18px 24px; margin: 0.18in 0; border-left: 4px solid #A85C3D;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #A85C3D; margin-bottom: 8px; font-weight: 600;">Voice Principle 02</div>
<div style="font-weight: 500; line-height: 1.45;"><strong>Names &gt; categories.</strong> Don't say "a top all-inclusive." Say "Excellence Playa Mujeres." Don't say "a popular destination." Say "Riviera Maya." Specificity is voice.</div>
</div>

<div class="hormozi-rule" style="background: #0A0A0A; color: #FAFAF8; padding: 18px 24px; margin: 0.18in 0; border-left: 4px solid #A85C3D;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #A85C3D; margin-bottom: 8px; font-weight: 600;">Voice Principle 03</div>
<div style="font-weight: 500; line-height: 1.45;"><strong>Numbers &gt; adjectives.</strong> Don't say "great upgrade." Say "$2,400 in cash-value upgrade." Don't say "luxurious." Say "$700/night." Specificity is voice, part 2.</div>
</div>

<div class="hormozi-rule" style="background: #0A0A0A; color: #FAFAF8; padding: 18px 24px; margin: 0.18in 0; border-left: 4px solid #A85C3D;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #A85C3D; margin-bottom: 8px; font-weight: 600;">Voice Principle 04</div>
<div style="font-weight: 500; line-height: 1.45;"><strong>Have a take.</strong> Every piece of content makes a claim. Vague observation is the voice of the brochure. "Tulum is performance art" is the voice of Preface.</div>
</div>

<div class="hormozi-rule" style="background: #0A0A0A; color: #FAFAF8; padding: 18px 24px; margin: 0.18in 0; border-left: 4px solid #A85C3D;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #A85C3D; margin-bottom: 8px; font-weight: 600;">Voice Principle 05</div>
<div style="font-weight: 500; line-height: 1.45;"><strong>The pull-back move.</strong> After a strong claim, give the qualifier. "Sandals is mid &mdash; though their Curaçao property is genuinely good." Confidence + nuance. Not absolute.</div>
</div>

<div class="hormozi-rule" style="background: #0A0A0A; color: #FAFAF8; padding: 18px 24px; margin: 0.18in 0; border-left: 4px solid #A85C3D;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #A85C3D; margin-bottom: 8px; font-weight: 600;">Voice Principle 06</div>
<div style="font-weight: 500; line-height: 1.45;"><strong>Earn the joke.</strong> Humor lands when it follows real value. Lead with the insight, finish with the line. Don't open with "lol" &mdash; close with it.</div>
</div>

<h2>The Voice Profile (For Content VAs)</h2>
<div class="callout">
<p><strong>Tone:</strong> Smart, opinionated, playful, slightly irreverent. Think: a sharp friend who travels well and tells you the truth.</p>
<p><strong>Vocabulary:</strong> Specific, concrete, brand-name-heavy. Numbers over adjectives.</p>
<p><strong>Sentence length:</strong> Short. Punchy. Mixed cadence with occasional longer sentence for rhythm.</p>
<p><strong>Allowed:</strong> Hot takes. Opinions. Self-aware humor. Calling things "mid." Brand callouts. "I think" / "I'd skip." Light emoji. The occasional meme reference (if good).</p>
<p><strong>Forbidden:</strong> "Indulge." "Savor." "Bespoke." "Unparalleled." "Curated." "Wanderlust." "Bucket list" (without self-aware framing). Brochure language. Vague aspirational adjectives. Em-dash sentences that go too long. Performative emoji.</p>
<p><strong>Reference brands (voice):</strong> Mejuri, Away, Glossier, Death Wish Coffee, Liquid Death (selectively).</p>
<p><strong>Anti-reference brands:</strong> Aman, Belmond, Brownell, Virtuoso publications, Travel + Leisure editorial.</p>
</div>
</section>

<!-- 06 DO DONT EXAMPLES -->
<section>
<h1><span class="num">Section 06</span>Voice Do's &amp; Don'ts (50 Examples)</h1>
<p class="section-intro">The fastest way to calibrate the voice. Read these. Internalize the pattern.</p>

<h2>Headlines &amp; Hooks</h2>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"There are 200 all-inclusives in the Caribbean. About a dozen are actually good."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Discover the magic of all-inclusive travel."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"You're spending $8K on a honeymoon. Let's make sure you don't land in a room with a parking-lot view."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Let us craft your perfect honeymoon experience."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Excellence Playa Mujeres &gt; Excellence Punta Cana. I will die on this hill."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Excellence Resorts offer some of the finest Caribbean experiences available today."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Stop logging into Marriott.com. I'll do it."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Streamline your business travel with our comprehensive booking services."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"I've slept in most of these."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Backed by extensive industry expertise."</div>
    </div>
</div>

<h2>Body Copy</h2>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Get Club access or skip. The base room is bait pricing &mdash; the actual product is the Club tier."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Many guests find that upgrading to a Club-level room enhances their stay considerably."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"The hotel pays my commission. Booking direct vs. through me is identical in price &mdash; the difference is what arrives in your room."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Our value-added services come at no incremental cost to clients, with compensation structured through industry-standard partner arrangements."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"If you're flying eleven hours, you should be staying at least eight nights. Jet lag is not a souvenir."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"For long-haul international travel, extended stays are recommended to fully experience the destination."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Sargassum season is real. Riviera Maya from June through September: the beaches are covered. Hotels can clean. They cannot stop the smell. If you must travel summer, go Caribbean (Turks, Anguilla, BVI) or Pacific Mexico."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Summer travel in some Mexican destinations can be impacted by seasonal seaweed conditions. We recommend consulting current beach reports prior to booking."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Royalton CHIC is fine if you're 22. The music will end you otherwise."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Royalton CHIC offers a vibrant, upbeat atmosphere suited to younger travelers."</div>
    </div>
</div>

<h2>Calls to Action</h2>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Book a 20-min call. No pitch, no pressure. If I'm not the right fit, I'll tell you."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Schedule your complimentary consultation today!"</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Newsletter at preface.travel. Travel takes, every other Friday. No spam."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Sign up for our exclusive insider newsletter and elevate your travel game!"</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Want to grab a coffee? Or drop a date in my Calendly: [link]."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Please use the form below to reach out and one of our representatives will be in touch."</div>
    </div>
</div>

<h2>Client-Facing Email &amp; Message</h2>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Quick note &mdash; the room you're looking at is sold out at the Excellence rate. Two options: bump to Excellence Club for $400 more (you'd get butler service + private pool + premium liquor), or shift dates one week earlier. Want to talk it through?"</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Dear [Client], Unfortunately your requested room category is no longer available. Please review the attached alternative options and let us know how you would like to proceed. Best regards."</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Welcome back! Hope it was as good as the photos. Two quick things: a) any chance you'd share a 2-line review on Google? b) if you loved the trip, sending one friend my way is the highest compliment."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Welcome back from your journey! We hope you had an unforgettable experience. We would love to hear your feedback through our Google review platform, and please remember to refer Preface to friends and family!"</div>
    </div>
</div>

<h2>Social Captions</h2>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Two rooms. Same hotel. Same price. <br/><br/>One you book on Booking.com. One you book through me. <br/><br/>The difference is $1,200 in upgrades. <br/><br/>This is the whole pitch."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"Did you know you can get amazing perks when booking with a travel advisor? Stop overpaying ✈️ DM us today! ⭐⭐⭐⭐⭐"</div>
    </div>
</div>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Hot take: most all-inclusives are mid. <br/><br/>I've been to 20+. About 6 I'd actually recommend. <br/><br/>The full list is in the newsletter."</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"All-inclusives are perfect for any traveler! From honeymooners to families, there's something for everyone! Comment below your favorite 🌴"</div>
    </div>
</div>

<h2>Newsletter Subject Lines</h2>

<div class="dodont">
    <div class="col do">
        <div class="lab">Do</div>
        <div class="ex">"Excellence vs. Excellence (the verdict)"<br/>"3 hotels I'd recommend in Tokyo. None are the Aman."<br/>"Sandals is mid. Here's what isn't."<br/>"Why your honeymoon shortlist is wrong"</div>
    </div>
    <div class="col dont">
        <div class="lab">Don't</div>
        <div class="ex">"This Week's Travel Tips!"<br/>"Newsletter — Issue 12"<br/>"Discover Amazing Resorts ✨"<br/>"Don't Miss Out On These Deals!"</div>
    </div>
</div>
</section>

<!-- 07 POSITIONING -->
<section>
<h1><span class="num">Section 07</span>Positioning Statement</h1>

<h2>The Official Positioning</h2>
<div class="manifesto-page">
    <div class="eyebrow">— The positioning, locked</div>
    <div class="statement">For under-40 professionals and their families who travel often and want to travel well, <em>Preface is the Toronto travel-advisor practice</em> that brings consortium-level perks and lived expertise to a relationship that doesn't require minimums or gatekeeping. <em>Where most travel advisors plan trips they've never taken, we book what we've slept in.</em></div>
</div>

<h2>The Triangle (Position Map)</h2>
<p>Three axes Preface positions against:</p>
<ol>
<li><strong>vs. OTAs (Booking.com / Expedia):</strong> Same price, more arrival value (upgrades + breakfast + credits) + a human in the loop when things break.</li>
<li><strong>vs. Old-school travel advisors (Brownell, ProTravel, traditional Virtuoso houses):</strong> Modern, accessible, opinionated, no minimums. Same consortium access via Fora's membership.</li>
<li><strong>vs. Modern competitors (other Fora advisors, Travel Leaders, Cruise Planners):</strong> Lived expertise (20+ all-inclusives), distinctive voice, multi-segment practice (leisure + business + group), Toronto-specific market focus.</li>
</ol>

<h2>The One-Line Differentiator</h2>
<p><strong>"We book what we've slept in."</strong></p>
<p>Six words. Replaceable in headlines and subject lines. Anti-position against every advisor who's never been to the property they're selling. Built-in receipt-style trust.</p>
</section>

<!-- 08 ELEVATOR PITCHES -->
<section>
<h1><span class="num">Section 08</span>Elevator Pitches</h1>
<p class="section-intro">Three lengths. One for every conversation moment. Internalize all three.</p>

<div class="pitch-card">
<div class="timer">— 10 seconds (for a stranger at a party)</div>
<div class="pitch">"I'm a travel advisor &mdash; mostly honeymoons, family trips, and business travel for execs. The hotel pays the commission, so it costs nothing more than Booking.com but you actually get upgrades, breakfast, and a human if things go sideways."</div>
</div>

<div class="pitch-card">
<div class="timer">— 30 seconds (for a referral conversation)</div>
<div class="pitch">"I built Preface &mdash; a travel-advisor practice for under-40s in Toronto. I work with Fora (Virtuoso member + Four Seasons + Hyatt Privé preferred partner), so when I book your honeymoon or your family week at an Excellence resort, the hotel layers on a room upgrade, daily breakfast, and a $100&ndash;200 hotel credit &mdash; <em>at the same rate you'd pay direct on Booking.com.</em>

The specialty: all-inclusives. I've stayed at 20+ properties. I also handle business travel for founders and execs &mdash; basically replacing the time you spend on Marriott.com with a 60-second text to me. Want a 20-min call to walk through your travel pattern?"</div>
</div>

<div class="pitch-card">
<div class="timer">— 120 seconds (for an intro call)</div>
<div class="pitch">"Quick context: I'm a Toronto-based travel advisor, recently launched after [X] years in B2B sales. The thesis: there's a whole generation of people now hitting their peak travel years &mdash; honeymoons, families, business travel &mdash; who never had a relationship with a travel advisor because the industry never built one for them. Their parents had advisors. They have Expedia.

What I do: I'm an independent advisor with Fora, which is the modern host agency. Through Fora's consortia memberships (Virtuoso, Four Seasons Preferred Partner, Belmond Bellini Club, Rosewood Elite, Hyatt Privé &mdash; including the Hyatt Inclusive Collection with Secrets and Dreams), I can book your trip at the same rate as Booking.com but with amenities layered on: room upgrades, daily breakfast, $100&ndash;200 in resort credits, early/late check-in/out, the works. None of that costs you extra. The hotel funds it through their advisor-marketing budget.

My specialty edge: all-inclusives. I've personally stayed at 20+ properties across the Caribbean and Mexico &mdash; Excellence, Le Blanc, Zoetry, Sandals, the Hyatt Inclusive Collection, etc. So when I'm telling you why Excellence Playa Mujeres beats Punta Cana, I'm not reading a brochure.

I also do business travel for founders and execs &mdash; that's a different lane: high frequency, lower per-trip margin, hotels through Privé and STARS and Hilton for Luxury, basically replacing the time you waste on Marriott.com.

The fee model is mostly $0 to clients &mdash; the hotel pays my commission. For complex trips (multi-stop honeymoons, milestone group trips) I charge a planning fee that ranges $300&ndash;2,500 depending on complexity.

The reason I'm telling you all this: the best clients in this business come from referrals. If anyone in your circle is planning a honeymoon, family trip, or has 25+ business travel nights a year, I'd love an introduction. <em>And if you want to test the model with your own trip, that's even better.</em>"</div>
</div>
</section>

<!-- 09 TAGLINES -->
<section>
<h1><span class="num">Section 09</span>Taglines &amp; Headline Library</h1>
<p class="section-intro">Approved taglines, organized by use case. Use them. Don't write new ones unless you've used these and they're not working.</p>

<h2>Primary Tagline (Master)</h2>
<div class="tagline" style="grid-column: 1 / -1; margin: 0.15in 0;">
    <div class="text">Travel for people who'd rather not <em>Expedia it.</em></div>
    <div class="when">USE: Homepage hero subtitle. Email signature. About bio.</div>
</div>

<h2>Secondary Taglines (Channel-Specific)</h2>

<div class="tagline-grid">
    <div class="tagline">
        <div class="text">We book what we've <em>slept in.</em></div>
        <div class="when">USE: All-Inclusives page. Receipts content. The "credentials" line everywhere.</div>
    </div>
    <div class="tagline">
        <div class="text"><em>Same price.</em> Better arrival.</div>
        <div class="when">USE: Math-comparison contexts. Cold email subject lines. Above-the-fold.</div>
    </div>
    <div class="tagline">
        <div class="text">Receipts, <em>not brochures.</em></div>
        <div class="when">USE: Newsletter signup CTA. Content marketing. About page.</div>
    </div>
    <div class="tagline">
        <div class="text">The travel advisor your <em>parents' advisor wouldn't be.</em></div>
        <div class="when">USE: Brand-positioning contexts. PR. Industry profiles.</div>
    </div>
    <div class="tagline">
        <div class="text"><em>20+ all-inclusives stayed.</em> Honest takes inside.</div>
        <div class="when">USE: All-Inclusives content. SEO meta-descriptions. IG bio.</div>
    </div>
    <div class="tagline">
        <div class="text">Stop logging into <em>Marriott.com.</em></div>
        <div class="when">USE: Business Travel page hero. LinkedIn for BT funnel.</div>
    </div>
</div>

<h2>The Headline Library (15 Reusable Patterns)</h2>
<table>
<thead><tr><th>Pattern</th><th>Example</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>[Number] [Things]. [Verdict].</td><td>"200 all-inclusives. About a dozen are good."</td><td>Hero / SEO</td></tr>
<tr><td>You're [doing X]. Let's [not do Y].</td><td>"You're spending $8K. Let's not land in a parking-lot view."</td><td>Hero / Email</td></tr>
<tr><td>[Action]. <em>[Italic verdict].</em></td><td>"All-inclusives, ranked. (Sort of.)"</td><td>Page title</td></tr>
<tr><td>[Strong claim]. <em>I'll die on this hill.</em></td><td>"Excellence Playa Mujeres &gt; Punta Cana. I'll die on this hill."</td><td>Hot take post</td></tr>
<tr><td>Stop [bad behavior]. I'll [do it for you].</td><td>"Stop logging into Marriott.com. I'll do it."</td><td>BT hero</td></tr>
<tr><td>[Brand X] is mid. [Better alternative].</td><td>"Sandals is mid. Excellence isn't."</td><td>Newsletter</td></tr>
<tr><td>[Question]. <em>[Italic answer].</em></td><td>"Why is your honeymoon shortlist wrong? <em>Three reasons.</em>"</td><td>Carousel hook</td></tr>
<tr><td>We [do the thing]. Most [don't].</td><td>"We book what we've slept in. Most advisors don't."</td><td>Brand positioning</td></tr>
<tr><td>Same [X]. Better [Y].</td><td>"Same price. Better arrival."</td><td>Tagline / CTA</td></tr>
<tr><td>Things that [are wrong]. Things that [are right].</td><td>"Things travel agents lie about. Things they should tell you."</td><td>Carousel</td></tr>
<tr><td>The [counter-intuitive truth] about [familiar thing].</td><td>"The truth about Sandals' rate parity."</td><td>Newsletter</td></tr>
<tr><td>If [condition], you should [do thing].</td><td>"If you're flying 11 hours, you should stay 8 nights."</td><td>Tip post</td></tr>
<tr><td>Why [specific brand] still [does the thing].</td><td>"Why Le Blanc still does breakfast better than every other resort."</td><td>SEO</td></tr>
<tr><td>I [did the thing]. Here's what [I found].</td><td>"I stayed at Royalton CHIC. Here's the verdict."</td><td>Review</td></tr>
<tr><td>The honest [adjective] [thing].</td><td>"The honest Maldives ranking."</td><td>List post</td></tr>
</tbody>
</table>
</section>

<!-- 10 PALETTE -->
<section>
<h1><span class="num">Section 10</span>Visual Identity — Palette</h1>
<p class="section-intro">Cool modern minimal base with one warm accent. Restrained on purpose &mdash; the writing is loud, the visuals are not.</p>

<h2>Core Palette</h2>
<div class="swatch-grid">
    <div class="swatch">
        <div class="color" style="background: #FAFAF8;"></div>
        <div class="meta">
            <div class="name">BG WARM</div>
            <div class="hex">#FAFAF8</div>
            <div class="use">Primary background. Off-white, never pure.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #F2F0EB;"></div>
        <div class="meta">
            <div class="name">BG ALT</div>
            <div class="hex">#F2F0EB</div>
            <div class="use">Section backgrounds, cards. Slight warm shift.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #0A0A0A;"></div>
        <div class="meta">
            <div class="name">INK</div>
            <div class="hex">#0A0A0A</div>
            <div class="use">Primary text. Buttons. Dark sections.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #2A2A2A;"></div>
        <div class="meta">
            <div class="name">INK SOFT</div>
            <div class="hex">#2A2A2A</div>
            <div class="use">Body text on white bg.</div>
        </div>
    </div>
</div>

<h2>Greys (Text Hierarchy)</h2>
<div class="swatch-grid">
    <div class="swatch">
        <div class="color" style="background: #6B6B6B;"></div>
        <div class="meta">
            <div class="name">GREY MID</div>
            <div class="hex">#6B6B6B</div>
            <div class="use">Secondary text, descriptions.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #B8B6B0;"></div>
        <div class="meta">
            <div class="name">GREY LIGHT</div>
            <div class="hex">#B8B6B0</div>
            <div class="use">Captions, fine print, dark-mode body text.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #E5E3DD;"></div>
        <div class="meta">
            <div class="name">LINE</div>
            <div class="hex">#E5E3DD</div>
            <div class="use">Borders, dividers, table lines.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #FFFFFF;"></div>
        <div class="meta">
            <div class="name">WHITE</div>
            <div class="hex">#FFFFFF</div>
            <div class="use">Use sparingly. Default to #FAFAF8.</div>
        </div>
    </div>
</div>

<h2>The Accent (Use Sparingly)</h2>
<div class="swatch-grid">
    <div class="swatch">
        <div class="color" style="background: #A85C3D;"></div>
        <div class="meta">
            <div class="name">COGNAC</div>
            <div class="hex">#A85C3D</div>
            <div class="use">Primary accent. Italics, key stats, links, accent CTAs.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #8E4A2F;"></div>
        <div class="meta">
            <div class="name">COGNAC DARK</div>
            <div class="hex">#8E4A2F</div>
            <div class="use">Hover states. Secondary accent.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #C8956D;"></div>
        <div class="meta">
            <div class="name">COGNAC LIGHT</div>
            <div class="hex">#C8956D</div>
            <div class="use">Tints, backgrounds for accent-on-accent. Rare.</div>
        </div>
    </div>
    <div class="swatch">
        <div class="color" style="background: #8a3a3a;"></div>
        <div class="meta">
            <div class="name">VERDICT NO</div>
            <div class="hex">#8A3A3A</div>
            <div class="use">Negative verdicts. "Not Recommend" tags. Use rarely.</div>
        </div>
    </div>
</div>

<h2>Palette Usage Rules</h2>
<ol>
<li><strong>80/15/5:</strong> 80% off-white + ink. 15% greys + lines. 5% cognac accent. Never invert these ratios.</li>
<li><strong>Cognac is italic, key stats, accent CTAs.</strong> Not headlines. Not buttons (except inverted on dark sections).</li>
<li><strong>Pure black (#000) is forbidden.</strong> Always #0A0A0A. Adds warmth.</li>
<li><strong>Pure white (#FFF) is forbidden too.</strong> Always #FAFAF8. Off-white reads less clinical.</li>
<li><strong>Don't introduce new accent colors</strong> without explicit brand approval. The cognac is the brand.</li>
</ol>
</section>

<!-- 11 TYPOGRAPHY -->
<section>
<h1><span class="num">Section 11</span>Visual Identity — Typography</h1>

<div class="type-spec">
    <div class="role">— Display / Headings</div>
    <div class="name">Fraunces</div>
    <div class="usage">Weights: 300 (light), 400 (regular), 500 (medium). Italic available for accent. Use Fraunces 400 for h1/h2, Fraunces 300 italic for accent phrases. Letter-spacing: -0.015 to -0.025em depending on size.</div>
    <div class="sample-display">All-inclusives, <em style="font-style: italic; color: #A85C3D; font-weight: 300;">ranked.</em></div>
</div>

<div class="type-spec">
    <div class="role">— Body / UI</div>
    <div class="name">Inter</div>
    <div class="usage">Weights: 400 (regular), 500 (medium), 600 (semibold). Use 400 for body text, 500 for navigation/buttons, 600 for emphasized inline. Letter-spacing: 0 to -0.005em.</div>
    <div class="sample-body">The hotel pays my commission. Same rate as Booking.com — except you arrive to upgrades, breakfast, hotel credits, and the email address of a human who's actually awake when something breaks.</div>
</div>

<div class="type-spec">
    <div class="role">— Mono / Detail / Eyebrows</div>
    <div class="name">JetBrains Mono</div>
    <div class="usage">Weight 400&ndash;600. Used for: section eyebrows, label tags, table headers, numeric details, "specs" feel. Letter-spacing: 0.1 to 0.2em uppercase.</div>
    <div class="sample-mono">— SECTION 01 / THE BRIEF · TICO #XXXXXXX · 20+ ALL-INCLUSIVES STAYED</div>
</div>

<h2>Type Scale (Web)</h2>
<table>
<thead><tr><th>Role</th><th>Size</th><th>Family</th><th>Weight</th><th>Tracking</th></tr></thead>
<tbody>
<tr><td>Hero H1</td><td>56&ndash;88px</td><td>Fraunces</td><td>400</td><td>-0.025em</td></tr>
<tr><td>Section H2</td><td>40&ndash;56px</td><td>Fraunces</td><td>400</td><td>-0.020em</td></tr>
<tr><td>H3 / card title</td><td>24&ndash;32px</td><td>Fraunces</td><td>400&ndash;500</td><td>-0.015em</td></tr>
<tr><td>H4 / label</td><td>16&ndash;22px</td><td>Fraunces or Inter</td><td>500</td><td>-0.010em</td></tr>
<tr><td>Body</td><td>15&ndash;17px</td><td>Inter</td><td>400</td><td>0em</td></tr>
<tr><td>Small / caption</td><td>13&ndash;14px</td><td>Inter</td><td>400</td><td>0em</td></tr>
<tr><td>Eyebrow / label</td><td>10&ndash;12px</td><td>JetBrains Mono</td><td>500</td><td>+0.15&ndash;0.20em uppercase</td></tr>
<tr><td>Big stat (display)</td><td>72&ndash;156px</td><td>Fraunces</td><td>300</td><td>-0.04em</td></tr>
</tbody>
</table>

<h2>Type Rules</h2>
<ol>
<li><strong>Italics belong to Fraunces.</strong> Use italic Fraunces for accent phrases in headlines. Color them cognac.</li>
<li><strong>Don't bold body text.</strong> Use Inter 500 (medium) for emphasized inline; reserve 600+ for navigation, buttons, table headers.</li>
<li><strong>Mono is for labels, not body.</strong> No paragraphs in mono. Eyebrows, tags, table headers, numeric stats only.</li>
<li><strong>Line height:</strong> Headings 1.05&ndash;1.15. Body 1.5&ndash;1.65.</li>
<li><strong>Never mix more than 3 typefaces on a page.</strong> Fraunces + Inter + JetBrains Mono is the full set.</li>
</ol>
</section>

<!-- 12 LAYOUT PRINCIPLES -->
<section>
<h1><span class="num">Section 12</span>Visual Identity — Layout &amp; Photography Principles</h1>

<h2>Layout Principles</h2>
<ol>
<li><strong>Generous white space.</strong> Sections breathe at 80&ndash;120px vertical padding. Tight layouts feel discount; spacious layouts feel premium.</li>
<li><strong>Editorial grid, not Bootstrap grid.</strong> Asymmetric column ratios (1.6:1, 1.2:1) are the default. Equal columns (1:1) only when content is genuinely equivalent.</li>
<li><strong>Hairline rules instead of cards.</strong> Use 1px borders + generous padding rather than drop-shadowed cards. Less Shopify, more Cereal Magazine.</li>
<li><strong>Numbers should be massive.</strong> 20+ all-inclusives stayed isn't "20+" at 14px. It's 80&ndash;156px Fraunces 300.</li>
<li><strong>Capital details, not capital sentences.</strong> JetBrains Mono in CAPS for eyebrows and labels. Never use CAPS for full sentences or paragraphs.</li>
<li><strong>One accent color per section.</strong> Cognac for italic or stat. Not for headings, not for backgrounds, not for body text.</li>
<li><strong>Page transitions through dark sections.</strong> Break visual monotony with one dark (#0A0A0A) section per page. Usually the CTA or a specialty showcase.</li>
</ol>

<h2>Photography Principles</h2>
<ol>
<li><strong>Real over stock.</strong> Photos of hotels we've actually visited. Photos of trips we've actually planned (with permission). Client photos welcomed (anonymized).</li>
<li><strong>Available light over staged.</strong> Natural light. Slightly cool color grading. Avoid the over-saturated influencer-resort look.</li>
<li><strong>Architecture and interior over food.</strong> Show the room. Show the property. Show the lobby. Food shots are restaurant-blog energy; rooms and interiors are travel-advisor energy.</li>
<li><strong>People sparingly.</strong> When people appear, they're: real clients (permission), the founder, or in genuine candid moments. Not stock travelers gazing at sunsets.</li>
<li><strong>Aspect ratios:</strong> 4:5 for IG primary, 16:9 for hero, 1:1 for grid posts, 9:16 for stories/reels.</li>
</ol>

<h2>What Visual Identity Looks Like (Pages)</h2>
<table>
<thead><tr><th>Element</th><th>Visual approach</th></tr></thead>
<tbody>
<tr><td>Hero</td><td>Big Fraunces headline. Generous spacing. One cognac italic accent phrase. CTA button (dark with hover-to-cognac).</td></tr>
<tr><td>Stats / credentials</td><td>Big Fraunces numerals (72&ndash;156px). Mono labels underneath. Hairline dividers between.</td></tr>
<tr><td>Comparison tables</td><td>Black header row. White rows with hairline dividers. Cognac for the "preface" column values.</td></tr>
<tr><td>Receipts / case studies</td><td>Dark card (#0A0A0A). Cognac accent tag. Mono numeric values. Bottom-stamped attribution.</td></tr>
<tr><td>Property listings</td><td>Asymmetric grid. Fraunces names + Mono location label + body take + verdict tag.</td></tr>
<tr><td>Newsletter</td><td>Single column ~600px. Fraunces headline. Inter body. Mono section labels. Cognac accent for italics.</td></tr>
<tr><td>Instagram carousel</td><td>Off-white BG. Black/cognac type. One stat per slide. Editorial layout, never template-y.</td></tr>
<tr><td>Business card / collateral</td><td>Off-white. Single Fraunces brand mark. Mono details. Cognac dot accent.</td></tr>
</tbody>
</table>
</section>

<!-- 13 APPLICATIONS -->
<section>
<h1><span class="num">Section 13</span>Brand Application Examples</h1>
<p class="section-intro">How the brand shows up across surfaces. Use these as templates.</p>

<h2>Email Signature</h2>
<div class="callout">
<p style="font-family: 'Inter', sans-serif; font-size: 11pt; color: #0A0A0A;">[Your Name]</p>
<p style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.1em; color: #6B6B6B;">PREFACE · INDEPENDENT TRAVEL ADVISOR · TICO #XXXXXXX</p>
<p style="font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; letter-spacing: 0.1em; color: #A85C3D;">20+ ALL-INCLUSIVES STAYED · FORA · VIRTUOSO · HYATT PRIVÉ</p>
<p style="font-family: 'Inter', sans-serif; font-size: 10pt; color: #6B6B6B;">preface.travel · @preface.travel</p>
</div>

<h2>Newsletter Header</h2>
<div class="callout">
<p style="font-family: 'Cormorant Garamond', serif; font-size: 24pt; font-weight: 400; color: #0A0A0A; margin-bottom: 4px;">Preface<span style="color: #A85C3D;">.</span></p>
<p style="font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #6B6B6B;">ISSUE 08 · MAY 21, 2026 · TRAVEL TAKES, EVERY OTHER FRIDAY</p>
</div>

<h2>Cold Email Signature</h2>
<p>Slimmer. Mono-only. No graphics. Improves deliverability.</p>
<div class="callout">
<p style="font-family: 'JetBrains Mono', monospace; font-size: 9.5pt; color: #0A0A0A;">— [First Name]<br/>Preface · Independent Travel Advisor<br/>preface.travel<br/>TICO #XXXXXXX | Fora Travel Inc.</p>
</div>

<h2>Instagram Bio</h2>
<div class="callout">
<p style="font-family: 'Inter', sans-serif; font-size: 11pt; color: #0A0A0A; line-height: 1.5;">
Preface 🌴<br/>
Travel advisor (Toronto)<br/>
20+ all-inclusives stayed · honest takes<br/>
Free upgrades + perks at same prices as Booking.com<br/>
↓ Newsletter + book a call
</p>
</div>

<h2>LinkedIn Headline</h2>
<div class="callout">
<p style="font-family: 'Inter', sans-serif; font-size: 11pt; color: #0A0A0A;">
Founder, Preface · Travel desk for Toronto founders + sales execs · Hyatt Privé / Marriott STARS preferred · TICO #XXXXXXX
</p>
</div>

<h2>Welcome Email (Sent on first signup)</h2>
<div class="callout">
<p style="font-family: 'Inter', sans-serif; font-size: 11pt; line-height: 1.6; color: #0A0A0A;">
<strong>Hey &mdash;</strong><br/><br/>
Welcome to the newsletter. Travel takes, every other Friday. Three quick things while you're here:<br/><br/>
1. <strong>The math:</strong> the hotel pays my commission. Booking through me costs the same as Booking.com but you get upgrades, breakfast, and a human in the loop. <a href="#" style="color: #A85C3D;">Here's how it works</a>.<br/><br/>
2. <strong>My specialty is all-inclusives.</strong> I've stayed at 20+. <a href="#" style="color: #A85C3D;">Here's the list with my takes</a>.<br/><br/>
3. <strong>If a trip's on the calendar,</strong> book a 20-min call (no pitch, no pressure): <a href="#" style="color: #A85C3D;">[link]</a>.<br/><br/>
&mdash; [Name]<br/>
<em style="color: #A85C3D;">P.S. Reply to this email anytime &mdash; it lands in my inbox, not a help desk.</em>
</p>
</div>
</section>

<!-- 14 REFERENCE BRANDS -->
<section>
<h1><span class="num">Section 14</span>Reference Brands &amp; Anti-References</h1>

<h2>Brands Whose Voice We Borrow From</h2>
<table>
<thead><tr><th>Brand</th><th>What we take</th><th>What we don't</th></tr></thead>
<tbody>
<tr><td><strong>Mejuri</strong></td><td>Modern minimal design, accessible-luxury positioning, smart casual voice for women's lifestyle</td><td>Pure D2C aesthetic; we're more editorial</td></tr>
<tr><td><strong>Away</strong></td><td>Premium-but-approachable, conversational copy on functional products, generous photography</td><td>Their luxury luggage focus &mdash; we're not a product company</td></tr>
<tr><td><strong>Glossier</strong></td><td>Self-aware voice, "talk to your friends" copy, building a brand from a media property</td><td>Beauty-specific cultural references; our demo is broader</td></tr>
<tr><td><strong>Death &amp; Co (cocktail bar / book)</strong></td><td>Editorial design polish + opinionated content + craft authority</td><td>The exclusive, members-only undertone</td></tr>
<tr><td><strong>The Skimm</strong></td><td>Newsletter voice that respects the reader's time; cultural awareness + clear utility</td><td>The political content; we stay in our lane</td></tr>
<tr><td><strong>Liquid Death</strong></td><td>Confidence to have an irreverent brand in a category that's normally serious</td><td>The metal/punk aesthetic — we're more sophisticated than rebellious</td></tr>
</tbody>
</table>

<h2>Brands We Are Explicitly Not</h2>
<table>
<thead><tr><th>Brand</th><th>Why we're not them</th></tr></thead>
<tbody>
<tr><td><strong>Aman / Belmond / Brownell</strong></td><td>Luxury hotel / classical luxury agency. We have the consortium access but not the gatekeeping vibe. They feel "members only." We feel "open."</td></tr>
<tr><td><strong>Expedia / Booking.com / Hotels.com</strong></td><td>OTAs are the antithesis. We're the human, opinionated, advisor-led alternative to algorithmic booking.</td></tr>
<tr><td><strong>Sandals / Beaches (marketing)</strong></td><td>Big TV ads, "Caribbean Magic," sweepstakes energy. We're the agency that books their resorts but writes about them differently.</td></tr>
<tr><td><strong>Travel + Leisure / Conde Nast Traveler</strong></td><td>Editorial polish without specific recommendations. We have takes; they hedge.</td></tr>
<tr><td><strong>Influencer travel agencies</strong></td><td>"Wanderlust" energy. Bucket lists. Affiliate-link aesthetic. We're the opposite.</td></tr>
<tr><td><strong>Old-school Virtuoso houses</strong></td><td>Smart-Dale-Carnegie typography, "discerning traveler" copy, 1990s websites. We have their access, none of their UX.</td></tr>
</tbody>
</table>

<h2>The North Star (Final Reference)</h2>
<p>Imagine Mejuri opened a travel-advisor practice and hired a smart, opinionated founder who happens to have stayed at every all-inclusive in Mexico. That's the shape. <strong>Mejuri-style aesthetics + Aman-level credibility + Death &amp; Co-level opinionation.</strong></p>
<p>If a piece of content doesn't sit somewhere in that triangle, it's wrong for Preface.</p>

<div class="divider">&middot; &middot; &middot;</div>
<p style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 13pt; font-style: italic; color: #4a4a47;">End of Brand Guide v1</p>
<p style="text-align: center; font-size: 9pt; color: #8B6F47;">Lock the brand at M3. Quarterly review.</p>
</section>
"""


def main():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Preface — Brand Guide</title>
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
