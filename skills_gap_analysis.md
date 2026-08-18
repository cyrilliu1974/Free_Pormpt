# skills.json 缺口分析 · 專案 prompts 可填補的 skill（依類別）

> 產出日期：2026-08-18
> 比對對象：`C:\AI\Skills_Library\skills.json`（462 skills / 30 categories）vs 本專案 `prompts/`（6,398 個 prompt / 21 categories）
> 方法：先完整讀取 skills.json 30 個類別的 `category_description`，再將每個 prompt 的 `related_skills`（指向 skills.json 的 `(cat, skill)`）與 skills.json 實際庫存交叉比對，最後按「類別」計算覆蓋/比重缺口。

---

## 1. 前提與關鍵結論

- **skills.json 的本質**：30 個類別幾乎全是在講「**如何建構 AI 系統 / agent / prompt 的元技能**」（Meta_Prompt、Orchestration、Logic&Audit、Agent runtime、Verification…），只有少數類別觸及具體商業領域。
- **專案 prompts 的本質**：6,398 個 prompt 全是**具體商業領域的可執行能力**（行銷、地產、法務、財務、人資、銷售…）。
- **交叉比對結果**：prompts 引用的 **148 組 `(cat, skill)` 全部存在於 skills.json 的 462 個技能中** → 不存在「幽靈 skill / 不存在的 skill」。
- **因此「缺口」是覆蓋面與比重缺口，不是缺失的技能名**：
  1. skills.json 的少數「具體領域」類別**過於稀薄**，卻承接了龐大的 prompt 需求；
  2. 兩個 skills.json 類別**零 prompt 支撐**（孤兒類別）；
  3. 多個專案 prompt 類別**在 skills.json 中根本沒有對應類別**，只能全部塌陷進 `Meta_Prompt&System_Design` 這個大雜燴。

---

## 2. skills.json 類別：庫存量 vs 專案 prompt 需求量

`lib` = skills.json 該類別技能數；`distinctPrompts` = 有多少個 prompt 經 `related_skills` 路由到該類別；`refs` = 路由連結總數。

| skills.json 類別 | lib | distinctPrompts | refs | 狀態 |
|---|--:|--:|--:|---|
| Meta_Prompt&System_Design | 22 | 5509 | 7303 | 🔴 過飽和（萬能兜底） |
| Context&Session_Management | 30 | 2019 | 2197 | 🔴 過飽和 |
| Academic_Research_Synthesis_Pipeline | 22 | 1730 | 1963 | 🟡 偏高 |
| Axiomatic_Logic&Audit_Systems | 40 | 1740 | 1936 | 🟡 偏高 |
| Human_In_Loop_Workflow_Engineering | 18 | 1305 | 1337 | 🟡 偏高 |
| Minimalist_Entrepreneurship_Execution | 11 | 839 | 1000 | 🟡 |
| Visual_Architecture&Creative_Engineering | 12 | 604 | 839 | 🟢 較均衡 |
| Self_Evolution&Refinement | 9 | 656 | 687 | 🟡 |
| Prompt&Manifest_Engineering | 29 | 348 | 367 | 🟢 |
| Domain_Specific_Reasoning | 7 | 342 | 342 | 🟠 **稀薄但需求大** |
| Domain_Specific_Expertise | 10 | 306 | 306 | 🟠 **稀薄但需求大** |
| Skill_Orchestration&Assembly | 20 | 178 | 180 | 🟢 |
| System_Verification&QA_Logic | 40 | 176 | 176 | 🟢 |
| Interactive_Pedagogy&Diagnostic_Systems | 7 | 143 | 155 | 🟠 **稀薄但需求大** |
| Strategic_Decision&Adversarial_Thinking | 16 | 94 | 106 | 🟢 |
| RPG&Immersive_World_Systems | 11 | 81 | 81 | 🟢 |
| Interactive_Narrative&Creative_Fiction_Engine | 10 | 53 | 58 | 🟢 |
| Agent_SOP_Framework&Extraction_Protocol | 5 | 45 | 45 | 🟢 |
| Agent_State&Trajectory_Engineering | 23 | 29 | 29 | 🟢 |
| Data_Structuring&Engineering | 3 | 24 | 24 | 🟠 稀薄 |
| Persona&Narrative_Synthesis | 11 | 15 | 15 | 🟠 **嚴重欠路由** |
| Input_Classification&Routing | 24 | 14 | 14 | 🟢 |
| Software_Architecture&Performance | 11 | 8 | 10 | 🟢 |
| Commercial_Growth&Acquisition | 10 | 8 | 8 | 🟠 **嚴重欠路由** |
| Structured_Knowledge_Navigation_Architecture | 4 | 6 | 6 | 🟠 稀薄 |
| Distributed_Cognition&Context_Orchestration | 14 | 5 | 5 | 🟢 |
| Autonomous_Agent_Execution_Logic | 29 | 4 | 4 | 🟢 |
| Academic_Insight&Forensics | 5 | 1 | 1 | 🟠 **近乎零路由** |
| UI_UX&Frontend_Engineering | 5 | 0 | 0 | ⚪ **孤兒（0 支撐）** |
| Operational_Governance&Reporting | 4 | 0 | 0 | ⚪ **孤兒（0 支撐）** |

