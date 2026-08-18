# API Documentation Analyzer and Summary Generator

## 簡介

The API Documentation Analyzer and Summary Generator is a free AI prompt that produces comprehensive, developer-ready overviews of API documentation for software engineers and technical teams. This API documentation prompt for ChatGPT, Claude, Gemini, and Grok analyzes a specified API and delivers a structured summary covering authentication methods, key endpoints with parameters, request and response formats, rate limits, usage restrictions, and working code examples in your preferred programming language. Developers use it to quickly understand third-party APIs, onboard teammates to internal services, or audit documentation completeness before integration. It tailors technical depth to match varying experience levels, from junior developers learning REST principles to senior engineers evaluating enterprise APIs. Reach for this prompt when you need to map an unfamiliar API, document an existing service, or prepare integration guides without manually sifting through sprawling reference pages. ● Identifies all main documentation sections and authentication flows, including OAuth, API keys, and token-based methods. ● Lists key endpoints with parameters, expected payloads, and response schemas in a scannable format. ● Highlights rate limits, pagination strategies, error codes, and usage restrictions to prevent integration surprises. ● Provides working code examples of common API calls and their responses in the specified programming language. ## Prompt

```
## Role
You are an expert API documentation specialist analyzing and summarizing API structure, endpoints, and functionality for developers.

## Task
Provide a comprehensive overview of the specified API documentation covering:

1. Main sections of the documentation
2. Authentication methods required
3. Key endpoints with parameters and descriptions
4. Request and response formats
5. Rate limits and usage restrictions
6. Examples of common API calls and their responses
7. Best practices and recommendations for effective use

## Context
API: {{api-name}}
Use case: {{use-case}}
Preferred language: {{programming-language}}

## Output
Structure your analysis with clear headings, subheadings, and bullet points or numbered lists for each section. Tailor technical depth and explanations to developers with varying experience levels, ensuring accuracy and clarity throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-name}}、{{programming-language}}、{{use-case}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The API Documentation Analyzer and Summary Generator is a free AI prompt that produces comprehensive, develope…
