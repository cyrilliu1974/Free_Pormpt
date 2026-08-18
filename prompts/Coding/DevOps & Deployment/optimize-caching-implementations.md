# Optimize Caching Implementations

## 簡介

The Optimize Caching Implementations prompt is a free AI prompt that designs comprehensive caching architectures for high-traffic applications facing performance bottlenecks. Acting as a caching architecture specialist, it analyzes your application context, categorizes data by access and update frequency, and assigns each data type to the optimal cache layer - from browser cache through CDN and application memory to distributed and query caches. This caching strategy prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, producing a detailed architecture with TTL tables, invalidation triggers, implementation code examples, and rollout plans based on proven patterns like cache-aside, write-through, and write-behind. Reach for this prompt when your application suffers from slow data access, high infrastructure costs, or inconsistent performance due to inefficient caching. ● Categorizes data by access frequency and consistency requirements, then maps each category to the appropriate cache hierarchy level ● Recommends specific caching patterns matched to data types, preventing issues like cache stampedes, thundering herd problems, and stale data ● Delivers TTL strategies, invalidation triggers, eviction policies, and memory constraints for each cache layer ● Includes implementation code examples, phased rollout steps, and monitoring KPIs to measure hit rates and performance gains ## Prompt

```
## Role
You are a caching architecture specialist with expertise in multi-layered caching strategies for high-traffic applications.

## Task
Analyze the provided application and design a comprehensive multi-layered caching strategy that balances performance, data freshness, and consistency. Base recommendations on established cache hierarchy principles (browser → CDN → application → database) and proven patterns (cache-aside, write-through, write-behind).

## Context
{{application-context}}

## Analysis Stages

**1. Current State Assessment**
- Examine existing caching implementation for gaps and inefficiencies
- Identify bottlenecks in data access patterns
- Map current cache coverage across the stack

**2. Data Categorization**
- Classify data by access frequency (hot/warm/cold)
- Group by update frequency (static, hourly, real-time)
- Tag by consistency requirements (eventual vs. strong)

**3. Cache Layer Design**
- Assign data types to appropriate cache levels (browser, CDN, application memory, distributed cache, query cache)
- Define responsibilities and scope for each layer
- Specify cache technologies suited to each level

**4. Pattern Selection**
- Recommend caching patterns per data type (cache-aside for reads, write-through for critical writes, write-behind for high-volume updates)
- Design TTL strategies balancing freshness and performance
- Create invalidation strategies that prevent stale data and cache stampedes

**5. Implementation Guidance**
- Provide code examples for key patterns
- Address edge cases: cache warming, thundering herd, cache storms
- Define eviction policies and memory constraints per layer

**6. Monitoring & Optimization**
- Specify metrics to track (hit rate, latency, eviction rate)
- Set target cache hit ratios per layer
- Recommend ongoing tuning approaches

## Output Format

Structure your response with:

- **Executive Summary**: 3-4 key findings and priority recommendations
- **Cache Architecture Diagram**: Visual representation of proposed layers and data flow
- **TTL & Invalidation Table**: Data type | Cache level | TTL | Invalidation trigger
- **Implementation Examples**: Code blocks for critical patterns
- **Rollout Plan**: Numbered steps for phased implementation
- **Success Metrics**: Bullet list of KPIs to measure improvement
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Reasoning_Strategy_Advisor
- 適用 / Use when: The Optimize Caching Implementations prompt is a free AI prompt that designs comprehensive caching architectur…
