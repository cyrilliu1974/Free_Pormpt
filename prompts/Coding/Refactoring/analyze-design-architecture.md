# Analyze Design Architecture With Domain-Driven Design

## 簡介

The Analyze Design Architecture With Domain-Driven Design is a free AI prompt that produces detailed modular architecture plans for software architects restructuring monolithic codebases into maintainable, domain-centric systems. This design architecture prompt for ChatGPT, Claude, Gemini, and Grok evaluates your current codebase structure, identifies hidden business domains obscured by layer-based organization, and designs bounded contexts with clear domain boundaries, aggregate roots, and interface abstractions that minimize coupling while enabling independent testing and deployment. Reach for this prompt when you face technical debt, interdependent deployments, or testing bottlenecks and need a concrete migration roadmap grounded in Eric Evans' Domain-Driven Design principles. ● Evaluates current project organization to uncover hidden business domains and coupling patterns within technical layers. ● Maps bounded contexts that encapsulate related business capabilities with minimal inter-domain dependencies. ● Defines aggregate roots as consistency boundaries and entry points for each domain. ● Proposes phased migration roadmaps that enable gradual transformation without disrupting existing functionality. ## Prompt

```
## Role

You are a software architect specializing in Domain-Driven Design with deep experience restructuring monolithic codebases into maintainable, domain-centric architectures.

## Task

Analyze the provided codebase and produce a comprehensive modular architecture plan using DDD principles: bounded contexts, aggregate roots, minimal coupling, and clear domain boundaries.

## Context

{{codebase-description}}

The architecture suffers from technical debt, interdependent deployments, and testing bottlenecks. Business domains are obscured by layer-based organization, and technical boundaries don't align with business logic.

## Analysis Required

- Evaluate current project organization and identify hidden business domains within the technical structure
- Map cross-cutting concerns, tight coupling patterns, and misaligned technical boundaries
- Identify core business domains and their natural boundaries
- Design bounded contexts that encapsulate related business capabilities
- Define aggregate roots as consistency boundaries and entry points
- Create interface abstractions that minimize inter-domain dependencies while maintaining necessary communication
- Propose modular architecture enabling independent testing, deployment, and scaling per domain
- Develop migration strategies for gradual transformation without disrupting existing functionality

## Output

Structure your response with these sections:

1. **Current State Analysis** – evaluation of existing structure, coupling patterns, misalignments
2. **Domain Identification** – core business domains and natural boundaries discovered
3. **Bounded Context Design** – proposed contexts with encapsulated capabilities
4. **Aggregate Root Definition** – consistency boundaries and entry points per domain
5. **Interface Abstraction Strategy** – communication contracts between domains
6. **Modular Architecture Proposal** – target structure with deployment and testing independence
7. **Migration Roadmap** – phased transformation plan with risk mitigation

Use bullet points, diagrams, and concrete examples for implementation clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{codebase-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Design Architecture With Domain-Driven Design is a free AI prompt that produces detailed modular a…
