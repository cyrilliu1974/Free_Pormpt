# skills.json 稀薄類別之「技能級缺口」分析 (v10)

> 延續 v8(數量視角) 與 v9(品質視角/模板去重) 的第三層深挖。
> 本檔只回答一件事:**skills.json 中 <20 個技能的 20 個稀薄類別, 哪些專案 prompt 真的「值得」納入成為新 skill** —— 不是看數量, 是看「技能級缺口 (skill-level gap)」。

---

## 方法與重要前提

1. **資料來源**:`C:\AI\Skills_Library\skills.json`(462 skills / 30 類);本專案 `prompts/_search-index.json`(6,398 筆, 每筆有 `related_skills`)。
2. **「對應的專案 prompt」定義**:將每個 prompt 的 `related_skills` 反查到其所屬類別, 得到該類別的 **feeding prompts**(已路由到該類別的專案 prompt)。
3. **判斷邏輯(品質, 非數量)**:
   - 對每個稀薄類別, 先讀**既有 skills.json 技能**(名稱+描述) 建立「能力基線」;
   - 再讀 feeding prompts(標題+摘錄), 逐一判斷: 該 prompt 代表的能力**是否已被既有技能涵蓋**?
     - 已涵蓋 = 既有技能只是換變數就能產出 → **不值得補**(冗餘);
     - 未被涵蓋 = 代表一個**新的、可複用、可組裝**的一般性能力單元 → **值得補(候選新 skill)**。
4. **詞彙重疊掃描的侷限(已驗證)**: 我用 bag-of-words Jaccard 把每個 feeding prompt 與該類別既有技能詞彙比對, 結果**全部類別都 ≈ 0.00–0.02**(見 `thin_gap_score.py` 輸出)。原因: skills.json 技能用高度抽象的元詞彙, 專案 prompt 用具體領域詞彙, 兩者幾乎不共享字。→ **詞彙重疊無法判斷涵蓋與否, 必須靠概念判讀**。本檔結論即基於概念判讀。

---

## 20 個稀薄類別 · 技能級缺口總評

> 排名依「真實技能級缺口強度」(值得補的候選 skill 數 × 需求廣度), 由強到弱。

