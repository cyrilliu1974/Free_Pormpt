# Research Methodology Framework Generator

## 簡介

The Research Methodology Framework Generator is a free AI prompt that builds structured research methodology frameworks for educational researchers and graduate students. This research methodology prompt for ChatGPT produces a markdown table with three columns - research design, data collection methods, and data analysis techniques - each containing detailed descriptions and justifications tailored to your educational subfield and research context. It runs on ChatGPT, Claude, Gemini, and Grok, and is designed for qualitative, quantitative, or mixed-methods research. Use it when planning a thesis, designing a study protocol, or responding to reviewer feedback on methodological clarity. The prompt asks you to specify your research topic, educational subfield (curriculum design, learning assessment, policy analysis, etc.), and research context, then delivers a coherent framework that balances scientific rigor with adaptability. ● Aligns research design, data collection, and analysis into one coherent framework. ● Provides explicit justifications for qualitative, quantitative, or mixed-methods approaches. ● Outputs a markdown table that integrates easily into grant proposals, IRB applications, and dissertation chapters. ● Adapts to a wide range of educational subfields, from pedagogy to policy research. ## Prompt

```
## Role
You are an expert research methodologist specializing in educational research design.

## Task
Develop a comprehensive research methodology framework for the specified educational research context. Your framework must:

- Define a research design appropriate to the topic and subfield
- Outline data collection methods suited to the research questions
- Describe data analysis techniques aligned with the chosen methods
- Provide rationale for methodological choices (qualitative, quantitative, or mixed-methods)
- Ensure coherence, scientific rigor, and validity throughout
- Remain adaptable to related research questions within the subfield

## Context
Research topic: {{research-topic}}

Educational subfield: {{subfield}}

Research context: {{research-context}}

## Output
Present your methodology framework as a markdown table with three columns:

| Research Design | Data Collection Methods | Data Analysis Techniques |
|-----------------|-------------------------|---------------------------|
| [Content] | [Content] | [Content] |

Within each column, provide detailed descriptions and justifications for your methodological choices.
```

## 用法 / Usage
- 必填變數 / Variables: {{research-context}}、{{research-topic}}、{{subfield}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Research Methodology Framework Generator is a free AI prompt that builds structured research methodology f…
