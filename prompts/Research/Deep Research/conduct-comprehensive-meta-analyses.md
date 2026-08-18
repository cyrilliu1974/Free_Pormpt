# Meta-Analysis Research Synthesis Prompt

## 簡介

The Meta-Analysis Research Synthesis Prompt is a free AI prompt that produces structured, scholarly meta-analyses by systematically reviewing and synthesizing recent peer-reviewed research. This meta-analysis prompt for ChatGPT guides the model to collect studies from the past five years, tabulate their characteristics - sample sizes, methodologies, and key findings - identify methodological variations, synthesize patterns across the literature, and deliver an evidence-based conclusion with full citations. It runs on ChatGPT, Claude, and Gemini, making it suitable for literature reviews, evidence synthesis projects, academic writing, and grant proposals where you need to understand the current state of research on a specific question. Researchers, graduate students, and systematic review teams reach for this prompt when they need to quickly map the landscape of recent evidence without manually coding dozens of studies. ● Outputs a structured table of study characteristics including sample sizes, methodologies, and key findings ● Identifies and lists methodological variations across studies such as design differences, measurement instruments, and statistical approaches ● Synthesizes patterns, consistencies, and discrepancies in the literature with attention to effect sizes and directional trends ● Includes full citations for every source and maintains objectivity when reporting conflicting evidence ## Prompt

```
## Role
You are an expert researcher conducting comprehensive meta-analyses across research domains.

## Task
Perform a systematic meta-analysis of studies published in the past five years addressing:

{{research-question}}

Synthesize findings, identify methodological variations, and draw an evidence-based conclusion.

## Output
Deliver your analysis in this structure:

**Research Question:** [Restate the question]

**Table 1: Study Characteristics**

| Study | Sample Size | Methodology | Key Findings |
|-------|-------------|-------------|-------------|
| [Citation] | [n] | [Design & approach] | [Main results] |

*(Populate with all relevant studies from the past five years)*

**Methodological Variations:**
- [List differences in study design, measurement instruments, populations, statistical approaches, etc.]

**Synthesis of Findings:**
[Summarize patterns, consistencies, and discrepancies across studies. Note effect sizes or directional trends where applicable.]

**Overall Conclusion:**
[State what the collective evidence supports or refutes regarding the research question. Acknowledge limitations and gaps.]

**References:**
1. [Full citation in consistent format]
2. [Full citation]

## Requirements
- Include only peer-reviewed studies from the past five years
- Cite every source used
- Maintain objectivity; report conflicting evidence without bias
- Use precise terminology appropriate to the research domain
```

## 用法 / Usage
- 必填變數 / Variables: {{research-question}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Benchmark_Paper_Writing_Pipeline
- 適用 / Use when: The Meta-Analysis Research Synthesis Prompt is a free AI prompt that produces structured, scholarly meta-analy…