| 排名 | 類別 | 既有skill | feeding数 | 缺口強度 | 值得補的候選 skill 數 | 一句結論 |
|---|---|---|---|---|---|---|
| 1 | Domain_Specific_Expertise | 10 | 306 | **強** | ~7 | 領域專家層只有 IP/專利+財務風險+自動化, 缺稅務/合約/HR/不動產/SEO/數據分析等整片領域 |
| 2 | Interactive_Pedagogy&Diagnostic_Systems | 7 | 155 | **強** | ~3 | 教學/診斷層只有 7 個元技能, 但 155 筆教育 feed 暴露出自適應路徑/評量題/類比講解等未實例化模式 |
| 3 | Self_Evolution&Refinement | 9 | 687 | **強** | ~2 | 既有 9 個是「精進 agent 自己的 skill 邏輯」, 但 687 筆是「幫使用者改文件/改文案」→ 缺內容修訂迴圈 |
| 4 | Commercial_Growth&Acquisition | 10 | 8* | 中 | ~3 | *路由嚴重低估: Marketing+Sales 真實需求千筆, 但只 8 筆路由到此; 缺落地頁/生命週期郵件/推薦迴圈等具體獲取模式 |
| 5 | Minimalist_Entrepreneurship_Execution | 11 | 1000 | 中 | ~1 | 核心旅程已涵蓋, 只缺「客戶上線與挽回流程」這一塊 |
| 6 | RPG&Immersive_World_Systems | 11 | 81 | 中 | ~1 | RPG 機制完整, 但跨 Marketing/HR/Education 出現的「遊戲化/忠誠/徽章/連勝」模式未被涵蓋 |
| 7 | Operational_Governance&Reporting | 4 | 0* | 中 | ~2 | *孤兒類別(0 路由), 但專案有大量月報/回顧/ KPI 報告 prompt 未被接; 同時既有 4 個偏元, 缺回顧協議與 KPI 監控設計 |
| 8 | UI_UX&Frontend_Engineering | 5 | 0* | 中 | ~1 | *孤兒類別(0 路由), 但專案 UI 類 prompt 很多(錯路由到 Art/Human_In_Loop); 既有 5 個聚焦 DNA/程式碼/效能/QA, 缺互動模式合成 |
| 9 | Domain_Specific_Reasoning | 7 | 342 | 中 | ~2–3 | 7 個是元推理框架; 342 筆是 SWOT/文獻回顧/政策分析等具體框架 → 抽象出少數高需求框架技能 |
| 10 | Software_Architecture&Performance | 11 | 10 | 中弱 | ~2 | 架構+DB效能+CI/CD 已涵蓋 10 筆; 缺前端渲染效能與測試案例策略 |
| 11 | Strategic_Decision&Adversarial_Thinking | 16 | 106 | 中弱 | ~1 | 16 個對抗/策略思維已很厚, 106 筆多為 SWOT/情境/風險(被元技能涵蓋); 只缺顯式情境規劃協議 |
| 12 | Data_Structuring&Engineering | 3 | 24 | 中弱 | ~1 | 3 個(ETL/Schema/動態Schema)已很通用; 缺「多文件結構轉換」(FAQ→KB 等) |
| 13 | Visual_Architecture&Creative_Engineering | 12 | 839 | 弱(已涵蓋) | ~1 | 839 筆 Art feed 幾乎都是 12 個元圖像技能的「變數實例」→ 已涵蓋; 至多補產品攝影構圖 |
| 14 | Human_In_Loop_Workflow_Engineering | 18 | 1337 | 弱(已涵蓋) | ~0–1 | 18 個人機協作元技能已非常完整; 1337 筆是內容, 被元技能組裝 → 已涵蓋 |
| 15 | Interactive_Narrative&Creative_Fiction_Engine | 10 | 58 | 弱(已涵蓋) | ~1 | 小說引擎 10 個技能完整; 58 筆是內容實例 → 已涵蓋; 至多補系統化規則引擎 |
| 16 | Persona&Narrative_Synthesis | 11 | 15 | 弱(已涵蓋) | ~0–1 | 15 筆多為既有 persona/sensory/narrative 技能的具體實例 → 已涵蓋 |
| 17 | Distributed_Cognition&Context_Orchestration | 14 | 5 | 無缺口 | 0 | 14 個跨 session/handoff/記憶技能已涵蓋完整空間; 專案無「上下文編排」能力可貢獻 |
| 18 | Structured_Knowledge_Navigation_Architecture | 4 | 6 | 無缺口 | 0 | 4 個知識導航技能已涵蓋小眾空間; 6 筆 feed 皆錯路由(非知識導航設計) |
| 19 | Agent_SOP_Framework&Extraction_Protocol | 5 | 45 | 無缺口 | 0 | 5 個是「技能萃取 SOP」小眾技能; 45 筆 feed 是內容寫作, 錯路由 → 無缺口 |
| 20 | Academic_Insight&Forensics | 5 | 1 | 無缺口 | 0 | 唯一 feed 是「房地產賣家名單分群」(錯路由, 非學術鑑識); 既有 5 個已涵蓋類別範圍 |

> 標 `*` 表示: feeding 數被路由機制低估/漏接(見各節說明), 實際專案需求更大。

---

## 各類別詳析

### 1. Domain_Specific_Expertise — 強缺口 (建議補 ~7 個)
既有 10 技能: `Automation&Flow_Optimization` · `Intellectual_Property_Intelligence` · `Professional_Relationship_Audit` · `Strategic_Growth_Analysis` · `Supply_Chain_Optimization_Logic` · `IP_Concept_Readiness_Assessment` · `Prior_Art_Iterative_Search_Engine` · `Differentiated_Claim_Drafting_Engine` · `Legal_Forensics&RAG` · `Financial_Risk&Deployment`。

306 筆 feeding 橫跨 Finance/Legal/Operations/SEO/Data/HR/RealEstate… 但既有技能**只深耕 IP/專利 (3) + 財務風險 + 自動化**, 大片領域完全空白。值得補的具體能力單元(各附代表 prompt):

