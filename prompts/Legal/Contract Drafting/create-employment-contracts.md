# Employment Contract Generator for ChatGPT

## 簡介

The Employment Contract Generator is a free AI prompt that drafts comprehensive employment agreements tailored to specific positions and company requirements. This employment contract prompt for ChatGPT guides the model to produce legally structured documents covering all essential elements: party identification and employment term, job responsibilities and reporting structure, compensation and bonus arrangements, benefits packages including health insurance and paid time off, confidentiality and non-disclosure obligations, termination conditions with notice periods and severance terms, and governing law provisions. It runs on ChatGPT, Claude, and Gemini, transforming employment details into professional contract documents that balance legal precision with readability. Legal teams, HR departments, and small business owners use it to create consistent, thorough employment agreements without starting from scratch each time. ● Produces complete contracts with logical section flow from parties and term through responsibilities, compensation, benefits, confidentiality, termination, and signature blocks ● Uses professionally appropriate legal language that remains accessible and avoids ambiguous phrasing that could trigger disputes ● Tailors all contract terms to the specific position details, company circumstances, and employment relationship provided in the input ● Covers essential protection mechanisms including confidentiality obligations, material return requirements, at-will status, notice periods, and cause termination grounds ## Prompt

```
## Role
You are an expert employment lawyer drafting a comprehensive employment contract. Use clear, legally sound language in a logical structure that covers all essential aspects of the employment relationship.

## Task
Draft a complete employment contract that includes:

**Parties & Term**
- Employer, employee name, and position
- Start date, end date (if applicable), and probationary period

**Responsibilities & Compensation**
- Primary and additional duties
- Reporting structure
- Base salary, bonus structure, and payroll schedule

**Benefits Package**
- Health insurance, retirement plan, paid time off, and other benefits

**Confidentiality & Termination**
- Definition of confidential information and non-disclosure obligations
- Return of materials requirements
- At-will employment status, notice period, severance terms, and grounds for cause termination

**Governing Law & Signatures**
- Jurisdiction governing the contract
- Signature lines for employer, employee, and date

## Context
{{employment-details}}

## Output
Format as a structured employment contract document with clearly labeled sections. Use professional legal language while remaining accessible. Tailor all terms to the specific position and company circumstances provided. Avoid ambiguous terms that could lead to disputes.
```

## 用法 / Usage
- 必填變數 / Variables: {{employment-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Employment Contract Generator is a free AI prompt that drafts comprehensive employment agreements tailored…
