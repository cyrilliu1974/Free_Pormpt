# Brand Positioning Map Generator for ChatGPT

## 簡介

The Brand Positioning Map Generator is a free AI prompt that builds a structured competitive positioning analysis for product managers, marketers, and brand strategists. This brand positioning prompt for ChatGPT analyzes your competitive landscape, identifies unique differentiators, defines your target market by demographics and psychographics, and distills your brand essence into a clear statement. It outputs a markdown table mapping Competition, Differentiators, Target Market, and Brand Essence, followed by strategic analysis covering market entry implications, messaging recommendations, and competitive advantage. Use it when launching a new product, repositioning an existing brand, or clarifying your market differentiation against named competitors. The prompt runs on ChatGPT, Claude, and Gemini. ● Maps your product against named competitors to reveal white-space opportunities and differentiation gaps ● Defines target market using demographic, psychographic, and behavioral lenses for precision segmentation ● Articulates brand essence as a concise statement that captures core identity and guides messaging ● Provides strategic analysis explaining implications for market entry, competitive advantage, and communication strategy ## Prompt

```
## Role
You are an expert brand strategist creating a brand positioning map.

## Task
Identify the unique value proposition and target market for the specified product or service. Deliver a structured positioning map that clarifies competitive differentiation and market position.

## Context
**Product/Service:** {{product-service}}
**Industry:** {{industry}}
**Main Competitors:** {{competitors}}
**Target Audience:** {{target-audience}}

Analyze the competitive landscape to identify where key players position themselves. Determine the unique differentiators that set this offering apart. Define the target market by considering demographics, psychographics, and behavioral characteristics. Distill the brand essence into a concise statement that captures core identity.

## Output
Present your analysis as a markdown table with 4 columns:

| Competition | Differentiators | Target Market | Brand Essence |
|-------------|-----------------|---------------|---------------|

Below the table, provide a brief strategic analysis explaining the implications of this positioning map for market entry, messaging, and competitive advantage.
```

## 用法 / Usage
- 必填變數 / Variables: {{competitors}}、{{industry}}、{{product-service}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Brand Positioning Map Generator is a free AI prompt that builds a structured competitive positioning analy…
