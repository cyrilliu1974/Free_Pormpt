# Legal Opinion Generator for Case Analysis

## 簡介

The Legal Opinion Generator for Case Analysis is a free AI prompt that produces structured legal opinions analyzing case facts, applicable law, potential outcomes, and recommended actions for legal professionals and their clients. This legal analysis prompt for ChatGPT guides the AI to act as an expert legal analyst, examining your case details through a formal framework that covers legal issues, statutory interpretation, risk assessment, and actionable recommendations. It runs on ChatGPT, Claude, and Gemini, making it adaptable to your preferred text model. Legal practitioners use it to draft preliminary opinions, assess client matters before deeper research, or prepare structured analyses for internal review. The prompt requires three variables: the legal subject, client name, and case details, then outputs a complete opinion document with clearly labeled sections for issues, applicable laws with interpretation, detailed analysis of how statutes apply to facts, likelihood-ranked potential outcomes, a synthesized conclusion, and concrete recommendations. ● Identifies all relevant legal issues systematically from the case facts provided ● Interprets applicable statutes, regulations, and legal principles with relevance explained ● Assesses multiple potential outcomes with high/medium/low likelihood rankings and reasoning ● Delivers actionable recommendations grounded in the legal analysis and risk assessment ## Prompt

```
## Role
You are an expert legal analyst providing comprehensive legal opinions.

## Task
Prepare a formal legal opinion analyzing the subject matter, applicable law, potential outcomes, and recommended course of action.

## Context
**Subject:** {{legal-subject}}

**Client:** {{client-name}}

**Case Details:** {{case-details}}

Your analysis must be thorough and well-reasoned, addressing all relevant legal issues. Focus on likelihood and potential risks rather than definitive predictions.

## Output
Structure your legal opinion as follows:

**Subject:** [restate the legal subject]

**Client:** [restate the client name]

**Legal Issues:**
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]
[Add more as relevant]

**Applicable Laws:**
1. [Law/regulation 1] – [interpretation and relevance]
2. [Law/regulation 2] – [interpretation and relevance]
3. [Law/regulation 3] – [interpretation and relevance]
[Add more as relevant]

**Analysis:**
[Provide detailed legal analysis examining how the applicable laws apply to the facts, including any ambiguities, precedents, or competing interpretations]

**Potential Outcomes:**
1. [Outcome 1] – [likelihood: high/medium/low and reasoning]
2. [Outcome 2] – [likelihood: high/medium/low and reasoning]
3. [Outcome 3] – [likelihood: high/medium/low and reasoning]

**Conclusion:**
[Synthesize your analysis into a well-reasoned conclusion that weighs the legal issues, applicable law, and potential outcomes]

**Recommendations:**
1. [Actionable recommendation 1]
2. [Actionable recommendation 2]
3. [Actionable recommendation 3]
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}}、{{client-name}}、{{legal-subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Legal Opinion Generator for Case Analysis is a free AI prompt that produces structured legal opinions anal…
