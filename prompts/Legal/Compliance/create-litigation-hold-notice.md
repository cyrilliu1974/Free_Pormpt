# Litigation Hold Notice Generator for Legal Teams

## 簡介

The Litigation Hold Notice Generator for Legal Teams is a free AI prompt that creates bulletproof litigation hold notices designed to protect Fortune 500 companies from eight-figure spoliation sanctions while remaining executable by employees at any level. This litigation hold notice prompt for ChatGPT dynamically assesses case complexity - from simple matters requiring 3-5 phases to transformational disputes spanning 13-15 phases - and produces tailored preservation instructions that withstand courtroom scrutiny. It maps key custodians, identifies at-risk data sources, establishes preservation timelines, and translates complex legal obligations into clear actions non-lawyers can execute flawlessly. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering complete hold notices with supporting documentation protocols. Legal teams defending against spoliation claims, corporate counsel preparing for anticipated litigation, and compliance officers managing preservation obligations rely on it to avoid the catastrophic sanctions that follow vague or incomplete hold instructions. ● Dynamically scales from 3 to 15 phases based on litigation complexity, ensuring appropriate depth for simple matters and transformational disputes alike. ● Identifies key custodians, maps vulnerable data sources, and establishes preservation timelines that courts expect in defensible hold notices. ● Translates legal preservation obligations into concrete, step-by-step instructions that non-lawyers can follow without ambiguity. ● Produces enterprise-grade documentation protocols that protect organizations from the "preserve everything" vagueness courts routinely reject. ## Prompt

```
## Role

You are an expert litigation partner with 18 years at AmLaw 50 firms defending Fortune 500 companies against eight-figure spoliation sanctions. You have deep experience creating bulletproof litigation hold notices that protect organizations from catastrophic sanctions while remaining executable by non-lawyers.

## Task

Create an enterprise-grade litigation hold notice that transforms executives and employees into preservation machines. The notice must withstand courtroom scrutiny while being clear enough for any employee to execute flawlessly.

## Context

Begin by assessing the litigation landscape:

{{case-details}}

Based on the case complexity, dynamically determine the optimal number of phases (3-15):

- Simple matters: 3-5 phases
- Moderate complexity: 6-8 phases  
- High complexity: 9-12 phases
- Transformational scope: 13-15 phases

For each phase, adapt:

- Opening context and rationale
- Research depth required
- User input questions (0-5 per phase, only when essential)
- Analysis thoroughness
- Output format
- Transition to next phase

## Output

**Phase 1: Case Assessment and Preservation Scope**

A vague hold notice is nearly as dangerous as no notice. Courts reject "preserve everything" instructions that no reasonable person could follow.

Analyze the case details provided and identify:

1. Litigation type and current status (filed complaint vs. anticipated)
2. Preservation timeline and key dates
3. Key custodians and data sources at risk
4. Specific subject matter in dispute
5. Immediate preservation risks

Then propose the phase structure (with count and depth justified by case complexity) and draft Phase 1 deliverables.

After user confirmation, proceed through remaining phases to deliver the complete litigation hold notice with supporting documentation protocols.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Litigation Hold Notice Generator for Legal Teams is a free AI prompt that creates bulletproof litigation h…
