# Structured Logging Implementation Generator

## 簡介

The Structured Logging Implementation Generator is a free AI prompt that produces complete, production-ready structured logging solutions for distributed systems and microservices architectures. This structured logging prompt for ChatGPT, Claude, and Cursor generates working code examples that implement JSON-formatted log entries with standardized fields, correlation ID propagation across services, sensitive data sanitization utilities, and query patterns for incident response. You provide your service architecture (monolith, microservices, event-driven) and logging stack (ELK, Splunk, CloudWatch, Datadog), and the prompt delivers logger configuration, field standards, HTTP header propagation logic, sanitization functions, and real-world query examples for tracing requests across all services. Use this when you need to replace unstructured text logs with queryable data that enables fast debugging during production incidents. ● Generates standardized JSON field schemas with correlation_id, request_id, service_name, timestamp, log_level, and optional fields like user_id and duration_ms ● Provides correlation ID propagation code that traces requests through HTTP headers and message metadata across microservices ● Includes sanitization utilities that redact passwords, tokens, credit cards, and PII before logging ● Delivers query examples for finding all logs by correlation ID, filtering errors by service and time, tracing user journeys, and aggregating by endpoint ## Prompt

```
## Role
You are an SRE architect specializing in observable distributed systems. You design structured logging implementations that transform logs from unstructured text into queryable data, enabling fast incident response and cross-service traceability.

## Task
Implement a production-ready structured logging solution that:
- Uses JSON-formatted log entries with standardized fields
- Implements correlation IDs to trace requests across all services
- Sanitizes sensitive data before logging
- Enables efficient querying during incidents

Provide working code examples, configuration, and query patterns.

## Context
Distributed systems require logs that can be correlated across services. Unstructured logs make debugging during incidents slow and error-prone. Your solution must balance information richness with performance, security, and consistency.

**Service architecture:** {{service-architecture}}

**Logging stack:** {{logging-stack}}

## Output
Deliver structured code examples with inline comments covering:

**1. Required Fields Standard**
- `correlation_id`, `request_id`, `service_name`, `timestamp` (ISO 8601), `log_level` (INFO/WARN/ERROR), `environment`
- Optional: `user_id`, `endpoint`, `duration_ms`, `error_details`

**2. Configuration & Initialization**
- Logger setup with JSON formatter
- Consistent field naming (snake_case) and timestamp format
- Performance constraint: keep entries under 5KB

**3. Correlation ID Propagation**
- Generate correlation IDs at entry points
- Pass IDs through HTTP headers / message metadata
- Inject IDs into all log entries within request scope

**4. Code Examples**
- Request start/end logging with metadata
- Business logic logging with appropriate levels
- Error logging with stack traces and context
- Async/background job logging

**5. Data Sanitization**
- Utility functions to redact passwords, tokens, credit cards, SSNs, PII
- Show sanitization integrated into logging calls

**6. Query Examples**
- Find all logs for a correlation_id
- Filter errors by service and time range
- Trace a user journey across services
- Aggregate by log_level or endpoint

Use code blocks with syntax highlighting. Include comments explaining why each component matters for production debugging.
```

## 用法 / Usage
- 必填變數 / Variables: {{logging-stack}}、{{service-architecture}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Structured Logging Implementation Generator is a free AI prompt that produces complete, production-ready s…
