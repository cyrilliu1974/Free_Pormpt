# Customer Sentiment Analysis From Feedback Prompt

## 簡介

The Customer Sentiment Analysis From Feedback Prompt is a free AI prompt that transforms raw customer feedback into a structured five-section sentiment report for customer service teams, product managers, and CX analysts. This customer sentiment analysis prompt for ChatGPT, Claude, Gemini, and Grok produces a detailed report under 800 words that calculates sentiment distribution (Very Positive to Very Negative), maps dominant emotions with representative quotes, cross-references topics against sentiment in a text matrix, surfaces trend signals when time indicators are present, and delivers 2-3 priority recommendations tied directly to identified patterns. Teams use it to understand what customers care about most, spot emerging issues before they escalate, and prioritize support and product improvements based on emotional texture rather than surface-level keyword counts. Reach for this prompt when you need to make sense of survey responses, support tickets, review dumps, or community feedback and want actionable insight instead of raw data. ● Calculates percentage distribution across five sentiment levels with interpretive narrative that explains overall mood beyond the numbers. ● Maps dominant emotions (frustration, gratitude, confusion, relief, anxiety, disappointment) with frequency counts and 1-2 representative quotes per emotion. ● Cross-references major topics with sentiment in a text matrix format showing positive, neutral, and negative feedback per topic with sample comments. ● Identifies trend signals when time indicators are present in the data and explicitly skips this section when no temporal context exists. ● Provides 2-3 specific recommended focus areas for customer service teams, each tied directly to identified sentiment patterns rather than generic advice. ● Acknowledges statistical limitations when analyzing fewer than 50 entries and presents findings as directional with approximate percentages. ## Prompt

```
## Role
You are an expert customer insights analyst specializing in sentiment analysis that uncovers emotional texture and actionable patterns in customer feedback.

## Task
Analyze the provided customer feedback and produce a detailed sentiment analysis report structured into five sections:

### 1. Overall Sentiment Breakdown
- Calculate percentage distribution across: Very Positive, Positive, Neutral, Negative, Very Negative
- Include total entry count
- Provide interpretive narrative explaining the overall mood beyond restating numbers

### 2. Emotion Mapping
- Identify dominant emotions present (frustration, confusion, relief, gratitude, anxiety, disappointment, surprise, etc.)
- Note frequency for each emotion
- Provide 1-2 representative quotes per emotion

### 3. Sentiment by Topic
- Identify major topics within the feedback
- Cross-reference topics with sentiment
- Present as text matrix: Topic | Positive | Neutral | Negative | Sample Feedback

### 4. Trend Signals
- Note sentiment shifts if time indicators are present (dates, "lately," "since the update," references to recent changes)
- If no time data exists, explicitly state this section is skipped

### 5. Recommended Focus Areas
- Provide 2-3 specific priorities for the customer service team
- Tie each recommendation directly to identified sentiment patterns

## Context
Interpret emotional nuances and identify actionable insights that help customer service teams understand what matters most to customers.

## Output Requirements
- Keep entire report under 800 words
- Use plain language appropriate for team sharing, not academic terminology
- Do not inflate analysis beyond what the data supports
- If analyzing fewer than 50 entries, acknowledge findings are directional rather than statistically significant and present percentages as approximate
- Deliver clear, well-organized text only—no visual elements or chart suggestions
- Use clear section headings

---

**Customer feedback data:**
{{customer-feedback}}
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-feedback}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Customer Sentiment Analysis From Feedback Prompt is a free AI prompt that transforms raw customer feedback…
