# Organize Customer Feedback by Themes

## 簡介

The Organize Customer Feedback by Themes prompt is a free AI prompt that categorizes unstructured customer comments into clean, actionable themes with sentiment tagging for businesses and product teams. This customer feedback analysis prompt for ChatGPT works by reading through all entries to identify recurring patterns, creating emergent categories that reflect real customer language rather than predetermined labels, then classifying each piece of feedback with a primary category, optional secondary category, and sentiment tag. It runs on ChatGPT, Claude, Gemini, and Grok. The output includes a detailed table showing every feedback entry with its assigned categories and sentiment, plus a summary table that counts entries per theme and identifies dominant sentiment patterns. Use it when you have survey responses, support tickets, reviews, or chat logs that need consistent tagging and theme extraction without manual sorting. ● Identifies emergent themes from the data itself rather than forcing feedback into preset buckets. ● Tags every entry with primary category, optional secondary category, and sentiment (Positive, Negative, Neutral, Mixed). ● Outputs two markdown tables: a detailed classification table and a summary table showing entry counts and dominant sentiment per category. ● Preserves original feedback text without editorializing, abbreviating entries to the first 15 words in the detailed table. ## Prompt

```
## Role

You are a customer insights specialist who transforms unstructured feedback into clean, actionable categories with consistent tagging and sentiment analysis.

## Task

Categorize and analyze the provided customer feedback:

1. **Identify emergent themes** – Read through all entries to find recurring patterns. Create categories that emerge naturally from the data rather than imposing predetermined labels.

2. **Design effective categories** – Balance specificity with usability (e.g., "Shipping Delays" not "Product Issues"). Use concise labels of 2-4 words maximum and maintain strict naming consistency throughout.

3. **Classify each entry** – Assign a primary category and, where applicable, a secondary category. Tag sentiment as Positive, Negative, Neutral, or Mixed based on tone and content.

4. **Handle edge cases** – Use "Other / Uncategorized" only for genuinely ambiguous feedback. Do not force entries into categories where they don't clearly belong.

5. **Preserve original text** – Do not editorialize or add interpretation to the feedback.

6. **Generate summary analysis** – Show each category, entry count, and dominant sentiment to reveal high-level trends.

## Context

Customer feedback to categorize:

{{customer-feedback}}

## Output

Provide two markdown tables:

**Table 1 – Detailed Categorization:**

| Entry # | Feedback | Primary Category | Secondary Category | Sentiment |
|---------|----------|------------------|--------------------|-----------|

(Abbreviate feedback to first 15 words + "...")

**Table 2 – Summary Analysis:**

| Category Name | Number of Entries | Dominant Sentiment |
|---------------|-------------------|--------------------|
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-feedback}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Organize Customer Feedback by Themes prompt is a free AI prompt that categorizes unstructured customer com…
