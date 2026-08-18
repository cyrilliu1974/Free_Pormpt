# hybrid_search.py — 本地 hybrid 檢索 (lexical + dense embedding + RRF)
# 純本地、免 LLM API。供 Streamlit 與 CLI 共用。
#
# 用法 / Usage:
#   python hybrid_search.py --json "你的需求描述" [--topN 5] [--cat Marketing] [--sub "Landing Page Copy"] [--mode hybrid|lexical]
#   python hybrid_search.py --build            # 強制重建 corpus embedding 快取
#
# 檢索組成:
#   [lexical] 欄位加權 TF + 中文 CN→EN 展開 + 英文同義擴展 + 中文 bigram
#             (與 query.mjs 語意一致, 保留「精確詞命中 / 分類限定」強信號)
#   [dense]   本地多語言 embedding (fastembed · intfloat/multilingual-e5-small),
#             中英文查詢與英文 prompt 對齊到同一向量空間, 補 lexical 抓不到的轉述/跨語意圖
#   [hybrid] Reciprocal Rank Fusion (RRF, k=60) 融合兩者排名,
#             => 不劣化精確命中, 且明顯優於純 lexical 的自然語言需求描述

import json
import multiprocessing
import os
import re
import sys
import numpy as np

# Streamlit Cloud 容器環境不支援 forkserver; 強制用 spawn 避免 ConnectionResetError
try:
    multiprocessing.set_start_method('spawn')
except RuntimeError:
    pass  # 已設定過則忽略


PROMPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
INDEX_PATH = os.path.join(PROMPTS_DIR, "_search-index.json")
EMB_PATH = os.path.join(PROMPTS_DIR, "_embeddings.npy")
EMB_META_PATH = os.path.join(PROMPTS_DIR, "_embed_meta.json")
EMB_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# ---------- 中英對照詞典 (中文觸發 → 英文展開) ----------
SYN = [
    ['行銷', 'marketing'], ['营销', 'marketing'],
    ['藝術', 'art design'], ['美術', 'art design'], ['設計', 'design'],
    ['音訊', 'audio'], ['音頻', 'audio'], ['音樂', 'music'], ['播客', 'podcast'],
    ['職涯', 'careers'], ['職業', 'careers'], ['面試', 'interview'], ['履歷', 'resume'], ['薪資', 'salary'],
    ['寫程式', 'coding'], ['編程', 'coding'], ['程式碼', 'code'], ['代碼', 'code'], ['除錯', 'debug'], ['调试', 'debug'], ['重構', 'refactor'], ['測試', 'test'], ['資料庫', 'database'], ['文檔', 'documentation'],
    ['客服', 'customer service'], ['客戶服務', 'customer service'], ['投訴', 'complaint'], ['回覆', 'support reply'],
    ['數據', 'data analysis'], ['資料', 'data'], ['視覺化', 'data visualization'], ['儀表板', 'dashboard'], ['看板', 'dashboard'], ['報表', 'report'],
    ['教育', 'education'], ['課程', 'course'], ['學習指南', 'study guide'], ['教案', 'lesson plan'], ['課綱', 'lesson plan'], ['學術', 'academic'], ['測驗', 'quiz'], ['作業', 'worksheet'],
    ['財務', 'finance'], ['金融', 'finance'], ['投資', 'investing'], ['稅', 'tax'], ['報稅', 'tax'], ['預算', 'budget'], ['現金流', 'cash flow'],
    ['人資', 'human resources'], ['人力資源', 'human resources'], ['招聘', 'hiring'], ['招募', 'recruitment'], ['績效', 'performance review'],
    ['法律', 'legal'], ['合約', 'contract'], ['合同', 'contract'], ['合規', 'compliance'], ['商標', 'trademark'], ['智慧財產', 'ip'], ['智慧财产', 'ip'], ['保密協議', 'nda'],
    ['不動產', 'real estate'], ['房地產', 'real estate'], ['房產', 'real estate'], ['租賃', 'lease'], ['物業管理', 'property management'], ['房貸', 'mortgage'], ['貸款', 'mortgage'], ['清單描述', 'listing description'],
    ['研究', 'research'], ['市場調查', 'market research'], ['市場研究', 'market research'], ['競爭分析', 'competitive analysis'], ['文獻', 'literature review'], ['深度研究', 'deep research'], ['來源摘要', 'source summarization'],
    ['搜尋引擎', 'seo'], ['關鍵字', 'keyword'], ['关键词', 'keyword'], ['連結', 'link building'], ['外鏈', 'link building'],
    ['銷售', 'sales'], ['業務', 'sales'], ['提案', 'proposal'], ['簡報', 'proposal'], ['開發信', 'cold outreach'], ['異議處理', 'objection handling'],
    ['策略', 'strategy'], ['商業計畫', 'business plan'], ['商業计划', 'business plan'], ['定價', 'pricing'], ['品牌', 'brand'], ['定位', 'positioning'], ['swot', 'swot'], ['目標', 'okr goal'],
    ['影片', 'video'], ['视频', 'video'], ['腳本', 'script'], ['劇本', 'script'],
    ['寫作', 'writing'], ['部落格', 'blog'], ['博客', 'blog'], ['標題', 'headline'], ['編輯', 'editing'], ['校對', 'proofreading'], ['創意', 'creative writing'], ['文風', 'voice persona'],
    ['生產力', 'productivity'], ['效率', 'productivity'], ['目標設定', 'goal setting'], ['時間管理', 'time management'], ['腦力激盪', 'brainstorm'], ['頭腦風暴', 'brainstorm'], ['決策', 'decision making'],
    ['營運', 'operations'], ['運營', 'operations'], ['工作流程', 'workflow'], ['專案管理', 'project management'], ['sop', 'sop'], ['會議', 'meeting'], ['品質', 'quality assurance'],
    ['代理', 'ai agent'], ['智能體', 'ai agent'],
    ['現金報價', 'cash offer'], ['現金買家', 'cash offer'], ['現金出價', 'cash offer'],
    ['評估', 'evaluate'], ['分析', 'analysis'], ['審核', 'review'],
    ['文案', 'copy ad'], ['廣告詞', 'ad copy'], ['落地頁', 'landing page'], ['登陸頁', 'landing page'],
    ['電子郵件', 'email'], ['郵件', 'email'], ['電郵', 'email'],
    ['社群', 'social media'], ['社交媒體', 'social media'], ['社媒', 'social media'],
    ['圖片', 'image'], ['影像', 'image'], ['照片', 'photo'], ['標誌', 'logo'], ['角色', 'character'], ['插畫', 'illustration'], ['產品攝影', 'product photography'], ['頭像', 'avatar'], ['肖像', 'portrait'],
    ['談判', 'negotiation'],
    ['零食', 'snack'], ['廣告攝影', 'advertising photography'], ['食物攝影', 'food photography'], ['食品攝影', 'food photography'],
    ['攝影', 'photography'], ['拍攝', 'photography shoot'], ['商品照', 'product photography'], ['產品照', 'product photography'],
    ['短影音', 'short video'], ['短片', 'short video'], ['reels', 'short video'], ['tiktok', 'short video'], ['youtube', 'video'],
    ['instagram', 'social media'], ['facebook', 'social media'], ['linkedin', 'social media'],
    ['logo', 'logo brand'], ['商標設計', 'logo brand'], ['品牌識別', 'brand identity'],
    ['包裝', 'packaging'], ['海報', 'poster'], ['橫幅', 'banner'], ['廣告圖', 'ad creative'],
]