- **Personal_Wealth_&_Tax_Planning_Logic** — 個人理財/稅務規劃(非機構市場進入)。代表: `Net Present Value Calculator`(sc31) · `Cross-Border Tax Analysis`(sc30) · `Estate Planning Assessment`(sc26) · `AMT Risk Assessment`(sc27) · `Dividend Stock Analyzer`(sc26)。既有 `Financial_Risk&Deployment` 只管「市場進入/波動配置/鎖倉」, 不含個人稅務/退休/遺產。
- **Contract_Drafting_Logic** (非 IP 合約) — 通用合約草擬。代表: `Contract Clause Library Builder`(sc27) · `Settlement Agreement Drafting`(sc25) · `Software License Agreement Drafting`(sc25) · `Trial Brief Outline`(sc25)。既有僅 `Legal_Forensics&RAG`(判決書解構) + IP 三件套, 無通用合約技能。
- **Regulatory_Compliance_Doc_Generation** — 合規文件生成。代表: `Privacy Policy Generator`(sc26) · `Compliance Report Generator`(sc25) · `Compliance Controls Matrix Builder`(sc26)。
- **HR_Policy_Compliance_Logic** — HR 政策與勞法合規。代表: `Essential HR Policies`(sc32) · `Employment Law Compliance Identifier`(sc25) · `Employee Offboarding Security Risk Analysis`(sc27)。既有 `Professional_Relationship_Audit` 只管信任/溝通。
- **Real_Estate_Deal_Structuring_Logic** — 不動產交易結構。代表: `Real Estate Leverage Risk Analysis`(sc31) · `Challenge Property Appraisal Errors`(sc29) · `BRRRR Capital Velocity`(sc22) · `Lease Agreement Clauses`(sc23)。
- **SEO_Technical_Audit_Logic** — SEO 技術審計。代表: `Disavow Toxic Backlinks`(sc28) · `Schema Markup for Voice Search`(sc27) · `Keyword Clustering`(sc26) · `Track SERP Features`(sc25)。
- **Data_Analysis_Pipeline_Logic** — 數據分析管線。代表: `Merge Two Dataframes`(sc32) · `Split-Apply-Combine Aggregation`(sc25) · `Prescriptive Analytics Framework`(sc23) · `Sales Dashboard Analysis`(sc25)。

> 結論: 這是**最大、最乾淨的技能級缺口**。建議抽象出上述 ~7 個一般技能(而非把 306 筆實例全塞進去)。

### 2. Interactive_Pedagogy&Diagnostic_Systems — 強缺口 (建議補 ~3 個)
既有 7 技能: `Theme_Manager_Engine` · `Transition_Orchestrator` · `Happiness_Multiplier` · `Feynman_Iterative_Teaching_Loop` · `Stateful_Curriculum_Workspace_Protocol` · `Diagnostic_Triage_Guide` · `Narrative_Domain_Input_Analyzer_Spec`。

155 筆 feeding 以 Education(74) 為主。既有 7 個偏「教學迴圈 + 診斷分流 + 課綱工作區」元技能, 但高需求且**未被實例化**的具體教學模式:

- **Adaptive_Learning_Path_Synthesizer** — 自適應學習路徑(依 ZPD 產生路徑)。代表: `Adaptive Learning Module Builder`(sc31×2) · `Custom Learning Path Generator`(sc31) · `Personalized Study Schedule Builder`(sc27)。`Stateful_Curriculum_Workspace_Protocol` 管「多 session 工作區」, 但「生成路徑本身」未獨立成技能, 且需求極高。
- **Assessment_Item_Generator** — 評量題/閃卡/微學習模組生成。代表: `Study Flashcard Generator`(sc30) · `Interactive Lesson Plan (15 Activities)`(sc30) · `Educational Microlearning Module Builder`(sc34) · `Programming Practice Exercise Generator`(sc23)。跨 Education/Coding/HR 反覆出現。
- **Concept_Explanation_By_Analogy** — 類比講解(真實世界類比拆解概念)。代表: `Data Types Explanation w/ Real-World Analogies`(sc35) · `Complex Topic Explainer`(sc33) · `Programming Concept Simplifier`(sc33)。`Feynman_Iterative_Teaching_Loop` 是「迭代簡化迴圈」, 不含「類比生成」這一具體手法。

> 結論: 7 個元技能相對 155 筆教育 feed 偏薄, 上述 3 個是**高需求、可複用**的具體教學技能, 值得補。

