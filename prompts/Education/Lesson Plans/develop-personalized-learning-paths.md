# Personalized Learning Path Generator for Any Subject

## 簡介

The Personalized Learning Path Generator is a free AI prompt that creates comprehensive adaptive learning frameworks for educators, instructional designers, and learning platform developers working in any subject area. This personalized learning path prompt for ChatGPT designs a complete adaptive learning system with three core components: a text-based flowchart mapping modules and decision points, a progress dashboard mockup for tracking learner performance, and explicit logic rules that dictate when and how content difficulty adjusts. It incorporates multiple assessment types - formative quizzes, summative tests, project-based evaluations, peer review, and self-reflection - and defines the branching logic for remediation and enrichment paths. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing structured output that can guide LMS configuration, curriculum design, or tutoring system development. Reach for this prompt when you need to map out how a course or training program should respond to different learner performance patterns, or when designing an adaptive system that personalizes content based on mastery thresholds and struggle indicators. ● Defines varied assessment methods and the exact conditions under which each triggers content or difficulty changes ● Produces a text-based flowchart with branching logic for remediation and enrichment paths ● Generates a progress dashboard mockup using tables, progress bars, and icons for visual clarity ● Outputs pseudocode or structured rules showing how performance scores trigger difficulty increases, decreases, or supplementary content ## Prompt

```
## Role
You are an expert adaptive learning strategist specializing in personalized learning paths, formative and summative assessment design, content customization, and performance-based difficulty adjustment.

## Task
Design a comprehensive, personalized learning path for {{subject}} that dynamically adapts to individual learner progress and performance.

## Requirements

**Assessment Strategy:**
- Incorporate varied assessment methods (formative quizzes, summative tests, project-based assessments, peer review, self-reflection) to gauge understanding at multiple levels
- Specify when and how each assessment type triggers content or difficulty adjustments

**Content Customization:**
- Define techniques for tailoring content to learner interests, prior knowledge, learning pace, and preferred modalities
- Include branching logic for remediation and enrichment paths

**Difficulty Adjustment Algorithm:**
- Create clear rules for increasing or decreasing difficulty based on assessment performance
- Specify thresholds, increments, and how the system responds to sustained struggle or mastery

## Output

Deliver your adaptive learning design in three components:

### 1. Learning Path Flowchart
Create a text-based flowchart using:
- **[Module Name (Difficulty)]** for learning modules
- **<Assessment Type>** for assessments
- **{Decision Criteria}** for branching/adaptation points
- **→** arrows to show progression
- **↻** to indicate feedback loops
- Include a symbol key

### 2. Progress Tracking Dashboard
Design a dashboard mockup as a formatted table:

```
+------------------------+-------------------+
| Learner: [Name] | Subject: {{subject}} |
+------------------------+-------------------+
| Module Completion: | Assessment Scores:|
| Module 1: ▓▓▓▓░░ 65% | Quiz 1: 78% |
| Module 2: ▓░░░░░ 15% | Project 1: 82% |
+------------------------+-------------------+
| Strengths: ✓ | Areas to Improve: ⚠ |
| • [Skill/concept] | • [Skill/concept] |
+------------------------+-------------------+
```

Use emojis, progress bars, or icons for visual clarity.

### 3. Customization & Adjustment Logic
- **Content Customization Techniques:** List 3-5 specific techniques with brief descriptions
- **Difficulty Adjustment Algorithm:** Provide pseudocode or structured rules showing exactly how performance data triggers difficulty changes

Example algorithm structure:
```
IF assessment_score >= mastery_threshold (e.g., 85%):
 → Increase difficulty +1 level OR unlock advanced module
ELSE IF assessment_score < struggle_threshold (e.g., 60%):
 → Decrease difficulty -1 level AND provide remediation
```
```

## 用法 / Usage
- 必填變數 / Variables: {{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Learning Path Generator is a free AI prompt that creates comprehensive adaptive learning fram…
