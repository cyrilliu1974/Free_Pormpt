# CTR Analysis and Monitoring Strategy for Keywords

## 簡介

The CTR Analysis and Monitoring Strategy for Keywords is a free AI prompt that develops a complete click-through rate tracking system for websites and their primary keywords. This keyword CTR analysis prompt for ChatGPT guides web analytics engineers and SEO professionals through building a multi-layer monitoring solution: it defines the tracking schema (data collection methodology, database architecture, correlation techniques), designs a visual dashboard (trend graphs, performance indicators, summary tables, and keyword clouds), and delivers data-driven insights paired with specific recommendations. The prompt runs on ChatGPT, Claude, and Gemini, using custom performance thresholds to automatically flag effective and underperforming keywords with visual markers. Real use cases include monitoring organic search performance after content updates, tracking keyword cannibalization, and identifying which terms drive engagement versus which need optimization. Reach for this prompt when you need a structured approach to keyword-level CTR tracking that goes beyond raw numbers to visualization and action steps. ● Creates a tracking schema that specifies tools, data collection intervals, database design, and methods to correlate CTR shifts with content changes ● Designs a dashboard with trend line graphs, threshold-based visual indicators, summary statistics tables, and keyword clouds sized by average CTR ● Generates 3-5 paired insights and recommendations grounded in the actual data patterns and performance thresholds you define ● Accepts custom effectiveness and poor-performance thresholds so the analysis adapts to your industry benchmarks and goals ## Prompt

```
## Role
You are an expert web analytics engineer specializing in click-through rate (CTR) tracking and analysis for websites.

## Task
Develop a comprehensive CTR monitoring system for {{website-url}} that includes:
1. A tracking schema for primary keywords
2. A dashboard design that visualizes trends and outliers
3. Actionable recommendations based on the analysis

## Context
Primary keywords to monitor: {{primary-keywords}}

Performance thresholds:
- Effective CTR: ≥{{effectiveness-threshold}}% (mark with ✅)
- Poor CTR: <{{poor-performance-threshold}}% (mark with ❌)

## Output
Deliver your analysis in this structure:

**Website URL:** {{website-url}}

**Primary Keywords:**
- List each keyword from the provided set

**Tracking Schema:**
1. Tracking tool setup for each primary keyword
2. Daily CTR data collection methodology and timeframe
3. Database architecture for data storage
4. Analysis techniques for identifying trends and outliers
5. Method to correlate CTR changes with content management system keyword updates

**Dashboard Design:**
- Line graph: daily CTR trends per keyword with keyword update markers
- Visual indicators: ✅ for CTRs ≥{{effectiveness-threshold}}%, ❌ for CTRs <{{poor-performance-threshold}}%
- Summary table: Keyword | Average CTR | Highest CTR | Lowest CTR
- Word cloud: keywords sized by average CTR

**Insights and Recommendations:**
Provide 3-5 data-driven insights, each paired with a specific, actionable recommendation for improving CTR performance.
```

## 用法 / Usage
- 必填變數 / Variables: {{effectiveness-threshold}}、{{poor-performance-threshold}}、{{primary-keywords}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CTR Analysis and Monitoring Strategy for Keywords is a free AI prompt that develops a complete click-throu…
