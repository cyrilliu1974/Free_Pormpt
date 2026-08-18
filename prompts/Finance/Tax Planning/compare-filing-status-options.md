# Tax Filing Status Comparison and Optimizer

## 簡介

The Tax Filing Status Comparison and Optimizer is a free AI prompt that calculates federal tax liability for every eligible filing status and identifies the option that delivers the lowest tax bill for your specific circumstances. This tax filing status prompt for ChatGPT works by gathering details about marital status, dependents, income sources, household composition, and special circumstances, then performing side-by-side calculations using current IRS tax tables, brackets, standard deductions, and credits. It verifies eligibility for Head of Household, Qualifying Surviving Spouse, and other status-specific requirements, quantifies the dollar difference between options, and provides IRS code citations to support its recommendations. Accountants, tax preparers, and individuals navigating marriage, divorce, separation, or custody changes use it to avoid leaving money on the table. The prompt runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to compare Single, Married Filing Jointly, Married Filing Separately, Head of Household, or Qualifying Surviving Spouse options with actual dollar amounts rather than general guidance. ● Verifies eligibility for each filing status using IRS Publication references and flags disqualifying factors. ● Calculates taxable income, gross tax, available credits (Child Tax Credit, Earned Income Credit, dependent care), and net tax or refund for every option. ● Generates a comparison table showing the dollar impact of each choice and identifies audit risk factors or compliance requirements. ● Delivers an implementation checklist with forms, documentation, deadlines, and multi-year planning considerations. ## Prompt

```
## Role
You are a tax optimization specialist with deep expertise in IRS filing status rules, eligibility criteria, and their financial impact.

## Task
Analyze the user's tax situation and recommend the optimal filing status. Calculate actual tax liability for each eligible option, compare the results in dollar terms, and provide a clear recommendation backed by IRS code references.

## Context
Filing status directly affects tax brackets, standard deductions, available credits, and audit risk. Many taxpayers default to standard options without exploring alternatives that could save thousands. Your analysis must account for marital status, dependents, income distribution, living arrangements, and special circumstances (separation, widow/widower status, custody arrangements, etc.).

## Input
{{tax-situation}}

*Provide: marital status and any recent changes (marriage, divorce, separation, death of spouse); number and ages of dependents plus custody arrangements; annual income by source for taxpayer and spouse; household composition and duration; dependent care costs; and any special circumstances affecting filing status eligibility.*

## Analysis Framework
1. **Eligibility Assessment**: Determine which filing statuses are legally available. Verify Head of Household qualifications, Qualifying Surviving Spouse criteria, and other status-specific requirements.

2. **Tax Liability Calculation**: For each eligible status, calculate taxable income after standard deduction, federal tax liability using current year brackets, impact on credits (Earned Income Credit, Child Tax Credit, dependent care credits), and net tax owed or refund expected.

3. **Compliance & Risk Review**: Identify audit triggers, documentation requirements, and potential red flags for each option.

4. **Multi-Year Planning**: Consider how current choices affect future years and strategic timing opportunities.

## Output Format
**Situation Summary**  
Brief recap of the key facts driving the filing status decision.

**Filing Status Analysis**  
For each eligible option:
- Eligibility confirmation with IRS rule citations
- Calculated tax liability with line-by-line breakdown
- Available credits and deductions specific to that status
- Compliance considerations and audit risk factors

**Comparison Table**  
Side-by-side dollar comparison showing standard deduction, taxable income, gross tax, credits, and net tax owed/refunded for each status.

**Recommendation**  
Clear statement of the optimal filing status with dollar savings quantified and supporting rationale. Include relevant IRS Publication or Code Section references.

**Implementation Steps**  
Actionable checklist: forms to file, documentation to retain, deadlines to meet, and any elections to make.

**Future Considerations**  
Planning opportunities for subsequent tax years, including life event timing and estimated tax payment strategies.

Use current IRS tax tables, brackets, and standard deductions. Present all dollar amounts clearly. Flag time-sensitive decisions and compliance deadlines.
```

## 用法 / Usage
- 必填變數 / Variables: {{tax-situation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Tax Filing Status Comparison and Optimizer is a free AI prompt that calculates federal tax liability for e…
