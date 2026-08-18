# Report Comparison Insights Prompt for Data Analysis

## 簡介

The Report Comparison Insights Prompt for Data Analysis is a free AI prompt that enables data analysts to systematically compare multiple reports and extract meaningful trends, patterns, and metric discrepancies. This report comparison prompt for ChatGPT guides the AI to act as an experienced data analyst who evaluates quantitative metrics across user-supplied reports, calculates percentage changes and growth rates, flags outliers and anomalies, and surfaces correlations between different data points. You provide your industry context and the reports with their date ranges and key metrics (revenue, conversion rate, customer acquisition cost, etc.), and the prompt returns a six-part markdown analysis: introduction, reports overview, comparison table, key insights in bullet form, detailed observations with external context, and a summary conclusion. It runs on ChatGPT, Claude, and Gemini, making it easy to drop in your datasets and receive consistent, shareable output. Reach for this prompt whenever you need to synthesize findings from quarterly reports, A/B test results, regional performance data, or any set of documents where side-by-side metric comparison will reveal strategic insights. ● Produces a markdown comparison table that aligns metrics across all supplied reports for at-a-glance review. ● Highlights percentage changes, growth rates, and statistical outliers without requiring manual spreadsheet formulas. ● Identifies correlations between metrics and considers external factors that may explain variances. ● Delivers findings in a six-section format (introduction, overview, table, key insights, detailed observations, conclusion) optimized for sharing with executives and teams. ## Prompt

```
## Role
You are an experienced data analyst skilled in interpreting and comparing complex reports to extract meaningful insights and trends.

## Task
Compare results across the provided reports to identify significant trends, patterns, and discrepancies. Focus on quantitative metrics that can be directly compared, highlight percentage changes or growth rates, identify outliers or anomalies, and look for correlations between different metrics. Avoid making assumptions without supporting data and prioritize the most impactful insights.

## Context
Industry: {{industry}}

Reports to compare: {{reports-and-metrics}}
(Include report names, date ranges, and the key metrics you want analyzed—e.g., revenue, conversion rate, customer acquisition cost, etc.)

## Output
Present your analysis in the following structured markdown format:

1. **Introduction**: Brief overview of the analysis objective
2. **Reports Overview**: List of reports being compared with their key characteristics
3. **Comparison Table**: Markdown table presenting key metrics and their values across reports
4. **Key Insights**: Bullet points highlighting the most significant findings
5. **Detailed Observations**: Short paragraphs explaining notable trends, correlations, or discrepancies; consider external factors that might influence variations
6. **Conclusion**: Summary of the main takeaways from the comparison
```

## 用法 / Usage
- 必填變數 / Variables: {{industry}}、{{reports-and-metrics}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Report Comparison Insights Prompt for Data Analysis is a free AI prompt that enables data analysts to syst…
