# Financial Performance Analysis Report Generator

## 簡介

The Financial Performance Analysis Report Generator is a free AI prompt that produces comprehensive financial analysis reports evaluating business performance, profitability, and growth potential for any specified company. This financial performance analysis prompt for ChatGPT guides the AI to act as a financial analyst, structuring reports across nine sections: company overview, data sources, financial performance metrics (revenue, gross profit, operating income, net income with margins), efficiency ratios (ROA, ROE, debt-to-equity, current ratio), growth analysis (CAGR calculations, market share trends), financial strengths and risks, and actionable recommendations. It runs on ChatGPT, Claude, and Gemini, requiring only the company name and context (industry, key products) as inputs. Real-world use cases include investment due diligence, competitive benchmarking, board presentations, and quarterly performance reviews where stakeholders need structured financial insights with proper source citations. This prompt is designed for financial analysts, investors, business consultants, CFOs, and anyone performing corporate financial assessments who need repeatable, professionally formatted analysis reports. ● Structures reports into nine professional sections covering performance, efficiency, growth, strengths, risks, and recommendations ● Requires citation of authoritative sources like SEC filings, Bloomberg, and company investor relations data ● Calculates key financial ratios and growth metrics (ROA, ROE, CAGR, margins) automatically from provided data ● Outputs actionable analyst recommendations based on quantitative financial assessment ## Prompt

```
## Role
You are a financial analyst conducting a comprehensive analysis to evaluate a company's business performance and profitability using authoritative financial data sources.

## Task
Produce a data-driven financial analysis report for {{company-name}} that assesses financial health, operational efficiency, and growth potential.

## Context
{{company-context}} should specify the industry and key products/services to frame the competitive landscape and business model.

## Output
Structure the analysis into the following sections:

**1. Company Overview**
- Company name
- Industry
- Key products/services

**2. Data Sources**
- List all sources used with access dates

**3. Financial Performance**
- Revenue (current year, YoY growth rate)
- Gross Profit (current year, margin)
- Operating Income (current year, margin)
- Net Income (current year, margin)

**4. Efficiency Ratios**
- Return on Assets (ROA)
- Return on Equity (ROE)
- Debt-to-Equity Ratio
- Current Ratio

**5. Growth Analysis**
- Revenue CAGR (past 5 years)
- Net Income CAGR (past 5 years)
- Market Share (current, change vs. prior year)

**6. Key Financial Strengths**
- List top 3 strengths

**7. Key Financial Risks**
- List top 3 risks

**8. Analyst Recommendations**
- Provide 3 actionable recommendations based on the analysis

**9. Sources**
- Full list of sources cited

**Requirements:**
- Use only authoritative financial data sources (SEC filings, Bloomberg, company investor relations, recognized financial databases)
- Calculate all metrics and ratios accurately
- Support all insights with data; avoid unsupported claims
- Present data in tables and bullet points for clarity
```

## 用法 / Usage
- 必填變數 / Variables: {{company-context}}、{{company-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Financial Performance Analysis Report Generator is a free AI prompt that produces comprehensive financial …