### 3. Self_Evolution&Refinement — 強缺口 (建議補 ~2 個)
既有 9 技能: `Methodological_Framework_Synthesis` · `Skill_Genesis_Protocol` · `Recursive_Self_Refinement` · `Multi_Phase_Iterative_Audit` · `Autoresearch_Skill_Optimization_Loop` · `Attempt_Capped_Self_Evolution_Loop` · `Score_Trajectory_Convergence_Controller` · `Output_Rubric_Scorer` · `Skill_Structure_And_Refinement_Discipline`。

**關鍵錯配**: 既有 9 個全部是「**精進 agent 自己內部的 skill 邏輯**」(recursive self-refinement 修的是 skill 的失敗步驟; rubric scorer 評的是 skill 輸出)。但 687 筆 feeding 幾乎全是「**幫使用者改文件/改文案/改程式**」(proofread, SEO rewrite, fix loop bounds, SOP generator, data validation)。這是**使用者內容修訂**, 不是 skill 自精進。

- **Iterative_Content_Revision_Protocol** — 將回饋納入草稿 + 多輪潤飾 + 依 rubric 評分(應用於**使用者文件**)。代表: `Text Proofreading Coach`(sc31) · `Incorporate Feedback Into Drafts`(sc28) · `Article Rewriting`(sc29) · `Grammar and Proofreading Correction`(sc29) · `Avoid Duplicate Content in Rewrites`(sc31)。橫跨 Writing/Coding/SEO/Marketing/Finance(687 筆全領域)。
- **Process_QA_Audit_Loop** — SOP/QA/流程改良審計。代表: `Standard Operating Procedure Generator`(sc29) · `Quality Assurance Review`(sc30) · `Process Improvement Brainstorming`(sc28) · `Quality Management System Implementation`(sc27)。

> 結論: 這是**跨領域最廣**的缺口(687 筆), 且概念上與既有 9 個有清晰邊界(使用者內容 vs agent 自我)。值得補 2 個。

### 4. Commercial_Growth&Acquisition — 中缺口 (建議補 ~3 個, 但路由低估)
既有 10 技能: `Commercial_Conversion&Deal_Structuring` · `Community_Trust_Engineering` · `Visual_Focal_To_Selling_Point` · `Multi_Angle_Content_Script` · `Tiered_Content_Authority` · `Deficiency_Active_Reframing` · `Technical_Claim_Translation_Quantification_Gate` · `Algorithmic_Spend&Bidding` · `Behavioral_Nudge_Architecture` · `Cultural_Context_Routing`。

**路由低估警訊**: 此類別只有 **8 筆 feeding**, 但按 v8 統計 Marketing(701)+SEO(512)+Sales(142)=1,355 筆 prompt 幾乎全塌陷進 `Meta_Prompt&System_Design`。亦即**真實獲取需求極大, 卻幾乎沒路由到本類別**。8 筆 feed 本身很弱(社群貼文/個人品牌/忠誠計畫), 但專案裡有大量具體獲取內容未被接:

- **Landing_Page_Conversion_Architecture** — 落地頁文案與結構。代表(來自 Marketing feed 但未路由此): `Landing Page Copy Generator for Conversion`(sc28) · `Product Page Conversion Optimization Consultant`(sc31)。
- **Lifecycle_Email_Sequence_Architecture** — 上線/培育/棄購郵件序列。代表: `Abandoned Cart Email Sequence`(sc31) · `Welcome Email Series`(sc30) · `Lead Nurturing Email Sequence`(sc31)。
- **Referral_Loop_Design** — 推薦/轉介迴圈。代表: `Referral-Based Sales Strategy`(sc25) · `Draft Referral Program Messages`(sc26) · `Referral Contest Launch Copy`(sc27)。

> 結論: 既有 10 個是「獲取元邏輯」(轉換/信任/助推/出價/在地化)已不錯; 缺口是**具體獲取模式技能**, 且本類別路由嚴重低估需求。建議補 2–3 個, 並**順便修路由**(讓 Marketing/Sales 的獲取 prompt 能接到此類別)。

