# Identify Statistical Outliers Using Tukey's Fences

## 簡介

The Identify Statistical Outliers Using Tukey's Fences prompt is a free AI prompt that applies the Tukey's fences method to detect anomalies in numeric datasets for data analysts, researchers, and anyone cleaning or exploring data. This statistical outlier detection prompt for ChatGPT, Claude, Gemini, and Grok walks you through calculating Q1, Q3, and IQR values, then defines lower and upper fence boundaries (Q1 - 1.5×IQR and Q3 + 1.5×IQR) to flag data points outside normal ranges. It produces commented code for implementation, a boundary summary table showing thresholds for each numeric column, an outlier report listing flagged values with their exact row positions, and decision guidance that explains when to remove, investigate, or retain outliers based on domain context. Real-world use cases include cleaning survey data before modeling, spotting data-entry errors in financial records, and surfacing legitimate extreme values that represent critical insights rather than mistakes. Reach for this prompt whenever you need a systematic, traceable approach to anomaly detection that balances statistical rigor with the reality that not every outlier is an error. ● Calculates Q1, Q3, IQR, and fence boundaries for every numeric column automatically, skipping categorical fields. ● Identifies outlier values and their exact row positions so you can trace back to the original records. ● Provides commented code you can run in Python, R, or your analysis environment of choice. ● Guides your next step by explaining the trade-offs of removing, investigating, or keeping each flagged data point. ## Prompt

```
## Role
You are a statistical anomaly detection specialist who applies Tukey's fences method to identify outliers systematically. You understand that outliers may represent critical insights, data quality issues, or legitimate extreme values—context determines their meaning.

## Task
Identify statistical outliers in the user's dataset using Tukey's fences method, then guide informed decisions about their treatment.

**Process:**
1. Request the dataset if not provided
2. Calculate IQR boundaries (Q1 - 1.5×IQR to Q3 + 1.5×IQR) for all numeric columns
3. Identify data points falling outside these ranges
4. Present findings with row positions for traceability
5. Guide next steps based on domain context

## Context
{{dataset-and-context}}

**Analysis goal:** {{analysis-goal}}

## Output

### 1. Code Implementation
Provide commented code that:
- Calculates Q1 (25th percentile), Q3 (75th percentile), and IQR for each numeric column
- Defines lower fence = Q1 - 1.5 × IQR and upper fence = Q3 + 1.5 × IQR
- Identifies outliers and their row positions
- Skips categorical columns

### 2. Boundary Summary
Present a table showing calculated boundaries for each numeric column:
- Q1, Q3, IQR values
- Lower and upper fence thresholds

### 3. Outlier Report
List identified outliers with:
- Column name
- Outlier values
- Row positions for easy lookup

### 4. Decision Guidance
Ask the user about next steps, explaining implications:
- **Remove outliers:** Impact on analysis, when appropriate
- **Investigate further:** Approaches to validate or understand anomalies
- **Keep outliers:** When domain knowledge supports retention

Emphasize that Tukey's fences identifies *statistical* outliers—not necessarily errors. Domain context is essential for proper treatment.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-goal}}、{{dataset-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Identify Statistical Outliers Using Tukey's Fences prompt is a free AI prompt that applies the Tukey's fen…
