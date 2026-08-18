# Optimize DataFrame Memory Usage Prompt

## 簡介

The Optimize DataFrame Memory Usage Prompt is a free AI prompt that analyzes pandas DataFrames and produces Python code to reduce memory consumption through safe type conversions for data engineers and analysts. This DataFrame memory optimization prompt for ChatGPT walks through profiling current memory usage, identifying columns that can be converted to more efficient data types (category dtype for low-cardinality strings, downcasted integers and floats based on value ranges, nullable integer types for NaN-containing columns, and datetime64 for date strings), implementing conversions with validation checks, and reporting before-and-after memory comparisons. It runs on ChatGPT, Claude, Gemini, and Grok, producing executable Python code blocks with error handling, fallback strategies, and detailed explanations of trade-offs. Use it when working with large pandas DataFrames that cause memory bottlenecks, slow processing, or out-of-memory errors in data pipelines. ● Profiles current memory usage and data types to identify the highest-impact optimization opportunities in your DataFrame. ● Detects object columns suitable for category dtype, numeric types that can be safely downcasted, and string columns that should be datetime64. ● Implements conversions with try-except error handling, validation checks for data truncation and lost values, and fallback strategies for failed conversions. ● Produces before-and-after memory comparison tables showing MB saved, percentage reduction, and type changes per column with precision warnings. ## Prompt

```
## Role
You are a pandas memory optimization specialist. Analyze DataFrames to identify type mismatches, implement safe conversions, and reduce memory footprint without corrupting data integrity.

## Task
Transform the user's DataFrame into a type-optimized structure by:

1. **Profiling** current memory usage and data types
2. **Identifying** optimization opportunities:
   - Object columns that should be category dtype (< 50% unique values)
   - Strings that should be datetime64
   - Numeric columns using oversized int/float types
3. **Converting** types safely:
   - Category dtype for low-cardinality data
   - Appropriate int8/16/32/64 or float16/32/64 based on value ranges
   - Nullable integer types (Int8, Int16, etc.) for columns with NaN
   - datetime64 with proper format parsing
4. **Validating** all conversions:
   - Check for data truncation in numeric downcasting
   - Verify no unique values lost in categorical conversion
   - Catch non-numeric strings, invalid dates, out-of-range values
5. **Reporting** before/after memory usage (MB and %), type changes per column, and any precision warnings

## Context
{{dataset-info}}

## Output
Provide executable Python code blocks with comments explaining each step:

- Initial memory profiling
- Type detection and analysis logic
- Conversion implementation with try-except error handling and fallback strategies
- Validation checks for data integrity
- Final memory comparison in tabular format

Prioritize columns with highest memory impact. Include detailed error messages for failed conversions. Use markdown between code blocks to explain trade-offs and recommendations.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-info}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Prompt_Assembly_Audit_Engine
- 適用 / Use when: The Optimize DataFrame Memory Usage Prompt is a free AI prompt that analyzes pandas DataFrames and produces Py…
