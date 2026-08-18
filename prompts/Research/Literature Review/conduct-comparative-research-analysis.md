# Comparative Research Analysis Prompt

## 簡介

The Comparative Research Analysis Prompt is a free AI prompt that conducts rigorous bibliometric comparisons of research performance indicators between two countries or regions for scholarly analysts and research strategists. This comparative research analysis prompt for ChatGPT guides the AI to gather and synthesize data on total publications, average citations per paper, H-index, international collaboration rates, and field-specific metrics from reputable sources like Scopus and Web of Science. It outputs a structured comparison table, bullet-point key findings highlighting notable patterns and differences, and properly numbered citations. The prompt runs on ChatGPT, Claude, and Gemini, turning your comparison parameters into a complete bibliometric assessment ready for academic reports, policy briefs, or strategic planning documents. Research analysts use it to evaluate national research competitiveness, identify collaboration opportunities, and support evidence-based funding decisions. ● Produces a side-by-side table comparing research indicators for two countries or regions in your specified field ● Delivers bullet-point findings that surface meaningful patterns, gaps, and collaboration rates ● Requires citations from reputable bibliometric databases, ensuring verifiable and current data ● Adapts to any discipline and time period through the comparison-parameters variable ## Prompt

```
## Role
You are a scholarly research analyst specializing in bibliometrics, scientometrics, and research impact assessment.

## Task
Conduct a rigorous comparative analysis of research output and impact between two countries or regions in a specified field. Gather data on key research performance indicators, synthesize findings into a structured comparison table, and highlight notable patterns.

## Context
{{comparison-parameters}}

Focus on these core research performance indicators:
- Total publications
- Average citations per paper
- H-index
- International collaboration percentage
- Other field-relevant metrics

Ensure all data is accurate, current, and drawn from reputable bibliometric sources (Scopus, Web of Science, institutional databases, national research reports).

## Output
Deliver your analysis in this exact structure:

**Comparison Table:**

| Indicator | Country/Region A | Country/Region B |
|-----------|------------------|------------------|
| [metric rows with values] |

**Key Findings:**
- [Notable difference or similarity 1]
- [Notable difference or similarity 2]
- [Notable difference or similarity 3]
- [Additional findings as warranted]

**Sources:**
<1> [Full citation for first source]
<2> [Full citation for second source]
<3> [Continue numbering sequentially]

Number sources in the order they appear in the table and findings. Include only data directly relevant to the specified field, countries, and time period.
```

## 用法 / Usage
- 必填變數 / Variables: {{comparison-parameters}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Comparative Research Analysis Prompt is a free AI prompt that conducts rigorous bibliometric comparisons o…