### 5. Minimalist_Entrepreneurship_Execution — 中缺口 (建議補 ~1 個)
既有 11 技能涵蓋核心旅程: `Idea_Validation_Engine` · `MVP_Build_Protocol` · `First_Customer_Acquisition_Engine` · `Minimalist_Pricing_Engine` · `Content_Led_Marketing_Engine` · `Sustainable_Growth_Governance` · `Company_Values_Architect` · `Minimalist_Decision_Reviewer` · `Product_Build_Planning_Protocol` · `Technical_Collaboration_Conduct_Protocol` · `Community_Business_Discovery_Engine`。

1000 筆 feeding 多被上述旅程技能涵蓋(`Evaluate Business Idea Viability`→Idea_Validation; `Pricing Optimization`→Minimalist_Pricing; `First Customer Acquisition Ideas`→First_Customer_Acquisition)。唯一明顯空白:

- **Customer_Onboarding_&_Recovery_Flow_Design** — 客戶上線與服務挽回流程。代表: `Onboarding FAQ Generator`(sc34) · `Customer Onboarding Checklist`(sc30×2) · `Automated Refund Processing Script`(sc31) · `Customer Outage Response Templates`(sc30×2) · `Social Media Comment Response`(sc34)。橫跨 Customer Service(52)+Operations+RealEstate。

> 結論: 核心旅程完整, 只缺「上線與挽回」這一塊。補 1 個即可。

### 6. RPG&Immersive_World_Systems — 中缺口 (建議補 ~1 個)
既有 11 技能: `Semantic_Attribute_Mapping` · `Fate_Director_Engine` · `Branching_Narrative_Logic` · `Sensory_Code_Interaction` · `Visual_Generation_Trigger` · `Multi_Agent_Scene_Pressure` · `Soul_Prototype_Architecture` · `Ritual_Randomness_Engine` · `Combat_Balance_Matrix` · `Economic_Ecosystem_Design` · `Meta_Game_Evolution`。

81 筆 feeding 多為內容(故事點子/推特hook/肖像/概念藝術)。但跨 Marketing/HR/Education 反覆出現的**遊戲化模式**未被涵蓋:

- **Gamification_Mechanic_Design** — 忠誠/徽章/連勝/獎勵機制。代表: `Loyalty Program Design`(sc27) · `Badge Reward System Builder`(sc24) · `Streak-Based Gamification Design`(sc24) · `Gamified Onboarding (Octalysis)`(sc23) · `Customer Loyalty Program Design Blueprint`(sc25)。`Economic_Ecosystem_Design`+`Meta_Game_Evolution` 是「遊戲內經濟/賽局」, 不含「對使用者的忠誠與遊戲化」。

> 結論: RPG 機制完整; 補 1 個遊戲化技能(跨領域高復用)。

### 7. Operational_Governance&Reporting — 中缺口 (孤兒類別, 建議補 ~2 個)
既有 4 技能: `Operational_Intelligence&Reporting`(SCQA 執行摘要) · `Incident_Lifecycle_Orchestration` · `Automation_Governance&Compliance_Audit` · `Session_Status_Bootloader`(KPI 快照)。

**0 筆 feeding(孤兒)**, 但專案有大量報告/治理 prompt 未被接(錯路由到 Operations/Data/Strategy/Finance): `Monthly Business Report Generator` · `Operational KPI Monitor` · `Progress Report Generator` · `Goal Achievement Post-Mortem` · `Local Market Update Report` · `Investor Report Builder` · `Tax Summary Report`。

- **Retrospective_PostMortem_Protocol** — 目標達成回顧 / 事件事後檢討。代表: `Goal Achievement Post-Mortem Analysis`(sc26) · `Incident`(由 Incident_Lifecycle 補, 但「事後回顧」未獨立)。
- **Operational_KPI_Monitor_Design** — 營運 KPI 監控與進度報告設計。代表: `Operational KPI Monitor and Analysis Report`(sc28) · `Progress Report Generator`(sc25) · `Monthly Business Report Generator`(sc26)。

> 結論: 既有的 `Operational_Intelligence&Reporting` 已涵蓋「資料→SCQA 摘要」, 但缺**回顧協議**與**KPI 監控設計**兩塊; 且本類別是孤兒(路由應修)。補 2 個。

