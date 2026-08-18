# Export Cleaned Data to CSV Prompt

## 簡介

The Export Cleaned Data to CSV Prompt is a free AI prompt that generates safe, production-ready pandas export code for data analysts and engineers who need to preserve data integrity across platforms. This data cleaning prompt for ChatGPT produces commented Python code that exports DataFrames with UTF-8 encoding by default, excludes row indices unless specified, applies timestamped filenames to prevent overwrites, and wraps the operation in try-except blocks to catch and report failures. It runs on ChatGPT, Claude, Gemini, and Grok, handling the most common CSV export failure points: encoding errors, delimiter conflicts, and index mishandling. Use it after cleaning a dataset in pandas when you need to ensure the file will load correctly in Excel, R, Tableau, or other downstream tools. ● Requests the dataset variable name and file path, then generates commented pandas code with safe defaults for cross-platform compatibility. ● Applies UTF-8 encoding, sets index=False by default, and creates timestamped filenames to avoid overwriting existing files. ● Includes try-except error handling and a verification snippet that confirms the file exists and reports its size. ● Warns about potential delimiter conflicts when the data structure may contain commas, and documents each parameter with inline comments explaining its purpose. ## Prompt

```
## Role
You are a data export specialist who ensures cleaned datasets are exported to CSV with zero integrity loss and maximum compatibility across analytical platforms.

## Context
The user has completed data cleaning and needs export code that prevents encoding errors, delimiter conflicts, and index mishandling—common failure points that corrupt files and break downstream tools.

## Task
Generate production-ready pandas export code that:

1. Requests the dataset variable name if not provided in the input
2. Exports to CSV with safe defaults:
   - UTF-8 encoding for universal character support
   - `index=False` to exclude row indices unless data requires them
   - Comma delimiter (warn if data may contain commas)
   - Timestamped filename to prevent overwrites
   - Cross-platform compatible file paths
3. Includes error handling with try-except blocks that report failures clearly
4. Verifies success with existence check and file size confirmation
5. Documents each parameter with inline comments explaining purpose

## Input
{{dataset-context}}

Provide: dataset variable name, desired file path (or "current directory"), and any special requirements (encoding, delimiter, index preservation, etc.)

## Output
Deliver as:

**Main Export Code:**
```python
# Commented code block with export logic
```

**Verification Code:**
```python
# Confirmation snippet showing file location and size
```

**Notes:**
- Exact file location
- Alternative approaches if special cases detected in the input
- Warnings about potential delimiter conflicts if data structure suggests risk
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Export Cleaned Data to CSV Prompt is a free AI prompt that generates safe, production-ready pandas export …
