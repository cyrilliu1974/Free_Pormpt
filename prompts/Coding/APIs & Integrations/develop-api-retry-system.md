# API Retry Logic with Exponential Backoff Generator

## 簡介

The API Retry Logic with Exponential Backoff Generator is a free AI prompt that produces production-grade retry code for distributed systems engineers and backend developers facing API integration challenges. This API retry logic prompt for ChatGPT, Claude, and Cursor generates complete code that includes exponential backoff with jitter, rate limit header parsing (Retry-After, X-RateLimit-Reset), error classification distinguishing retryable from permanent failures, and circuit breaker patterns to prevent cascading outages. It transforms your API context into structured, documented retry functions that respect server constraints, prevent retry storms, and fail gracefully under load. Reach for this prompt when you need to implement resilient API integrations that handle transient failures, rate limit violations, and server downtime without triggering business disruptions. ● Exponential backoff with jitter (1s, 2s, 4s, 8s delays) and configurable maximum attempts to prevent thundering herd problems. ● Header parsing utilities that extract and honor Retry-After, X-RateLimit-Reset, and X-RateLimit-Remaining to respect server boundaries. ● Error classification logic that distinguishes retryable errors (429, 503, 502, timeouts) from permanent failures (400, 401, 403, 404) with idempotency checks for state-modifying requests. ● Circuit breaker pattern with monitoring hooks to fail fast when APIs are consistently down and track retry patterns in production. ## Prompt

```
## Role

You are an expert distributed systems engineer specializing in resilient API integration patterns.

## Task

Implement production-grade API retry logic with exponential backoff for {{api-context}}. The solution must prevent retry storms, respect rate limits, and fail gracefully under pressure.

## Context

API failures cascade into business disruptions when retry logic is naive. Aggressive retries transform minor issues into catastrophic outages. Rate limit violations trigger escalating penalties and potential account suspension. The implementation must treat server constraints as hard boundaries.

## Requirements

**Exponential Backoff Strategy:**
- Calculate delays as 1s, 2s, 4s, 8s with jitter to prevent thundering herd
- Maximum 5 retry attempts, cap delay at 32 seconds
- Always honor `Retry-After` headers when present—they override backoff calculations

**Rate Limit Handling:**
- Parse and respect `Retry-After`, `X-RateLimit-Reset`, `X-RateLimit-Remaining` headers
- Extract server-provided timing and adjust retry schedules accordingly

**Error Classification:**
- **Retryable:** 429 (rate limit), 503 (service unavailable), 502 (bad gateway), network timeouts
- **Non-retryable:** 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found)
- Never retry state-modifying requests unless idempotency is guaranteed

**Safeguards:**
- Implement circuit breakers to fail fast when APIs are consistently down
- Add hard limits to prevent infinite loops
- Include monitoring hooks to track retry patterns

## Output

Provide structured, production-ready code with:

1. **Main retry function** implementing exponential backoff with jitter
2. **Header parsing utilities** to extract rate limit information
3. **Error classification logic** distinguishing retryable from permanent failures
4. **Circuit breaker pattern** to prevent cascading failures
5. **Example usage** demonstrating rate limit hits, transient server errors, and permanent errors
6. **Configuration options** for customizing max attempts, base delay, and jitter range

Use clear variable names, modular functions, and detailed inline comments explaining each component. Structure code for easy integration into existing systems.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The API Retry Logic with Exponential Backoff Generator is a free AI prompt that produces production-grade retr…
