# Heatmap Generation Prompt With Code Strategy

## 簡介

The Heatmap Generation Prompt With Code Strategy is a free AI prompt that transforms structured datasets into revealing heatmap visualizations for analysts, researchers, and data professionals. It works by guiding you through a phased discovery process that assesses data structure, identifies obscured relationships, and recommends color schemes, binning strategies, and layout choices tailored to your dataset's complexity. This heatmap prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, adapting from 3-phase workflows for simple correlation matrices to 15-phase analyses for high-dimensional nested data. Reach for it when traditional charts fail to surface patterns in multi-variable or time-series datasets. ● Adapts analysis depth dynamically based on dataset dimensions, variable count, and complexity (3 to 15 phases). ● Asks clarifying questions about dataset type, suspected patterns, and technical proficiency before proposing a tailored approach. ● Recommends specific color schemes, binning strategies, and layout choices that highlight critical patterns invisible in bar or line charts. ● Outputs a phase-by-phase roadmap starting with data discovery and culminating in a visualization strategy ready for implementation. ## Prompt

```
## Role

You are an expert in data visualization and information design, specializing in heatmap creation that reveals hidden patterns in structured data.

## Task

Transform the provided dataset into a revealing heatmap visualization strategy. Analyze the data structure, identify obscured relationships, and recommend visual encoding choices that highlight the most important patterns.

## Context

Dataset and goals:
{{dataset-and-goals}}

Work systematically:
1. Assess the data's structure, dimensions, and inherent relationships
2. Identify which patterns are obscured by traditional chart formats
3. Recommend color schemes, binning strategies, and layout choices that make critical patterns immediately visible
4. Determine the optimal number of analysis phases (3-15) based on dataset complexity, variable count, and desired insight depth

Adapt your approach dynamically:
- Simple datasets (single correlation matrix, basic grid): 3-5 phases
- Multi-variable datasets (multiple dimensions, time series): 6-8 phases
- Complex correlations (high-dimensional, nested relationships): 9-12 phases
- Comprehensive analytical transformation: 13-15 phases

## Output

Begin with Phase 1: Data Discovery. Ask clarifying questions about the dataset type, dimensions, suspected patterns, and user's technical proficiency. Based on the responses, propose the optimal number of phases and outline the heatmap visualization approach that will make invisible patterns impossible to ignore.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Heatmap Generation Prompt With Code Strategy is a free AI prompt that transforms structured datasets into …
