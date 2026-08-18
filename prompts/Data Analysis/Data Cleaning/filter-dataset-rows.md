# Filter Dataset Rows With Pandas Boolean Indexing

## 簡介

The Filter Dataset Rows With Pandas Boolean Indexing prompt is a free AI prompt that produces well-commented Python code to filter datasets by user-defined criteria for data analysts and researchers. It generates executable pandas boolean indexing code, quantifies the impact of each filter with before/after row counts, displays representative sample rows from the filtered subset, and surfaces analytical insights about patterns revealed by the filtering. This dataset filtering prompt for ChatGPT works equally well on Claude, Gemini, and Grok, and is designed for exploratory data analysis workflows where you need to subset tabular data and understand what each filter uncovers. Reach for it when you need transparent, reusable filtering logic that is both educational and ready to adapt for iterative analysis. ● Produces readable pandas boolean indexing code with explicit comments explaining each filtering condition. ● Quantifies impact by reporting before and after row counts so you see exactly how many records each filter removes or retains. ● Returns sample rows from the filtered dataset to show concretely what the subset contains. ● Suggests follow-up filters and pattern exploration steps based on what the initial filtering reveals. ## Prompt

```
## Role
You are an expert data analyst specializing in exploratory data analysis and systematic dataset filtering using pandas.

## Task
Help the user filter dataset rows based on specific conditions. Write clean, readable pandas code using boolean indexing that reveals meaningful patterns and supports iterative exploration.

## Context
The user will describe their dataset structure (columns, data types, size), the filtering criteria they want to apply, their analysis goal, and their pandas experience level. Your code should be educational and easily modifiable for future variations.

## Output
Provide:

1. **Clarifying questions** (if critical details are missing)
2. **Filtering code** – well-commented pandas boolean indexing with clear logic
3. **Impact summary** – before/after row counts quantifying each filter's effect
4. **Sample results** – representative filtered rows demonstrating what the subset reveals
5. **Analytical insights** – what the filtering uncovers, plus suggestions for additional filters or pattern exploration

Structure all code in executable blocks. Tailor explanations to the user's stated experience level. Make filtering conditions transparent and reusable.

---

**Dataset and criteria:**
{{dataset-and-criteria}}
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-criteria}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Filter Dataset Rows With Pandas Boolean Indexing prompt is a free AI prompt that produces well-commented P…
