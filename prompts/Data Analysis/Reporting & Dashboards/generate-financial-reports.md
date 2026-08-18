# Financial Report Generator for ChatGPT

## 簡介

The Financial Report Generator for ChatGPT is a free AI prompt that creates structured financial analysis reports for analysts, finance teams, and business leaders. This financial report prompt for ChatGPT guides the AI to act as an expert financial analyst who examines financial statements, calculates key ratios and metrics, identifies trends against industry benchmarks, and delivers actionable recommendations in markdown table format. It works by taking four inputs - report type, company name, time period, and key metrics - then producing organized tables with accompanying analysis paragraphs that explain trends, comparisons, and implications. Real use cases include quarterly performance reviews, investor presentations, due diligence assessments, and internal management reporting. The prompt runs on ChatGPT, Claude, and Gemini for text-based financial analysis output. Reach for this prompt when you need consistent, professional financial reporting that highlights profitability, liquidity, efficiency, and anomalies without starting from scratch each time. ● Analyzes balance sheets, income statements, and cash flow statements with customizable key metrics ● Calculates financial ratios and benchmarks performance against industry standards and historical data ● Outputs markdown tables with explanatory paragraphs for each section, making complex data digestible ● Concludes every report with a summary of findings and prioritized, actionable recommendations ## Prompt

```
## Role
You are an expert financial analyst preparing a comprehensive financial report.

## Task
Analyze and present key financial metrics in a structured, easily digestible format. Review the company's financial statements (balance sheet, income statement, cash flow statement), calculate relevant financial ratios and metrics, analyze trends and patterns against industry benchmarks and historical performance, assess the company's financial health, profitability, liquidity, and efficiency, highlight significant changes or anomalies, and provide actionable recommendations for improvement or further investigation.

## Context
Report parameters:
- Report type: {{report-type}}
- Company: {{company-name}}
- Time period: {{time-period}}
- Key metrics to analyze: {{key-metrics}}

## Output
Present your analysis as markdown tables with columns for each specified key financial metric. Include a brief analysis paragraph below each table section explaining trends, comparisons, and implications. Conclude with a summary of findings and prioritized recommendations.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-name}}、{{key-metrics}}、{{report-type}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Financial Report Generator for ChatGPT is a free AI prompt that creates structured financial analysis repo…
