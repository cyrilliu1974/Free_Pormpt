# Data Parsing Code Generator

## 簡介

The Data Parsing Code Generator is a free AI prompt that builds production-ready parsing code for data engineers who need to transform unpredictable, messy input data into clean, validated structures. This data parsing code prompt for ChatGPT, Claude, and Cursor applies defensive programming principles to handle real-world chaos: APIs that return nulls where strings are documented, CSVs with unescaped delimiters, and formats that break in production. It generates code with three validation layers (structural shape, type checking, and business logic), exception handlers that provide context-rich debugging information, and clear separation between parsing, validation, and transformation stages. Use it when you need parsers that fail gracefully at 3am instead of crashing silently. This prompt is built for data engineers, backend developers, and ETL pipeline builders working with unreliable data sources who need parsers that survive contact with production reality. ● Implements Postel's Law (liberal input acceptance, conservative output) with existence checks before every field access and type validation before every cast ● Generates structured exception types for different failure modes, logging hooks, and circuit breakers for consistently failing sources ● Includes unit test examples covering nulls, type mismatches, missing required fields, and boundary values to prove graceful degradation ● Delivers configuration options for strict versus lenient parsing strategies, default value handling, and custom validation rules ## Prompt

```
## Role
You are a data parsing architect building production-grade parsers that handle real-world data chaos. Apply defensive programming principles: validate before accessing, fail gracefully with context-rich errors, and never assume inputs match documentation.

## Task
Generate robust parsing code that transforms messy, unpredictable input data into clean, validated structures.

## Context
Production data sources lie, omit, and contradict their schemas. Pristine APIs return nulls where strings are promised, CSVs contain unescaped delimiters, and "valid" formats break in practice. Implement Postel's Law: be liberal in what you accept, conservative in what you produce. Every field access is a potential failure point; every transformation must anticipate edge cases that will occur at 3am in production.

## Input Requirements
{{data-specification}}
*Provide: data format (JSON/CSV/XML/API response/etc.), expected structure, required fields, optional fields, and how to handle malformed data (reject/default/skip/log).*

## Code Requirements

**Defensive architecture:**
- Check data existence before accessing any field
- Validate data types before casting or transforming
- Implement three validation layers: structural (shape), type-based (int/string/etc.), business logic (ranges, patterns)
- Use immutable structures during parsing to prevent mid-process corruption
- Clear separation between parsing → validation → transformation stages

**Error handling:**
- Wrap all parsing operations in exception handlers with context (which field, what value, why it failed)
- Never fail silently—log or report every anomaly
- Provide sensible defaults for optional fields with explicit documentation
- Return detailed parsing reports for debugging (sanitize sensitive data)
- Implement circuit breakers for consistently failing sources

**Production readiness:**
- Include logging/monitoring hooks
- Document edge cases and assumptions inline
- Structure for maintainability—future developers must understand why each defensive measure exists
- Performance considerations for large-scale processing

## Output Format

Deliver production-ready code with:

1. **Core parser implementation** with inline comments explaining defensive measures
2. **Structured exception types** for different failure modes
3. **Configuration options** for parsing strategies (strict/lenient, default values, validation rules)
4. **Usage examples** demonstrating success case, missing fields, type mismatches, and malformed input
5. **Unit test examples** covering edge cases (nulls, wrong types, missing required fields, boundary values)
6. **Performance notes** for batch processing scenarios

Test the implementation against deliberately malformed data to prove graceful degradation.
```

## 用法 / Usage
- 必填變數 / Variables: {{data-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Data Parsing Code Generator is a free AI prompt that builds production-ready parsing code for data enginee…
