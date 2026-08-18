# Private Messaging Platform Development Prompt

## 簡介

The Private Messaging Platform Development Prompt is a free AI prompt that produces a full technical implementation guide for engineers building secure, real-time chat applications. It walks you through architecture design, end-to-end encryption, WebSocket messaging engines, group management, media handling, UI polish, security hardening, and deployment - all tailored to your stack, scale, and compliance needs. This private messaging platform development prompt for ChatGPT, Claude, Gemini, and Grok is ideal for full-stack developers creating communication tools for families, businesses, or close-knit communities who need Signal-level encryption combined with intuitive, warm user experience. Reach for it when you are architecting a chat app from scratch or refactoring an existing messaging feature to meet modern security and performance standards. ● Architectural foundation and database schema design for scalable real-time messaging, including entity relationships and data models. ● End-to-end encryption implementation with key management, secure session handling, and compliance-ready security protocols. ● Real-time messaging engine built on WebSocket infrastructure, message queuing, and delivery guarantees for low-latency communication. ● Group management, invitation flows, permissions, media handling, file uploads, reactions, threading, and rich communication features. ● User interface design guidance, component architecture, responsive layouts, accessibility standards, performance optimization, and deployment pipelines with monitoring and CI/CD setup. ## Prompt

```
## Role

You are an expert full-stack engineer and real-time communication architect specializing in secure messaging platforms.

## Task

Develop a complete, production-ready private messaging application that combines end-to-end encryption with polished UX and organizational clarity. The platform should feel intimate and secure—like a digital living room rather than a corporate tool.

## Context

{{technical-context}}

Include your current programming and system architecture experience, preferred technology stack (frontend/backend), target user groups, specific security/compliance requirements, and deployment preferences (hosting environment, expected scale).

## Output

Provide a comprehensive implementation guide structured in these phases:

● **Architecture Foundation and Database Schema Setup** – System design decisions, entity relationships, data models
● **Authentication and Security Implementation** – End-to-end encryption, key management, secure session handling
● **Real-Time Messaging Engine Development** – WebSocket infrastructure, message queuing, delivery guarantees
● **Group Management and Invitation Systems** – Permissions, member lifecycle, invite flows
● **Media Handling and Rich Communication Features** – File uploads, previews, reactions, threading
● **User Interface Design and Experience Polish** – Component architecture, responsive layouts, accessibility
● **Security Hardening and Performance Optimization** – Threat mitigation, caching strategies, load testing
● **Deployment Strategy and Monitoring Setup** – CI/CD pipelines, observability, incident response

For each phase, provide detailed technical specifications, relevant code examples, and clear implementation steps tailored to the technical context provided. Present recommendations in bullet point format using ●.
```

## 用法 / Usage
- 必填變數 / Variables: {{technical-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Private Messaging Platform Development Prompt is a free AI prompt that produces a full technical implement…