> 觀察：前 5 名元類別吃掉了絕大多數路由；具體領域類別（黃/橙）普遍「技能少、需求卻不小」，而 `UI_UX` 與 `Operational_Governance` 完全沒有 prompt 路由進去。

---

## 3. 依類別：哪些 prompt 的 skill 可填補 skills.json 缺口

### 3.1 Commercial_Growth&Acquisition（lib=10，卻只有 8 筆路由）← Marketing / SEO / Sales
- **缺口理由**：該類別描述是「把市場信號/品牌資產/受眾洞察轉成可執行的商業轉化動作（付費獲客、行為誘因、銷售轉化、跨文化本地化）」。但 Marketing(701)+SEO(512)+Sales(142)=**1,355 個 prompt** 幾乎全部塌陷到 `Meta_Prompt&System_Design`，只有 8 筆路由進此類別。
- **可填補的 prompt skill（實例）**：
  - Marketing：`Pain Point Ad Copy Generator for Direct Response`、`Limited-Time Offer Copy Generator for Urgency Campaigns`、`App Store Description Generator`
  - SEO：`Seasonal SEO Campaign Builder`、`Market Trend SEO Opportunity Analysis`
  - Sales：`Build Cloud-Based Cold Calling Systems`、`Influencer Outreach Message Generator`
- **建議**：把這三類的「獲客/轉化/本地化」型 prompt 抽出為該類別的具體 skill 單元（如 `Direct_Response_Ad_Copy`、`Urgency_Offer_Framework`、`Cold_Outreach_Sequence`）。

### 3.2 Domain_Specific_Expertise（lib=10）+ Domain_Specific_Reasoning（lib=7）← Finance / Legal / Real Estate / HR
- **缺口理由**：這是 skills.json 中**唯一**承接具體專業領域的類別，但 10+7=17 個技能要代表 Finance(295)+Legal(216)+Real Estate(145)+HR(334)+Sales(142) 等數百個 prompt，明顯不足。
- **可填補的 prompt skill（實例）**：
  - Finance：`Zero-Based Budget Builder`、`Subscription Spending Audit`、`Business Expense Pattern Analysis`
  - Legal：`Compliance Reporting Gap Analysis`、`Compliance Risk Warning Sign Analysis`、`Corporate Policy Drafting`
  - Real Estate：`Buyer Conversion Script Generator`、`Buyer Lead Segmentation Framework`、`Home Offer Letter Writer`
  - HR：`Employee Burnout Analysis`、`Employee Feedback Analysis`、`Analyze Employee Disengagement Causes`
- **建議**：按領域拆分子類（Finance / Legal / Real Estate / HR），把上述 prompt 轉為對應的領域 reasoning / expertise skill。

### 3.3 Interactive_Pedagogy&Diagnostic_Systems（lib=7，143 筆路由）← Education
- **缺口理由**：Education 有 **436 個 prompt**，但只有 143 筆路由到此類別（其餘多塌陷到 Meta_Prompt / Academic_Research_Synthesis）。
- **可填補的 prompt skill（實例）**：`Character Comparison Analysis for Literary Study`、`Literary Narrative Analysis Essay Outline Generator`、`Character Development Analysis`。
- **建議**：擴充「自適應教學序列 / 診斷分流」型 skill。

### 3.4 Academic_Insight&Forensics（lib=5，僅 1 筆路由）← Research
- **缺口理由**：**最嚴重欠路由**的領域類別。Research 有 **279 個 prompt**，但只有 1 筆路由進此類別（描述為「論文取證、分層掃描、方法論逆推、批判模擬」）。
- **可填補的 prompt skill（實例）**：`Competitive Industry Landscape Analysis`、`Competitor Brand Positioning Analysis`、`Compliance Reporting Gap Analysis`。
- **建議**：這 279 個 Research prompt 中大量是「競品/產業/差距分析」，正是 forensics 型技能，應大舉路由並轉為 skill。

### 3.5 Persona&Narrative_Synthesis（lib=11，僅 15 筆路由）← Writing
- **缺口理由**：Writing 有 **359 個 prompt**，但只有 15 筆路由到此類別（其餘塌陷到 Meta_Prompt / Academic_Research_Synthesis）。
- **可填補的 prompt skill（實例）**：`Content Structure Analysis`、`Avoid Duplicate Content in Rewrites`、`Blog Post Idea Generator`。
- **建議**：把「語氣/敘事/角色」型寫作 prompt 轉為 persona & narrative skill。

