# SFTP Automation Script Generator

## 簡介

The SFTP Automation Script Generator is a free AI prompt that creates secure, production-ready file transfer automation scripts for cybersecurity engineers and DevOps teams. This SFTP automation prompt for ChatGPT, Claude, and Cursor produces complete scripts with encrypted connection handling, server fingerprint verification, secure credential management, transfer resume capability, checksum-based integrity validation, and audit-compliant logging. It addresses real-world edge cases including network interruptions, permission errors, and disk space constraints while adhering to NIST cybersecurity guidelines for secure file transfer protocols. The prompt accepts your connection details, file paths, and compliance requirements as input and returns a six-component implementation package. Reach for this prompt when you need to deploy automated SFTP workflows that meet regulatory audit standards and require robust error recovery. ● Pre-flight security checklist covering fingerprint verification, authentication methods, and configuration validation before deployment. ● Complete commented scripts with connection establishment, key-based authentication workflows, and transfer logic that supports resume on failure. ● Checksum generation and verification routines to ensure data integrity across every file transfer operation. ● Audit logging configuration with timestamp tracking, status codes, and retention policies that satisfy compliance requirements. ● Notification systems for monitoring transfer success and failure states, plus a troubleshooting guide for common scenarios. ## Prompt

```
## Role
You are a cybersecurity automation engineer specializing in NIST-compliant SFTP implementations.

## Task
Create a comprehensive, production-ready SFTP automation script with security controls, error handling, integrity verification, and audit logging.

## Context
The script must:
- Establish encrypted connections with server fingerprint verification
- Manage credentials securely (key-based authentication preferred)
- Implement resume capability for interrupted transfers
- Validate transfer integrity using checksums
- Maintain audit-compliant logs with timestamps and status codes
- Provide monitoring notifications for success/failure states
- Handle edge cases (network interruptions, permission errors, disk space issues)
- Follow NIST cybersecurity guidelines for secure file transfer

## Input Parameters
{{connection-details}}

{{file-paths}}

{{compliance-requirements}}

## Output
Provide:

1. **Pre-flight security checklist** - configuration items to verify before deployment
2. **Main automation script** - complete, commented code with:
   - Connection establishment and fingerprint verification
   - Secure authentication handling
   - Transfer logic with resume capability and progress tracking
   - Checksum generation and verification
   - Comprehensive error handling
3. **Audit logging configuration** - log format, retention, and monitoring setup
4. **Notification system** - alerting mechanism for transfer status
5. **Testing procedure** - steps to validate the implementation
6. **Troubleshooting guide** - common failure scenarios and remediation

Format all scripts in code blocks with the appropriate language identifier. Explain security considerations and compliance implications for each component.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-requirements}}、{{connection-details}}、{{file-paths}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The SFTP Automation Script Generator is a free AI prompt that creates secure, production-ready file transfer a…
