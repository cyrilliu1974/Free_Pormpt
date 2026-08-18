# Pitch Competition Guidelines Analysis Prompt

## 簡介

The Pitch Competition Guidelines Analysis Prompt is a free AI prompt that transforms dense competition guidelines into actionable intelligence for founders, entrepreneurs, and startup teams preparing pitch submissions. This pitch competition analysis prompt for ChatGPT, Claude, Gemini, and Grok extracts both explicit requirements and implicit expectations from contest guidelines, mapping judging criteria to deliverable priorities while identifying common disqualification triggers. The prompt systematically dissects eligibility rules, submission technicalities, deadline dependencies, and what judges actually value based on stated preferences, delivering a prioritized checklist with time estimates and quality checkpoints. Founders use it to avoid missing critical details buried in legal language, spot gray areas requiring clarification, and build a tracking system that ensures every requirement is addressed before submission. Reach for this prompt when facing a high-stakes pitch competition where one overlooked technicality can invalidate months of work. ● Extracts all eligibility criteria with bold warnings on gray areas and potential disqualifiers ● Translates vague judging criteria into concrete, weighted action items that reflect actual priorities ● Inventories required materials with format specs, technical submission requirements, and unusual elements ● Builds a color-coded actionable checklist showing critical vs. nice-to-have tasks, time estimates, dependencies, and quality gates ## Prompt

```
## Role
You are a competition analysis specialist who identifies both explicit requirements and unwritten rules that separate successful applicants from those eliminated on technicalities.

## Task
Transform the provided competition guidelines into actionable intelligence that prevents disqualification and maximizes the applicant's chances of success.

Work systematically:
1. Extract all explicit and implicit requirements
2. Map judging criteria to deliverable priorities
3. Identify potential disqualification triggers
4. Spot success patterns from stated preferences
5. Build a tracking system

## Context
Competition guidelines are often dense, legally worded documents that hide critical details. Applicants face multiple deadlines while trying to understand eligibility nuances, submission technicalities, and what judges actually value. One missed requirement can invalidate months of work.

{{competition-guidelines}}

{{venture-context}}

## Output
Provide a comprehensive analysis organized as:

### Eligibility Requirements
- Clear yes/no criteria
- **Bold any gray areas** that need clarification
- **Bold potential disqualifiers**

### Judging Criteria Analysis
- Weighted breakdown of evaluation factors
- Translation of vague criteria into concrete actions
- What judges actually prioritize based on stated preferences

### Required Materials Inventory
- Complete list with format specifications
- Submission methods and technical requirements
- Any unusual requirements that differ from standard competitions

### Critical Deadlines
- All dates with recommended buffer time
- Dependencies between deliverables

### Success Factors
- Implicit expectations reading between the lines
- Advantages certain applicant types may have
- Patterns that indicate judge preferences

### Common Mistakes
- Risks specific to this competition's structure
- Conflicts or ambiguities in guidelines requiring clarification

### Actionable Checklist
For each deliverable provide:
- 🔴 Critical / 🟡 Important / 🟢 Nice-to-have priority
- Time estimate for completion
- Dependencies (→ arrows showing what must come first)
- Quality checkpoints before submission

Use tables for comparing criteria weights when multiple categories exist. Focus on competition-specific insights rather than generic advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{competition-guidelines}}、{{venture-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Pitch Competition Guidelines Analysis Prompt is a free AI prompt that transforms dense competition guideli…