# ---------- 英文同義詞擴展 (英文查詢子串觸發) ----------
EN_SYN = [
    ['writ', ['draft', 'compose', 'author', 'copy', 'content', 'craft']],
    ['improv', ['optimize', 'enhance', 'refine', 'boost', 'polish', 'upgrade']],
    ['summar', ['summary', 'condense', 'recap', 'abstract']],
    ['creat', ['generate', 'make', 'build', 'produce', 'design']],
    ['plan', ['strategy', 'roadmap', 'blueprint', 'framework']],
    ['email', ['newsletter', 'message', 'outreach', 'sequence']],
    ['ad', ['advertisement', 'advertising', 'promo', 'promotion']],
    ['social', ['instagram', 'facebook', 'linkedin', 'tiktok', 'engagement']],
    ['blog', ['article', 'post', 'editorial']],
    ['seo', ['search engine', 'ranking', 'keyword', 'organic']],
    ['analy', ['analyze', 'analysis', 'breakdown', 'diagnose']],
    ['design', ['layout', 'wireframe', 'ui', 'ux']],
    ['code', ['script', 'program', 'function', 'develop']],
    ['review', ['feedback', 'critique', 'audit', 'evaluate']],
    ['translat', ['localize', 'language', 'multilingual']],
    ['compar', ['contrast', 'versus', 'difference']],
    ['explain', ['clarify', 'describe', 'illustrate']],
    ['learn', ['study', 'tutorial', 'guide']],
    ['brainstorm', ['ideas', 'ideation', 'options']],
    ['negoti', ['bargain', 'deal', 'persuasion']],
    ['photograph', ['photo', 'image', 'shoot', 'camera']],
    ['snack', ['food', 'chip', 'candy', 'beverage', 'packaged']],
    ['landing', ['page', 'conversion', 'funnel', 'cta']],
    ['persona', ['voice', 'tone', 'character', 'personality']],
    ['script', ['screenplay', 'dialogue', 'video']],
]