### 8. UI_UX&Frontend_Engineering — 中缺口 (孤兒類別, 建議補 ~1 個)
既有 5 技能: `Design_DNA_Extraction` · `Frontend_Code_Materialization` · `Axiomatic_Design_System_Enforcement` · `Web_Performance_Optimization` · `Visual_QA_Verification`。

**0 筆 feeding(孤兒)**, 但專案 UI 類 prompt 極多(錯路由到 Art/Human_In_Loop/Visual_Architecture): `E-Commerce Wishlist UI Design` · `Multi-Step Checkout Flow UI` · `User Persona Document for UI/UX` · `Wireframe Design Plan` · `Mobile-First Layout` · `Search Bar Interface Design` · `Quick-View Product Card UI` · `Empty State UX` · `Microinteraction Design`。

- **UI_Interaction_Pattern_Synthesis** — 互動模式合成(F-pattern 橫幅/微互動/空狀態/結帳流程)。代表: `Banner Layout Design (F-Pattern)`(sc26) · `Microinteraction Design Strategy`(sc28) · `Empty State UX Design`(sc23) · `Multi-Step Checkout Flow UI`(sc25)。既有 5 個聚焦 DNA/程式碼/設計系統/效能/QA, **不含互動模式生成**。

> 結論: 既有 5 個已不錯; 補 1 個互動模式合成技能即可。同時本類別是孤兒, 路由應修。

### 9. Domain_Specific_Reasoning — 中缺口 (建議補 ~2–3 個)
既有 7 技能: `Reasoning_Type_Labeling` · `Framework_Constrained_Reasoning` · `Structural_Mapping_Analysis` · `Adversarial_Argument_Construction` · `Risk_Weighted_Strategic_Output` · `Heterogeneous_Agent_Team_Composition` · `Multi_Perspective_Simulation`。

342 筆 feeding(Research/Legal/Finance/Strategy…)是具體分析框架: SWOT / 文獻回顧 / 政策分析 / 競爭格局 / 回歸分析。既有 7 個是「**強制使用框架**」的元推理, 但**不內含特定框架**。抽象出少數高需求框架技能(勿全塞 342 筆):

- **SWOT_Competitive_Framework_Reasoner** — SWOT/競爭格局分析。代表: `SWOT Analysis`(sc27×多) · `Competitive Landscape Analysis Report`(sc29) · `Competitor Analysis Report`(sc29)。
- **Literature_Review_Synthesis_Logic** — 文獻回顧與綜述。代表: `Academic Literature Review Generator`(sc33) · `Academic Paper Analysis`(sc31) · `Research Paper Summary and Synthesis`(sc30)。
- **Policy_Impact_Assessment_Reasoner** — 政策/法規影響評估。代表: `Policy Analysis Synthesis Report`(sc37) · `Regulatory Impact Assessment`(sc28) · `Identify Critical Compliance Gaps`(sc27)。

> 結論: 元推理框架已足, 但熱門具體框架未實例化。補 2–3 個代表性框架技能。

### 10. Software_Architecture&Performance — 中弱缺口 (建議補 ~2 個)
既有 11 技能: `Domain_Boundary_Integrity` · `Unidirectional_Dependency_Boundary` · `Deep_Module_Interface_Design` · `Live_Terminology_Precision` · `Trade_off_Matrix_Rationalization` · `Static_Dynamic_Boundary` · `Terminal_Workflow_Optimization` · `CI_CD_Pipeline_Design` · `Database_Performance_Tuning_Logic` · `Physics_Kinetic_Narrative` · `Spatial_Geometry&Immersive`。

10 筆 feeding 多被涵蓋(`Database Query Optimization`/`Find Redundant Tables`→DB_Performance_Tuning; `Data Archiving`→部分)。缺口:

- **Frontend_Rendering_Perf_Logic** — 前端渲染效能(React 瓶頸)。代表: `React Rendering Bottleneck Optimizer`(sc22)。`Web_Performance_Optimization`(在 UI_UX 類)管 LCP/CLS, 但 React 渲染瓶頸未獨立。
- **Test_Case_Strategy_Design** — 整合/單元測試案例策略。代表: `Integration Test Case Generator`(sc28)。既有無測試策略技能。

> 結論: 既有 11 個已厚; 補 2 個小技能即可。

