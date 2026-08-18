import json, re, os, glob
from collections import Counter, defaultdict

BASE = 'C:/AI/Free_Pormpt/prompts'
JSON_IDX = 'C:/AI/Free_Pormpt/prompts/_search-index.json'

# skills.json categories that hold SPECIFIC/domain skill units (not generic meta/infra)
SPECIFIC = {'Domain_Specific_Expertise','Domain_Specific_Reasoning','Commercial_Growth&Acquisition',
'Persona&Narrative_Synthesis','Visual_Architecture&Creative_Engineering','UI_UX&Frontend_Engineering',
'Interactive_Pedagogy&Diagnostic_Systems','RPG&Immersive_World_Systems','Interactive_Narrative&Creative_Fiction_Engine',
'Strategic_Decision&Adversarial_Thinking','Academic_Research_Synthesis_Pipeline','Academic_Insight&Forensics',
'Minimalist_Entrepreneurship_Execution','Operational_Governance&Reporting'}

STOP = set('''a an the you your we our their to of for in on at by with and or as is are be can will should
must may need do does done using use write create provide include each this that these those it its from into
over under more most less such not no if then than but about which what who how when where why all any some
one two three first second step steps section sections format output response structure'''.split())

def extract_body(path):
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    m = re.search(r'```(.*?)```', txt, re.DOTALL)
    if m: return m.group(1)
    m2 = re.search(r'##\s*Prompt\s*(.*?)(?=\n##\s)', txt, re.DOTALL)
    return m2.group(1) if m2 else ''

def normalize(body):
    body = re.sub(r'\{\{.*?\}\}', ' ', body)
    body = re.sub(r'[^a-z0-9 ]', ' ', body.lower())
    return set(t for t in body.split() if len(t) > 2 and t not in STOP)

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

with open(JSON_IDX, encoding='utf-8') as f:
    idx = json.load(f)
slug_top = {it['slug']: (it['related_skills'][0]['cat'] if it.get('related_skills') else None) for it in idx}

files = [f for f in glob.glob(os.path.join(BASE,'**','*.md'), recursive=True) if os.path.basename(f)!='index.md']
by_cat = defaultdict(list)
for f in files:
    by_cat[os.path.relpath(f, BASE).split(os.sep)[0]].append(f)

THRESH = 0.30
cat_stats = {}
covered_by_skillcat = Counter()
novel_by_projcat = Counter()
for cat, flist in by_cat.items():
    clusters = []
    for f in flist:
        toks = normalize(extract_body(f))
        slug = os.path.splitext(os.path.basename(f))[0]
        tc = slug_top.get(slug)
        best=None; bj=0
        for cl in clusters:
            j=jaccard(toks, cl[0])
            if j>bj: bj=j; best=cl
        if best is not None and bj>=THRESH:
            best[1].append(slug); best[2][tc]+=1
        else:
            clusters.append([toks,[slug],Counter({tc:1})])
    raw=len(flist); dist=len(clusters)
    nov=0; cov=0
    for cl in clusters:
        tc = cl[2].most_common(1)[0][0] if cl[2] else None
        if tc in SPECIFIC:
            cov+=1; covered_by_skillcat[tc]+=1
        else:
            nov+=1; novel_by_projcat[cat]+=1
    cat_stats[cat]=dict(raw=raw, distinct=dist, novel=nov, covered=cov, ratio=round(dist/raw,3))

print(f'{"category":16} {"raw":>5} {"distinct":>8} {"supplement":>10} {"covered":>8}')
for cat in sorted(cat_stats, key=lambda x:-cat_stats[x]['raw']):
    s=cat_stats[cat]
    print(f'{cat:16} {s["raw"]:>5} {s["distinct"]:>8} {s["novel"]:>10} {s["covered"]:>8}')
tr=sum(s['raw'] for s in cat_stats.values()); td=sum(s['distinct'] for s in cat_stats.values())
tn=sum(s['novel'] for s in cat_stats.values()); tc2=sum(s['covered'] for s in cat_stats.values())
print(f'{"TOTAL":16} {tr:>5} {td:>8} {tn:>10} {tc2:>8}')
print(f'\nCompression (distinct/raw) = {td/tr:.3f}  -> template-variant redundancy ~ {100*(1-td/tr):.1f}%')
print(f'\nDistinct templates that skills.json LACKS a specific skill for (true supplement): {tn}')
print(f'Distinct templates already covered by a specific skills.json skill: {tc2}')
print('\nWhere skills.json already has specific coverage (by skill category):')
for k,v in covered_by_skillcat.most_common():
    print(f'  {k}: {v}')
out=dict(threshold=THRESH, per_category=cat_stats, totals=dict(raw=tr,distinct=td,novel=tn,covered=tc2),
         covered_by_skillcat=dict(covered_by_skillcat), novel_by_projcat=dict(novel_by_projcat))
with open('C:/AI/Free_Pormpt/_template_dedup.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
print('\nsaved _template_dedup.json')
