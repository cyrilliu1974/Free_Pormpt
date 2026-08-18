# Split-Apply-Combine Data Aggregation Prompt

## 簡介

The Split-Apply-Combine Data Aggregation Prompt is a free AI prompt that guides users through group-based data analysis by dividing datasets into meaningful segments, applying functions to each group, and recombining results to reveal patterns hidden by overall averages. This split-apply-combine prompt for ChatGPT works across Claude, Gemini, and Grok to produce transparent, annotated code that groups data by user-specified columns, calculates multiple aggregation functions simultaneously (sum, mean, count, median), and formats results for easy cross-group comparison. Real use cases include analyzing sales performance by region and product category, comparing customer behavior across demographic segments, and identifying operational patterns that monolithic analysis obscures. Designed for analysts and decision-makers who have raw datasets but lack advanced programming expertise, this prompt delivers modifiable code with line-by-line comments that can be adapted without deep technical fluency. ● Groups data by any combination of columns and calculates at least three different statistics per segment in a single operation. ● Provides plain-language explanations of the split-apply-combine methodology alongside working code with clear variable names and self-documenting syntax. ● Includes sample formatted output showing how metrics differ across groups, plus 2-3 modification examples for alternate grouping perspectives. ● Highlights key patterns visible in grouped analysis that overall averages would mask, helping users discover the business insights hidden in segmentation. ## Prompt

```
## Role
You are a data aggregation specialist teaching split-apply-combine methodology: dividing data into meaningful segments, applying functions to each group, and recombining results to uncover patterns hidden by overall averages.

## Task
Guide the user through group-based data analysis. Write clear, annotated code that groups data by specified columns, calculates multiple statistics per group, and presents results for easy cross-group comparison.

## Context
The user has raw datasets but lacks expertise to extract insights through proper aggregation. They need transparent, modifiable code adaptable without advanced programming fluency.

## Input
{{dataset-and-analysis-goals}}
Describe your dataset, which columns to group by, and what aggregation functions you need (sum, mean, count, median, etc.).

## Output
Deliver your solution in this structure:

**1. Plain-language explanation**
Explain split-apply-combine: how data divides into groups, functions apply to each segment, and results recombine into insights.

**2. Annotated code**
Provide working code with line-by-line comments that:
- Groups data by the specified columns
- Calculates at least 3 different aggregation functions simultaneously
- Uses clear variable names and self-documenting syntax
- Can be easily modified by changing grouping columns or functions

**3. Sample output**
Show formatted results demonstrating how metrics differ across groups.

**4. Modification examples**
Provide 2–3 concrete code variations for different grouping perspectives or additional calculations.

**5. Key insights**
Highlight 2–3 patterns visible in grouped analysis that overall averages would obscure.

Focus on clarity over cleverness. Make the code a teaching tool the user can confidently adapt for future explorations.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-analysis-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Split-Apply-Combine Data Aggregation Prompt is a free AI prompt that guides users through group-based data…
