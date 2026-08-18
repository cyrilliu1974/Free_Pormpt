# ML Training Checklist Generator for Production Readiness

## 簡介

The ML Training Checklist Generator for Production Readiness is a free AI prompt that creates sequential, audit-ready ML training workflows for data science and engineering teams recovering from costly deployment failures. This ML training checklist prompt for ChatGPT, Claude, Gemini, and Grok produces a structured three-phase workflow covering pre-training verification (data validation, environment setup, baseline establishment), during-training monitoring (convergence signals, performance degradation, system health), and post-training validation (reproducibility confirmation, production-readiness gates). Each checklist item includes a checkbox-ready action step, quantitative success criteria with specific thresholds, the failure mode it prevents, and a quick verification method using commands or scripts. The prompt draws on Chip Huyen's machine learning systems methodology to address data validation gaps, missing baselines, convergence failures, and reproducibility breakdowns before they reach production. Reach for this prompt when your ML team operates under delivery pressure while stakeholders demand bulletproof reproducibility, or when past failures require a systematic approach to catch issues early. ● Tailors checklists to your specific failure history and technical environment using {{failure-context}} and {{technical-stack}} variables ● Provides quantitative thresholds and verification commands instead of vague "looks good" guidance ● Structures items sequentially so each validation step builds on prior confirmations ● Flags commonly skipped critical items with warning callouts to prevent assumption-based gaps ## Prompt

```
## Role

You are an ML systems architect building a pre-deployment training checklist for a team recovering from costly ML failures. Draw on Chip Huyen's *Designing Machine Learning Systems* methodology to create a sequential, audit-ready workflow that prevents data validation gaps, missing baselines, convergence failures, and reproducibility breakdowns.

## Context

{{failure-context}}

The team operates under delivery pressure while stakeholders require bulletproof reproducibility. Every checklist item must catch a specific failure mode before it reaches production.

## Task

Create a comprehensive ML training checklist structured in three phases:

### 1. Pre-Training Verification
Data validation, environment setup, and baseline establishment before training begins.

### 2. During-Training Monitoring
Real-time convergence signals, performance degradation checks, and system health indicators.

### 3. Post-Training Validation
Reproducibility confirmation and production-readiness gates.

**For each checklist item, provide:**
- Clear, actionable step (checkbox-ready)
- Quantitative success criteria (specific thresholds, not "looks good")
- The common failure mode it prevents
- Quick verification method (command, script, or manual check)

Prioritize items sequentially—each step must build on prior validations. Make no assumptions; explicitly verify even "obvious" preconditions. Include both automated checks and critical manual verification points. Reference Huyen framework tools/methods where applicable.

## Output

Format as a structured checklist with:
- Checkboxes for each item
- Numbered steps within each phase
- Sub-bullets for success criteria, failure prevention, and verification
- Warning callouts for commonly skipped critical items
- Quick-reference sections for commands or validation snippets
- Print-friendly layout for physical check-off during training runs

**Avoid** generic theory, vague advice, or assuming perfect conditions. Every item must be directly actionable by an engineer under resource constraints.

---

**Technical environment:**  
{{technical-stack}}
```

## 用法 / Usage
- 必填變數 / Variables: {{failure-context}}、{{technical-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The ML Training Checklist Generator for Production Readiness is a free AI prompt that creates sequential, audi…
