# Backup Automation Script Generator

## 簡介

The Backup Automation Script Generator is a free AI prompt that creates production-ready backup automation scripts implementing the 3-2-1 data protection strategy for system administrators and DevOps engineers. This backup automation script prompt for ChatGPT, Claude, and Cursor generates executable code that creates three copies of your data across two different media types with one offsite location. The prompt produces complete scripts with intelligent scheduling for incremental and full backups, checksum verification to detect silent corruption, configurable compression, automatic retention rotation (daily, weekly, monthly), and detailed logging. It handles edge cases like network failures, partial completions, and storage limits while prioritizing recovery speed and vendor lock-in avoidance through open formats. Reach for this prompt when you need to implement or upgrade backup automation that must survive real-world infrastructure failures and support fast disaster recovery. ● Produces executable scripts with dependency lists, OS compatibility notes, and configuration templates explaining every parameter. ● Implements strict 3-2-1 backup strategy with local, network/external, and cloud/offsite copies built into the automation. ● Includes deployment instructions with cron and task scheduler commands plus emergency recovery checklists. ● Generates troubleshooting guides organized by failure scenario to accelerate diagnosis during outages. ## Prompt

```
## Role

You are a backup automation architect specializing in data loss prevention and disaster recovery.

## Task

Create production-ready backup automation scripts implementing the 3-2-1 strategy (three copies, two different media, one offsite) with verification, rotation, and recovery testing built in.

## Context

Backup requirements:
{{backup-requirements}}

Target platform(s):
{{target-platform}}

## Requirements

**Architecture:**
- Implement strict 3-2-1 strategy: local copy, network/external copy, cloud/offsite copy
- Handle edge cases: network failures, partial completions, storage limits
- Use open formats to avoid vendor lock-in

**Core Features:**
- Intelligent scheduling for incremental and full backups
- Checksum verification for every file to detect silent corruption
- Configurable compression balancing storage efficiency and recovery speed
- Automatic rotation managing retention: daily (7 days), weekly (4 weeks), monthly (12 months)
- Detailed logging that is human-readable during crises and machine-parseable for analysis

**Reliability:**
- Build resilience assuming network and storage unreliability
- Never trust completion without verification
- Prioritize recovery speed in design decisions
- Include recovery testing procedures as part of automation

## Output

Provide:

1. **Executable code** with headers listing dependencies and OS compatibility
2. **Configuration templates** with parameter explanations and examples
3. **Deployment instructions** including cron/task scheduler setup commands
4. **Recovery procedures** formatted as emergency checklists
5. **Troubleshooting guide** organized by failure scenario

Use code blocks for scripts, tables for configuration options, and numbered lists for procedures.
```

## 用法 / Usage
- 必填變數 / Variables: {{backup-requirements}}、{{target-platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Agent_Runtime_Charter_Design
- 適用 / Use when: The Backup Automation Script Generator is a free AI prompt that creates production-ready backup automation scr…
