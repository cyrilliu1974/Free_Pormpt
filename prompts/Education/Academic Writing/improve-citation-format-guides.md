# Citation Format Guide Generator for Academia

## 簡介

The Citation Format Guide Generator for Academia is a free AI prompt that creates comprehensive side-by-side citation format guides for students and faculty in higher education. This citation format guide prompt for ChatGPT produces structured markdown tables that compare multiple citation styles - APA, MLA, Chicago, and others - with publication-ready examples for books, journal articles, websites, conference papers, and edited volumes. The prompt instructs ChatGPT, Claude, or Gemini to analyze key differences across styles, highlight common citation errors, and explain the academic integrity rationale behind proper attribution. It addresses institution-specific problem areas, making it ideal for librarians, writing centers, faculty development teams, and academic support staff who need customized citation resources. ● Compares multiple citation styles in a single markdown table with complete, accurate examples for common source types ● Identifies the 3-5 most important distinguishing features across citation styles in a summary row ● Includes a dedicated column for common citation errors and a final section on attribution principles and error-prevention strategies ● Accepts custom variables for institution name, citation styles, audience discipline and level, and known problem areas to address ## Prompt

```
## Role
You are an academic citation expert developing improved citation format guides for higher education.

## Task
Create a comprehensive, user-friendly citation guide that compares multiple citation styles side-by-side. The guide should:

- Analyze key differences and similarities across the specified citation styles
- Provide clear, accurate examples for common source types: books, journal articles, websites, conference papers, and edited volumes
- Include a section on avoiding common citation errors specific to each style
- Explain the academic integrity rationale behind proper attribution
- Address known problem areas in current citation practices at the institution

## Context
Institution: {{institution}}
Citation styles to compare: {{citation-styles}}
Audience level and discipline focus: {{audience}}
Known citation challenges to address: {{problem-areas}}

## Output
Deliver the guide as a markdown table with:

- Column headers: Source Type | [Style 1] | [Style 2] | [Style N] | Common Errors
- Row organization by source type, with complete formatted examples in each style column
- A summary row highlighting the 3-5 most important distinguishing features across styles
- A final section below the table (bullet list) covering attribution principles and error-prevention strategies

Ensure examples are publication-ready and reflect current edition guidelines for each style.
```

## 用法 / Usage
- 必填變數 / Variables: {{audience}}、{{citation-styles}}、{{institution}}、{{problem-areas}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Citation Format Guide Generator for Academia is a free AI prompt that creates comprehensive side-by-side c…
