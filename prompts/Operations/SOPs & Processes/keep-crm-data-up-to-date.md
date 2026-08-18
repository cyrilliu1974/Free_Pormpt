# CRM Data Update Process Template

## 簡介

The CRM Data Update Process Template is a free AI prompt that creates a structured workflow for maintaining accurate customer information in your CRM system for sales and marketing teams. This CRM data management prompt for ChatGPT walks you through a five-step verification process, then outputs a ready-to-use markdown table for recording Name, Email, Phone, and Last Contact Date updates. It runs on ChatGPT, Claude, Gemini, and Grok, and adapts to any CRM platform - Salesforce, HubSpot, Pipedrive, or custom systems. Real-world use cases include quarterly data audits, post-campaign contact cleanup, and onboarding legacy records into a new CRM. The prompt emphasizes verification before changes, flags incomplete entries for manual review, and helps you spot data-quality patterns that inform future process improvements. Reach for this prompt when you need a repeatable SOP for CRM hygiene, whether you're a solo founder managing a hundred contacts or a RevOps team scaling to thousands of records. ● Systematic five-step process covering record access, field review, verification, flagging, and documentation ● Markdown table template with columns for Name, Email, Phone, and Last Contact Date, plus inline instructions for each field ● Built-in data validation rules: email format checks, phone country-code guidance, ISO date formatting, and flagging logic for generic addresses ● Context-aware design that adapts to your industry and CRM platform through two simple variables ## Prompt

```
## Role
You are a Customer Relationship Management (CRM) specialist responsible for maintaining accurate, current customer data to support sales and marketing operations.

## Task
Create a systematic process for updating customer records in {{crm-platform}}, ensuring data integrity across Name, Email, Phone, and Last Contact Date fields.

## Context
- Industry: {{business-context}}
- Records are updated based on information from your primary data sources
- Incomplete or suspicious records should be flagged for manual review
- Pattern detection during updates will inform future CRM strategy

## Process
1. Access the CRM platform and identify records requiring updates
2. Review each field systematically, prioritizing the four core data points
3. Verify existing data accuracy before making changes
4. Flag records with missing or questionable information
5. Document significant changes, trends, or data quality issues observed

## Output
Provide your customer data update template as a markdown table:

| Name | Email | Phone | Last Contact Date |
|------|-------|-------|-------------------|
| [Full customer name] | [Valid email address] | [Phone with country code if international] | [YYYY-MM-DD format] |
| [Next customer...] | [...] | [...] | [...] |

**Instructions for completion:**
- **Name**: Enter full legal or preferred business name
- **Email**: Verify format validity; flag generic addresses (info@, admin@) for review
- **Phone**: Include country/area codes; note preferred contact method if known
- **Last Contact Date**: Use ISO format (YYYY-MM-DD); record the most recent meaningful interaction
- **Flagging**: Add a note column or asterisk (*) next to incomplete/uncertain entries for follow-up
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{crm-platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The CRM Data Update Process Template is a free AI prompt that creates a structured workflow for maintaining ac…
