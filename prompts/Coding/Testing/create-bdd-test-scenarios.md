# BDD Test Scenario Generator

## 簡介

The BDD Test Scenario Generator is a free AI prompt that writes structured Behavior-Driven Development test scenarios in Gherkin syntax for quality assurance engineers and product teams. This BDD test scenario prompt for ChatGPT, Claude, Gemini, and Grok transforms a system description into complete Feature files organized around user behavior and business value. It outputs proper Given-When-Then structures that establish context, describe actions, and define expected outcomes using concrete examples and plain language non-technical stakeholders can review. Teams use it to document acceptance criteria for new features, create shared understanding between developers and product owners, and ensure test coverage spans both happy paths and edge cases before writing code. Reach for this prompt when you need test scenarios that serve as executable specifications and a single source of truth across disciplines. ● Outputs full Gherkin syntax with Feature, Background, Scenario, Given, When, and Then keywords structured for readability. ● Organizes scenarios by feature area with business-focused titles that communicate value to product managers and executives. ● Covers positive flows, edge cases, and error conditions using specific data examples rather than abstract descriptions. ● Writes from the user's perspective in plain business language, avoiding technical jargon so acceptance criteria can be validated before development begins. ## Prompt

```
## Role

You are a Quality Assurance Engineer and BDD specialist writing test scenarios in Gherkin syntax that non-technical stakeholders can understand and validate.

## Task

Write comprehensive BDD test scenarios for the following system:

{{system-description}}

Follow strict Given-When-Then structure:
- **Given** establishes context and preconditions
- **When** describes the user action or trigger event
- **Then** defines the expected outcome

Focus on user behavior and business value, not technical implementation. Cover both positive flows and edge cases using concrete examples with specific data.

Organize by feature areas. For each feature include:
- A business-focused title and description
- Multiple scenarios covering the complete user journey
- Background steps when scenarios share common setup
- Scenario titles that clearly communicate business value

Ensure every scenario tells a complete story from the user's perspective in plain business language.

## Output

Deliver proper Gherkin syntax using Feature, Background, Scenario, Given, When, Then keywords. Include clear acceptance criteria. Write from the user's perspective using business language, not technical jargon.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The BDD Test Scenario Generator is a free AI prompt that writes structured Behavior-Driven Development test sc…
