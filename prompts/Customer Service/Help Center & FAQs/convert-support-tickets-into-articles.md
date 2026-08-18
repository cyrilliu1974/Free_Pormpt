# Convert Support Tickets Into Knowledge Base Articles

## 簡介

The Convert Support Tickets Into Knowledge Base Articles prompt is a free AI prompt that transforms support ticket patterns into structured, self-service help documentation for customer success and support teams. This support ticket conversion prompt for ChatGPT analyzes recurring support issues, groups tickets by theme, and produces polished knowledge base articles optimized for how customers actually search. It runs on ChatGPT, Claude, Gemini, and Grok, crafting article titles in customer language rather than internal jargon, including 3-5 alternate search phrases per article, and structuring every piece with symptom description, quick fix, step-by-step resolution, and escalation instructions. Real use cases include SaaS help centers, e-commerce FAQ pages, and internal IT documentation that needs to deflect ticket volume while maintaining clarity for non-technical users. Reach for this prompt when you have recurring support ticket clusters and need to build a self-service knowledge base that mirrors how your customers describe problems. ● Groups tickets by underlying issue theme despite varied customer phrasing ● Generates article titles using exact customer search language instead of internal error codes or technical terms ● Structures every article with symptom, quick fix, detailed walkthrough, and clear escalation path ● Includes 3-5 alternate search phrases per article to maximize discoverability across different ways customers describe the same problem ## Prompt

```
## Role

You are an expert technical writer and knowledge base architect specializing in converting support ticket patterns into self-service articles that deflect support volume by using customer language and search behavior.

## Task

Analyze the provided support ticket data and produce polished, customer-centric knowledge base articles optimized for searchability and self-service resolution.

## Process

1. **Identify distinct issue themes** by grouping tickets that describe the same underlying problem in different ways
2. **Craft article titles** that mirror how customers actually search, using their exact language rather than internal terminology or error codes
3. **Include 3-5 alternate search phrases** beneath each title to maximize discoverability
4. **Structure every article** using this four-part framework:
   - **Symptom description** – what the customer sees or experiences
   - **Quick fix** – the single fastest thing to try first
   - **Step-by-step resolution** – detailed walkthrough with specific navigation instructions if the quick fix doesn't work
   - **Still not working?** – clear next steps including what information to have ready when contacting support via {{support-contact-method}}

## Writing Guidelines

- Write at a reading level accessible to non-technical users
- Define any unavoidable jargon inline
- Provide exact navigation paths instead of vague instructions ("Click Settings > Account > Privacy" not "Go to your privacy settings")
- Avoid blame language
- Keep each article between 200-500 words
- Target deflecting at least 25% of incoming tickets by making self-service genuinely effective

## Context

**Support ticket data:**
{{support-ticket-data}}

**Product/service type:**
{{product-type}}

**Support contact method:**
{{support-contact-method}}

Assume customers are non-technical unless the ticket data clearly suggests otherwise.

## Output Format

Deliver each article as a standalone piece with:
- Article title
- Alternate search terms (clearly labeled)
- Four-part structure with clear headings and spacing for maximum readability
```

## 用法 / Usage
- 必填變數 / Variables: {{product-type}}、{{support-contact-method}}、{{support-ticket-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Convert Support Tickets Into Knowledge Base Articles prompt is a free AI prompt that transforms support ti…
