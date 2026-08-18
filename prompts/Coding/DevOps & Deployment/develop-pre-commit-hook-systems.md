# Pre-Commit Hook System Implementation Prompt

## 簡介

The Pre-Commit Hook System Implementation Prompt is a free AI prompt that generates complete pre-commit hook configurations for development teams who need automated code quality enforcement before commits reach version control. This pre-commit hook prompt for ChatGPT, Claude, and Cursor produces a full implementation guide that includes installation commands, configuration files for Husky and lint-staged, check definitions mapped to file types, setup instructions, developer documentation, and troubleshooting steps. You provide your project context (tech stack, existing tools, team workflow), and the prompt designs a system that runs linting, testing, and formatting checks only on staged files, auto-fixes what it can, and blocks commits when critical issues are found. It works across JavaScript, TypeScript, Python, and other common development stacks, ensuring cross-platform compatibility and clear error messages that guide developers toward fixes rather than frustrating them. Reach for this prompt when setting up a new repository's quality gates, standardizing commit practices across a team, or replacing manual code review steps with automated enforcement. ● Configures lint-staged to run checks only on staged files, keeping pre-commit operations fast even in large repositories. ● Maps file patterns to appropriate quality tools (ESLint, Prettier, pytest, Black) with auto-fix enabled where safe and blocking behavior for critical failures. ● Provides complete configuration files including package.json scripts, Husky hook scripts, and linter configs ready to copy into your repository. ● Includes a developer guide explaining what happens during commits, how to skip hooks in emergency scenarios, and how to resolve common failure cases. ## Prompt

```
## Role
You are a DevOps engineer specializing in automated code quality enforcement. Your task is to implement a pre-commit hook system using Husky and lint-staged that catches issues before they reach version control.

## Task
Design and configure a pre-commit hook system that:

1. **Runs targeted checks** only on staged files for speed
2. **Auto-fixes** formatting issues automatically
3. **Blocks commits** when critical issues are detected (failing tests, lint errors)
4. **Provides clear error messages** that tell developers exactly what failed and how to fix it
5. **Integrates seamlessly** with the existing development workflow

## Context
{{project-context}}

## Requirements
- Configure Husky to manage Git hooks
- Use lint-staged to run checks only on staged files
- Map file types to appropriate quality checks (linting, testing, formatting)
- Design error handling that is actionable, not punitive
- Ensure cross-platform compatibility
- Keep the system simple and extensible

## Output
Provide a complete implementation guide structured as:

### 1. Installation
Commands to install Husky, lint-staged, and necessary linters/formatters for the specified stack.

### 2. Configuration Files
Complete configuration files:
- `package.json` scripts and lint-staged config
- `.husky/pre-commit` hook script
- Linter/formatter config files as needed

### 3. Check Definitions
Which checks run on which file patterns, with rationale for auto-fix vs. block decisions.

### 4. Setup Instructions
Step-by-step commands to initialize the system in the repository.

### 5. Developer Guide
How the system works, what developers will experience, and how to handle common scenarios (skip hooks when necessary, resolve failures).

### 6. Troubleshooting
Common errors and their solutions, organized by symptom.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Agent_State&Trajectory_Engineering · Trajectory_Pair_Generation_Protocol
- 適用 / Use when: The Pre-Commit Hook System Implementation Prompt is a free AI prompt that generates complete pre-commit hook c…
