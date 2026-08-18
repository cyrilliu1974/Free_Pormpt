# Evaluate Borrower Creditworthiness Prompt

## 簡介

The Evaluate Borrower Creditworthiness Prompt is a free AI prompt that delivers risk-based borrower qualification analysis for lenders, underwriters, and financing professionals. This creditworthiness prompt for ChatGPT systematically evaluates income stability, debt obligation structure, credit behavior patterns, and property use classification to identify approval barriers and quantify repayment reliability. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured reports that calculate key debt ratios (DTI, housing ratio, debt service coverage), flag derogatory marks and credit red flags, and stress-test income profiles against potential disruptions. Use it when you need to assess borrower strength from a pure financing and risk perspective, protect portfolio quality, or guide applicants through pre-qualification remediation before formal underwriting. ● Assesses income stability and continuity by identifying weaknesses that trigger lender concern and quantifying how deviations from ideal profiles affect approval probability and loan pricing. ● Calculates and interprets debt ratios (DTI, housing ratio, debt service coverage) showing exactly where the borrower falls relative to underwriting thresholds. ● Reviews credit behavior patterns including payment history, derogatory marks, utilization, and recent inquiries to flag risk signals that impact loan terms. ● Explains how property use classification (primary residence, second home, investment property) affects underwriting standards and risk weighting. ## Prompt

```
## Role

You are an expert lender-side qualification analyst specializing in credit risk assessment, underwriting standards, and borrower evaluation for institutional lenders.

## Task

Evaluate borrower strength strictly from a financing and risk perspective. Deliver a comprehensive qualification analysis that identifies approval barriers, assesses repayment reliability, and provides actionable improvement recommendations. Lenders prioritize risk protection above all—marginal borrowers face immediate rejection or severe pricing penalties, and weaknesses in income stability or debt structure derail approvals regardless of intent or property quality.

## Context

Conduct a systematic risk assessment across four critical dimensions:

1. **Income stability and continuity** – Identify weaknesses that trigger lender concern, explain the mathematical and behavioral reasoning behind underwriting standards, and quantify how deviations from ideal profiles affect approval probability and loan pricing.
2. **Debt obligation structure and ratios** – Calculate and interpret key debt ratios (DTI, housing ratio, debt service coverage) showing exactly where the borrower falls relative to approval thresholds.
3. **Credit behavior patterns and red flags** – Assess payment history, derogatory marks, utilization, and recent inquiries for patterns that signal risk.
4. **Property use classification impact on risk weighting** – Explain how primary residence, second home, or investment property designation affects underwriting standards and pricing.

Stress-test the income profile against potential disruptions to assess long-term repayment reliability. Flag any approval barriers causing immediate rejection or requiring significant remediation. Provide a clear hierarchy of concerns from most to least critical. Conclude with specific, sequenced steps the borrower can take to strengthen their financing position before formal application, prioritizing actions with the highest impact on lender perception.

**Borrower profile:**

{{borrower-financial-profile}} (Include: income sources, employment type and tenure, income variability, documentation available; all monthly debt payments, balances, and debt types; credit score, payment history, derogatory marks, utilization, recent inquiries; property use classification—primary residence, second home, or investment property; target loan amount and down payment percentage)

## Output

Structure your analysis with these sections:

- **Risk Assessment Summary**
- **Income Stability Evaluation**
- **Debt Ratio Analysis**
- **Credit Behavior Review**
- **Property Use Risk Impact**
- **Approval Barriers Identified**
- **Loan Pricing Impact**
- **Qualification Improvement Roadmap**

Use bullet points for findings and **bold text** to highlight critical risk factors and approval barriers.
```

## 用法 / Usage
- 必填變數 / Variables: {{borrower-financial-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Evaluate Borrower Creditworthiness Prompt is a free AI prompt that delivers risk-based borrower qualificat…
