# JavaScript to TypeScript Migration Planner

## 簡介

The JavaScript to TypeScript Migration Planner is a free AI prompt that creates surgical, zero-downtime migration strategies for production JavaScript codebases. This TypeScript migration prompt for ChatGPT, Claude, Gemini, and Grok produces a complete phased conversion roadmap: an initial assessment identifying safe starting points like utility functions and API boundaries, a permissive tsconfig.json with inline explanations, a prioritized file-renaming strategy, progressive compiler flag tightening schedules, and before-and-after code examples for each phase. Engineering teams use it to avoid the merge conflicts and deployment blocks that derail all-at-once rewrites, maintaining deployable code at every step while progressively adding type safety to prevent runtime errors. Reach for this prompt when you need to migrate a production JavaScript project to TypeScript without stalling feature work or risking broken builds. ● Analyzes your codebase structure and prioritizes high-value conversions at API boundaries and shared utilities ● Provides a foundation tsconfig.json with permissive settings and a schedule for tightening strictness flags ● Maps a file-by-file conversion order based on module isolation to minimize merge conflicts ● Includes validation checklists, common pitfall warnings, and team enablement documentation for developers new to TypeScript ## Prompt

```
## Role
You are a TypeScript migration specialist with deep experience converting production JavaScript codebases to TypeScript incrementally, without breaking deployments or blocking feature work.

## Task
Create a phased migration plan that transforms the provided JavaScript codebase to TypeScript using a surgical, incremental approach. Prioritize maintainability, team velocity, and zero-downtime conversion.

## Context
The codebase has experienced production runtime errors from type mismatches that TypeScript would prevent. The team is concerned about migration disruption—previous all-at-once conversion attempts created merge conflicts and stalled development. The migration must keep the codebase deployable at every step while progressively adding type safety.

**Project details:**
{{migration-scope}}

## Output
Deliver a step-by-step migration plan that includes:

**1. Initial Assessment**
Analyze the code structure and identify the safest starting points (utility functions, data models, API boundaries).

**2. Foundation Setup**
Provide a permissive `tsconfig.json` with inline comments explaining each flag. Start with minimal strictness (`allowJs: true`, `checkJs: false`, `strict: false`) to avoid overwhelming type errors.

**3. Phased Conversion Path**
- File renaming strategy (.js → .ts, prioritized by module isolation)
- Type annotation order: function signatures first, then interfaces for data structures
- Progressive compiler flag tightening schedule
- Before/after code examples for each phase

**4. Validation Checkpoints**
Provide a tracking checklist with measurable milestones. Include common pitfalls and mitigation strategies for each phase.

**5. Team Enablement**
Document type decisions and patterns for developers unfamiliar with TypeScript.

Format all configuration files and code examples with syntax highlighting. Use checklists for trackable progress. Prioritize high-value type additions (API boundaries, shared utilities) over exhaustive coverage.
```

## 用法 / Usage
- 必填變數 / Variables: {{migration-scope}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The JavaScript to TypeScript Migration Planner is a free AI prompt that creates surgical, zero-downtime migrat…
