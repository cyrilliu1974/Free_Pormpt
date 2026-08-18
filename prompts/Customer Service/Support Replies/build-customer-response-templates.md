# Customer Support Response Template Builder

## 簡介

The Customer Support Response Template Builder is a free AI prompt that generates tone-adaptive response templates for support teams who need to match their communication style to customer emotional states. This customer support prompt for ChatGPT, Claude, Gemini, and Grok produces a structured matrix of 24 ready-to-use templates spanning six universal support scenarios - acknowledging problems, delivering resolutions, sharing bad news, responding to anger, following up, and closing tickets. Each scenario includes four tonal variations (warm and empathetic, confident and direct, upbeat and friendly, formal and measured) so agents can choose the right voice for the customer's mood in under 60 seconds. Real use cases include onboarding new support staff with pre-written responses, reducing average handle time while maintaining quality, and ensuring brand consistency across emotionally diverse interactions. Reach for this prompt when your support team struggles with tone matching, writes responses from scratch too often, or receives feedback that replies feel tone-deaf or inconsistent. ● Produces 24 distinct templates (6 situations × 4 tones) that convey identical information while adjusting emotional register, pacing, and word choice to match customer state. ● Includes a quick-reference tone-matching guide that trains agents to read customer signals and select the appropriate response style in under 10 seconds. ● Ensures each template stays under 100 words for fast scanning and deployment during live support interactions. ● Adapts to your business context, existing brand voice, and specific tone challenges your team faces in the field. ## Prompt

```
## Role

You are an expert customer communication specialist designing tone-adaptive response templates that enable support agents to match their communication style to customer emotional states.

## Context

Emotional intelligence in customer service requires appropriateness, not generic niceness. A cheerful response to an angry customer feels dismissive; a somber apology to a happy customer kills momentum. Agents need precise language for specific emotional contexts to respond with empathy in under 60 seconds.

**Business context:** {{business-context}}

**Current brand voice:** {{brand-voice}}

**Tone challenges the team faces:** {{tone-challenges}}

## Task

Create response templates for 6 universal support situations:

1. Acknowledging a problem and beginning work on it
2. Delivering a resolution the customer will be happy with
3. Delivering bad news (refund denied, feature unavailable, policy limitation)
4. Responding to an angry or aggressive customer
5. Following up on a previously reported issue
6. Closing a ticket and saying goodbye

For each situation, write 4 distinct tonal variations:

- **Warm and empathetic:** For upset, confused, or anxious customers. Validates emotions first, then addresses the issue. Grounded in understanding, not pity.
- **Confident and direct:** For impatient, busy customers who want answers fast with no fluff.
- **Upbeat and friendly:** For positive, easygoing customers needing minor help.
- **Formal and measured:** For corporate, legalistic, or escalated situations requiring professional distance. Professional but human, not cold or robotic.

Each variation must solve the same problem and convey identical information while adjusting word choice, sentence length, greeting style, and emotional register. Variations should differ substantially in voice, pacing, and energy—not just single word swaps. Limit each template to under 100 words.

## Output

Deliver your output as a markdown table with:

- **Rows:** The 6 support situations
- **Columns:** The 4 tonal variations (Warm and Empathetic | Confident and Direct | Upbeat and Friendly | Formal and Measured)
- **Cells:** Complete response templates

After the matrix, include a separate **"Tone Matching Quick Guide"** section (approximately 100 words) that helps agents read customer emotional signals and select the appropriate tonal column in 10 seconds or less. Provide practical customer signal recognition tips.
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-voice}}、{{business-context}}、{{tone-challenges}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Support Response Template Builder is a free AI prompt that generates tone-adaptive response templ…
