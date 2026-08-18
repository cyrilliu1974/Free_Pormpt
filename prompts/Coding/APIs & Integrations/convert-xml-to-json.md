# XML to JSON Conversion Code Generator

## 簡介

The XML to JSON Conversion Code Generator is a free AI prompt that produces transformation code to migrate XML data into modern JSON structures for developers and data engineers. This XML to JSON conversion prompt for ChatGPT analyzes XML samples, applies your conversion rules, and generates production-ready code in your target language that handles namespaces, attributes, mixed content, and array detection while maintaining data integrity. It runs on ChatGPT, Claude, and code editors like Cursor, delivering structured analysis of your XML hierarchy followed by transformation code with error handling, inline comments, and clean output formatting. Use it when integrating legacy XML systems with JSON-based APIs, migrating data pipelines, or building ETL workflows that require reliable structural mapping. ● Analyzes XML hierarchy depth, attribute placement, namespace prefixes, and repeating elements to identify conversion requirements. ● Designs transformation rules that map XML elements to JSON keys, handle attributes with your chosen convention, and detect array patterns automatically. ● Generates implementation code with validation logic, error handling, detailed inline comments, and syntax highlighting for your target programming language. ● Ensures output JSON follows modern API standards for nested structures and is ready for production integration. ## Prompt

```
## Role

You are an expert data transformation engineer specializing in XML-to-JSON conversion, structured data migration, and cross-platform data interoperability.

## Task

Analyze the provided XML samples and generate clean, efficient transformation code that converts XML to JSON while preserving data hierarchy and meeting modern API standards.

## Context

XML's element-attribute model requires careful mapping to JSON's key-value structure. Handle:

- Namespaces and namespace declarations
- XML attributes (convert using the specified convention)
- Mixed content and nested hierarchy
- Array detection where multiple elements share the same name
- Repeating elements that must become JSON arrays

Follow these conversion principles:

- XML elements → JSON objects or keys
- Attributes → special properties per the specified convention
- Namespace information → preserve or strip as specified
- Repeated elements → JSON arrays with proper detection
- Output → clean, readable JSON matching industry API conventions

## Input

**XML samples:**
{{xml-samples}}

**Conversion rules:**
{{conversion-rules}}

**Target programming language:**
{{programming-language}}

## Output

Provide your response in these sections:

### 1. XML Structure Analysis
- Hierarchy depth and nesting patterns
- Attribute usage and placement
- Namespace declarations and prefixes
- Repeating elements and array candidates

### 2. Transformation Rules
- Element-to-key mapping strategy
- Attribute naming convention
- Namespace handling approach
- Array detection logic

### 3. Implementation Code

Deliver transformation code with:
- Proper error handling and validation
- Detailed inline comments explaining each conversion step
- Clean output formatting
- Syntax highlighting

Ensure the generated JSON follows modern API standards for nested data structures and is production-ready.
```

## 用法 / Usage
- 必填變數 / Variables: {{conversion-rules}}、{{programming-language}}、{{xml-samples}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Skills_Catalog_Node_Extractor
- 適用 / Use when: The XML to JSON Conversion Code Generator is a free AI prompt that produces transformation code to migrate XML…
