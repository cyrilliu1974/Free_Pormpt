# Cryptographic Code Generator Builder

## 簡介

The Cryptographic Code Generator Builder is a free AI prompt that produces production-ready React TypeScript applications for generating unpredictable, enterprise-grade secure codes in high-stakes environments like fintech and authentication systems. This code generator prompt for ChatGPT, Claude, and Cursor walks through the complete architecture of a Web Crypto API-based application, including cryptographic random generation functions, real-time entropy calculation, collision probability indicators, multi-format support, batch processing, Stripe-inspired dark UI, and CSV/JSON export with full audit trails. It replaces insecure Math.random() implementations with cryptographic standards used by companies like Stripe, Coinbase, and Auth0. Reach for this prompt when you need to build secure code generation infrastructure for account recovery tokens, two-factor authentication codes, API keys, voucher systems, or any application where weak randomness could enable fraud or account takeover. ● Implements Web Crypto API with secure random generation, entropy visualization, and collision avoidance for unpredictable code output. ● Generates a security dashboard displaying real-time entropy metrics, collision probability calculations, and strength indicators. ● Includes multi-format code generation engine with batch processing, virtualization for large volumes, and responsive progress tracking. ● Exports generation metadata with CSV/JSON formats, audit trails, and contextual security warnings for compliance documentation. ## Prompt

```
## Role

You are a cryptographic security engineer building production-ready secure code generation applications using Web Crypto API with enterprise-grade security standards.

## Context

The application must generate unpredictable, cryptographically secure codes for high-stakes environments where weak randomness could lead to account takeovers or fraud. Traditional approaches using Math.random() or timestamp-based seeds are unacceptable. The solution requires security standards used by companies like Stripe, Coinbase, and Auth0.

## Task

Build a complete React TypeScript application for secure code generation that includes:

• **Cryptographic Foundation**: Web Crypto API implementation with secure random generation functions
• **Security Dashboard**: Real-time entropy calculation, collision probability, and strength indicators
• **Code Generation Engine**: Multi-format support with collision detection and batch processing capabilities
• **Professional UI**: Stripe-inspired dark theme with security-focused UX design
• **Export System**: CSV/JSON export with generation metadata and audit trails
• **Security Education**: Contextual warnings, entropy visualization, and best practice guidance
• **Performance Optimization**: Virtualization for large batches with responsive progress indicators

## Requirements

**Code Types and Formats**: {{code-requirements}}

**Security and Compliance**: {{security-context}}

**Volume and Performance**: {{volume-requirements}}

## Output

Deliver a complete React TypeScript application with cryptographically secure implementations and zero predictability. Include all components, hooks, utility functions, and type definitions needed for immediate deployment.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-requirements}}、{{security-context}}、{{volume-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Cryptographic Code Generator Builder is a free AI prompt that produces production-ready React TypeScript a…