FIELDS = [('title', 5), ('keywords', 4), ('category', 3), ('subcategory', 3), ('perfect_for', 2), ('snippet', 1)]


def base_tok(s):
    return [t for t in re.split(r"\s+", re.sub(r"[^a-z0-9一-鿿\s]", " ", (s or "").lower()).replace("&", " ").replace("_", " ").replace("/", " ")) if len(t) >= 2]


def expand_query(ql):
    en_terms = []
    for zh, en in SYN:
        if zh in ql:
            en_terms += en.split()
    for trig, syns in EN_SYN:
        if trig in ql:
            en_terms += syns
    qt = set(base_tok(ql))
    for e in en_terms:
        qt.add(e)
    zh = "".join(re.findall(r"[一-鿿]", ql))
    bigrams = set(zh[i:i + 2] for i in range(len(zh) - 1))
    return qt, bigrams, sorted(set(en_terms))


def lexical_score(e, ql, qt, bigrams):
    s = 0
    reasons = set()
    fv = {
        'title': (e.get('title') or '').lower(),
        'keywords': ((" ".join(e['keywords']) if isinstance(e.get('keywords'), list) else (e.get('keywords') or ''))).lower(),
        'category': (e.get('category') or '').lower(),
        'subcategory': (e.get('subcategory') or '').lower(),
        'perfect_for': (e.get('perfect_for') or '').lower(),
        'snippet': (e.get('snippet') or '').lower(),
    }
    if fv['title'].find(ql) >= 0:
        s += 12; reasons.add('標題整句命中')
    if fv['snippet'].find(ql) >= 0:
        s += 4; reasons.add('內文整句命中')
    for fname, w in FIELDS:
        text = fv[fname]
        if not text:
            continue
        for qtok in qt:
            if qtok and qtok in text:
                s += w
                reasons.add(f"{fname} 含「{qtok}」")
        if fname == 'snippet':
            for qtok in qt:
                if qtok:
                    cnt = text.count(qtok)
                    if cnt > 1:
                        s += min(cnt, 3)
    for bg in bigrams:
        if bg and (bg in fv['title'] or bg in fv['snippet']):
            s += 2; reasons.add(f"中文詞「{bg}」")
    return s, reasons


def doc_text(e):
    parts = [e.get('title') or '',
             " ".join(e['keywords']) if isinstance(e.get('keywords'), list) else (e.get('keywords') or ''),
             e.get('category') or '', e.get('subcategory') or '', e.get('perfect_for') or '', e.get('snippet') or '']
    return " . ".join(p for p in parts if p)


def read_content(rel_path):
    fp = os.path.join(PROMPTS_DIR, rel_path)
    if not os.path.exists(fp):
        return ''
    t = open(fp, encoding='utf-8').read()
    i = t.find('## Prompt')
    return t[i:] if i >= 0 else t


def load_index():
    with open(INDEX_PATH, encoding='utf-8') as f:
        return json.load(f)


def ensure_embeddings(index, verbose=True):
    """建立/載入 corpus embedding 快取。"""
    if os.path.exists(EMB_PATH) and os.path.exists(EMB_META_PATH):
        meta = json.load(open(EMB_META_PATH, encoding='utf-8'))
        if meta.get('count') == len(index):
            arr = np.load(EMB_PATH)
            if arr.shape[0] == len(index):
                if verbose:
                    print(f"[hybrid] 載入快取 embeddings: {arr.shape}", file=sys.stderr)
                return arr
    if verbose:
        print("[hybrid] 建立 embeddings 快取 (首次, 需下載模型)...", file=sys.stderr)
    from fastembed import TextEmbedding
    model = TextEmbedding(model_name=EMB_MODEL)
    texts = [doc_text(e) for e in index]
    try:
        vecs = np.vstack([np.asarray(v, dtype=np.float32) for v in model.embed(texts, batch_size=64, parallel=0)])
    except (ConnectionResetError, OSError) as exc:
        # 部分容器環境 spawn 仍會失敗, 逐條 embed 避免多進程
        if verbose:
            print(f"[hybrid] 批次 embedding 失敗 ({exc}), 回退到逐條模式...", file=sys.stderr)
        vecs_list = []
        for t in texts:
            vecs_list.append(np.asarray(next(model.embed([t])), dtype=np.float32))
        vecs = np.vstack(vecs_list)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    vecs = vecs / norms
    np.save(EMB_PATH, vecs)
    json.dump({'count': len(index), 'model': EMB_MODEL, 'dim': int(vecs.shape[1])},
              open(EMB_META_PATH, 'w', encoding='utf-8'))
    if verbose:
        print(f"[hybrid] 已建立 embeddings: {vecs.shape}", file=sys.stderr)
    return vecs


