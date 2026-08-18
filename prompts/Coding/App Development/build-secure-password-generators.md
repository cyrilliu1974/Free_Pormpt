# Secure Password Generator App Builder

## 簡介

The Secure Password Generator App Builder is a free AI prompt that produces a production-ready React TypeScript application for generating cryptographically secure passwords using the Web Crypto API. This password generator prompt for ChatGPT, Claude, and Cursor outputs complete application code with enterprise-grade security features, including proper entropy implementation, resistance to dictionary attacks and rainbow tables, and defenses against GPU-accelerated brute force attempts. You supply your app requirements - design aesthetic, target users, deployment environment, compliance needs (NIST, SOC 2), and priority features like batch generation or export options - and receive a structured implementation plan followed by fully functional code. Real use cases include building authentication tools for enterprise software, creating security utilities for developer portfolios, and deploying password generators for team workflows. Reach for this prompt when you need a secure, accessible password generator application without building cryptographic infrastructure from scratch. ● Delivers React component architecture with state management, data flow optimization, and rendering strategies tailored to your requirements. ● Implements Web Crypto API for high-entropy password generation with documented attack resistance and security best practices. ● Includes responsive UI with theme support, animations, real-time customization controls, strength meters, and password history management. ● Provides accessibility features including keyboard navigation, ARIA support, error handling, and export functionality ready for deployment. ## Prompt

```
## Role

You are a security engineer and frontend developer specializing in authentication systems for high-security environments.

## Task

Build a complete React TypeScript password generator application that produces cryptographically secure passwords using the Web Crypto API, resistant to dictionary attacks, rainbow tables, and GPU-accelerated brute force attempts.

## Context

{{app-requirements}}

Include design aesthetic, target users, deployment environment, security compliance needs (e.g., NIST, SOC 2), and priority features such as batch generation, export options, password history, accessibility requirements, and any constraints.

## Output

Provide a complete, production-ready implementation structured as:

### Architecture & Component Planning
- React component structure and state management approach
- Data flow and rendering optimization strategy

### Cryptographic Security Implementation
- Password generation using Web Crypto API with proper entropy
- Security best practices and attack resistance measures

### Modern UI/UX Design
- Responsive interface with theme support and smooth animations
- Visual feedback and user-friendly controls

### Interactive Features
- Real-time password customization (length, character sets, complexity rules)
- Strength meter with visual indicators
- Password history management and export functionality

### Accessibility & Polish
- Keyboard navigation and ARIA support for screen readers
- Micro-interactions and comprehensive error handling

### Complete React TypeScript Code
- Single-component, deployable artifact
- All functionality integrated and ready to deploy

Present each section with detailed implementation guidance, then provide the full functional code.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Secure Password Generator App Builder is a free AI prompt that produces a production-ready React TypeScrip…
