# Security and Reliability Code Audit Prompt

## 簡介

The Security and Reliability Code Audit Prompt is a free AI prompt that performs deep security vulnerability scanning and reliability analysis for developers and security engineers protecting applications from exploits and system failures. This security audit prompt for ChatGPT examines codebases line-by-line for OWASP Top 10 vulnerabilities including injection flaws, broken authentication, insecure dependencies, and misconfigurations, while simultaneously auditing for reliability weaknesses such as missing error boundaries, inadequate timeout patterns, and observability gaps. It runs on ChatGPT, Claude, and Cursor, producing a structured report with vulnerable code examples, severity ratings (Critical / High / Medium / Low), secure replacement snippets, and a prioritized remediation roadmap with effort estimates. Real use cases include pre-deployment security reviews, incident post-mortems, compliance audits, and hardening legacy systems. Reach for this prompt when you need to systematically identify attack vectors and failure points in an application before they become production incidents. ● Scans for input validation flaws, authentication weaknesses, insecure dependencies, and security misconfigurations across all user-facing surfaces. ● Identifies reliability risks including error handling deficiencies, missing health checks, race conditions, and inadequate circuit breaker patterns. ● Delivers specific vulnerable code examples paired with secure replacement snippets ready for immediate implementation. ● Produces a prioritized remediation roadmap separating quick wins from long-term hardening efforts, complete with effort estimates and alerting threshold recommendations. ## Prompt

```
## Role
You are a security and reliability engineer conducting a comprehensive vulnerability assessment and reliability audit. Assume every line of code is a potential attack vector and every system interaction is a failure point.

## Task
Analyze the provided codebase for:

- OWASP Top 10 vulnerabilities (injection flaws, broken authentication, security misconfigurations, insecure dependencies)
- Input validation weaknesses across all user-facing surfaces
- Authentication and authorization gaps
- Error handling and logging deficiencies
- System health monitoring and observability gaps
- Availability and resilience risks

For each identified issue, provide:

- Specific code examples demonstrating the vulnerability or gap
- Severity assessment (Critical / High / Medium / Low)
- Concrete remediation steps with code snippets ready for implementation
- Priority ranking for fixes

## Context
{{application-context}}

## Output
Structure your report with these sections:

### Security Vulnerabilities
- List findings organized by severity
- Include vulnerable code examples
- Provide secure replacement code

### Reliability Issues
- Identify failure points and race conditions
- Highlight missing error boundaries and retry logic
- Flag inadequate timeout and circuit breaker patterns

### Health Check Implementation
- Recommend monitoring endpoints and metrics
- Suggest alerting thresholds
- Provide sample health check code

### Remediation Roadmap
- Prioritized action items with effort estimates
- Quick wins vs. long-term hardening

Use bullet points and code blocks for maximum clarity and actionability.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Security and Reliability Code Audit Prompt is a free AI prompt that performs deep security vulnerability s…
