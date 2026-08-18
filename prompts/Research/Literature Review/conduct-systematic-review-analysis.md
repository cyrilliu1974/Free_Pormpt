# Systematic Review Analysis Prompt for Research Papers

## 簡介

The Systematic Review Analysis Prompt for Research Papers is a free AI prompt that conducts structured evidence synthesis across peer-reviewed literature for researchers, academics, and evidence-based professionals. This systematic review prompt for ChatGPT walks through the full methodology: formulating focused research questions, defining inclusion and exclusion criteria, developing multi-database search strategies, screening studies against predefined criteria, extracting structured data, assessing quality and risk of bias, synthesizing findings through narrative analysis, and drawing evidence-based conclusions with proper citations. It works on ChatGPT, Claude, and Gemini to produce publication-ready reports with abstract, methods, results, discussion, and references sections. Use it when you need to map the current state of research in a field, identify knowledge gaps, or establish evidence-based recommendations for practice or policy. ● Guides the full systematic review workflow from research question formulation through final conclusions ● Applies standardized quality assessment tools and risk-of-bias evaluation to ensure rigor ● Structures output into publication-ready sections with tables, markdown formatting, and visual indicators for criteria assessment ● Supports customizable timeframes, citation styles, and language filters to match journal or institutional requirements ## Prompt

```
## Role
You are a systematic review expert who conducts comprehensive evidence synthesis using structured methodology to analyze the current state of research in a field.

## Task
Conduct a systematic review on {{topic-field}} following established systematic review methodology:

1. Formulate a clear, focused research question based on the topic
2. Define inclusion and exclusion criteria for study selection
3. Develop a search strategy and systematically search relevant databases
4. Screen and select studies based on predefined criteria
5. Extract data from included studies
6. Assess quality and risk of bias using appropriate tools
7. Synthesize findings through narrative analysis, identifying patterns, similarities, and differences
8. Interpret results and draw evidence-based conclusions
9. Cite all sources in {{citation-style}} format

## Context
Include peer-reviewed studies published within the last {{timeframe-years}} years in {{languages}}. Exclude non-peer-reviewed publications, studies with insufficient data, and those with inadequate methodological quality. Focus on studies directly addressing the research question.

## Output
Deliver a comprehensive report structured as:

**Title:** Systematic Review on [topic]

**Abstract**

**Introduction**

**Methods**
- Research question
- Inclusion and exclusion criteria
- Search strategy
- Study selection
- Data extraction
- Quality assessment

**Results**
- Study characteristics
- Synthesis of findings

**Discussion**
- Summary of evidence
- Strengths and limitations
- Implications for practice and research
- Knowledge gaps and future research directions

**Conclusion**

**References**

Use markdown formatting with clear headings. Include tables where relevant to present study characteristics or findings. Use ✅ and ❌ to indicate criteria met/not met during quality assessment.
```

## 用法 / Usage
- 必填變數 / Variables: {{citation-style}}、{{languages}}、{{timeframe-years}}、{{topic-field}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Systematic Review Analysis Prompt for Research Papers is a free AI prompt that conducts structured evidenc…
