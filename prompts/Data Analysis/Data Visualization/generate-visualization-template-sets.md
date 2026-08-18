# Educational Data Visualization Template Generator

## 簡介

The Educational Data Visualization Template Generator is a free AI prompt that creates customized visualization template sets for educators and instructional designers. This data visualization prompt for ChatGPT analyzes your educational topic and learning objectives to produce 8-12 matched templates, each pairing a specific chart type with its ideal data type and pedagogical use case. The prompt runs on ChatGPT, Claude, and Gemini, delivering results in a clean markdown table that maps visualization methods to subject-matter facets. Use it when designing a course module, planning a data literacy workshop, preparing slides for different learning styles, or building a visual communication guide for students. ● Identifies the key data types inherent to your educational topic and the insights they surface. ● Recommends 8-12 diverse chart types - bar, line, scatter, heatmap, flowchart, and more - each matched to a specific pedagogical use case. ● Outputs a markdown table with Chart Type, Data Type, and Use Case columns for instant reference and integration into lesson plans. ● Accommodates your preferred visualization tools and adapts templates to different learning styles and audience backgrounds. ## Prompt

```
## Role
You are an expert data visualization specialist creating a set of effective visualization templates for educational content.

## Task
Generate a comprehensive set of visualization templates that communicate insights and trends for the given educational topic. Analyze the topic to identify key data types and potential insights, then select appropriate chart types that best represent the data and support the learning objectives. Ensure the templates are diverse, cover various aspects of the subject, and cater to different learning styles.

## Context
Educational topic and goals: {{educational-topic-and-objectives}}

Target audience: {{audience}}

Preferred data types and visualization tools: {{data-and-tools}}

## Output
Present your visualization templates as a markdown table with three columns:

| Chart Type | Data Type | Use Case |
|------------|-----------|----------|

Each row should provide a clear, concise description of a visualization template tailored to the specified educational topic. Include 8-12 diverse templates that address different facets of the subject matter.
```

## 用法 / Usage
- 必填變數 / Variables: {{audience}}、{{data-and-tools}}、{{educational-topic-and-objectives}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Educational Data Visualization Template Generator is a free AI prompt that creates customized visualizatio…
