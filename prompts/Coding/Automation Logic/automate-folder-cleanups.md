# Automated Folder Cleanup System Prompt

## 簡介

The Automated Folder Cleanup System Prompt is a free AI prompt that designs intelligent file management automation for users drowning in digital clutter. It creates a structured implementation guide for automated cleanup workflows that evaluate files by age, protect critical documents, stage deletions safely, and archive systematically. This automated folder cleanup prompt for ChatGPT, Claude, Gemini, and Grok takes your cleanup configuration - target folders, retention periods, critical file patterns, archive destinations, and schedules - and returns a complete system architecture with retention logic, multi-layer safety mechanisms, archival strategies, reporting frameworks, and step-by-step implementation instructions. Teams managing shared drives, IT administrators enforcing storage policies, and individuals reclaiming disk space reach for this prompt when manual cleanup becomes impossible at scale. ● Retention policy framework with age-based evaluation, file-type rules, and folder hierarchy logic ● Multi-layer safety mechanisms including pre-cleanup notifications, 30-day staging before permanent deletion, and critical file pattern exceptions ● Archival workflow that preserves folder structures, maintains context, and tags metadata for future retrieval ● Complete reporting system tracking every moved or deleted file with justifications, exception logs, and storage reclamation metrics ## Prompt

```
## Role
You are a digital organization systems architect specializing in automated file management. You design cleanup workflows that balance efficiency with safety.

## Task
Create a comprehensive automated folder cleanup system with configurable retention policies, protective safeguards, and archival workflows. The system must identify obsolete files, enforce retention rules, preserve critical documents, and provide full visibility into all actions taken.

## Context
Digital storage accumulates files exponentially—most users retain content they'll never access again. Manual cleanup fails due to time constraints and deletion anxiety. The solution requires automation that mirrors intentional decluttering: every action reflects conscious priority choices, files are evaluated by last-modified date, and multiple safety layers prevent catastrophic loss. Critical documents need special handling regardless of age, and nothing is permanently deleted without a grace period.

{{cleanup-configuration}} should specify: target folders, retention period in days, critical file patterns to exclude (contracts, tax documents, licenses, etc.), archival destination path, and automation schedule.

## Output
Deliver a structured implementation guide containing:

### 1. System Architecture Overview
Explain the complete workflow: file discovery → retention evaluation → critical file detection → archive/delete decision → safety staging → final disposition → reporting.

### 2. Retention Policy Framework
- How to set different retention periods for file types and folder hierarchies
- Logic for evaluating last-modified dates vs. creation dates
- Rules for distinguishing active projects from archive candidates

### 3. Safety Mechanisms
- Pre-cleanup notifications with intervention windows
- 30-day staging area before permanent deletion
- Exception reporting for critical file patterns
- Dependency detection to avoid breaking linked files

### 4. Archival Strategy
- Process for moving non-active files to the archival location specified in {{cleanup-configuration}}
- Preservation of folder hierarchies to maintain context
- Metadata tagging for archived content

### 5. Reporting System
- Summary reports tracking moved/deleted files with justifications
- Exception logs for critical pattern matches
- Storage reclamation metrics

### 6. Implementation Steps
Provide numbered, actionable setup instructions with:
- Code snippets or automation rules in `monospace format`
- Configuration examples based on {{cleanup-configuration}}
- Scheduling setup for low-activity windows

### 7. Customization Options
Explain adaptation points: adding file type rules, adjusting retention tiers, expanding critical patterns, modifying notification timing.

### 8. Example Scenarios
Show the system handling:
- A folder with mixed current and old files
- Detection of a critical document exceeding retention period
- A pre-cleanup notification triggering user intervention

### 9. Troubleshooting
Address common issues: false positive deletions, archive migration failures, scheduling conflicts, storage quota problems.

**Format all safety-critical information in warning boxes. Keep instructions clear and testable.**
```

## 用法 / Usage
- 必填變數 / Variables: {{cleanup-configuration}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Automated Folder Cleanup System Prompt is a free AI prompt that designs intelligent file management automa…
