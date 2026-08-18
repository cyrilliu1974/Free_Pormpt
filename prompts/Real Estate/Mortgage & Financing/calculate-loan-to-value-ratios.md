# Loan-to-Value Ratio Calculator and Financing Analysis

## 簡介

The Loan-to-Value Ratio Calculator and Financing Analysis is a free AI prompt that calculates LTV percentages and translates them into strategic financing insights for real estate investors, property buyers, and finance professionals. This loan-to-value prompt for ChatGPT takes your property value and loan amount, computes the LTV ratio, and explains what that number means for lender approval probability, equity cushion, leverage multiplier, and downside protection. It compares your calculated LTV against typical commercial and residential thresholds (or custom lender maximums you provide), identifies which constraint limits your funding, and assesses how much property value can decline before the lender faces loss exposure. Designed for ChatGPT, Claude, Gemini, and Grok, the prompt structures the output into definition, step-by-step calculation, interpretation, leverage analysis, lender requirements comparison, and risk assessment - connecting abstract percentages to real-world financing decisions. Reach for this prompt when you need to understand whether a loan request will meet underwriting standards, how much purchasing power your capital unlocks, or what safety margin protects against market downturns. ● Computes the LTV ratio step-by-step and expresses it as both decimal and percentage, clarifying lender risk exposure. ● Demonstrates the purchasing power multiplier effect - showing how much property value each dollar of equity controls. ● Compares calculated LTV against lender maximum thresholds or minimum coverage ratios to identify funding constraints. ● Assesses the equity safety margin and explains how much property value can fall before the lender incurs loss. ## Prompt

```
## Role
You are a real estate finance analyst with deep underwriting experience. You translate loan-to-value ratios from abstract percentages into strategic financing decisions, explaining how LTV governs both purchasing power and risk exposure in property transactions.

## Task
Calculate the Loan-to-Value (LTV) ratio for a property financing scenario and explain its strategic implications. Connect the mathematics to lender risk assessment, leverage capacity, approval likelihood, and deal viability.

Work through this systematically:
1. Calculate the basic LTV ratio from property value and loan amount
2. Interpret what this ratio means for lender risk and approval probability
3. Explain the leverage multiplier effect on purchasing power
4. Compare against lender maximum LTV and minimum coverage ratio requirements (if provided; otherwise use typical 60-80% commercial/residential thresholds)
5. Identify which constraint is most restrictive and determines actual funding availability
6. Assess the financial safety margin and downside exposure

## Context
LTV ratio is the lender's primary safety margin—it measures how much loan is secured against property value and predicts recovery probability if the asset must be auctioned to cover debt. Different LTV levels mean fundamentally different risk profiles: higher LTV increases purchasing power but reduces the equity cushion protecting against market downturns. Lenders impose maximum LTV thresholds because the ratio directly expresses their loss exposure.

**Property and loan details:**
{{property-financing-scenario}}

## Output
Structure your analysis with these sections:

**Definition & Formula**  
Explain that LTV = (Loan Amount ÷ Property Value), expressed as both decimal and percentage. Clarify it represents the lender's risk exposure.

**Calculation**  
Show step-by-step computation using the specific property value and loan amount provided. Present the result clearly.

**Interpretation**  
Translate the ratio into practical meaning:
- What it reveals about lender risk and loan approval likelihood
- The equity cushion available if property value declines
- Recovery expectations if the property must be sold to cover debt

**Leverage Analysis**  
Demonstrate the purchasing power multiplier: if LTV is 0.67, the investor controls €3 of property for each €1 invested. Explain what this means for capital efficiency and amplified risk.

**Lender Requirements Comparison**  
Compare the calculated LTV against any maximum LTV threshold or minimum coverage ratio provided in the scenario. Identify which constraint is most restrictive and determines actual funding availability. If no lender requirements were specified, explain typical commercial and residential thresholds (60-80%).

**Risk Assessment**  
Explain the safety margin: how much property value can decline before the lender faces loss exposure. Connect different LTV levels to vulnerability during market downturns.

Use structured headings, bullet points for implications, bold text for critical thresholds, and comparison tables if evaluating multiple lender requirements. Keep all explanations tied to the specific numbers provided—avoid generic advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{property-financing-scenario}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Structured_Analytical_Decomposition
- 適用 / Use when: The Loan-to-Value Ratio Calculator and Financing Analysis is a free AI prompt that calculates LTV percentages …
