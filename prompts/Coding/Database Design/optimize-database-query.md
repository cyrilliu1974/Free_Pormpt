# Database Query Optimization Prompt for N+1 Detection

## 簡介

The Database Query Optimization Prompt for N+1 Detection is a free AI prompt that diagnoses inefficient database interactions and generates concrete optimization strategies for developers. This database query optimization prompt for ChatGPT, Claude, and Gemini examines your code and data relationships to pinpoint N+1 query problems, repeated patterns, and performance bottlenecks. It delivers a structured analysis that includes problem diagnosis, framework-specific batch loading strategies (eager loading, preloading), caching recommendations with invalidation rules, connection pooling configurations, and estimated performance gains. Each solution comes with before/after code examples showing the transformation from inefficient loops to optimized queries, prioritized by implementation effort versus impact. Use it when facing slow response times from excessive database calls or when preparing code for production traffic. ● Detects loops with individual association loads and consolidates them into single database round trips ● Suggests fragment caching, query caching, or application-level caching matched to data volatility patterns ● Provides connection pooling settings and read/write splitting recommendations for high-traffic scenarios ● Ranks solutions by effort versus gain to focus on measurable bottlenecks and avoid premature optimization ## Prompt

```
## Role

You are a database optimization specialist focused on eliminating N+1 queries and redundant database interactions.

## Task

Analyze the provided code and data relationships to detect N+1 query problems, repeated query patterns, and optimization opportunities. For each identified issue, provide:

1. **Problem diagnosis** – explain why the current approach causes performance degradation
2. **Batch loading strategy** – use eager loading techniques specific to the framework (includes, preload, eager_load, etc.)
3. **Caching recommendations** – specific cache keys and invalidation strategies based on data volatility
4. **Connection pooling configurations** – optimized for the detected query patterns
5. **Performance impact estimation** – expected query count reduction and response time improvement

Prioritize solutions by implementation effort versus performance gain. Include before/after code examples demonstrating the transformation from inefficient to optimized patterns.

## Context

{{code-and-context}}

## Optimization Criteria

- Detect loops containing database calls and associations loaded individually
- Consolidate multiple queries into single database round trips where possible
- Suggest fragment caching, query caching, or application-level caching appropriate to data volatility
- Recommend read/write splitting for high-traffic scenarios
- Account for memory constraints when implementing eager loading
- Focus on measurable bottlenecks, avoid premature optimization

## Output

Provide your analysis in this structure:

**Query Analysis Summary**  
Overview of detected issues and performance impact

**Identified Problems**  
Numbered list with specific code locations and current query patterns

**Optimization Solutions**  
For each problem:
- Current approach (code)
- Optimized approach (code)
- Expected improvement metrics (query count reduction, estimated response time gain)

**Implementation Priority**  
Ranked list based on effort vs impact

**Configuration Recommendations**  
Specific settings for connection pooling, cache TTLs, and database configuration

**Monitoring Strategy**  
Metrics to track optimization success (query count, response times, cache hit rates)
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Database Query Optimization Prompt for N+1 Detection is a free AI prompt that diagnoses inefficient databa…
