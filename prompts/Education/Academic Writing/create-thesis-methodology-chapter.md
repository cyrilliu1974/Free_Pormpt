# Thesis Methodology Chapter Generator

## 簡介

The Thesis Methodology Chapter Generator is a free AI prompt that produces complete, structured methodology chapters for doctoral dissertations, master's theses, and academic research papers. This thesis methodology prompt for ChatGPT takes your research topic, research questions, and methodology details - including design approach, data collection instruments, sampling strategy, and analytical techniques - and outputs an eight-section chapter formatted in markdown with clear headings, bullet lists, and dependency grammar structures that enhance readability. It walks through research design justification, data gathering procedures, population and sampling characteristics, preparation and analysis workflows (including software tools), honest limitation disclosures, and ethical considerations. Researchers use it to transform raw methodology notes into polished, reproducible chapters ready for committee review. It runs on ChatGPT, Claude, and Gemini. This prompt is built for graduate students, doctoral candidates, and academic researchers who need to document their methodology with the clarity and rigor required by institutional review boards and academic publishers. ● Outputs all eight required methodology sections: topic, questions, design, collection, sampling, analysis, limitations, and ethics ● Applies dependency grammar framework to ensure each sentence and paragraph flows logically from the previous one ● Explains technical terms in context and avoids unexplained jargon, making the chapter accessible to interdisciplinary committees ● Structures content with markdown headings, subheadings, and lists that meet thesis formatting standards ## Prompt

```
## Role
You are an expert researcher with deep knowledge of research design and methodology across various fields.

## Task
Write a comprehensive methodology chapter for a thesis. Detail the research approach, data gathering techniques, sampling methods, and analytical procedures. Provide clear rationale for selected methods and address limitations. Structure the writing using dependency grammar to ensure clarity and coherence.

## Context
Research topic: {{research-topic}}

Research questions: {{research-questions}}

Methodology details: {{methodology-details}}
(Include: research design and justification; data collection methods, procedures, and instruments; population, sampling technique, sample size and characteristics; data preparation, analytical methods, tools and software; limitations; ethical considerations)

## Output
Structure the methodology chapter with these sections:

1. **Research Topic**: State the research topic
2. **Research Questions**: List the research questions
3. **Research Design**: Describe the design and justify its selection
4. **Data Collection**: Detail methods, procedures, and instruments
5. **Sampling**: Describe population, technique, sample size and characteristics
6. **Data Analysis**: Explain preparation, analytical methods, and tools/software
7. **Limitations**: Address limitations and potential issues honestly
8. **Ethical Considerations**: Discuss relevant ethical considerations

Use dependency grammar throughout. Format in markdown with clear headings and subheadings. Use bullet points or numbered lists where appropriate. Explain technical terms when used. Avoid jargon without context.
```

## 用法 / Usage
- 必填變數 / Variables: {{methodology-details}}、{{research-questions}}、{{research-topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Thesis Methodology Chapter Generator is a free AI prompt that produces complete, structured methodology ch…
