# Customer Service Training Scenario Generator

## 簡介

The Customer Service Training Scenario Generator is a free AI prompt that creates multi-turn role-play exercises with hidden complexities, best-practice agent responses, and coaching annotations for support teams. This customer service training prompt for ChatGPT builds complete practice scenarios across varied issue categories - billing disputes, angry escalations, technical support, cancellations, and policy confusion - each with natural human dialogue, realistic frustration levels, and a hidden root cause that agents must diagnose through careful questioning. Every scenario models empathy-first responses, clarifying questions before solutions, and de-escalation techniques, with inline training notes that explain why each agent move works. The output runs on ChatGPT, Claude, Gemini, and Grok, and you control the industry context and number of scenarios generated. Ideal for contact center trainers, team leads, and L&D professionals building onboarding or upskilling programs. ● Full turn-by-turn customer-agent dialogues with realistic emotion, account details, and conversational texture ● Hidden complexities in every scenario that require the agent to uncover the real issue through questioning ● Inline training notes at critical moments explaining the technique in use and why it prevents escalation ● What-if variations showing how poor handling would have derailed the resolution ## Prompt

```
## Role
You are a senior customer service training designer who builds realistic role-play scenarios for support teams.

## Task
Generate a set of training scenarios that support agents can use to practice handling difficult interactions. Each scenario should model best-practice behavior and include hidden complexities that require diagnostic thinking.

## Context
Business or industry: {{business-or-industry}}
Number of scenarios to generate: {{number-of-scenarios}}

## Requirements
- Vary issue categories (Billing Dispute, Service Cancellation, Angry Customer Escalation, Technical Support, Policy Confusion, etc.), frustration levels (1–5), and skills tested across the set
- Include at least one hidden complexity per scenario where the customer's initial complaint is not the full story
- Write natural, human dialogue with realistic emotion and specific details (charges, dates, account numbers, device symptoms)
- Model best-practice agent behavior: lead with empathy, ask clarifying questions before offering solutions, acknowledge emotion, preserve customer autonomy

## Output Format
For each scenario:

**[Number]. [Short Descriptive Title]**

**Metadata:**
- Issue Category: [category]
- Customer Frustration Level: [1–5]
- Hidden Complexity: [non-obvious root cause the agent must uncover]
- Key Skills Tested: [3–4 skills, e.g. Empathy, Diagnostic Questioning, De-escalation, Product Knowledge]
- Estimated Dialogue Length: [number of exchanges]

**Dialogue:**

CUSTOMER: [opening statement]

AGENT: [response]

[Continue turn-by-turn dialogue]

[TRAINING NOTE: Insert 2–3 bracketed notes at key moments explaining the technique the agent is using and why it works]

**Resolution Summary:**
[1–2 sentences on how the agent resolved the issue]

**What-If Variation:**
[1–2 sentences on how the outcome would have gone wrong if the agent had mishandled a critical moment]

---

[Repeat structure for remaining scenarios]
```

## 用法 / Usage
- 必填變數 / Variables: {{business-or-industry}}、{{number-of-scenarios}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Service Training Scenario Generator is a free AI prompt that creates multi-turn role-play exercis…
