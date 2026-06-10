# Latitude 43 — Sales Simulation Library

Total sims: **84**. Rounds 1–7. **64** distinct persona names. **198,933** words of synthetic dialogue + evaluation.

Briefs that drove each round live in [`briefs/`](briefs/). The original prompt for each sim is captured in the `agent_id` field — full JSONL transcripts are at `~/.claude/projects/-home-user-Travel-agent/<session>/subagents/<agent_id>.jsonl`.

## Round 7 — Repeat matrix with sharper personas (15 sims)

| Sim | Model | Stage | FTG | Persona | Outcome | File |
|---|---|---|---|---|---|---|
| 1 | A | cold | FTG1 | hugo-beauchamp | soft yes to a second meeting with the gatekeeper (marisol) i | [md](r7/sim-01-modelA-hugo-beauchamp-cold-FTG1.md) |
| 2 | B | cold | FTG2 | hugo-beauchamp | verbal close on atlas office unlimited at $349/month, month- | [md](r7/sim-02-modelB-hugo-beauchamp-cold-FTG2.md) |
| 3 | C | cold | FTG3 | hugo-beauchamp | **what worked, with receipts:** | [md](r7/sim-03-modelC-hugo-beauchamp-cold-FTG3.md) |
| 4 | A | deep-discovery | FTG2 | vanessa-coyne | soft yes pending advisor consult thursday. probability of cl | [md](r7/sim-04-modelA-vanessa-coyne-deep-discovery-FTG2.md) |
| 5 | B | deep-discovery | FTG3 | vanessa-coyne | soft yes pending coo review. vanessa committed to a monday d | [md](r7/sim-05-modelB-vanessa-coyne-deep-discovery-FTG3.md) |
| 6 | C | deep-discovery | FTG1 | vanessa-coyne | verbal commitment to atlas office at $499/mo, contingent on  | [md](r7/sim-06-modelC-vanessa-coyne-deep-discovery-FTG1.md) |
| 7 | A | discovery-close | FTG3 | brett-holloran | closed. atlas office at $249/mo, ftg3 in writing, intake sch | [md](r7/sim-07-modelA-brett-holloran-discovery-close-FTG3.md) |
| 8 | B | discovery-close | FTG1 | brett-holloran | close. atlas office unlimited at $349/mo, ftg1 deployed agai | [md](r7/sim-08-modelB-brett-holloran-discovery-close-FTG1.md) |
| 9 | C | discovery-close | FTG2 | brett-holloran | close on atlas office at $499/month, annual, with ftg2 attac | [md](r7/sim-09-modelC-brett-holloran-discovery-close-FTG2.md) |
| 10 | A | negotiation | FTG1 | tomasz-werner | closed at full price, month-to-month, no discount given, two | [md](r7/sim-10-modelA-tomasz-werner-negotiation-FTG1.md) |
| 11 | B | negotiation | FTG2 | tomasz-werner | closed. $189/mo light unlimited, ftg2 intact as written, no  | [md](r7/sim-11-modelB-tomasz-werner-negotiation-FTG2.md) |
| 12 | C | negotiation | FTG3 | tomasz-werner | closed plus at list ($249), 30-day money-back honored, price | [md](r7/sim-12-modelC-tomasz-werner-negotiation-FTG3.md) |
| 13 | A | warm-referral | FTG2 | eliana-caspersen-park | closed. atlas office at $249/mo, first trip named (kyoto, no | [md](r7/sim-13-modelA-eliana-caspersen-park-warm-referral-FTG2.md) |
| 14 | B | warm-referral | FTG3 | eliana-caspersen-park | closed. agreement to be sent same day, ea onboarding thursda | [md](r7/sim-14-modelB-eliana-caspersen-park-warm-referral-FTG3.md) |
| 15 | C | warm-referral | FTG1 | eliana-caspersen-park | closed at $499/mo atlas office. ftg extended verbally and co | [md](r7/sim-15-modelC-eliana-caspersen-park-warm-referral-FTG1.md) |

## Round 6 — 3 models × 5 stages × 3 FTGs (15 sims · `r6-brief.md`)

| Sim | Model | Stage | FTG | Persona | Outcome | File |
|---|---|---|---|---|---|---|
| 1 | A | cold | FTG1 | devin-holloway | soft yes pending carla loop-in. realistic for cold inbound a | [md](r6/sim-01-modelA-devin-holloway-cold-FTG1.md) |
| 2 | B | cold | FTG2 | devin-holloway | soft close at 80% — intake sent, agreement under review, fri | [md](r6/sim-02-modelB-devin-holloway-cold-FTG2.md) |
| 3 | C | cold | FTG3 | devin-holloway | soft yes pending overnight reflection. devin self-selected t | [md](r6/sim-03-modelC-devin-holloway-cold-FTG3.md) |
| 4 | A | onboarding | FTG2 | lara-whittaker | clean onboarding. trip named (jackson hole, june 18–21). ftg | [md](r6/sim-04-modelA-lara-whittaker-onboarding-FTG2.md) |
| 5 | B | onboarding | FTG3 | lara-whittaker | strong onboarding. ea bought in by minute 30. principal alre | [md](r6/sim-05-modelB-lara-whittaker-onboarding-FTG3.md) |
| 6 | C | onboarding | FTG1 | lara-whittaker | strong onboarding. buyer arrived with live price doubt ("wat | [md](r6/sim-06-modelC-lara-whittaker-onboarding-FTG1.md) |
| 7 | A | irop | FTG3 | theo-bardakian | retention preserved, not strengthened. member exits the call | [md](r6/sim-07-modelA-theo-bardakian-irop-FTG3.md) |
| 8 | B | irop | FTG1 | theo-bardakian | member retained, trip recovered, nps-defining moment convert | [md](r6/sim-08-modelB-theo-bardakian-irop-FTG1.md) |
| 9 | C | irop | FTG2 | theo-bardakian | irop recovered (jfk flight, met meeting albeit with a downgr | [md](r6/sim-09-modelC-theo-bardakian-irop-FTG2.md) |
| 10 | A | mid-year | FTG1 | erica-lin | save with downgrade. $249 → $99, retained at lower arr but h | [md](r6/sim-10-modelA-erica-lin-mid-year-FTG1.md) |
| 11 | B | mid-year | FTG2 | erica-lin | save with downgrade. arr drops from $4,188 to $2,268 (a 46%  | [md](r6/sim-11-modelB-erica-lin-mid-year-FTG2.md) |
| 12 | C | mid-year | FTG3 | erica-lin | save at $249. arr drops from $5,988 to $2,988 (-50%). ltv tr | [md](r6/sim-12-modelC-erica-lin-mid-year-FTG3.md) |
| 13 | A | price-objection | FTG2 | marcus-voiland | closed office at $249/mo with ftg2 attached. marcus moved fr | [md](r6/sim-13-modelA-marcus-voiland-price-objection-FTG2.md) |
| 14 | B | price-objection | FTG3 | marcus-voiland | cycle time from objection to commit: roughly 11 minutes of d | [md](r6/sim-14-modelB-marcus-voiland-price-objection-FTG3.md) |
| 15 | C | price-objection | FTG1 | marcus-voiland | closed on plus ($249). buyer self-selected. ftg1 named on th | [md](r6/sim-15-modelC-marcus-voiland-price-objection-FTG1.md) |

## Round 5 — Free-form playbook stress tests (14 sims)

| # | Stage | Persona | Outcome | File |
|---|---|---|---|---|
| 1 | onboarding | sarah-brennan | sarah agreed to a 90-day re-onboarding with a structural rul | [md](r5/sim-01-sarah-brennan-onboarding.md) |
| 2 | cold | aaron-reeves | this was a competent call. not great, competent. you got the | [md](r5/sim-02-aaron-reeves-cold.md) |
| 3 |  | robert-kane | sign | [md](r5/sim-03-robert-kane.md) |
| 4 |  | constance-albright | walks | [md](r5/sim-04-constance-albright.md) |
| 5 | conference-followup | sam-reyes |  | [md](r5/sim-05-sam-reyes-conference-followup.md) |
| 6 |  | thomas-voss | sign | [md](r5/sim-06-thomas-voss.md) |
| 7 | cold-discovery | priya-shah |  | [md](r5/sim-07-priya-shah-cold-discovery.md) |
| 8 |  | derek-liu | walks | [md](r5/sim-08-derek-liu.md) |
| 9 |  | maya-choi | sign | [md](r5/sim-09-maya-choi.md) |
| 10 | irop | daniel-vasquez |  | [md](r5/sim-10-daniel-vasquez-irop-pht-va.md) |
| 11 |  | olivia-greene | **think (leaning walk)** | [md](r5/sim-11-olivia-greene.md) |
| 12 | onboarding | maria-chen-rodriguez | david did the thing most founders fail at on onboarding call | [md](r5/sim-12-maria-chen-rodriguez-onboarding.md) |
| 13 | negotiation | aaron-schmidt | sign | [md](r5/sim-13-aaron-schmidt-negotiation.md) |
| 14 | cold-discovery | marcus-hale | close | [md](r5/sim-14-marcus-hale-cold-discovery.md) |

## Round 4 — Cold leads only (12 sims · `sim-brief-r4-cold.md`)

| # | Stage | Persona | Outcome | File |
|---|---|---|---|---|
| 1 | cold | steven-hayes | close | [md](r4/sim-01-steven-hayes-cold.md) |
| 2 | cold | karen-reilly-hosseini | no close | [md](r4/sim-02-karen-reilly-hosseini-cold.md) |
| 3 | cold | walter-greene | walked | [md](r4/sim-03-walter-greene-cold.md) |
| 4 | cold | tom-russo | sign | [md](r4/sim-04-tom-russo-cold.md) |
| 5 | cold | yusef-khan-ramirez | sign | [md](r4/sim-05-yusef-khan-ramirez-cold.md) |
| 6 | cold | alistair-hayes-whitmore | sign | [md](r4/sim-06-alistair-hayes-whitmore-cold.md) |
| 7 | cold | daniel-cho | soft yes | [md](r4/sim-07-daniel-cho-cold.md) |
| 8 | cold | jennifer-boswell | sign | [md](r4/sim-08-jennifer-boswell-cold.md) |
| 9 | cold | robert-mwangi-patterson | sign | [md](r4/sim-09-robert-mwangi-patterson-cold.md) |
| 10 | cold | marcus-lindqvist | sign | [md](r4/sim-10-marcus-lindqvist-cold.md) |
| 11 | cold | megan-donovan | close | [md](r4/sim-11-megan-donovan-cold.md) |
| 12 | cold | sarah-pollard-wei | sign | [md](r4/sim-12-sarah-pollard-wei-cold.md) |

## Round 3 — Edge-case stages (10 sims · `sim-brief-r3.md`)

| # | Stage | Persona | Outcome | File |
|---|---|---|---|---|
| 1 | press-inbound | marcus-davenport | sign | [md](r3/sim-01-marcus-davenport-press-inbound.md) |
| 2 | one-trip | henry-park-wilson | walked | [md](r3/sim-02-henry-park-wilson-one-trip.md) |
| 3 | irop | greg-tanaka | sign | [md](r3/sim-03-greg-tanaka-irop.md) |
| 4 | ea-gatekeeper | beatriz-cardoso | sign | [md](r3/sim-04-beatriz-cardoso-ea-gatekeeper.md) |
| 5 | conference-followup | aisha-williams-brown | sign | [md](r3/sim-05-aisha-williams-brown-conference-followup.md) |
| 6 | spouse-buyer | caroline-whitfield-park | sign | [md](r3/sim-06-caroline-whitfield-park-spouse-buyer.md) |
| 7 | ea-gatekeeper | andrew-lee | sign | [md](r3/sim-07-andrew-lee-ea-gatekeeper.md) |
| 8 | hostile-referral | lisa-ferraro |  | [md](r3/sim-08-lisa-ferraro-hostile-referral.md) |
| 9 | winback | vanessa-castro | walked | [md](r3/sim-09-vanessa-castro-winback.md) |
| 10 | cold-discovery | trevor-mitchell | sign | [md](r3/sim-10-trevor-mitchell-cold-discovery.md) |

## Round 2 — Post-R1 retries (3 sims)

| # | Persona | Outcome | File |
|---|---|---|---|
| 1 | helena-rodriguez | sign | [md](r2/sim-01-helena-rodriguez.md) |
| 2 | marcus-wang | ghosted | [md](r2/sim-02-marcus-wang.md) |
| 08 | sarah-donnelly | sign | [md](r2/sim-08-sarah-donnelly.md) |

## Round 1 — First-pass personas (15 sims · `sim-brief.md`)

| # | Persona | Outcome | File |
|---|---|---|---|
| 1 | david-lieberman | sign | [md](r1/sim-01-david-lieberman.md) |
| 2 | janelle-watson | sign | [md](r1/sim-02-janelle-watson.md) |
| 3 | anaya-patel | walked | [md](r1/sim-03-anaya-patel.md) |
| 4 | james-park | close | [md](r1/sim-04-james-park.md) |
| 5 | marcus-brennan | no close | [md](r1/sim-05-marcus-brennan.md) |
| 6 | lakshmi-iyer-whitfield | walked | [md](r1/sim-06-lakshmi-iyer-whitfield.md) |
| 7 | yuki-tanaka-brooks | sign | [md](r1/sim-07-yuki-tanaka-brooks.md) |
| 8 | james-carruthers | close | [md](r1/sim-08-james-carruthers.md) |
| 9 | margaret-foster | walks | [md](r1/sim-09-margaret-foster.md) |
| 10 | mateo-hernandez-vega | sign | [md](r1/sim-10-mateo-hernandez-vega.md) |
| 11 | daniel-park | walks | [md](r1/sim-11-daniel-park.md) |
| 12 | robert-maslow | walked | [md](r1/sim-12-robert-maslow.md) |
| 13 | tyler-brooks | walked | [md](r1/sim-13-tyler-brooks.md) |
| 14 | caroline-buchanan-hayes | sign | [md](r1/sim-14-caroline-buchanan-hayes.md) |
| 15 | reginald-reg-whitmore |  | [md](r1/sim-15-reginald-reg-whitmore-irop.md) |

## Methodology notes

- Each sim was run as a background sub-agent. The prompt fed a persona, stage, and the relevant brief; the agent role-played both the buyer and the founder, then graded its own transcript.
- R1–R5 explored persona breadth and stage variety. R6 and R7 collapsed onto a 3 model × 5 stage × 3 FTG matrix to compare pricing/guarantee variants on matched personas.
- `model A` = v2.0 pricing ($99 Light / $249 Office). `model B` = Unlimited ($189/$349). `model C` = Three-tier ($99/$249/$499).
- `FTG1` = first month + $1K labor credit. `FTG2` = full refund + free month + $500 service credit. `FTG3` = 30-day money-back guarantee.
