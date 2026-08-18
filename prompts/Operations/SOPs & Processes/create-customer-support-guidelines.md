# Customer Support Guidelines Generator for AI

## 簡介

The Customer Support Guidelines Generator is a free AI prompt that creates complete, structured customer support documentation for businesses and service teams. This customer support prompt for ChatGPT takes a single product or service description and produces a full guidelines document covering communication channels, inquiry and complaint handling processes, escalation procedures, common scenario walkthroughs, and performance metrics. The output includes step-by-step instructions for support representatives, concrete examples for typical customer interactions, and frameworks for continuous improvement. It runs on ChatGPT, Claude, Gemini, and Grok, delivering plain-language documentation that support teams can adopt immediately. Use it when onboarding new support staff, standardizing response protocols across teams, or documenting best practices for customer service operations. ● Produces guidelines covering inquiry handling, complaint resolution, escalation triggers, and common customer scenarios ● Includes communication channel protocols, SLA targets, and performance metrics for tracking team effectiveness ● Delivers step-by-step procedures written for support representatives, not end customers ● Structures output with product overview, general guidelines, scenario walkthroughs, and continuous improvement practices ## Prompt

```
## Role

You write customer support guidelines. Given a product or service description, you produce a complete, structured guide that support representatives can follow day-to-day.

## Context

Product or service: {{product-service}}

## Task

Produce a customer support guidelines document covering all sections below. Write for support representatives, not customers. Keep language plain and direct. Include step-by-step instructions, escalation procedures, and concrete examples for common scenarios.

## Output

### Product/Service Overview
Brief description of the product/service and its key features.

### Communication Channels
- Email support
- Live chat
- Phone support
- Social media
- Help center / ticketing system

### General Guidelines
1. Respond within established SLA timeframes
2. Use professional, empathetic tone
3. Personalize responses with customer name
4. Document all interactions in CRM
5. Follow security protocols for account verification

### Inquiry Handling Process
1. Acknowledge receipt promptly
2. Verify customer identity and gather context
3. Research issue using internal knowledge base
4. Provide clear, actionable solution
5. Confirm resolution and offer additional help

### Complaint Handling Process
1. Listen actively without interrupting
2. Acknowledge the issue and apologize for inconvenience
3. Take ownership and explain next steps
4. Implement solution or escalate if needed
5. Follow up to ensure satisfaction

### Escalation Procedure
1. Identify escalation triggers: technical complexity, policy exceptions, legal threats, VIP customers
2. Document full interaction history and attempted resolutions
3. Route to appropriate tier-2 specialist or team lead
4. Notify customer of escalation with expected timeline

### Common Scenarios

**Scenario 1: Account Access Issues**
- Description: Customer cannot log in due to forgotten password or locked account
- Solution: Guide through password reset process; verify identity via security questions; unlock account after verification; document attempt patterns

**Scenario 2: Billing Discrepancies**
- Description: Customer disputes charge or reports incorrect amount
- Solution: Pull transaction history; explain charge breakdown; process refund if error confirmed; escalate if dispute remains unresolved

**Scenario 3: Feature Requests**
- Description: Customer asks for functionality not currently available
- Solution: Acknowledge request positively; explain current capabilities and workarounds; log feature request in product feedback system; provide timeline if roadmap allows

### Performance Metrics
- First response time (target: under 2 hours)
- Resolution time (target: 80% within 24 hours)
- Customer satisfaction score (CSAT target: 4.5+/5)
- Ticket reopening rate (target: below 5%)
- Escalation rate

### Continuous Improvement
1. Review support tickets weekly to identify patterns and knowledge gaps
2. Update internal documentation based on new issues or solutions
3. Participate in team training sessions and share learnings from complex cases
```

## 用法 / Usage
- 必填變數 / Variables: {{product-service}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Customer Support Guidelines Generator is a free AI prompt that creates complete, structured customer suppo…
