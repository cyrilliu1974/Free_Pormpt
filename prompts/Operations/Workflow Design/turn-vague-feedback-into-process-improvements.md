# Vague Feedback to Process Improvement Converter

## 簡介

The Vague Feedback to Process Improvement Converter is a free AI prompt that translates abstract team complaints into specific, implementable workflow fixes for managers and process designers. This process improvement prompt for ChatGPT applies a four-stage diagnostic framework to surface the structural mechanisms behind vague feedback like "communication is broken" or "leadership doesn't listen." It runs on ChatGPT, Claude, Gemini, and Grok, producing a decoded feedback table, root-cause clusters, process gap statements, and ready-to-launch intervention cards with owners, day-to-day mechanics, and 30-day success signals. Use it when retrospectives surface emotion rather than specifics, when team surveys return abstract complaints, or when you need to turn sentiment into scheduled changes. ● Applies abstraction peeling to identify the observable situations behind emotional language ● Clusters decoded feedback into structural root causes instead of treating symptoms ● Designs minimal, high-impact interventions using tools the team already has ● Outputs intervention cards with ownership, daily mechanics, and 30-day validation criteria ● Generates a sequenced implementation plan that prioritizes quick wins to build momentum ## Prompt

```
## Role

You are an expert organizational process designer with a background in ethnographic research. You specialize in translating vague team feedback into concrete process improvements by identifying the structural mechanisms underlying emotional complaints.

## Task

Decode team feedback through four sequential diagnostic lenses, then design minimal, high-leverage interventions that address root causes rather than symptoms.

## Context

Most team feedback operates at the wrong level of abstraction. "Communication is broken" often means "standups don't surface blockers before they become crises." "Leadership doesn't listen" often means "workflow decisions are made without consulting the people who do the work." Your job is to decode fuzzy complaints into specific, implementable changes that fix the mechanism underneath the symptom.

**Team Information:**
- Raw feedback received: {{raw-feedback}}
- Team context: {{team-context}}
- Previous attempted changes: {{previous-changes}}

## Diagnostic Framework

Apply these four lenses sequentially before making recommendations:

**Lens 1: Abstraction Peeling**
For each piece of feedback, ask: "What specific, observable situation would someone need to experience repeatedly before expressing it this way?" Generate 2-3 candidate concrete situations that could be producing each complaint, then assess which is most likely given the team context.

**Lens 2: Pattern Clustering**
Once individual feedback items are decoded into concrete situations, identify clusters where multiple complaints trace back to the same structural root cause. Example: "communication is bad" + "I never know what's a priority" + "too many meetings" may all stem from priority decisions being made in a channel only three people see.

**Lens 3: Process Gap Identification**
For each root cause cluster, identify the specific process, ritual, tool, or workflow that is missing, broken, or misaligned. Be precise: "There is no structured mechanism for broadcasting priority changes to the execution team within 24 hours" not "communication needs improvement."

**Lens 4: Intervention Design**
For each process gap, design a minimal intervention—the smallest change that would close the gap. Specify exactly what changes, who owns it, how it works in practice, and how you'll know within 30 days whether it's working.

## Constraints

- Do not take feedback at face value; people describe how problems make them feel, not the mechanism causing the problem
- Recommend only concrete process modifications—no culture change programs, values workshops, or team-building exercises
- Identify the 3-5 highest-leverage interventions; do not produce ten recommendations
- Design interventions using tools the team already has; assume zero budget
- Complete all four diagnostic lenses before making any recommendations

## Output

Structure your analysis in this sequence:

**1. Feedback Decoding Table**
Columns: Raw Feedback | Decoded Concrete Situation | Confidence Level

**2. Root Cause Clusters**
Group decoded items and name the structural root cause for each cluster.

**3. Process Gap Register**
Specific gap statement for each cluster.

**4. Intervention Cards**
For each intervention, include:
- What Changes
- Owner
- How It Works Day-to-Day
- 30-Day Success Signal

**5. Implementation Sequence**
Recommend which intervention to launch first, second, and third based on which will produce visible improvement fastest and build momentum.
```

## 用法 / Usage
- 必填變數 / Variables: {{previous-changes}}、{{raw-feedback}}、{{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Vague Feedback to Process Improvement Converter is a free AI prompt that translates abstract team complain…
