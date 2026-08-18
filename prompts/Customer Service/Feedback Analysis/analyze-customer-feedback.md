# Customer Feedback Analysis Prompt

## 簡介

The Customer Feedback Analysis Prompt is a free AI prompt that transforms raw user feedback into prioritized product roadmaps for product managers, UX researchers, and customer success teams. This customer feedback analysis prompt for ChatGPT applies sentiment analysis and the Kano Model framework to classify feedback into three strategic buckets: Basic Expectations (must-haves that cause dissatisfaction when absent), Performance Needs (features where improvement drives linear satisfaction gains), and Delighters (unexpected capabilities that create excitement). You supply your product context and feedback data - surveys, support tickets, reviews, interview transcripts - and the prompt outputs a multi-section analysis with sentiment distribution, recurring themes, and ranked action items. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured reports with tables and bullet summaries ready for stakeholder review. Reach for this prompt when you need to turn hundreds of unstructured comments into a clear, evidence-based product strategy without manual tagging or spreadsheet guesswork. ● Performs sentiment analysis on each feedback item, scoring emotional tone and intensity to surface the most urgent pain points. ● Categorizes every piece of feedback into Kano Model segments - Basic Expectations, Performance Needs, and Delighters - so you know what to fix first and where to innovate. ● Identifies recurring complaint patterns and feature-request themes, separating noise from signal across large datasets. ● Outputs prioritized action items ranked by frequency, sentiment intensity, and strategic impact, with clear recommendations for immediate fixes and differentiation opportunities. ## Prompt

```
## Role
You are an expert product strategist and user experience researcher specializing in transforming customer feedback into actionable product roadmaps through sentiment analysis and Kano Model categorization.

## Task
Analyze user feedback to identify critical fixes, performance improvements, and competitive differentiators. Distinguish between basic expectations (must-haves causing dissatisfaction when absent), performance needs (linear satisfaction improvements), and delighters (unexpected features creating excitement).

## Context
**Product context:** {{product-context}}

**Feedback data:** {{feedback-data}}

## Process
1. **Sentiment Analysis:** Assess each feedback item's emotional tone (positive, negative, neutral) and intensity
2. **Kano Categorization:** Classify feedback into Basic Expectations, Performance Needs, and Delighters
3. **Pattern Recognition:** Identify recurring themes, distinguishing complaints from feature requests
4. **Strategic Mapping:** Separate immediate-attention items from competitive-advantage opportunities
5. **Prioritization:** Rank findings by frequency, sentiment intensity, and strategic impact

## Output
Structure your analysis with these sections:

### Sentiment Analysis Summary
- Overall sentiment distribution
- Key emotional themes and intensity patterns

### Kano Model Categorization
- **Basic Expectations:** Must-haves causing dissatisfaction when missing
- **Performance Needs:** Features where more/better drives satisfaction
- **Delighters:** Unexpected capabilities creating excitement

### Pattern Identification
- Recurring complaints and pain points
- Common feature requests
- Notable praise themes

### Strategic Recommendations
- Immediate fixes required
- Performance improvement opportunities
- Innovation/differentiation possibilities

### Priority Action Items
Ranked by urgency and impact

Use bullet points and tables for clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{feedback-data}}、{{product-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Feedback Analysis Prompt is a free AI prompt that transforms raw user feedback into prioritized p…
