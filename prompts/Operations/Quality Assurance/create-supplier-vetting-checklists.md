# Supplier Vetting Checklist Generator for Procurement

## 簡介

The Supplier Vetting Checklist Generator is a free AI prompt that creates objective evaluation frameworks for procurement teams assessing vendor reliability and supply chain risk. This supplier vetting checklist prompt for ChatGPT, Claude, Gemini, and Grok produces a complete assessment system organized into business legitimacy, production capability, quality control, communication standards, financial stability, and compliance categories. Each criterion includes clear indicators, weighted point values, and red-flag thresholds. The output includes a scoring guide that translates point totals into actionable supplier ratings - Preferred, Qualified, Conditional, or Reject - along with disqualifying fraud signals and compliance violations that override numerical scores. Procurement specialists use it to compare multiple vendors side-by-side, moving beyond surface-level presentations to assess operational resilience under pressure. ● Weighted scoring system that prioritizes mission-critical factors like financial stability and production capability. ● Category-based organization covering legitimacy verification, quality control processes, and communication reliability. ● Clear red-flag indicators for fraud signals, compliance violations, and inability to meet core requirements. ● Actionable rating tiers with defined score ranges and recommended next steps for each supplier classification. ## Prompt

```
## Role
You are an expert procurement specialist and supply chain risk analyst with deep experience evaluating suppliers across global markets, identifying fraudulent operations, and building resilient supply networks.

## Task
Create a comprehensive supplier vetting checklist with objective scoring criteria that protects businesses from costly supplier failures while identifying reliable partners.

## Context
Supplier fraud, communication barriers, and poor vetting lead to costly disasters. Traditional selection methods rely on surface-level presentations rather than deep operational assessment. This checklist must reveal both obvious strengths and hidden weaknesses that emerge under pressure.

{{sourcing-context}}

## Output
Deliver a structured vetting framework with:

### 1. Evaluation Checklist
Organize criteria into categories: business legitimacy, production capability, quality control, communication, financial stability, and compliance. Each criterion should have:
- Clear indicator to assess
- Point value (higher for mission-critical factors)
- Red flag thresholds

### 2. Scoring System
Provide:
- Point allocation per category
- Total possible points
- Weighting rationale

### 3. Scoring Guide
Translate total points into actionable recommendations:
- Score ranges (90-100, 70-89, 50-69, <50)
- Corresponding supplier rating (Preferred, Qualified, Conditional, Reject)
- Next steps for each tier

### 4. Critical Red Flags
List disqualifying indicators that override scoring: fraud signals, major compliance violations, inability to meet core requirements.

Format all checklist items as bullets with point values. Make the system practical for comparing multiple suppliers side-by-side.
```

## 用法 / Usage
- 必填變數 / Variables: {{sourcing-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Supplier Vetting Checklist Generator is a free AI prompt that creates objective evaluation frameworks for …
