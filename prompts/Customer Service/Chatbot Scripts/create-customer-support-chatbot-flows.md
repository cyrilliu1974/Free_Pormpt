# Customer Support Chatbot Flow Designer

## 簡介

The Customer Support Chatbot Flow Designer is a free AI prompt that creates structured conversation flows, escalation logic, and performance frameworks for businesses building customer service chatbots. This chatbot flow prompt for ChatGPT, Claude, and Gemini produces decision-tree conversation maps covering order tracking, returns, and product inquiries, complete with emotional acknowledgment patterns, handoff triggers, and brand-aligned response templates. It walks you through FAQ taxonomy, dialogue variations, escalation conditions, tone guardrails, sample conversations, and metrics tracking so your chatbot knows when to solve and when to escalate. Use it when launching a new support bot, reducing ticket volume, or improving self-service rates without sacrificing customer trust. ● Builds hierarchical FAQ structures that anticipate customer needs before the first message. ● Generates decision-tree flows with emotion-first responses under 50 words, multiple resolution paths, and fallback handling. ● Defines precise escalation triggers for emotional distress, multi-issue cases, high-value accounts, and compliance concerns. ● Delivers tone guidelines with do/don't examples, sample end-to-end conversations, and a six-metric performance dashboard. ## Prompt

```
## Role

You are a customer experience architect specializing in conversational AI design. You understand conversation psychology, emotional de-escalation, and when automation should defer to human judgment.

## Task

Design comprehensive chatbot conversation flows covering order tracking, returns, and product queries. The flows must maintain a professional yet warm tone, provide clear resolution paths, and identify precisely when to escalate to human agents.

## Context

Business and customer profile:
{{business-context}}

Top support issues and current performance:
{{support-landscape}}

Brand voice and tone:
{{brand-voice}}

## Output

Deliver the chatbot system design in this structure:

**1. FAQ Category Structure**  
Hierarchical taxonomy anticipating customer needs before they ask.

**2. Conversation Flows**  
Decision-tree format for each major support area (order tracking, returns, product queries) showing:  
- Customer input variations  
- Bot responses that acknowledge emotion first, then provide actionable information  
- Clear next steps and alternative paths  
- Responses under 50 words each  

**3. Escalation Triggers**  
Specific conditions requiring human handoff:  
- Emotional distress indicators (language patterns, repeated frustration)  
- Multi-issue complexity  
- High-value accounts  
- Legal, safety, or compliance concerns  

**4. Tone Guidelines**  
Dos and don'ts with examples demonstrating your brand voice while avoiding corporate jargon and robotic phrasing.

**5. Sample Conversations**  
Complete dialogue examples for each primary flow showing natural interaction.

**6. Performance Metrics**  
Dashboard framework tracking resolution rate, escalation frequency, conversation length, customer satisfaction, and self-service success.

**Design Principles:**  
- Acknowledge emotion before delivering information  
- Provide multiple resolution paths  
- Make escalation feel like service elevation, not abandonment  
- Prevent circular conversation loops  
- Include fallback responses for edge cases  
- Balance efficiency with accuracy
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-voice}}、{{business-context}}、{{support-landscape}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Support Chatbot Flow Designer is a free AI prompt that creates structured conversation flows, esc…
