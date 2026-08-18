# Environment Variable Configuration Prompt

## 簡介

The Environment Variable Configuration Prompt is a free AI prompt that generates secure, production-ready environment variable configuration guides for DevOps engineers and developers following Twelve-Factor App principles. This environment variable configuration prompt for ChatGPT, Claude, and Cursor produces code examples for loading and validating environment variables at startup, deployment patterns for Docker, Kubernetes, AWS, Azure, and GCP, a security checklist covering secret storage solutions like HashiCorp Vault and AWS Secrets Manager, and a step-by-step migration path from hard-coded configuration to externalized config. It accepts your tech stack, configuration requirements, and target platform as input, then outputs language-specific code with validation, default handling, API client initialization patterns, platform-specific injection methods,.gitignore rules, and rollback strategies. Reach for this prompt when you need to externalize configuration, prepare an application for multi-environment deployment, or audit existing configuration management for security gaps. ● Produces code examples for environment variable loading with startup validation, fail-fast checks, and default value handling for local development. ● Generates platform-specific deployment patterns for Docker, Kubernetes, AWS, Azure, and GCP with environment promotion workflows. ● Includes a security checklist covering secret storage solutions,.gitignore configuration, least-privilege access, and pre-deployment validation. ● Provides a migration path with rollback strategies to move from current configuration methods to externalized environment-based config. ## Prompt

```
## Role

You are an expert DevOps engineer and security architect specializing in Twelve-Factor App methodology, configuration management, and secure deployment practices.

## Task

Generate a comprehensive environment variable configuration guide that separates configuration from code, enables seamless deployment across development, staging, and production environments, and maintains security standards. Keep secrets out of version control while ensuring consistent deployments without code modifications.

## Context

**Tech stack:** {{tech-stack}}

**Configuration requirements:** {{config-requirements}}

**Target platform:** {{platform}}

## Output

Provide:

### Code Examples

For the specified language/framework, show:

- Environment variable loading with validation at startup
- Default value handling for local development
- API client initialization patterns from environment config
- Startup checks that fail fast on misconfiguration

### Deployment Patterns

For the target platform (Docker, Kubernetes, AWS, Azure, GCP, etc.), demonstrate:

- How to inject environment variables
- Platform-specific configuration approaches
- Environment promotion workflows

### Security Checklist

Cover:

- Secret storage solutions (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, etc.)
- .env file handling and .gitignore rules
- Environment-specific configuration strategies
- Validation that catches errors before deployment
- Least-privilege access patterns

### Migration Path

Provide step-by-step guidance to move from the current configuration method to this best-practice approach, including rollback strategies.

Structure all code blocks with language labels, use clear headings, and provide bulleted implementation steps.
```

## 用法 / Usage
- 必填變數 / Variables: {{config-requirements}}、{{platform}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Paper_Quality_Hardening_Loop
- 適用 / Use when: The Environment Variable Configuration Prompt is a free AI prompt that generates secure, production-ready envi…
