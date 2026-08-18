# Email Service Architecture Design Prompt

## 簡介

The Email Service Architecture Design Prompt is a free AI prompt that generates enterprise-grade transactional email system implementation strategies for developers and infrastructure engineers. This email service architecture prompt for ChatGPT, Claude, Gemini, and Grok produces a step-by-step technical guide tailored to your provider (SendGrid, Mailgun, AWS SES), tech stack, and volume requirements. It covers SMTP/API integration patterns, HTML template systems with variable interpolation, retry logic, logging, delivery tracking, SPF/DKIM/DMARC configuration, rate limiting, and troubleshooting protocols. Real use cases include building transactional email pipelines for SaaS authentication flows, notification systems, and customer communication platforms that demand high deliverability and sender reputation management. Reach for this prompt when you need to architect or audit an email service layer that handles edge cases, scales under load, and meets modern spam filter requirements. ● Produces provider-specific integration guidance for SendGrid, Mailgun, AWS SES, and other major email platforms with code examples and configuration snippets. ● Designs HTML template systems with dynamic variable interpolation, error handling with intelligent retry strategies, and logging architectures for visibility. ● Addresses SPF, DKIM, and DMARC security setup, rate limiting to protect sender reputation, and troubleshooting workflows for common delivery failures. ● Accounts for scalability under high volume, edge case handling, and modern spam filter sophistication to maintain inbox placement rates. ## Prompt

```
## Role

You are an expert email infrastructure architect specializing in transactional email systems that achieve enterprise-grade deliverability, template management, error handling, and tracking.

## Task

Design a comprehensive email service implementation strategy tailored to the provided technology stack and requirements. Deliver a step-by-step implementation guide covering:

- SMTP/API integration with the specified email service provider
- HTML template system with dynamic variable interpolation
- Robust error handling with intelligent retry logic
- Comprehensive logging and monitoring
- Delivery confirmation tracking
- Configuration recommendations for deliverability optimization
- Security considerations (SPF, DKIM, DMARC)
- Rate limiting strategies
- Troubleshooting protocols for common failure scenarios

Address edge cases, scalability under load, and sender reputation management. Account for modern spam filter sophistication and the high stakes of email delivery failures.

## Context

{{email-service-setup}}

*Include: email service provider (SendGrid, Mailgun, AWS SES, etc.), programming language and framework, expected volume (emails per day/month), email types needed (welcome, password reset, notifications, etc.), and hosting/server environment.*

## Output

Structure your response with clear section headings. Provide technical implementation details in bullet points with code examples and configuration snippets where applicable.
```

## 用法 / Usage
- 必填變數 / Variables: {{email-service-setup}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Email Service Architecture Design Prompt is a free AI prompt that generates enterprise-grade transactional…
