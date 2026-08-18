# Chat Widget Development Prompt

## 簡介

The Chat Widget Development Prompt is a free AI prompt that generates complete, production-ready chat interface code for frontend developers and full-stack engineers. This chat widget prompt for ChatGPT produces a fully functional floating chat component with expand/collapse animations, message display areas featuring sender avatars and timestamps, typing indicators, connection status displays, and real-time communication via WebSocket or polling. Built to run on ChatGPT, Claude, and Cursor, it outputs structured code snippets organized by component - floating button, message area, input interface, and real-time integration - following proven conversational UI patterns from established messaging platforms. Use it when building customer support widgets, in-app messaging, live chat systems, or any real-time communication interface that requires familiar, intuitive interactions. ● Floating button with smooth expand/collapse animations and visual state transitions. ● Message display with sender avatars, timestamps, grouping by sender, and auto-scroll to latest messages. ● Typing indicators and connection status displays for real-time feedback. ● Text input interface with send functionality and message delivery confirmation. ## Prompt

```
## Role
You are an expert UI/UX developer specializing in chat interface design and real-time communication systems.

## Task
Provide a complete, production-ready chat widget implementation including:
- Floating button with expand/collapse animations
- Message display area with sender avatars, timestamps, and message grouping
- Typing indicators and connection status displays
- Text input interface with send functionality
- Real-time communication integration (WebSocket or polling)
- Message delivery confirmation and auto-scroll behavior

## Context
The widget must follow proven conversational UI patterns from popular messaging platforms: real-time responsiveness, visual feedback, intuitive interactions.

**Technical Stack:** {{tech-stack}}

**Integration Requirements:** {{integration-requirements}}

## Output
Structure your response with clear section headings for each component. Include practical code snippets ready for production use. Organize implementation steps sequentially for smooth development workflow.
```

## 用法 / Usage
- 必填變數 / Variables: {{integration-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Chat Widget Development Prompt is a free AI prompt that generates complete, production-ready chat interfac…
