# Network Performance Optimization Prompt

## 簡介

The Network Performance Optimization Prompt is a free AI prompt that analyzes network architecture and delivers concrete code implementations to reduce latency for DevOps engineers and infrastructure teams. This network performance optimization prompt for ChatGPT identifies bottlenecks across DNS lookup times, TCP handshake overhead, TLS negotiation costs, and payload transfer inefficiencies, then provides production-ready code for connection pooling, request multiplexing, header compression, protocol selection, and CDN architecture. It runs on ChatGPT, Claude, Gemini, and Grok, generating executive summaries, prioritized optimization strategies with expected latency improvements in milliseconds, monitoring metrics, and sequenced implementation roadmaps. Teams use it to diagnose request patterns, eliminate unnecessary round trips, optimize HTTP/1.1, HTTP/2, and HTTP/3 deployments, and build measurable performance improvements into high-traffic systems. Reach for this prompt when you need to reduce latency in production environments where response time directly impacts user experience and business outcomes. ● Identifies critical bottlenecks in DNS resolution, TCP/TLS negotiation, and payload transfer with specific latency cost breakdowns. ● Delivers production-ready code for connection reuse, request multiplexing, compression strategies, and protocol upgrades. ● Provides monitoring metrics and validation tools to measure each optimization's real-world impact. ● Includes prioritized implementation roadmaps that sequence changes by impact versus effort for practical rollout. ## Prompt

```
## Role

You are a network performance optimization specialist with expertise in DNS resolution, TCP/TLS optimization, HTTP protocols (HTTP/1.1, HTTP/2, HTTP/3), payload compression, CDN architecture, connection pooling, and request batching.

## Task

Analyze the provided network architecture and deliver a comprehensive latency reduction plan with concrete code implementations and measurable performance improvements.

## Context

**Network Architecture:**
{{network-architecture}}

**Performance Goals:**
{{performance-goals}}

## Analysis Requirements

Identify bottlenecks across DNS lookup times, TCP handshake overhead, TLS negotiation costs, and payload transfer inefficiencies. Examine request patterns for unnecessary round trips and batching opportunities. Evaluate current compression strategies and protocol selection effectiveness.

Design solutions addressing connection reuse and pooling, request multiplexing, header and payload compression, protocol selection optimization, CDN leverage and edge computing, and request batching.

## Output

Structure your response with:

1. **Executive Summary**: Top 3-5 critical bottlenecks and expected cumulative latency reduction
2. **Optimization Sections** (one per strategy):
   - Problem statement
   - Concrete code implementation (production-ready)
   - Expected latency improvement (milliseconds or percentage)
   - Implementation priority (High/Medium/Low)
3. **Monitoring & Validation**: Specific metrics and tools to measure each improvement
4. **Implementation Roadmap**: Sequenced rollout plan based on impact vs effort
```

## 用法 / Usage
- 必填變數 / Variables: {{network-architecture}}、{{performance-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Network Performance Optimization Prompt is a free AI prompt that analyzes network architecture and deliver…
