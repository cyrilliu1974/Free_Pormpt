# JWT Security Architecture Design Prompt

## 簡介

The JWT Security Architecture Design Prompt is a free AI prompt that generates production-ready authentication systems for developers building secure web applications. This JWT architecture prompt for ChatGPT, Claude, and Gemini produces complete implementation guidelines covering HTTP-only cookie storage, automatic token refresh mechanisms, server-side validation middleware, and secure logout procedures. Given your application context, it generates code examples and step-by-step deployment instructions that prevent XSS attacks, token theft, and session hijacking. Use it when migrating from vulnerable client-side token storage, hardening existing authentication flows, or building new secure login systems that handle sensitive user data. ● Generates HTTP-only cookie configurations with security headers and CSRF protection settings ● Designs automatic token refresh systems that maintain sessions without user-visible interruptions ● Produces server-side middleware patterns for token validation and user state management ● Includes comprehensive error handling for token tampering, expiration scenarios, and attack vectors ## Prompt

```
## Role

You are a security-focused authentication architect specializing in JWT implementations with expertise in server-side authentication systems that eliminate client-side token exposure.

## Task

Design a production-ready JWT security architecture that prevents XSS attacks, token theft, and session hijacking. Deliver implementation guidelines for HTTP-only cookie storage, automatic token refresh, server-side validation middleware, and secure logout procedures.

## Context

{{application-context}}

The authentication system must handle sensitive user data in an environment with active security threats. Previous client-side token management created exploitable vulnerabilities. The solution must be secure yet seamless for end users.

## Requirements

- Eliminate all client-side token exposure through HTTP-only cookie implementation
- Design automatic token refresh that maintains seamless sessions without user intervention
- Create server-side validation middleware patterns for token verification and user state management
- Implement comprehensive error handling for token tampering, expiration, and attack scenarios
- Include security headers, CSRF protection, and session management
- Provide production-ready code examples and step-by-step implementation guides
- Address common JWT security pitfalls with specific mitigation strategies

## Output

Structure your response with:

**Security Architecture Overview**  
Core principles and overall JWT implementation strategy

**HTTP-Only Cookie Implementation**  
Cookie configuration, security headers, and settings with code examples

**Automatic Token Refresh System**  
Session refresh mechanism that maintains user authentication seamlessly

**Server-Side Validation Middleware**  
Middleware patterns for token validation and user data attachment

**Secure Logout Procedures**  
Token invalidation and session cleanup implementation

**Frontend Integration**  
Clean client-side implementation that avoids token handling

**Security Monitoring & Error Handling**  
Logging, monitoring, and error handling strategies for authentication events

**Implementation Checklist**  
Step-by-step deployment checklist with security verification steps
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The JWT Security Architecture Design Prompt is a free AI prompt that generates production-ready authentication…
