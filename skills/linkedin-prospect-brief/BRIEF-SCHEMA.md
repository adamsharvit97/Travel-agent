# Brief schema and analysis guide

## The analyst's stance

Read the profile and activity feed the way a senior salesperson reads it before a call — looking for negative space: what this person clearly doesn't want, the moves that would mark you as part of the noise, and the one moment this week where showing up would feel like good timing instead of selling.

## Discipline rules (non-negotiable)

1. Every claim anchors to the source text. Empty beats invented.
2. Sensitive personal categories (health, religion, politics, sexuality) are excluded from personal signals even if visible.
3. Anti-patterns derive from THIS prospect's content. Each `why` must cite something specific (a post, a phrase, an explicit CTA). If nothing anchors, return fewer — or none.
4. `risk_signals` only with real evidence. No speculation.
5. Outreach drafts obey the seller's voice rules. Objection answers adapt the seller's objection bank.
6. Where the seller profile defines audience types, classify the prospect into one and use that type's pain pattern, tier recommendation, and buying triggers.

## Where anti-patterns come from (six evidence categories)

1. **Direct evidence** — they posted about hating something; that's the anti-pattern.
2. **What everyone else is doing** — a post with 50 comments doesn't need your 51st; find the less-crowded entry point.
3. **Their ICP** — if they sell X, they're not buying X; don't pitch it.
4. **Identity vs. topic** — surface-level reference to something core to their identity reads as a Google check.
5. **Their explicit CTAs** — if they publish a way to reach them (open calendar link, "DM me"), don't invent another.
6. **Community dynamics** — small worlds; parallel outreach to their clients gets back to them.

## Brief JSON schema

Return exactly this object. Empty string/array for anything unsupported by the source.

```json
{
  "name": "", "headline": "", "location": "",
  "snapshot": { "current_role": "", "prior_roles": [], "education": "", "credentials": "", "network": "" },
  "summary": "2-3 sentence read: who this person is and why they matter to the seller",
  "hot_moments": [ { "what": "", "why": "", "use": "how to use it this week" } ],
  "recent_changes": [ "role/employment/announcement changes, dated where visible" ],
  "company": { "name": "", "what_they_do": "", "size": "", "recent_changes": [], "notes": "" },
  "industry_pulse": "what is hot or painful in their sector right now; what it means for the pitch angle",
  "tenure_stability": { "arc": "", "read": "honeymoon / settled / restless / flight-risk", "approach": "" },
  "power_role": { "type": "", "budget_authority": "", "buying_decision": "who decides on this kind of spend", "implication": "" },
  "offer_fit": { "recommendation": "which of the seller's products/tiers", "price": "", "fit": "strong / moderate / weak", "rationale": "", "volume_estimate": "evidence-based usage/need estimate" },
  "need_signals": [ { "signal": "any mention of the pain the seller's offer solves", "source": "", "use": "" } ],
  "stakeholders": [ { "who": "", "role": "EA / co-founder / boss / spouse-as-influencer", "why": "" } ],
  "reach": { "channel": "", "best_time": "", "reply_window": "", "avoid": "" },
  "mirror_language": { "their_words": [], "avoid_words": [], "directive": "" },
  "tone": { "style": "", "formality": "", "directive": "" },
  "influences": [],
  "recent_events": [ { "event": "trips, conferences, milestones (~90 days)", "when": "", "use": "" } ],
  "personal_signals": [],
  "posting_patterns": { "cadence": "", "categories": [], "engagement": "" },
  "risk_signals": [],
  "buying_signals": [ { "signal": "", "timing": "" } ],
  "warm_paths": [ { "path": "mutuals, shared ex-employers, schools, communities", "how_to_ask": "" } ],
  "hooks": [ { "hook": "", "leverage": "ranked best first" } ],
  "objections": [ { "q": "objection in their voice", "a": "seller's answer adapted to this prospect" } ],
  "outreach": [
    { "variant": "A — recommended angle", "channel": "", "subject": "", "body": "", "rationale": "" },
    { "variant": "B — alternate angle", "channel": "", "subject": "", "body": "", "rationale": "" },
    { "variant": "C — personal-thread angle (only after a warm signal)", "channel": "", "subject": "", "body": "", "rationale": "" }
  ],
  "plan": [ { "step": 1, "action": "", "timing": "specific day/window per the seller's cadence rules" } ],
  "antipatterns": [ { "dont": "", "why": "cites something specific from the source" } ],
  "voice_notes": [ "places where a draft risks drifting off the seller's voice or compliance rules" ]
}
```

## Render input

`scripts/build_brief.py` takes one JSON file:

```json
{
  "seller": {
    "company": "", "tagline": "", "website": "", "location": "",
    "colors": { "primary": "#0E1A2B", "accent": "#B8924C" },
    "contact": { "name": "", "email": "", "phone": "" },
    "footer_note": "", "compliance_note": ""
  },
  "brief": { ...the schema above... }
}
```

All seller fields come from `seller-profile.md`. `compliance_note` (optional) prints as a labeled strip at the end of the brief.
