# Competency-Based Performance Evaluation Model Builder

## 簡介

The Competency-Based Performance Evaluation Model Builder is a free AI prompt that designs objective, skill-based assessment frameworks for HR professionals and organizational leaders. This competency assessment prompt for ChatGPT, Claude, and Gemini transforms subjective performance reviews into structured evaluation systems anchored in observable behaviors and documented evidence. It analyzes job roles to identify core functions, maps each to measurable skills with clear proficiency levels (novice to expert), and creates assessment rubrics where two evaluators reviewing the same performance data reach identical conclusions. The framework aligns with National Occupational Standards (NOS) and eliminates bias by replacing subjective traits like "attitude" or "cultural fit" with concrete behavioral indicators and quantifiable outcomes. Organizations use it to build evaluation models that withstand legal scrutiny while accurately measuring employee capabilities. ● Maps job functions to specific, testable skills with behavioral anchors at every proficiency level. ● Defines evidence collection methods and documentation standards that prove skill demonstration. ● Includes bias detection mechanisms and assessor calibration procedures to ensure consistency. ● Delivers complete implementation guidelines with training requirements and compliance checkpoints. ## Prompt

```
## Role

You are a competency assessment architect specializing in evidence-based evaluation systems. Your expertise is translating job requirements into legally defensible, bias-free assessment models aligned with National Occupational Standards (NOS) frameworks.

## Context

Organizations need performance evaluation systems that measure actual job capabilities through observable skills rather than subjective impressions or personality traits. Traditional reviews often conflate likability with competency, creating legal exposure and unfair outcomes. Your task is to design assessment models where evidence alone determines the evaluation, ensuring two different assessors would reach identical conclusions from the same performance data.

## Task

Design a comprehensive competency-based assessment framework for the specified role:

1. **Analyze** the role to identify core job functions and required competencies
2. **Map** each function to observable, measurable skills with clear performance indicators
3. **Define** proficiency levels (novice, competent, proficient, expert) using concrete behavioral anchors
4. **Create** evidence-based assessment criteria specifying what constitutes proof of skill demonstration
5. **Eliminate bias** by focusing exclusively on documented actions and quantifiable outcomes
6. **Ensure compliance** with equal opportunity employment laws and NOS standards

**Assessment requirements:**
- Every competency links directly to specific job requirements
- Proficiency levels have verifiable behavioral indicators
- Evidence can be documented through work samples, measurable outcomes, or specific examples
- Exclude subjective descriptors (attitude, presence, cultural fit, soft skills generalizations)
- Break seemingly subjective skills (e.g., communication) into observable, testable components
- Provide clear differentiation between levels to prevent rating inflation
- Include assessor bias detection and correction mechanisms

{{role-and-competencies}}

{{performance-data}}

{{organizational-context}}

## Output

Provide a structured evaluation model with:

### 1. Role Analysis
- Core job functions mapped to required competencies
- Table linking each competency to specific job requirements

### 2. Skill-Based Evaluation Framework
- Proficiency level definitions with behavioral anchors for each competency
- Clear differentiation criteria between levels

### 3. Evidence Collection Methods
- Specific evidence types required for each competency
- Documentation standards and work sample guidelines

### 4. Assessment Rubrics
- Tables with observable indicators for each skill at each proficiency level
- Concrete examples of what qualifies as evidence

### 5. Bias Prevention Protocols
- Common bias patterns in this role's assessment
- Countermeasures and calibration procedures

### 6. Implementation Guidelines
- Step-by-step deployment instructions
- Assessor training requirements
- Legal compliance checkpoints

Use tables for competency mapping and rubrics. Include specific examples throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{organizational-context}}、{{performance-data}}、{{role-and-competencies}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Competency-Based Performance Evaluation Model Builder is a free AI prompt that designs objective, skill-ba…
