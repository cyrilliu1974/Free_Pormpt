# Customer Feedback to Support Training Prompt

## 簡介

The Customer Feedback to Support Training Prompt is a free AI prompt that transforms raw customer feedback into actionable training materials for support teams. It systematically identifies recurring themes in feedback, extracts the specific skills required to address those issues, defines ideal behavioral standards, and creates realistic role-play scenarios - all grounded exclusively in actual customer voices rather than management assumptions. This customer feedback prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, and delivers a complete training roadmap organized into eight structured phases: pattern identification, skill extraction, impact analysis, ideal-response modeling, scenario building, priority ranking, feedback-loop design, and continuous-improvement planning. Use it when you need to convert survey responses, support tickets, reviews, or interview transcripts into coaching materials that frontline staff can rehearse and managers can measure. ● Surfaces 3–5 recurring themes and pain points directly from the feedback without external assumptions. ● Maps each theme to the specific support skills or behaviors required, such as handling billing disputes or managing delivery expectations. ● Creates 3–5 realistic role-play scenarios formatted as coaching scripts with 3–5 exchanges each. ● Ranks training priorities by urgency, weighing both frequency and severity, and proposes feedback loops for ongoing evaluation. ## Prompt

```
## Role
You are a customer experience strategist who translates raw customer feedback into practical training materials for support teams.

## Task
Analyze the provided customer feedback and produce actionable training points for frontline support staff. Work through each phase systematically to ensure insights are grounded in actual customer experiences.

## Context
Effective support training bridges the gap between management expectations and frontline realities. Your analysis will identify skill gaps, model ideal behaviors, and prioritize interventions based on real customer voices.

**Customer Feedback:**
{{customer-feedback}}

## Process

### Phase 1: Identify Patterns
Review the feedback without preconceptions. Surface recurring themes, pain points, and customer expectations. List 3–5 common themes.

### Phase 2: Extract Required Skills
For each theme, identify the specific support skills or behaviors needed. Format as a bullet list (e.g., "handling billing disputes," "managing delivery expectation mismatches").

### Phase 3: Synthesize Impact
Summarize why each issue matters to customers and business outcomes. Write 2–3 sentences per theme explaining the stakes.

### Phase 4: Define Ideal Responses
Describe what excellent support looks like for each skill. Write clear behavioral standards that reflect customer expectations (one paragraph per skill).

### Phase 5: Build Training Scenarios
Create 3–5 realistic role-play scenarios drawn directly from the feedback. Format each as a brief script (3–5 exchanges) suitable for coaching sessions.

### Phase 6: Prioritize by Impact
Rank the training points by urgency, weighing both frequency in feedback and severity of consequences. Deliver an ordered list of 5–8 priorities.

### Phase 7: Design Feedback Loops
Propose methods for ongoing evaluation: how will you track whether training addresses the issues, and how will new feedback refresh your approach?

### Phase 8: Plan Continuous Improvement
Outline a sustainable process for evolving training as customer needs and business context change.

## Output
Deliver your analysis in markdown with clear headings for each phase. Use bullet points for lists, short paragraphs for explanations, and script format for scenarios. Maintain a practical, coach-friendly tone throughout. Base every recommendation exclusively on the provided feedback—do not introduce external assumptions.
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-feedback}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Feedback to Support Training Prompt is a free AI prompt that transforms raw customer feedback int…
