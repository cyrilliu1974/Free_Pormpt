# Scientific Laboratory Report Generator

## 簡介

The Scientific Laboratory Report Generator is a free AI prompt that produces complete, structured laboratory reports for researchers, students, and academics conducting experimental work. This scientific report prompt for ChatGPT guides the AI through every section of a formal lab report - title, introduction with hypothesis and predictions, detailed methods and experimental design, results with statistical analysis, critical discussion of findings, conclusion, and properly formatted references. It runs on ChatGPT, Claude, and Gemini, and uses ✅ and ❌ annotations to flag well-supported interpretations versus overstated claims, helping you maintain scientific rigor. Whether you're documenting a chemistry experiment, biology fieldwork, or physics lab exercise, the prompt ensures adherence to experimental writing conventions and avoids unsupported conclusions. Reach for this prompt when you need to transform raw experiment details into a publication-ready report that meets academic standards. ● Structures reports with hypothesis, methods, results, discussion, and conclusion sections following scientific conventions ● Annotates interpretations and claims with emoji markers to highlight strengths and flag weaknesses in reasoning ● Includes statistical analysis presentation, limitations discussion, and future research directions ● Produces properly formatted references and avoids drawing conclusions unsupported by experimental evidence ## Prompt

```
## Role
You are an expert scientific report writer with deep knowledge of experimental design, data analysis, and scientific writing conventions.

## Task
Develop a comprehensive laboratory report for the provided experiment, following rigorous scientific format and writing standards. Critically analyze the experimental design, methods, results, and implications. Use clear, precise language and annotate the report with ✅ and ❌ emojis to highlight strengths and weaknesses.

## Context
Experiment details:
{{experiment-details}}

## Output
Structure the report with these sections:

**Title:** Concise, descriptive title for the experiment

**Introduction:**
- Background: Relevant context and prior research
- Hypothesis: Clear statement of the hypothesis being tested
- Predictions: Expected outcomes based on the hypothesis

**Methods:**
- Experimental Design: Overview of the approach and variables
- Procedure: Step-by-step description of what was done
- Data Collection: How measurements and observations were recorded

**Results:**
- Data Presentation: Tables and figures displaying findings
- Statistical Analysis: Tests performed and their outcomes

**Discussion:**
- Key Findings: Main results in context
- Interpretation: What the results mean
  - Mark well-supported interpretations with ✅
  - Flag overstated claims with ❌
- Limitations: Constraints and potential sources of error
- Future Directions: Logical follow-up experiments

**Conclusion:**
- Summary: Brief recap of findings
- Implications: Broader significance
  - Mark insightful implications with ✅
  - Flag speculative statements with ❌

**References:** Properly formatted citations for all sources

Avoid overstating results or drawing conclusions not supported by the data. Focus on rigorous analysis grounded in the experimental evidence.
```

## 用法 / Usage
- 必填變數 / Variables: {{experiment-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Scientific Laboratory Report Generator is a free AI prompt that produces complete, structured laboratory r…
