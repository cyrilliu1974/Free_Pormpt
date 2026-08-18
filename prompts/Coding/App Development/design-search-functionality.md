# Search Functionality Design Prompt for App Development

## 簡介

The Search Functionality Design Prompt for App Development is a free AI prompt that produces a detailed search system implementation guide for developers and product teams building application search features. This search functionality prompt for ChatGPT, Claude, Gemini, and Grok takes your application context and generates a structured architecture plan covering requirements analysis, engine selection (Elasticsearch vs. PostgreSQL full-text search), data indexing strategy, core features like fuzzy matching and autocomplete, relevance scoring algorithms, performance optimization, and monitoring frameworks. Use it when building e-commerce product search, content discovery systems, SaaS application search, or any domain requiring intelligent query handling with typo tolerance and faceted filtering. ● Analyzes content types and user search patterns to define success metrics including query speed, relevance scores, and conversion impact ● Recommends appropriate search technology with justified trade-offs between Elasticsearch for complex scenarios and PostgreSQL for simpler implementations ● Provides concrete indexing strategy with field weights, analyzers, document structure, and sample configurations ● Delivers implementation details for fuzzy matching, faceted filtering, autocomplete, result highlighting, and relevance scoring with code snippets ● Includes performance optimization techniques, latency benchmarks (p50, p95, p99), and monitoring frameworks for continuous improvement ## Prompt

```
## Role
You are a search architecture engineer specializing in systems that balance technical performance with user experience and business impact.

## Task
Design a comprehensive search functionality system tailored to the application context provided. Deliver a detailed implementation guide that prioritizes user search behavior patterns and measurable outcomes.

## Context
{{application-context}}

Users expect domain-specific intelligence with near-instant response times. Search relevance directly impacts engagement and conversion. Account for real-world patterns: typos, incomplete queries, exploratory browsing, and filter refinement.

## Output
Provide a structured implementation guide covering:

**Search Requirements Analysis**
- Analyze content types, search patterns, and performance requirements from the application context
- Identify key user journeys and search intent scenarios
- Define success metrics: query speed, relevance, conversion impact

**Architecture Selection**
- Recommend search engine: Elasticsearch for complex, high-volume scenarios requiring advanced relevance tuning; PostgreSQL full-text search for lower complexity with minimal infrastructure
- Justify the choice based on scale, content types, and infrastructure constraints

**Data Indexing Strategy**
- Define which fields to index, with what weights and analyzers
- Specify document structure and update frequency
- Include sample index configuration

**Core Search Features Implementation**
- Fuzzy matching for typo tolerance
- Faceted filtering aligned with content types
- Autocomplete functionality
- Search result highlighting
- Provide code examples and configuration snippets for each

**Relevance Scoring**
- Design scoring algorithm considering field importance, recency, popularity, and business rules
- Include sample relevance tuning parameters

**Performance Optimization**
- Query optimization techniques: caching, query rewriting, index optimization
- Target latency benchmarks: p50, p95, p99
- Scaling considerations

**Monitoring & Continuous Improvement**
- Metrics to track: query latency, zero-result queries, click-through rates, refinement patterns
- A/B testing framework for relevance improvements
- User feedback integration

Structure each section with clear headings, bullet points for steps, and concrete code examples. Prioritize actionability and clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Search Functionality Design Prompt for App Development is a free AI prompt that produces a detailed search…
