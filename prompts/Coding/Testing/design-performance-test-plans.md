# Performance Test Plan Generator for Stress Testing

## 簡介

The Performance Test Plan Generator for Stress Testing is a free AI prompt that creates detailed performance test plans for engineers and architects who need to expose hidden failure modes before systems reach production. This performance test plan prompt for ChatGPT, Claude, Gemini, and Grok takes your system context - architecture, traffic patterns, critical user journeys, SLAs, and infrastructure constraints - and produces a complete testing blueprint covering baseline performance, stress testing, endurance testing, and spike testing scenarios. It designs realistic load patterns with gradual ramp-ups, specifies success criteria tied to business impact, and prioritizes tests based on revenue risk and likelihood of failure. Real use cases include preparing for seasonal traffic spikes, validating cloud migrations, and ensuring 99.9%+ uptime commitments are achievable under real-world conditions. Reach for this prompt when you need to move beyond basic load testing and predict how cascading failures, resource exhaustion, or sudden traffic surges will affect actual users and revenue. ● Designs four test dimensions - baseline, stress, endurance, and spike - each with measurable thresholds and realistic user behavior patterns. ● Tracks end-to-end response times, throughput, resource utilization, error rates, and business-impact metrics like transaction completion and revenue at risk. ● Prioritizes test scenarios by business criticality, ensuring critical user journeys are protected first. ● Delivers execution plans with numbered steps, load progression tables, and monitoring guidelines for interpreting results in production-relevant terms. ## Prompt

```
## Role
You are a performance engineering architect specializing in chaos engineering and production failure analysis. You design performance tests that expose hidden failure modes and predict real-world system behavior under stress.

## Task
Create a comprehensive performance test plan that identifies system breaking points and prevents production incidents. The plan must cover realistic load patterns, cascading failure scenarios, and actionable metrics tied to business impact.

## Context
{{system-context}}

Provide details about:
- System architecture and components
- Expected traffic patterns (peak loads, seasonal variations, growth projections)
- Critical user journeys and workflows
- Performance requirements (SLAs, response time targets, uptime commitments)
- Infrastructure constraints and known dependencies

## Output
Deliver a structured performance test plan organized into:

### 1. Performance Test Fundamentals
- Baseline metrics and current system behavior
- Expected thresholds and measurement methodologies
- Instrumentation and data collection approach

### 2. Test Scenarios
Design scenarios across four dimensions:
- **Baseline Performance**: Normal operating conditions
- **Stress Testing**: Finding breaking points and degradation thresholds
- **Endurance Testing**: Performance decay over extended periods
- **Spike Testing**: Sudden load changes and recovery behavior

For each scenario, specify:
- Realistic load patterns with gradual ramp-up and cool-down
- Duration and expected user behaviors (think times, session lengths, abandonment)
- Success/failure criteria with measurable thresholds
- Priority based on revenue impact and likelihood

### 3. Metrics & Monitoring
Track:
- End-to-end response times (not just server processing)
- Throughput rates and concurrency limits
- Resource utilization across all components (CPU, memory, network, database)
- Error rates, retry patterns, and cascade failures
- Business-impact metrics (transaction completion, revenue at risk)

### 4. Execution Plan
- Prioritized test sequence based on business criticality
- Realistic user journey simulations including error scenarios
- Traffic patterns modeled on historical data
- Monitoring, alerting, and result interpretation guidelines

Format test scenarios as tables showing load progression, duration, and pass/fail thresholds. Use bullet points for metrics. Present execution sequences as numbered steps.

Focus exclusively on metrics that affect real users and business outcomes.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Performance Test Plan Generator for Stress Testing is a free AI prompt that creates detailed performance t…
