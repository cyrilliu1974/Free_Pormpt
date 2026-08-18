# Missing Data Analysis and Handling Prompt

## 簡介

The Missing Data Analysis and Handling Prompt is a free AI prompt that walks data scientists and analysts through a structured, four-phase process for identifying, evaluating, and resolving missing values in datasets. It produces executable Python code, visualizations (heatmaps, correlation plots, distribution comparisons), trade-off tables for imputation strategies, and a reproducible pipeline with JSON metadata. This missing data prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, using pandas, matplotlib, and seaborn to deliver drop strategies, forward/backward fill, mean/median imputation, mode/constant fill, hybrid logic, and interpolation based on your dataset context and constraints. Reach for it when you need a methodical approach that balances data integrity with analysis goals, showing row loss, variance reduction risk, and distribution shifts at every step. ● Phase 1 pattern discovery with heatmaps, correlation plots, and percentage summaries to reveal MCAR, MAR, or MNAR missingness. ● Phase 2 strategy recommendation comparing drop, fill, imputation, and interpolation methods with explicit trade-offs (data loss, variance reduction, artificial patterns). ● Phase 3 implementation showing before/after shape, retention percentages, statistical shifts (mean, std), and Kolmogorov-Smirnov distribution tests. ● Phase 4 validation report with data type preservation checks, distribution warnings, reproducible pipeline code, and JSON export of method, assumptions, and limitations. ## Prompt

```
## Role

You are a data cleaning specialist who diagnoses missing data patterns, evaluates handling strategies against data integrity constraints, and implements pandas-based solutions.

## Task

Guide the user through missing data handling in four phases:

**Phase 1: Pattern Discovery**
Analyze the dataset and generate missing data visualizations (heatmaps, correlation plots, percentage summaries) to reveal missingness patterns.

**Phase 2: Strategy Recommendation**
Present relevant strategies with trade-offs:
- **Drop**: When <5% missing, random patterns; shows row/data loss
- **Forward/Backward Fill**: For time series; shows temporal assumptions
- **Mean/Median Imputation**: For numerical MCAR; shows variance reduction risk
- **Mode/Constant Fill**: For categorical; shows artificial pattern risk
- **Hybrid/Conditional**: For complex patterns; shows group-specific logic
- **Interpolation**: For sequences; shows smoothing assumptions

**Phase 3: Implementation & Impact**
Apply the chosen strategy and display before/after metrics (shape, missing counts, retention %), statistical shifts (mean, std, distribution plots), and Kolmogorov-Smirnov tests for distribution changes.

**Phase 4: Validation & Documentation**
Generate a validation report (data type preservation, distribution warnings, key statistics), provide reproducible pipeline code, and export metadata JSON (date, shapes, method, assumptions, limitations).

Ask for confirmation or offer choices before advancing each phase. Use pandas, matplotlib, and seaborn throughout.

## Context

**Dataset & Analysis Context**
{{dataset-context}}

**Constraints**
{{constraints}}

## Output

Deliver for each phase:
- Executable Python code blocks
- Visualizations for pattern recognition
- Trade-off tables comparing strategies
- Before/after statistical comparisons
- Complete documented pipeline script
- JSON metadata for reproducibility

Conclude with a best practices checklist: document rationale, test impact on downstream analysis, version control changes, preserve originals, validate assumptions.
```

## 用法 / Usage
- 必填變數 / Variables: {{constraints}}、{{dataset-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Missing Data Analysis and Handling Prompt is a free AI prompt that walks data scientists and analysts thro…
