# Secure File Encryption Script Generator

## 簡介

The Secure File Encryption Script Generator is a free AI prompt that produces complete, production-ready encryption scripts for developers and security engineers working in high-risk data environments. This encryption script prompt for ChatGPT generates working code that implements AES-256 encryption, secure key derivation using PBKDF2 or Argon2, and HMAC-based integrity verification to detect tampering. It runs on ChatGPT, Claude, and Cursor, producing complete compression and encryption workflows with full decryption procedures, error handling for corrupted archives and wrong passwords, and clear naming conventions for encrypted outputs. Use it when you need ready-to-deploy cryptographic security code that follows industry best practices without spending hours configuring libraries and building boilerplate. Reach for this prompt when you need tested encryption implementations for file protection, secure data transfer pipelines, or compliance-driven security requirements. ● Outputs complete encryption and decryption scripts with setup instructions, dependencies, and command-line usage examples ● Implements secure key derivation functions (PBKDF2 or Argon2) and HMAC integrity checks to prevent tampering ● Includes comprehensive error handling for common failure modes like corrupted files, incorrect passwords, and missing archives ● Provides security warnings about password management and key storage to prevent implementation mistakes ## Prompt

```
## Role
You are a cryptographic security engineer with deep expertise in enterprise encryption systems and data protection for high-risk environments.

## Task
Generate complete, production-ready file compression and encryption scripts that implement cryptographic best practices. Follow industry-standard approaches: AES-256 encryption, proper key derivation (PBKDF2 or Argon2), HMAC integrity verification, and comprehensive error handling.

## Context
{{implementation-context}}

The scripts must be secure, practical, and follow principles from established cryptographic literature. Every recommendation should prioritize maximum security while remaining implementable in real-world scenarios.

## Requirements
- Complete compression and encryption workflow with working code
- Secure key derivation using PBKDF2 or Argon2
- HMAC-based integrity checks to detect tampering
- Clear naming conventions for encrypted outputs
- Full decryption procedures with error handling
- Warnings about secure password storage and key management
- Handle failure scenarios: corrupted archives, wrong passwords, missing files

## Output
Structure your response with clear section headings. Provide:

1. **Setup & Dependencies** - installation instructions and imports
2. **Encryption Script** - complete working code with inline comments
3. **Decryption Script** - complete working code with inline comments
4. **Usage Examples** - concrete command-line invocations
5. **Security Warnings** - critical password management guidance
6. **Error Handling** - how the scripts handle common failure modes

Format all technical instructions as bullet points. All code must be complete and ready to run without modification.
```

## 用法 / Usage
- 必填變數 / Variables: {{implementation-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Secure File Encryption Script Generator is a free AI prompt that produces complete, production-ready encry…
