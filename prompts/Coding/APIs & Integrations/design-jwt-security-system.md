# JWT Security Architecture Design Prompt

## 簡介

The JWT Security Architecture Design Prompt is a free AI prompt that produces a comprehensive authentication security system for developers building or hardening token-based user sessions. This JWT security prompt for ChatGPT, Claude, Gemini, and Grok outputs a multi-layered architecture covering HTTP-only cookie storage, automatic session refresh without exposing tokens to JavaScript, middleware validation patterns, security monitoring, and threat response mechanisms. It addresses real threats including XSS attacks, token theft, session hijacking, and concurrent session abuse, providing code examples tailored to your technology stack and specific security requirements. Use it when migrating away from localStorage-based token management, auditing an existing authentication system, or designing a new secure session flow from scratch. ● Produces HTTP-only cookie configurations with SameSite, Secure, Domain, and Path attributes plus necessary security headers (CSP, HSTS, X-Frame-Options). ● Designs automatic token refresh flows using access token and refresh token rotation strategies that keep sessions alive without JavaScript access to credentials. ● Builds middleware validation logic that verifies signatures, checks expiration, attaches user context, and handles invalid or expired tokens gracefully. ● Delivers threat detection rules for concurrent sessions, impossible travel, and brute force attempts, plus mechanisms to revoke compromised tokens and force re-authentication. ## Prompt

```
## Role

You are a security architect specializing in authentication systems. You design JWT implementations that eliminate client-side token exposure vulnerabilities while maintaining seamless user experience.

## Task

Design a comprehensive JWT security architecture for the provided application. Create implementation guidelines covering HTTP-only cookie storage, automatic session refresh, middleware validation, security monitoring, and threat response mechanisms.

## Context

The application handles sensitive user data and faces threats including XSS attacks, token theft, and session hijacking. Previous implementations failed due to client-side token management creating exploitable attack vectors. The solution must protect against sophisticated attacks while remaining invisible to users.

{{tech-stack}}

{{security-requirements}}

## Output

Provide:

**Security Architecture**
Overall JWT design eliminating client-side vulnerabilities, explaining how components work together to prevent common attack vectors.

**HTTP-Only Cookie Implementation**
Configuration for secure cookie storage including SameSite, Secure, Domain, and Path attributes. Include necessary security headers (CSP, HSTS, X-Frame-Options).

**Session Management**
Automatic token refresh flow that maintains sessions without exposing tokens to client JavaScript. Cover access token/refresh token rotation and expiration strategies.

**Middleware Design**
Token validation middleware that verifies signatures, checks expiration, and attaches user context to requests. Include error handling for invalid/expired tokens.

**Threat Detection & Response**
Monitoring for suspicious activity (concurrent sessions, impossible travel, brute force). Mechanisms to revoke compromised tokens and force re-authentication.

**Code Examples**
Implementation snippets for the specified technology stack covering cookie setup, middleware, refresh endpoints, and logout flows.

**Security Testing**
Verification strategies including penetration testing approaches, automated security scans, and validation checklists for XSS resistance and token security.

**Deployment Checklist**
Step-by-step pre-production verification ensuring all security measures are correctly configured.

Focus on actionable technical solutions with specific configurations. Address common pitfalls and their prevention.
```

## 用法 / Usage
- 必填變數 / Variables: {{security-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The JWT Security Architecture Design Prompt is a free AI prompt that produces a comprehensive authentication s…
