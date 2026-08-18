# benchmark.py — relevance 基準 (擴充版, 依 skills.json 隨機生成)
# 量測 lexical / RRF / convex 與不同 dense 權重在「分類層級相關性」上的 MRR@5 / nDCG@5 / 命中率@5。
#
# 用法: python benchmark.py
# 說明:
#   - QUERIES 為擴充種子集: 原 18 題真實需求 + 依 skills.json 隨機抽取技能、再連到 _search-index.json
#     的 related_skills, 取得「該技能真正對應的 prompt 類別」作為可接受的 rels (category-level proxy)。
#     共 78 題 (中英文混合), 覆蓋 21 大類中 15+ 類, 用於比較各檢索策略的相對好壞。
#   - 相關性以「結果的 category 是否落在 rels」做二元判定, 僅用於比較策略, 非精確到單一 prompt 人工標註。
#   - 結果印出每個方法的 MRR@5 / nDCG@5 / 命中率@5 (top5 內至少有一筆相關)。

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hybrid_search as hs

# (查詢, [可接受的類別]) — 78 題, 中英文混合, 多數錨定 skills.json 技能及其對應 prompt 類別
QUERIES = [
    # ===== 原 18 題核心種子 (已驗證) =====
    ("評估房地產現金買家報價是否可靠", ["Real Estate"]),
    ("幫我寫一首關於秋天的詩", ["Writing", "Audio"]),
    ("設計一個產品攝影的廣告圖", ["Art and Design"]),
    ("寫一封英文冷開發信給潛在客戶", ["Sales"]),
    ("做 SEO 關鍵字研究與排名規劃", ["SEO"]),
    ("寫 landing page 的轉換文案", ["Marketing"]),
    ("準備軟體工程師行為面試題", ["Careers"]),
    ("設計國小數學教案與學習單", ["Education"]),
    ("審閱一份租約並標出風險條款", ["Legal"]),
    ("寫一支 60 秒短影音腳本", ["Video"]),
    ("幫我做個人月預算表與現金流規劃", ["Finance"]),
    ("客服退回商品的投訴處理回覆", ["Customer Service"]),
    ("設計一個 AI agent 的工作流", ["AI Agents"]),
    ("想一句品牌 slogan 與命名建議", ["Marketing"]),
    ("把這份銷售數據做成視覺化儀表板", ["Data Analysis"]),
    ("幫我寫績效考核面談的問題", ["Human Resources"]),
    ("研究競品並產出競爭分析報告", ["Research", "Strategy"]),
    ("寫一篇部落格文章大綱", ["Writing"]),

    # ===== 依 skills.json 隨機抽取技能, 連到 related_skills 取得對應 prompt 類別 (新增 60 題) =====
    # — Real Estate —
    ("幫我評估房貸借款人的信用狀況是否可靠", ["Real Estate"]),
    ("我想做不動產賣家名單的分群與開發", ["Real Estate"]),
    ("起草法律要求的產權揭露聲明書", ["Legal"]),
    # — Marketing / Strategy —
    ("我想做社群個人品牌經營策略", ["Marketing"]),
    ("生成一個學生成功故事的社群行銷貼文", ["Marketing"]),
    ("設計一個產品本地化進軍全球市場的策略", ["Strategy"]),
    ("幫我寫一份組織的法規合規風險評估", ["Legal"]),
    # — Human Resources / Careers —
    ("幫人資建立溝通培訓課程", ["Human Resources"]),
    ("寫一份職涯學習策略報告", ["Careers"]),
    ("教我面試準備, 作為職涯教練", ["Careers"]),
    ("用職涯探索測驗幫我找到適合的方向", ["Careers"]),
    ("生成一份帶有職涯行動計畫的 LinkedIn 履歷教練建議", ["Careers"]),
    ("建立營運團隊的任務交接準則", ["Operations"]),
    # — Finance —
    ("規劃企業短期融資的現金流方案", ["Finance"]),
    ("建立五年財務預測模型", ["Finance"]),
    # — Art and Design (量大, 多技能) —
    ("設計一個美術風格的奢華汽車廣告圖", ["Art and Design"]),
    ("做一個美術風格的 2D 扁平網頁橫幅", ["Art and Design"]),
    ("設計一個美術風格的 NFT 角色生物", ["Art and Design"]),
    ("生成美術風格的電影感肖像光影提示", ["Art and Design"]),
    ("建立美術風格的等距奇幻村莊圖像", ["Art and Design"]),
    ("生成美術風格的超現實漂浮球體藝術", ["Art and Design"]),
    ("設計一個 3D 金屬別針產品卡片", ["Art and Design"]),
    ("做一個美術風格的街頭藝術模板壁畫", ["Art and Design"]),
    ("建立一個飯店預訂 App 的介面模型", ["Art and Design"]),
    ("設計一個當代 spa 室內空間", ["Art and Design"]),
    ("生成超寫實冰淇淋食物攝影提示", ["Art and Design"]),
    ("設計一個單色 3D 圖示重新貼圖", ["Art and Design"]),
    ("做一個橘色 3D 卡通圖示渲染", ["Art and Design"]),
    ("生成一張寫實動物貼紙", ["Art and Design"]),
    ("做一個動態運動裝備登陸頁圖像", ["Art and Design"]),
    # — Audio / Video —
    ("寫一系列有腳本的播客節目", ["Audio"]),
    ("寫一支產品發表會的短影音腳本", ["Video"]),
    # — Customer Service / Sales —
    ("建立客服的客戶引導清單", ["Customer Service"]),
    ("分析客服的客戶流失模式", ["Customer Service"]),
    ("寫一封銷售談判摘要的電子郵件", ["Sales"]),
    ("寫一則客服系統故障的即時聊天回應模板", ["Customer Service"]),
    # — Coding (量大) —
    ("我想用寫程式的方式設計 App 線框圖", ["Coding"]),
    ("用寫程式分析慢查詢來調校資料庫效能", ["Coding"]),
    ("用程式碼找出資料庫結構中多餘的表格", ["Coding"]),
    ("做程式碼審核與重構建議", ["Coding"]),
    ("幫學生用寫程式解釋演算法", ["Coding"]),
    ("教除錯的方法論訓練", ["Coding"]),
    ("用寫程式設定 iPhone App 專案", ["Coding"]),
    ("用寫程式建立 AI 網頁應用部署環境", ["Coding"]),
    ("用寫程式設計一個技術共同創辦人的產品開發流程", ["Coding"]),
    # — Education / Research / Writing —
    ("寫教育領域的學術研究提示", ["Education"]),
    ("產生學術研究的註釋書目", ["Education"]),
    ("寫一篇深度研究報告的文獻回顧", ["Research"]),
    ("幫我寫一首關於海洋的創意詩", ["Writing", "Audio"]),
    ("寫一封英文冷開發郵件給新的潛在客戶", ["Sales"]),
    # — AI Agents —
    ("評估 AI 代理的多場景提示工程框架", ["AI Agents"]),
    ("幫我設計一個 AI 代理人的任務分類與組裝路由", ["AI Agents"]),
    # — English variants (天然任務描述, 同樣錨定 skills.json 技能) —
    ("Help me evaluate whether a mortgage borrower's creditworthiness is reliable", ["Real Estate"]),
    ("I need a LinkedIn personal branding strategy for a solopreneur", ["Marketing"]),
    ("Draft a product localization strategy for entering global markets", ["Strategy"]),
    ("Write an ethical risk assessment for my organization's compliance program", ["Legal"]),
    ("Build a communication training program for my team", ["Human Resources"]),
    ("Generate a student success story social media post", ["Marketing"]),
    ("Segment seller leads for real estate prospecting", ["Real Estate"]),
    ("Plan short-term financing options for my business cash flow", ["Finance"]),
    ("Build a five-year financial forecast model", ["Finance"]),
    ("Design a luxury automotive campaign image", ["Art and Design"]),
    ("Make a 2D flat web banner for business ads", ["Art and Design"]),
    ("Design an NFT creature character", ["Art and Design"]),
    ("Write a podcast series with episode scripts", ["Audio"]),
    ("Build a customer onboarding checklist", ["Customer Service"]),
    ("Draft a customer outage response template for live chat", ["Customer Service"]),
    ("Write a negotiation summary email after a sales call", ["Sales"]),
    ("Design an app wireframe focused on user-centered UX", ["Coding"]),
    ("Analyze churn patterns for customer success", ["Customer Service"]),
    ("Write a career learning strategy report", ["Careers"]),
    ("Coach me on improving my LinkedIn profile with a career action plan", ["Careers"]),
    ("Prepare for a job interview as a career coach", ["Careers"]),
    ("Tune a database by analyzing slow queries and index usage", ["Coding"]),
    ("Find redundant tables in my database schema", ["Coding"]),
    ("Review code for clean code principles and logic issues", ["Coding"]),
    ("Audit code quality and suggest refactoring", ["Coding"]),
    ("Explain an algorithm to beginners and students", ["Coding"]),
    ("Teach debugging methodology", ["Coding"]),
    ("Configure iPhone app project settings", ["Coding"]),
    ("Set up an AI webapp deployment environment", ["Coding"]),
    ("Write an academic research study prompt for ChatGPT", ["Education"]),
    ("Generate an annotated bibliography for academic research", ["Education"]),
    ("Design a monochrome 3D icon retexture", ["Art and Design"]),
    ("Create an orange 3D cartoon icon render", ["Art and Design"]),
    ("Generate a photorealistic animal sticker", ["Art and Design"]),
    ("Create a hyperrealistic ice cream food photography prompt", ["Art and Design"]),
    ("Design a contemporary spa interior", ["Art and Design"]),
    ("Build task handoff guidelines for teams", ["Operations"]),
    ("Draft a property disclosure statement", ["Legal"]),
    ("Evaluate a multi-scenario prompt engineering framework", ["AI Agents"]),
    ("Create a cinematic portrait lighting prompt for Midjourney", ["Art and Design"]),
    ("Design a concept art style generator", ["Art and Design"]),
]


