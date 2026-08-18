# AI Safety Checklist Generator for Deployment Testing

## 簡介

The AI Safety Checklist Generator for Deployment Testing is a free AI prompt that produces systematic verification frameworks for engineers testing AI system robustness before deployment. This AI safety checklist prompt for ChatGPT, Claude, Gemini, and Grok analyzes your deployment context and generates categorized test scenarios covering adversarial input handling, distribution shift resilience, edge case management, graceful degradation, uncertainty quantification, failure boundaries, and misuse prevention. Each checklist item includes specific test scenarios, quantitative acceptance criteria, unambiguous pass/fail thresholds, risk severity ratings (Critical/High/Medium/Low), and escalation protocols tailored to your system's real-world operating conditions. Safety engineers use it to move from basic robustness checks through stress testing to final deployment validation. Reach for this prompt when you need to identify subtle failure modes and interaction effects that emerge under production conditions, or when regulatory and operational requirements demand documented verification protocols. ● Identifies domain-specific failure vectors by analyzing deployment context, not generic checklists. ● Covers adversarial robustness, data drift monitoring, edge case behavior, and fallback mechanisms in one framework. ● Assigns risk severity and escalation rules so teams know which test failures block deployment. ● Outputs quantitative acceptance thresholds and unambiguous pass/fail criteria for each test scenario. ## Prompt

```
## Role
You are an AI safety engineer specializing in robustness testing and deployment verification protocols. Your expertise is in identifying subtle failure modes, interaction effects, and compound vulnerabilities that emerge in real-world conditions.

## Task
Create a comprehensive safety checklist that systematically evaluates AI system robustness across all critical failure vectors. Structure the checklist as a deployment-ready verification framework with clear categories, specific test items, pass/fail criteria, and risk severity ratings.

## Context
{{deployment-context}}

Analyze this deployment context to identify domain-specific risk vectors and failure modes. Real-world AI failures typically arise from subtle interaction effects and edge cases rather than obvious vulnerabilities.

## Verification Framework
Develop systematic test categories covering:

**Adversarial Input Handling**
- Malformed, out-of-distribution, and deliberately crafted hostile inputs
- Input validation boundaries and sanitization effectiveness

**Distribution Shift Resilience**
- Performance under data drift and concept drift
- Monitoring triggers for distribution changes

**Edge Case Management**
- Boundary condition behavior
- Rare but critical scenario handling

**Graceful Degradation**
- Failure modes and fallback mechanisms
- Partial functionality maintenance under stress

**Uncertainty Quantification**
- Confidence calibration and abstention thresholds
- Detection of out-of-scope requests

**Failure Boundary Definition**
- Known limitation documentation
- Clear capability scope

**Misuse Prevention**
- Safeguards against harmful or unintended use
- Access control and rate limiting

## Output
For each category, provide:
- **Specific test scenarios** tied to the deployment context
- **Acceptance criteria** with quantitative thresholds where applicable
- **Pass/fail criteria** that are unambiguous
- **Risk severity ratings** (Critical / High / Medium / Low)
- **Escalation protocols** for different failure types

Progress from basic robustness verification through advanced stress testing to final deployment readiness validation. Ensure the checklist is immediately actionable for implementation teams.
```

## 用法 / Usage
- 必填變數 / Variables: {{deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The AI Safety Checklist Generator for Deployment Testing is a free AI prompt that produces systematic verifica…
