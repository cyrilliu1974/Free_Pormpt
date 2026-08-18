# Google Sheets Automation Code Generator

## 簡介

The Google Sheets Automation Code Generator is a free AI prompt that produces executable automation code for safely updating Google Sheets while preserving formulas, handling API limits, and maintaining data integrity through failures. This Google Sheets automation prompt for ChatGPT, Claude, and Cursor generates complete code organized into six sections: secure authentication setup (service accounts or OAuth with automatic token refresh), data extraction and transformation pipelines, Sheet update logic with batch operations and exponential backoff (initial 1s, max 32s), error handling for network failures and concurrent edits, scheduling with cron-compatible syntax, and deployment instructions with testing scenarios. It treats Sheets as a presentation layer receiving validated data, respecting the 100 requests per 100 seconds API quota and implementing read-back validation to confirm writes. Real use cases include syncing database records to dashboards, populating reports from API endpoints on schedule, and bridging disparate data systems with audit trails. Reach for this prompt when you need to build reliable Sheets integrations that handle authentication complexity, quota exhaustion (HTTP 429), concurrent access conflicts, and partial write failures with rollback capability. ● Generates secure authentication code for service accounts or OAuth with environment variable loading and automatic token refresh strategies ● Implements batch operations with exponential backoff retry logic and idempotent writes that safely resume after network interruptions or quota exhaustion ● Preserves existing formulas in target ranges, validates data types before writes, and performs read-back confirmation to ensure data integrity ● Includes audit logging with timestamps and affected ranges, failure alerts with actionable diagnostics, and rollback mechanisms for failed operations ## Prompt

```
## Role

You are an automation architect specializing in Google Sheets integrations. Your experience spans API quota management, concurrent edit handling, authentication patterns, and dimensional modeling principles applied toSheet automation. You design systems that treat Sheets as a presentation layer for transformed data, not as a transactional database.

## Task

Create production-ready Google Sheets automation code that safely updates sheets while preserving formulas, handling API limits, and maintaining data integrity through failures.

## Context

The automation must solve real operational challenges:

- **Authentication complexity**: Service accounts and OAuth tokens require secure management and automatic refresh
- **API constraints**: 100 requests per 100 seconds quota, write operations that may be throttled
- **Concurrent access**: Multiple users or processes editing simultaneously
- **Data integrity**: Formula preservation, atomic updates, type validation
- **Failure modes**: Network interruptions, permission errors, quota exhaustion, partial writes
- **Audit requirements**: Track what changed, when, and maintain rollback capability

Apply dimensional modeling principles: establish staging areas for extraction, transformation logic for cleaning, and treat the target Sheet as the final presentation layer receiving validated data on schedule.

## Input

{{automation-spec}}

*Provide: (1) Google Sheet URL, (2) authentication method (service account JSON path or OAuth credentials), (3) data source (database connection, API endpoint, or file path), (4) update schedule (cron expression or frequency), (5) notification endpoint (email, webhook URL, or Slack channel).*

## Output

Deliver executable code organized into these sections:

### 1. Configuration & Authentication

- Secure credential loading from environment variables
- Service account or OAuth setup with automatic token refresh
- Connection validation before operations begin

### 2. Data Extraction & Transformation

- Source data retrieval with connection pooling
- Transformation logic applying business rules
- Schema validation before Sheet writes

### 3. Sheet Update Implementation

- Target range identification preserving formula cells
- Batch operations for quota efficiency
- Exponential backoff retry logic (initial 1s, max 32s)
- Idempotent write operations that handle interruptions
- Read-back validation confirming successful writes

### 4. Error Handling & Recovery

- Comprehensive exception catching for:
  - Network failures and timeouts
  - Permission and authentication errors
  - Quota exhaustion (HTTP 429)
  - Concurrent edit conflicts
  - Data validation failures
- Rollback mechanisms for failed operations
- Audit logging with timestamp, process ID, affected ranges, change summary

### 5. Scheduling & Monitoring

- Scheduler implementation (cron-compatible) with timezone handling
- Failure alerts within 5 minutes containing actionable diagnostics
- Success confirmations with record counts and execution time
- Performance metrics tracking (duration, rows processed, API calls used)

### 6. Deployment Instructions

- Step-by-step setup guide
- Environment variable configuration
- Dependency installation commands
- Testing scenarios covering happy path and failure modes

**Code requirements:**

- Include inline comments explaining critical decisions and potential failure points
- Use appropriate syntax highlighting in code blocks
- Ensure operations are idempotent (safe to retry)
- Never log credentials or sensitive data
- Implement least-privilege access patterns
- Respect the 100 requests/100 seconds API limit
- Preserve existing formulas in target ranges
- Maintain data type integrity during writes

Provide example usage demonstrating a complete update cycle.
```

## 用法 / Usage
- 必填變數 / Variables: {{automation-spec}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Google Sheets Automation Code Generator is a free AI prompt that produces executable automation code for s…
