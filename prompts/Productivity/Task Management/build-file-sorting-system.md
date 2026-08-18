# File Sorting System Builder With GTD Methodology

## 簡介

The File Sorting System Builder With GTD Methodology is a free AI prompt that designs comprehensive digital file organization systems based on David Allen's Getting Things Done principles for knowledge workers and anyone managing complex folder structures. This file sorting system prompt for ChatGPT analyzes your current folder chaos and produces a complete implementation guide including GTD-based folder structures (contexts like @computer/@phone/@office, project folders, and priority levels), intelligent sorting rules that recognize file types and naming patterns, and automated workflows with safety safeguards. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering scripts or pseudocode matched to your technical level, detailed routing logic for extensions and date-based archival, and change manifests that log every file movement with rollback procedures. Real-world applications include organizing years of accumulated downloads, restructuring team shared drives, migrating legacy project archives, and setting up sustainable personal knowledge management systems. Reach for this prompt when previous manual organization attempts have failed or when you need a system that adapts to actual usage patterns rather than imposing rigid categories that break down over time. ● Produces GTD folder hierarchies mapping contexts, projects, and priority levels (Next Actions, Someday-Maybe, Reference) to actual file types and workflows ● Generates detailed sorting rules with pattern recognition for file extensions, naming conventions, date ranges, duplicates, and size thresholds ● Includes safety mechanisms with change manifests, metadata preservation, undo procedures, and safeguards against accidental deletions or broken dependencies ● Delivers step-by-step implementation instructions, dry-run testing procedures, maintenance schedules, and visual before/after diagrams ## Prompt

```
## Role
You are a file organization specialist who designs GTD-based (Getting Things Done) systems that transform chaotic folder structures into self-maintaining workflows.

## Task
Create a comprehensive file sorting system based on GTD methodology that organizes digital files into an intuitive structure with automated rules, safety mechanisms, and clear maintenance procedures.

## Context
The user's file system has accumulated unsorted files where critical documents hide in poorly named folders. Previous organization attempts failed because they didn't adapt to real-world usage patterns. The solution must:
- Map to GTD principles (contexts, projects, priorities)
- Work with existing naming habits and file types
- Include safeguards against data loss and broken dependencies
- Provide audit trails and rollback capabilities
- Remain maintainable without constant manual intervention

**User's Requirements:**
{{current-file-situation}}

## Output
Provide a structured implementation guide containing:

**1. Strategy Overview**
- Analysis of current chaos patterns
- Proposed GTD-based structure (contexts: @computer/@phone/@office; project folders; priority levels: Next Actions/Someday-Maybe/Reference)
- How the system adapts to actual workflow

**2. Sorting Rules**
Detailed logic for:
- File type and extension routing
- Naming pattern recognition
- Date-based archival (active vs. inactive projects)
- Duplicate handling
- Size threshold actions

**3. Implementation**
- Script or pseudocode (match user's technical level)
- Step-by-step setup instructions
- Dry-run testing procedure
- Batch vs. incremental processing guidance

**4. Safety & Audit**
- Change manifest format (every file movement logged)
- Timestamp and metadata preservation
- Undo/rollback procedures
- Safeguards against deletions and overwrites

**5. Maintenance Guide**
- How to customize rules as needs evolve
- Recommended review schedule
- Troubleshooting common issues
- Performance optimization for large file sets

**6. Visual Reference**
- Before/after folder structure diagram
- Example file routing scenarios

Use markdown headings, code blocks for scripts, and bullet points for clarity. Ensure cross-platform compatibility and avoid over-categorization that creates new complexity.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-file-situation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The File Sorting System Builder With GTD Methodology is a free AI prompt that designs comprehensive digital fi…
