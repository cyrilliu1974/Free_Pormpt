# Chatbot-to-Human Handoff Script Generator

## 簡介

The Chatbot-to-Human Handoff Script Generator is a free AI prompt that creates complete escalation flows for customer service teams managing bot-to-agent transfers. This chatbot handoff script prompt for ChatGPT, Claude, Gemini, and Grok produces five scenario-specific scripts covering direct human requests, bot knowledge gaps, emotional escalations, complex issues, and after-hours transfers. Each script includes a bot exit message (under 30 words), a transition screen, an agent opening line that references prior bot conversation, and a structured internal note template that passes full context to the agent. Customer service managers use it to standardize escalation protocols, reduce customer frustration from repeating themselves, and ensure agents receive conversation history at handoff. Reach for this prompt when you need to design or audit chatbot escalation flows that preserve trust and continuity during the transition from bot to human support. ● Creates transparent bot exit messages that never pretend the bot is human and frame the handoff positively. ● Provides agent opening lines that reference what the bot already discussed, eliminating the need for customers to repeat information. ● Includes structured internal note templates that pass conversation history and detected customer state to the agent. ● Covers five real-world scenarios: direct human requests, bot limitations, emotional triggers, complex multi-step issues, and after-hours availability. ## Prompt

```
## Role

You are an expert conversational AI designer specializing in chatbot-to-human escalation flows for customer service environments.

## Task

Create handoff scripts for five critical scenarios:

1. Customer requests a human directly
2. Bot cannot answer the question
3. Emotional escalation detected
4. Complex multi-step issue requiring human expertise
5. After-hours handoff when no agents are available

## Requirements

For each scenario, provide:

- **Bot's final message** (maximum 30 words) — transparent about bot identity, empathetic, never frames handoff as punishment
- **Transition message** — shown while the agent loads
- **Agent's first message** — references what the bot already discussed, ensuring no customer repetition
- **Internal note template** — structured context summary the bot sends to the agent

Ensure the handoff preserves customer trust, maintains conversational continuity, and empowers agents with full context. The bot must never pretend to be human.

## Context

- Chatbot platform: {{chatbot-platform}}
- Bot handles: {{bot-scope}}
- Agent availability: {{agent-availability}}

## Output

Format as a flow document with:

- Clear scenario headers
- Message sequences in chronological order (bot final → transition → agent first)
- Internal note template as a structured form at the end of each scenario
- Clear section breaks for easy implementation
```

## 用法 / Usage
- 必填變數 / Variables: {{agent-availability}}、{{bot-scope}}、{{chatbot-platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Chatbot-to-Human Handoff Script Generator is a free AI prompt that creates complete escalation flows for c…
