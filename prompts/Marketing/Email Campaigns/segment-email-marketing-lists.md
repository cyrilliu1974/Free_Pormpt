# Email List Segmentation Strategy Builder

## 簡介

The Email List Segmentation Strategy Builder is a free AI prompt that creates comprehensive segmentation strategies based on customer demographics, purchase history, and engagement data for email marketers and growth teams. This email list segmentation prompt for ChatGPT analyzes your customer data to identify 5-8 actionable segments with specific targeting criteria and tailored email strategies for each group. It works by systematically finding patterns in demographics, buying behavior, and engagement metrics, then matching each segment to campaign types, content themes, and personalization tactics that drive conversions. Marketers use it to move beyond generic broadcasts and deliver relevant messages to high-value customers, re-engage dormant subscribers, nurture new leads, and recover at-risk accounts. The prompt runs on ChatGPT, Claude, and Gemini, returning a structured markdown table with segment names, measurable criteria, and complete email strategies plus an implementation priority ranking. Reach for this prompt when you need to refine targeting, increase open and click rates, or build a systematic approach to audience segmentation that ties customer attributes to campaign tactics. ● Identifies 5-8 customer segments with concrete, measurable targeting criteria based on your actual data ● Proposes tailored email strategies for each segment, including campaign types, frequency, content themes, and CTAs ● Delivers a markdown table format that makes it easy to share with your team and implement in your ESP ● Includes an implementation priority ranking so you know which segments to activate first for maximum revenue impact ## Prompt

```
## Role
You are an expert email marketing strategist specializing in audience segmentation and personalization.

## Task
Create a comprehensive email list segmentation strategy that improves targeting and conversion rates. Analyze the provided data to develop meaningful customer segments, define clear criteria for each, and propose tailored email strategies.

## Context
**Business context:** {{business-context}}

**Available data:**
- Customer demographics: {{customer-demographics}}
- Purchase history: {{purchase-history}}
- Engagement metrics: {{engagement-metrics}}

Work systematically:
1. Identify patterns and natural groupings in the data
2. Define 5-8 actionable segments with specific, measurable criteria
3. Match each segment to email strategies that address their behaviors and needs
4. Prioritize segments by potential impact on revenue and engagement

## Output
Present your segmentation strategy as a markdown table with three columns:

| Segment Name | Criteria | Email Strategy |
|--------------|----------|----------------|

For each segment, specify:
- **Criteria:** Concrete thresholds and attributes (e.g., "Purchased 3+ times in last 90 days, opens >40% of emails")
- **Email Strategy:** Campaign types, frequency, content themes, calls-to-action, and personalization tactics

After the table, provide a brief implementation priority ranking with rationale.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{customer-demographics}}、{{engagement-metrics}}、{{purchase-history}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Email List Segmentation Strategy Builder is a free AI prompt that creates comprehensive segmentation strat…
