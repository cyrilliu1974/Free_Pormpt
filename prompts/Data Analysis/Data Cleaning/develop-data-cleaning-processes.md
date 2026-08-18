# Data Cleaning Process Plan Generator for Education

## 簡介

The Data Cleaning Process Plan Generator for Education is a free AI prompt that produces a comprehensive, table-based data cleaning plan tailored to educational institutions. This data cleaning prompt for ChatGPT guides the model to act as an expert data analyst and deliver a structured markdown table with five columns: Data Source, Data Type, Cleaning Steps, Validation Methods, and Expected Outcomes. It addresses common data quality challenges in education settings - missing values, outliers, formatting inconsistencies, duplicate entries, and domain-specific issues - while applying current best practices in data quality assurance. Whether you're preparing student demographic data, academic records, or financial datasets for analysis, this prompt ensures each data source receives specific cleaning actions, defined validation checks, and measurable quality targets. Data managers, institutional researchers, and IT teams in schools, colleges, and universities will find this prompt invaluable when they need to document and standardize data cleaning workflows across multiple systems. The prompt runs on ChatGPT, Claude, Gemini, and Grok, accepting a single variable for institution and data context to customize the output. ● Produces a five-column markdown table that maps each data source to its type, cleaning sequence, validation checks, and quality benchmarks. ● Addresses typical education data issues including duplicates, missing values, inconsistent formatting, and outliers in demographic, academic, and financial datasets. ● Customizes output based on the institution's specific data context, systems, and quality challenges you describe in the variable. ● Defines measurable outcomes such as completeness percentages, zero-duplicate guarantees, and standardized field formats for accountability. ## Prompt

```
## Role
You are an expert data analyst specializing in data quality assurance for educational institutions.

## Task
Develop a comprehensive data cleaning process plan that ensures data accuracy, consistency, and completeness. Deliver the plan as a structured table covering all phases from source identification through validation.

## Context
Educational institution context: {{institution-and-data-context}}

Address common data quality issues including missing values, outliers, formatting inconsistencies, duplicate entries, and any domain-specific challenges. Apply current best practices in data cleaning and quality assurance to maintain dataset integrity throughout the process.

## Output
Provide your data cleaning process plan in a markdown table with exactly 5 columns:

| Data Source | Data Type | Cleaning Steps | Validation Methods | Expected Outcomes |
|-------------|-----------|----------------|--------------------|-----------------|

Each row should represent a distinct data source or data category. For each:
- **Data Source**: Identify the origin system or file
- **Data Type**: Specify the nature of data (demographic, academic, financial, etc.)
- **Cleaning Steps**: List specific actions in logical sequence (e.g., remove duplicates, standardize formats, handle nulls, treat outliers)
- **Validation Methods**: Define checks to confirm cleaning success (e.g., range checks, completeness rates, cross-field validation)
- **Expected Outcomes**: State measurable quality improvements (e.g., "95% completeness", "zero duplicates", "standardized date format")

Include multiple rows to cover all relevant data sources in the institution's ecosystem.
```

## 用法 / Usage
- 必填變數 / Variables: {{institution-and-data-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Cleaning Process Plan Generator for Education is a free AI prompt that produces a comprehensive, tabl…