### 11–12. Strategic_Decision&Adversarial_Thinking / Data_Structuring&Engineering — 中弱缺口
- **Strategic_Decision&Adversarial_Thinking**(16 技能, 106 feed): 16 個對抗/策略思維已非常完整(機率/二階/第一性原理/對抗風險審計/外部性)。106 筆多為 SWOT/情境/風險 → 被元技能涵蓋。至多補 **Scenario_Planning_Protocol**(顯式情境樹+災難模擬, 與 Second_Order_Effect 有邊界) 1 個。
- **Data_Structuring&Engineering**(3 技能, 24 feed): `Data_ETL_Execution`+`Schema_Enforcer`+`Industry_Schema_Dynamic_Generator` 已很通用, 24 筆(合規清單/FAQ→KB/試算表)多被涵蓋。至多補 **Structured_Document_Transformation**(FAQ→KB、清單→矩陣等多文件結構轉換) 1 個。

### 13–16. 已涵蓋, 不值得補(或至多補 1 個弱項)
- **Visual_Architecture&Creative_Engineering**(12, 839): 839 筆 Art feed 幾乎全是 12 個元圖像技能(Style DNA / Spatial Fidelity / Instruction Compiler / Diagram / Mermaid / Canvas / Animation)的**變數實例** → 已涵蓋。至多補 `Photorealistic_Product_Shot_Composition`(電商產品攝影構圖) 1 個弱項。
- **Human_In_Loop_Workflow_Engineering**(18, 1337): 18 個人機協作元技能(分期/檢查點/RFC/插入卡/QA 閘)已極完整; 1337 筆是內容, 被元技能組裝 → 已涵蓋。無須補。
- **Interactive_Narrative&Creative_Fiction_Engine**(10, 58): 小說引擎 10 個技能完整; 58 筆是內容實例 → 已涵蓋。至多補 `Systematic_Rulebook_Engine`(交易playbook式系統化規則, 來自 Finance feed) 1 個弱項。
- **Persona&Narrative_Synthesis**(11, 15): 15 筆多為 persona/sensory/narrative 技能的具體實例 → 已涵蓋。至多補 `Sentiment_Aware_Reply_Coach`(情緒感知回覆, 來自 Sales feed) 1 個弱項。

### 17–20. 無技能級缺口(既有已涵蓋 / feed 錯路由)
- **Distributed_Cognition&Context_Orchestration**(14, 5): 14 個跨 session/handoff/記憶/身分技能已涵蓋完整空間; 專案無「上下文編排」能力可貢獻。5 筆 feed 皆錯路由(日記/資產負債表/房源描述) → **無缺口**。
- **Structured_Knowledge_Navigation_Architecture**(4, 6): 4 個知識導航技能已涵蓋小眾空間; 6 筆 feed 皆錯路由(肖像/日誌/whistleblower) → **無缺口**。
- **Agent_SOP_Framework&Extraction_Protocol**(5, 45): 5 個是「技能萃取 SOP」小眾技能; 45 筆 feed 是內容寫作(錯路由) → **無缺口**。
- **Academic_Insight&Forensics**(5, 1): 唯一 feed 是「房地產賣家名單分群」(錯路由, 非學術鑑識); 既有 5 個已涵蓋類別範圍 → **無缺口**。

---

## 行動建議(可執行清單)

**A. 真正值得補的候選新 skill(按優先級, 共 ~24 個)** — 這些是「技能級缺口」, 不是數量填充:

