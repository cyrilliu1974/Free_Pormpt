# Event Handler Implementation Prompt

## 簡介

The Event Handler Implementation Prompt is a free AI prompt that generates production-ready event handler code using the Observer Pattern for software architects and developers working with event-driven systems. This event handler prompt for ChatGPT, Claude, and Cursor takes your event specification and produces complete handler functions with type definitions, error isolation logic, resource cleanup routines, registration examples, and integration notes tailored to existing codebases with limited documentation. It enforces architectural principles like single responsibility, decoupling from event sources, and failure isolation so individual handlers cannot crash your system. Use this prompt when retrofitting event-driven patterns into legacy code, designing new observers that must coexist with undocumented frameworks, or establishing maintainable handler conventions for your team. ● Produces handler functions with immutable event data structures, preventing shared state corruption and race conditions. ● Implements retry logic for transient failures and context-rich logging so handler errors never propagate to the event system. ● Includes explicit cleanup and unsubscription code to prevent memory leaks in long-running applications. ● Provides registration examples and design notes covering testing strategy, integration approach, and edge cases specific to your event type. ## Prompt

```
## Role

You are a software architect specializing in event-driven systems and the Observer Pattern.

## Task

Design and implement a production-ready event handler using the Observer Pattern for {{event-specification}}.

## Context

The implementation must integrate into an existing codebase where:
- The framework has its own event system with limited documentation
- Handlers must remain decoupled from event sources
- Individual handler failures cannot crash the system
- The team needs clear, maintainable patterns

## Requirements

**Architecture principles:**
- Single responsibility: each handler addresses one concern
- Decoupling: handlers cannot reference event sources; no circular dependencies; event data passed as immutable objects
- Error isolation: handler failures must log with context but not propagate; implement retry logic for transient failures
- Resource safety: explicit cleanup, proper unsubscription, memory leak prevention
- Clear naming: `onUserRegistered`, `handlePaymentCompleted` style

**Avoid:** Generic handlers that do too much, synchronous blocking, assumptions about event ordering, unprotected shared state modification.

## Output

Provide:

1. **Handler function** with parameter structure and type definitions
2. **Implementation logic** with inline comments explaining key decisions
3. **Error handling** for specific failure scenarios
4. **Resource cleanup** code if the handler acquires resources
5. **Registration example** showing how to wire the handler into the event system
6. **Design notes** covering integration approach, testing strategy, and potential issues

Format as clean, commented code blocks ready for production use.
```

## 用法 / Usage
- 必填變數 / Variables: {{event-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Event Handler Implementation Prompt is a free AI prompt that generates production-ready event handler code…
