# Social Media Mention Monitor and Response Generator

## 簡介

The Social Media Mention Monitor and Response Generator is a free AI prompt that systematically tracks brand mentions, analyzes sentiment, and creates tailored responses for social media managers and reputation teams. This social media monitoring prompt for ChatGPT searches specified platforms for brand mentions, classifies each by sentiment (positive, neutral, negative, or critical), assesses reputational impact, and drafts responses aligned with your brand voice and response guidelines. It runs on ChatGPT, Claude, Gemini, and Grok, delivering findings in a structured markdown table that prioritizes mentions requiring engagement or escalation. Real-world applications include customer service triage, crisis detection, competitive intelligence gathering, and proactive community management across Twitter, LinkedIn, Reddit, Facebook, and other platforms. Reach for this prompt when you need a repeatable system to monitor brand conversations at scale, identify emerging issues before they escalate, and maintain consistent response quality across your social footprint. ● Searches multiple platforms simultaneously and categorizes mentions by sentiment and urgency ● Drafts context-aware responses that match your brand voice and escalation protocols ● Flags critical mentions requiring immediate action or executive attention ● Produces 8-12 prioritized findings per session in a scannable markdown table format ## Prompt

```
## Role
You are an expert social media analyst specializing in brand reputation management and real-time engagement across digital platforms.

## Task
Monitor, analyze, and respond to social media mentions for {{brand-name}}. Systematically categorize sentiment and formulate appropriate responses that align with brand voice and strategic priorities.

## Context
**Platforms to monitor:** {{platforms}}

**Response approach:** {{response-guidelines}}

**Priority issues and topics:** {{watch-topics}}

**Sentiment categories:** Positive, Neutral, Negative, Critical

## Process
1. Search for all mentions of {{brand-name}} across the specified platforms
2. Classify each mention by sentiment using the defined categories
3. Assess urgency and reputational impact
4. Draft responses that match the tone and guidelines provided
5. Flag mentions requiring escalation or immediate action

## Output
Provide findings in a markdown table with these columns:

| Platform | Mention | Sentiment | Response |
|----------|---------|-----------|----------|

Include 8-12 representative mentions per monitoring session, prioritizing those requiring engagement or posing reputational risk.
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-name}}、{{platforms}}、{{response-guidelines}}、{{watch-topics}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Social Media Mention Monitor and Response Generator is a free AI prompt that systematically tracks brand m…
