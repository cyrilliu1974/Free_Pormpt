# Test Case Description Writer for Software QA

## 簡介

The Test Case Description Writer for Software QA is a free AI prompt that generates structured, complete test-case documentation for software quality assurance teams and testers. This test case prompt for ChatGPT, Claude, Gemini, and Grok analyzes your software requirements and testing environment to produce detailed test cases covering positive and negative scenarios, edge cases, boundary values, and different user roles. Each test case includes a unique ID, objective, priority level, preconditions, numbered test steps, expected results, actual results fields for execution tracking, and requirement traceability. The prompt considers both functional testing and non-functional aspects such as performance, security, and usability, ensuring comprehensive test coverage across all critical software behaviors. QA engineers, test leads, and development teams use this prompt when documenting test plans, preparing for regression cycles, or establishing traceability between requirements and test execution. ● Outputs test cases with all standard fields: ID, objective, priority, preconditions, numbered steps, expected and actual results, and requirement traceability. ● Covers positive paths, negative scenarios, edge cases, boundary value analysis, and permission-based testing across user roles. ● Prioritizes test cases by criticality and impact, helping teams focus on high-risk areas first. ● Ensures alignment between software requirements and test coverage, supporting audit and compliance needs. ## Prompt

```
## Role
You are an expert software quality assurance engineer writing comprehensive, structured test-case descriptions.

## Task
Create clear, detailed test cases that ensure thorough software testing coverage. Each test case must include:
- Test Case ID and Objective
- Preconditions
- Test Steps (numbered)
- Expected Results
- Actual Results (field)

## Context
**Software Application & Requirements:**
{{software-and-requirements}}

**Development & Testing Environment:**
{{environment-and-tools}}

Consider the following in your test design:
- Both positive and negative scenarios
- Edge cases and boundary value analysis
- Different user roles and permissions where applicable
- Functional and non-functional aspects (performance, security, usability)
- Traceability to requirements
- Prioritization based on criticality and impact

## Output
Provide test cases in this structured format:

**Test Case ID:** [Unique identifier]
**Objective:** [What this test validates]
**Priority:** [Critical/High/Medium/Low]
**Preconditions:** [Setup requirements]
**Test Steps:**
1. [Action]
2. [Action]
**Expected Results:** [What should happen]
**Actual Results:** [To be filled during test execution]
**Traceability:** [Requirement ID]
```

## 用法 / Usage
- 必填變數 / Variables: {{environment-and-tools}}、{{software-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Test Case Description Writer for Software QA is a free AI prompt that generates structured, complete test-…
