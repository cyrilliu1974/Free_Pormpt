# Academic Paper Analysis Prompt for Literature Review

## 簡介

The Academic Paper Analysis Prompt for Literature Review is a free AI prompt that conducts structured evaluation of highly cited academic papers to identify themes, gaps, and research implications for scholars and graduate students. This academic paper analysis prompt for ChatGPT walks through identifying the most influential papers on a research question, summarizing each study's methodology, key findings, and limitations, then synthesizing insights across all sources in a comparison table and discussion section. It outputs a complete literature review document formatted with introduction, methodology, individual paper summaries, comparison table, thematic discussion, conclusion, and a reference list in your chosen citation style (APA, MLA, Chicago, etc.). The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for researchers conducting systematic reviews, PhD candidates preparing dissertation chapters, and academics mapping a field before designing new studies. ● Summarizes methodology, results, and limitations for each of the 10 most cited papers on your research question ● Generates a comparison table mapping unique contributions, methods, and findings across all studies ● Identifies common themes, conflicting results, and under-researched areas to guide future inquiry ● Formats all references in your specified citation style (APA, MLA, Chicago, or others) ## Prompt

```
## Role
You are an expert researcher skilled at synthesizing key insights from academic literature in the relevant field.

## Task
Conduct a thorough analysis of the top 10 most cited papers addressing the research question below. For each paper, summarize its methodology, key results, and limitations. Then synthesize findings across papers to identify themes, gaps, and implications.

## Context
Research question: {{research-question}}

Citation style: {{citation-style}}

## Output
Structure your analysis as follows:

**Introduction**
- Brief overview of the research question and its significance
- Scope of the analysis (top 10 most cited papers)

**Methodology**
- Describe the process used to identify and select the top 10 most cited papers
- Outline the approach for analyzing and synthesizing information from each paper

**Paper Summaries**
For each of the 10 papers, provide:
1. Author(s), Year, Title
2. Methodology: Brief description of the research methods used
3. Key Results: Concise summary of the main findings
4. Limitations: Identified limitations or gaps in the research

**Comparison Table**
Create a table with these columns:
- Paper (Author, Year)
- Methodology
- Key Results
- Limitations
- Unique Contributions

Use ✓ to indicate presence of a feature and ✗ for absence.

**Discussion**
- Identify common themes, trends, or conflicting findings across papers
- Discuss collective strengths and weaknesses of the analyzed research
- Highlight potential areas for future research based on identified gaps

**Conclusion**
- Summarize key insights gained from the analysis
- Reflect on implications of the findings for the research question

**References**
- List all sources cited using the specified citation style
```

## 用法 / Usage
- 必填變數 / Variables: {{citation-style}}、{{research-question}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Academic Paper Analysis Prompt for Literature Review is a free AI prompt that conducts structured evaluati…
