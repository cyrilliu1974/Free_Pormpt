# Async Job Poller With Exponential Backoff

## 簡介

The Async Job Poller With Exponential Backoff is a free AI prompt that generates production-ready polling code for software engineers building distributed systems and long-running job workflows. This async job poller prompt for ChatGPT, Claude, and Cursor produces complete, commented code that monitors job status endpoints, implements exponential backoff algorithms to reduce server load, and handles all lifecycle states including pending, processing, completed, and failed. Engineers use it to build reliable polling systems for API integrations, background task monitors, batch processing pipelines, and webhook alternatives where immediate callbacks are unavailable. Reach for this prompt when you need a polling pattern that balances responsiveness with resource efficiency, prevents infinite loops through configurable timeouts, and gracefully manages transient errors. ● Implements exponential backoff algorithms that intelligently increase polling intervals to minimize unnecessary API calls and server load. ● Handles all standard job states with extensible state transition logic and support for custom status values beyond the default lifecycle. ● Enforces configurable timeout limits and retry mechanisms to prevent infinite polling and ensure your application receives clear success or failure signals. ● Outputs fully commented code including the core polling function, state handlers, timeout enforcement, error logging, and a working usage example ready to integrate. ## Prompt

```
## Role
You are an expert software architect specializing in asynchronous job processing, distributed systems, and resilient polling patterns.

## Task
Implement a production-ready async job poller with exponential backoff, timeout management, and comprehensive error handling. The system must efficiently monitor long-running operations while minimizing server load through smart interval management.

## Context
The poller must handle job lifecycle states (pending, processing, completed, failed), prevent infinite polling through configurable timeouts, and provide clear final results or detailed error information.

## Configuration
**Language**: {{programming-language}}

**Polling parameters**: {{polling-config}}  
*Specify: status endpoint URL, initial interval (seconds), maximum timeout (seconds), and any custom job states beyond pending/processing/completed/failed*

## Output
Provide complete, commented code in properly formatted blocks:

1. Core polling function with exponential backoff algorithm
2. State transition handler for all job lifecycle states
3. Timeout enforcement and retry logic
4. Error handling with logging
5. Usage example demonstrating initialization, polling loop, and result handling
6. Configuration parameters as constants or a config object

Include inline comments explaining backoff calculation, state checks, and error scenarios.
```

## 用法 / Usage
- 必填變數 / Variables: {{polling-config}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Async Job Poller With Exponential Backoff is a free AI prompt that generates production-ready polling code…
