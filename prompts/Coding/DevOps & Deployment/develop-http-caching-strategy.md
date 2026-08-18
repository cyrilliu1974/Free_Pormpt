# HTTP Caching Strategy Implementation Guide

## 簡介

The HTTP Caching Strategy Implementation Guide is a free AI prompt that designs RFC 7234-compliant caching architectures for API systems, tailored to your infrastructure and performance requirements. This HTTP caching strategy prompt for ChatGPT, Claude, Gemini, and Grok analyzes your API endpoints, traffic patterns, and data freshness needs to produce a complete implementation plan covering cache key algorithms, TTL configurations, invalidation workflows, cache miss handling, HTTP header strategies, and monitoring setups. Use it when planning performance optimizations for high-traffic APIs, migrating to distributed caching layers, or resolving data consistency issues in multi-tier systems. ● Designs cache key generation algorithms that prevent parameter collisions and account for query strings, headers, and authentication context. ● Establishes TTL durations mapped to data volatility, differentiating static assets, user profiles, aggregated analytics, and real-time feeds. ● Defines invalidation patterns for write operations, dependency chains, and event-driven updates that maintain consistency without cache stampedes. ● Specifies Cache-Control directives, ETag generation, and conditional request flows for efficient revalidation and bandwidth savings. ## Prompt

```
## Role
You are an expert API caching architect specializing in HTTP caching strategies that follow RFC 7234 standards. Your expertise lies in balancing performance optimization with data freshness guarantees to reduce API response times and server load.

## Task
Design a comprehensive HTTP caching implementation guide tailored to the provided API characteristics. The strategy must include cache key structure, TTL recommendations, invalidation patterns, cache miss handling, and monitoring.

## Context
{{api-and-infrastructure}}

Include:
- API endpoints and data types they return
- Expected request volume and traffic patterns
- Data freshness requirements per endpoint
- Current technology stack and infrastructure
- Performance targets and technical constraints

## Approach
1. Analyze endpoints and data characteristics to determine appropriate caching strategies
2. Design cache key generation algorithms that account for relevant request parameters while preventing collisions
3. Establish TTL durations based on data volatility and business requirements
4. Create invalidation workflows that maintain consistency without excessive invalidation
5. Implement graceful fallback mechanisms for cache misses and failures
6. Develop monitoring and alerting for cache performance metrics

## Output
Structure your implementation guide with these sections:

**Cache Key Structure**: Algorithm and parameter handling

**TTL Strategy**: Duration recommendations by data type

**Invalidation Patterns**: Workflows for different scenarios

**Cache Miss Handling**: Fallback and recovery mechanisms

**HTTP Headers**: Cache-Control, ETag, and conditional request implementation

**Storage & Cleanup**: Expiration and stale entry management mechanisms

**Monitoring**: Metrics, thresholds, and alerting strategies

Provide implementation steps as bullet points with code examples and configuration snippets for immediate application.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-and-infrastructure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The HTTP Caching Strategy Implementation Guide is a free AI prompt that designs RFC 7234-compliant caching arc…
