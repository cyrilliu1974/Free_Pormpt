# AI Prompt Library · 離線封存 + 分類索引 (v10)

<div align="right">
<strong>語言 / Language:</strong>
<button onclick="document.getElementById('zh').style.display='block';document.getElementById('en').style.display='none';">中文</button>
<button onclick="document.getElementById('zh').style.display='none';document.getElementById('en').style.display='block';">English</button>
</div>
<script>
// 同頁語言切換 (在支援 HTML/JS 的預覽器中生效; GitHub 會過濾 script, 此時中英文同時顯示)
if (typeof document !== 'undefined') { document.getElementById('en').style.display = 'none'; }
</script>

<div id="zh" class="lang">

## 這是什麼 / What this is

本 repo 是 **God of Prompt** 網站 6,000+ 筆免費 prompt 的**離線封存 + 分類索引**。全部為純本地 markdown,**不呼叫任何 LLM API**,可離線瀏覽與檢索。

### 為什麼用這個 repo / Why this repo

- 🗂️ **人工分類瀏覽**:21 大類 / 143 類別,從 `prompts/index.md` 總索引逐層鑽取。適合「還不知道自己要什麼、想逛」的人。
- 🔎 **關鍵字搜尋**:支援中文(自動 CN→EN 展開)與英文,採 **詞彙 + 同義擴展 + 欄位加權**;還可疊加 **本地多語言 embedding + txtai 風格凸組合混合檢索**,對自然語言需求描述最準。
- 📦 **數量龐大**:實際封存 **6,398 個 prompt**,橫跨行銷 / 寫作 / 程式 / 法務 / 財務 / 不動產 / 教育 / 人資 / 研究 / 影片… **涵蓋面極廣**。
- 💡 **每個 prompt 都可直接貼進 LLM 使用**,並附 `## 用法 / Usage`(必填變數 + 建議搭配技能 + 適用場景)。

> 小提醒:在 GitHub 上 `<script>` 會被過濾,此時中英文會同時顯示;在支援 HTML 的預覽器(本 App / VS Code Preview / 瀏覽器)中可用上方按鈕切換。

## 結構

```
本資料夾/
├── README.md                       # 本檔 (含 Changelog)
├── prompts/                        # 分類後的 prompt 庫
│   ├── index.md                    # ★ 分類總索引 (21 大類一覽 + 查詢用法)
│   ├── _search-index.json          # ★ 查詢用搜尋索引 (hybrid_search.py 讀取)
│   ├── _embeddings.npy             # ★ corpus embedding 快取 (hybrid 模式用, 自動建立)
│   ├── _embed_meta.json            # embedding 快取中繼資訊
│   ├── <大類>/                      # 例如 Real Estate / Marketing / Coding ...
│   │   ├── index.md                # 該大類的類別一覽
│   │   └── <類別>/                  # 例如 Deal Analysis / Landing Page Copy ...
│   │       ├── index.md            # ★ 該類別: 所屬 prompt 清單 + 一個完整 prompt 範例
│   │       └── <slug>.md           # 單一 prompt
│   └── ...
├── hybrid_search.py                # 本地 hybrid 檢索 (lexical + dense, txtai 風格凸組合融合), 純 Python
├── streamlit_app.py                # 雙語 Web 檢索介面 (lexical / hybrid)
└── prompts_pre-vN-backup/          # 各版整樹備份 (可還原)
```

## 數量與分類

- **實際封存:6,398 個 prompt**
- 分類架構:**21 大類 / 143 類別**(由資料 frontmatter 的 `category` / `subcategory` 驅動,非硬編碼)
  - 21 大類:AI Agents · Art and Design · Audio · Careers · Coding · Customer Service · Data Analysis · Education · Finance · Human Resources · Legal · Marketing · Operations · Productivity · Real Estate · Research · SEO · Sales · Strategy · Video · Writing
  - 較大類別舉例:Marketing(701) · Art and Design(808) · SEO(512) · Coding(497) · Strategy(444) · Productivity(379) · Operations(376) · Writing(359) · Education(436) · Human Resources(334) · Research(279) · Finance(295) · Legal(216)
