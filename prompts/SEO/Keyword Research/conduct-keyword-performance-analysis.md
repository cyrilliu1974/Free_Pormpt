# Keyword Performance Analysis Prompt for Google Analytics

## 簡介

The Keyword Performance Analysis Prompt for Google Analytics is a free AI prompt that analyzes website keyword data to identify high-performing and underperforming search terms for SEO strategists and site owners. This keyword research prompt for ChatGPT processes your Google Analytics export and surfaces the top 5 keywords driving traffic alongside up to 3 underperforming terms that need attention. It evaluates clicks, impressions, click-through rate, and average position to deliver a structured report with specific, actionable recommendations tailored to your actual content. The prompt runs on ChatGPT, Claude, and Gemini, transforming raw analytics data into concrete optimization strategies you can implement immediately. Reach for this prompt when you need to turn Google Analytics keyword data into clear action items without spending hours manually comparing metrics and brainstorming fixes. ● Identifies your 5 best-performing keywords with full metrics (clicks, impressions, CTR, position) so you can double down on what works ● Flags underperforming keywords and provides targeted recommendations for each, not generic advice ● Outputs a scannable report format that separates winners from opportunities, making triage instant ● Focuses on click-through rate, conversion rate, and bounce rate as the primary performance indicators ## Prompt

```
## Role
You are an expert Google Analytics user and keyword strategist who analyzes website performance data to uncover SEO optimization opportunities.

## Task
Conduct a thorough analysis of keyword performance using the provided Google Analytics data. Identify the top 5 performing keywords and up to 3 underperforming keywords based on clicks, impressions, CTR, and average position. Summarize findings in a scannable format and provide actionable, specific recommendations tailored to the website's content.

## Context
{{analytics-data}}

Focus on click-through rate, conversion rate, and bounce rate as primary indicators. Avoid generic advice—recommendations must be concrete strategies the user can implement immediately.

## Output
Format your analysis as follows:

**Website:** [Extract from data]

**Analysis Period:** [Date range from data]

**Top 5 Performing Keywords:**
1. [Keyword 1] ✅
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]

2. [Keyword 2] ✅
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]

3. [Keyword 3] ✅
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]

4. [Keyword 4] ✅
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]

5. [Keyword 5] ✅
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]

**Underperforming Keywords & Recommendations:**
1. [Keyword 1] ❌
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]
   - **Recommendation:** [Specific, actionable strategy]

2. [Keyword 2] ❌
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]
   - **Recommendation:** [Specific, actionable strategy]

3. [Keyword 3] ❌
   - Clicks: [NUMBER]
   - Impressions: [NUMBER]
   - CTR: [PERCENTAGE]
   - Avg. Position: [NUMBER]
   - **Recommendation:** [Specific, actionable strategy]
```

## 用法 / Usage
- 必填變數 / Variables: {{analytics-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Keyword Performance Analysis Prompt for Google Analytics is a free AI prompt that analyzes website keyword…
