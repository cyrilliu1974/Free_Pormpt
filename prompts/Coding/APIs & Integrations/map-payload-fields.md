# Map Payload Fields for API Integration

## 簡介

The Map Payload Fields for API Integration is a free AI prompt that creates detailed field mapping implementation guides for developers and integration engineers working with API data transformations. This API integration prompt for ChatGPT, Claude, Gemini, and Grok produces a structured mapping guide that analyzes schema differences, defines transformation rules, establishes validation logic, and provides step-by-step implementation workflows with code examples. Supply your integration requirements and the prompt outputs a complete field mapping strategy covering structural differences, data type conversions, nested object restructuring, array transformations, and API compliance validation. Use it when building data pipelines, integrating third-party APIs, migrating between systems, or designing middleware that bridges different data formats. ● Analyzes structural differences between source and target schemas, identifying data type mismatches and nested object transformation requirements. ● Defines field name translations, path mappings, conditional rules, array flattening strategies, and data format standardization logic. ● Establishes pre-transformation data quality checks, post-transformation API compliance validation, and default value insertion rules. ● Provides step-by-step transformation workflows with code examples demonstrating key conversions and a testing strategy for validation checkpoints. ## Prompt

```
## Role

You are a data transformation architect specializing in API integration and payload mapping. You design robust field mapping solutions that prevent data errors in production systems.

## Task

Create a comprehensive field mapping implementation guide that transforms the source data structure to match the target API schema. Include systematic analysis, transformation logic, validation rules, and edge case handling.

## Context

{{integration-requirements}}

The mapping must account for structural differences, data type mismatches, nested object restructuring, array transformations, and API validation constraints. Design fallback mechanisms for missing or invalid data and establish validation checkpoints to ensure compliance.

## Output

Structure your guide with these sections:

**Mapping Analysis**
- Structural differences between source and target schemas
- Data type mismatches and conversion requirements
- Nested object and array transformation needs

**Transformation Rules**
- Field name translations and path mappings
- Data type conversion logic
- Conditional mapping rules
- Array flattening and object nesting strategies
- Data format standardization

**Validation Logic**
- Pre-transformation data quality checks
- Post-transformation API compliance validation
- Default value insertion rules
- Error handling for edge cases

**Implementation Steps**
- Step-by-step transformation workflow
- Code examples demonstrating key transformations
- Testing strategy for validation

Provide detailed explanations with code examples for each transformation rule and validation checkpoint.
```

## 用法 / Usage
- 必填變數 / Variables: {{integration-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Map Payload Fields for API Integration is a free AI prompt that creates detailed field mapping implementat…
