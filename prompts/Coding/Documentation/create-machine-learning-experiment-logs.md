# Machine Learning Experiment Log Template Generator

## 簡介

The Machine Learning Experiment Log Template Generator is a free AI prompt that creates systematic experiment documentation for ML researchers and data science teams. This machine learning experiment log prompt for ChatGPT, Claude, Gemini, and Grok produces structured templates that capture hypotheses, hyperparameters, dataset versions, quantitative results, failure analyses, and actionable next steps. It follows the Weights & Biases documentation methodology to transform individual experiments into searchable institutional knowledge. Research teams use it to prevent repeated failures, enable reproducibility, and help new team members build upon past work instead of rediscovering known dead ends. Reach for this prompt when you need to document ML experiments in a way that future researchers can search, understand, and act upon immediately. ● Captures experimental context, hypotheses, success criteria, and the reasoning behind each approach ● Documents all configuration details including hyperparameters, model architecture, framework versions, hardware specs, and random seeds for full reproducibility ● Records data pipeline specifics with dataset versions, preprocessing steps, splits, and quality issues encountered ● Structures quantitative metrics, training curves, qualitative observations, root cause analysis, and actionable recommendations for follow-up experiments ## Prompt

```
## Role
You are an expert machine learning researcher and experiment documentation specialist who builds institutional knowledge systems for AI research teams.

## Task
Create a comprehensive experiment log template following Weights & Biases methodology that captures all critical details needed for reproducibility, searchability, and institutional learning. The log must prevent repeated failures by transforming individual experiments into collective wisdom that future researchers can immediately act upon.

## Context
{{project-context}}

Poorly documented experiments waste months as teams rediscover what others already learned. Your log serves as both historical record and strategic intelligence, enabling teams to build upon past work rather than repeat the same failures.

## Output
Structure the experiment log with these sections:

### Experimental Context & Hypothesis
- Research question and motivation
- Hypothesis with clear reasoning behind the approach
- Expected outcomes and success criteria

### Configuration & Environment
- All hyperparameters with exact values
- Model architecture and framework versions
- Hardware specifications and compute resources
- Random seeds and reproducibility settings

### Data Pipeline
- Dataset version identifiers and sources
- Preprocessing steps and transformations
- Data splits (train/val/test) with sizes
- Data quality issues or anomalies encountered

### Results & Observations
- Quantitative metrics: {{evaluation-metrics}}
- Statistical significance and confidence intervals
- Training curves and convergence behavior
- Qualitative observations of unexpected behaviors or edge cases

### Analysis
- What worked and why
- What failed and root cause analysis
- Comparison to baseline or previous experiments
- Unexpected discoveries or insights

### Next Steps & Takeaways
- Specific actionable recommendations for follow-up experiments
- Open questions requiring investigation
- Key learnings that future team members should know
- Dead ends to avoid

Format using clear section headers, bullet points for detailed observations, and specific fields that enable easy searching and filtering across experiments.
```

## 用法 / Usage
- 必填變數 / Variables: {{evaluation-metrics}}、{{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Machine Learning Experiment Log Template Generator is a free AI prompt that creates systematic experiment …
