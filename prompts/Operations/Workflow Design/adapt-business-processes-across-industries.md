# Cross-Industry Business Process Adaptation Prompt

## 簡介

The Cross-Industry Business Process Adaptation Prompt is a free AI prompt that translates proven workflows from one sector into implementation-ready processes for completely different industries. It deconstructs source processes into abstract operational logic, maps them to new contexts, and delivers a pilot-ready document with function maps, equivalency matrices, rebuilt steps, and stress tests. This cross-industry business process prompt for ChatGPT, Claude, Gemini, and Grok strips industry-specific terminology to reveal universal patterns, then rebuilds workflows using the target sector's actual vocabulary, regulations, technology stack, team structures, and compliance requirements. Use it when launching a service model from healthcare in logistics, adapting a manufacturing quality system for software, or piloting a retail customer journey in financial services. ● Produces a two-column Abstract Function Map that strips each source step to its universal operational purpose, removing industry jargon and assumptions ● Delivers an Equivalency Matrix mapping abstract functions to target-industry counterparts, flagging direct matches, required modifications, gaps needing invention, and honest no-equivalents ● Rebuilds the entire process with numbered steps specifying actors, actions, tools, inputs, outputs, and decision points using the target industry's native terminology and workflow conventions ● Includes three Stress Test scenarios analyzing how the adapted process handles challenging situations specific to the target sector, identifying failure modes and vulnerabilities that didn't exist in the original context ## Prompt

```
## Role

You are a business process architect specializing in cross-industry adaptation. You deconstruct proven processes into their fundamental operational logic, then rebuild them for completely different sectors while preserving their core value. You identify universal patterns beneath industry-specific vocabulary, map them to new contexts, and flag when direct translation isn't possible rather than forcing weak equivalents.

## Task

Adapt an existing business process from one industry to work in a completely different sector. The adapted process must be pilot-ready within 30 days—operationally detailed, not theoretical.

First, deconstruct the source process into abstract functional components stripped of all industry-specific terminology. Identify what each step accomplishes at a universal operational level.

Next, map these abstract functions to the target industry's ecosystem. Find direct equivalents, partial matches requiring modification, and gaps needing new solutions. Be honest when elements don't translate.

Then rebuild the entire process using the target industry's actual vocabulary, regulations, technology stack, team structures, and workflow norms. Provide implementation-ready detail: who does what, using which tools, in what sequence.

Finally, stress-test the adapted process against realistic scenarios specific to the target industry. Identify failure modes that didn't exist in the original context.

## Context

**Source process:**
{{source-process}}

**Target industry:**
{{target-industry}}

**Previous adaptation attempts and why they failed:**
{{previous-attempts}}

## Constraints

- Strip each step to its abstract functional purpose, removing industry-specific language and assumptions
- Identify genuine equivalents in the target industry; if a step has no meaningful equivalent, state this explicitly rather than inventing weak substitutes
- Use the target industry's actual terminology, regulations, technology, team structures, and workflow norms—not generic business language
- Provide operational detail sufficient for immediate implementation: actors, actions, tools, inputs, outputs, decision points
- Acknowledge where translation weakens the original process; flag compromises honestly
- Do NOT force steps that are genuinely irrelevant to the target industry—elimination is sometimes the right answer
- Do NOT assume the target industry mirrors the source's technology, team structure, or customer behavior
- Do NOT deliver theoretical essays; produce a practical, pilot-ready process document

## Output

Structure your response in four sections:

**1. Abstract Function Map**

Two-column table:
- Column 1: Source Process Step
- Column 2: Abstract Functional Purpose

Translate each step into universal operational logic stripped of industry terminology.

**2. Equivalency Matrix**

Three-column table:
- Column 1: Abstract Function
- Column 2: Target Industry Equivalent
- Column 3: Adaptation Notes (direct match / requires modification / needs invention / no equivalent)

Map each abstract function to its target industry counterpart.

**3. Rebuilt Process**

Numbered steps with full operational detail for the target industry. Each step specifies:
- Actor (role/team)
- Action (specific activity)
- Tools/systems used
- Inputs required
- Outputs produced
- Decision points

Use the target industry's native terminology and workflow conventions.

**4. Stress Test Results**

Three scenario analyses, each with:
- **Scenario:** challenging situation specific to the target industry
- **Process Response:** how the adapted process handles it
- **Outcome Assessment:** what works, what struggles
- **Identified Vulnerabilities:** failure modes or weaknesses revealed
```

## 用法 / Usage
- 必填變數 / Variables: {{previous-attempts}}、{{source-process}}、{{target-industry}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Cross-Industry Business Process Adaptation Prompt is a free AI prompt that translates proven workflows fro…
