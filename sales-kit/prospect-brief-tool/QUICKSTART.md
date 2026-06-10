# Latitude 43 — Prospect Brief Tool · Quickstart

One HTML file. No install, no API key, no account beyond a free claude.ai login. Paste a LinkedIn profile in; get back a branded pre-call brief with hot moments, mirror language, warm-intro paths, objection responses, three outreach drafts, and a multi-touch plan — exportable to PDF.

---

## Setup (once, ~3 minutes)

1. Save `latitude43-prospect-brief.html` anywhere on your computer (Desktop, OneDrive — doesn't matter).
2. Double-click it. It opens in your browser.
3. The **Settings** card appears on first open. Enter your name, email, and phone. These go in the brief header and footer. Saved in your browser only.
4. Drag the **Capture LinkedIn page** button to your bookmarks bar. Don't click it on the tool page — drag it.

Done.

## Per prospect (~5 minutes)

1. Open the prospect's LinkedIn profile in your browser. Click the **Capture LinkedIn page** bookmarklet. A toast confirms the page text is on your clipboard.
2. Switch to the tool. Paste into **Profile content**.
3. Go back to LinkedIn and open the profile's activity: add `/recent-activity/all/` to the profile URL. Click the bookmarklet again. Paste into **Recent activity**. *Optional but strongly recommended — posts are the richest signal source. Skipping this thins the brief.*
4. Pick the **Prospect type** (founder / VC-PE / RIA / family office). This calibrates the pitch angle and the Atlas tier recommendation.
5. Click **Generate brief**. The full prompt is copied to your clipboard and claude.ai opens in a new tab.
6. In claude.ai: paste (Ctrl+V), send, wait ~30 seconds. Claude returns a large JSON block. Copy the whole `{...}` block.
7. Back in the tool: paste into the **Step 4** box, click **Render brief**.
8. Click **Save as PDF** in the top bar. Choose "Save as PDF" in the print dialog. Out comes the branded brief.

The last 30 prospects are saved in the **Recent prospects** archive — click a chip to reload a brief without re-running anything.

## What's in the brief

Up to 26 sections; empty ones auto-hide. The high-leverage ones:

- **Hot moments right now** — what's moving in their world this week, with a USE → angle for each.
- **Atlas fit & tier recommendation** — Light Unlimited $189/mo / Office Unlimited $349/mo (or Society disqualify-up), with an evidence-based travel-volume estimate.
- **Travel footprint & pain signals** — every flight, conference, roadshow, or airport gripe in their content. This is the buying signal for a travel office.
- **Mirror language** — their exact words vs the generic equivalents not to use.
- **Connection paths & warm intros** — mutuals, shared ex-employers, schools, communities, and how to ask.
- **Likely objections & pre-baked responses** — calibrated to this prospect, seeded from the discovery playbook.
- **Three outreach drafts** — voice-guide enforced (no exclamation marks, no banned vocabulary, private-bank register). Copy buttons on each.
- **Plan of attack** — multi-touch with specific timing, following the cadence rules (Tue/Wed 9:00–10:30 a.m. local first touch, one follow-up at +5 business days, never past two touches without a fresh signal).
- **Anti-patterns** — things *not* to do, each anchored to something specific in their content.

## FAQ

**Do coworkers need anything installed?** No. The file is fully self-contained. Email it, OneDrive it, Teams it. They save and double-click.

**Does it need a paid Claude account?** No. A free claude.ai account handles the paste-in/paste-out flow.

**Is prospect data sent anywhere?** Only to claude.ai, when you paste the prompt there yourself. The tool itself makes no network calls. Settings and the archive live in your browser's localStorage.

**The brief came back thin.** You probably skipped the recent-activity paste. Posts drive the hot moments, mirror language, and anti-patterns. Capture `/recent-activity/all/` and regenerate.

**"Could not parse that as JSON."** Copy Claude's entire `{...}` block — from the first `{` to the last `}` — and paste again. A re-ask in claude.ai ("return only the JSON") fixes the rare malformed response.

**Compliance.** Outreach drafts follow the brand voice guide, but anything member- or prospect-facing still gets normal pre-send review. The brief excludes sensitive personal categories (health, religion, politics) by design.

---

*Latitude 43 · Members' travel office for founders, GPs, and principals · Internal sales tooling.*
