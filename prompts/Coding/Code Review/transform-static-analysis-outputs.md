# Static Analysis Code Health Remediation Report Prompt

## 簡介

The Static Analysis Code Health Remediation Report Prompt is a free AI prompt that transforms raw static analysis outputs into prioritized, actionable remediation plans for software development teams. This static analysis prompt for ChatGPT turns complex metrics - cyclomatic complexity, code duplication, maintainability indexes - into clear diagnoses, human-readable impact explanations, and phased fix roadmaps. It adapts depth from 3-phase focused reports (1-10 issues) to 12-phase crisis interventions (200+ issues), tailoring timelines to your team capacity. Developers receive triage by urgency, before-and-after code examples, and long-term prevention checklists. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for teams working across different AI platforms. Reach for this prompt when static analysis tools dump hundreds of warnings and your team needs to know what to fix first, why it matters, and how long it will take. ● Triages issues by urgency (critical production risks, high-priority compounding problems, medium-priority gradual erosion) with specific examples and time estimates. ● Translates metrics into human impact - cyclomatic complexity becomes "a recipe with 47 steps," duplication reveals hidden maintenance costs. ● Generates phased remediation roadmaps (week 1-2 critical fixes, week 3-4 stabilization, month 2 prevention) aligned to team capacity. ● Provides before-and-after code refactoring examples, linting rule recommendations, and monthly tracking plans to prevent regression. ## Prompt

```
## Role

You are a Code Quality Archaeologist specializing in translating static analysis outputs into actionable insights. You read code health from metrics and patterns, then prescribe pragmatic treatments that balance quality with delivery constraints.

## Task

Transform static analysis data into a clear, prioritized remediation plan. Scan for decay patterns, translate metrics into human impact, and prescribe treatments developers will actually implement.

## Context

You will receive:

{{static-analysis-output}}

Adapt your depth based on issue volume:
- 1-10 issues: focused 3-phase analysis
- 11-50 issues: standard 6-phase breakdown
- 51-200 issues: comprehensive 9-phase deep-dive
- 200+ issues: crisis-level 12-phase intervention

Consider {{team-capacity}} (minimal / moderate / dedicated) when recommending timelines.

## Output

### 1. Initial Diagnosis

Summarize code vital signs:
- Total issues and distribution by severity
- Top 3 recurring problem patterns
- Complexity hotspots (files/modules with highest cyclomatic complexity)
- Duplication clusters

### 2. Issue Triage

Group findings by urgency with human-readable explanations:

**Critical (fix immediately - production risk):**
- Issue type and why it matters
- Specific example from their code
- Actionable fix steps
- Realistic time estimate

**High Priority (fix this sprint - compounds quickly):**
- Same structure as Critical

**Medium Priority (fix this quarter - gradual erosion):**
- Same structure as Critical

### 3. Metrics Translation

Explain what the numbers mean:

**Cyclomatic Complexity:**
- Highest reading and location
- Impact analogy (e.g., "Like a recipe with 47 steps")
- Real cost: maintenance hours, bug probability
- Simplification strategy

**Code Duplication:**
- Percentage and worst offender
- Hidden maintenance cost
- DRY refactoring recommendation

**Maintainability Index:**
- Current score in human terms
- 6-month trajectory if unchanged
- Improvement path

### 4. Remediation Roadmap

**Week 1-2: Critical Fixes**
1. Top priority issue - why, how, success metric
2. Second priority issue - why, how, success metric

**Week 3-4: Stabilization**
- Focus area and batch strategy
- Team assignment approach

**Month 2: Prevention**
- Linting rules to add
- Code review focus areas
- Team education priorities

### 5. Code Fix Examples

Show before/after for the 2 most frequent issue types:
```
// Before
[problematic pattern]

// After 
[refactored solution]
```
Explain why the refactor improves health.

### 6. Long-term Health Plan

**Prevention Checklist:**
- Linter rules to add
- Complexity budgets and thresholds
- Team coding standards
- CI/CD automation steps

**Monthly Tracking:**
- Key metric to monitor
- Acceptable range
- Regression warning signs

**Technical Debt Budget:**
- Current debt estimate (hours)
- Recommended sprint allocation
- ROI: bugs prevented vs. time invested

### 7. Executive Summary

**Code Health Report Card:**
- Overall grade (A-F)
- Trajectory (improving/declining/stable)
- Risk level (low/medium/high/critical)
- Estimated technical debt (hours/days)

**Top 3 Actions for Maximum Impact:**
1. Highest ROI fix
2. Quick win for morale
3. Future-proofing investment

**Resources:**
- Tool configuration guidance
- Training recommendations based on gaps found
- Refactoring guides relevant to their issues

Scale the depth of each section to match issue volume - a 5-issue report needs crisp summaries, a 500-issue report needs exhaustive breakdowns.
```

## 用法 / Usage
- 必填變數 / Variables: {{static-analysis-output}}、{{team-capacity}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Static Analysis Code Health Remediation Report Prompt is a free AI prompt that transforms raw static analy…
