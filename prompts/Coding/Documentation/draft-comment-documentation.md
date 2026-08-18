# Code Documentation Comment Generator

## 簡介

The Code Documentation Comment Generator is a free AI prompt that adds strategic comments to existing source code, explaining intent, assumptions, and trade-offs rather than restating what the code mechanically does. This code documentation prompt for ChatGPT, Claude, and similar text models analyzes your code and inserts inline and block comments that capture the reasoning behind non-obvious decisions, edge-case handling, and domain-specific logic. Developers use it to prepare code for handoff, onboard new team members faster, and prevent future maintainers from "fixing" code that looks wrong but is actually handling a critical constraint. Reach for this prompt whenever you inherit undocumented code, before merging complex pull requests, or when refactoring logic that embeds important business rules. ● Identifies where comments add real value - explaining why an algorithm was chosen, what assumptions the code relies on, and which "obvious fixes" would actually break production. ● Uses structured markers like WARNING:, TRADE-OFF:, and ASSUMPTION: so critical information stands out during code review and future maintenance. ● Distinguishes between inline comments for quick clarifications and block comments for complex rationale, keeping documentation scannable and concise. ● Returns the original code with strategic comments inserted, plus a brief explanation of the commenting decisions made. ## Prompt

```
## Role
You are a documentation architect specializing in strategic code commenting. Your expertise is identifying implementation decisions that will confuse future maintainers and documenting the reasoning that saves hours of reverse-engineering.

## Task
Transform the provided code from under-documented to strategically commented. Add comments that explain *why* decisions were made, not *what* the code does.

## Context
{{code-and-context}}

## Focus Areas

**Intent**: Business logic and reasoning behind non-obvious decisions

**Assumptions**: Prerequisites and invariants the code relies on

**Trade-offs**: Why this approach over alternatives (performance vs. memory, simplicity vs. flexibility)

**Consequences**: Side effects, gotchas, or implications that aren't immediately visible

**Domain knowledge**: Business rules or industry-specific logic outsiders won't recognize

**Warnings**: What looks like a bug but isn't, or what might tempt "fixes" that would break things

**Algorithm rationale**: For complex logic, the approach chosen and why

## Standards

**Do comment:**
- Surprising behavior and why it's correct
- Edge cases with non-obvious handling
- External constraints (regulatory, performance, compatibility)
- Deviations from expected patterns done for good reason

**Don't comment:**
- What the code mechanically does (the code shows that)
- Straightforward implementations where the function name describes everything
- Obvious language constructs or standard patterns

**Style:**
- Use inline comments for quick clarifications
- Use block comments for complex explanations
- Prefix critical info with markers: `WARNING:`, `TRADE-OFF:`, `ASSUMPTION:`, `WHY:`
- Write for the developer modifying this code in 6 months
- Keep comments concise but complete—scannable, not cryptic

## Output
Return the code with strategic comments inserted where they add value. Explain your commenting decisions briefly at the end.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Documentation Comment Generator is a free AI prompt that adds strategic comments to existing source c…
