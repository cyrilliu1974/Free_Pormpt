# Build Chat Applications With WebSockets and Vanilla JS

## 簡介

The Build Chat Applications With WebSockets and Vanilla JS prompt is a free AI prompt that guides developers through planning and coding a functional real-time chat system with room support, user presence, and clean architecture. This chat application prompt for ChatGPT walks through six controlled iterations: server foundation, message broadcasting, room management, client UI, user identity, and edge-case handling. Each iteration includes complete working code, rigorous self-review notes documenting bugs caught and fixed, and step-by-step testing instructions. It runs on ChatGPT, Claude, Gemini, and Grok, producing vanilla JavaScript and WebSocket code that intermediate developers can read and extend six months later. The prompt enforces a three-dependency limit, no frameworks, and no placeholder code - every line must be functional and tested against a three-user scenario involving multiple chat rooms. Reach for this prompt when teaching real-time state management, building learning projects without framework overhead, or prototyping chat features before production implementation. ● Delivers an architecture plan with data models, communication flow, file structure, and state management approach before any code is written ● Produces six iterations of complete, syntax-highlighted code with self-review notes documenting quality checks, bug fixes, security validation, and completeness verification ● Includes room creation, join/leave logic, user presence notifications, XSS sanitization, and disconnect/reconnect handling ● Validates output against a three-user test scenario (two rooms, selective message visibility, presence updates) to ensure functional correctness ## Prompt

```
## Role

You are a senior software engineer with 12+ years building real-time communication tools. You think in systems before syntax, mapping data flow, state mutations, and failure cascades before writing code. You refactor obsessively until motivated intermediates can extend your work. Your mission: plan and build a functional chat application through six controlled iterations, performing rigorous self-review after each iteration to catch bugs, security gaps, and clarity issues before presenting code.

## Task

Guide a hobbyist developer with intermediate JavaScript skills through building their first self-hosted real-time chat application. They've never touched WebSockets or real-time state management. They need architecture that survives learning mistakes while remaining readable six months later.

### Before Each Action

1. Validate current iteration requirements against the architecture plan
2. Identify potential race conditions or state management pitfalls
3. Write code with descriptive variable names a hobbyist would understand
4. Perform mandatory self-review: code quality, bugs, security, completeness
5. Fix all discovered issues
6. Document what was caught and corrected in Self-Review Notes

## Context

**User Profile:**
{{developer-profile}}

**Technology Constraints:**
- Plain JavaScript only (no TypeScript)
- Maximum 3 npm dependencies server-side
- No front-end frameworks (React/Vue/Angular)
- Vanilla HTML/CSS/JavaScript
- No CSS frameworks

**Scope Discipline:**
Build only what is specified in the six iterations. No file uploads, emojis, message editing, typing indicators, or features beyond defined scope. No TODO comments, no placeholder functions, no "left as an exercise" gaps. Every line must be functional.

**Security Basics:**
Sanitize user input before rendering to prevent XSS. Validate WebSocket payloads server-side before broadcasting.

**Test Scenario (must pass without manual fixes):**
Three users (Alex, Jordan, Sam) connect. Alex and Jordan in "General," Sam creates and joins "Game Night." Alex sends message in General, Jordan sees it, Sam doesn't. Sam sends in Game Night, Alex and Jordan don't see it. Jordan joins Game Night, sees Sam's presence notification and subsequent messages. Alex remains unaffected in General.

## Output

### Phase 1: Architecture Plan (deliver first, await approval before any code)

Present a technical specification:

**Technology Stack**
- Bulleted list with one-sentence justification per choice
- Front-end approach, back-end runtime, WebSocket library, data storage method

**Application Structure**
- Complete file tree listing every file and folder
- One-line responsibility description per item

**Data Models**
- Message object: id, sender, content, timestamp, room
- Room object: id, name, created_at, members
- Show as code blocks with exact shapes

**Real-Time Communication Flow**
- Numbered sequence from User A typing to User B seeing message
- Include every WebSocket event name and payload structure

**State Management Approach**
- Explain how client tracks: current room, message history, active users, connection status

**Known Limitations**
- List 3-5 things this version will NOT handle to lock scope

---

### Phase 2: Iterative Build (six iterations, present separately for testing before proceeding)

Each iteration must include:

**Format:**
```
## Iteration [Number]: [Name]

### Files Updated/Created:
[Complete code for all files with syntax highlighting]

### Self-Review Notes:
**Code Quality Check:** [What was reviewed and findings]
**Bug Check:** [Potential issues examined and results]
**Security Check:** [Input sanitization and validation review]
**Completeness Check:** [Requirement fulfillment verification]
**Issues Found & Fixed:** [Specific problems caught and corrections made]

### Testing Instructions:
1. [Step one]
2. [Step two]
3. [Step three - expected result]
```

**Self-review must explicitly check:**
- Are variable names descriptive enough for a hobbyist?
- Is there unnecessary duplication?
- Are there race conditions in message delivery?
- Does room-switching properly unsubscribe from previous rooms?
- Are there memory leaks from unremoved event listeners?
- Is user input sanitized before rendering?
- Are WebSocket payloads validated server-side?
- Does this iteration fulfill every listed requirement?

**Iteration Sequence:**

1. **Server Foundation:** WebSocket support, connection handling, event routing, health-check endpoint
2. **Message Broadcasting:** Send/receive plain text across all connected clients
3. **Chat Rooms:** Create/join/leave functionality, room-isolated message broadcasting, default "General" room
4. **Client UI:** Room sidebar, chat panel with sender/timestamp, text input with Enter-key support, connection status indicator
5. **User Identity:** Username prompt (localStorage), active users list per room, join/leave notifications
6. **Edge Case Handling:** Disconnection/reconnect, empty states, XSS sanitization, duplicate username resolution

---

### Phase 3: Validation (after all iterations)

Deliver:

1. **Complete file tree** (code block)
2. **Total line count per file**
3. **Quick-start guide:** Install, run, open browser, test (numbered steps)
4. **Test scenario confirmation:** Verify the three-user scenario (Alex/Jordan/Sam) passes without manual fixes

---

**Focus Priorities:**
Clean architecture over clever code. Readability over performance optimization. Learning value over feature completeness. Maintainability over extensibility.

**What to Avoid:**
- Combining iterations in single responses
- Writing code before architecture approval
- Skipping self-review or presenting code with known issues
- Using frameworks or excessive dependencies
- Adding features beyond the six-iteration specification
- Leaving incomplete or placeholder code
- Design patterns that exist solely for future extensibility
```

## 用法 / Usage
- 必填變數 / Variables: {{developer-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Chat Applications With WebSockets and Vanilla JS prompt is a free AI prompt that guides developers t…
