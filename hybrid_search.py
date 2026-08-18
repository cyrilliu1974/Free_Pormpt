# hybrid_search.py — 本地 hybrid 檢索 (lexical + dense embedding, txtai 風格融合)
# 純本地、免 LLM API。供 Streamlit 與 CLI 共用。
#
# 用法 / Usage:
#   python hybrid_search.py --json "你的需求描述" [--topN 5] [--cat Marketing] [--sub "Landing Page Copy"] [--mode hybrid|lexical] [--fusion rrf|convex]
#   python hybrid_search.py --build            # 強制重建 corpus embedding 快取
#
# 檢索組成 (融合方式參考 txtai: neuml/txtai hybrid 引擎):
#   [lexical] 欄位加權 TF + 中文 CN→EN 展開 + 英文同義擴展 + 中文 bigram
#             (與 query.mjs 語意一致, 保留「精確詞命中 / 分類限定」強信號)
#   [dense]   本地多語言 embedding (fastembed · paraphrase-multilingual-MiniLM-L12-v2),
#             中英文查詢與英文 prompt 對齊到同一向量空間, 補 lexical 抓不到的轉述/跨語意圖;
#             向量表示納入 title/keywords + snippet + ## Prompt 正文前 N 字元
#   [hybrid] 兩條流 (sparse 詞彙 / dense 向量) 各取 limit*MULT 候選後融合, 候選取聯集:
#     - 預設 RRF (reciprocal rank fusion): final = Σ (1/(rank+1))·weight, 只看排名不受分數尺度影響
#       (本機 lexical 是未校準原始分數, RRF 最穩健; 權重 = [bias, 1-bias])
#     - 可切 convex: sparse min-max 正規化到 [0,1] + dense cosine 做凸組合 (需已校準分數, 如 BM25F)
#     => 不劣化精確命中, 且明顯優於純 lexical 的自然語言需求描述

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
EMB_VERSION = 2                  # 遞增以強制重建 embedding 快取 (doc_text 改動 / 模型更換時)
EMB_DOC_BODY_CHARS = 1000        # dense 表示額外納入 ## Prompt 正文前 N 字元, 改善「格式/約束」類召回

# —— Hybrid 融合參數 (參考 txtai: neuml/txtai hybrid 引擎) ——
# txtai 依 sparse 分數是否已正規化選擇融合法: normalized→convex, 否則→RRF (rank-based)。
# 本機 lexical 是未校準的原始欄位加權分數, 故預設用 RRF (只看排名、不受分數尺度影響, 最穩健);
# 若日後換成 BM25F 並有可靠正規化, 可切到 convex。
#   RRF:     final = Σ (1/(rank+1)) * weight, 兩流聯集, 權重 = [bias, 1-bias]
#   convex:  sparse 做 min-max 正規化到 [0,1] + dense cosine, 凸組合 (需已校準分數)
HYBRID_FUSION = "rrf"            # "rrf" (預設) | "convex"
HYBRID_BIAS = 0.5                # dense 權重; sparse 權重 = 1 - HYBRID_BIAS。調大→更偏語意, 調小→更偏關鍵字。
                                 # 預設 0.5 (經 benchmark.py 在 111 題種子集量測, 該集依 skills.json 隨機抽取
                                 # 技能並連到 prompt 類別生成, 中英文混合, 覆蓋 15+ 大類):
                                 #   rrf bias=0.5 → MRR@5=0.947 / nDCG@5=0.932 / 命中率@5=97.3% (全組最佳);
                                 #   優於 bias=0.3 (95.5%) 與 0.1 (89.2%), 也優於 convex 各檔;
                                 #   且對房地產/寫詩/廣告圖查詢仍不引入離題 (已逐項驗證)。
HYBRID_TOPK_MULT = 10            # 每條流先各取 limit*MULT 候選再融合 (同 txtai, 控制融合規模與耗時)

# —— 模型與索引快取 (避免每次查詢重建 TextEmbedding / 避免內容變動卻沿用舊向量) ——
_EMB_MODEL_CACHE = None

def _get_embed_model():
    global _EMB_MODEL_CACHE
    if _EMB_MODEL_CACHE is None:
        from fastembed import TextEmbedding
        _EMB_MODEL_CACHE = TextEmbedding(model_name=EMB_MODEL)
    return _EMB_MODEL_CACHE

