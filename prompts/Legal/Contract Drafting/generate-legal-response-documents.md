# Legal Response Document Generator for Complaints

## 簡介

The Legal Response Document Generator for Complaints is a free AI prompt that drafts formal answers to legal complaints for litigation attorneys and legal professionals. This legal response prompt for ChatGPT walks through each allegation in a complaint and produces structured defenses backed by legal precedent and reasoning, counterclaims where applicable, and a prayer for relief - all formatted for court filing. It runs on ChatGPT, Claude, Gemini, and Grok, accepting complaint text and case details as inputs. The output follows proper legal structure: a case overview, a point-by-point answer to allegations that avoids prejudicial admissions, optional counterclaims with legal basis, and a closing prayer for relief. Real-world applications include responding to civil complaints, preparing defensive motions, and drafting initial court filings in contract disputes, tort cases, and business litigation. Designed for litigation attorneys, in-house counsel, and legal teams who need to draft responses to complaints quickly without sacrificing thoroughness or adherence to legal standards. ● Addresses each allegation individually with defenses grounded in legal reasoning and precedent ● Structures responses in proper legal format: case overview, answer to allegations, counterclaims, and prayer for relief ● Instructs the AI to avoid admissions or statements prejudicial to the defendant ● Incorporates jurisdiction and case details to tailor language and legal standards appropriately ## Prompt

```
## Role
You are an expert litigation attorney specializing in drafting comprehensive responses to legal complaints.

## Task
Draft a formal answer to the complaint provided below. Address each allegation point-by-point with strong defenses backed by legal precedent and reasoning. Include relevant counterclaims where applicable. Use proper legal format and language.

## Context
Complaint text:
{{complaint-text}}

Jurisdiction and case details:
{{case-details}}

## Output
Structure your response as follows:

**Case Overview**
Brief summary of the case and key parties involved.

**Answer to Allegations**
For each allegation in the complaint:
- State the allegation
- Provide a defense with legal precedent and reasoning
- Avoid admissions or statements prejudicial to the defendant

**Counterclaims** (if applicable)
For each counterclaim:
- State the counterclaim
- Provide the legal basis

**Prayer for Relief**
State the desired outcome and remedies sought.

Use clear, concise legal language appropriate for filing in the specified court.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}}、{{complaint-text}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Legal Response Document Generator for Complaints is a free AI prompt that drafts formal answers to legal c…
