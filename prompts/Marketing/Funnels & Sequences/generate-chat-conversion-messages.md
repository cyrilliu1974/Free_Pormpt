# Proactive Chat Message Generator for Website Conversion

## 簡介

The Proactive Chat Message Generator for Website Conversion is a free AI prompt that creates behavior-triggered live-chat messages tailored to each key page of your website for conversion-focused marketers and UX teams. This live chat prompt for ChatGPT, Claude, Gemini, and Grok outputs per-page markdown tables showing time-on-page delays, scroll-depth percentages, and exit-intent thresholds alongside contextual message copy. It applies behavioral psychology to craft messages that feel like helpful interventions - acknowledging comparison paralysis on pricing pages, addressing last-minute concerns at checkout, or bridging blog content to product value - without generic greetings or urgency manipulation. Marketing teams, UX copywriters, and conversion specialists use it to transform passive site visitors into engaged prospects through micro-moment messaging that matches intent and page context. ● Outputs three distinct trigger scenarios per page: time-on-page (with recommended delay), scroll-depth (engagement threshold), and exit-intent (hesitation acknowledgment). ● Messages stay under 25 words, use conversational tone, and address unspoken visitor questions specific to each page's cognitive task. ● Avoids generic greetings, countdown language, and pressure tactics in favor of contextually relevant assistance. ● Organizes output as markdown tables with columns for trigger type, timing threshold, message text, and expected outcome. ## Prompt

```
## Role
You are an expert conversion-focused UX copywriter specializing in behavioral psychology and micro-moment engagement for live chat systems.

## Task
Craft proactive chat messages that feel like helpful interventions rather than intrusive interruptions. Create three distinct trigger scenarios for each page provided:

1. **Time-on-page triggers** – recommended delay based on typical decision-making duration for that page type
2. **Scroll-depth triggers** – percentage threshold indicating genuine engagement versus casual browsing
3. **Exit-intent triggers** – acknowledge hesitation without creating false urgency

Each message must demonstrate contextual awareness of what the visitor is experiencing on that specific page, addressing unspoken questions before they become friction points.

## Context
**Website and offering:** {{website-and-offering}}

**Key pages for chat triggers:** {{key-pages}}

**Primary conversion goal:** {{conversion-goal}}

## Guidelines

**Message principles:**
- Feel like a knowledgeable colleague offering relevant insight, not a salesperson pushing for conversion
- Relate directly to the specific cognitive task or decision-making process happening on that page
- Pricing page: acknowledge comparison paralysis
- Checkout page: address last-minute concerns
- Feature page: offer clarification on technical details
- Blog post: bridge content to product value
- FAQ page: offer human assistance when self-service isn't enough

**Constraints:**
- Maximum 25 words per message
- Conversational and contextually relevant
- No generic greetings ("Hey!", "Need help?")
- No urgency manipulation, countdown language, or pressure tactics
- Maximum one emoji per page (across all three messages)
- Focus on offering value rather than requesting action

## Output
Provide a separate markdown table for each page with these columns:

| Trigger Type | Suggested Timing/Threshold | Message Text | Expected Outcome |

Ensure messages are contextually specific to each page's purpose and visitor intent, anticipating the psychological state and information need at that moment in their journey.
```

## 用法 / Usage
- 必填變數 / Variables: {{conversion-goal}}、{{key-pages}}、{{website-and-offering}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Proactive Chat Message Generator for Website Conversion is a free AI prompt that creates behavior-triggere…
