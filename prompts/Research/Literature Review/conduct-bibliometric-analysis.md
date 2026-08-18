# Bibliometric Analysis Prompt for Research Fields

## 簡介

The Bibliometric Analysis Prompt for Research Fields is a free AI prompt that produces comprehensive research output analysis with publication trends, citation patterns, and collaboration networks for any academic discipline. This bibliometric analysis prompt for ChatGPT walks through publication counts by year, identifies the most-cited papers in a field, maps institutional collaboration frequency, and delivers Python code (NetworkX + Plotly) to render an interactive co-authorship network diagram. It runs on ChatGPT, Claude, Gemini, and Grok, making it suitable for researchers conducting literature reviews, grant writers summarizing field activity, or institutional analysts benchmarking research impact. The prompt structures output into six sections: introduction, publication trends table, top-10 citation table, collaboration institution rankings, visualization code, and APA references. Reach for this prompt when you need to quantify scholarly output across a custom time window or compare collaboration dynamics between institutions in a given domain. ● Tabulates year-by-year publication counts and total citations for the specified research field and time period. ● Ranks the top 10 most-cited papers with full author, title, year, and citation metadata. ● Identifies the top 10 collaborating institutions by collaboration frequency. ● Supplies annotated Python code using NetworkX and Plotly to generate an interactive co-authorship network graph. ● Concludes with APA-formatted source citations for reproducibility and academic rigor. ## Prompt

```
## Role
You are a bibliometric analyst and data visualization specialist conducting a comprehensive analysis of research output over a specified time period.

## Task
Analyze publication trends, citation patterns, and collaboration networks for the given research field and time range. Present findings in structured tables and provide code for an interactive co-authorship network visualization.

## Context
Research field: {{research-field}}
Time period: {{time-period}}

## Output
Deliver your analysis in the following structure:

**1. Introduction**
Briefly introduce the research field and time period being analyzed.

**2. Publication Trends**
- Total Publications: [number]
- Publications per Year:

| Year | Number of Publications |
|------|------------------------|
| [year] | [count] |

Include all years in the specified range.

**3. Citation Analysis**
- Total Citations: [number]
- Top 10 Most Cited Papers:

| Paper Title | Authors | Year | Citations |
|-------------|---------|------|--------|
| [title] | [authors] | [year] | [count] |

List papers in descending order by citation count.

**4. Collaboration Networks**
- Total Unique Authors: [number]
- Top 10 Collaborating Institutions:

| Institution | Collaborations |
|-------------|----------------|
| [name] | [count] |

List institutions in descending order by collaboration count.

**5. Co-Authorship Network Visualization**
Provide clean, efficient Python code using NetworkX and Plotly to generate an interactive co-authorship network diagram. Include comments explaining key steps.

**6. Sources**
Cite all data sources and references using APA format.
```

## 用法 / Usage
- 必填變數 / Variables: {{research-field}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Bibliometric Analysis Prompt for Research Fields is a free AI prompt that produces comprehensive research …
