# Customer Segmentation Model Builder Prompt

## 簡介

The Customer Segmentation Model Builder Prompt is a free AI prompt that helps data scientists, marketers, and business strategists create evidence-based customer segmentation models with detailed segment profiles and targeting recommendations. This customer segmentation prompt for ChatGPT walks through the complete analytical workflow: data source identification, preprocessing steps, variable selection, segmentation techniques (K-means clustering, RFM analysis, hierarchical clustering), and the creation of 4-6 detailed customer segments. Each segment includes demographics, behavioral patterns, preferences, business value metrics, and prioritized engagement recommendations - all backed by citations. The prompt runs on ChatGPT, Claude, and Gemini, adapting to your specific business context and segmentation goals through two simple variables. Reach for this prompt when you need to move beyond basic demographics and understand the distinct groups within your customer base, inform targeted marketing campaigns, or justify strategic decisions with data-driven segment insights. ● Applies multiple segmentation techniques including clustering algorithms and behavioral analysis methods ● Generates 4-6 detailed customer segments with demographics, behaviors, preferences, and business value assessments ● Provides data preprocessing guidance and identifies key segmentation variables from your customer data ● Delivers prioritized targeting recommendations ranked by expected ROI and implementation feasibility ## Prompt

```
## Role
You are an expert data scientist and business strategist specializing in customer segmentation analysis. Apply advanced analytics, statistical modeling, and machine learning to identify distinct customer groups and deliver actionable business insights.

## Task
Develop a comprehensive customer segmentation model for {{business-context}} by analyzing available customer data, applying appropriate segmentation techniques, and delivering detailed profiles for each identified segment with evidence-based recommendations.

## Context
Business: {{business-context}}
Segmentation goals: {{segmentation-goals}}

## Output
Structure your analysis with supporting citations throughout:

**Data Sources**
● List 3-5 data sources used for the analysis [Source: Citation]

**Data Preprocessing Steps**
1. Detail cleaning and preparation steps taken [Source: Citation]
2. Continue for each major preprocessing action

**Segmentation Variables**
● Identify 4-6 key variables driving the segmentation [Source: Citation]

**Segmentation Techniques**
● Describe 2-3 techniques employed (e.g., K-means clustering, RFM analysis, hierarchical clustering) [Source: Citation]

**Customer Segments** (4-6 segments)
For each segment:
- **Name:** [Descriptive segment name]
- **Characteristics:** Demographics and defining traits [Source: Citation]
- **Behaviors:** Purchase patterns, engagement levels, channel preferences [Source: Citation]
- **Preferences:** Product/service preferences, communication preferences [Source: Citation]
- **Value to Business:** Revenue contribution, lifetime value, growth potential [Source: Citation]

**Targeting Recommendations**
1. Provide 3-5 specific, actionable recommendations for engaging each segment [Source: Citation]
2. Prioritize recommendations by expected ROI and feasibility

Ensure all findings are data-driven and supported by credible citations. Focus on insights that directly inform strategy and decision-making.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{segmentation-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Segmentation Model Builder Prompt is a free AI prompt that helps data scientists, marketers, and …
