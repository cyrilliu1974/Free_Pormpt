# Password Manager Implementation Plan Prompt

## 簡介

The Password Manager Implementation Plan Prompt is a free AI prompt that produces comprehensive security architecture blueprints for cybersecurity professionals and IT teams building or deploying password management systems. This password manager prompt for ChatGPT, Claude, Gemini, and Grok walks through every layer of a secure password vault: AES-256 encryption specifications, configurable password generation algorithms with entropy controls, master password handling, intuitive UI workflows that balance convenience with auto-lock and clipboard clearing, logical categorization for scaling vaults, and both local and cloud backup strategies with recovery procedures. You specify the account types to protect and your deployment environment, and the prompt returns a step-by-step implementation plan with technical recommendations for encryption, key derivation, authentication mechanisms, and synchronization. Reach for this prompt when you need a structured blueprint to evaluate vendors, guide in-house development, or document security policies for password management across teams or organizations. ● Specifies encryption standards, password generation entropy, and memory protection techniques for secure credential storage. ● Designs user workflows that make adding, retrieving, and updating passwords intuitive while maintaining auto-lock and clipboard hygiene. ● Structures organization systems with tagging, notes, and categorization that scale as the password vault grows. ● Provides backup and recovery strategies covering local, cloud, and hybrid approaches with master password loss scenarios. ## Prompt

```
## Role
You are a cybersecurity expert implementing a password manager system.

## Task
Design a secure password manager that stores and generates strong, unique passwords. Deliver a complete implementation plan covering security architecture, user interface, organization system, usage guidelines, and backup strategy.

## Context
Account types to support: {{account-types}}
Deployment environment: {{deployment-context}}

## Requirements

### Security Architecture
- Define encryption methods for password storage (AES-256 recommended unless specified otherwise)
- Specify password generation algorithms with configurable entropy levels
- Detail secure storage techniques including master password handling and memory protection
- Address key derivation and authentication mechanisms

### User Interface Design
- Create intuitive workflows for adding, retrieving, and updating passwords
- Balance accessibility with security (auto-lock, clipboard clearing, visual indicators)
- Design for the specified device types and form factors

### Organization System
- Structure account entries with clear categorization
- Enable searchable notes and tags for each password entry
- Implement logical grouping that scales as the password vault grows

### Usage Guidelines
- Provide best practices for master password creation
- Define password rotation policies by account sensitivity
- Explain security features users should enable
- Outline common pitfalls to avoid

### Backup and Recovery
- Detail the backup strategy (local, cloud, or hybrid)
- Specify recovery procedures if the master password is lost or devices fail
- Address encryption of backup files and secure synchronization

## Output
Deliver your implementation plan with clear headings for each component above. Use step-by-step numbered instructions within each section. Include specific technical recommendations where appropriate.
```

## 用法 / Usage
- 必填變數 / Variables: {{account-types}}、{{deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Password Manager Implementation Plan Prompt is a free AI prompt that produces comprehensive security archi…
