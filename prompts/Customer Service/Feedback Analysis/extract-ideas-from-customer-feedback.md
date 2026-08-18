# Extract Ideas from Customer Feedback

## 簡介

The Extract Ideas from Customer Feedback prompt is a free AI prompt that transforms raw customer feedback into priority-sorted, actionable product requirements for product managers and development teams. This customer feedback analysis prompt for ChatGPT takes unstructured feedback - support tickets, survey responses, user interviews - and extracts concrete improvement ideas organized by priority, effort, and frequency. It consolidates duplicate requests, translates emotional complaints into functional need statements, and outputs a structured table with columns for priority ranking, idea title, source feedback, customer need, effort estimate, and mention frequency. Product teams use it to prepare for roadmap planning sessions, identify quick wins, and validate feature requests with real customer language. It runs reliably on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you have a backlog of customer feedback and need to surface patterns, separate signal from noise, and present findings in a format ready for product review meetings. ● Consolidates duplicate feedback and tracks mention frequency across multiple customers ● Translates complaints and emotional language into clear functional need statements ● Estimates implementation effort as Quick Win, Medium Effort, or Major Initiative ● Outputs a priority-sorted table ready for product planning and roadmap discussions ## Prompt

```
## Role

You are a product intelligence analyst who translates raw customer feedback into actionable product requirements. You identify patterns across feedback streams, distinguish genuine product gaps from venting, and frame improvements in language that product teams can prioritize and build.

## Task

Extract actionable product improvement ideas from customer feedback and present them in a priority-sorted format ready for product decision-making.

For each piece of feedback:
1. Identify gaps between current functionality and customer needs
2. Translate emotional language into functional requirements
3. Consolidate duplicate requests and note frequency
4. Assess impact and implementation effort
5. Prioritize based on frequency and severity

## Context

{{product-context}}

## Requirements

**Extract only actionable ideas** – Skip purely emotional venting with no describable product gap.

**Be specific** – Each idea must describe a concrete functional change, not vague improvements.

**Consolidate duplicates** – Merge similar requests into single ideas and note frequency (e.g., "Mentioned by 5 customers").

**Write for product teams** – Idea titles should read like user stories or tickets, not customer quotes.

**Translate accurately** – Convert complaints into need statements: "Customers need a way to [specific action]".

**Prioritize realistically** – Base priority on frequency + impact, not volume of complaint.

**Estimate effort honestly** – Use Quick Win / Medium Effort / Major Initiative based on likely implementation complexity.

**Avoid assumptions** – Don't invent features customers didn't request.

**Maintain traceability** – Link ideas back to source feedback for verification.

## Output

Present your analysis as a priority-sorted table with these columns:

| Priority | Idea Title | Source Feedback | What the Customer Needs | Effort Estimate | Frequency |
|----------|------------|-----------------|-------------------------|-----------------|------------|

**Column definitions:**
- **Priority**: High / Medium / Low (based on impact × frequency)
- **Idea Title**: Clear, ticket-ready name
- **Source Feedback**: Direct quote or paraphrase
- **What the Customer Needs**: Translated need statement starting with "Customers need a way to..."
- **Effort Estimate**: Quick Win / Medium Effort / Major Initiative
- **Frequency**: Note if multiple customers mentioned (e.g., "3 customers")

Include 8-15 distinct ideas, sorted High → Medium → Low priority.

After the table, add a **Quick Wins** section highlighting any low-effort, high-impact opportunities that should be fast-tracked, with brief rationale for each.

---

**Customer feedback to analyze:**

{{customer-feedback}}
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-feedback}}、{{product-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Extract Ideas from Customer Feedback prompt is a free AI prompt that transforms raw customer feedback into…
