# Standards Alignment Analysis Prompt for Curriculum

## 簡介

The Standards Alignment Analysis Prompt for Curriculum is a free AI prompt that evaluates how effectively educational curricula address specific standards and generates concrete recommendations for instructional designers and educators. This standards alignment prompt for ChatGPT systematically assesses your curriculum against any set of educational standards - state frameworks, Common Core, NGSS, or institution-specific benchmarks. It identifies strengths, pinpoints gaps, and proposes practical improvements covering teaching methods, resource integration, and assessment strategies. The output is a clean markdown table with three columns: Standard, Current Alignment, and Suggestions. Educators use it when developing new courses, auditing existing programs for accreditation, or ensuring compliance with district or national standards. The prompt runs on ChatGPT, Claude, Gemini, and Grok. ● Evaluates each standard individually, detailing current strengths and gaps in curriculum coverage ● Provides specific, practical suggestions for teaching methods, materials, and assessments that improve alignment ● Outputs results in a markdown table format for easy sharing with stakeholders and incorporation into planning documents ● Adapts to any educational context - K-12, higher education, corporate training, or professional development ## Prompt

```
## Role
You are an expert curriculum analyst specializing in standards alignment and instructional design.

## Task
Analyze the provided curriculum against the specified educational standards and deliver actionable recommendations to strengthen alignment. Systematically assess how well each standard is currently addressed, identify gaps, and propose concrete improvements incorporating teaching methods, resources, and assessment strategies.

## Context
Educational standards: {{educational-standards}}

Curriculum details: {{curriculum-details}}

Educational context: {{educational-context}}

## Output
Present your analysis as a markdown table with three columns:

| Standard | Current Alignment | Suggestions |
|----------|------------------|-------------|

Each row should cover one standard with:
- **Standard**: The specific standard being evaluated
- **Current Alignment**: How well the curriculum currently addresses this standard (strengths and gaps)
- **Suggestions**: Specific, practical improvements to enhance alignment

Ensure each evaluation is comprehensive yet concise.
```

## 用法 / Usage
- 必填變數 / Variables: {{curriculum-details}}、{{educational-context}}、{{educational-standards}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Standards Alignment Analysis Prompt for Curriculum is a free AI prompt that evaluates how effectively educ…
