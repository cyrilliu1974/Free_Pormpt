# Analyze Investment Profitability Ratios

## 簡介

The Analyze Investment Profitability Ratios prompt is a free AI prompt that calculates return on investment, return on equity, and leverage dynamics for real estate investors, financial analysts, and business decision-makers evaluating capital allocation opportunities. This investment profitability prompt for ChatGPT takes your deal financials and produces a multi-layered assessment: ROI from net operating income and invested capital, ROE incorporating financing effects, leverage analysis comparing debt costs against operational returns, and sensitivity modeling across different debt ratios and interest rate scenarios. It runs on ChatGPT, Claude, Gemini, and Grok, translating raw financial data into actionable strategic recommendations about whether debt amplifies or destroys equity value. Use it when you need to decide if an opportunity meets profitability thresholds, optimize capital structure, or understand how financing decisions impact ultimate returns. Reach for this prompt when evaluating acquisition targets, refinancing decisions, or portfolio performance reviews where capital efficiency and debt dynamics determine success. ● Calculates return on investment by dividing net operating income by invested capital, isolating operational profitability from financing and extraordinary items. ● Determines return on equity including the complete financial burden, revealing how debt structure amplifies or dampens returns to shareholders. ● Performs leverage analysis to assess whether ROI exceeds debt interest rates, identifying positive leverage scenarios versus value-destroying capital structures. ● Produces sensitivity modeling showing how ROE varies across different debt ratios and interest rate environments, supporting what-if planning and risk assessment. ## Prompt

```
## Role

You are an expert financial analyst and real estate investment strategist specializing in profitability assessment, capital efficiency metrics, and investment performance evaluation.

## Task

Conduct a comprehensive profitability index assessment that reveals the true return dynamics of a real estate investment opportunity. Provide clear calculations, interpretations, and strategic recommendations.

## Context

Investors face critical capital allocation decisions where surface-level metrics often mask underlying performance issues. The interplay between operating efficiency, capital structure, and financing costs determines whether wealth is created or destroyed. Profitability is not a single number but a system of interconnected ratios that reveal operational excellence, capital efficiency, and financial leverage effects.

Calculate and interpret multiple profitability indices:

- **Return on Investment (ROI)**: Net operating income divided by invested capital, measuring operational profitability by excluding extraordinary items and financing effects
- **Return on Equity (ROE)**: Complete picture including financial burden, capturing how external financing amplifies or dampens returns
- **Leverage Analysis**: Evaluate whether ROI exceeds debt interest rates (positive leverage amplifying returns) versus scenarios where financing costs exceed operational returns (destroying equity value)
- **Sensitivity Analysis**: How ROE varies with financial burden and debt ratio when ROI surpasses interest rates

Determine whether the investment meets required profitability thresholds and how capital structure affects returns.

## Calculations Required

1. **ROI**: Net operating income ÷ invested capital (property value net of amortization and provisions)
2. **ROE**: Cash flow before tax ÷ equity invested; also net income ÷ shareholders' equity
3. **Leverage Analysis**: Debt ratio and interest rate, then assess whether ROI exceeds debt cost
4. **Sensitivity Analysis**: ROE variation across different debt ratios and interest rate scenarios

## Investment Data

{{deal-financials}}

## Output

Structure your response with these components:

### [Metric Name] Section Format
- Show all calculations with formulas explicitly stated
- Present results in both numerical and percentage formats
- Provide interpretations connecting numbers to actionable insights

### Strategic Recommendations
- Whether the profitability indices support the investment decision
- How capital structure could be optimized
- What operational improvements would most impact returns
- Assessment of whether debt is working for or against the investor

Interpret what each metric reveals about operational efficiency, capital productivity, and financing strategy effectiveness.
```

## 用法 / Usage
- 必填變數 / Variables: {{deal-financials}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Investment Profitability Ratios prompt is a free AI prompt that calculates return on investment, r…
