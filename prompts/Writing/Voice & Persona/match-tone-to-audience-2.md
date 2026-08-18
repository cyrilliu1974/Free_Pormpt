# Audience Tone Adaptation Prompt for Copy

## 簡介

The Audience Tone Adaptation Prompt for Copy is a free AI prompt that rewrites marketing copy for multiple audience segments, adjusting tone, vocabulary, and framing to match each group's demographics and pain points. This audience tone adaptation prompt for ChatGPT works by analyzing your original copy and target segments, then producing a structured table that shows side-by-side adaptations. Each row contains the segment profile, the rewritten copy with vocabulary and emphasis tuned to that group's priorities, the tone characteristics applied, and an engagement score (1-10) estimating resonance. It runs on ChatGPT, Claude, Gemini, and Grok, preserving your core value proposition while shifting language, examples, and framing to fit each audience's context. Use it when launching campaigns across B2B and B2C segments, localizing messaging for different regions, or A/B testing tone variations before committing to production. ● Produces a markdown table comparing original copy against segment-specific adaptations, tone notes, and predicted engagement scores ● Maintains the core value proposition across all versions while adjusting vocabulary, pain-point emphasis, and examples to fit each audience ● Labels tone characteristics explicitly (formal vs. conversational, technical vs. accessible) so you understand the strategic choices in each rewrite ● Scores engagement potential (1-10) for each adaptation, helping prioritize which versions to test or deploy first ## Prompt

```
## Role
You are an expert copywriter and content strategist specializing in audience adaptation and multi-segment messaging.

## Task
Analyze the provided copy and create tailored versions for each audience segment. For every segment, adapt the messaging to resonate with their specific demographics, preferences, and pain points while preserving the core value proposition.

## Context
Original copy:
{{original-copy}}

Audience segments to target:
{{audience-segments}}

## Output
Provide a markdown table with the following structure:

| Audience Segment | Original Copy | Adapted Copy | Tone Characteristics | Engagement Score (1-10) |
|-----------------|---------------|--------------|---------------------|------------------------|

For each row:
- **Audience Segment**: Name and key characteristics of the segment
- **Original Copy**: The source copy (same for all rows)
- **Adapted Copy**: Version rewritten for that segment's language, priorities, and pain points
- **Tone Characteristics**: Specific tone and style choices used in the adaptation
- **Engagement Score**: Your assessment (1-10) of how effectively this version will resonate with the segment

Ensure each adaptation maintains the core message and value proposition while adjusting vocabulary, emphasis, examples, and framing to match each audience's context.
```

## 用法 / Usage
- 必填變數 / Variables: {{audience-segments}}、{{original-copy}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Audience Tone Adaptation Prompt for Copy is a free AI prompt that rewrites marketing copy for multiple aud…
