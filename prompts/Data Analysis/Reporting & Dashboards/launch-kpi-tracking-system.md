# KPI Tracking System Design Prompt

## 簡介

The KPI Tracking System Design Prompt is a free AI prompt that generates a complete, scalable analytics architecture for businesses seeking to track performance metrics and enable data-driven decision-making. This KPI tracking system prompt for ChatGPT walks through your specific business scenario and delivers a structured blueprint covering critical performance indicators, data source identification, end-to-end system architecture (ingestion, processing, storage, and reporting layers), visualization platform recommendations, and a phased implementation roadmap. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across major text AI platforms. Use it when launching a new analytics capability, consolidating fragmented reporting, or aligning metrics with strategic goals across teams. ● Identifies 1-5 KPIs most critical to the business domain and strategic objectives ● Proposes four-layer system architecture covering data ingestion, processing, storage, and analytics ● Recommends three data visualization platforms with rationale specific to the use case ● Delivers a five-step implementation roadmap with timelines, dependencies, and success criteria for the first 90 days ## Prompt

```
## Role
You are a business analytics expert specializing in designing comprehensive KPI tracking and analytics systems across multiple industries.

## Task
Design a robust, scalable business analytics system tailored to the user's specific scenario. Identify relevant KPIs, propose system architecture for data capture and processing, recommend visualization tools, and provide an implementation roadmap.

## Context
Business scenario: {{business-scenario}}

Consider the industry vertical, company scale, existing infrastructure constraints, and strategic objectives when designing the solution.

## Output
Structure your response with these sections:

**Business Domain**
[Summarize the domain and its analytics maturity]

**Key Performance Indicators**
1-5 KPIs most critical to this domain and aligned with stated goals

**Data Sources**
Internal systems, external feeds, and third-party platforms needed

**System Architecture**
- Data Ingestion Layer: Collection methods and ETL processes
- Data Processing Layer: Transformation, enrichment, and business logic
- Data Storage Layer: Database design and data warehouse strategy
- Analytics and Reporting Layer: Query engines and analytical capabilities

**Data Visualization Tools**
3 recommended platforms with rationale for this use case

**Implementation Roadmap**
5-step phased deployment plan with timelines and dependencies

**Expected Benefits**
Quantify improvements in decision speed, operational efficiency, and strategic insight

**Potential Challenges**
Technical, organizational, and data quality obstacles with mitigation strategies

**Recommendations**
Prioritized next steps and success criteria for the first 90 days
```

## 用法 / Usage
- 必填變數 / Variables: {{business-scenario}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The KPI Tracking System Design Prompt is a free AI prompt that generates a complete, scalable analytics archit…
