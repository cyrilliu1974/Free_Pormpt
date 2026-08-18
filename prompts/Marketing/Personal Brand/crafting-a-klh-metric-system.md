# KLH Marketing Metrics Framework Generator

## 簡介

The KLH Marketing Metrics Framework Generator is a free AI prompt that builds a complete performance measurement system for marketers and business owners who need to track what matters. This marketing metrics prompt for ChatGPT guides the model to produce a three-tier table of Key metrics (success indicators), Leading metrics (predictive signals), and Health metrics (safeguards against broken processes). You provide a business overview, and the prompt returns 2–4 metrics per category with impact explanations and industry-specific numeric benchmarks. It runs on ChatGPT, Claude, and Gemini, making it easy to generate a data-driven measurement framework in minutes. Real use cases include setting up dashboards for SaaS startups, aligning team KPIs for e-commerce brands, and auditing existing analytics for service businesses. Reach for this prompt when you need clarity on which metrics to monitor, when spreadsheets feel overwhelming, or when you want benchmarks grounded in your industry and growth stage. ● Outputs a four-column table with Metric Type, Marketing Metric, Impact on Marketing, and Industry Benchmark. ● Focuses on simple-to-calculate metrics that generate actionable insights, not vanity numbers. ● Tailors Key, Leading, and Health metrics to your specific business stage, niche, and operations. ● Includes specific numeric benchmarks aligned with industry standards, so you know where you stand. ## Prompt

```
## Role
You are an expert digital marketer specializing in performance measurement and metric selection.

## Task
Generate a complete marketing metrics system using the KLH Framework (Key, Leading, Health metrics) tailored to the business described below.

## Context
**KLH Framework:**
- **Key metrics:** Most important metrics showing whether the product is successful
- **Leading metrics:** Metrics that predict how key metrics will change in the future
- **Health metrics:** Metrics showing whether experiments or operations have broken anything

**Business information:**
{{business-overview}}

## Requirements
- Include 2-4 metrics for each type (Key, Leading, Health)
- Focus on metrics that are simple to calculate and track
- Each metric must generate actionable marketing insights
- Provide a specific numeric benchmark for each metric, aligned with the business stage and industry—do not describe the benchmark, give the number

## Output
Return a table with exactly four columns:

| Metric Type | Marketing Metric | Impact on Marketing | Industry Benchmark |
|-------------|------------------|---------------------|--------------------|
| Key | ... | ... | ... |
| Leading | ... | ... | ... |
| Health | ... | ... | ... |
```

## 用法 / Usage
- 必填變數 / Variables: {{business-overview}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The KLH Marketing Metrics Framework Generator is a free AI prompt that builds a complete performance measureme…
