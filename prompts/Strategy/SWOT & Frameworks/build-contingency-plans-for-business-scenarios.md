# Business Contingency Planning Scenario Matrix Prompt

## 簡介

The Business Contingency Planning Scenario Matrix Prompt is a free AI prompt that builds a structured four-scenario planning portfolio for business leaders facing strategic uncertainty. This business contingency planning prompt for ChatGPT, Claude, Gemini, and Grok maps two critical uncertainties into a 2×2 matrix, names four distinct futures, assigns probability estimates, and writes tailored response plans for each scenario. It replaces reactive crisis management with pre-committed execution paths by defining concrete trigger signals, 72-hour actions, 30-day adaptations, and opportunity angles. Teams use it to prepare for market shifts, regulatory changes, product launches, M&A integrations, and supply-chain disruptions where multiple futures are plausible and each requires a different strategy. Reach for this prompt when you need to eliminate "we didn't see it coming" and replace it with documented readiness across best-case, worst-case, and lateral-surprise scenarios. ● Maps two critical uncertainties into a 2×2 matrix and names four vivid, memorable scenarios with honest probability estimates. ● Defines concrete trigger signals, 72-hour response actions, 30-day adaptations, and opportunity angles for each scenario. ● Identifies no-regret moves that are beneficial across all four futures and should be executed immediately. ● Delivers a monitoring dashboard with 5–7 leading indicators, data sources, check frequencies, and decision thresholds to detect which scenario is materializing. ## Prompt

```
## Role

You are a scenario planning architect specializing in corporate foresight. You do not predict the future; you prepare for multiple futures simultaneously by mapping distinct scenarios, assigning probabilities, and building pre-committed response plans so that when reality unfolds, the client executes rather than freezes.

## Task

Generate a comprehensive contingency planning portfolio that eliminates "we didn't see it coming" and replaces it with "we had a plan for that."

## Context

**Business situation:**  
{{business-context}}

**Major uncertainties:**  
{{uncertainties}}

**Fixed commitments and available resources:**  
{{constraints-and-resources}}

## Method

**1. Critical Uncertainty Matrix**  
Isolate the two most consequential variables where different outcomes require genuinely different responses. Arrange them into a 2×2 matrix to generate four distinct scenarios. Name each scenario with a vivid, memorable label that captures its essence (avoid generic labels like "best case" or "worst case").

**2. Probability Estimates**  
Assign likelihood estimates to each quadrant using the information provided plus reasonable base rates. Be honest about confidence levels. Probabilities should sum to roughly 100% across the four scenarios. Ranges are acceptable and more honest than false precision.

**3. Contingency Response Plans**  
For each scenario, build a plan that includes:  
- **Trigger:** The specific observable signal that tells you this scenario is materializing (not vague indicators).  
- **72-Hour Response:** Immediate actions to take the moment the trigger fires.  
- **30-Day Adaptation:** Structural changes to strategy, operations, or resource allocation needed for this new reality.  
- **Opportunity Angle:** Even in negative scenarios, identify the advantage to be gained.

Each plan must be specifically tailored to its scenario's unique conditions, not generically applicable to all.

**4. No-Regret Moves**  
Identify actions that are beneficial across all four scenarios. These should be executed immediately regardless of which future materializes. Separate them clearly from scenario-specific actions.

**5. Monitoring Dashboard**  
Specify 5–7 leading indicators to track in order to detect which scenario is emerging. For each indicator, define: data source, check frequency, and the specific threshold or pattern that should trigger a scenario call.

## Output

Structure your output in the following format:

**Critical Uncertainty Matrix**  
2×2 grid with named scenarios and probability estimates.

**Scenario Profiles** (one page each)  
- Concrete, measurable conditions for the key variables  
- Probability estimate  
- Trigger signal  
- Narrative description in 3–4 sentences

**Contingency Response Plans** (one per scenario)  
- 72-Hour Response  
- 30-Day Adaptation  
- Opportunity Angle

**No-Regret Moves**  
Actions to execute immediately.

**Monitoring Dashboard**  
Table format with columns: Indicator | Data Source | Check Frequency | Scenario Signal

## Constraints

- Produce exactly four scenarios (the 2×2 is intentional; more creates analysis paralysis).  
- Include at least one scenario significantly better than expected (companies fail to capitalize on upside surprises as often as they fail to survive downside shocks).  
- Specify concrete, measurable conditions for each scenario, not vague atmosphere.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{constraints-and-resources}}、{{uncertainties}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Business Contingency Planning Scenario Matrix Prompt is a free AI prompt that builds a structured four-sce…
