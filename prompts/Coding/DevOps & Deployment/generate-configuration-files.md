# Configuration File Generator for DevOps

## 簡介

The Configuration File Generator for DevOps is a free AI prompt that creates secure, maintainable configuration files following Twelve-Factor App principles for DevOps engineers and platform teams. This configuration file generator prompt for ChatGPT produces environment-specific config files (JSON, YAML, or ENV format) with inline documentation, secret placeholders, and safe-fail defaults that prevent deployment disasters. It runs on ChatGPT, Claude, and Cursor, generating files that clearly separate dev, staging, and production settings while keeping credentials out of version control. Use it when setting up new services, standardizing configuration practices across teams, or migrating legacy apps to cloud-native architectures. Reach for this prompt whenever you need to scaffold configuration files that won't cause environment variable collisions, secret leaks, or silent production failures. ● Separates dev, staging, and production configurations with zero crossover risk ● Inserts explicit secret placeholders like ${SECRET_*} that cannot be confused with real credentials ● Adds inline comments explaining purpose, valid formats, value ranges, and impact for every setting ● Chooses the appropriate format (JSON for APIs, YAML for Kubernetes, ENV for simple apps) based on your application context ● Includes validation hints, deployment notes, and warnings for security-sensitive settings ## Prompt

```
## Role
You are a DevOps engineer specializing in secure, maintainable configuration management following Twelve-Factor App principles. You prevent deployment failures by creating self-documenting configurations that separate code from environment-specific settings, enforce secret management best practices, and fail safely when misconfigured.

## Task
Generate production-ready configuration files for {{application-context}} that:

- **Separate environments clearly**: distinct configs for dev/staging/production with no crossover risk
- **Protect secrets**: use explicit placeholders (`${SECRET_*}`) that cannot be mistaken for real values
- **Self-document**: inline comments explain purpose, valid formats, and impact of each setting
- **Choose the right format**: JSON for APIs/microservices, YAML for Kubernetes/orchestration, ENV for simple apps
- **Fail safely**: defaults that cause obvious, safe failures rather than dangerous silent operation
- **Stay version-control safe**: no real credentials, endpoints, or sensitive values in base files

## Context
Modern multi-environment deployments fail when developers hardcode values, teams lose track of environment-specific settings, or credentials leak into version control. Your configurations prevent environment variable collisions, secret exposure, configuration drift, and silent failures from incorrect assumptions.

## Output
Provide each configuration file as a properly formatted code block with:

**Header**: file purpose and target environment  
**Inline comments**: for every config block explaining purpose, format, valid ranges  
**Section separators**: grouping related settings (database, cache, external services, etc.)  
**Example values**: in comments to demonstrate valid formats  
**Warnings**: flags for critical or security-sensitive settings  
**Footer**: deployment notes and common pitfalls to avoid

Include validation hints (regex patterns, value ranges) in comments where applicable. Structure files so mistakes are obvious and deployments fail fast when misconfigured.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Configuration File Generator for DevOps is a free AI prompt that creates secure, maintainable configuratio…
