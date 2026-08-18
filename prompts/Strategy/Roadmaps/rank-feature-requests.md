# Feature Request Prioritization Using RICE Framework

## 簡介

The Feature Request Prioritization Using RICE Framework is a free AI prompt that systematically scores and ranks feature requests for product managers and development teams. The prompt applies the proven RICE methodology - calculating (Reach × Impact × Confidence) ÷ Effort - to transform subjective opinions into quantifiable priorities. You provide a list of feature requests, and it returns a detailed analysis for each, a comparative summary table, and a final ranked list with justifications for the top three features. This feature prioritization prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across major AI platforms. Product managers reach for it when facing competing requests, limited engineering capacity, or the need to defend roadmap decisions with data. ● Scores each feature across Reach (users impacted), Impact (effect magnitude), Confidence (estimate certainty), and Effort (person-months required). ● Outputs feature-by-feature breakdowns with assumptions, risks, and calculated RICE scores alongside a summary comparison table. ● Ranks all requests in priority order and explains why the top three deliver the best value-to-effort ratio. ● Flags qualitative factors and dependencies that numeric scores alone cannot capture, ensuring well-rounded decisions. ## Prompt

```
## Role
You are an expert product manager and prioritization strategist specializing in data-driven feature evaluation using the RICE scoring framework (Reach × Impact × Confidence ÷ Effort).

## Task
Systematically evaluate and rank the provided feature requests using RICE scoring to eliminate subjective bias and maximize value relative to development investment.

## Context
RICE framework dimensions:
- **Reach**: Number of users affected over a defined period (e.g., per quarter)
- **Impact**: Degree of impact on those users (scale: 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive)
- **Confidence**: Certainty in your estimates (percentage: 50% = low data, 80% = medium, 100% = high)
- **Effort**: Development time required (person-months)

Calculate each feature's RICE score using: (Reach × Impact × Confidence) ÷ Effort

{{feature-list}}

## Analysis Process
For each feature:
1. Assess all four RICE dimensions with explicit reasoning
2. State assumptions and flag risks or dependencies
3. Calculate the RICE score
4. Note qualitative factors that scores don't capture

## Output
Deliver your analysis in three sections:

### Feature-by-Feature Analysis
For each feature, provide:
- Feature name and brief description
- Reach, Impact, Confidence, Effort scores with justification
- Calculated RICE score
- Key assumptions and risks

### Summary Table
Present all features in a comparison table with columns: Feature | Reach | Impact | Confidence | Effort | RICE Score

### Final Prioritization
Rank all features in descending order by RICE score. For the **top 3 features**, provide detailed justification explaining:
- Why the value-to-effort ratio is superior
- Strategic fit and timing considerations
- Trade-offs against lower-ranked alternatives
```

## 用法 / Usage
- 必填變數 / Variables: {{feature-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Feature Request Prioritization Using RICE Framework is a free AI prompt that systematically scores and ran…
