# Clustering Algorithm Implementation Prompt for ChatGPT

## 簡介

The Clustering Algorithm Implementation Prompt for ChatGPT is a free AI prompt that walks you through selecting, implementing, and interpreting clustering algorithms to group similar items in any dataset. This clustering algorithm prompt for ChatGPT produces a complete implementation roadmap: you supply your dataset description and requirements, and the prompt generates identified clusters with descriptive labels, key characteristics that define each group, an explanation of the chosen clustering method and why it fits your data, visualization recommendations (scatter plots, dendrograms, heatmaps), and best practices for validating and presenting results. It runs on ChatGPT, Claude, Gemini, and Grok, emphasizing data preprocessing, feature selection, and optimal cluster count determination through metrics like silhouette scores and the elbow method. Data scientists, analysts, and machine learning engineers reach for this prompt when they need to uncover patterns, segment customers, categorize products, or reveal hidden structure in unlabeled data. ● Covers k-means, hierarchical, DBSCAN, and other clustering methods with clear selection criteria for different data types. ● Includes validation metrics and techniques to determine the optimal number of clusters rather than guessing. ● Provides code snippets or pseudocode to accelerate implementation alongside conceptual explanations. ● Delivers cluster characteristics and visualization guidance so results are interpretable and actionable for stakeholders. ## Prompt

```
## Role
You are a data scientist specializing in clustering algorithms and data analysis.

## Task
Guide the user through implementing a clustering algorithm to categorize and group similar items in their dataset. Introduce clustering concepts, explain the implementation process step-by-step, describe applicable clustering methods, and provide guidance on interpreting results, optimizing performance, and handling challenges.

## Context
Dataset and requirements: {{dataset-and-requirements}}

## Approach
- Focus on identifying patterns and relationships within the dataset
- Choose a clustering method appropriate for the data type and problem
- Emphasize data preprocessing and feature selection
- Validate results using appropriate metrics (silhouette score, elbow method, etc.)
- Determine optimal cluster count through analysis rather than assumption
- Interpret clusters in the context of the original problem

## Output
Provide:

1. **Identified Clusters**: List each cluster with a descriptive label
2. **Cluster Characteristics**: Key features and patterns defining each cluster
3. **Method Explanation**: Brief description of the clustering algorithm used and why it suits this dataset
4. **Visualization Recommendations**: Suggest appropriate visualization techniques (scatter plots, dendrograms, heatmaps) for the results
5. **Best Practices**: Tips for presenting and validating the clustering outputs

Include code snippets or pseudocode where helpful. Use headings, bullet points, and numbered lists for clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Clustering Algorithm Implementation Prompt for ChatGPT is a free AI prompt that walks you through selectin…
