# Student Success Prediction Model Prompt

## 簡介

The Student Success Prediction Model Prompt is a free AI prompt that helps educational institutions develop data-driven frameworks to identify students at risk of academic failure and design targeted intervention strategies. This student success prediction prompt for ChatGPT guides you through systematic analysis: evaluating available data sources, prioritizing risk factors by predictive strength, and matching intervention strategies to your institution's actual resources and capacity. It runs on ChatGPT, Claude, and Gemini, producing a structured markdown table that maps each data source to specific risk factors and corresponding evidence-based interventions. Use it when planning early-warning systems, designing retention programs, or building academic support frameworks grounded in your institution's real constraints and student population characteristics. ● Evaluates institutional data sources and identifies predictive features for academic risk ● Prioritizes risk factors based on evidence and detection feasibility ● Designs intervention strategies matched to available resources and capacity constraints ● Produces a coherent three-column table mapping data sources, risk factors, and actionable responses ## Prompt

```
## Role
You are an expert data scientist and educational analyst specializing in academic risk assessment and student success modeling.

## Task
Develop a predictive model framework that identifies students at risk of academic failure. Analyze data sources to determine key risk factors and propose evidence-based intervention strategies tailored to the institution's capacity and student population.

## Context
{{institutional-context}}

Work systematically through:
1. Data source evaluation and feature identification
2. Risk factor prioritization based on predictive strength
3. Intervention strategy design matched to available resources and capacity
4. Coherent mapping between data indicators, risks, and actionable responses

## Output
Provide your analysis as a markdown table with three columns: **Data Sources** | **Risk Factors** | **Intervention Strategies**

Each row must represent a coherent relationship where:
- The data source enables detection of
- The specific risk factor, which is addressed by
- The proposed intervention strategy

Ensure interventions are realistic given the stated resource and capacity constraints.
```

## 用法 / Usage
- 必填變數 / Variables: {{institutional-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Student Success Prediction Model Prompt is a free AI prompt that helps educational institutions develop da…
