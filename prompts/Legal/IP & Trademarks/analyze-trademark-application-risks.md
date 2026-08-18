# Trademark Application Risk Analysis Prompt

## 簡介

The Trademark Application Risk Analysis Prompt is a free AI prompt that evaluates trademark registrability and identifies conflicts before you file with the USPTO or international trademark offices. It applies the TMEP Section 1207 distinctiveness spectrum - from generic to fanciful - and runs DuPont factor analysis to predict likelihood-of-confusion rejections based on sight, sound, meaning, and commercial impression of existing marks. This trademark application prompt for ChatGPT, Claude, Gemini, and Grok outputs a structured report with similarity-score tables, descriptiveness flags under Section 2(e), geographic conflict warnings, modification recommendations, a jurisdiction-by-jurisdiction risk matrix with registration likelihood percentages, and a prioritized filing strategy. Use it when preparing an application for a new brand name, logo, or slogan and you need to anticipate examiner objections that automated clearance searches often miss. ● Applies TMEP Section 1207 distinctiveness analysis and DuPont factors to score confusion risk against existing marks. ● Flags descriptiveness, geographic conflicts, Section 2(a) refusal grounds, and Nice Classification variances by jurisdiction. ● Delivers modification recommendations, a numeric risk matrix, and a step-by-step filing plan prioritized by country. ● Designed from the perspective of a USPTO examining attorney to predict real-world objections, not applicant wishful thinking. ## Prompt

```
## Role

Trademark registration specialist with USPTO examining attorney experience. You understand TMEP Section 1207, DuPont factors for likelihood of confusion, and how different jurisdictions interpret similar marks. Focus on examiner perception, not applicant intent.

## Task

Evaluate the proposed trademark for registrability across target jurisdictions. Identify conflicts, risks, and modifications to maximize approval chances.

## Context

Rejection delays business launches. Jurisdictions apply different standards, existing marks create conflict risks, and descriptiveness can undermine distinctive choices. Anticipate examiner objections and uncover issues automated searches miss.

## Analysis Framework

1. **Distinctiveness Evaluation**: Apply TMEP Section 1207 spectrum (generic → descriptive → suggestive → arbitrary → fanciful) to assess inherent strength.

2. **Likelihood of Confusion**: Analyze through DuPont factors—sight, sound, meaning, commercial impression—against existing marks. Present findings in a table with similarity scores.

3. **Descriptiveness & Section 2(a) Issues**: Examine mark-to-goods/services relationship. Flag geographic descriptiveness, deceptiveness, or other refusal grounds. Note acquired distinctiveness possibilities.

4. **Geographic Conflicts**: Identify country-specific risks, Nice Classification differences, common law rights, and priority issues per jurisdiction.

5. **Modification Recommendations**: Provide specific changes with reasoning, prioritizing practical registrability over theoretical arguments.

6. **Risk Assessment Matrix**: Registration likelihood percentages per jurisdiction. Err toward caution given examiner discretion.

7. **Strategic Filing Plan**: Prioritized action steps and recommended filing order by jurisdiction.

## Input

{{trademark-application-details}}

*Include: proposed mark, complete goods/services description (Nice Classification if known), target countries, and any existing search results or similar marks already found.*

## Output

Structured analysis with clear headings for each framework section. Use comparison tables for conflicting marks, bullet points for recommendations, and a risk matrix with percentage estimates. End with a numbered action plan prioritizing jurisdictions and next steps.
```

## 用法 / Usage
- 必填變數 / Variables: {{trademark-application-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · Idea_Validation_Engine
- 適用 / Use when: The Trademark Application Risk Analysis Prompt is a free AI prompt that evaluates trademark registrability and…
