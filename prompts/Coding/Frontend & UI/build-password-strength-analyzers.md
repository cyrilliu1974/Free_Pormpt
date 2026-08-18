# Password Strength Analyzer Component Builder

## 簡介

The Password Strength Analyzer Component Builder is a free AI prompt that generates enterprise-grade password validation systems for security-focused frontend engineers and UX designers. This password strength analyzer prompt for ChatGPT, Claude, and Cursor produces a complete React TypeScript component with real-time entropy analysis, pattern detection for dictionary words and sequences, color-coded visual feedback, and a memory-friendly password generator that suggests secure alternatives users will actually adopt. The output includes comprehensive TypeScript types, accessibility support with keyboard navigation and screen reader announcements, performance optimization through debouncing, and integration examples. Use it when you need to move beyond basic password checkers and build validation systems that guide users toward genuinely secure passwords while explaining security flaws in clear, actionable language. ● Produces real-time validation engines that calculate entropy, detect common patterns, and score passwords against NIST and OWASP standards based on your security policy ● Generates visual feedback systems with animated progress bars, color-coded strength indicators, and explanations of what makes passwords weak or strong ● Creates intelligent password suggestion algorithms that balance memorability with security requirements and explain why each alternative is both safe and easy to remember ● Delivers full accessibility implementation including keyboard navigation, ARIA labels, screen reader support, and WCAG 2.1 AA compliance ## Prompt

```
## Role

You are an expert security-focused frontend engineer building enterprise-grade password validation systems with deep knowledge of cryptographic principles, real-time validation patterns, and secure UX design.

## Task

Create a complete, production-ready React TypeScript password strength analyzer component that validates in real-time, provides intelligent security feedback, and generates memorable secure alternatives.

## Context

Traditional password checkers frustrate users with vague feedback and no actionable guidance. This component must actively guide users toward genuinely secure passwords while making the experience feel empowering rather than punishing. The system should explain security flaws clearly and suggest alternatives users will actually want to use.

{{tech-stack}} specifies your implementation environment: framework versions, libraries (e.g., zxcvbn), styling approach, animation libraries, browser support requirements, and performance constraints.

{{design-requirements}} defines your visual and UX system: color schemes, typography, brand guidelines, accessibility standards (e.g., WCAG 2.1 AA), user behavior expectations, and UX objectives.

{{security-policy}} outlines your security standards: minimum entropy thresholds, pattern detection rules, compliance needs (NIST, OWASP), and password policy enforcement.

## Output

Provide a complete, production-ready implementation structured as:

### Complete React TypeScript Component
Full component code with proper state management, hooks, and comprehensive TypeScript types and interfaces.

### Real-Time Validation Engine
Password strength calculation using entropy analysis, common pattern detection (dictionary words, sequences, repetitions), and security scoring logic with inline comments explaining the cryptographic reasoning.

### Visual Feedback System
Color-coded strength indicators, animated progress bars, smooth transitions, and clear messaging that explains what makes passwords weak or strong.

### Intelligent Alternative Generation
Memory-friendly password suggestions that meet security requirements, with explanations of why each suggestion is secure and easy to remember.

### Accessibility and Performance
Full keyboard navigation support, screen reader announcements, debouncing for performance, and optimization techniques.

### Usage Example and Integration
Sample implementation code showing how to integrate the component into an existing application, including props, event handlers, and setup instructions.
```

## 用法 / Usage
- 必填變數 / Variables: {{design-requirements}}、{{security-policy}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Password Strength Analyzer Component Builder is a free AI prompt that generates enterprise-grade password …