### 3.6 Operational_Governance&Reporting（lib=4，0 路由）← Operations / Strategy【最大孤兒缺口】
- **缺口理由**：該類別描述是「持續營運、利害關係人對齊、把複雜資料綜合成執行摘要」。**Operations(376)+Strategy(444)=820 個 prompt** 卻**沒有任何一筆**路由進此類別（全部塌陷到 Meta_Prompt / Context&Session_Management）。
- **可填補的 prompt skill（實例）**：Operations 的 `Analyze Meeting Notes`、`Meeting Minutes Template`、`Team Meeting Facilitation Framework`；Strategy 的 `Business Idea Feasibility Analysis`、`Business Expansion Feasibility Analysis`。
- **建議**：這是最該「啟用」的孤兒類別——把營運/治理/報告型 prompt 路由並轉為 skill。

### 3.7 UI_UX&Frontend_Engineering（lib=5，0 路由）← Art and Design
- **缺口理由**：Art and Design 有 **808 個 prompt**（其中大量是廣告橫幅/落地頁/網頁 banner），但 0 筆路由進此類別（多數進 Visual_Architecture&Creative_Engineering）。
- **可填補的 prompt skill（實例）**：`2D Flat Web Banner Generator`、`Athletic Apparel Grid Advertisement`、`Beer Advertisement Instagram Grid`。
- **建議**：把「介面/前端/網頁視覺」型 prompt 路由到此類別，補足其 0 支撐狀態。

### 3.8 Visual_Architecture&Creative_Engineering（lib=12，839 路由）— 已較充足
- Art and Design 對此類別路由充足（823 筆），不需額外填補，屬健康類別。

---

## 4. skills.json 完全缺少的「專案類別」（無對應類別）

以下專案 prompt 類別幾乎 100% 塌陷進 `Meta_Prompt&System_Design`，**skills.json 沒有專屬類別可承接**，domain 佔比均偏低：

| 專案類別 | prompt 數 | 主要路由 | domain 佔比 | 缺口性質 |
|---|--:|---|--:|---|
| Customer Service | 167 | Meta_Prompt / Axiomatic_Logic | 21.4% | 缺「客戶體驗 / 客服話術」類別 |
| Productivity | 379 | Meta_Prompt / Context&Session | 14.6% | 缺「生產力系統 / 工作流」類別 |
| Data Analysis | 194 | Meta_Prompt / Axiomatic_Logic | 22.9% | 缺「資料分析 / 指標」類別 |
| Careers | 94 | Meta_Prompt / Context&Session | 17.7% | 缺「職涯發展」類別 |
| Audio | 16 | Meta_Prompt / HITL | 18.8% | 缺「音樂 / 音訊生成」類別 |
| Video | 2 | Meta_Prompt | 33.3% | 缺「影片製作」類別（樣本極少） |

> 這些類別在 skills.json 中找不到歸屬，是結構性缺口——建議**新增對應類別**，而非塞進現有元類別。

---

## 5. 我的建議（依缺口嚴重度排序）

1. **啟用兩個孤兒類別**（最高優先）：`Operational_Governance&Reporting`（吃 Operations+Strategy 820 prompt）、`UI_UX&Frontend_Engineering`（吃 Art&Design 設計/前端 prompt）。
2. **大舉擴充稀薄領域類別**：`Commercial_Growth&Acquisition`（補 Marketing/SEO/Sales 獲客轉化）、`Academic_Insight&Forensics`（補 Research 取證分析）、`Domain_Specific_Expertise`+`Domain_Specific_Reasoning`（補 Finance/Legal/Real Estate/HR）、`Interactive_Pedagogy&Diagnostic_Systems`（補 Education）、`Persona&Narrative_Synthesis`（補 Writing）。
3. **新增 skills.json 缺失的具體領域類別**：Customer Service、Productivity、Data Analysis、Careers、Audio、Video——這些 prompt 目前只能塌陷進 `Meta_Prompt&System_Design`，失去領域語意。
4. **降載過飽和元類別**：`Meta_Prompt&System_Design` 被 5,509 個 prompt 當兜底，應把具體領域 prompt 抽到上述領域類別，避免單類別膨脹失真。

---

## 6. 附註（方法學）

- 「專案 prompt 所帶有的 skill」= 每個 prompt `## 用法 / Usage` 區塊的 `related_skills`（`cat` + `skill` + `score`），由 `_search-index.json` 的 `related_skills` 欄位提供。
- 交叉比對以 `(cat, skill)` 為鍵；skills.json 技能主鍵為 `skill_name`。
- 所有 6,398 個 prompt 皆有 `related_skills`（覆蓋率 100%），故結論具代表性。
- 「過飽和 / 稀薄 / 孤兒」判定依據：`lib`（庫存技能數）與 `distinctPrompts`/`refs`（prompt 路由需求）的相對大小。
