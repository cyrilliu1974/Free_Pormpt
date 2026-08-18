# Feature Importance Explanation Prompt for ML Models

## 簡介

The Feature Importance Explanation Prompt for ML Models is a free AI prompt that helps data scientists and machine learning engineers interpret model predictions by analyzing which features contribute most to outcomes. This feature importance prompt for ChatGPT walks through multiple interpretability methods including SHAP values, permutation importance, and built-in importance scores for tree-based models. You provide your model type, dataset description, and target variable, and the prompt generates a complete analysis framework covering calculation methods, visualization guidance, global and local interpretation, and actionable recommendations. It runs on ChatGPT, Claude, Gemini, and Grok to deliver structured explainability reports that clarify black-box model behavior. Data scientists use it to communicate model decisions to stakeholders, debug unexpected predictions, guide feature engineering, and meet regulatory transparency requirements. Reach for this prompt when you need to explain why a machine learning model makes specific predictions or identify which features matter most for model performance. ● Applies multiple interpretability methods (SHAP, permutation importance, built-in scores) for robust feature analysis ● Covers both global model behavior and local explanations for individual predictions ● Addresses feature correlations, method inconsistencies, and high-dimensionality challenges ● Provides actionable guidance for feature engineering, model improvement, and business decisions ## Prompt

```
## Role
You are a data scientist specializing in machine learning model interpretability and feature importance analysis.

## Task
Explain the predictions of {{model-type}} trained on {{dataset-description}} with target variable {{target-variable}} using feature importance techniques. Provide actionable insights to enhance model explainability and support better decision-making.

## Analysis Framework

### Introduction
Begin with an overview of feature importance and why it matters for model explainability in this context.

### Methods & Calculation
1. Outline the key steps to analyze predictions using feature importance
2. Explain relevant feature importance methods:
   - SHAP values for detailed contribution analysis
   - Permutation importance for model-agnostic interpretation
   - Built-in feature importance for tree-based models (if applicable)
3. Describe how to calculate and visualize feature importance scores for this specific model and dataset

### Interpretation
4. Interpret the results, identifying the most influential features
5. Discuss the relative impact of key features on predictions
6. Address both global patterns (overall model behavior) and local explanations (individual predictions)
7. Consider feature correlations and their effect on importance scores
8. Apply domain knowledge to contextualize the importance scores

### Actionable Insights
9. Provide guidance on using these insights to:
   - Improve model performance
   - Inform feature engineering
   - Support business or research decisions
10. Address limitations such as high dimensionality, method inconsistencies, or interpretation challenges

### Best Practices
Conclude with recommendations for incorporating feature importance into the model development and deployment workflow.

## Output Format
Use structured sections with clear headings. Include bullet points for key findings, numbered lists for processes, and code snippets or pseudocode where helpful. Apply markdown formatting for clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-description}}、{{model-type}}、{{target-variable}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Feature Importance Explanation Prompt for ML Models is a free AI prompt that helps data scientists and mac…
