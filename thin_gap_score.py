#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Per-thin-category skill-level gap scanner.

For each skills.json category with <20 skills:
  - build the vocabulary of its EXISTING skills (name+description+variants)
  - for each feeding project prompt (related_skills references this cat):
      compute bag-of-words Jaccard between prompt(title+snippet) and existing-skill vocab
  - low Jaccard  => prompt's capability vocabulary is NOT present in existing skills
                    => candidate NEW skill worth considering
  - high Jaccard => already covered by existing skills

Output: per category -> count of low-overlap feeds + top candidate prompts.
"""
import json, re, os, sys
from collections import defaultdict

ROOT = r"C:\AI\Free_Pormpt"
SKILLS = r"C:\AI\Skills_Library\skills.json"
IDX = os.path.join(ROOT, "prompts", "_search-index.json")

STOP = set("""a an the of to for and or with in on at by from as is are be can will your you
this that these those it its their our we i my me he she they them his her not no if then else
using use used into out over under between through across via per each any all some more most
how what when where who why which while about into generate create make build write design plan
prompt chatgpt claude ai tool help guide template system step steps first second based using
using our your you'll you're we'll they're generator builder writer assistant coach expert
script strategy framework method approach model analysis report generator prompt for chatgpt
and claude with ai tool help me create a an the of to for""".split())

def tok(s):
    s = s.lower()
    s = re.sub(r"&#x27;|&amp;|&quot;|&#39;", "'", s)
    s = re.sub(r"[^a-z0-9\s\-]", " ", s)
    out = set()
    for w in s.split():
        w = w.strip("-")
        if len(w) > 2 and w not in STOP:
            out.add(w)
    return out

# ---- load skills.json ----
with open(SKILLS, encoding="utf-8") as f:
    sk = json.load(f)
lib = sk["High_Impact_Skills_Library"]
cats = lib["categories"]

existing_by_cat = {}
all_cat_names = []
for c in cats:
    cname = c["category_name"].strip("'")
    all_cat_names.append(cname)
    skills = c.get("skills", [])
    text = set()
    for s in skills:
        sn = s.get("skill_name", "")
        sd = s.get("description", "")
        v = s.get("variants", "")
        if isinstance(v, list):
            vtxt = " ".join(str(x) for x in v)
        else:
            vtxt = str(v)
        blob = f"{sn} {sd} {vtxt}"
        text |= tok(blob)
    existing_by_cat[cname] = (len(skills), text)

# ---- thin categories ----
THIN = {n: (cnt, v) for n, (cnt, v) in existing_by_cat.items() if cnt < 20}

# ---- load search index ----
with open(IDX, encoding="utf-8") as f:
    idx = json.load(f)

# map: cat -> list of (title, score, snippet_tokens)
feeds = defaultdict(list)
for it in idx:
    rs = it.get("related_skills") or []
    title = it.get("title", "")
    snip = it.get("snippet", "") or ""
    ptok = tok(title + " " + snip)
    for r in rs:
        cat = r.get("cat", "")
        if cat in THIN:
            feeds[cat].append((title, r.get("score", 0), ptok))

THRESH = 0.06  # Jaccard below this => vocabulary not represented in existing skills

print("="*90)
print(f"THIN CATEGORIES: {len(THIN)}   | Jaccard threshold(low=new candidate): {THRESH}")
print("="*90)
summary = []
for cat in sorted(THIN, key=lambda c: -len(feeds.get(c, []))):
    cnt, evocab = THIN[cat]
    fl = feeds.get(cat, [])
    if not fl:
        print(f"\n### {cat}  (skills={cnt}, feeds=0)  -> ORPHAN: no project prompt routes here")
        summary.append((cat, cnt, 0, 0, "orphan"))
        continue
    low, high = [], []
    for title, score, ptok in fl:
        inter = len(evocab & ptok)
        union = len(evocab | ptok) or 1
        j = inter / union
        rec = (title, score, round(j, 3), len(ptok))
        (low if j < THRESH else high).append(rec)
    low.sort(key=lambda r: r[2])  # lowest overlap first
    summary.append((cat, cnt, len(fl), len(low), "scored"))
    print(f"\n### {cat}  (skills={cnt}, feeds={len(fl)}, low-overlap(candidate new)={len(low)}, covered={len(high)})")
    print(f"  -- TOP candidate NEW-skill prompts (lowest Jaccard, title | score | J | prompt_tokens):")
    for title, score, j, ntok in low[:18]:
        print(f"     · {title[:64]:64} sc={score:>2} J={j:<5} n={ntok}")

print("\n" + "="*90)
print("SUMMARY (cat | skills | feeds | candidate-new | status)")
print("="*90)
for cat, cnt, nf, nl, st in summary:
    print(f"  {cat:42} skills={cnt:>2} feeds={nf:>4} new~={nl:>4}  {st}")