def _index_md5():
    import hashlib
    h = hashlib.md5()
    with open(INDEX_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

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


def _prompt_body(rel_path, max_chars=EMB_DOC_BODY_CHARS):
    """取 ## Prompt 正文前 N 字元 (略過 Role 樣板首句), 用於 enrich dense 表示。"""
    t = read_content(rel_path)
    if not t:
        return ''
    nl = t.find('\n')
    body = t[nl + 1:].strip() if nl >= 0 else t.strip()
    low = body[:200].lower()
    if low.startswith('you are a') or low.startswith('you are an'):
        dot = body.find('. ')
        if dot > 0:
            body = body[dot + 2:].strip()
    return body[:max_chars]


def doc_text(e):
    parts = [e.get('title') or '',
             " ".join(e['keywords']) if isinstance(e.get('keywords'), list) else (e.get('keywords') or ''),
             e.get('category') or '', e.get('subcategory') or '', e.get('perfect_for') or '', e.get('snippet') or '']
    body = _prompt_body(e.get('path') or '')
    if body:
        parts.append(body)
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
    """建立/載入 corpus embedding 快取 (依 count + version + 索引指紋判斷是否需要重建)。"""
    if os.path.exists(EMB_PATH) and os.path.exists(EMB_META_PATH):
        meta = json.load(open(EMB_META_PATH, encoding='utf-8'))
        if (meta.get('count') == len(index) and meta.get('version') == EMB_VERSION
                and meta.get('index_md5') == _index_md5()):
            arr = np.load(EMB_PATH)
            if arr.shape[0] == len(index):
                if verbose:
                    print(f"[hybrid] 載入快取 embeddings: {arr.shape}", file=sys.stderr)
                return arr
    if verbose:
        print("[hybrid] 建立 embeddings 快取 (首次/失效, 需模型)...", file=sys.stderr)
    model = _get_embed_model()
    texts = [doc_text(e) for e in index]
    try:
        # parallel=None -> fastembed 走主行程單執行緒 (不開多進程)。
        # 注意: 不能用 parallel=0 —— fastembed 0.8.0 會把 0 解讀成 "用全部 CPU" 而 spawn 子進程,
        # 在 Streamlit/scripts 環境下子進程會以 forkserver 重新 import 本模組, 造成遞迴 bootstrap 崩潰。
        vecs = np.vstack([np.asarray(v, dtype=np.float32) for v in model.embed(texts, batch_size=64, parallel=None)])
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
    json.dump({'count': len(index), 'version': EMB_VERSION, 'model': EMB_MODEL,
               'dim': int(vecs.shape[1]), 'index_md5': _index_md5()},
              open(EMB_META_PATH, 'w', encoding='utf-8'))
    if verbose:
        print(f"[hybrid] 已建立 embeddings: {vecs.shape}", file=sys.stderr)
    return vecs


def _fuse(scored, dense_sorted, sims, bias, method):
    """融合 sparse(詞彙) 與 dense(向量) 兩流, 返回 {pool_local_idx: score}。"""
    w_dense, w_sparse = bias, 1.0 - bias
    fused = {}
    if method == 'convex':
        if scored:
            svals = [s for _, s, _ in scored]
            smin, smax = min(svals), max(svals)
            srange = (smax - smin)
            sparse_norm = {i: ((s - smin) / srange if srange else (1.0 if s > 0 else 0.0))
                           for i, s, _ in scored}
        else:
            sparse_norm = {}
        dense_norm = {gi: float(sims[gi]) for gi in dense_sorted}
        for gi in set(sparse_norm) | set(dense_norm):
            fused[gi] = w_dense * dense_norm.get(gi, 0.0) + w_sparse * sparse_norm.get(gi, 0.0)
    else:  # rrf (default)
        sparse_rank = {i: r + 1 for r, (i, _, _) in enumerate(scored)}
        dense_rank = {gi: r + 1 for r, gi in enumerate(dense_sorted)}
        for gi in set(sparse_rank) | set(dense_rank):
            sc = w_sparse / sparse_rank[gi] if gi in sparse_rank else 0.0
            dc = w_dense / dense_rank[gi] if gi in dense_rank else 0.0
            fused[gi] = sc + dc
    return fused


def search(query, top_n=5, cat=None, sub=None, mode='hybrid', index=None, emb=None, fusion=None):
    if index is None:
        index = load_index()
    ql = query.lower().strip()
    qt, bigrams, _ = expand_query(ql)

    pool, pool_rows = [], []
    for i, e in enumerate(index):
        if cat and (e.get('category') or '').lower() != cat.lower():
            continue
        if sub and (e.get('subcategory') or '').lower() != sub.lower():
            continue
        pool.append(e)
        pool_rows.append(i)

    # —— 瀏覽模式: 顯示所選 (大類/類別) 底下的「全部」prompt, 不排序/不檢索 ——
    if mode == 'all':
        pool_sorted = sorted(pool, key=lambda e: (e.get('title') or '').lower())
        results = []
        for rank, e in enumerate(pool_sorted, start=1):
            results.append({
                'rank': rank, 'score': 0,
                'title': e.get('title'), 'category': e.get('category'),
                'subcategory': e.get('subcategory'), 'path': e.get('path'),
                'archetype': e.get('archetype') or None,
                'related_skills': e.get('related_skills') or [],
                'reasons': set(),
                'content': read_content(e.get('path') or '')[:6000],
            })
        return {'query': query, 'cat': cat, 'sub': sub, 'mode': mode, 'count': len(results), 'results': results}

    scored = [(i, *lexical_score(e, ql, qt, bigrams)) for i, e in enumerate(pool)]
    scored = [x for x in scored if x[1] > 0]
    scored.sort(key=lambda x: x[1], reverse=True)
    # sparse 流截斷 (同 txtai: 每流各取 limit*MULT 候選再融合, 讓行為/耗時更穩定)
    sparse_topk = max(top_n * HYBRID_TOPK_MULT, top_n)
    scored = scored[:sparse_topk]
    lex_rank = [i for i, _, _ in scored]

    dense_top = set()
    if mode == 'hybrid':
        if emb is None:
            emb = ensure_embeddings(index)
        model = _get_embed_model()
        qvec = np.asarray(next(model.embed([query])), dtype=np.float32)
        n = np.linalg.norm(qvec)
        if n > 0:
            qvec = qvec / n
        pool_vecs = emb[pool_rows]
        sims = pool_vecs @ qvec
        sims = np.clip(sims, 0.0, 1.0)  # 單位向量 cosine ∈ [-1,1]; 裁掉微小負值, 使 dense 分數落在 [0,1]

        # dense 流取前 limit*MULT 候選 (用 argpartition, O(N) 不排序全庫)
        dense_topk = max(top_n * HYBRID_TOPK_MULT, top_n)
        k = min(dense_topk, len(pool))
        if k > 0:
            part = np.argpartition(-sims, k - 1)[:k]
            dense_sorted = sorted(part.tolist(), key=lambda gi: float(sims[gi]), reverse=True)
        else:
            dense_sorted = []
        dense_set = set(dense_sorted)

        fused = _fuse(scored, dense_sorted, sims, HYBRID_BIAS, fusion or HYBRID_FUSION)
        final = sorted(fused.keys(), key=lambda gi: fused[gi], reverse=True)[:top_n]
        # 標記「有 dense 貢獻」的結果 (用於理由註記): 該文件確實出現在 dense 候選中
        dense_top = {gi for gi in final if gi in dense_set}
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
            'score': round(float(fused.get(gi, 0)), 3) if mode == 'hybrid' else lex_s,
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
    fusion = None
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
        elif a == '--fusion':
            fusion = args[i + 1]; i += 1
        elif a == '--build':
            ensure_embeddings(load_index()); return
        elif a.startswith('--'):
            pass
        else:
            qparts.append(a)
        i += 1
    q = " ".join(qparts).strip()
    if not q:
        print("用法: python hybrid_search.py --json \"需求描述\" [--topN 5] [--cat X] [--sub Y] [--mode hybrid|lexical] [--fusion rrf|convex]")
        return
    res = search(q, top_n, cat, sub, mode, fusion=fusion)
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
