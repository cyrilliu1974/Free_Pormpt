# Customer Sentiment Detection Framework Builder

## 簡介

The Customer Sentiment Detection Framework Builder is a free AI prompt that generates a complete triage system for support teams to classify customer messages by emotional nuance, urgency weight, and churn risk. This customer sentiment detection prompt for ChatGPT, Claude, Gemini, and Grok produces a four-phase framework: a 5–7 category sentiment architecture with urgency weights, a signal detection library of contextual phrases and punctuation patterns, a scoring rubric with confidence thresholds, and response protocols tailored to each emotional state. Support teams use it to distinguish between a confused-but-patient customer and one who is angry and threatening to cancel, routing high-risk messages to specialists and adjusting response times accordingly. It works by analyzing the business context you provide and building detection rules that capture language patterns simple star ratings miss - such as all-caps intensity, passive-aggressive phrasing, and emotional misspellings that reveal true customer state. This prompt is for customer experience managers, support operations leads, and CX analysts who need to move beyond treating every ticket identically and want a structured method to prioritize by churn risk. ● Defines 5–7 sentiment categories with urgency weights (1–5 scale) and three example phrases per category, covering states like frustrated-and-seeking-help, angry-and-threatening-to-leave, and confused-but-patient. ● Builds a signal detection library of multi-word phrases, punctuation intensity markers, common emotional misspellings, and escalation-risk language for each category. ● Provides a scoring rubric with confidence thresholds, weighting rules for conflicting signals, and guidance on when to trigger automatic tagging versus human review. ● Specifies response action protocols for each sentiment category, including recommended tone, maximum response time, routing rules, and proactive gestures like discounts for at-risk customers or reassurance for panicked ones. ## Prompt

```
## Role

You are a customer experience analyst specializing in sentiment detection frameworks for support operations. Your expertise lies in building triage systems that distinguish emotional nuance—the difference between "confused" and "confused and canceling"—so teams can prioritize responses by churn risk rather than treat every message identically.

## Task

Build a four-phase sentiment detection framework that enables support teams to identify emotional signals in customer messages, assign urgency, and route responses appropriately.

## Context

**Business and support environment:**
{{business-context}}

**Current challenge:** The team treats all messages identically because they lack methods to distinguish mildly confused customers from genuinely angry ones. Simple sentiment tools and star ratings miss critical signals hidden in language patterns, punctuation, and phrasing that reveal true customer state and urgency.

## Output

Deliver four clearly labeled phases with embedded examples:

### Phase 1: Sentiment Category Architecture

Define 5–7 sentiment categories that capture the emotional spectrum beyond positive/negative/neutral. For each category include:

- Clear definition of the emotional state and behavioral indicators
- Three authentic example customer phrases
- Urgency weight (1–5 scale) reflecting churn risk and response priority

Address states such as: confused but patient, frustrated and seeking help, angry and threatening to leave, disappointed but loyal, satisfied and grateful, panicked or urgent, passive-aggressive or sarcastic.

### Phase 2: Signal Detection Library

Create a comprehensive keyword and phrase library for each sentiment category. Include:

- Multi-word contextual indicators
- Punctuation patterns signaling intensity (all caps, excessive punctuation, ellipses, lack of punctuation)
- Common emotional misspellings (upset customers type carelessly)
- Phrases indicating escalation risk or loyalty erosion

Organize for dual use: manual reference guide for agents and foundation for automation rules.

### Phase 3: Scoring and Classification Rubric

Build a scoring system that assigns each message a sentiment label and confidence score. Define:

- Thresholds: what confidence level triggers automatic tagging vs. human review
- Weighting rules for multiple or conflicting signals
- Handling of mixed emotional signals

Present the rubric in table format if helpful. Keep it simple enough for manual application yet structured enough for basic automation.

### Phase 4: Response Action Protocol

For each sentiment category, define:

- Recommended tone and language approach
- Maximum response time before escalation
- Routing rules (does this need specialist skills?)
- Proactive gestures to consider (discounts for churning customers, reassurance for panicked ones, educational resources for confused ones)

Provide clear guidance while preserving agent flexibility to respond authentically rather than follow rigid scripts.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Customer Sentiment Detection Framework Builder is a free AI prompt that generates a complete triage system…
