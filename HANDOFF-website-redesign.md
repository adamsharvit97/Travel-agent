# Handoff — Latitude 43 website redesign (lookbook style)

**Date:** 2026-06-10
**Repo:** `adamsharvit97/Travel-agent` · **branch:** `claude/adoring-feynman-Xj54w` (all work committed and pushed, committed and pushed (latest: `ddd3790`).
**Next session's job:** redesign the Latitude 43 website (`website/`) in the visual style of `deals/brand/mockup-3-lookbook.html`, which the founder called "absolutely perfect for the website."

---

## 1. What Latitude 43 is

A one-advisor luxury travel office, Toronto (43°N), serving small-business owners across the US.
**Mission (founder's words):** give small businesses easy travel so they can focus on getting the job done — or having a good time with family — with peace of mind that they're getting the best possible bookings and everything is taken care of.

**Brand register:** *adjacent to Amalfi Private Jets* — luxury but comfortable, dark and sleek, intimate/residential rather than marble-lobby. The canonical reference is Hotel Le Toiny, not the Four Seasons lobby. Full forensic study: `research/amalfi-deep-dive.md`. See also `research/brand-register-private-aviation.md`, `research/positioning-master.md`.

**Hard constraint from the founder:** the site must NOT look AI-generated. The previous deliverable (`website/toronto-deal-calendar.html`) was rejected as "AI slop." Photography-heavy, specific, understated copy; no generic SaaS patterns.

## 2. The chosen design direction

`deals/brand/mockup-3-lookbook.html` — open it first. Its DNA:

- **Palette:** warm near-black `#0C0A09` / `#13110F`, lines `#2A241C`, text `#F2ECDF`, soft `#C6BCA6`, mute `#827763`, champagne gold `#D9B987`, bright gold `#F2D29E`
- **Type:** Playfair Display (display, italics for emphasis) · Inter (body) · JetBrains Mono (10px uppercase, letter-spaced `.2em` eyebrows/labels)
- **Imagery:** full-bleed photography, `brightness(.7–.75) saturate(.9)`, bottom gradient veils to near-black, captions sitting on the image
- **Patterns:** hero feature card → two side-by-side tiles → quiet bordered list rows; brand mark "Latitude *43°*" with italic gold degree
- Mockups 1 and 2 (same folder) are siblings; mockup-2's matrix may inform any data displays

## 3. Current site to redesign

`website/` — ~20 pages in an older "v3" style (navy `#0E1A2B`, brass `#B8924C`, EB Garamond, `styles.css`, `v3-*` classes). Structure worth keeping: index, approach, atlas (membership), journal, about, contact, for-founders / for-investors / for-advisors / for-solo, fees, faq, case-studies, press. Pricing on index: Atlas Principal $3,600 / Atlas Office $12,000 / Atlas Firm $36,000 per year.

**Note:** the legacy "Preface"-brand files (`preface-*`/`design-*` at the root) have been removed from the repo. `website/toronto-deal-calendar.html` should likely be removed from the site (see §4).

## 4. Adjacent workstream (do not conflate)

The hotel deal calendar is an **email deliverable, not a website page** (founder may not be allowed to host it). Pipeline lives in `deals/` (catalog, observations, generators, README). The three email mockups in `deals/brand/` double as the brand exploration that produced the chosen style. Don't rebuild deal pages into the site.

## 5. Suggested first moves

1. `git fetch origin claude/adoring-feynman-Xj54w && git checkout` it (or merge into the session's designated branch).
2. Open `deals/brand/mockup-3-lookbook.html` and `website/index.html` side by side.
3. Restyle the homepage first as the proof piece; get founder sign-off before propagating to the other pages.
4. Photography selection matters as much as CSS — curate Unsplash (or licensed) shots that feel residential/cinematic, never stocky.

## 6. Suggested skills

- `brainstorming` — before starting the redesign (explore intent: which pages, how much restructure vs. reskin).
- `ui-ux-pro-max` / `ui-styling` — for the build itself.
- `brand` — to keep voice/visual identity consistent with the Amalfi-adjacent register.
- `verify` or `run` — to eyeball pages in a browser before showing the founder.

## 7. Voice notes (anti-"AI slop")

Understated, specific, first-person-office: "the desk," "we'll watch the rate," "the weeks the city's best rooms soften." No exclamation points, no feature-grid boosterism, no "unlock/seamless/elevate." Short letters, ledger lists, mono labels. When in doubt, read the copy in `deals/brand/mockup-1-cinematic.html`.
