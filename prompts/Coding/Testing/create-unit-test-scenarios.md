# Unit Test Scenario Generator for TDD

## 簡介

The Unit Test Scenario Generator for TDD is a free AI prompt that creates focused, production-ready unit test scenarios for developers practicing test-driven development. This unit test prompt for ChatGPT analyzes your code and generates test scenarios that follow the Arrange-Act-Assert pattern, progressing logically from happy-path cases through edge cases to error conditions. It works with any language and testing framework - simply provide your code, specify your framework (Jest, PyTest, JUnit, etc.), and list any specific concerns or edge cases you want covered. Each generated test includes clear naming, complete implementation code, and explanatory comments that describe input parameters, expected results, and the behavior being verified. Runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need structured test coverage for new features, want to add tests to legacy code, or are learning TDD practices and need examples of well-structured unit tests. ● Generates tests that verify one behavior at a time with descriptive names and clear intent ● Organizes scenarios in logical progression from simple happy paths to complex edge cases and error conditions ● Includes concrete examples with specific input values and expected outputs rather than abstract placeholders ● Provides explanatory comments for each test describing the rationale, parameters, and behavior under verification ## Prompt

```
## Role

You are a test-driven development specialist writing effective unit tests that catch bugs before production.

## Task

Generate comprehensive unit test scenarios for the provided code following TDD principles: small, focused tests that verify one behavior at a time using the Arrange-Act-Assert pattern.

## Context

**Code to test:**
{{code-to-test}}

**Language and framework:**
{{language-framework}}

**Edge cases or concerns:**
{{specific-concerns}}

## Approach

1. Analyze the code to identify core behaviors requiring verification
2. Start with the happy path, then cover edge cases, then error conditions
3. Progress from simple to complex scenarios
4. Use concrete examples rather than abstractions
5. Name each test to make its intent immediately obvious
6. Include explanatory comments describing the testing rationale

## Output

For each test scenario, provide:

- **Clear test case heading** describing what behavior is being verified
- **Code block** with the complete test implementation
- **Comments** explaining:
  - Input parameters and their significance
  - Expected result with concrete values
  - The specific behavior being tested

Organize tests in logical progression, ensuring each focuses on exactly one behavior. Format all test code in properly syntax-highlighted blocks.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-to-test}}、{{language-framework}}、{{specific-concerns}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Unit Test Scenario Generator for TDD is a free AI prompt that creates focused, production-ready unit test …
