# API Integration Code Generator

## 簡介

The API Integration Code Generator is a free AI prompt that produces production-ready JavaScript for RESTful API integrations with authentication, error handling, and retry logic for developers building distributed systems. It generates complete code modules that handle rate limits, token expiration, network failures, and unpredictable API behavior, making it a practical API integration prompt for ChatGPT, Claude, and Cursor that goes beyond boilerplate to address real-world deployment challenges. The prompt delivers structured code with base configuration, authentication layers, differentiated error types, exponential backoff retry mechanisms, response validation, and usage examples. Reach for this prompt when you need to integrate third-party APIs into production applications where reliability and maintainability matter more than speed of initial implementation. ● Implements secure authentication headers with token refresh logic for expired credentials. ● Adds retry mechanisms with exponential backoff for transient network failures and rate limit handling. ● Generates differentiated error handling that distinguishes between network errors, authentication failures, and API-specific errors. ● Includes request/response interceptors, loading state management, and response validation against expected data structures. ## Prompt

```
## Role
You are an API integration architect specializing in production-grade RESTful integrations that handle rate limits, network failures, token expiry, and unpredictable API behavior.

## Task
Generate production-ready JavaScript code that implements a robust RESTful API integration with comprehensive error handling, authentication, retry logic, and graceful degradation.

## Context
{{api-details}}

Assume the API operates in an unreliable environment where requests may fail, tokens expire mid-flight, and transient errors occur. The code must be maintainable, well-commented, and ready for immediate deployment.

## Requirements
- Use the HTTP client specified in the API details (fetch or axios)
- Implement proper HTTP methods with correct request formatting
- Include secure authentication headers for the specified auth method
- Add comprehensive error handling that distinguishes network errors, auth failures, and API-specific errors
- Implement retry logic with exponential backoff for transient failures
- Parse and validate response data against the expected structure
- Manage loading states for frontend integration
- Use request/response interceptors where appropriate
- Maintain clear separation of concerns

## Output
Structure the code with:

1. **Base Configuration** – API client setup with base URL, default headers, and timeout settings
2. **Authentication Layer** – Secure header injection and token refresh logic
3. **Request Methods** – Functions for each required HTTP verb with proper body formatting
4. **Error Handling** – Differentiated error types with actionable messages
5. **Retry Mechanism** – Exponential backoff for failed requests
6. **Response Processing** – Validation and parsing logic
7. **Usage Examples** – Sample calls demonstrating the integration

Include inline comments explaining critical integration decisions, error boundaries, and why specific patterns were chosen.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The API Integration Code Generator is a free AI prompt that produces production-ready JavaScript for RESTful A…
