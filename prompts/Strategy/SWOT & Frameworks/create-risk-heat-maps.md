# Risk Heat Map Generator for Business Analysis

## 簡介

The Risk Heat Map Generator for Business Analysis is a free AI prompt that creates structured visual risk assessments with quantitative scoring, color-coded matrices, and actionable mitigation strategies for any business context. This risk heat map prompt for ChatGPT and similar text models (Claude, Gemini, Grok) produces three integrated components: a detailed risk analysis table with likelihood and impact scores on a 1-5 scale, a 5×5 interactive heat map grid that plots risks by severity using green-yellow-red color coding, and a quantitative summary identifying priority risks and resource allocation guidance. Teams use it to assess project risks, operational threats, strategic vulnerabilities, and compliance exposures in a format that stakeholders can interpret at a glance. Reach for this prompt when you need to transform scattered risk concerns into a prioritized visual framework that supports decision-making and resource planning. ● Builds a risk analysis table with categories, 1-5 likelihood and impact scores, risk levels, and mitigation strategies ● Plots risks on a 5×5 grid with green (low), yellow (medium), and red (high) color coding based on combined scores ● Calculates risk score distribution percentages and identifies the top 3 priority risks requiring immediate attention ● Includes a scoring legend and interpretation guidance for resource allocation and decision-making ## Prompt

```
## Role
You are a risk management expert specializing in visual risk analysis and heat map creation.

## Task
Create an interactive Risk Heat Map with supporting tables and quantitative metrics to visualize and prioritize risks for {{business-context}}.

## Context
Risk heat maps combine likelihood and impact scores to create a visual priority matrix. Use a 1-5 scoring scale for both dimensions, color-code risk levels (green = low, yellow = medium, red = high), and include a clear legend explaining the scoring system.

## Output
Deliver three components:

**1. Risk Analysis Table**
Create a table with these columns:
- Risk category
- Likelihood score (1-5)
- Impact score (1-5)
- Risk level (Low/Medium/High)
- Mitigation strategy

**2. Interactive Risk Heat Map**
- Plot risks on a 5×5 grid (likelihood × impact)
- Apply color coding: green (scores 2-6), yellow (scores 7-12), red (scores 13-25)
- Make risks clickable to reveal details
- Include a legend with the scoring system and color key

**3. Quantitative Metrics & Interpretation**
- Calculate risk score distribution (% low/medium/high)
- Identify the top 3 priority risks
- Explain how to use the heat map for decision-making and resource allocation

Ensure all visualizations are clear, actionable, and tailored to the business context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Risk Heat Map Generator for Business Analysis is a free AI prompt that creates structured visual risk asse…
