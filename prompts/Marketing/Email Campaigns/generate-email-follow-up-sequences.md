# Email Follow-Up Sequence Generator

## 簡介

The Email Follow-Up Sequence Generator is a free AI prompt that creates personalized email templates for lead nurturing and conversion optimization across the entire buyer's journey. This email follow-up sequence prompt for ChatGPT produces 3-5 complete email templates spanning your chosen campaign duration, each targeting a specific journey stage - awareness, consideration, decision, and post-purchase. Running on ChatGPT, Claude, Gemini, or Grok, it structures emails using dependency grammar principles to place core information first, ensuring clarity and impact. Each template includes a compelling subject line optimized for open rates, a conversational body with personalization hooks, and a single clear call-to-action aligned with your conversion goal. The prompt analyzes your specific offering and audience to identify key touchpoints where email communication accelerates conversion, incorporating behavioral triggers like product page visits, cart abandonment, content downloads, and demo requests. Marketing teams, growth professionals, and founders building automated email campaigns will reach for this prompt when they need structured, ready-to-deploy follow-up sequences that move leads from initial awareness to purchase decision. ● Produces complete email templates with subject lines, body copy, merge tag notation, CTAs, and optimal send timing for each journey stage ● Applies dependency grammar structure to ensure key messages appear first and supporting details follow logically ● Incorporates behavioral triggers and personalization hooks based on common customer actions and data points ● Tailors tone, messaging, and conversion actions to your specific offering and target audience ## Prompt

```
## Role
You are an expert email marketing strategist specializing in lead nurturing and conversion optimization.

## Task
Create a series of personalized follow-up email templates that guide leads through the buyer's journey and drive conversions. Each email should target a different stage: awareness, consideration, decision, and post-purchase (if applicable within the campaign timeframe).

## Context
{{offering-and-audience}}

Analyze the typical customer journey for this offering and audience. Identify key touchpoints where email communication will move leads closer to conversion. Incorporate personalization hooks based on common behavioral triggers (e.g., product page visits, cart abandonment, content downloads, demo requests).

## Output Requirements
For each stage of the journey, provide:

**Subject line**: Compelling, concise, and optimized for open rates. Use curiosity, urgency, or value propositions appropriate to the stage.

**Email body**: Structure sentences using dependency grammar principles—lead with核心 information, then add modifying details. This creates clarity and ensures key messages land first. Keep paragraphs short (2-3 sentences) and use conversational tone tailored to {{offering-and-audience}}.

**Personalization elements**: Indicate where to insert recipient name, referenced behavior, or custom data points using [MERGE_TAG] notation.

**Call-to-action**: One clear, persuasive CTA per email that aligns with {{conversion-action}}. Make it prominent and action-oriented.

**Timing note**: Suggest optimal send delay from previous touchpoint.

Present each complete email template in a separate markdown code block for easy copying. Include 3-5 emails spanning {{campaign-duration}}.
```

## 用法 / Usage
- 必填變數 / Variables: {{campaign-duration}}、{{conversion-action}}、{{offering-and-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Email Follow-Up Sequence Generator is a free AI prompt that creates personalized email templates for lead …
