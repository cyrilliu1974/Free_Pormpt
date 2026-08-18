# Webhook Signature Verification Code Generator

## 簡介

The Webhook Signature Verification Code Generator is a free AI prompt that produces secure, production-ready code to authenticate webhook payloads and prevent tampering, replay, and timing attacks for developers building API integrations. This webhook signature verification prompt for ChatGPT, Claude, and Cursor generates complete HMAC-based verification functions that follow the security patterns of Stripe, GitHub, and other major platforms. It outputs code with inline comments explaining each cryptographic decision, constant-time string comparison to prevent timing attacks, timestamp validation to block replay attacks, and error handling that avoids leaking security information. Real use cases include validating incoming webhooks from payment processors, third-party APIs, and any service that signs HTTP callbacks. Reach for this prompt when you need to implement or audit webhook verification logic in any language and want code that handles edge cases like missing headers, malformed signatures, and expired timestamps. ● Outputs HMAC-SHA256 signature reconstruction and constant-time comparison to prevent both tampering and timing side-channel attacks. ● Includes configurable timestamp tolerance windows and replay-attack prevention logic. ● Generates usage examples showing how to extract and verify raw request bodies in webhook handlers. ● Lists common implementation pitfalls developers encounter, such as comparing strings with standard equality operators or parsing JSON before verification. ## Prompt

```
## Role
You are a security implementation specialist focused on webhook signature verification.

## Task
Generate production-ready webhook signature verification code that implements HMAC-based cryptographic signing to prevent tampering and replay attacks, following security patterns used by Stripe and GitHub.

## Context
The system needs webhook signature verification to protect against:
- **Tampering attacks**: unauthorized modification of webhook payloads
- **Replay attacks**: reuse of captured legitimate webhooks
- **Timing attacks**: exploitation of string comparison timing differences

The code must be secure against common vulnerabilities while remaining maintainable.

## Security Requirements
1. Use HMAC-based cryptographic signing for payload authentication
2. Implement constant-time string comparison to prevent timing attacks
3. Include timestamp validation with configurable tolerance window
4. Verify signatures against raw request body (exact byte match)
5. Provide error messages that don't leak security information
6. Handle edge cases: missing headers, malformed signatures, expired timestamps
7. Avoid pitfalls: standard string comparison, ignoring replay protection

## Output
Provide the implementation in this structure:

**Security Overview**
Brief explanation of why webhook signature verification is critical and the attack vectors it prevents.

**Main Verification Function**
Complete function with detailed inline comments explaining each security decision, including:
- Signature reconstruction using HMAC
- Constant-time comparison implementation
- Timestamp validation for replay prevention
- Proper error handling for common failure scenarios

**Helper Functions** (if needed)
Any supporting utilities required by the main function.

**Usage Example**
Clear integration example showing how to use the verification function in a webhook handler, demonstrating proper raw body handling.

**Common Mistakes to Avoid**
List of implementation pitfalls developers frequently encounter.

Format all code with proper syntax highlighting for {{programming-language}}. Use {{webhook-config}} to configure the signing secret and timestamp tolerance (in seconds, typically 300 for 5 minutes). Ensure the implementation works with raw request bodies.
```

## 用法 / Usage
- 必填變數 / Variables: {{programming-language}}、{{webhook-config}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Webhook Signature Verification Code Generator is a free AI prompt that produces secure, production-ready c…
