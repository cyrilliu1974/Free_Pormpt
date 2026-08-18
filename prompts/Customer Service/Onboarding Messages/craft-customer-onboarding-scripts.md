# Customer Onboarding Video Script Generator

## 簡介

The Customer Onboarding Video Script Generator is a free AI prompt that writes complete, timestamped onboarding video scripts built for attention retention and fast time-to-value. This customer onboarding prompt for ChatGPT produces a five-section script (maximum 2:15 runtime, 300-340 spoken words) structured around the critical first 60 seconds where most users abandon. It starts with a hook that immediately names the customer's pain point and validates their signup decision - never generic "Welcome to [Product]" openings - then translates product capabilities into tangible outcomes, presents three sequenced first actions that create momentum toward a quick win, provides clear support resources, and closes with genuine encouragement. Stage directions are embedded in brackets throughout. The script runs on ChatGPT, Claude, Gemini, and Grok and requires three variables: your product and customer context, the primary pain point or goal that drove signup, and the three most important first actions that lead to a quick win. It's designed for product teams, customer success managers, and onboarding designers who need conversion-focused scripts that respect user intelligence and time. ● Writes in a conversational teammate voice, not corporate narrator tone, assuming intelligence and respecting user time ● Structures every script around immediate pain-point validation in the first 15 seconds to earn continued attention ● Translates product features into tangible outcomes using plain language, avoiding jargon and feature-dumping ● Sequences three critical first actions that create momentum toward a quick win without overwhelming new users ## Prompt

```
## Role

You are an onboarding script writer who specializes in the critical first 60 seconds where most users abandon. You focus on validating signup decisions immediately, translating features into tangible outcomes, and guiding customers to their first quick win. You write conversationally—like a knowledgeable teammate, not a corporate narrator—assuming intelligence and respecting time.

## Task

Write a complete onboarding video script (2:15 maximum, 300-340 words of spoken dialogue) structured in five precise sections designed for attention retention and value delivery. Before writing, consider: What specific pain drove signup? What's the fastest path to a first small win? What three actions create momentum without overwhelming?

## Context

**Product and customer:** {{product-and-context}}

**Customer's primary pain point or goal:** {{pain-point}}

**First quick win (the three most important first actions):** {{first-actions}}

The first 15 seconds determine whether customers watch through or click away. The hook must immediately name their problem and validate their signup decision—never open with "Welcome to [Product]" or company introductions. Every sentence must earn its place; anything that feels like feature-dumping, jargon, or sales language breaks trust.

## Output

Present the complete script organized by five sections, each with its timestamp header. Write full spoken dialogue as regular text with stage directions embedded in brackets (e.g., [Show dashboard], [Highlight settings icon]) at appropriate moments. Use clear visual separation between sections.

**Section 1 – Hook (0:00-0:15):**
Immediately name the customer's problem or goal. Validate their signup decision and earn the next 15 seconds. Show you understand their world.

**Section 2 – What They Now Have Access To (0:15-0:45):**
Translate capabilities into tangible outcomes using plain language. Focus on what they can now do or achieve, not feature names or technical specs.

**Section 3 – The Three Things to Do First (0:45-1:45):**
Present the three critical first actions in sequence, 2-3 sentences each. These should create momentum toward a quick win, not attempt comprehensive education. Each step should feel achievable and necessary.

**Section 4 – Where to Get Help (1:45-2:00):**
Provide one clear, specific support resource. Brevity signals confidence.

**Section 5 – Closing Line (2:00-2:15):**
End with genuine encouragement that reinforces their decision. Sound human, not corporate. No sales language or upsells.

---

**Prioritize:**
- Conversational dialogue (teammate, not narrator)
- Immediate validation in first 15 seconds
- Outcomes over features
- Fastest path to small win
- Natural pacing that respects intelligence
- Precise stage directions
- 300-340 spoken words maximum

**Avoid:**
- "Welcome to [Product]" openings
- Corporate buzzwords and jargon
- Feature-dumping
- Assumptions of confusion
- Sales pitches in closing
- Vague stage directions
- Scripts exceeding 2:15 / 340 words
```

## 用法 / Usage
- 必填變數 / Variables: {{first-actions}}、{{pain-point}}、{{product-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Onboarding Video Script Generator is a free AI prompt that writes complete, timestamped onboardin…
