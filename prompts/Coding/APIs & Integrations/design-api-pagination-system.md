# API Pagination System Design Prompt

## 簡介

The API Pagination System Design Prompt is a free AI prompt that generates complete, production-ready pagination solutions for backend engineers and API integration specialists working with high-traffic applications. This API pagination prompt for ChatGPT, Claude, and Cursor analyzes your API requirements and target programming language to deliver a full implementation guide covering offset-based, cursor-based, and link-based pagination schemes. It produces working code with iterator or generator patterns that automatically fetch subsequent pages, respect rate limits, aggregate results without memory overflow, and handle edge cases like empty responses, network timeouts, and malformed data. Backend developers use it to build reliable data retrieval systems for REST APIs, third-party integrations, and microservices that must process large datasets efficiently. Reach for this prompt when you need to implement or refactor pagination logic that scales under load and recovers gracefully from failures. ● Analyzes pagination schemes (offset, cursor, link-based) and recommends the optimal retrieval pattern for your API. ● Generates iterator or generator code that automatically fetches pages, detects stopping conditions, and respects rate limits. ● Implements result aggregation strategies that combine multi-page datasets without memory overflow. ● Includes error handling for network failures, malformed responses, empty pages, and rate-limit exhaustion with retry logic. ● Provides performance optimizations such as concurrent requests (where safe), memory management, and caching strategies. ● Delivers runnable code examples in your chosen programming language with inline comments explaining every implementation decision. ## Prompt

```
## Role

You are an expert API integration specialist designing pagination solutions for high-traffic applications.

## Task

Create a complete, production-ready pagination implementation guide that handles automatic page fetching, result aggregation, error recovery, and performance optimization.

## Context

{{api-requirements}}

## Requirements

**Analysis & Architecture**
- Identify the pagination scheme (offset-based, cursor-based, or link-based) and design the optimal retrieval pattern
- Build iterator or generator patterns that automatically fetch subsequent pages while respecting rate limits
- Implement stopping conditions that accurately detect final pages or target result counts

**Implementation Components**
- Result aggregation that efficiently combines data from multiple pages without memory overflow
- Comprehensive error handling for empty pages, malformed responses, network timeouts, and rate limiting
- Performance optimizations including concurrent requests (where safe) and memory management for large datasets

**Code Delivery**
- Provide complete, runnable code examples in {{programming-language}}
- Include detailed inline comments explaining each implementation decision

## Output

Structure your response with clear section headings:

1. **Pagination Strategy Analysis** - which scheme is in use and why your approach fits
2. **Core Implementation** - complete code with the pagination handler
3. **Error Handling & Recovery** - retry logic, rate limit handling, failure modes
4. **Performance Optimizations** - concurrency, memory efficiency, caching where applicable
5. **Usage Examples** - how to call and integrate the solution

For each section, provide working code with step-by-step explanations.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-requirements}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The API Pagination System Design Prompt is a free AI prompt that generates complete, production-ready paginati…
