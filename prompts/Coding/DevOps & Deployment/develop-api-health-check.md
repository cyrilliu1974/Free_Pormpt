# API Health Check Implementation Generator

## 簡介

The API Health Check Implementation Generator is a free AI prompt that produces production-ready health check code for DevOps engineers and microservices architects managing distributed systems. This API health check prompt for ChatGPT, Claude, and Cursor generates complete implementation code with endpoint validation, dependency testing, response time measurement, retry logic, and error handling patterns. It outputs configuration examples, JSON response schemas, deployment guidelines distinguishing startup/liveness/readiness probes, and failure mode handling for network timeouts, authentication errors, and partial degradation scenarios. Use it when building service monitoring for load balancers, Kubernetes orchestration, or operations dashboards that need intelligent traffic routing decisions. ● Validates endpoint connectivity, authentication, response codes, and optional body formats with configurable thresholds. ● Implements intelligent retry logic for transient failures and tests critical dependencies like databases, external APIs, and message queues. ● Provides clear status reporting JSON schemas that load balancers and orchestration platforms consume for routing decisions. ● Includes deployment recommendations for probe intervals, failure thresholds, graceful degradation, and comprehensive logging for operations teams. ## Prompt

```
## Role
You are an expert DevOps engineer and microservices architect specializing in resilient distributed systems and health check patterns.

## Task
Create a production-ready API health check implementation that validates service availability and guides load balancer traffic routing decisions.

## Context
{{health-check-requirements}}

The health check will be consumed by load balancers, orchestration platforms, and monitoring systems to make traffic routing decisions and alert operations teams.

## Requirements
The implementation must include:

- Endpoint connectivity validation and authentication verification
- Response code and optional body format checking
- Response time measurement with configurable thresholds
- Intelligent retry logic for transient failures
- Dependency health verification (database connections, external APIs, message queues)
- Clear status reporting for monitoring systems and load balancers
- Comprehensive error handling, timeout management, and logging
- Graceful degradation patterns for various failure scenarios

## Output
Provide:

1. **Implementation code** in {{programming-language}} with inline comments explaining key design decisions
2. **Configuration examples** showing timeout values, retry policies, and dependency check definitions
3. **Response format specification** (JSON schema or equivalent) that monitoring systems will consume
4. **Deployment considerations** including recommended probe intervals, failure thresholds, and startup/liveness/readiness distinctions
5. **Error handling patterns** for common failure modes (network timeouts, authentication failures, dependency outages, partial degradation)

Structure the code in clear, well-commented blocks ready for production deployment.
```

## 用法 / Usage
- 必填變數 / Variables: {{health-check-requirements}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The API Health Check Implementation Generator is a free AI prompt that produces production-ready health check …
