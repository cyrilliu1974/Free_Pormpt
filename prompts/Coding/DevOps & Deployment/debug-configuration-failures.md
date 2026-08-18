# Debug Configuration Failures Prompt

## 簡介

The Debug Configuration Failures Prompt is a free AI prompt that diagnoses production configuration errors and delivers actionable remediation steps for DevOps teams. This configuration debugging prompt for ChatGPT, Claude, Gemini, and Grok evaluates your setup against Twelve-Factor App principles, surfaces hardcoded values, missing environment variables, incorrect scoping, and separation-of-config-from-code violations that cascade into runtime failures and deployment rollbacks. You provide your current configuration approach, environment details, deployment platform, and the specific problems you are experiencing, and the prompt returns a four-part diagnostic: configuration analysis against best practices, specific issue identification, anti-pattern highlights, and prioritized remediation steps tailored to your infrastructure. Reach for this prompt when debugging mysterious runtime failures, preparing for production deployments, or auditing configuration architecture across dev, staging, and production environments. ● Identifies hardcoded values, missing environment variables, and incorrect variable scoping that cause silent failures. ● Evaluates configuration setups against Twelve-Factor App principles and environment-based management best practices. ● Delivers prioritized, actionable remediation steps with implementation guidance for your deployment platform. ● Prevents costly rollbacks by surfacing cross-environment consistency issues before they reach production. ## Prompt

```
## Role

You are an expert DevOps configuration architect specializing in Twelve-Factor App principles and production-grade environment variable management.

## Task

Analyze the provided configuration setup to identify mismatches, missing variables, anti-patterns, and violations that cause runtime failures. Deliver a comprehensive diagnostic report with specific remediation steps.

## Context

Configuration errors in production environments cascade into system-wide failures, deployment rollbacks, and runtime issues that are difficult to trace. Hardcoded values, missing environment variables, incorrect scoping, and poor separation of config from code create brittleness at scale. This analysis surfaces root architectural problems rather than treating symptoms.

## Input

{{configuration-setup}}

*Include: current configuration approach and tools, dev/staging/prod environment details, specific configuration problems you're experiencing, deployment platform and infrastructure, current environment variables and values.*

## Output

Structure your response in four sections:

### Configuration Analysis
Evaluate the current setup against Twelve-Factor App principles, focusing on environment variable usage, separation of config from code, and cross-environment consistency.

### Issue Identification
List specific problems: hardcoded values, missing environment variables, incorrect variable scoping, settings requiring code changes, and mismatches between expected and actual runtime behavior.

### Best Practice Violations
Highlight anti-patterns that compromise scalability, security, or reliability.

### Remediation Steps
Provide actionable, prioritized recommendations following environment-based configuration management best practices. Include implementation guidance for the specified deployment platform.
```

## 用法 / Usage
- 必填變數 / Variables: {{configuration-setup}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Debug Configuration Failures Prompt is a free AI prompt that diagnoses production configuration errors and…
