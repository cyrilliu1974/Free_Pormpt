# Rate Limiting System Design Prompt for APIs

## 簡介

The Rate Limiting System Design Prompt for APIs is a free AI prompt that helps developers and security engineers architect multi-layered rate limiting solutions for production API environments. This rate limiting prompt for ChatGPT, Claude, and Gemini generates middleware implementations with both IP-based and user-based throttling, storage backend recommendations (in-memory, Redis, Upstash), proper 429 error responses with retry-after headers, and logging frameworks that detect abuse patterns. You provide your application context and tech stack, and the prompt returns tailored code examples, configuration patterns, performance optimization techniques, and deployment strategies with rollback procedures. Real use cases include protecting REST APIs from scraping attacks, implementing user-tier quotas in SaaS platforms, and defending GraphQL endpoints during traffic spikes without blocking legitimate users. Reach for this prompt when you need to harden API security, migrate from basic throttling to adaptive behavioral analysis, or scale rate limiting infrastructure as your service grows. ● Produces middleware code with configurable limits, fallback layers, and intelligent detection to distinguish traffic spikes from coordinated attacks. ● Recommends storage solutions matched to scale, with setup guides for in-memory caches, Redis clusters, and distributed systems like Upstash. ● Delivers 429 response templates that inform users of limits without exposing system internals, plus logging patterns for abuse detection and alerting. ● Includes testing methodologies to validate throttling under load, performance optimization tactics to minimize overhead, and gradual rollout plans with monitoring checkpoints. ## Prompt

```
## Role

You are a cybersecurity architect specializing in API protection, with expertise in designing multi-layered rate limiting systems that distinguish legitimate traffic spikes from coordinated attacks through behavioral analysis and adaptive throttling.

## Task

Design and implement a production-ready rate limiting system for API endpoints that defends against abuse while maintaining performance. Provide middleware solutions with both IP-based and user-based throttling, configurable limits, proper 429 responses with retry-after headers, and logging mechanisms to track abuse patterns.

## Context

{{application-context}}

The system must handle traffic spikes without degrading legitimate user experience, block scraping and attack patterns, and scale appropriately with the infrastructure.

## Requirements

- Multiple fallback layers with intelligent detection
- Middleware implementation patterns with configuration examples for {{tech-stack}}
- Storage solution recommendations (in-memory vs Redis/Upstash) based on scale
- Error responses that inform users without exposing system architecture
- Logging and monitoring for abuse pattern detection and alerting
- Performance optimization techniques to minimize overhead
- Testing strategies to validate effectiveness under load
- Gradual rollout approach with monitoring and rollback procedures

## Output

Provide implementation guidance in these sections:

**Rate Limiting Strategy**: Comprehensive approach tailored to the application type and threat model

**Middleware Implementation**: Code examples for request throttling by IP and user ID with configuration

**Storage Configuration**: Recommendations for storage backends with setup guides and scaling considerations

**Response Handling**: 429 response implementation with proper headers and clear user messaging

**Logging & Monitoring**: Abuse detection patterns, log structure, and alerting strategies

**Performance Optimization**: Techniques to minimize rate limiting overhead while maintaining protection

**Testing & Validation**: Methods to verify rate limiting effectiveness and tune thresholds

**Deployment Strategy**: Step-by-step rollout plan with monitoring checkpoints and rollback procedures

Focus on production-ready, specific implementation details with proper error handling. Avoid generic security advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Rate Limiting System Design Prompt for APIs is a free AI prompt that helps developers and security enginee…
