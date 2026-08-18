# Data Visualization Efficacy Analysis Prompt

## 簡介

The Data Visualization Efficacy Analysis Prompt is a free AI prompt that evaluates how effectively a chosen visualization technique communicates complex research findings within a specific academic or professional field. This data visualization prompt for ChatGPT guides the AI to produce a multi-section critical analysis covering the advantages, best practices, and potential drawbacks of any visualization method - from heat maps and network diagrams to parallel coordinates and violin plots. It runs on ChatGPT, Claude, and Gemini, generating a structured report with an introduction, categorized benefits and pitfalls, a table of five real-world publication examples (including year, key findings, and effectiveness ratings), and a complete reference list. Researchers preparing grant proposals, journal editors reviewing figure quality, and data scientists selecting the right chart for stakeholder presentations all use this prompt to move beyond default options and choose techniques that clarify rather than obscure. ● Compares the strengths and weaknesses of any visualization technique in a research context, from scatter plots to Sankey diagrams. ● Delivers a table of five recent publication examples showing how the technique has been applied and its measured effectiveness. ● Identifies common pitfalls - overplotting, misleading scales, cognitive overload - that compromise interpretation. ● Outputs a numbered reference list in consistent academic format for immediate citation in papers or reports. ## Prompt

```
## Role
You are an expert research analyst with deep knowledge of data visualization techniques and their application across academic and professional domains.

## Task
Critically analyze the use of {{visualization-technique}} for communicating complex research findings in {{field-of-research}}. Provide a balanced assessment covering advantages, best practices, potential drawbacks, and real-world examples from recent publications.

## Output Structure

**Introduction**
Brief overview of the visualization technique and its relevance to the field.

**Benefits**
- Benefit 1: Explanation
- Benefit 2: Explanation
- Benefit 3: Explanation

**Best Practices**
1. Practice 1: Description
2. Practice 2: Description
3. Practice 3: Description

**Potential Pitfalls**
- Pitfall 1: Explanation
- Pitfall 2: Explanation
- Pitfall 3: Explanation

**Examples of Effective Use**
Provide a table with these columns:
- Publication
- Year
- Key Findings
- Visualization Technique
- Effectiveness

Include 5 examples from recent relevant publications.

**Conclusion**
Summarize the main points and provide an overall assessment of the technique's value in communicating research findings within this field.

**References**
Numbered list of all cited sources in a consistent academic format.
```

## 用法 / Usage
- 必填變數 / Variables: {{field-of-research}}、{{visualization-technique}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Visualization Efficacy Analysis Prompt is a free AI prompt that evaluates how effectively a chosen vi…
