# Password Manager App Builder Prompt

## 簡介

The Password Manager App Builder Prompt is a free AI prompt that generates a complete, production-ready password management application for developers building secure vault solutions. This password manager prompt for ChatGPT produces full React-TypeScript source code with zero-knowledge encryption using Web Crypto API and PBKDF2 key derivation, breach monitoring integration, and offline-first storage architecture. It outputs a vault dashboard with search and categorization, password generator with entropy calculation, multi-format support for credentials and secure notes, auto-lock session management, and responsive UI components. The prompt runs on ChatGPT, Claude, and Cursor, delivering structured code with implementation comments, security best practices documentation, and deployment instructions. Developers receive working hooks, utilities, and error handling ready to customize and deploy. Reach for this prompt when you need to build a secure password vault application from scratch with enterprise-grade cryptographic systems and intuitive user experience built in. ● Outputs complete React-TypeScript application code with Web Crypto API zero-knowledge encryption and master password authentication flows. ● Generates vault dashboard UI with search, categorization, password strength analysis, and support for credentials, cards, notes, and 2FA codes. ● Includes breach monitoring integration, password generator with entropy calculation, auto-lock session management, and offline-first data storage. ● Delivers production-ready source code with all components, hooks, utilities, implementation comments, security documentation, and setup instructions. ## Prompt

```
## Role

You are a security-focused software engineer and cryptographic systems architect.

## Task

Create a complete React-TypeScript password manager with zero-knowledge encryption, enterprise-grade security, and intuitive UI. The application must handle real-world scenarios including family sharing, breach monitoring, and offline-first operation.

## Context

{{project-requirements}}

## Output

Deliver a complete, production-ready React-TypeScript application structured as follows:

**Foundation & Cryptographic Architecture**
- Project setup with Web Crypto API implementation
- Zero-knowledge encryption system using PBKDF2 key derivation
- Master password handling and authentication flow

**Core Interface**
- Vault dashboard with search, categorization, and smooth animations
- Responsive design with intuitive navigation
- Multi-format support: passwords, credit cards, secure notes, 2FA codes

**Security Features**
- Password generator with entropy calculation
- Security strength analysis
- Breach monitoring integration
- Auto-lock and session management

**Storage & Deployment**
- Offline-first architecture with secure data migration
- Complete source code with all components, hooks, and utilities
- Implementation comments and security best practices documentation
- Error handling, performance optimization, and setup instructions

Provide working code in ready-to-deploy format.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Password Manager App Builder Prompt is a free AI prompt that generates a complete, production-ready passwo…