def evaluate(mode, fusion=None, bias=None):
    if bias is not None:
        hs.HYBRID_BIAS = bias
    mrr_sum = ndcg_sum = hit_sum = 0.0
    index = hs.load_index()
    emb = hs.ensure_embeddings(index, verbose=False)
    for q, rels in QUERIES:
        res = hs.search(q, top_n=5, mode=mode, fusion=fusion, index=index, emb=emb)
        rels_at = [1 if r["category"] in rels else 0 for r in res["results"]]
        # MRR@5
        mrr = 0.0
        for i, rel in enumerate(rels_at, start=1):
            if rel:
                mrr = 1.0 / i
                break
        # nDCG@5 (binary relevance)
        dcg = sum(rel / math.log2(i + 1) for i, rel in enumerate(rels_at, start=1))
        num_rel = sum(rels_at)
        ndcg = 0.0
        if num_rel > 0:
            idcg = sum(1.0 / math.log2(j + 1) for j in range(1, min(num_rel, 5) + 1))
            ndcg = dcg / idcg
        hit = 1.0 if num_rel > 0 else 0.0
        mrr_sum += mrr
        ndcg_sum += ndcg
        hit_sum += hit
    n = len(QUERIES)
    return mrr_sum / n, ndcg_sum / n, hit_sum / n


def main():
    print(f"基準題數: {len(QUERIES)}  (category-level 相關性 proxy, 中英文混合, 依 skills.json 生成)\n")
    rows = []
    rows.append(("lexical", evaluate("lexical")))
    for b in (0.1, 0.3, 0.5, 0.7):
        rows.append((f"rrf  (bias={b})", evaluate("hybrid", fusion="rrf", bias=b)))
    for b in (0.1, 0.3, 0.5):
        rows.append((f"convex (bias={b})", evaluate("hybrid", fusion="convex", bias=b)))

    print(f"{'方法':<18}{'MRR@5':>10}{'nDCG@5':>10}{'命中率@5':>12}")
    print("-" * 52)
    for name, (mrr, ndcg, hit) in rows:
        print(f"{name:<18}{mrr:>10.3f}{ndcg:>10.3f}{hit:>11.1%}")

    # 找出最佳 hybrid 設定 (以命中率@5 為主, 其次 MRR@5)
    best = max(rows[1:], key=lambda r: (r[1][2], r[1][0]))
    print(f"\n→ 最佳 hybrid 設定: {best[0]} (命中率@5={best[1][2]:.1%}, MRR@5={best[1][0]:.3f})")


if __name__ == "__main__":
    main()
