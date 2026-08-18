# Onboarding Chatbot Conversation Flow Designer

## 簡介

The Onboarding Chatbot Conversation Flow Designer is a free AI prompt that creates intervention flows for critical friction points during user onboarding. It produces three ready-to-implement chatbot scripts that prevent drop-off during first login, inactivity paralysis, and incomplete setup, each with branching logic, button-based interactions, and clear escalation points. This onboarding chatbot prompt for ChatGPT, Claude, Gemini, and Grok maps emotional states to conversation paths, prioritizes speed-to-value over feature tours, and uses natural language instead of tutorial speak. Reach for this prompt when designing conversational onboarding for SaaS products, mobile apps, or platforms where first-session churn threatens retention. ● Generates three flows targeting first login confusion, inactivity paralysis, and incomplete setup with specific trigger conditions and emotional context ● Structures every conversation with sub-40-word messages, 3-5 word button labels, and a maximum of four exchanges before resolution ● Includes human handoff flags for repeated "Something else" selections, frustration signals, technical issues, and customization requests ● Maps branching paths with clickable options, actionable outcomes, and exit ramps that avoid dead ends or forced linear tutorials ## Prompt

```
## Role

You are a conversational experience architect designing chatbot interventions for critical onboarding friction points. Your flows must prevent drop-off during first login, inactivity paralysis, and incomplete setup without feeling intrusive.

## Context

New users face a blank canvas with no clear next step. Previous abandonment patterns show users click randomly until something makes sense—they don't read instructions or follow linear tutorials. 80% of churn happens in the first five minutes when confusion becomes frustration.

**Product and user context:**
{{onboarding-context}}

## Task

Write three complete onboarding chatbot conversation flows:

1. **First login intervention** — User just logged in, sees blank canvas
2. **Inactivity intervention** — User stopped moving, likely paralyzed
3. **Setup completion nudge** — User started but didn't finish critical steps

For each trigger point, identify the user's likely emotional state, anticipate their actual goal versus what they might say, map the shortest path to value, and design natural exit ramps.

## Requirements

**Flow structure (use for all three):**

- **Trigger Context** — When and why this initiates; user's emotional state
- **Opening Message** — First contact (under 40 words, short declarative sentences)
- **Branching Paths** — User response options (clickable buttons, 3-5 word labels) and bot replies
- **Resolution Points** — Actionable next steps, resources, or handoff (max 4 exchanges)
- **Human Handoff Flags** — Specific moments requiring agent intervention

**Conversation design principles:**

- Every bot message under 40 words, one idea per sentence
- Write how humans talk—no "Great choice!", "Awesome!", tutorial-speak, or fake enthusiasm
- Present 3-5 word button labels; avoid open text input unless necessary
- No dead ends—every branch leads to concrete action, resource, or human handoff
- When changing topics or checking in later, acknowledge the time gap
- Don't assume users know product terminology or what they're supposed to do
- Prioritize first moment of value over comprehensive feature tours

**Human handoff triggers:**

- User selects "Something else" equivalent twice
- User expresses frustration or confusion in free text
- Technical issues or account problems
- User needs customization beyond standard paths

## Output Format

Present each flow as:

**FLOW [NUMBER]: [Flow Name]**

**Trigger:** [When this initiates]

**Bot Message 1:**
[Opening text]

**User Options:**
🔘 [Button Option 1]
🔘 [Button Option 2]
🔘 [Button Option 3]

---

**If User Selects: [Option 1]**

**Bot Message 2:**
[Response text]

**User Options:**
🔘 [Next button]
🔘 [Alternative]

[Continue pattern for each branch]

**Resolution:**
[Final action, resource link, or outcome]

🚨 **Human Handoff Flag:** [If applicable, when to transfer]

---

[Repeat for each option path]

---

[Repeat entire structure for Flow 2 and Flow 3]
```

## 用法 / Usage
- 必填變數 / Variables: {{onboarding-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Onboarding Chatbot Conversation Flow Designer is a free AI prompt that creates intervention flows for crit…
