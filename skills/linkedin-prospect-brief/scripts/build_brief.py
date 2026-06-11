#!/usr/bin/env python3
"""Render a prospect brief JSON into a branded, print-ready HTML report.

Usage:
    python3 build_brief.py input.json -o brief.html

input.json = {"seller": {...}, "brief": {...}} per BRIEF-SCHEMA.md.
Stdlib only. Empty sections are hidden automatically.
"""
import argparse
import datetime
import html
import json
import sys


def esc(v):
    return html.escape(str(v)) if v is not None else ""


def non_empty(v):
    if v is None:
        return False
    if isinstance(v, str):
        return v.strip() != ""
    if isinstance(v, (list, tuple)):
        return any(non_empty(x) for x in v)
    if isinstance(v, dict):
        return any(non_empty(x) for x in v.values())
    return True


def ul(items):
    lis = "".join(f"<li>{esc(x)}</li>" for x in items if non_empty(x))
    return f"<ul>{lis}</ul>"


def kv(obj, labels):
    rows = []
    for key, label in labels:
        v = obj.get(key)
        if not non_empty(v):
            continue
        if isinstance(v, (list, tuple)):
            v = "; ".join(str(x) for x in v)
        rows.append(f'<div class="k">{esc(label)}</div><div>{esc(v)}</div>')
    return '<div class="kv">' + "".join(rows) + "</div>"


def items(arr, lead, meta=None, use=None):
    out = []
    for it in arr:
        if isinstance(it, str):
            out.append(f'<div class="item"><div class="lead">{esc(it)}</div></div>')
            continue
        if not non_empty(it):
            continue
        h = f'<div class="item"><div class="lead">{esc(it.get(lead, ""))}</div>'
        if meta and non_empty(it.get(meta)):
            h += f'<div class="meta">{esc(it[meta])}</div>'
        if use and non_empty(it.get(use)):
            h += f'<div class="use"><b>USE &rarr;</b> {esc(it[use])}</div>'
        out.append(h + "</div>")
    return "".join(out)


class Renderer:
    def __init__(self):
        self.n = 0
        self.parts = []

    def sec(self, title, inner, cond=True):
        if not cond or not inner:
            return
        self.n += 1
        self.parts.append(
            f'<div class="bsec"><h3><span class="idx">{self.n:02d}</span>'
            f"{esc(title)}</h3>{inner}</div>"
        )


