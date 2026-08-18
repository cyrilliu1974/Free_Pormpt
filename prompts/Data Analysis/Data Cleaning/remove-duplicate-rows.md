# Remove Duplicate Rows – Python Pandas Data Cleaning

## 簡介

The Remove Duplicate Rows prompt is a free AI prompt that generates complete Python code to identify, analyze, and eliminate duplicate records from datasets for data analysts and developers. This duplicate removal prompt for ChatGPT walks you through a systematic five-step process: loading and inspecting your dataset structure, identifying duplicates using pandas `.duplicated()` and `.drop_duplicates()` methods based on your custom criteria, analyzing duplicate patterns with counts and sample records, removing duplicates while preserving first occurrences, and validating the results with before-and-after statistics. The prompt produces executable code blocks with detailed inline comments, explanatory text for each step, sample output examples showing dataframes and statistics, and validation checks confirming successful removal. It runs on ChatGPT, Claude, Gemini, Grok, and other text-based AI models that handle code generation. Reach for this prompt whenever you need to clean messy datasets, ensure data integrity before analysis, or learn pandas-based deduplication techniques with clear documentation. ● Customizable duplicate criteria – define which columns determine uniqueness for your specific dataset ● Detailed duplicate pattern analysis – see counts, row locations, and example records before removal ● Before-and-after reporting – displays eliminated records and row count changes with validation checks ● Educational code structure – inline comments and step-by-step explanations teach pandas deduplication methods ## Prompt

```
## Role
You are an expert data analyst and Python developer specializing in pandas-based duplicate detection and removal.

## Task
Generate complete, executable Python code that identifies, analyzes, and removes duplicate records from a dataset. Walk the user through each step with detailed comments and explanations, showing exactly what duplicates exist, where they appear, and what was removed.

## Context
Dataset: {{dataset-description}}

Duplicate criteria: {{duplicate-criteria}}

## Process

1. **Load and inspect** the dataset structure (shape, columns, dtypes, memory usage)
2. **Identify duplicates** using pandas methods based on the specified criteria
3. **Analyze duplicate patterns** – show counts, locations, and display example duplicate records
4. **Remove duplicates** while preserving first occurrences, with before/after row counts
5. **Report results** – display sample eliminated records and validate the cleaning
6. **Summarize** – confirm successful removal and provide insights on duplicate patterns found

## Output

Provide:
- Executable Python code blocks with detailed inline comments
- Explanatory text before each code section describing what the step accomplishes
- Sample output examples (dataframes, statistics, messages) showing what the analysis and removal would produce
- Validation checks confirming duplicates were successfully removed

Use `pandas` methods like `.duplicated()`, `.drop_duplicates()`, and boolean indexing. Format code for readability with clear variable names.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-description}}、{{duplicate-criteria}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Remove Duplicate Rows prompt is a free AI prompt that generates complete Python code to identify, analyze,…
