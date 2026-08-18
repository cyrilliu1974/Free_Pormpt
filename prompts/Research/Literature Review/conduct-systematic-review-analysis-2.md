# Systematic Review Analysis Prompt for Meta-Analysis

## 簡介

The Systematic Review Analysis Prompt for Meta-Analysis is a free AI prompt that structures rigorous evidence synthesis for researchers evaluating intervention effectiveness in specific populations. This systematic review prompt for ChatGPT guides you through every phase of a methodologically sound meta-analysis: defining search strategies across databases, creating PRISMA flowcharts for study selection, building study characteristics tables, assessing methodological quality with tools like Cochrane Risk of Bias or Newcastle-Ottawa Scale, calculating pooled effect sizes with confidence intervals, generating forest plots, and producing GRADE summary-of-findings tables. It runs on ChatGPT, Claude, and Gemini, outputting structured markdown reports with visual evidence summaries, heterogeneity analysis (I² statistics), and transparent documentation of strengths, limitations, and clinical implications. Researchers use it to accelerate systematic reviews for clinical guidelines, academic publications, and evidence-based practice recommendations. Designed for systematic reviewers, meta-analysts, clinical researchers, and evidence synthesis teams who need to follow PRISMA reporting standards while maintaining scientific rigor. ● Automates creation of PRISMA flowcharts, forest plots, and summary-of-findings tables in structured markdown format. ● Calculates pooled effect sizes, confidence intervals, and heterogeneity metrics (I²) with subgroup and sensitivity analysis guidance. ● Incorporates standard quality-assessment tools (Cochrane Risk of Bias, Newcastle-Ottawa Scale) and GRADE certainty-of-evidence ratings. ● Produces discussion sections covering clinical significance, limitations, practice implications, and future research recommendations. ## Prompt

```
## Role
You are a systematic reviewer and meta-analyst conducting a comprehensive evidence synthesis to assess intervention effectiveness.

## Task
Conduct a rigorous systematic review and meta-analysis evaluating the effectiveness of {{intervention}} for {{condition}} in {{population}}. Critically appraise study quality, calculate effect sizes, examine heterogeneity, and synthesize findings with visual evidence summaries.

## Output Structure
Deliver your review using markdown with these sections:

### 1. Search Strategy
- Databases searched
- Search terms and Boolean operators
- Inclusion and exclusion criteria
- Date ranges and filters applied

### 2. Study Selection Flowchart
Insert a PRISMA flowchart showing records identified, screened, excluded, and included.

### 3. Study Characteristics Table
Summarize key characteristics: author/year, design, sample size, intervention details, comparator, outcomes measured, follow-up duration.

### 4. Methodological Quality Assessment
- Tool used (e.g., Cochrane Risk of Bias, Newcastle-Ottawa Scale)
- Summary of quality assessment results across domains
- Table or graph displaying risk of bias

### 5. Effect Size Analysis
- Effect size metric used (e.g., standardized mean difference, odds ratio, risk ratio)
- Pooled effect size with 95% confidence interval
- I² statistic with interpretation of heterogeneity (low/moderate/high)
- Subgroup or sensitivity analyses if heterogeneity is substantial

### 6. Forest Plot
Insert a forest plot displaying individual study effect sizes, confidence intervals, weights, and the pooled estimate with prediction interval.

### 7. Summary of Findings Table
Insert a GRADE summary of findings table rating certainty of evidence (high/moderate/low/very low) for each outcome.

### 8. Discussion
- Summary of main results and clinical significance
- Strengths and limitations of the review
- Implications for clinical practice
- Recommendations for future research

### 9. References
List all cited sources in APA format.

## Quality Standards
- Maintain objectivity and avoid bias in study selection and interpretation
- Report transparently on limitations and sources of heterogeneity
- Ensure all claims are supported by included studies
- Follow PRISMA reporting guidelines throughout
```

## 用法 / Usage
- 必填變數 / Variables: {{condition}}、{{intervention}}、{{population}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Experiment_Design&AB_Testing
- 適用 / Use when: The Systematic Review Analysis Prompt for Meta-Analysis is a free AI prompt that structures rigorous evidence …
