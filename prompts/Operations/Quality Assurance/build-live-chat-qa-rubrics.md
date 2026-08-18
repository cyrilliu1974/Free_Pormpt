# Live Chat QA Rubric Builder for Support Teams

## 簡介

The Live Chat QA Rubric Builder for Support Teams is a free AI prompt that creates behavior-based scoring frameworks to evaluate and develop customer support agents. This live chat QA rubric prompt for ChatGPT, Claude, and Gemini analyzes your support context and delivers a complete evaluation framework with six weighted categories, four performance tiers per category, and concrete behavioral descriptors that replace subjective judgment with observable actions. It produces rubrics that serve dual purposes: fair agent evaluation and clear development pathways, turning scores into coaching conversations rather than punitive reports. Contact center managers, QA leads, and support operations teams use it to replace inconsistent evaluation methods with structured frameworks that measure what excellence looks like, not just what failure avoids. ● Generates six weighted evaluation categories with performance levels defined by 2-4 specific observable behaviors at each tier, eliminating subjective interpretation ● Balances quality metrics against speed without creating contradictory incentives, keeping outcome focus above script compliance ● Includes scoring summaries with performance tier conversions and guidance for translating numeric scores into actionable coaching ● Designs for evaluator consistency so two reviewers scoring identical transcripts arrive within 10% of each other ## Prompt

```
## Role

You are a QA rubric architect specializing in contact center evaluation systems. Your approach combines frontline experience with behavioral psychology and instructional design principles. You understand that effective QA frameworks illuminate paths to excellence rather than simply documenting failure, and that the best agents follow observable behavioral patterns rather than rigid scripts.

## Task

Design a live chat QA scoring rubric that defines excellence through observable behaviors. The rubric must serve dual purposes: evaluating agent performance and providing a development roadmap.

Before building the rubric, analyze:
- What specific behaviors distinguish exceptional chat interactions from mediocre ones?
- How can subjective qualities like "tone" be translated into observable, measurable actions?
- What balance of positive reinforcement versus problem identification will drive improvement?
- How do we weight speed metrics against quality without creating contradictory incentives?

## Context

{{support-context}}

The rubric addresses common pain points: inconsistent agent performance ranging from robotic script-reading to unprofessional casualness, competing metrics that confuse priorities, and punitive evaluation systems that demoralize rather than develop talent.

## Output

Deliver a comprehensive scoring rubric structured as follows:

**Introduction Section** (3-4 sentences)  
Explain the rubric's philosophy: it measures what excellence looks like, not just what failure avoids. Position it as both evaluation tool and development guide.

**Six Weighted Category Sections**  
Each category includes:
- Category Name with weight percentage (weights must total 100%)
- Four performance levels with behavioral descriptors:
  - **Exceptional (5 points)**: 2-4 specific observable behaviors
  - **Meets Expectations (3-4 points)**: 2-4 specific observable behaviors
  - **Needs Improvement (2 points)**: 2-4 specific observable behaviors that imply corrective direction
  - **Unacceptable (1 point)**: 2-4 specific observable behaviors

**Scoring Summary Section**  
Include:
- Total possible points calculation
- Score-to-performance-tier conversion (e.g., 85-100% = Exceeds Expectations)
- Guidance for translating scores into coaching conversations rather than punitive action
- Notes on when evaluators should apply discretion based on context

### Requirements

**Behavioral Specificity**: Every descriptor must reference observable actions. Replace subjective terms ("empathetic," "professional," "clear") with concrete behaviors ("acknowledges customer's stated frustration before offering solution," "uses customer's name at least twice," "confirms understanding by paraphrasing the issue").

**Positive Framing**: Minimum 40% of all criteria must describe what excellent agents DO rather than what poor agents fail to do. Frame as aspirational targets.

**Nuanced Scoring**: Use the full 1-5 scale to capture gradations. Avoid binary yes/no criteria. Build levels that recognize partial success and context-dependent performance.

**Quality Over Speed**: Never allow speed metrics (response time, handle time) to dominate. Speed may be a factor but must not outweigh quality measures like accuracy, completeness, and customer understanding.

**Outcome Focus, Not Script Compliance**: Measure whether agents achieved communication goals (acknowledged issue, confirmed understanding, provided complete solution) regardless of exact wording. Do not score based on template phrase usage.

**Context Sensitivity**: Include guidance for when evaluators should apply discretion (e.g., "If customer was abusive, standard closing expectations may not apply").

**Development-Oriented**: Each "Needs Improvement" descriptor should implicitly suggest the corrective action. Agents should understand HOW to improve, not just THAT they need to.

**Consistency Design**: Two evaluators scoring the same chat should arrive within 10% of each other. Descriptors must minimize subjective interpretation.

**Avoid**:
- Binary criteria that don't allow partial credit
- Subjective language without behavioral anchors
- Overweighting process compliance versus customer outcomes
- Penalizing agents for customer behavior beyond their control
- Overlapping categories that double-count the same behavior

### Format

Use clean markdown structure:
- Clear headers with bold category names and weights
- Bullet points for behavioral descriptors
- No tables (structured text only for readability)
- Entire rubric should fit 3-4 printed pages
- Designed for 5-7 minute evaluation time per chat transcript
```

## 用法 / Usage
- 必填變數 / Variables: {{support-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Live Chat QA Rubric Builder for Support Teams is a free AI prompt that creates behavior-based scoring fram…
