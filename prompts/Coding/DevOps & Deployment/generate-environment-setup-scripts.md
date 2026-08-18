# Environment Setup Script Generator

## 簡介

The Environment Setup Script Generator is a free AI prompt that creates bulletproof, self-documenting environment automation scripts for DevOps engineers and infrastructure teams. This environment setup script prompt for ChatGPT, Claude, and Cursor produces a complete setup automation solution including pre-installation system checks, dependency validation, version-pinned package installation, environment variable configuration, post-installation verification tests, and rollback mechanisms for failed installations. The generated scripts are idempotent - safe to run multiple times without breaking existing configurations - and include inline documentation explaining each section. Use it to automate onboarding for new team members, ensure consistency across development and production environments, or eliminate manual configuration errors that cause deployment failures. Reach for this prompt when you need to standardize environment setup across a team, migrate infrastructure to code, or reduce onboarding time from weeks to minutes. ● Outputs scripts with declarative configuration and dependency ordering that prevent installation conflicts and version mismatches. ● Includes pre-flight system checks and post-installation verification tests to catch incompatibilities before they reach production. ● Generates rollback procedures and error-handling logic so failed installations can be safely reversed without manual intervention. ● Produces markdown documentation covering prerequisites, quick-start instructions, troubleshooting steps, and configuration options alongside the script. ## Prompt

```
## Role
You are an expert DevOps infrastructure engineer specializing in production-ready environment automation and infrastructure-as-code.

## Task
Create a comprehensive, idempotent environment setup script with documentation that eliminates manual configuration errors and enables rapid team onboarding.

## Context
Environment inconsistencies are causing production failures, onboarding takes weeks, and manual setup creates security vulnerabilities. The script must be bulletproof, self-documenting, and safe to run multiple times without breaking existing configurations.

### Target Environment
{{target-os}}

### Stack Requirements
{{stack-requirements}}

## Output
Deliver a complete setup automation solution with:

### 1. Setup Script
- Pre-installation system checks and dependency validation
- Package installation in correct dependency order with version pinning
- Environment variables and PATH configuration with proper precedence
- Post-installation verification (version checks, functionality tests)
- Rollback mechanisms for failed installations
- Comprehensive error handling and logging
- Cross-platform compatibility where applicable
- Inline documentation via comments explaining each section

### 2. Setup Documentation
Provide markdown documentation covering:
- Prerequisites and system requirements
- Quick-start instructions
- Troubleshooting common issues
- Configuration options
- Rollback procedures

Structure the script in clearly labeled sections. Follow declarative configuration principles and ensure idempotent operations throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{stack-requirements}}、{{target-os}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Environment Setup Script Generator is a free AI prompt that creates bulletproof, self-documenting environm…
