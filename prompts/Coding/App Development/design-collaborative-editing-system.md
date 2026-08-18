# Real-Time Collaborative Editing System Design Prompt

## 簡介

The Real-Time Collaborative Editing System Design Prompt is a free AI prompt that produces detailed technical architectures for multi-user editing applications with conflict resolution, state synchronization, and performance optimization strategies. This real-time collaboration prompt for ChatGPT, Claude, Gemini, and Grok delivers complete system designs covering operational transforms, CRDTs, user presence tracking, offline handling, and technology stack recommendations with implementation code examples. It addresses the distributed state problems developers face when building Google Docs-style editing, collaborative whiteboards, or any application where multiple users modify shared data simultaneously. The prompt generates phase-by-phase implementation roadmaps, testing strategies for race conditions and network failures, and solutions for maintaining sub-100ms latency under concurrent load. Reach for this prompt when architecting any application requiring simultaneous editing by multiple users, from code editors and design tools to document platforms and spreadsheet applications. ● Provides conflict resolution strategy selection and implementation details for operational transforms, CRDTs, or hybrid approaches tailored to your application context. ● Delivers user presence, cursor tracking, and selection awareness implementations that show who is editing what in real time. ● Includes performance optimizations like message batching, throttling, and compression to handle multiple concurrent editors without lag. ● Covers offline handling and sync recovery patterns that prevent data loss when users disconnect and reconnect during active editing sessions. ## Prompt

```
## Role

You are a real-time collaboration systems architect with deep expertise in distributed state synchronization, conflict resolution algorithms (operational transforms, CRDTs), and building responsive multi-user editing experiences at scale.

## Task

Design a complete real-time collaborative editing system for the specified application. Provide:

- Technical architecture with conflict resolution strategy (OT, CRDT, or hybrid)
- User presence and cursor/selection tracking implementation
- Performance optimizations for multiple concurrent editors
- Offline handling and sync recovery patterns
- Specific technology recommendations with implementation rationale
- Step-by-step implementation roadmap with code examples
- Testing strategy for race conditions, network failures, and rapid concurrent edits

Focus on preventing data loss, handling edge cases that commonly break collaboration, and maintaining sub-100ms perceived latency.

## Context

**Application Details:**
{{application-context}}

**Technical Constraints:**
{{technical-constraints}}

## Output

Structure your response as:

**Architecture Overview**
High-level system design and data flow

**Technology Stack**
Recommended libraries/services (e.g., Yjs, Supabase Realtime, Socket.io) with rationale

**Conflict Resolution**
Detailed approach for concurrent edit handling with algorithm choice justification

**User Presence & Awareness**
Implementation for active collaborators, cursors, and selections

**Performance & Scale**
Optimizations for responsiveness under load (batching, throttling, compression)

**Offline & Recovery**
Disconnection handling and conflict-free reconnection strategy

**Implementation Roadmap**
Phased development steps with code examples

**Testing Approach**
Validation methods for concurrent scenarios and failure modes
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}}、{{technical-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Real-Time Collaborative Editing System Design Prompt is a free AI prompt that produces detailed technical …
