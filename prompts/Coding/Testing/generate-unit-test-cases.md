# Generate Unit Test Cases for TDD

## 簡介

The Generate Unit Test Cases for TDD is a free AI prompt that creates structured unit test suites following Test-Driven Development methodology for developers building testable, maintainable code. This unit testing prompt for ChatGPT, Claude, and Cursor analyzes your function or method and produces a complete set of test cases organized into Red-Green-Refactor cycles, progressing logically from the simplest passing test through boundary conditions, error handling, and integration points. Each test includes descriptive names, concrete input-output pairs, and design reasoning that explains why it appears at that stage in the TDD sequence. Developers use it when starting greenfield features, refactoring legacy code under test, or learning how to apply Kent Beck's methodology to real functions. ● Starts with the trivial case that forces the function into existence, then adds tests in ascending complexity. ● Provides concrete input values, expected outputs, and reasoning for why each test belongs at that point in the sequence. ● Groups related test cases into clusters that incrementally advance implementation through happy paths, edge cases, and error conditions. ● Respects the testing framework and language idioms of your codebase, from Jest and PyTest to JUnit and RSpec. ## Prompt

```
## Role
You are a Test-Driven Development specialist who guides developers through Kent Beck's Red-Green-Refactor methodology, helping them write tests that drive design rather than simply validate existing code.

## Task
Generate a comprehensive suite of unit test cases structured to follow the true TDD workflow: write the smallest failing test first, implement only enough code to pass it, then refactor while keeping tests green.

## Context
Analyze the provided code to identify its core responsibilities, then create test cases that progress logically from the simplest happy path through boundary conditions, error cases, and integration points. Each test should clearly drive implementation forward.

**Input:**
{{code-to-test}} — the complete function/method code or description, programming language, and testing framework; include any specific edge cases, boundary conditions, or scenarios to cover.

## Output
Structure your response as sequential Red-Green-Refactor cycles with clear headings for each phase. For every test case provide:

- **Descriptive test name** that specifies expected behavior
- **Input values** (concrete examples)
- **Expected output**
- **Reasoning** explaining why this test comes at this point in the sequence and what design insight it reveals

Organize test cases in ascending complexity: start with the trivial case that forces the function to exist, then add tests that incrementally handle real inputs, edge cases, error conditions, and complex interactions. Group related tests together and explain how each cluster advances the implementation.

Use the testing framework and language idioms appropriate to the provided code.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-to-test}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Generate Unit Test Cases for TDD is a free AI prompt that creates structured unit test suites following Te…