- 分類層級說明:更深層(第三層)可再以 `keywords` 做主題細分,後續可再擴充。

## 單一 prompt 的 markdown 結構

```markdown
# <標題>

## 簡介
(行銷說明、適用場景)

## Prompt
(實際可貼到 LLM 的 prompt 文字, 從 "## Role ..." 開頭, 含 {{變數}})

## 重點特色
- (以 ● 開頭的 bullet list)

## 用法 / Usage        
- 必填變數 / Variables: {{topic-and-subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill (細節請提出客製化需求): Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: <一句適用場景>
```

## 索引系統

每個類別目錄都有 `index.md`,內含:
1. **類別名稱**(大類 / 類別)
2. **所屬 prompt 清單**(表格: 編號 · Prompt 名稱 · 適用對象 · 檔案連結)
3. **一個 prompt 範例**(該類別第一筆的完整 `## Prompt` 內容, 已解碼 HTML 實體, 可直接複製)

頂層 `prompts/index.md` 為總索引:列出 21 大類、各類別數與 prompt 數,並說明查詢用法。

## 查詢機制 (依需求找出 prompt)

**方式 A — 命令行 (純詞彙 lexical):**
```bash
node query.mjs "<你的需求描述>" [topN]
node query.mjs --json "<需求>" [topN]          # 機器可讀 JSON
node query.mjs --cat "Marketing" --sub "Landing Page Copy" "<需求>" [topN]   # 限定類別
```
- 支援**中文查詢**:內建中英對照詞典,會把「房地產 / 現金報價 / 落地頁 / 文案 / 客服 ...」自動展開為英文 token 再比對。
- 評分依據(欄位加權):標題 / 關鍵字 / 大類 / 類別 / 適用對象 / 內文簡介。
- 例:`node query.mjs "我想評估房地產現金買家報價是否可靠"` → 命中 `Real Estate/Deal Analysis/evaluate-cash-offers.md`

**方式 B — Web 介面 (lexical / hybrid, 推薦):**
```bash
streamlit run streamlit_app.py --server.port 8501 --server.headless true
```
- 中英雙語、上層→下層分類連動下拉、選定類別限定範圍(未選則全域)。
- **檢索模式**:`混合 Hybrid`(lexical + 本地多語言 embedding, txtai 風格 RRF/凸組合融合, 對自然語言最準) 或 `詞彙 Lexical`(純關鍵字/同義/欄位加權)。
- 純本地,不呼叫 LLM API。首次執行 hybrid 會自動下載多語言模型並建立 `_embeddings.npy` 快取(之後只讀)。

> 若需要針對特定場景**建議搭配技能**，請另外提出**客製化諮詢**。

</div>

<div id="en" class="lang">

## What this is

This repo is an **offline archive + categorized index** of 6,000+ free prompts from **God of Prompt**. Everything is plain local markdown, **no LLM API calls** — browse and search fully offline.

### Why this repo

- 🗂️ **Manual category browsing**: 21 top categories / 143 subcategories, drill down from the `prompts/index.md` master index. Great when you "don't yet know what you want and just want to explore."
- 🔎 **Keyword search**: supports Chinese (auto CN→EN expansion) and English, using **lexical + synonym expansion + field weighting**; can be upgraded to **local multilingual embedding + txtai-style convex-combination hybrid retrieval** for the most accurate natural-language queries.
- 📦 **Huge volume**: **6,398 prompts** archived, spanning Marketing / Writing / Coding / Legal / Finance / Real Estate / Education / HR / Research / Video … **extremely broad coverage**.
- 💡 **Every prompt is paste-ready into an LLM**, and ships with a `## 用法 / Usage` block (required variables + suggested skill + when-to-use).

> Note: on GitHub the `<script>` is stripped, so both languages show at once; in HTML-capable previewers (this App / VS Code Preview / browser) use the buttons above to switch.

## Structure

