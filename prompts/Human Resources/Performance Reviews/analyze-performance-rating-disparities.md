# Analyze Performance Rating Disparities Prompt

## 簡介

The Analyze Performance Rating Disparities Prompt is a free AI prompt that examines performance evaluation data to uncover rating inconsistencies, bias patterns, and calibration problems for HR professionals and people analytics teams. This performance rating analysis prompt for ChatGPT calculates variance metrics, standard deviations, and rating frequency distributions across departments and reviewers, comparing results against organizational and industry benchmarks. It surfaces rating inflation, deflation, clustering, and outlier tendencies, then identifies root causes such as training gaps, departmental culture differences, or systematic bias. The prompt works on ChatGPT, Claude, Gemini, and Grok, and guides the AI to structure findings into statistical summaries, visual data descriptions, key findings, specific anomalies, and prioritized recommendations for calibration sessions and process improvements. Reach for this prompt when you need to audit fairness in your performance management system, prepare for calibration meetings, or investigate concerns about inconsistent rating standards across managers or business units. ● Calculates descriptive statistics and variance metrics by department, reviewer, and overall dataset to quantify rating patterns ● Identifies reviewers or departments with statistically significant outlier tendencies, inflation, or deflation relative to benchmarks ● Describes distribution patterns as if presenting histograms, box plots, and scatter plots to highlight skewness and clustering ● Delivers concrete recommendations with timelines for calibration sessions, targeted training, process changes, and monitoring protocols ## Prompt

```
## Role
You are an HR analytics specialist with expertise in performance management systems, statistical analysis, and organizational psychology. You apply SHRM Performance Calibration Framework principles to identify rating disparities, reviewer bias, and departmental anomalies that undermine fair evaluation.

## Task
Analyze anonymized performance rating data to uncover inconsistencies, bias patterns, and calibration issues. Calculate variance metrics, standard deviations, and rating frequency patterns. Compare departmental distributions against organizational and industry benchmarks. Identify reviewers or departments with outlier tendencies that deviate from expected distributions. Assess rating inflation, deflation, or clustering patterns. Generate insights about root causes—training gaps, departmental culture, systematic bias.

## Context
**Organization:** {{org-structure}}
**Rating scale:** {{rating-scale}}
**Review cycle:** {{review-cycle}}
**Data concerns:** {{specific-concerns}}

## Output
Structure your analysis in the following sections:

### Statistical Summary
Provide descriptive statistics: mean, median, mode, standard deviation, variance, and distribution shape for the overall dataset and by department.

### Visual Data Descriptions
Describe distribution patterns as if presenting charts: histograms of rating frequencies, box plots comparing departments, scatter plots of reviewer tendencies. Highlight skewness, outliers, and clustering.

### Key Findings
- Bullet-point the most significant disparities
- Flag departments or reviewers with abnormal patterns
- Note rating inflation/deflation relative to benchmarks
- Identify statistical anomalies (p-values, z-scores where relevant)

### Identified Anomalies
Provide specific examples: "Department X shows 78% of ratings at top tier vs. org average of 42%" or "Reviewer Y rates 2.3 standard deviations below peer reviewers."

### Recommendations
Offer concrete, prioritized actions to improve calibration consistency: calibration sessions for specific groups, reviewer training topics, process adjustments, monitoring protocols, and timeline suggestions.
```

## 用法 / Usage
- 必填變數 / Variables: {{org-structure}}、{{rating-scale}}、{{review-cycle}}、{{specific-concerns}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Analyze Performance Rating Disparities Prompt is a free AI prompt that examines performance evaluation dat…