def search(query, top_n=5, cat=None, sub=None, mode='hybrid', index=None, emb=None):
    if index is None:
        index = load_index()
    ql = query.lower().strip()
    qt, bigrams, _ = expand_query(ql)

    pool = index
    if cat:
        pool = [e for e in pool if (e.get('category') or '').lower() == cat.lower()]
    if sub:
        pool = [e for e in pool if (e.get('subcategory') or '').lower() == sub.lower()]

    scored = [(i, *lexical_score(e, ql, qt, bigrams)) for i, e in enumerate(pool)]
    scored = [x for x in scored if x[1] > 0]
    scored.sort(key=lambda x: x[1], reverse=True)
    lex_rank = [i for i, _, _ in scored]

    dense_top = set()
    if mode == 'hybrid':
        if emb is None:
            emb = ensure_embeddings(index)
        from fastembed import TextEmbedding
        model = TextEmbedding(model_name=EMB_MODEL)
        qvec = np.asarray(next(model.embed([query])), dtype=np.float32)
        n = np.linalg.norm(qvec)
        if n > 0:
            qvec = qvec / n
        pool_vecs = emb[[index.index(e) for e in pool]]
        sims = pool_vecs @ qvec
        dense_rank = sorted(range(len(pool)), key=lambda k: float(sims[k]), reverse=True)
        k = 60
        rrf = {}
        for rank, gi in enumerate(lex_rank, start=1):
            rrf[gi] = rrf.get(gi, 0) + 1.0 / (k + rank)
        for rank, gi in enumerate(dense_rank, start=1):
            rrf[gi] = rrf.get(gi, 0) + 1.0 / (k + rank)
        fused = sorted(rrf.keys(), key=lambda gi: rrf[gi], reverse=True)
        final = fused[:top_n]
        dense_top = set(dense_rank[:10])
    else:
        final = lex_rank[:top_n]

    results = []
    for rank, gi in enumerate(final, start=1):
        e = pool[gi]
        lex_s = next((s for i, s, _ in scored if i == gi), 0)
        reasons = next((r for i, s, r in scored if i == gi), set())
        if mode == 'hybrid' and gi in dense_top:
            reasons = set(reasons) | {"語意相符 (embedding)"}
        results.append({
            'rank': rank,
            'score': round(float(rrf.get(gi, 0)), 3) if mode == 'hybrid' else lex_s,
            'title': e.get('title'), 'category': e.get('category'), 'subcategory': e.get('subcategory'),
            'path': e.get('path'),
            'archetype': e.get('archetype') or None,
            'related_skills': e.get('related_skills') or [],
            'reasons': sorted(reasons),
            'content': read_content(e.get('path') or '')[:6000],
        })
    return {'query': query, 'cat': cat, 'sub': sub, 'mode': mode, 'count': len(results), 'results': results}


def main():
    args = sys.argv[1:]
    json_out = False
    cat = sub = None
    top_n = 5
    mode = 'hybrid'
    qparts = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == '--json':
            json_out = True
        elif a == '--cat':
            cat = args[i + 1]; i += 1
        elif a == '--sub':
            sub = args[i + 1]; i += 1
        elif a == '--topN':
            top_n = int(args[i + 1]); i += 1
        elif a == '--mode':
            mode = args[i + 1]; i += 1
        elif a == '--build':
            ensure_embeddings(load_index()); return
        elif a.startswith('--'):
            pass
        else:
            qparts.append(a)
        i += 1
    q = " ".join(qparts).strip()
    if not q:
        print("用法: python hybrid_search.py --json \"需求描述\" [--topN 5] [--cat X] [--sub Y] [--mode hybrid|lexical]")
        return
    res = search(q, top_n, cat, sub, mode)
    if json_out:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"查詢: {q}  (mode={mode}, 範圍: {cat or '全部'}{('/ '+sub) if sub else ''})")
        print(f"找到 {res['count']} 筆:\n")
        for r in res['results']:
            print(f"{r['rank']}. [{r['score']}] {r['title']}")
            print(f"   {r['category']} / {r['subcategory']}  -> {r['path']}")
            print(f"   理由: {'; '.join(r['reasons'])}")
            print()


if __name__ == '__main__':
    main()
