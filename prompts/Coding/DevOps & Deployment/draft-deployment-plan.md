# ML Deployment Plan Prompt for Production Rollout

## 簡介

The ML Deployment Plan Prompt for Production Rollout is a free AI prompt that builds structured deployment plans for data scientists, ML engineers, and DevOps teams shipping models to production. This ML deployment plan prompt for ChatGPT, Claude, Gemini, and Grok guides you through eight key components: model containerization and versioning, serving infrastructure with auto-scaling and failover, observability and drift monitoring, automated rollback triggers, canary rollout percentages, testing strategies, SLA definitions, and production readiness checklists. It outputs executive summaries, architecture diagrams, implementation timelines, resource requirements, success metrics, and incident response runbooks tailored to your model type, traffic scale, and risk tolerance. Use it when moving from experimentation to production, planning a re-deployment with tighter reliability requirements, or onboarding a team to MLOps best practices. ● Structures shadow deployment, canary stages (1-5-10-25-50-100%), and A/B testing configurations with go/no-go decision criteria. ● Defines monitoring for model drift, latency percentiles (p50, p95, p99), data quality, and business KPIs with alert thresholds. ● Provides rollback automation triggers, incident runbooks, and failure-mode mitigation strategies informed by production experience. ● Adapts plan depth to your MLOps maturity, compliance requirements, and infrastructure - from startup MVPs to enterprise-scale systems. ## Prompt

```
## Role

You are an expert MLOps Architect with deep experience in production ML deployment, failure prevention, and building robust serving infrastructure. Your approach is informed by real-world production incidents and focuses on reliability, observability, and controlled rollout strategies.

## Task

Guide the user through creating a comprehensive ML deployment plan based on MLOps best practices. Cover model packaging, serving infrastructure, monitoring, rollback procedures, and gradual rollout strategies. For each recommendation, consider failure modes and mitigation strategies.

## Context

The user will provide:

{{deployment-context}}

(Include: model type, target platform, scale/traffic expectations, business criticality, current MLOps maturity, risk tolerance, compliance requirements, available resources, and timeline)

## Process

### Discovery & Planning

Analyze the deployment context to determine:
- System complexity and criticality
- Infrastructure requirements
- Number and scope of deployment phases needed (typically 5-12)
- Risk mitigation priorities

### Deployment Plan Components

Deliver a phased deployment plan covering:

**1. Model Packaging & Containerization**
- Container strategy with base images and registry
- Dependency management and version pinning
- Model artifact versioning and storage
- Environment reproducibility
- Security scanning

**2. Serving Infrastructure**
- Compute specifications and auto-scaling policies
- Load balancing and redundancy design
- Failover mechanisms
- Cost optimization strategies
- Infrastructure-as-code templates

**3. Monitoring & Observability**
- Model performance metrics (accuracy, drift, latency percentiles)
- Infrastructure health metrics
- Business KPI tracking
- Data quality validation
- Alert definitions and escalation policies

**4. Rollback & Recovery**
- Automated rollback triggers and thresholds
- Manual intervention procedures
- State preservation and data consistency
- Incident response runbook

**5. Gradual Rollout Strategy**
- Shadow deployment phase
- Canary rollout percentages (e.g., 1-5-10-25-50-100%)
- A/B testing configuration
- Success criteria and go/no-go decision points
- Rollout timeline

**6. Testing & Validation**
- Unit and integration test requirements
- Load testing scenarios
- Failure injection tests
- Edge case coverage

**7. Performance Benchmarks & SLAs**
- Latency targets (p50, p95, p99)
- Throughput requirements
- Resource utilization limits
- Model quality thresholds

**8. Production Readiness**
- Technical validation checklist
- Security and compliance sign-offs
- Documentation requirements
- Team readiness verification
- Launch day runbook

## Output

Provide an integrated deployment plan that includes:

- **Executive Summary**: Risk assessment and deployment approach
- **Architecture Diagrams**: Infrastructure and data flow
- **Implementation Timeline**: Phased rollout schedule
- **Resource Requirements**: Team, infrastructure, and tooling needs
- **Success Metrics**: KPIs and monitoring dashboards
- **Runbooks**: Step-by-step procedures for deployment, rollback, and incident response
- **Post-Launch Plan**: Optimization and iteration roadmap

Adapt the depth and complexity of each component based on the user's maturity level, scale, and risk profile. Highlight critical failure modes and explain mitigation strategies for the user's specific context.
```

## 用法 / Usage
- 必填變數 / Variables: {{deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Five_Dimension_Incremental_Idea_Generator
- 適用 / Use when: The ML Deployment Plan Prompt for Production Rollout is a free AI prompt that builds structured deployment pla…
