# API Error Handling System Design Prompt

## 簡介

The API Error Handling System Design Prompt is a free AI prompt that builds RFC 7807-compliant error standardization systems for development teams integrating third-party APIs. This error handling prompt for ChatGPT, Claude, Gemini, and Grok analyzes your API integration details and produces complete documentation including error mapping tables, production-ready parser code, hierarchical exception classes, before-and-after transformation samples, and integration guides. Teams use it to convert cryptic API responses from payment processors, shipping providers, or SaaS platforms into consistent, debuggable error objects that preserve original context while presenting clear messages to both end users and developers. It adapts to JSON, XML, or mixed response formats and handles malformed data gracefully. Reach for this prompt when you need to standardize error handling across multiple APIs, migrate legacy integrations to RFC 7807, or onboard a new third-party service with unpredictable error formats. ● Maps arbitrary API error structures to RFC 7807 fields (type, title, status, detail, instance) with custom extension fields for API-specific metadata. ● Produces hierarchical exception architectures that categorize error codes, preserve original context, and include correlation IDs for monitoring systems. ● Delivers parser implementations in your target language that handle malformed responses, missing fields, and unexpected formats without breaking. ● Creates dual-layer error messages: human-readable descriptions with next steps for end users, plus technical details and debugging metadata for developers. ## Prompt

```
## Role

API integration architect specializing in resilient error handling and RFC 7807 standardization.

## Task

Design a comprehensive error standardization system that transforms inconsistent third-party API errors into RFC 7807 Problem Details format. Your system must:

**Analyze & Map**
Parse the provided API error structures and map them to RFC 7807 fields (type, title, status, detail, instance). Design extension fields for API-specific metadata.

**Exception Architecture**
Build a hierarchical exception system that maps error codes to specific types, preserves original context, provides meaningful messages, and includes debugging metadata.

**Parser Implementation**
Implement robust parsing logic that handles malformed responses gracefully, extracts information from various formats, falls back intelligently when data is missing, and logs parsing failures.

**User Feedback Design**
Create dual-layer error messages: clear descriptions with actionable next steps for end users, plus technical details and correlation IDs for developers.

## Context

{{api-integration-details}}

*Provide: API error codes and descriptions, sample error response structures (JSON/XML/etc.), target programming language, logging/monitoring system in use, and user audience technical levels.*

## Output

Deliver structured documentation with:

- **Error mapping tables**: Original format → RFC 7807 transformation with field-by-field breakdown
- **Parser implementation**: Production-ready code examples in the target language
- **Exception hierarchy**: Class/type diagrams showing inheritance, categorization, and error code ranges
- **Before/after samples**: Real error responses demonstrating the transformation
- **Integration guide**: Step-by-step implementation with existing codebase integration points
- **Test scenarios**: Edge cases covering malformed responses, missing fields, unexpected formats, and null values

**Requirements:**

*Must have:* Strict RFC 7807 compliance, resilience to malformed/unexpected responses, preserved original error data for debugging, minimal parsing overhead, easy extensibility for new APIs and error types.

*Avoid:* Over-engineering simple error cases, rigid mappings that break with minor API changes, exposing sensitive technical details to end users, losing original error context during transformation.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-integration-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The API Error Handling System Design Prompt is a free AI prompt that builds RFC 7807-compliant error standardi…
