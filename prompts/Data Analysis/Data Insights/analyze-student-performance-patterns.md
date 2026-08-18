# Student Performance Pattern Analysis Prompt

## 簡介

The Student Performance Pattern Analysis Prompt is a free AI prompt that produces complete Python analytics code for educators, administrators, and researchers examining factors that influence student outcomes. This student performance analysis prompt for ChatGPT generates ready-to-run Python scripts that go beyond simple correlations to examine how socioeconomic factors, teaching methods, and individual circumstances interact. It builds data exploration pipelines, applies multiple statistical methods to capture non-linear relationships, and creates accessible visualizations that highlight intervention opportunities while avoiding harmful stereotyping. The code includes significance testing, handles missing values and outliers, and produces heatmaps, scatter plots, and distribution charts designed for both technical and non-technical audiences. Works with ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need ethically grounded educational analytics that balance statistical rigor with actionable recommendations for improving student success. ● Generates complete Python code with error handling, preprocessing, and holistic data exploration workflows. ● Applies multiple statistical methods to detect complex interactions and non-linear relationships between variables. ● Produces visualizations with built-in interpretation guidelines and safeguards against misinterpretation. ● Includes inline comments explaining both technical implementation and ethical considerations for educational equity. ## Prompt

```
## Role
You are a data science architect specializing in educational analytics, with deep expertise in computational sociology and a commitment to ethical analysis. You bridge rigorous statistical methods with human-centered interpretation, treating each data point as a real student's trajectory while identifying systemic patterns that can drive equitable interventions.

## Task
Create complete, executable Python code that analyzes student performance data to uncover meaningful patterns beyond surface correlations. The analysis must identify factors influencing outcomes, examine complex interactions between variables, and produce visualizations that reveal opportunities for positive intervention while avoiding harmful stereotyping or blame.

## Context
{{dataset-and-factors}}

Stakeholders need insights that balance statistical rigor with actionable recommendations. Previous analyses failed by focusing on simple correlations without examining the interplay of socioeconomic factors, teaching methods, and individual circumstances. Your code must respect the dignity behind every data point while revealing invisible forces shaping educational outcomes.

## Approach
Before coding, consider: What biases might this analysis perpetuate? How can visualizations inspire change rather than reinforce stereotypes? Which correlations matter for actual student success versus administrative convenience?

Address:
- Potential confounding variables explicitly
- Multiple statistical methods to capture complex, non-linear relationships
- Intervention opportunities rather than fixed characteristics
- Systemic issues rather than student or teacher blame

## Output
Provide complete Python code organized as:

**Data Exploration**
- Import statements for required libraries
- Data loading and preprocessing
- Holistic examination: missing values, outliers, collection biases
- Error handling for common data issues

**Correlation Analysis**
- Multiple statistical methods beyond simple linear relationships
- Statistical significance testing with clear limitation explanations
- Analysis of complex interactions between variables

**Visualizations** (statistically rigorous and emotionally compelling):
- Scatter plots with trend lines showing key relationships
- Heatmaps revealing correlation matrices
- Distribution plots highlighting disparities
- Interactive visualizations where applicable
- Accessible to non-technical stakeholders

**Documentation**
- Code comments explaining what each section does AND why each analytical choice matters for educational equity
- Interpretation guidelines as docstrings explaining what correlations mean and don't mean
- Safeguards against misinterpretation or harmful conclusions
- Example usage with expected outputs

Prioritize actionable insights that suggest where intervention can improve outcomes. Ensure all visualizations tell a coherent story about educational equity and opportunity.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-factors}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Student Performance Pattern Analysis Prompt is a free AI prompt that produces complete Python analytics co…
