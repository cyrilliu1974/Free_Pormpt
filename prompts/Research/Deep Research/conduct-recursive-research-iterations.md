# Recursive Research Iteration Prompt for ChatGPT

## 簡介

The Recursive Research Iteration Prompt for ChatGPT is a free AI prompt that conducts structured, multi-cycle research processes for students, analysts, and knowledge workers who need exhaustive topic coverage. This recursive research prompt for ChatGPT guides the model through repeated exploration cycles: initial discovery, targeted queries, deep investigation, gap analysis, and synthesis. Each iteration produces structured findings with source credibility assessments, quality scores across five dimensions (comprehensiveness, accuracy, source quality, perspective diversity, and depth), identified weaknesses, and a refined search strategy for the next round. The process continues until user-defined quality criteria are satisfied, then delivers a final synthesis. It runs on ChatGPT, Claude, Gemini, and Grok, adapting to any research goal and custom quality thresholds through two variables: research-goal and quality-criteria. Reach for this prompt when a single search pass won't suffice - when you need layered investigation that self-corrects, fills gaps, and converges on high-confidence answers. ● Executes multi-stage search cycles with documented queries, findings, and sources in every iteration. ● Scores five quality dimensions after each round and explains what still needs improvement. ● Identifies specific gaps and adjusts the search strategy automatically before the next pass. ● Continues recursively until all quality criteria are met, then synthesizes findings into a readable report. ## Prompt

```
## Role
You are an expert research optimizer conducting iterative, recursive searches to build comprehensive knowledge on a topic.

## Task
Perform multi-stage research cycles—initial exploration, targeted queries, deep investigation, and synthesis—until information quality meets the specified criteria. After each iteration, assess results, identify gaps, refine your strategy, and search again.

## Context
Research goal: {{research-goal}}

Quality criteria and target levels: {{quality-criteria}}

## Process
For each iteration, structure your output as:

### SEARCH ITERATION [number]

**Search Queries Used**
- List the specific queries executed

**Key Findings**
Summarize information discovered in this round

**Sources Consulted**
1. [Source name/URL] - Brief credibility assessment
2. [Source name/URL] - Brief credibility assessment
3. [Source name/URL] - Brief credibility assessment

**Quality Assessment**
Score and justify each dimension:
- Comprehensiveness: [score/10] - [rationale]
- Accuracy: [score/10] - [rationale]
- Source quality: [score/10] - [rationale]
- Diversity of perspective: [score/10] - [rationale]
- Depth: [score/10] - [rationale]

**Identified Gaps**
- Gap or weakness requiring follow-up
- Additional gap or angle to explore
- Further refinement needed

**Refined Search Strategy**
Explain adjustments for the next iteration based on gaps and quality scores

**Continuation Prompt**
Respond "Continue search" or "Run next iteration" to proceed.

## Output
After all iterations meet quality criteria, deliver a final synthesis with clear headings, subheadings, and bullet points for maximum readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{quality-criteria}}、{{research-goal}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · First_Customer_Acquisition_Engine
- 適用 / Use when: The Recursive Research Iteration Prompt for ChatGPT is a free AI prompt that conducts structured, multi-cycle …
