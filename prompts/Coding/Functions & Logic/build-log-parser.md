# Log Parser Builder for Structured Data Extraction

## 簡介

The Log Parser Builder for Structured Data Extraction is a free AI prompt that creates custom log parsers to extract, filter, and analyze raw log data for engineers and security professionals. This log parser prompt for ChatGPT takes your log samples and parsing requirements and builds a complete solution that identifies patterns, extracts key fields (timestamps, log levels, error codes, IP addresses, user identifiers), applies severity and time-range filters, and generates summary statistics. It runs on ChatGPT, Claude, and Cursor, producing ready-to-implement parsing logic with regex patterns and code blocks alongside sample parsed output in JSON or CSV format. Real use cases include parsing application logs for debugging, analyzing web server access logs for security audits, extracting metrics from system logs for observability dashboards, and processing event streams for compliance reporting. Reach for this prompt when you need to turn messy log files into clean, structured datasets for downstream analysis or monitoring workflows. ● Identifies recurring patterns, delimiters, and field structures in your raw log samples automatically ● Generates regex patterns and parsing logic in executable code blocks tailored to your specific log format ● Applies filters by severity level (DEBUG through CRITICAL) and custom time ranges as specified ● Produces summary statistics including error frequency distribution, peak activity windows, common issues, and behavioral trends ## Prompt

```
## Role
You are an expert log analysis engineer specializing in parsing unstructured log data into structured, queryable formats.

## Task
Create a comprehensive log parser that extracts key fields, applies filters, and generates summary statistics from raw log entries.

## Context
Raw logs contain valuable information about system behavior, security incidents, and performance bottlenecks, but require systematic pattern recognition and field extraction to become actionable. Your parser should identify recurring patterns, delimiters, and data structures, then extract standard fields (timestamps, log levels, source components, error codes, IP addresses, user identifiers, message content) using regex or parsing rules. Apply filtering by severity (DEBUG, INFO, WARN, ERROR, CRITICAL) and time ranges as specified. Generate summary statistics including error frequency, peak activity periods, common issues, and trends.

{{log-samples}}

{{parsing-requirements}}

## Output
Structure your response with:

1. **Pattern Analysis** – Identify recurring patterns, delimiters, and field structures in the logs
2. **Parsing Rules** – Provide regex patterns or parsing logic in code blocks
3. **Sample Output** – Show parsed data in the requested format with consistent field naming and data types
4. **Summary Statistics** – Include error frequency, peak activity periods, common issues, and trend analysis

Deliver parser logic ready for implementation and sample parsed output demonstrating the transformation.
```

## 用法 / Usage
- 必填變數 / Variables: {{log-samples}}、{{parsing-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Log Parser Builder for Structured Data Extraction is a free AI prompt that creates custom log parsers to e…
