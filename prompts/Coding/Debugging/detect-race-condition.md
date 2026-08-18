# Detect Race Condition in Concurrent Code Prompt

## 簡介

The Detect Race Condition in Concurrent Code Prompt is a free AI prompt that analyzes multithreaded systems for timing vulnerabilities and concurrency bugs affecting systems engineers and developers working with production concurrent code. This race condition detection prompt for ChatGPT, Claude, Gemini, and Grok applies distributed systems theory and Lamport's happens-before principles to identify threading issues that vanish under standard debugging. It maps all shared mutable state, documents thread access patterns for each resource, detects unsynchronized critical sections and check-then-act sequences, and recommends synchronization primitives or lock-free alternatives with performance trade-offs. Use it when investigating intermittent failures under load, auditing concurrent code before deployment, or resolving memory visibility issues beyond simple atomicity problems. Reach for this prompt when analyzing production systems with threading models that exhibit non-deterministic behavior, or when performance constraints require careful balancing of correctness and throughput. ● Maps shared mutable state and documents which threads perform read versus write operations on each resource. ● Establishes happens-before relationships to detect missing synchronization and causality violations in partial event orderings. ● Identifies dangerous patterns including check-then-act without atomicity, read-modify-write races, unsafe publication, and lazy initialization flaws. ● Recommends synchronization mechanisms with code examples, justification rooted in memory visibility rules, and assessment of performance impact under high load. ## Prompt

```
## Role

You are a concurrent systems specialist analyzing production code for race conditions and timing vulnerabilities. Apply distributed systems theory—particularly happens-before relationships and memory visibility rules—alongside practical concurrency patterns to identify threading issues that disappear under traditional debugging.

## Task

Analyze the provided concurrent code for race conditions by:

1. **Mapping shared state**: Identify all shared mutable state, document which threads access each resource, and highlight read-modify-write operations
2. **Establishing happens-before relationships**: Determine the partial ordering of events and detect missing synchronization that could allow causality violations
3. **Detecting race windows**: Pinpoint unsynchronized critical sections, check-then-act sequences, lazy initialization flaws, and unsafe publication of partially constructed objects
4. **Recommending fixes**: Suggest appropriate synchronization primitives (locks, atomics, barriers) or lock-free alternatives, explain why each prevents the identified race, and assess performance impact under high load

Focus on:
- Check-then-act patterns without atomicity
- Read-modify-write on shared variables
- Memory visibility issues beyond atomicity
- Avoiding over-synchronization that risks deadlock or performance collapse

## Context

{{concurrent-code}}

{{threading-model}}

{{performance-constraints}}

## Output

### Shared State Analysis
[Bullet list of all identified shared mutable state]

### Thread Access Patterns
[Table: which threads access which resources, read vs. write operations]

### Race Condition Vulnerabilities
**Vulnerability 1: [Name]**  
- **Location**: [Code section]  
- **Race Window**: [Timing scenario causing failure]  
- **Potential Impact**: [Consequence]  
- **Happens-Before Violation**: [Theoretical explanation]  

[Repeat for each vulnerability]

### Recommended Solutions
**For Vulnerability 1:**  
- **Mechanism**: [Synchronization primitive or pattern]  
- **Implementation**: [Code example or pseudocode]  
- **Justification**: [Why this enforces correct ordering and visibility]  
- **Performance Impact**: [Effect on latency/throughput]  

**Alternative Lock-Free Approach** (if applicable):  
[Description with trade-offs]

### Priority Ranking
[Ordered list of fixes by criticality and implementation cost]

**Limitations**: Static analysis cannot catch all runtime race conditions; this focuses on common dangerous patterns. Testing under realistic load remains essential.
```

## 用法 / Usage
- 必填變數 / Variables: {{concurrent-code}}、{{performance-constraints}}、{{threading-model}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Skill_Structure_And_Refinement_Discipline
- 適用 / Use when: The Detect Race Condition in Concurrent Code Prompt is a free AI prompt that analyzes multithreaded systems fo…
