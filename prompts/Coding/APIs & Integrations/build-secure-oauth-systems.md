# OAuth 2.0 Security Implementation Generator

## 簡介

The OAuth 2.0 Security Implementation Generator is a free AI prompt that produces production-ready authorization systems with defense against CSRF attacks, token leakage, open redirects, and PKCE bypass vulnerabilities for developers building secure API integrations. This OAuth 2.0 prompt for ChatGPT, Claude, and Cursor generates complete code implementing authorization code, client credentials, and implicit grant flows, each annotated with security warnings and attack-prevention explanations. It outputs encrypted token storage logic, cryptographically secure state parameter handling, redirect URI validation, rate limiting, monitoring hooks, and ASCII flow diagrams showing every security checkpoint. Use it when you need to build or audit OAuth systems that must withstand sophisticated attacks and comply with RFC 6749 specifications. 0 Security Implementation Generator: it is a tested, ready-to-run security-focused code prompt for ChatGPT, Claude, and Cursor that delivers threat models, defensive code patterns, and deployment checklists preventing the most commonly exploited OAuth vulnerabilities. ● Threat modeling that explains which attack chains each security measure breaks and why misconfigurations lead to breaches ● Grant type implementations with explicit warnings about appropriate use cases and common pitfalls for authorization code, client credentials, and implicit flows ● Token management code covering encryption requirements, rotation strategies, expiration handling, and secure storage preventing leakage ● CSRF-proof state parameter logic using cryptographically secure random generation, plus redirect URI validation blocking open redirect attacks ● Security-safe error handling that fails closed without exposing attack surface information, plus rate limiting and suspicious activity detection hooks ● Production deployment checklist in checkbox format verifying every security control before launch ## Prompt

```
## Role
You are a security implementation architect specializing in OAuth 2.0 authorization systems, approaching every implementation from an attacker's perspective and prioritizing threat modeling and defense against common vulnerabilities.

## Task
Build a production-ready, RFC 6749-compliant OAuth 2.0 authorization system for {{application-context}}. The implementation must be secure by design, preventing CSRF attacks, token leakage, open redirects, insufficient entropy, and PKCE bypass vulnerabilities.

## Context
Most OAuth implementations fail due to misconfigurations exploited by sophisticated actors who target token handling flaws, redirect URI validation gaps, and insufficient randomness. Treat security as the primary requirement.

## Requirements
- Implement authorization code, client credentials, and implicit grant types with clear security warnings about appropriate use cases
- Secure token storage with encryption requirements and rotation strategy
- Cryptographically secure state parameter implementation preventing CSRF
- Redirect URI validation preventing open redirect attacks
- Error handling that never leaks security information
- Rate limiting and monitoring hooks for suspicious activity detection
- PKCE implementation for public clients

## Output
Deliver production-ready code with:

1. **Threat Model**: Explain the specific vulnerabilities this implementation prevents and the attack chains it breaks

2. **Complete OAuth 2.0 Flow**: Include inline security annotations explaining why each defensive measure exists

3. **Grant Type Implementations**: Provide code for authorization code, client credentials, and implicit flows with warnings about when each should and should NOT be used

4. **Token Management**: Detail storage strategy, encryption requirements, expiration handling, and refresh token rotation

5. **State Parameter Logic**: Show CSRF prevention with cryptographically secure random generation and validation

6. **Security-Safe Error Handling**: Demonstrate responses that fail safely without revealing attack surface information

7. **Monitoring Integration**: Include rate limiting implementation and hooks for logging suspicious patterns

8. **ASCII Flow Diagram**: Visualize the complete authorization process showing security checkpoints

9. **Deployment Security Checklist**: Provide checkbox-formatted verification steps for production readiness

Use clear section headers, syntax-highlighted code blocks, and markdown blockquotes to highlight security-critical warnings. Comments should explain not just what the code does but what attacks it prevents.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The OAuth 2.0 Security Implementation Generator is a free AI prompt that produces production-ready authorizati…
