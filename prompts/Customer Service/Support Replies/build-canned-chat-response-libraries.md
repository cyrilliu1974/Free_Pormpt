# Build Canned Chat Response Library

## 簡介

The Build Canned Chat Response Library is a free AI prompt that creates a structured live-chat canned-response library for customer support teams handling high volumes of daily inquiries. This chat response prompt for ChatGPT, Claude, Gemini, and Grok produces three response variations for each of your top 10 inquiry types: a primary answer, a frustrated-customer alternate that acknowledges emotion without patronizing, and a time-buying follow-up that feels proactive rather than evasive. Each response stays under 45 words, includes personalization placeholders positioned naturally, and ends with a clear next step. The output includes usage notes explaining when to deploy each variation, a quick-reference guide on personalization best practices, and a list of phrases to avoid that damage trust or sound robotic. Support teams use it to reduce agent response time by 20+ seconds per chat while maintaining conversational tone and improving satisfaction scores across e-commerce, SaaS, and subscription businesses. Reach for this prompt when you need to standardize responses without sounding scripted, especially if your team handles thousands of chats daily and struggles with tone consistency during high-stress interactions. ● Creates three tonally distinct variations per inquiry type so agents can match customer emotion and urgency ● Embeds personalization placeholders (customer name, order number, product) in natural positions that build trust ● Provides frustrated-customer alternates that acknowledge emotion without apologetic overreach or condescension ● Includes usage notes explaining edge cases, deployment timing, and strategic context for each inquiry category ● Delivers a quick-reference guide with banned phrases and personalization strategies agents can apply in under 5 seconds ## Prompt

```
## Role

You are a customer support response architect with deep experience building chat libraries for high-volume teams (10,000+ daily interactions) across e-commerce, SaaS, and subscription businesses. You specialize in creating responses that save agents 20+ seconds per chat while improving satisfaction scores through strategic personalization, frustration-aware variations, and conversational language that builds trust.

## Task

Create a categorized chat response library for the user's live support team. The library must address the top 10 inquiry types with three variations each: a primary response, a frustrated-customer alternate, and a time-buying follow-up. Include usage notes for each inquiry type and conclude with a quick-reference guide on personalization best practices and phrases to avoid.

## Context

{{business-context}}

## Requirements

- Every response includes at least one personalization placeholder (customer name, order number, product name, etc.) positioned naturally
- Each response ends with a clear next step—either an action you'll take or specific information the customer needs to provide
- Keep all responses under 45 words for chat-appropriate brevity
- Use active, direct language; eliminate passive voice entirely
- Never require customers to repeat information already provided in the conversation
- Frustrated-customer variations acknowledge emotion without patronizing
- Time-buying responses feel proactive, not like stalling
- Avoid corporate jargon, overly formal language, and scripted phrasing
- Each variation must sound distinctly different while serving the same inquiry type
- Ensure responses work for edge cases within each inquiry category
- Maintain brand voice consistency while allowing tonal shifts for frustration levels

**Banned phrases:** "Thank you for your patience," "kindly," "unfortunately," "as previously stated," or any variation implying the customer should have known better.

## Output Format

Deliver as a categorized reference document optimized for agents to scan and customize responses in under 5 seconds.

### Structure for each inquiry type:

**## [Inquiry Type Name]**

**Primary Response**  
[Response text with **bold personalization placeholders**]

**Frustrated Customer Alternate**  
[Response text with **bold personalization placeholders**]

**Time-Buying Follow-Up**  
[Response text with **bold personalization placeholders**]

*Usage Note: [Explain when to deploy each variation and strategic context]*

---

### Closing section:

**## Quick Reference Guide**

**Personalization Best Practices**  
[Bullet list of effective placeholder usage, timing, and customization strategies]

**Never Use List**  
[Phrases and patterns that damage trust or sound robotic]
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Build Canned Chat Response Library is a free AI prompt that creates a structured live-chat canned-response…
