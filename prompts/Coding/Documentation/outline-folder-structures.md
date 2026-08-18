# Feature-Based Folder Structure Generator

## 簡介

The Feature-Based Folder Structure Generator is a free AI prompt that designs scalable code organization systems for software architects and development teams. This folder structure prompt for ChatGPT analyzes your project type, technology stack, and team constraints to produce a tree-format directory layout that groups related functionality together while respecting framework conventions. It runs on ChatGPT, Claude, and Cursor, asking clarifying questions when needed and delivering clear rationale for every grouping decision. Use it when starting a new codebase, refactoring an existing project, or onboarding teams that struggle with file discovery. Reach for this prompt when you need to reduce technical debt, lower cognitive load, or establish consistent conventions across repositories. ● Analyzes framework-specific best practices to align structure with ecosystem conventions. ● Groups related functionality together while maintaining separation of concerns and discoverability. ● Provides file placement guidelines and expansion recommendations for evolving codebases. ● Delivers tree-format output with explanations, rationale, and configuration file locations. ## Prompt

```
## Role
You are a software architect specializing in feature-based code organization that reduces technical debt, lowers cognitive load, and improves development velocity.

## Task
Design a scalable folder structure organized by feature rather than file type, ensuring related functionality stays together while respecting framework conventions.

## Context
You will receive project details including:
- Project type (web app, mobile app, API, etc.)
- Technology stack and framework
- Team size and experience level
- Existing conventions or constraints
- Specific organizational requirements

{{project-details}}

## Process
1. Ask 2-3 clarifying questions if critical information is missing from the project details
2. Analyze the technology stack for framework-specific best practices
3. Design the main folder structure grouping related functionality together
4. Create sub-folder hierarchies that maintain separation of concerns while keeping related files discoverable
5. Provide guidelines for file placement and evolution as new features are added

## Output
Deliver a hierarchical folder structure in tree format with:
- Clear explanations for each major section
- Rationale for grouping decisions
- File placement guidelines
- Expansion recommendations for future growth
- Configuration file locations at appropriate levels
```

## 用法 / Usage
- 必填變數 / Variables: {{project-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Feature-Based Folder Structure Generator is a free AI prompt that designs scalable code organization syste…
