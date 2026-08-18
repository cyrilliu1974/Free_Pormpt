# Request Timeout Configuration Code Generator

## 簡介

The Request Timeout Configuration Code Generator is a free AI prompt that produces multi-layered timeout strategies to prevent cascading failures and resource exhaustion in distributed systems. This request timeout prompt for ChatGPT, Claude, and Cursor generates production-ready code that addresses connection establishment, data transmission, and total request lifecycle timeouts. It delivers specific timeout values justified by network topology, retry logic with exponential backoff and jitter, circuit breaker integration, and resource cleanup procedures. Engineers use it to prevent connection pool depletion, thread hangs, and abandoned transactions caused by indefinite network waits. The prompt outputs implementation code tailored to your language or framework - whether Node.js, Python, Java, Go, or others - complete with inline explanations, edge case handling, and monitoring configurations. Reach for this prompt when you need to implement defensive timeout patterns that account for DNS resolution overhead, TLS handshakes, slow data streams, and cross-region latency. ● Generates connection timeout code accounting for DNS resolution, network latency, and TLS handshake overhead with justified values for local, cross-region, and third-party scenarios ● Implements read timeout strategies with chunk reading logic, partial data handling, and API-characteristic-based timeout values ● Produces total request lifecycle management code with retry exponential backoff, jitter, circuit breaker integration, and proper cancellation cleanup ● Includes monitoring configurations, graceful degradation patterns, summary tables of recommended timeout ranges, and edge case handling for connection pool exhaustion ## Prompt

```
## Role
Distributed systems engineer specializing in defensive timeout patterns and network resilience.

## Task
Design and implement a multi-layered timeout strategy that prevents cascading failures, resource exhaustion, and indefinite waits. Provide production-ready code with specific timeout values, error handling, retry logic with exponential backoff and jitter, and monitoring approaches.

## Context
The application experiences catastrophic failures from indefinite network waits that cascade into resource exhaustion. Connection pools deplete, threads hang, and transactions are abandoned. Previous implementations failed by addressing symptoms rather than the multi-layered nature of network failures.

**Requirements:**
{{timeout-requirements}}

**Target stack:**
{{language-or-framework}}

## Output
Structure your implementation across three critical layers:

### 1. Connection Timeout Configuration
- TCP connection establishment timeouts with DNS resolution and network latency considerations
- TLS handshake overhead accounting
- Specific timeout values with justification based on network topology (local vs. cross-region)

### 2. Read Timeout Implementation
- Data transmission timeouts and chunk reading strategies
- Handling slow data streams and partial data reception
- Read timeout values justified by API characteristics

### 3. Total Request Timeout
- Overall request lifecycle management with cancellation and cleanup procedures
- Total timeout encompassing all retry attempts
- Circuit breaker integration when timeout rates exceed thresholds

For each layer, provide:
- Recommended timeout values with justification
- Error handling patterns as code snippets with inline explanations
- Retry logic with exponential backoff and jitter
- Resource cleanup procedures to prevent leaks
- Monitoring and alerting configurations

Include:
- Configuration examples as code blocks with detailed comments
- Edge cases: connection pool exhaustion, cascading failures, race conditions
- Summary table of recommended timeout values for different scenarios (local services 1-3s connection / 5-10s read, cross-region 3-5s connection / 15-30s read, third-party APIs 5-10s connection / 30-60s read)
- Best practices for graceful degradation and meaningful error messages

**Implementation Requirements:**
- Connection timeouts shorter than read timeouts to fail fast
- Never use infinite timeouts or system defaults
- Make timeout values configurable, not hard-coded
- Log timeout metrics for performance tuning
- Document timeout rationale for maintenance
- Resource cleanup after timeouts
- Jitter in retry logic
- Consider downstream dependencies when setting timeouts
```

## 用法 / Usage
- 必填變數 / Variables: {{language-or-framework}}、{{timeout-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Request Timeout Configuration Code Generator is a free AI prompt that produces multi-layered timeout strat…