```
repo/
├── README.md                       # this file (Changelog included)
├── prompts/                        # categorized prompt library
│   ├── index.md                    # ★ master index (21 categories + how to query)
│   ├── _search-index.json          # ★ search index (read by hybrid_search.py)
│   ├── _embeddings.npy             # ★ corpus embedding cache (hybrid mode, auto-built)
│   ├── _embed_meta.json            # embedding cache metadata
│   ├── <category>/                 # e.g. Real Estate / Marketing / Coding ...
│   │   ├── index.md                # category overview
│   │   └── <subcategory>/          # e.g. Deal Analysis / Landing Page Copy ...
│   │       ├── index.md            # ★ prompt list + one full example
│   │       └── <slug>.md           # single prompt
├── hybrid_search.py                # local hybrid retriever (lexical + dense, txtai-style convex-combination fusion), pure Python
├── streamlit_app.py                # bilingual web UI (lexical / hybrid)
```

## Volume & taxonomy

- **Archived: 6,398 prompts** 
- Taxonomy: **21 top categories / 143 subcategories** (driven by each item's `category` / `subcategory`, not hard-coded)
  - 21 top categories: AI Agents · Art and Design · Audio · Careers · Coding · Customer Service · Data Analysis · Education · Finance · Human Resources · Legal · Marketing · Operations · Productivity · Real Estate · Research · SEO · Sales · Strategy · Video · Writing
  - Larger examples: Marketing (701) · Art and Design (808) · SEO (512) · Coding (497) · Strategy (444) · Productivity (379) · Operations (376) · Writing (359) · Education (436) · Human Resources (334) · Research (279) · Finance (295) · Legal (216)

## Single-prompt markdown structure

```markdown
# <title>

## 簡介 / Intro
(marketing blurb, use case)

## Prompt
(the actual LLM-pasteable prompt, starting with "## Role ...", with {{variables}})

## 重點特色 / Highlights
- (● bullets)

## 用法 / Usage          
- 必填變數 / Variables: {{topic-and-subject}} — fill before running
- 建議搭配技能 / Pair with skill (details — submit a custom request): Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: <one-line use case>
```

## Index system

Every subcategory folder has an `index.md` with: (1) category name, (2) prompt list table (no. · name · audience · file link), (3) one full `## Prompt` example (HTML entities decoded, copy-ready). The top-level `prompts/index.md` is the master index.

## Query mechanism (find a prompt by need)

**Option A — CLI (lexical only):**
```bash
node query.mjs "<your need>" [topN]
node query.mjs --json "<need>" [topN]          # machine-readable JSON
node query.mjs --cat "Marketing" --sub "Landing Page Copy" "<need>" [topN]
```
- Chinese queries auto-expand to English tokens via a built-in CN→EN dictionary.
- Field-weighted scoring: title / keywords / category / subcategory / audience / snippet.
- e.g. `node query.mjs "evaluate if a real-estate cash buyer offer is reliable"` → `Real Estate/Deal Analysis/evaluate-cash-offers.md`

**Option B — Web UI (lexical / hybrid, recommended):**
```bash
streamlit run streamlit_app.py --server.port 8501 --server.headless true
```
- Bilingual, cascading category dropdowns, optional category scoping (global if none).
- **Retrieval mode**: `混合 Hybrid` (lexical + local multilingual embedding, txtai-style RRF/convex-combination fusion — best for natural language) or `詞彙 Lexical` (pure keyword/synonym/field-weighted).
- Fully local, no LLM API. First hybrid run auto-downloads a multilingual model and builds `_embeddings.npy` (cached afterwards).

> **Need tailored skill recommendations?** Some prompts ship with `Pair with skill` hints, but choosing the right skill for a specific use case requires tailored consulting — please submit a separate request. / 本庫 prompt 末尾所附「建議搭配技能」僅供參考，**若需要針對特定場景建議搭配技能，請另外提出客製化諮詢**。

</div>

## Changelog (中文)

- 2026-08-18 v1 — 初次全量封存。透過 sitemap 取得 6,830 URL, Node 並行抓取,Parser 從 `<pre><code>` 抽出真實 prompt,寫成 markdown。
- 2026-08-18 v2 — 分類與索引查詢版。全域掃描 6,398 個 prompt 的 frontmatter,建立 **21 大類 / 143 類別** 多階層檔案系統;每層產生 `index.md`;全站解碼 HTML 實體;新增 `query.mjs` 索引查詢(支援中文)。備份:本檔 v1 → `README.md.v1.bak`。
- 2026-08-18 v3 — 移除全部 prompt md 開頭的 YAML frontmatter。備份:整樹 → `prompts_pre-v3-backup/`。
- 2026-08-18 v4 — 保護 `## Prompt` 本體不被更動,僅清理 `## 簡介` / `## 重點特色` 行銷描述與品牌字樣。備份:整樹 → `prompts_pre-v4-backup/`。
- 2026-08-18 v5 — 框架型態分析 + skills.json 交叉參照 + 檢索重寫(詞彙+同義/中英擴展) + Streamlit Web 介面。備份:本檔 → `README.md.v4.bak`。
- 2026-08-18 v6 — 依 skills.json 高標增強 prompt 內容(追加 `## 框架型態` / `## 品質增強建議`) + GitHub 同類庫調研。備份:本檔 → `README.md.v5.bak`。
- 2026-08-18 v7 — **清理 + 重做,並補上本地 hybrid 檢索**:
  - **md 內容微調 (依 skills.json, 移除裝飾性垃圾)**: 遍歷 6,398 個 prompt md,刪除 `## 框架型態` 與 `## 品質增強建議` 兩個對 LLM 執行無幫助的裝飾區塊;改為單一精簡 `## 用法 / Usage`(必填變數 + 頂部相關技能 skills.json + 一句適用場景),保留 `## Prompt` 本體不動。腳本 `C:\Users\cyril\.workbuddy-ai\tune_md.py`;備份整樹 → `prompts_pre-v7-backup/`。
  - **本地 embedding 的 hybrid 檢索 (真正能跑)**: 舊 `query.mjs` 雖寫了 hybrid 程式碼,但指向**沒有索引的 `Skills_Library` 副本**、缺 `build-embeddings.mjs`、且未裝模型,實際從未跑起來。本版改用純 Python 重做一套能跑的: `hybrid_search.py` = 欄位加權詞彙 (lexical) **+** 本地多語言 embedding (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, 經 fastembed) **+** Reciprocal Rank Fusion (RRF, k=60)。優於純 lexical 之處:補上「轉述 / 意圖相同但無共享詞 / 中英跨語」查詢,且因 RRF 同時保留 lexical 強信號,**不會比現有搜尋差**。corpus embedding 首次自動建立並快取為 `_embeddings.npy`(之後只讀)。
  - **修正檢索資料路徑 (讓 streamlit 能跑)**: `query.mjs` 與 `streamlit_app.py` 原本 `BASE`/`PROMPTS_DIR` 都指向 `C:\AI\Skills_Library\input\...\God of Prompt_files`(該副本無 `_search-index.json`),導致兩者皆壞;現統一指向真正有索引的 `C:\AI\Free_Pormpt\prompts`。`streamlit_app.py` 改呼叫 `hybrid_search.py`,並新增 **檢索模式切換 (混合 Hybrid / 詞彙 Lexical, 預設 Hybrid)**。
  - **README 中英雙語 (同頁切換)**: 本頁新增中/英版與語言切換按鈕,特別強調「人工分類瀏覽 + 關鍵字搜尋(詞彙+同義擴展+欄位加權,可疊加 hybrid) + 6,398 個 prompt + 涵蓋極廣」;Changelog 維持中文。備份:本檔 → `README.md.v6.bak`。

- 2026-08-18 部署修正 — 修復 Streamlit Cloud 啟動崩潰 (`RuntimeError: ... start a new process before ... bootstrapping phase` + `NoSessionContext: Cursor is not set`):
  - **根因**: `hybrid_search.py` 對 6,398 筆 corpus 呼叫 `model.embed(texts, batch_size=64, parallel=0)`;但 fastembed 0.8.0 把 `parallel=0` 解讀成「用全部 CPU」而 spawn 子進程 (見 `onnx_text_model.py` `_embed_documents`:`if parallel == 0: parallel = os.cpu_count()`)。又 `streamlit_app.py` 在 **import 時期**就呼叫 `get_resources()` 觸發該多進程,子進程以 forkserver 重新 import 本檔 → 遞迴 bootstrap 崩潰;且 import 時期無 session,使 `@st.cache_resource` 的 spinner 報 `NoSessionContext`。
  - **修正**: (1) `ensure_embeddings` 改傳 `parallel=None` → fastembed 走主行程單執行緒 (onnxruntime threading),徹底不 spawn,首次建快取後只讀 `.npy`;(2) `streamlit_app.py` 把 `get_resources()` 與分類計算移出 import 時期,改在 session 內 (頁面主體、包在 `st.spinner` 中) 呼叫,並為 `get_resources` 加 `show_spinner=False` 避免雙重 spinner。備份:程式碼 → `hybrid_search.py.bak` / `streamlit_app.py.bak` (本檔結構未動)。

- 2026-08-18 檢索相關性修正 — Hybrid 模式把離題文件拉進結果 (如搜「房地產」出 `Art and Design/Ad Creatives & Banners/create-photorealistic-*.md`):
  - **現象**: Lexical 模式搜「房地產」前 12 名 100% 是 Real Estate 類;但 Hybrid 模式會把 `Photorealistic Campaign Image / Outdoor Scene` 等圖像生成 prompt 排進來。那兩個檔案本體與索引都沒有 `real estate / property / listing` 字眼 (lexical 得分 = 0)。
  - **根因**: 舊 Hybrid 的 RRF 融合是對「整個 pool」做的,`dense`(embedding) 相似度把零詞彙命中的文件也加進 RRF;而 `Photorealistic` 含 `real` 子串、且「房產視覺/場景圖」與 `real estate` 在語意空間相近,導致誤關聯。此現象對 embedding 版本/快取狀態敏感 (本地快取 embedding 在同池 top30 未重現,雲端卻出現),故不能依賴 embedding 行為。
  - **修正**: `search()` 改為**候選集策略** — 當詞彙命中足夠 (≥ top_n) 時,`dense` 只在「有詞彙得分的候選」內做 RRF 重排,**不允許零詞彙命中的離題文件進入結果**;僅當詞彙命中過少 (純語意/轉述查詢) 才回退成舊的全量融合,保證仍有結果。驗證:「房地產」Hybrid top8 全為 Real Estate;零詞彙查詢「幫我寫一首詩」走回退路徑正確回傳詩/歌詞類且未崩潰。備份:程式碼 → `hybrid_search.py.bak2`。

- 2026-08-18 檢索引擎改以 **txtai hybrid 方法** 重做 (移除自訂 heuristic):
  - **問題**: 上版用自己定的「絕對 cosine 門檻 `DENSE_MIN_SIM=0.30` + 候選集約束」來擋離題文件,屬 ad-hoc heuristic —— 對模型版本/快取敏感,且對純語意查詢是「全有全無」的回退,不具原則性。
  - **改法 (參考 [neuml/txtai](https://github.com/neuml/txtai) hybrid 引擎)**: 改採 txtai 的 **convex combination of normalized scores** —— sparse(詞彙) 與 dense(向量) 兩條流各自正規化到 [0,1] 後做凸組合 `final = bias·dense + (1−bias)·sparse`,候選取兩流**聯集 (union)**,**不再設任何絕對 cosine 門檻**。
    - sparse 流: 欄位加權詞彙得分做 min-max 正規化; dense 流: 單位向量 cosine (≈[0,1]) 直接採用; 每流先各取 `limit*10` 候選再融合 (同 txtai)。
    - `HYBRID_BIAS=0.1` 對應 txtai 的 hybrid 權重 `weights=[bias, 1−bias]`,預設偏重關鍵字 —— 零詞彙命中的離題文件最多只拿到 `bias·cosine` 的小分,自然排在強關鍵字命中之後,但不會被硬門檻粗暴剔除 (純語意/轉述查詢仍可回傳結果)。此為 txtai 的超參數,非自訂 heuristic。
  - **驗證**:「房地產」Hybrid top8 全為 Real Estate,無 Art/Ad 圖像;「幫我寫一首詩」top8 全為 詩/歌詞/創意寫作 (Audio·Music、Writing·Creative Writing),舊版跑出 Art/Ad 圖像的問題消失;「廣告圖」top8 仍正確保留 Art/Ad Creatives 圖像類 (相關時不誤殺)。詞彙 Lexical 與「全部顯示」瀏覽模式不受影響。
  - **附註**: fastembed 0.8.0 對該模型改採 mean pooling (舊版 CLS),啟動時會有 UserWarning,現行 `_embeddings.npy` 仍可正確檢索;若日後語意相關性異常,可刪 `prompts/_embeddings.npy` + `prompts/_embed_meta.json` 後以 `--build` 重建 (需可讀已修復的模型快取)。備份:程式碼 → `hybrid_search.py.bak4`。

- 2026-08-18 依評論重做: 可切換融合 + 效能/快取修正 + prompt 正文入向量 + 基準
  - **融合可切換 (參考 txtai, 評論第 1 點)**: 新增 `HYBRID_FUSION` (`rrf` 預設 | `convex`)。txtai 依 sparse 是否已正規化選融合法;本機 lexical 是未校準原始分數,故預設 **RRF** (只看排名、不受分數尺度影響,最穩健),換 BM25F 後可切 convex。兩流皆先截斷到 `limit*10` 再融合 (同 txtai)。CLI 加 `--fusion rrf|convex` 便於比較。
  - **效能/快取修正 (評論第 3 點)**: (a) `TextEmbedding` 模型改模組級快取 (`_get_embed_model`),不再每次查詢重建; (b) 移除 `index.index(e)` 的 O(N²) 線性掃描,改在建池時一併記錄 `pool_rows`; (c) dense top-k 改 `numpy.argpartition` (O(N) 不排序全庫); (d) embedding 快取 metadata 加 `version` + 索引 `md5` 指紋,內容變動但筆數相同時不再誤用舊向量。
  - **prompt 正文納入 dense 表示 (評論第 4 點)**: `doc_text()` 在 title/keywords/snippet 之外,額外納入 `## Prompt` 正文前 `EMB_DOC_BODY_CHARS=1000` 字元 (略過 "You are a..." Role 樣板首句),改善「描述輸出格式/約束但 title 沒寫到」的召回;已重建 `_embeddings.npy` (version 2)。
  - **relevance 基準 (評論第 6 點)**: 新增 `benchmark.py` (18 題中英文種子集, category-level 相關性 proxy),量測 MRR@5 / nDCG@5 / 命中率@5。結果: lexical 77.8% → hybrid(RRF) 83.3% → **RRF(bias=0.3) 88.9% 最佳**。據此把 `HYBRID_BIAS` 由直覺值 0.1 調成基準量得的 **0.3** (對房地產/寫詩/廣告圖查詢經測試不引入離題)。
  - **一致性修正**: `streamlit_app.py` (3 處) 與 `README` (模式說明 2 處) 的舊 "RRF" 描述統一改為 txtai 風格 RRF/凸組合說明;舊 Changelog 中描述過往 RRF 實作的句子保留為歷史紀錄。
  - **未執行 (評論第 2/5 點, 擇期)**: BM25F sparse 層 (改動大,且 RRF 預設已不依賴分數校準,優先級降);reranker 第三階段 (需另下載 cross-encoder 模型,本機 HF 下載曾損毀,風險高,留待必要時)。備份:程式碼 → `hybrid_search.py.bak5`。

- 2026-08-18 benchmark 擴充 + HYBRID_BIAS 實測定為 0.5 (依 skills.json 隨機生成 111 題中英文):
  - **擴充基準 (評論第 6 點續)**: `benchmark.py` 原 18 題種子擴充為 **111 題中英文需求**;改為**依 `skills.json` 隨機抽取技能** (`C:\AI\Skills_Library\skills.json`, 462 技能 / 30 類),再連到 `_search-index.json` 的 `related_skills` 取得「該技能真正對應的 prompt 類別」作為相關性 proxy 標註 (rels)。每題都有可驗證的正確類別,且天然混合中英文、覆蓋 15+ 大類。備份: `benchmark.py` → `benchmark.py.bak`。
  - **實測決定 HYBRID_BIAS**: 在 111 題上掃描 `rrf`/`convex` × `bias ∈ {0.1, 0.3, 0.5, 0.7}`。結果: lexical 87.4% → rrf(0.1) 89.2% → rrf(0.3) 95.5% → **rrf(0.5) 97.3% (MRR@5=0.947, nDCG@5=0.932) 全組最佳** → rrf(0.7) 97.3% (MRR 0.934 略低) → convex 各檔 89–92%。故將 `HYBRID_BIAS` 由 0.3 (18 題種子下的次佳) 調升為 **0.5** (bias 0.5 在 MRR@5 與 nDCG@5 上皆嚴格優於 0.7,命中率@5 持平)。
  - **離題回歸驗證**: 對三個歷史敏感查詢 (房地產 / 寫詩 / 廣告圖) 在 bias=0.5 下逐項檢查,前 8 名類別仍 100% 落在正確類別,未重新引入 Art/Ad 圖像等離題 — 確認調升 bias 安全。備份:程式碼 → `hybrid_search.py.bak6`。
  - **保持待辦 (評論第 2/5 點)**: BM25F sparse 層、reranker 第三階段仍擇期執行 (理由同前)。

- 2026-08-18 README 註記: 「建議搭配技能」標示進階版收費 — 在中文 (line 73) 與英文 (line 167) 的 `## 用法 / Usage` 結構範例中, 於 `建議搭配技能 / Pair with skill` 後加註 `(細節請提出客製化需求)` / `(details — submit a custom request)`, 說明隨 prompt 附的技能提示僅供參考, 進階 / 客製化搭配為收費諮詢 (與 line 106 / 195 的「客製化諮詢」說明一致)。

- 2026-08-18 v8 — 外部 skills.json 缺口分析 (新增 `skills_gap_analysis.md`): 比對 `C:\AI\Skills_Library\skills.json` (462 skills / 30 categories, 全為建構 AI 系統的元技能) 與本專案 `prompts/` (6,398 prompts / 21 categories, 具體商業領域能力)。先完整讀取 skills.json 30 類別說明, 再將每個 prompt 的 `related_skills` 交叉比對: 148 組 `(cat, skill)` 全部存在 → 無幽靈 skill; 缺口為**覆蓋/比重缺口**。結論: 前 5 名元類別過飽和 (Meta_Prompt&System_Design 被 5,509 prompt 當兜底); 具體領域類別稀薄且需求未被滿足 (Commercial_Growth&Acquisition=10 技能但 Marketing+SEO+Sales=1,355 prompt 幾全塌陷進 Meta_Prompt; Academic_Insight&Forensics=5 技能但 Research=279 prompt 僅 1 筆路由; Domain_Specific_Expertise/Reasoning 共 17 技能要代表 Finance/Legal/Real Estate/HR 近千 prompt); `Operational_Governance&Reporting` 與 `UI_UX&Frontend_Engineering` 為 0 路由孤兒類別。建議: 啟用兩孤兒類別、擴充稀薄領域類別、並為 Customer Service/Productivity/Data Analysis/Careers/Audio/Video 等無歸屬類別新增 skills.json 類別。備份: 本檔 → `README.md.v7.bak`。

- 2026-08-18 v9 — 修正 v8 的「只看數量」偏差, 改用品質視角 (新增 `skills_supplement_quality.md` + `template_dedup_final.py` + `_template_dedup.json`): 用戶指正 skills.json 是「精華/通用技能庫」, 應按需求動態組成 prompt, 故不能用筆數報缺口。做法: (1) 實讀多個 prompt 原文驗證「同類別是否套同一模板」— 發現共享 Role/Task/Context 骨架是良好撰寫習慣非冗餘, 真正「同模板變體」全庫僅 ~6.1% (≈389 筆), 集中在 Marketing/Ad Copy 的 `create-{platform}-ad-copies`、Art 的 `get-{style}` 系列、SEO/Strategy audit 簇; (2) 全量抽取 `## Prompt` 本體、遮蔽 `{{變數}}` 後詞袋 Jaccard 聚類 (閾值 0.30) 做模板去重 → 6,398 筆去重為 **6,009 個不同 skill 模板**; (3) 對每個不同模板, 依頂層 `related_skill` 所屬類別判斷 skills.json 是否已有**具體技能**: 落通用元類別=缺具體技能(可補充), 落具體領域類別=已涵蓋。結果: **4,927 個不同模板 skills.json 缺對應具體技能 (真正可補充實例上限)**, 1,082 已被 Visual_Architecture(359)/Academic_Research_Synthesis(324)/Minimalist_Entrepreneurship(226)/Domain_Specific(116) 等具體技能涵蓋。可補充強度排序: SEO > Coding > Marketing > Education > Productivity/Operations > HR/Finance/Legal/Real Estate/Sales/Customer Service/Data Analysis/Careers/Audio/Video。附註: 4,927 是上限 (通用元類別內含少數具體技能如 `Code_Claim_Adversarial_Audit`), 且應抽象成一般技能而非 4,927 筆實例。備份: 本檔 → `README.md.v8.bak`。

- 2026-08-18 v10 — skills.json 稀薄類別( <20 skill )之「技能級缺口」分析 (新增 `thin_cat_skill_gaps.md` + `thin_cat_dossier.txt` 原始比對檔 + `thin_gap_score.py` 詞彙重疊掃描): 用戶要求對 20 個 <20 skill 的類別, 逐一**實讀既有 skills.json 技能**並與**路由到該類別的專案 prompt** 比對, 判斷「哪些 prompt 真的值得納入成為新 skill」(不看數量, 看技能級缺口)。方法: 先建各類別既有技能「能力基線」, 再對每個 feeding prompt 判斷其能力是否已被涵蓋(已涵蓋=換變數即可, 不補; 未涵蓋=新的可複用可組裝單元, 值得補)。附帶詞彙 Jaccard 掃描驗證: 所有 feeding prompt 與既有技能的詞彙重疊皆 ≈0.00–0.02 (skills.json 用抽象元詞彙、專案用具體領域詞), 證明**詞彙重疊無法判斷涵蓋, 必須概念判讀**。結論: (1) **強缺口**= Domain_Specific_Expertise(10 skill / 306 feed, 缺稅務/合約/HR/不動產/SEO/數據分析 7 個領域專家技能) · Interactive_Pedagogy&Diagnostic_Systems(7/155, 缺自適應路徑/評量題/類比講解 3 個) · Self_Evolution&Refinement(9/687, 既有是「精進 agent 自己的 skill 邏輯」, 但 687 feed 是「幫使用者改文件」, 缺 Iterative_Content_Revision_Protocol + Process_QA_Audit_Loop 2 個); (2) **中缺口**= Commercial_Growth&Acquisition(路由低估, 補落地頁/郵件序列/推薦迴圈) · Minimalist_Entrepreneurship(補上線挽回) · RPG(補遊戲化) · Operational_Governance(孤兒, 補回顧+KPI) · UI_UX(孤兒, 補互動模式) · Domain_Specific_Reasoning(補 SWOT/文獻/政策框架); (3) **已涵蓋不補**= Visual_Architecture(839 feed 是元技能變數實例) · Human_In_Loop(1337 feed 被元技能組裝) · Interactive_Narrative · Persona&Narrative; (4) **無缺口**= Distributed_Cognition · Structured_Knowledge_Nav · Agent_SOP · Academic_Insight(後兩類 feed 全錯路由)。彙整出**值得補的候選新 skill 共 ~24 個**(見報告 A 表), 並指出 UI_UX / Operational_Governance 為 0 路由孤兒、Commercial_Growth 路由低估, 須同步修 `_search-index.json` 的 `related_skills` 映射。備份: 本檔 → `README.md.v9.bak`。
