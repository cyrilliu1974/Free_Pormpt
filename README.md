# AI Prompt Library · 離線封存 + 分類索引 (v7)

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
- 🔎 **關鍵字搜尋**:支援中文(自動 CN→EN 展開)與英文,採 **詞彙 + 同義擴展 + 欄位加權**;還可疊加 **本地多語言 embedding + RRF 混合檢索**,對自然語言需求描述最準。
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
├── hybrid_search.py                # 本地 hybrid 檢索 (lexical + dense + RRF), 純 Python
├── streamlit_app.py                # 雙語 Web 檢索介面 (lexical / hybrid)
└── prompts_pre-vN-backup/          # 各版整樹備份 (可還原)
```

## 數量與分類

- **實際封存:6,398 個 prompt**(其餘約 330 個因來源站累積限速未能抓取,見下方說明)
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

## 用法 / Usage          # v7 新增: 精簡、對執行有用, 不堆裝飾分析
- 必填變數 / Variables: {{topic-and-subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
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
- **檢索模式**:`混合 Hybrid`(lexical + 本地多語言 embedding + RRF, 對自然語言最準) 或 `詞彙 Lexical`(純關鍵字/同義/欄位加權)。
- 純本地,不呼叫 LLM API。首次執行 hybrid 會自動下載多語言模型並建立 `_embeddings.npy` 快取(之後只讀)。

> 若需要針對特定場景**建議搭配技能**，請另外提出**客製化諮詢**。

</div>

<div id="en" class="lang">

## What this is

This repo is an **offline archive + categorized index** of 6,000+ free prompts from **God of Prompt**. Everything is plain local markdown, **no LLM API calls** — browse and search fully offline.

### Why this repo

- 🗂️ **Manual category browsing**: 21 top categories / 143 subcategories, drill down from the `prompts/index.md` master index. Great when you "don't yet know what you want and just want to explore."
- 🔎 **Keyword search**: supports Chinese (auto CN→EN expansion) and English, using **lexical + synonym expansion + field weighting**; can be upgraded to **local multilingual embedding + RRF hybrid retrieval** for the most accurate natural-language queries.
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
├── hybrid_search.py                # local hybrid retriever (lexical + dense + RRF), pure Python
├── streamlit_app.py                # bilingual web UI (lexical / hybrid)
```

## Volume & taxonomy

- **Archived: 6,398 prompts** (the other ~330 failed due to source-site rate limits, see notes below)
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

## 用法 / Usage          # v7: concise, execution-useful, no decorative analysis
- 必填變數 / Variables: {{topic-and-subject}} — fill before running
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
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
- **Retrieval mode**: `混合 Hybrid` (lexical + local multilingual embedding + RRF — best for natural language) or `詞彙 Lexical` (pure keyword/synonym/field-weighted).
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
