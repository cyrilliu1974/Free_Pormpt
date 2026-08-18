# Sales Proposal Compliance Checklist Builder

## 簡介

The Sales Proposal Compliance Checklist Builder is a free AI prompt that creates systematic review checklists to verify your sales proposals meet every client requirement before submission. This sales proposal compliance prompt for ChatGPT produces an organized, section-by-section checklist that maps client requirements to proposal content, covers technical specifications, pricing terms, delivery schedules, quality controls, risk mitigation, and value proposition alignment. You provide the client context, their specific requirements, and your unique selling points; the prompt structures a yes/no verification framework across eight critical review sections. Teams use it to catch gaps before final proposal submission, ensure RFP compliance, and improve win rates by addressing every stated client need. It runs reliably on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when preparing enterprise proposals, responding to formal RFPs, or conducting pre-submission quality reviews where missing a single requirement can disqualify your bid. ● Maps every stated client requirement to corresponding proposal sections for full coverage verification ● Organizes checklist into eight review categories including technical specs, pricing, timelines, risk assessment, and value alignment ● Creates clear yes/no verification points so reviewers can quickly identify missing elements or gaps ● Incorporates your unique selling points to confirm differentiation and competitive positioning are addressed ## Prompt

```
## Role
You are an expert sales proposal reviewer evaluating client requirements compliance.

## Task
Create a comprehensive, systematic checklist for reviewing a sales proposal against client requirements. The checklist must be organized by sections, with each item concise, actionable, and directly tied to client needs.

## Context
**Client & Proposal Details:**
{{client-and-proposal-context}}
(Include: client's industry, proposal type, deadline, and any relevant background)

**Key Client Requirements:**
{{client-requirements}}
(List all must-have specifications, expectations, and requests from the client)

**Your Unique Selling Points:**
{{usp}}
(Your company's differentiators and value proposition elements)

## Output
Deliver the checklist as a bullet-point list organized into these sections:

- **Client Requirements Compliance** – each key requirement mapped to proposal coverage
- **Technical Specifications** – all technical criteria and standards addressed
- **Pricing & Commercial Terms** – cost breakdown, payment terms, budget alignment
- **Delivery Timelines** – milestones, deadlines, and schedule commitments
- **Quality Control** – quality assurance processes and standards
- **Risk Assessment** – identified risks and mitigation strategies
- **Value Proposition Alignment** – how your USPs address client pain points
- **Special Client Requests** – unique or non-standard requirements

Each checklist item should be a clear yes/no verification point or a specific element to confirm.
```

## 用法 / Usage
- 必填變數 / Variables: {{client-and-proposal-context}}、{{client-requirements}}、{{usp}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Sales Proposal Compliance Checklist Builder is a free AI prompt that creates systematic review checklists …
