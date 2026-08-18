# Excel to CSV Converter Script Builder

## 簡介

The Excel to CSV Converter Script Builder is a free AI prompt that generates robust Python conversion scripts for developers and data engineers working with Excel data. This Excel to CSV converter prompt for ChatGPT produces complete, commented Python code that handles multiple sheets, preserves data types (dates, numbers, text, formulas), manages empty cells, and gracefully handles edge cases like special characters and large files. It runs on ChatGPT, Claude, and Cursor, generating scripts with clear error handling, minimal dependencies, and intuitive file naming conventions derived from sheet names. Real-world use cases include automating data migration pipelines, batch-processing Excel reports for analytics systems, and building reliable data extraction workflows that require preserving formatting and data types during conversion. Reach for this prompt when you need a maintainable, production-ready Excel-to-CSV script that follows UNIX philosophy - single-purpose, composable, and robust. ● Handles multiple sheets with automatic or manual selection, converting each to a separate CSV file with clear naming conventions ● Preserves data integrity across dates, numbers, text, and formulas while managing empty cells and special characters ● Includes comprehensive error handling with actionable messages for file access issues, invalid sheets, and corrupted workbooks ● Delivers well-documented code with installation commands, usage examples, docstrings, and separation of validation, conversion, and execution logic ## Prompt

```
## Role
You are an automation architect specializing in robust data conversion scripts. You prioritize data integrity, clear error handling, and maintainable code that follows UNIX philosophy.

## Task
Create a production-grade Python script that converts Excel workbooks to CSV format while preserving data integrity. Handle multiple sheets, various data types (dates, numbers, text, formulas), empty cells, and common edge cases.

## Context
{{conversion-requirements}}

The script must be:
- **Single-purpose**: Excel → CSV conversion only, composable with other tools
- **Robust**: Handle edge cases (mixed data types, empty cells, special characters, large files) with clear error messages
- **Portable**: Minimal dependencies, well-documented
- **User-friendly**: Intuitive file naming derived from sheet names, clear usage examples

## Output
Provide a complete, commented Python script with:

1. **Dependencies** - Required libraries with installation commands
2. **Configuration** - File path validation, sheet selection logic (by name or index)
3. **Core conversion logic** - Sheet extraction, data type detection and preservation, empty cell handling
4. **Error handling** - Graceful failures with actionable messages for common issues (file not found, invalid sheet, permission errors, corrupted workbooks)
5. **Output management** - Clean CSV generation with sheet-based naming convention in specified directory
6. **Documentation** - Docstrings for each function, usage examples demonstrating common scenarios

Structure code with clear separation of concerns: validation functions, conversion functions, error handling, and main execution flow. Include inline comments explaining non-obvious logic, especially around data type preservation and edge case handling.
```

## 用法 / Usage
- 必填變數 / Variables: {{conversion-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Skills_Catalog_Node_Extractor
- 適用 / Use when: The Excel to CSV Converter Script Builder is a free AI prompt that generates robust Python conversion scripts …
