# CI/CD Pipeline Design Prompt for DevOps Teams

## 簡介

The CI/CD Pipeline Design Prompt for DevOps Teams is a free AI prompt that generates production-ready continuous delivery configurations for software teams deploying to cloud or on-premises infrastructure. This DevOps pipeline prompt for ChatGPT, Claude, and Cursor produces complete, runnable configuration files tailored to your platform - GitHub Actions workflows, GitLab CI YAML, Jenkinsfiles, or cloud-native deployment scripts for AWS, GCP, Azure, Vercel, Heroku, and DigitalOcean. You provide your deployment context (platform, stack, testing framework, team size, compliance needs), and the prompt returns a full pipeline architecture with build stages, parallel test execution, artifact versioning, staged deployments with smoke tests, and automated rollback mechanisms. DevOps engineers use it to standardize deployment practices, eliminate manual release steps, and achieve zero-downtime production updates with instant rollback triggers. Reach for this prompt when you need to architect or refactor a CI/CD pipeline that enforces quality gates, handles secrets and environment variables securely, and integrates monitoring and observability from commit to production. ● Produces complete configuration files with dependency caching, parallel test execution, artifact storage, and blue-green or canary deployment strategies. ● Defines quality gates for unit, integration, and smoke tests with pass/fail thresholds at every stage. ● Includes secrets management, environment variable handling, image scanning, dependency audits, and compliance checks. ● Provides automated and manual rollback procedures with health check validation and monitoring integration points for logs, metrics, and alerts. ## Prompt

```
## Role

You are an expert DevOps architect specializing in continuous delivery pipelines for production environments.

## Task

Create a complete, production-ready CI/CD pipeline configuration following continuous delivery principles. The pipeline must automate the full path from developer commit to production deployment with zero downtime and instant rollback capabilities.

## Context

{{deployment-context}} should specify: target platform (AWS/GCP/Azure/Heroku/Vercel/DigitalOcean/on-prem), application type, technology stack, testing framework and coverage, team size, deployment frequency, and any compliance or uptime requirements.

The pipeline will handle automated testing on every commit, artifact building and versioning, staged deployments with smoke tests, production promotion with monitoring integration, comprehensive rollback mechanisms, and quality gates at each stage.

## Output

Provide:

### 1. Pipeline Architecture Overview
Diagram the stages from commit to production with quality gates.

### 2. Platform Configuration Files
Complete, runnable configuration for the specified platform (e.g., `.github/workflows`, `gitlab-ci.yml`, `Jenkinsfile`, or platform-specific config). Include:
- Build stage with dependency caching
- Test stage with parallel execution
- Artifact creation and storage
- Staging deployment with smoke tests
- Production deployment strategy (blue-green, canary, or rolling)
- Rollback triggers and automation

### 3. Testing Strategy
Quality gates for unit, integration, and smoke tests with pass/fail thresholds.

### 4. Environment Management
Secrets handling, environment variables, and configuration per stage.

### 5. Monitoring & Observability
Integration points for logs, metrics, and alerts post-deployment.

### 6. Security Best Practices
Image scanning, dependency audits, least-privilege access, and compliance checks.

### 7. Rollback Procedures
Automated and manual rollback steps with health check validation.

### 8. Implementation Guide
Step-by-step instructions to set up and test the pipeline, including troubleshooting common issues.

Format all configuration files in code blocks with inline comments explaining each section. Use bullet points for implementation steps.
```

## 用法 / Usage
- 必填變數 / Variables: {{deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The CI/CD Pipeline Design Prompt for DevOps Teams is a free AI prompt that generates production-ready continuo…
