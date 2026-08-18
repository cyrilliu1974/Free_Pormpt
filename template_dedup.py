import json, re, os, glob
from collections import Counter, defaultdict

BASE = 'C:/AI/Free_Pormpt/prompts'
JSON_IDX = 'C:/AI/Free_Pormpt/prompts/_search-index.json'

# skills.json generic(meta/infra) vs specific(domain) classification
GENERIC = {'Meta_Prompt&System_Design','Context&Session_Management','Skill_Orchestration&Assembly',
'Input_Classification&Routing','Prompt&Manifest_Engineering','Agent_State&Trajectory_Engineering',
'Autonomous_Agent_Execution_Logic','Distributed_Cognition&Context_Orchestration','Agent_SOP_Framework&Extraction_Protocol',
'System_Verification&QA_Logic','Software_Architecture&Performance','Data_Structuring&Engineering',
'Structured_Knowledge_Navigation_Architecture','Self_Evolution&Refinement','Axiomatic_Logic&Audit_Systems',
'Human_In_Loop_Workflow_Engineering'}

STOP = set('''a an the you your we our their to of for in on at by with and or as is are be can will should
must may need do does done using use write create provide include each this that these those it its from into
over under more most less such not no if then than but about which what who how when where why all any some
one two three first second step steps section sections format output response structure'''.split())

def extract_body(path):
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    m = re.search(r'```(.*?)```', txt, re.DOTALL)
    if m:
        return m.group(1)
    # fallback: text after ## Prompt
    m2 = re.search(r'##\s*Prompt\s*(.*?)(?=\n##\s)', txt, re.DOTALL)
    return m2.group(1) if m2 else ''

def normalize(body):
    body = re.sub(r'\{\{.*?\}\}', ' ', body)        # mask variables
    body = re.sub(r'[^a-z0-9 ]', ' ', body.lower())
    toks = [t for t in body.split() if len(t) > 2 and t not in STOP]
    return set(toks)

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

# load index for top related skill per slug
with open(JSON_IDX, encoding='utf-8') as f:
    idx = json.load(f)
slug_top_cat = {}
slug_cat = {}
for it in idx:
    rs = it.get('related_skills') or []
    slug_top_cat[it['slug']] = rs[0]['cat'] if rs else None
    slug_cat[it['slug']] = it['category']

THRESH = 0.55
results = {}   # category -> dict(raw, clusters list of (rep_tokens, [slugs], topcat_counter))

files = glob.glob(os.path.join(BASE, '**', '*.md'), recursive=True)
# exclude index.md files
files = [f for f in files if os.path.basename(f) != 'index.md']

by_cat = defaultdict(list)
for f in files:
    rel = os.path.relpath(f, BASE)
    parts = rel.split(os.sep)
    cat = parts[0]
    by_cat[cat].append(f)

cat_stats = {}
for cat, flist in by_cat.items():
    clusters = []   # list of [rep_tokens, [slugs], Counter(topcat)]
    for f in flist:
        body = extract_body(f)
        toks = normalize(body)
        slug = os.path.splitext(os.path.basename(f))[0]
        topcat = slug_top_cat.get(slug)
        assigned = None
        for cl in clusters:
            if jaccard(toks, cl[0]) >= THRESH:
                assigned = cl
                break
        if assigned is None:
            clusters.append([toks, [slug], Counter({topcat:1})])
        else:
            assigned[1].append(slug)
            assigned[2][topcat] += 1
    raw = len(flist)
    nclust = len(clusters)
    novel = 0
    covered = 0
    for cl in clusters:
        tc = cl[2].most_common(1)[0][0] if cl[2] else None
        if tc is None:
            covered += 1
        elif tc in GENERIC:
            novel += 1
        else:
            covered += 1
    cat_stats[cat] = dict(raw=raw, distinct=nclust, novel=novel, covered=covered,
                          ratio=round(nclust/raw, 3) if raw else 0)

# print table sorted by raw desc
print(f'{"category":16} {"raw":>5} {"distinctTemplates":>16} {"compression":>11} {"novel(gap)":>11} {"covered":>8}')
for cat in sorted(cat_stats, key=lambda x:-cat_stats[x]['raw']):
    s = cat_stats[cat]
    print(f'{cat:16} {s["raw"]:>5} {s["distinct"]:>16} {s["ratio"]:>11.2f} {s["novel"]:>11} {s["covered"]:>8}')

print()
tot_raw = sum(s['raw'] for s in cat_stats.values())
tot_dist = sum(s['distinct'] for s in cat_stats.values())
tot_novel = sum(s['novel'] for s in cat_stats.values())
tot_cov = sum(s['covered'] for s in cat_stats.values())
print(f'TOTAL raw={tot_raw} distinctTemplates={tot_dist} compression={tot_dist/tot_raw:.2f} novel(gap)={tot_novel} covered={tot_cov}')

# save detailed for report
out = {'threshold': THRESH, 'per_category': cat_stats,
       'totals': dict(raw=tot_raw, distinct=tot_dist, novel=tot_novel, covered=tot_cov)}
with open('C:/AI/Free_Pormpt/_template_dedup.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('saved _template_dedup.json')
