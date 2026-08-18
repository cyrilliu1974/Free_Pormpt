# Customer Onboarding Survey Builder

## 簡介

The Customer Onboarding Survey Builder is a free AI prompt that creates conversational post-onboarding surveys designed to maximize completion rates while uncovering actionable insights for product teams and customer success managers. This customer onboarding survey prompt for ChatGPT, Claude, Gemini, and Grok produces a structured questionnaire for users who have completed their first two weeks with your product. It balances quantitative rating questions with qualitative open-ended follow-ups, ensuring each question ties directly to improving onboarding or flagging at-risk accounts. You supply your product description, customer base, and suspected friction points, and the prompt returns a logical flow of under 10 questions complete with scale labels, question rationale, and insight targets. Teams building SaaS onboarding flows, customer success programs, or product-led growth funnels use it to replace generic satisfaction surveys with research-grade instruments that respect user time. Reach for this prompt when you need a survey that feels genuinely interested in helping customers rather than collecting vanity metrics, or when your existing feedback tools yield high abandonment and low signal. ● Outputs conversational, non-leading questions that flow from broad impressions to specific pain points and forward-looking engagement opportunities. ● Includes full scale labels for every rating question to remove respondent ambiguity and improve data quality. ● Frames open-ended questions to elicit specific, actionable feedback rather than generic praise or complaints. ● Explains the insight captured by each question so your team understands what to do with the responses. ## Prompt

```
## Role

You are an expert customer research specialist who designs surveys that maximize completion rates while surfacing genuinely actionable insights.

## Task

Create a post-onboarding customer survey for users who have completed their first two weeks with the product. The survey must:

- Balance quantitative rating questions with qualitative open-ended questions that uncover the "why" behind the numbers
- Ensure each question serves a clear purpose tied to improving the onboarding experience or identifying at-risk customers
- Avoid double-barreled questions, leading language, and corporate checkbox exercises
- Flow naturally from broad impressions to specific pain points, ending with forward-looking engagement opportunities
- Feel conversational, relevant, and genuinely interested in helping rather than just collecting metrics
- Stay under 10 total questions to respect the customer's time

## Context

**Product:** {{product-description}}

**Customer base:** {{customer-base}}

**Suspected friction points:** {{friction-points}}

Assume typical onboarding materials (tutorial videos, documentation, email sequence) and standard support channels (in-app chat, email, knowledge base) unless the product description indicates otherwise.

## Output

For each survey question, provide:

1. **Question text** (conversational, non-technical language)
2. **Question type** (rating scale or open-ended)
3. **Scale details** (for rating questions: full scale with labels, e.g., 1 = Very Difficult, 5 = Very Easy)
4. **Insight captured** (brief note explaining what this question reveals)

Structure the survey to progress logically through the customer experience. For rating questions, provide clear scale labels that remove ambiguity. For open-ended questions, frame them to encourage specific, actionable responses rather than generic praise or complaints.
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-base}}、{{friction-points}}、{{product-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Onboarding Survey Builder is a free AI prompt that creates conversational post-onboarding surveys…
