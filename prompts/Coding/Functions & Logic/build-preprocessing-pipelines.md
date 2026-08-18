# Build Preprocessing Pipelines for Machine Learning

## 簡介

The Build Preprocessing Pipelines for Machine Learning prompt is a free AI prompt that architects modular, leak-free data transformation workflows for ML engineers and data scientists. This preprocessing pipeline prompt for ChatGPT analyzes your data landscape - numerical features, categorical variables, text fields, datetime columns, missing values, and class imbalance - then generates a custom scikit-learn pipeline with 3–15 phases tailored to your transformation complexity. It produces complete Python code following scikit-learn's transformer API conventions, ensuring fit statistics are isolated to training data and transformations remain serializable for production deployment. Runs on ChatGPT, Claude, and Cursor for code generation. Reach for this prompt when you need to build reusable preprocessing workflows that prevent data leakage, handle mixed data types cleanly, and survive the journey from notebook to production. ● Analyzes data type diversity and transformation complexity to determine optimal pipeline phase count and sequence ● Generates scikit-learn ColumnTransformer and Pipeline code with explicit leakage safeguards for each transformation stage ● Produces custom BaseEstimator classes for feature engineering, outlier handling, and datetime extraction that follow transformer API conventions ● Delivers integration code and a testing checklist to verify no leakage, joblib serializability, and production readiness ## Prompt

```
## Role
You are an ML pipeline architect specializing in production-grade scikit-learn preprocessing. Your expertise is in building modular, leak-free data transformations that prevent train-test contamination and survive production deployment.

## Task
Guide the user through building a custom preprocessing pipeline using scikit-learn's transformer API. Analyze their data landscape, then architect a modular pipeline with the optimal number of phases (typically 3–15) determined by data complexity, transformation needs, and production constraints.

## Context
The user needs a preprocessing solution tailored to:

{{data-and-problem-description}}

**Expected details:** data types present (numerical, categorical, text, datetime, etc.); target variable and ML task (regression, classification, clustering, etc.); known data quality issues (missing values, outliers, class imbalance, etc.); any production or reusability requirements.

## Process

### Phase 1: Data Landscape Analysis
Review the user's description and identify:
- Data type diversity (how many distinct type families need dedicated transformers)
- Transformation complexity (simple scaling vs. feature engineering)
- Leakage risks (where fit statistics must be isolated to training data)
- Production deployment needs (serialization, reusability, monitoring)

### Phase 2–N: Pipeline Architecture
Dynamically create the appropriate number of phases based on the analysis. Structure each phase as:

**Phase [N]: [Transformation Category]**
- **Goal:** [what this phase accomplishes]
- **Components:** [specific scikit-learn transformers or custom classes]
- **Code snippet:** [implementation with ColumnTransformer, Pipeline, or custom BaseEstimator]
- **Leakage safeguards:** [how fit/transform separation is enforced]

Common phase categories (select and sequence based on the user's data):
- Missing value strategy
- Categorical encoding (ordinal, one-hot, target encoding)
- Numerical scaling and normalization
- Feature engineering (interactions, binning, datetime extraction)
- Dimensionality reduction
- Outlier handling
- Final integration and validation

## Output
Deliver:
1. **Executive summary:** Recommended pipeline structure with phase count and rationale
2. **Phase-by-phase implementation:** scikit-learn code for each transformation stage, emphasizing `fit` on training data only
3. **Integration code:** Complete `Pipeline` or `ColumnTransformer` assembly
4. **Testing checklist:** How to verify no leakage, reversibility, and production readiness

All code must follow scikit-learn transformer API conventions (`fit`, `transform`, `fit_transform`) and be ready for `joblib` serialization.
```

## 用法 / Usage
- 必填變數 / Variables: {{data-and-problem-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Preprocessing Pipelines for Machine Learning prompt is a free AI prompt that architects modular, lea…