def render(seller, b):
    r = Renderer()
    today = datetime.date.today().strftime("%a, %b %d, %Y")
    primary = seller.get("colors", {}).get("primary", "#1a2333")
    accent = seller.get("colors", {}).get("accent", "#b08d4f")
    contact = seller.get("contact", {})
    contact_line = " &middot; ".join(
        esc(x) for x in [contact.get("name"), contact.get("phone"), contact.get("email")] if x
    )

    head = (
        f'<div class="brief-head"><span class="eyebrow">{esc(seller.get("company", ""))}'
        f" &middot; Prospect Brief &middot; {today}</span>"
        f'<h1>{esc(b.get("name", "Prospect"))}</h1>'
    )
    if non_empty(b.get("headline")):
        loc = f' &middot; {esc(b["location"])}' if non_empty(b.get("location")) else ""
        head += f'<div class="sub">{esc(b["headline"])}{loc}</div>'
    head += f'<div class="contact">{contact_line}</div></div>'

    if non_empty(b.get("snapshot")):
        r.sec("Profile snapshot", kv(b["snapshot"], [
            ("current_role", "Current role"), ("prior_roles", "Prior roles"),
            ("education", "Education"), ("credentials", "Credentials"), ("network", "Network")]))
    if non_empty(b.get("summary")):
        r.sec("The read", f"<p>{esc(b['summary'])}</p>")
    if non_empty(b.get("hot_moments")):
        r.sec("Hot moments right now", items(b["hot_moments"], "what", "why", "use"))
    if non_empty(b.get("recent_changes")):
        r.sec("Recent changes", ul(b["recent_changes"]))
    if non_empty(b.get("company")):
        inner = kv(b["company"], [("name", "Company"), ("what_they_do", "What they do"),
                                  ("size", "Size"), ("notes", "Notes")])
        if non_empty(b["company"].get("recent_changes")):
            inner += '<div class="subhead">Recent changes</div>' + ul(b["company"]["recent_changes"])
        r.sec("Company snapshot", inner)
    if non_empty(b.get("industry_pulse")):
        r.sec("Industry vertical pulse", f"<p>{esc(b['industry_pulse'])}</p>")
    if non_empty(b.get("tenure_stability")):
        r.sec("Tenure & role stability", kv(b["tenure_stability"], [
            ("arc", "Career arc"), ("read", "Read"), ("approach", "Approach")]))
    if non_empty(b.get("power_role")):
        r.sec("Power & role analysis", kv(b["power_role"], [
            ("type", "Type"), ("budget_authority", "Budget authority"),
            ("buying_decision", "Buying decision"), ("implication", "Implication")]))
    if non_empty(b.get("offer_fit")):
        r.sec("Offer fit & recommendation", kv(b["offer_fit"], [
            ("recommendation", "Recommendation"), ("price", "Price"), ("fit", "Fit"),
            ("volume_estimate", "Volume estimate"), ("rationale", "Rationale")]))
    if non_empty(b.get("need_signals")):
        r.sec("Need & pain signals", items(b["need_signals"], "signal", "source", "use"))
    if non_empty(b.get("stakeholders")):
        r.sec("Adjacent stakeholders", items(b["stakeholders"], "who", "role", "why"))
    if non_empty(b.get("reach")):
        r.sec("Best time & channel", kv(b["reach"], [
            ("channel", "Channel"), ("best_time", "Best time"),
            ("reply_window", "Reply window"), ("avoid", "Avoid")]))
    ml = b.get("mirror_language") or {}
    if non_empty(ml):
        inner = ('<div class="mirror"><div class="good"><h4>Their words — use these</h4>'
                 + (ul(ml.get("their_words", [])) if non_empty(ml.get("their_words")) else "<p>—</p>")
                 + '</div><div class="bad"><h4>Generic equivalents — avoid</h4>'
                 + (ul(ml.get("avoid_words", [])) if non_empty(ml.get("avoid_words")) else "<p>—</p>")
                 + "</div></div>")
        if non_empty(ml.get("directive")):
            inner += f'<p class="directive"><em>{esc(ml["directive"])}</em></p>'
        r.sec("Mirror language", inner)
    if non_empty(b.get("tone")):
        r.sec("Tone calibration", kv(b["tone"], [
            ("style", "Style"), ("formality", "Formality"), ("directive", "Directive")]))
    if non_empty(b.get("influences")):
        r.sec("Influences they cite", ul(b["influences"]))
    if non_empty(b.get("recent_events")):
        r.sec("Recent travel & events", items(b["recent_events"], "event", "when", "use"))
    if non_empty(b.get("personal_signals")):
        r.sec("Personal signals", ul(b["personal_signals"]))
    if non_empty(b.get("posting_patterns")):
        r.sec("Posting patterns", kv(b["posting_patterns"], [
            ("cadence", "Cadence"), ("categories", "Categories"), ("engagement", "Engagement")]))
    if non_empty(b.get("risk_signals")):
        r.sec("Risk signals", ul(b["risk_signals"]))
    if non_empty(b.get("buying_signals")):
        r.sec("Buying signals & triggers", items(b["buying_signals"], "signal", "timing"))
    if non_empty(b.get("warm_paths")):
        r.sec("Connection paths & warm intros", items(b["warm_paths"], "path", None, "how_to_ask"))
    if non_empty(b.get("hooks")):
        r.sec("Personalization hooks (ranked)", items(b["hooks"], "hook", "leverage"))
    if non_empty(b.get("objections")):
        qa = "".join(
            f'<div class="qa"><div class="q">Q: {esc(o.get("q",""))}</div>'
            f'<div class="a">A: {esc(o.get("a",""))}</div></div>'
            for o in b["objections"] if non_empty(o))
        r.sec("Likely objections & pre-baked responses", qa)
    if non_empty(b.get("outreach")):
        vs = []
        for i, v in enumerate(b["outreach"]):
            if not non_empty(v):
                continue
            label = esc(v.get("variant", f"Variant {i + 1}"))
            if non_empty(v.get("channel")):
                label += f' &middot; {esc(v["channel"])}'
            block = f'<div class="variant"><div class="vhead">{label}</div><div class="vbody">'
            if non_empty(v.get("subject")):
                block += f'<div class="subj"><b>SUBJECT</b> {esc(v["subject"])}</div>'
            block += f'<div class="body-text">{esc(v.get("body",""))}</div>'
            if non_empty(v.get("rationale")):
                block += f'<div class="why">{esc(v["rationale"])}</div>'
            vs.append(block + "</div></div>")
        r.sec("Outreach drafts", "".join(vs))
    if non_empty(b.get("plan")):
        steps = "".join(
            f'<div class="plan-step"><div class="pn">{esc(p.get("step", i + 1))}</div>'
            f'<div><div>{esc(p.get("action",""))}</div>'
            + (f'<div class="pt">{esc(p["timing"])}</div>' if non_empty(p.get("timing")) else "")
            + "</div></div>"
            for i, p in enumerate(b["plan"]) if non_empty(p))
        r.sec("Plan of attack", steps)
    if non_empty(b.get("antipatterns")):
        antis = "".join(
            f'<div class="anti"><div class="d">{esc(a.get("dont",""))}</div>'
            f'<div class="w">{esc(a.get("why",""))}</div></div>'
            for a in b["antipatterns"] if non_empty(a))
        r.sec("Anti-patterns — do not do these", antis)
    if non_empty(b.get("voice_notes")):
        r.sec("Voice & compliance notes", ul(b["voice_notes"]))

    foot_bits = [seller.get("footer_note"), seller.get("website"), seller.get("location")]
    foot = " &middot; ".join(esc(x) for x in foot_bits if x)
    foot += ("<br>Internal sales brief. Source: public LinkedIn content. "
             "Pre-send review applies to all outreach.")
    if non_empty(seller.get("compliance_note")):
        foot += f'<br><span class="comp">{esc(seller["compliance_note"])}</span>'

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(b.get("name", "Prospect"))} — Prospect Brief — {esc(seller.get("company", ""))}</title>
<style>
  :root {{ --primary: {primary}; --accent: {accent}; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: Georgia, 'Times New Roman', serif; font-size: 15px; line-height: 1.6;
         color: #222; background: #f6f4ef; }}
  .wrap {{ max-width: 860px; margin: 0 auto; padding: 40px 24px; }}
  .brief-head {{ background: var(--primary); color: #f4f1ea; padding: 34px 36px; }}
  .eyebrow {{ font-family: Helvetica, Arial, sans-serif; font-size: 0.68rem; letter-spacing: 0.22em;
              text-transform: uppercase; color: var(--accent); font-weight: 600; display: block;
              margin-bottom: 8px; }}
  .brief-head h1 {{ font-size: 2.2rem; font-weight: 400; }}
  .brief-head .sub {{ opacity: 0.85; font-style: italic; margin-top: 6px; }}
  .brief-head .contact {{ margin-top: 18px; font-family: Helvetica, Arial, sans-serif;
                          font-size: 0.8rem; opacity: 0.9; }}
  .bsec {{ background: #fff; border: 1px solid #e2dccd; border-top: none; padding: 24px 36px;
           page-break-inside: avoid; }}
  .bsec h3 {{ font-size: 1.15rem; color: var(--primary); margin-bottom: 12px; padding-bottom: 8px;
              border-bottom: 1px solid #e2dccd; }}
  .bsec h3 .idx {{ color: var(--accent); margin-right: 10px; font-size: 0.95rem; }}
  .bsec p, .bsec li {{ font-size: 0.93rem; }}
  .bsec ul {{ padding-left: 20px; }} .bsec li {{ margin-bottom: 7px; }}
  .kv {{ display: grid; grid-template-columns: 190px 1fr; gap: 6px 18px; font-size: 0.93rem; }}
  .kv .k {{ color: #777; font-family: Helvetica, Arial, sans-serif; font-size: 0.72rem;
            letter-spacing: 0.1em; text-transform: uppercase; padding-top: 3px; }}
  .subhead {{ font-family: Helvetica, Arial, sans-serif; font-size: 0.72rem; letter-spacing: 0.1em;
              text-transform: uppercase; margin-top: 12px; font-weight: 700; }}
  .item {{ border-left: 3px solid var(--accent); padding: 8px 14px; margin-bottom: 12px;
           background: #f6f4ef; page-break-inside: avoid; }}
  .item .lead {{ font-weight: 700; }}
  .item .meta {{ font-size: 0.82rem; color: #666; margin-top: 3px; }}
  .item .use {{ font-size: 0.85rem; margin-top: 5px; }}
  .item .use b {{ color: var(--accent); font-family: Helvetica, Arial, sans-serif;
                  font-size: 0.7rem; letter-spacing: 0.08em; }}
  .mirror {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }}
  .mirror h4 {{ font-family: Helvetica, Arial, sans-serif; font-size: 0.75rem;
                letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 8px; }}
  .mirror .good h4 {{ color: var(--accent); }} .mirror .bad h4 {{ color: #a33; }}
  .directive {{ margin-top: 12px; }}
  .qa {{ margin-bottom: 14px; page-break-inside: avoid; }}
  .qa .q {{ font-weight: 700; }} .qa .a {{ margin-top: 3px; }}
  .variant {{ border: 1px solid #e2dccd; margin-bottom: 18px; page-break-inside: avoid; }}
  .variant .vhead {{ background: #f6f4ef; padding: 10px 16px; font-weight: 700; font-size: 0.9rem; }}
  .variant .vbody {{ padding: 14px 16px; }}
  .variant .subj {{ font-size: 0.88rem; margin-bottom: 8px; }}
  .variant .subj b {{ color: var(--accent); font-family: Helvetica, Arial, sans-serif;
                      font-size: 0.7rem; letter-spacing: 0.08em; }}
  .variant .body-text {{ white-space: pre-wrap; font-size: 0.92rem; background: #f6f4ef;
                         padding: 14px; border-left: 3px solid var(--primary); }}
  .variant .why {{ font-size: 0.82rem; color: #666; margin-top: 10px; font-style: italic; }}
  .plan-step {{ display: flex; gap: 14px; margin-bottom: 12px; page-break-inside: avoid; }}
  .plan-step .pn {{ font-size: 1.3rem; color: var(--accent); min-width: 26px; }}
  .plan-step .pt {{ font-family: Helvetica, Arial, sans-serif; font-size: 0.76rem; color: #666;
                    letter-spacing: 0.06em; }}
  .anti {{ border-left: 3px solid #a33; background: #faf5f2; padding: 8px 14px;
           margin-bottom: 10px; page-break-inside: avoid; }}
  .anti .d {{ font-weight: 700; }} .anti .w {{ font-size: 0.85rem; color: #666; margin-top: 2px; }}
  .brief-foot {{ background: var(--primary); color: #d8d2c2; padding: 18px 36px;
                 font-family: Helvetica, Arial, sans-serif; font-size: 0.75rem;
                 letter-spacing: 0.05em; }}
  .brief-foot .comp {{ color: var(--accent); }}
  @media print {{
    body {{ background: #fff; }} .wrap {{ max-width: none; padding: 0; }}
    .bsec {{ border-left: none; border-right: none; }}
  }}
</style></head><body><div class="wrap">
{head}
{''.join(r.parts)}
<div class="brief-foot">{foot}</div>
</div></body></html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", help="JSON file: {seller: {...}, brief: {...}}")
    ap.add_argument("-o", "--output", default="brief.html")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)
    seller, brief = data.get("seller"), data.get("brief")
    if not isinstance(seller, dict) or not isinstance(brief, dict):
        sys.exit("input must be a JSON object with 'seller' and 'brief' objects")

    out = render(seller, brief)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {args.output} ({len(out):,} bytes, {out.count('class=\"bsec\"')} sections)")


if __name__ == "__main__":
    main()
