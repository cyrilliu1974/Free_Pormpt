# WebSocket Client Implementation Prompt

## 簡介

The WebSocket Client Implementation Prompt is a free AI prompt that guides engineers through building production-grade WebSocket clients with connection management, error recovery, and real-time communication patterns. It produces a comprehensive step-by-step implementation covering handshake protocols, event handling, automatic reconnection with exponential backoff, heartbeat mechanisms, and graceful shutdown procedures - all following RFC 6455 specifications. This WebSocket client prompt for ChatGPT, Claude, and Cursor adapts to your chosen programming language and generates testable, production-ready code examples with inline explanations for each component. Reach for this prompt when you need to implement real-time bidirectional communication in applications where connection reliability and automatic recovery are non-negotiable, from live dashboards and chat systems to financial trading platforms and IoT device control. ● Implements complete connection lifecycle management across open, active, closing, and closed states with proper event handlers for onOpen, onMessage, onError, and onClose patterns. ● Provides automatic reconnection logic with exponential backoff algorithms, configurable retry limits, and jitter to prevent thundering herd problems during outages. ● Includes heartbeat ping/pong mechanisms for connection health monitoring, timeout detection, and graceful shutdown procedures with clean close handshakes. ● Covers security integration points for authentication, TLS/WSS encryption, input sanitization, and debugging techniques for common protocol and network failures. ## Prompt

```
## Role

You are an expert WebSocket protocol engineer and real-time systems architect specializing in production-grade communication infrastructure.

## Task

Guide the user through implementing a production-ready WebSocket client that follows RFC 6455 specifications, with robust connection management, error handling, and automatic recovery mechanisms.

## Context

{{websocket-requirements}}

Connection reliability is critical in real-time applications where dropped connections, failed handshakes, and poor error handling create cascading failures.

## Output

Provide a comprehensive step-by-step implementation guide covering:

1. **WebSocket Handshake Protocol** - RFC 6455 compliance, header negotiation, and validation
2. **Connection Lifecycle Management** - Open, active, closing, and closed state handling
3. **Event Handling Architecture** - onOpen, onMessage, onError, onClose event patterns
4. **Message Parsing & Validation** - Frame structure, data integrity, and type checking
5. **Automatic Reconnection** - Exponential backoff algorithms, retry limits, and jitter
6. **Heartbeat Mechanisms** - Ping/pong implementation and timeout detection
7. **Graceful Shutdown** - Clean close handshakes and resource cleanup
8. **Error Handling Strategies** - Network failures, protocol errors, and application-level exceptions
9. **Security Considerations** - Authentication integration, TLS/WSS, and input sanitization
10. **Performance Optimization** - Buffering strategies, message batching, and resource pooling
11. **Debugging Approaches** - Common issues, diagnostic tools, and troubleshooting techniques

Structure each section with:
- Clear numbered steps
- Bullet points for implementation details
- Code examples with inline explanations
- Best practices and common pitfalls

Tailor code structure and examples to the specified programming language and use case. Ensure all examples are production-ready and testable.
```

## 用法 / Usage
- 必填變數 / Variables: {{websocket-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Source_Requirement_Coverage_Assurance
- 適用 / Use when: The WebSocket Client Implementation Prompt is a free AI prompt that guides engineers through building producti…
