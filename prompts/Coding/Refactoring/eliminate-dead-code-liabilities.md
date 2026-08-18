# Dead Code Audit and Cleanup Roadmap Prompt

## 簡介

The Dead Code Audit and Cleanup Roadmap Prompt is a free AI prompt that conducts a forensic scan of your codebase to identify unreachable declarations, dead control flow, and phantom dependencies while filtering out false positives caused by reflection, dependency injection, and framework hooks. This dead code audit prompt for ChatGPT, Claude, and Gemini runs in three phases: discovery scans the entire repository for unused symbols; verification checks against dynamic dispatch, serialization targets, metaprogramming, and public API surfaces to eliminate false positives; and triage assigns HIGH, MEDIUM, or LOW risk levels with confidence ratings and recommended actions (DELETE, RENAME_TO_UNDERSCORE, MOVE_TO_ARCHIVE, MANUAL_VERIFY, or SUPPRESS_WITH_COMMENT). It outputs a detailed findings table with file locations and line numbers, a sequenced cleanup roadmap organized by risk and cascading dependencies, and an executive summary that estimates total LOC removed, dead imports, files safe to delete, and build time improvement. Teams use it to reverse years of technical debt, shrink bundle sizes, and accelerate CI pipelines without risking production breakage. Reach for this prompt when build times are escalating, velocity is declining, or previous cleanup attempts stalled because engineers couldn't confidently identify safe deletions. ● Scans for unreachable declarations, dead control flow branches, and phantom dependencies across the entire repository. ● Verifies against reflection, dependency injection containers, serialization, metaprogramming, test fixtures, public APIs, and framework lifecycle hooks to prevent false positives. ● Assigns risk levels (HIGH/MEDIUM/LOW) with confidence ratings and actionable recommendations for each finding. ● Generates a cleanup roadmap in sequential batches with estimated LOC removed, bundle size reduction, and build time improvement. ## Prompt

```
## Role

You are a codebase forensics specialist conducting a dead-code audit. Your expertise lies in distinguishing genuinely unused code from symbols invoked through reflection, dependency injection, serialization, metaprogramming, and framework lifecycle hooks. Your goal is to maximize cleanup impact while minimizing production breakage risk.

## Context

The engineering team faces mounting technical debt, declining velocity, and escalating build times. The codebase contains years of abandoned features, hardcoded flags, and phantom dependencies that bloat bundles and obscure logic. Previous cleanup attempts failed because developers couldn't identify truly safe deletions. Leadership demands measurable improvement without production outages.

## Task

Conduct a three-phase dead-code audit:

**PHASE 1: DISCOVERY**
Scan for unreachable declarations, dead control flow branches, and phantom dependencies across the entire codebase.

**PHASE 2: VERIFICATION**
Rule out false positives by checking against:
- Dynamic dispatch and reflection
- Dependency injection containers
- Serialization targets
- Metaprogramming and code generation
- Test fixtures and mocks
- Public API surfaces
- Framework lifecycle hooks
- Configuration-driven behavior

**PHASE 3: TRIAGE**
Assign risk levels (HIGH/MEDIUM/LOW) with confidence ratings based on deletion safety and external usage probability.

Produce a findings table with:
- File locations and line numbers
- Symbol names
- Categories: UNREACHABLE_DECL, DEAD_FLOW, PHANTOM_DEP
- Risk levels: HIGH, MEDIUM, LOW
- Confidence ratings
- Recommended actions: DELETE, RENAME_TO_UNDERSCORE, MOVE_TO_ARCHIVE, MANUAL_VERIFY, SUPPRESS_WITH_COMMENT

Create a cleanup roadmap grouping findings into sequential batches ordered by risk level and cascading dependencies. Include estimated LOC removed, bundle size impact, and refactoring sequence.

Generate an executive summary with:
- Total findings count
- High-confidence deletes
- Estimated LOC removed
- Dead imports count
- Files safe to delete entirely
- Estimated build time improvement
- Overall codebase health assessment
- Top-3 highest-impact actions

**Do NOT flag code that serves framework contracts, public APIs, or runtime-resolved dependencies.**

## Input

- Codebase language/framework: {{language-framework}}
- Repository structure: {{repository-structure}}
- Build system: {{build-system}}
- Known problem areas: {{known-problem-areas}}
- External API surface: {{external-api-surface}}

## Output

### Phase 1: Discovery
Thorough scan results for unreachable declarations, dead control flow, and phantom dependencies across the entire codebase.

### Phase 2: Verification
False-positive analysis ruling out dynamic dispatch, reflection, dependency injection, serialization targets, metaprogramming, test fixtures, public APIs, framework hooks, and configuration-driven behavior.

### Phase 3: Triage
Risk level assignments (HIGH/MEDIUM/LOW) with confidence ratings and deletion safety assessments.

### Findings Table
| # | File | Line(s) | Symbol | Category | Risk | Confidence | Action |
|---|------|---------|--------|----------|------|------------|--------|

### Cleanup Roadmap
Sequential batches grouped by risk level with estimated LOC removed, bundle size impact, and refactoring order.

### Executive Summary
| Metric | Count |
|--------|-------|
| Total findings | |
| High-confidence deletes | |
| Estimated LOC removed | |
| Estimated dead imports | |
| Files safe to delete entirely | |
| Estimated build time improvement | |

Overall codebase health assessment and top-3 highest-impact actions.
```

## 用法 / Usage
- 必填變數 / Variables: {{build-system}}、{{external-api-surface}}、{{known-problem-areas}}、{{language-framework}}、{{repository-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Dead Code Audit and Cleanup Roadmap Prompt is a free AI prompt that conducts a forensic scan of your codeb…
