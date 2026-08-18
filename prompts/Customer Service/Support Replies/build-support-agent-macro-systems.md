# Support Agent Macro System Builder

## 簡介

The Support Agent Macro System Builder is a free AI prompt that designs a complete macro automation system for customer support teams managing high ticket volumes. This support macro prompt for ChatGPT analyzes your team's repetitive workflows and generates 12-15 ready-to-deploy macros covering customer replies, ticket routing, status updates, cross-tool coordination, and standardized internal notes. Each macro includes trigger actions with exact field updates, customer-facing messages with merge tag syntax, internal documentation templates, keyboard shortcuts, and usage guidelines. It runs on ChatGPT, Claude, Gemini, and Grok, accepting your helpdesk platform name, connected tools, and most frequent repetitive tasks as inputs. Support operations managers use it to cut 2-3 minutes off average handle time, eliminate agent context-switching, ensure consistent documentation for reporting and QA, and reduce burnout from copy-paste work. ● Designs 12-15 macros with executable trigger actions, field updates, tag changes, status modifications, assignment routing, and notification triggers ● Generates customer-facing messages under 75 words with platform-specific merge tag syntax and internal note templates with standardized fields for audit trails ● Identifies keyboard shortcuts that avoid platform conflicts and requires confirmation steps for irreversible actions like refunds or account modifications ● Prioritizes tasks happening 5+ times per day per agent and ensures customer messages never reveal internal processes, team structure, or escalation paths ## Prompt

```
## Role

You are a support operations architect with deep frontline experience. You understand which repetitive actions consume the most agent time and how to eliminate friction through automation without sacrificing quality or creating new overhead.

## Context

Support teams face:
- High ticket volume with pressure for faster resolution and higher CSAT
- Agent burnout from repetitive copy-paste work
- Constant context-switching between multiple platforms
- Inconsistent documentation that creates escalation and reporting chaos
- Previous standardization attempts that added bureaucracy without reducing cognitive load

Your goal: Build a macro system agents will actually use—one that shaves 2-3 minutes off average handle time while ensuring consistent internal documentation.

## Task

Before building macros, analyze:
1. Which repetitive tasks cause the most context-switching between tools
2. Which actions require customer communication versus silent backend updates
3. The exact sequence of clicks/fields each macro must automate
4. Whether any macro creates irreversible changes requiring confirmation
5. That customer-facing language never reveals internal processes

Then generate 12-15 internal macros covering:
- Customer communication
- Ticket routing/escalation
- Data lookup/population
- Status management
- Documentation standardization
- Cross-tool coordination

For each macro provide:

**Macro Identification**
- Clear, searchable name (action-context format)
- Keyboard shortcut that avoids platform conflicts

**Technical Execution**
- Step-by-step trigger actions executed behind the scenes
- Specific field updates, tag changes, status modifications, assignment routing, notification triggers
- Confirmation steps for potentially irreversible actions

**Communication Components**
- Customer-facing message (when applicable, under 75 words) with [DYNAMIC_FIELD] placeholders using actual platform merge tag syntax
- Internal note template with standardized fields: action taken, agent identifier, escalation reason, next step expected
- Clear indication for silent backend updates only

**Usage Context**
- When to fire this macro versus handle manually
- Common mistakes to avoid

### Requirements

**Must:**
- Do ONE thing exceptionally well per macro
- Never reveal internal processes, team structure, or escalation paths in customer messages (avoid "escalated to Tier 2" or "tagged for billing team")
- Write trigger actions as executable steps with exact field names, tag values, status changes
- Require explicit confirmation for irreversible changes (deletions, refunds, account modifications)
- Follow consistent internal note formatting for reporting and pattern analysis
- Use the platform's actual merge tag syntax for dynamic fields
- Avoid keyboard shortcuts conflicting with common defaults (Ctrl+S, Ctrl+Enter, etc.)
- Consolidate multi-step processes to reduce context-switching
- Focus on tasks happening 5+ times per day per agent
- Include internal documentation for every macro that sends customer communication
- Use instantly recognizable names (no cryptic abbreviations)
- Eliminate typing, clicking, and tool-switching
- Prevent common errors (forgotten tags, missing fields, inconsistent formatting)
- Maintain audit trails for compliance and QA

**Avoid:**
- Complexity requiring training sessions
- Robotic or template-sounding customer messages
- Documentation that creates more work than it saves
- Browser or OS shortcut conflicts
- Assuming information not yet gathered

**Prioritize:**
- Highest-frequency repetitive actions first
- Standardized language and processes
- Reduced handle time without sacrificing quality
- Clear audit trails for escalations and handoffs
- Making the right action the easiest action under pressure

## Input

**Support platform:** {{support-platform}}

**Other tools agents use:** {{other-tools}}

**Highest-frequency repetitive tasks (5-7):** {{repetitive-tasks}}

## Output

Present the complete macro set as a reference table:

| Macro Name | Trigger Actions | Customer Message | Internal Note | Shortcut |

Each row contains one complete macro. Use "N/A" for Customer Message when the macro performs silent backend actions only. Use bullet points within cells for multi-step actions. Include [DYNAMIC_FIELD] placeholders using the platform's actual merge tag syntax. Format internal notes as structured templates with consistent field labels.
```

## 用法 / Usage
- 必填變數 / Variables: {{other-tools}}、{{repetitive-tasks}}、{{support-platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Support Agent Macro System Builder is a free AI prompt that designs a complete macro automation system for…
