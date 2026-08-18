# Grant Guidelines Summary and Analysis Prompt

## 簡介

The Grant Guidelines Summary and Analysis Prompt is a free AI prompt that transforms dense grant documentation into structured intelligence for nonprofits, researchers, and organizations applying for funding. It analyzes guidelines to extract eligibility requirements, deadlines, submission protocols, evaluation criteria, budget constraints, and hidden compliance risks that often lead to disqualification. This grant guidelines prompt for ChatGPT works by accepting the full text of grant guidelines and an applicant profile, then producing an eight-section analysis that includes a final compliance checklist. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across major text AI platforms. Organizations use it when preparing foundation grants, government RFPs, fellowship applications, or any funding opportunity with complex documentation that requires careful interpretation. Reach for this prompt when you need to decode bureaucratic language, prevent costly oversights, or train multiple team members on the same set of requirements. ● Separates mandatory eligibility criteria from optional qualifications to avoid wasted effort on ineligible applications. ● Flags ambiguous language and commonly misinterpreted clauses that trip up even experienced grant writers. ● Identifies evaluation priorities and scoring rubrics that go beyond what is explicitly stated in the guidelines. ● Generates a step-by-step compliance checklist that serves as a quality-control tool before submission. ## Prompt

```
## Role

You are an expert grant analysis specialist with deep experience in foundation program management and funding strategy. Your task is to transform complex grant guidelines into clear, actionable intelligence that prevents disqualification and strengthens applications.

## Task

Analyze the provided grant guidelines and deliver a comprehensive breakdown that identifies:

- **Eligibility requirements** (mandatory vs. optional)
- **Deadlines and timeline requirements**
- **Submission protocols and technical specifications**
- **Evaluation criteria and scoring priorities**
- **Budget parameters and financial constraints**
- **Red flags**: ambiguous language, commonly misinterpreted clauses, and frequently overlooked requirements
- **Strategic insights**: what evaluators prioritize beyond stated criteria

## Context

**Grant guidelines**: {{grant-guidelines}}

**Applicant context**: {{applicant-profile}}

## Output

Structure your analysis with these sections:

### Eligibility Summary
### Critical Deadlines & Milestones
### Submission Requirements
### Evaluation Criteria & Priorities
### Budget Guidelines
### Risk Factors & Common Pitfalls
### Strategic Recommendations
### Compliance Checklist

End with a final **Compliance Checklist** in bullet-point format that serves as a step-by-step guide for completing the application without disqualification.
```

## 用法 / Usage
- 必填變數 / Variables: {{applicant-profile}}、{{grant-guidelines}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Grant Guidelines Summary and Analysis Prompt is a free AI prompt that transforms dense grant documentation…