| 優先級 | 歸屬類別 | 建議新 skill 名 | 對應代表性專案 prompt(證據) |
|---|---|---|---|
| 高 | Domain_Specific_Expertise | Personal_Wealth_&_Tax_Planning_Logic | NPV Calc / Cross-Border Tax / Estate Planning |
| 高 | Domain_Specific_Expertise | Contract_Drafting_Logic | Contract Clause Library / Settlement / License |
| 高 | Domain_Specific_Expertise | Regulatory_Compliance_Doc_Generation | Privacy Policy / Compliance Report / Controls Matrix |
| 高 | Domain_Specific_Expertise | HR_Policy_Compliance_Logic | Essential HR Policies / Employment Law Compliance |
| 高 | Domain_Specific_Expertise | Real_Estate_Deal_Structuring_Logic | Leverage Risk / Appraisal Challenge / BRRRR |
| 高 | Domain_Specific_Expertise | SEO_Technical_Audit_Logic | Disavow Backlinks / Voice Search Schema / Keyword Clustering |
| 高 | Domain_Specific_Expertise | Data_Analysis_Pipeline_Logic | Merge Dataframes / Split-Apply-Combine / Prescriptive Analytics |
| 高 | Interactive_Pedagogy | Adaptive_Learning_Path_Synthesizer | Adaptive Learning Module / Custom Learning Path |
| 高 | Interactive_Pedagogy | Assessment_Item_Generator | Study Flashcard / Microlearning Module / Practice Exercise |
| 高 | Interactive_Pedagogy | Concept_Explanation_By_Analogy | Data Types w/ Analogies / Concept Simplifier |
| 高 | Self_Evolution | Iterative_Content_Revision_Protocol | Proofreading Coach / Incorporate Feedback / Article Rewriting |
| 高 | Self_Evolution | Process_QA_Audit_Loop | SOP Generator / QA Review / Process Improvement |
| 中 | Commercial_Growth | Landing_Page_Conversion_Architecture | Landing Page Copy / Product Page Optimization |
| 中 | Commercial_Growth | Lifecycle_Email_Sequence_Architecture | Abandoned Cart / Welcome / Nurturing Sequences |
| 中 | Commercial_Growth | Referral_Loop_Design | Referral Program / Referral Contest |
| 中 | Minimalist_Entrepreneur | Customer_Onboarding_&_Recovery_Flow_Design | Onboarding FAQ / Refund Script / Outage Response |
| 中 | RPG&Immersive | Gamification_Mechanic_Design | Loyalty Program / Badge / Streak Gamification |
| 中 | Operational_Gov | Retrospective_PostMortem_Protocol | Goal Post-Mortem / Incident Review |
| 中 | Operational_Gov | Operational_KPI_Monitor_Design | Operational KPI Monitor / Progress Report |
| 中 | UI_UX | UI_Interaction_Pattern_Synthesis | F-Pattern Banner / Microinteraction / Empty State |
| 中 | Domain_Specific_Reasoning | SWOT_Competitive_Framework_Reasoner | SWOT / Competitive Landscape |
| 中 | Domain_Specific_Reasoning | Literature_Review_Synthesis_Logic | Academic Literature Review / Paper Analysis |
| 低 | Software_Arch | Frontend_Rendering_Perf_Logic | React Rendering Bottleneck |
| 低 | Software_Arch | Test_Case_Strategy_Design | Integration Test Case Gen |

**B. 路由修正(與補 skill 同等重要)**: `UI_UX&Frontend_Engineering` 與 `Operational_Governance&Reporting` 是 **0 路由孤兒類別**, 但專案有大量對應 prompt(分別錯路由到 Art/Human_In_Loop 與 Operations/Data/Strategy)。`Commercial_Growth&Acquisition` 路由嚴重低估(Marketing+Sales 千筆塌陷進 Meta_Prompt)。建議同步修 `_search-index.json` 的 `related_skills` 映射, 讓這些類別能被正確接住。

**C. 不動**: 第 13–20 名類別(Visual_Architecture / Human_In_Loop / Interactive_Narrative / Persona&Narrative / Distributed_Cognition / Structured_Knowledge_Nav / Agent_SOP / Academic_Insight) — 既有技能已涵蓋或 feed 錯路由, **無須補 skill**。

---

## 與 v8/v9 的關係
- v8(數量): 指出「元類別過飽和 + 領域類別稀薄 + 2 孤兒類別」→ 本檔把「稀薄」落實為**具體值得補的 skill 清單**。
- v9(品質/模板去重): 指出 4,927 個不同模板缺具體技能(上限) → 本檔從中**篩出技能級缺口 ~24 個候選**, 並區分「已涵蓋(不補)」與「值得補」。
- 本檔結論: **skills.json 的技能級缺口集中在「具體領域專家層」(Domain_Specific_Expertise) 與「教學/自精進/獲取」三個執行層**, 而非 meta 層; 補這 ~24 個抽象技能即可顯著補齊, 且應同時修路由讓孤兒/低估類別接住真實需求。
