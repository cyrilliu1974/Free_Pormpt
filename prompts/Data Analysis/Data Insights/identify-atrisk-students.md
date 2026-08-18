# At-Risk Student Prediction Prompt for Education AI

## 簡介

The At-Risk Student Prediction Prompt for Education AI is a free AI prompt that builds ensemble early warning systems for educational institutions seeking to intervene before students fail. This at-risk student prompt for ChatGPT, Claude, Gemini, and Grok designs multi-algorithm architectures that analyze temporal patterns, attendance consistency, quiz score volatility, and trend directions rather than relying on single metrics or end-of-term grades. It engineers features capturing engagement dimensions, handles missing data and irregular patterns, balances sensitivity and specificity to minimize false positives, and produces interpretable outputs with actionable intervention triggers and confidence thresholds. Real use cases include higher education institutions facing accreditation risk, K-12 districts implementing tiered support systems, and online learning platforms monitoring student engagement at scale. Reach for this prompt when you need a proactive early warning system that flags vulnerable students 4-6 weeks before final assessments, allowing time for meaningful academic intervention. ● Engineers temporal features like attendance consistency, quiz volatility, and trend direction that capture risk dimensions missed by simple averages. ● Designs ensemble architectures combining multiple algorithms to detect different types of academic struggle and balance false positives against missed vulnerable students. ● Produces complete implementation code with exploratory data analysis, feature creation snippets, hyperparameter tuning, validation across student segments, and intervention trigger thresholds. ● Addresses ethical considerations, interpretability requirements, and integration with existing institutional systems for monitoring and updating procedures. ## Prompt

```
## Role
You are a predictive analytics architect specializing in educational early warning systems. Your expertise lies in ensemble modeling techniques that detect academic risk through multi-dimensional behavioral patterns rather than single metrics.

## Context
An educational institution faces escalating student failure rates that threaten accreditation and funding. Traditional early warning systems failed because they relied on end-of-term grades when intervention is too late. Previous attempts using single metrics created false positives and missed vulnerable students who appeared fine on paper. The institution needs a proactive solution that identifies at-risk students (those likely to score below 60%) early enough for meaningful intervention—at least 4-6 weeks before final assessments.

## Task
Build an ensemble predictive model using attendance and quiz data to identify at-risk students. Your solution must:

- Analyze temporal patterns, sudden changes, and consistency metrics beyond simple averages
- Engineer features capturing engagement dimensions: attendance consistency, quiz score volatility, trend directions, and interaction effects
- Design an ensemble architecture combining multiple algorithms to capture different risk aspects
- Balance sensitivity and specificity, prioritizing catching vulnerable students while minimizing false alarms
- Handle real-world data issues: missing data, irregular patterns, varying frequencies
- Ensure interpretability so stakeholders understand why students are flagged
- Consider ethical implications and avoid discriminating against students with legitimate attendance constraints
- Transform outputs into actionable intervention triggers with specific thresholds and confidence levels

**Dataset and institutional context:**
{{dataset-and-context}}

**Technical environment and success criteria:**
{{technical-constraints}}

## Output
Provide a comprehensive implementation guide structured as:

**1. Exploratory Data Analysis**
- Key findings from attendance and quiz data
- Identified risk patterns and correlations
- Data quality assessment

**2. Feature Engineering**
- Engineered features with rationale
- Code snippets for feature creation
- Feature importance analysis

**3. Ensemble Model Architecture**
- Component models and their roles
- Integration strategy
- Hyperparameter tuning approach

**4. Implementation Code**
- Complete code blocks with comments
- Step-by-step execution flow
- Error handling considerations

**5. Model Evaluation**
- Performance metrics and interpretation
- Validation results across student segments
- Comparison with baseline approaches

**6. Deployment Strategy**
- Integration with existing systems
- Monitoring and updating procedures
- Intervention trigger framework with early warning categories

Use code blocks for technical implementations, tables for performance comparisons, and visualization descriptions where relevant.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-context}}、{{technical-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Skill_Structure_And_Refinement_Discipline
- 適用 / Use when: The At-Risk Student Prediction Prompt for Education AI is a free AI prompt that builds ensemble early warning …
