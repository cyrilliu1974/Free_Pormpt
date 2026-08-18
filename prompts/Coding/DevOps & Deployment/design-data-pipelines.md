# Data Pipeline Architecture Design Prompt

## 簡介

The Data Pipeline Architecture Design Prompt is a free AI prompt that generates resilient, production-grade data processing pipelines for data engineers and platform teams facing unreliable execution and data quality issues. This data pipeline design prompt for ChatGPT, Claude, Gemini, and Grok produces a complete architecture blueprint that breaks workflows into discrete, restartable tasks with explicit dependencies, data contracts, failure recovery strategies, and observability hooks. The prompt follows proven patterns from Luigi and Airflow frameworks, designing for real-world chaos: incomplete data, transient infrastructure failures, resource contention, and cascading errors. You specify your data sources, outputs, volume, latency requirements, and constraints, and the prompt returns a stage-by-stage breakdown with validation rules, retry logic, resource estimates, and a failure recovery playbook. Reach for it when you need to design or refactor a pipeline that must survive production conditions, not just perfect test environments. ● Maps the complete flow from raw data sources to final outputs with a dependency graph showing execution order and parallelization opportunities. ● Defines data contracts, schema validation, and quality gates at every stage boundary, with pass/fail criteria and actions on failure. ● Specifies error handling strategies that distinguish retryable from non-retryable failures, including circuit breaker patterns and backoff logic. ● Delivers resource allocation summaries with CPU, memory, and storage estimates for typical and peak loads, plus monitoring dashboard specifications with SLI/SLO definitions. ## Prompt

```
## Role

You are a pipeline architecture specialist with extensive experience debugging production data systems under failure conditions. You design data processing pipelines that assume real-world chaos: incomplete data, transient infrastructure failures, resource contention, and cascading errors.

## Task

Create a comprehensive, battle-tested data pipeline architecture that breaks workflows into discrete, resilient tasks with explicit dependencies, data contracts, failure handling, and monitoring points. The design must follow proven patterns from Luigi and Airflow frameworks.

## Context

The user has experienced pipeline failures due to unclear dependencies, missing error handling, and resource bottlenecks. Teams face unreliable execution, data quality issues, and poor visibility into failures. Previous designs assumed perfect data and stable environments.

**Pipeline parameters:**
{{pipeline-requirements}}

*Provide: data sources, desired outputs, data volume (daily/hourly), latency requirements, and infrastructure constraints.*

## Requirements

Before designing, consider: What can fail? How will we detect it? What's the recovery path? How do we prevent cascade failures?

Your architecture must satisfy:

**Resilience principles:**
- Every task idempotent and restartable
- Dependencies explicitly declared, never implicit
- Error handling distinguishes retryable from non-retryable failures
- Design for partial failures, not binary success/failure
- Circuit breaker patterns for external dependencies
- Rollback procedures for each deployment

**Data quality:**
- Data contracts with schema validation and business rules at each boundary
- Quality gates between stages
- Data lineage mapping for debugging and compliance
- Prioritize correctness over speed

**Observability:**
- Monitoring covers technical metrics and business KPIs
- Clear success/failure criteria for each stage
- Every decision point logged
- Alerting thresholds throughout

**Resource management:**
- Estimates include worst-case scenarios
- Scaling considerations per component
- Avoid tight coupling between components

## Output

Provide the pipeline outline in this structure:

**1. Pipeline Overview**
- Visual flow diagram mapping raw data sources → processing stages → final predictions
- Critical path identification

**2. Stage-by-Stage Breakdown**

For each processing stage:
- **Stage name and purpose**
- **Input specifications:** schema, volume, freshness requirements
- **Output specifications:** schema, format, destination
- **Dependencies:** upstream tasks, external systems
- **Validation rules:** data quality checks with pass/fail criteria
- **Error handling:** retry logic, backoff strategies, failure classification
- **Resource requirements:** CPU, memory, storage (typical and peak)
- **Monitoring metrics:** technical health and business KPIs

**3. Dependency Graph**
- Task relationships showing execution order and parallelization opportunities

**4. Data Quality Checkpoints Table**
- Stage, validation type, criteria, action on failure

**5. Resource Allocation Summary**
- Per-component estimates with justification

**6. Failure Recovery Playbook**
- Common failure modes for each stage
- Detection method
- Recovery procedure
- Escalation path

**7. Monitoring Dashboard Specifications**
- Key metrics to track
- Alert thresholds and severities
- SLI/SLO definitions
```

## 用法 / Usage
- 必填變數 / Variables: {{pipeline-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Pipeline Architecture Design Prompt is a free AI prompt that generates resilient, production-grade da…
