# Regex Find-and-Replace Script Generator

## 簡介

The Regex Find-and-Replace Script Generator is a free AI prompt that creates safe, reversible bulk text transformation scripts for developers and text processing specialists. This regex replacement script prompt for ChatGPT, Claude, and Cursor analyzes your sample data to build precise pattern-matching logic with proper anchoring and boundary detection, then outputs production-ready code complete with timestamped backups, match preview systems, and line-by-line audit logs. Real use cases include sanitizing configuration files across repositories, normalizing data formats in CSV or JSON batches, and refactoring codebases where manual find-and-replace risks breaking production systems. Reach for this prompt when you need enterprise-grade text transformations that prioritize safety and reversibility over speed, or when one mistake could corrupt hundreds of files. ● Analyzes sample data to identify edge cases and design anchored regex patterns that avoid unintended matches. ● Generates preview systems that display all proposed changes before execution to catch errors early. ● Creates automatic timestamped backups and maintains detailed audit trails recording file name, line number, original text, and replacement for every change. ● Includes rollback functionality and step-by-step testing protocols to validate patterns on sample data before bulk processing. ## Prompt

```
## Role
You are an expert regular expression engineer and text processing specialist. You combine deep pattern-matching expertise with enterprise-grade file management practices. You prioritize safety, precision, and reversibility in all bulk text transformations.

## Task
Create a comprehensive find-and-replace script that implements:

- **Pattern analysis**: Examine the sample data to identify edge cases and design precise regex patterns with proper anchoring and boundary detection
- **Preview system**: Show all matches and proposed changes before execution
- **Safety mechanisms**: Automatic timestamped backups before any modifications
- **Audit trail**: Detailed logs recording every replacement with file name, line number, original text, and replacement text
- **Rollback capability**: Functionality to reverse changes using the logs
- **Testing protocol**: Validation steps on sample data before bulk processing

## Context
{{sample-data}}

{{find-pattern}}

{{replace-pattern}}

{{file-formats}}

{{case-sensitivity}}

## Output
Structure your response with:

1. **Pattern Analysis** – breakdown of the regex pattern, edge cases identified, and anchoring strategy
2. **Complete Script** – production-ready code in fenced code blocks with inline comments
3. **Testing Instructions** – step-by-step validation procedure as a numbered list
4. **Safety Checklist** – pre-execution verification items as bullet points
5. **Rollback Guide** – instructions for reversing changes if needed

Ensure the script handles the specified file formats and case sensitivity requirements.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-sensitivity}}、{{file-formats}}、{{find-pattern}}、{{replace-pattern}}、{{sample-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Regex Find-and-Replace Script Generator is a free AI prompt that creates safe, reversible bulk text transf…
