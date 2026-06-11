---
name: linkedin-prospect-brief
description: Build a pre-call sales intelligence brief from a LinkedIn profile — hot moments, buying signals, mirror language, warm-intro paths, objection responses, outreach drafts, and a timed plan of attack, rendered as a branded printable HTML report. Use when the user asks to "brief" a prospect, research a LinkedIn profile for outreach, or prepare for a sales call. Works for any business via a one-time seller profile.
---

# LinkedIn Prospect Brief

Turns a LinkedIn profile (plus recent activity) into a branded pre-call brief written the way a top-1% salesperson prepares: negative space, leverage, and the exact human moment to show up.

## Quick start

```
brief https://www.linkedin.com/in/example/
```

or the user pastes profile text directly. Output: a branded HTML brief (print-ready for PDF) plus the three highest-leverage actions in chat.

## Workflow

1. **Load the seller profile.** Look for `seller-profile.md` in the project root, then in this skill's folder. This file carries everything company-specific: the offer, pricing, audience types, voice rules, objection bank, cadence rules. If it doesn't exist, interview the user using [SELLER-PROFILE-TEMPLATE.md](SELLER-PROFILE-TEMPLATE.md) and save their answers as `seller-profile.md` in the project root before continuing. Never invent seller facts — pricing, claims, and objection answers come only from this file.

2. **Gather prospect data.**
   - If web browsing or fetch tools are available, retrieve the profile page and its recent activity (`<profile-url>/recent-activity/all/`).
   - Otherwise ask the user to paste the profile text and (strongly encouraged) the recent-activity text. Posts are the richest signal source — without them, hot moments, mirror language, and anti-patterns will be thin. Say so.

3. **Analyze.** Produce the brief JSON per [BRIEF-SCHEMA.md](BRIEF-SCHEMA.md). Hard rules:
   - Every claim anchors to the source text. Leave fields empty rather than invent.
   - Exclude sensitive personal categories (health, religion, politics, sexuality) from personal signals even if visible.
   - Anti-patterns must derive from THIS prospect's content; each "why" cites something specific. Fewer is better than generic.
   - Outreach drafts obey the seller's voice rules verbatim. Objection responses adapt the seller's objection bank — never invent different positioning.
   - The plan of attack follows the seller's cadence rules.
   - If the seller profile lists compliance constraints (e.g., FINRA marketing rules), apply them to every draft and flag anything borderline in `voice_notes`.

4. **Render.** Assemble `{"seller": {...}, "brief": {...}}` (seller block fields are listed in BRIEF-SCHEMA.md §Render input) and run:
   ```
   python3 scripts/build_brief.py input.json -o <Prospect_Name>_brief.html
   ```
   The script is stdlib-only and deterministic. Empty sections auto-hide. The user prints to PDF from the browser.

5. **Deliver.** Send the HTML file. In chat, summarize only: the read in one paragraph, the recommended outreach variant, and the first three plan steps with timing. Do not dump the whole brief into chat.

## Notes

- One seller profile serves the whole team; the `contact` block personalizes the header per sender.
- Re-running for a prospect: regenerate rather than patch — source content moves fast.
- If the user wants format changes (new sections, different branding), edit BRIEF-SCHEMA.md and `scripts/build_brief.py` together — the schema keys and the renderer must stay in sync.
