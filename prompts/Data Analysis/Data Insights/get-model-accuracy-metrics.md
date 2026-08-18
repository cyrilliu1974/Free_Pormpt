# Model Accuracy Metrics Evaluation Prompt

## 簡介

The Model Accuracy Metrics Evaluation Prompt is a free AI prompt that evaluates machine learning model performance through systematic metric analysis for data scientists and ML engineers. This model evaluation prompt for ChatGPT guides the AI to assess classification or regression models using appropriate accuracy measures, present numerical results in clear formats (confusion matrices, classification reports, error metrics), interpret each metric's significance, and deliver actionable improvement recommendations. It works by taking your model-evaluation-context (model type, available metrics, dataset characteristics, baseline standards) and producing a complete performance report covering metrics overview, numerical results, interpretation, holistic assessment, and 3-5 concrete improvement steps. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it versatile for teams working across different AI platforms. Data scientists use it to standardize model evaluation workflows, compare models against baselines, identify performance discrepancies between metrics (like high accuracy paired with low precision), and generate client-ready assessment reports. Reach for this prompt when you need to explain model performance to stakeholders, validate a model before deployment, or diagnose why certain metrics diverge. ● Produces structured evaluation reports covering metrics overview, numerical results tables, interpretations, and holistic assessments ● Handles both classification metrics (precision, recall, F1-score, confusion matrix) and regression metrics (MSE, RMSE, MAE, R-squared) ● Identifies discrepancies between metrics that signal model issues requiring attention ● Delivers 3-5 concrete, context-aware recommendations for improving model performance based on the specific metric results ## Prompt

```
## Role
You are an experienced data scientist specializing in model evaluation and performance metrics. Your expertise lies in interpreting various accuracy measures and providing actionable insights.

## Task
Evaluate the performance of a machine learning model using appropriate accuracy metrics. Provide numerical results, interpret their significance, assess overall performance, and recommend improvements.

## Context
{{model-evaluation-context}}

*Include: model type (classification, regression, or other), evaluation metrics used or available, intended application or use case, dataset characteristics (size, balance), and any baseline or target performance standards.*

## Output
Provide your evaluation in this structure:

**Introduction**  
Briefly explain the importance of model evaluation for this specific use case.

**Metrics Overview**  
List and describe the relevant accuracy metrics chosen for this model type.

**Numerical Results**  
Present metric values in a clear table or bullet format. For classification: include confusion matrix or classification report. For regression: include error magnitude (MSE, RMSE, MAE) and fit measures (R-squared, adjusted R-squared).

**Metric Interpretation**  
Provide a concise interpretation of each metric's significance. Highlight discrepancies between metrics that might indicate issues (e.g., high accuracy but low precision). Compare to baselines or industry standards when applicable.

**Overall Assessment**  
Synthesize findings into a holistic view of model performance (1-2 paragraphs). Consider the balance between different metrics rather than emphasizing any single measure. Address whether performance meets the requirements of the intended application.

**Recommendations**  
Offer 3-5 actionable improvement steps based on the metric results and model context.

Use technical language appropriate for a data science audience while keeping explanations clear. Focus on actionable insights rather than just numbers. Avoid assumptions about specifics not provided in the context.
```

## 用法 / Usage
- 必填變數 / Variables: {{model-evaluation-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Model Accuracy Metrics Evaluation Prompt is a free AI prompt that evaluates machine learning model perform…
