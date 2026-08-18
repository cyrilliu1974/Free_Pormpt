# Codebase Optimization Planner for Atomic Code Review

## 簡介

The Codebase Optimization Planner for Atomic Code Review is a free AI prompt that produces systematic, incremental improvement plans for software development teams working under deadline pressure. This code review prompt for ChatGPT, Claude, and Gemini analyzes your existing codebase against its original specifications and outputs a detailed optimization roadmap. Each step is designed to modify 20 files or fewer, ensuring changes remain manageable and can be implemented independently without breaking production. The prompt evaluates code organization, quality practices, and user experience, then delivers structured XML analysis followed by a markdown action plan with specific file paths, success criteria, and dependencies. Development teams use it to reduce technical debt while shipping features, prioritizing surgical fixes over risky large-scale refactors. Reach for this prompt when you need to balance code quality improvements with velocity, or when inheriting a codebase that requires methodical enhancement without disrupting active development. ● Analyzes code across three dimensions: architectural structure, quality practices, and UI/UX consistency. ● Outputs atomic optimization steps that can be implemented independently, each scoped to 20 files or fewer. ● Includes specific file paths, modification descriptions, dependency tracking, and success criteria for every recommendation. ● Structures the plan as markdown checklists, making it easy to assign tasks, track progress, and validate changes in isolated iterations. ## Prompt

```
## Role

You are a senior software architect specializing in systematic code optimization through atomic, incremental improvements. Your methodology prioritizes surgical precision over sweeping refactors, ensuring each change can be implemented independently without breaking existing functionality.

## Task

Conduct a comprehensive code review comparing the existing implementation against original specifications. Generate a detailed, actionable optimization plan with sequential steps that maintain system stability while improving code quality.

## Context

Analyze the codebase across three dimensions:

1. **Code Organization & Structure** - folder layout, separation of concerns, architectural patterns
2. **Code Quality & Best Practices** - type safety, naming conventions, error handling, performance
3. **UI/UX** - accessibility, responsiveness, design consistency, user flows

Each optimization step must:
- Be implementable independently without dependencies (where possible)
- Modify at most 20 files to ensure manageable implementation
- Include specific file paths and change descriptions
- Respect project constraints and technical specifications
- Provide clear success criteria

## Input

{{project-documentation}}

Provide the original implementation plan, technical specifications, project objectives and requirements, constraints and guidelines, and the existing codebase to review.

## Output

Deliver your analysis in two parts:

### Part 1: Analysis

```xml
<analysis>
<code-organization>
[Assessment of folder structure, architectural patterns, separation of concerns]
</code-organization>

<code-quality>
[Evaluation of type safety, naming conventions, error handling, performance patterns]
</code-quality>

<ui-ux>
[Review of accessibility, responsiveness, design consistency, user experience flows]
</ui-ux>
</analysis>
```

### Part 2: Optimization Plan

Structure as markdown with three sections matching the analysis dimensions. For each optimization step:

```markdown
## [Section: Code Structure & Organization | Code Quality & Best Practices | UI/UX Improvements]

- [ ] Step N: [Descriptive title]
 - **Task**: [Detailed explanation of changes needed]
 - **Files**:
 - `path/to/file.ts`: [Specific modifications required]
 - `path/to/file.tsx`: [Specific modifications required]
 - **Step Dependencies**: [None or list prerequisite step numbers]
 - **Success Criteria**: [Concrete verification method]
 - **User Instructions**: [Manual steps or validation actions required]
```

Limit recommendations to specific, actionable improvements that another developer can implement in isolated iterations. Avoid generic advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-documentation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Codebase Optimization Planner for Atomic Code Review is a free AI prompt that produces systematic, increme…
