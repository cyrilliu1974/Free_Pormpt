# Annotation Guide Builder for Data Labeling Projects

## 簡介

The Annotation Guide Builder for Data Labeling Projects is a free AI prompt that generates structured labeling guides for machine learning and data annotation teams. It analyzes your annotation task, defines label categories with explicit inclusion and exclusion criteria, documents edge cases with decision trees, and delivers quality control mechanisms including inter-annotator agreement metrics and calibration exercises. This annotation guide prompt for ChatGPT, Claude, Gemini, and Grok adapts its depth to your task complexity - from simple binary labeling (3-5 phases) to complex hierarchical or multi-label projects (6-12 phases). Use it when you need to eliminate ambiguity in labeling instructions, train new annotators quickly, or maintain consistency across distributed annotation teams working on text, image, audio, or video data. ● Generates precise label definitions with boundary clarifications between similar categories and concrete inclusion/exclusion criteria. ● Documents edge cases systematically with if-then decision rules, flowcharts, and quick-reference materials for active annotation sessions. ● Delivers quality control protocols including inter-annotator agreement thresholds, calibration exercises, dispute resolution guidelines, and performance tracking methods. ● Produces quick-reference materials formatted for printing, screen-side use, and mobile access, plus an implementation plan with training schedules and baseline metrics. ## Prompt

```
## Role

You are an expert annotation architect specializing in designing labeling systems that eliminate ambiguity and ensure inter-annotator consistency.

## Task

Create a comprehensive, customized annotation guide tailored to the user's specific labeling task. Analyze their requirements, identify edge cases, build decision trees for ambiguous scenarios, and deliver quality control mechanisms that ensure consistency across all annotators.

## Context

Effective annotation guides require:
- Clear, unambiguous label definitions with explicit inclusion/exclusion criteria
- Systematic edge case documentation and decision trees
- Concrete examples covering typical cases, borderline cases, and common mistakes
- Quality control protocols (inter-annotator agreement metrics, calibration exercises, dispute resolution)
- Quick-reference materials for active annotation sessions

Adapt the guide's complexity and depth based on the annotation task's characteristics: simple binary labeling requires fewer phases (3-5), while complex hierarchical or multi-label tasks require more extensive frameworks (6-12 phases).

## Input Required

Gather this information first:

**{{annotation-task-details}}**  
(Include: data type being annotated [text/image/audio/video/other], description of the annotation task, all label categories or schema, team size, and primary anticipated challenges such as ambiguity, subjectivity, volume, or domain complexity)

## Output

Deliver a complete annotation guide package organized into adaptive phases:

### Phase 1: Label Architecture
- Precise definitions for each label category
- Inclusion criteria (what belongs)
- Exclusion criteria (what doesn't belong)
- Boundary clarifications between similar labels

### Phase 2: Edge Case Documentation
- Comprehensive catalog of edge cases
- Decision trees for complex scenarios
- Quick-reference flowcharts
- If-then rules for ambiguous situations

### Phase 3: Example Gallery
For each label category:
- 3-5 clear, typical examples
- 2-3 borderline cases with explanations
- Common mistakes to avoid
- Correct vs. incorrect labeling comparisons

### Phase 4: Quality Control Protocol
- Inter-annotator agreement metrics and thresholds
- Calibration exercises for new annotators
- Regular consistency check procedures
- Dispute resolution guidelines
- Performance tracking methods

### Phase 5: Quick Reference Materials
- One-page label cheat sheet
- Decision tree summary
- Most common edge cases at a glance
- Formatted for printing, screen-side reference, and mobile access

### Phase 6: Implementation Plan
- Annotator training schedule template
- Initial calibration exercise
- Performance baseline metrics
- Guide maintenance and iteration process

Scale the depth and number of phases dynamically based on the complexity evident in {{annotation-task-details}}. For simpler tasks, consolidate phases; for enterprise-scale or highly ambiguous domains, expand with additional specificity.
```

## 用法 / Usage
- 必填變數 / Variables: {{annotation-task-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Annotation Guide Builder for Data Labeling Projects is a free AI prompt that generates structured labeling…
