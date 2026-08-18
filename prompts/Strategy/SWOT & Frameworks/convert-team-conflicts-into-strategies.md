# Team Conflict Resolution Strategy Prompt

## 簡介

The Team Conflict Resolution Strategy Prompt is a free AI prompt that reconciles clashing leadership viewpoints into a single higher-order strategy for decision-makers and facilitators. Instead of splitting the difference or choosing sides, it steelmans both positions, maps real versus surface conflicts, extracts non-negotiable insights, and builds a third option that preserves what matters from each side. This team conflict resolution prompt for ChatGPT works on Claude, Gemini, and Grok by guiding the model through a structured dialectical synthesis method that replaces either-or thinking with strategic reframing or phased sequencing. Use it when your team is stuck between two reasonable but incompatible proposals and a weak compromise will satisfy no one. ● Steelmans each position in 3-4 paragraphs, articulating supporting logic even the original proponent may not have stated. ● Builds a tension-mapping table distinguishing genuine contradictions from surface conflicts that can coexist if reframed or sequenced. ● Extracts one non-negotiable insight per side and designs a synthesis or phased approach that honors both. ● Pre-empts objections from each camp with direct, reasoned responses so the facilitator can defend the strategy. ## Prompt

```
## Role

You are a strategic facilitator specializing in resolving leadership conflicts through dialectical synthesis. Your method produces unified strategies that integrate competing viewpoints without compromise.

## Task

Reconcile two conflicting team positions into a higher-order strategic solution.

For each position:
- Restate it in its strongest possible form, adding supporting logic the original proponent may not have articulated
- Make each version compelling enough that a reasonable person would find it persuasive on its own

Then:
- Identify exactly where and why the positions conflict
- Distinguish genuine contradictions (adopting one eliminates the other) from surface contradictions (both could coexist if reframed or sequenced)
- Extract the one non-negotiable insight from each side that any strategy must preserve
- Build a third option that incorporates both non-negotiable insights while resolving genuine contradictions

This is not a compromise where both sides lose something, but a reframing that makes the original either/or unnecessary. If clean synthesis isn't possible, design a phased approach where both strategies deploy sequentially to reduce risk.

Finally, anticipate what proponents of each position will dislike about the synthesis and address each objection with reasoning.

## Context

**Position A:** {{position-a}}

**Position B:** {{position-b}}

**Strategic choice at stake:** {{strategic-choice}}

**Stakes and constraints:** {{stakes-and-context}}

## Output

Structure your response with these sections in order:

1. **Steelman of Position A** (3–4 paragraphs)
2. **Steelman of Position B** (3–4 paragraphs)
3. **Tension Mapping** (markdown table with columns: Point of Conflict | Genuine or Surface | Resolution Path)
4. **Non-Negotiable Insights** (one per side, clearly labeled)
5. **Synthesized Strategy** (detailed recommendation with implementation steps)
6. **Objection Pre-emptions** (two per side with direct responses)

**Requirements:**
- Do not produce a wishy-washy middle ground that satisfies nobody
- Do not dismiss either position as "wrong" without showing why
- The synthesis must be specific and actionable, not vague "let's do a bit of both"
- Avoid attributing unstated motivations or psychologizing the disagreement
- Stay focused on strategic logic
```

## 用法 / Usage
- 必填變數 / Variables: {{position-a}}、{{position-b}}、{{stakes-and-context}}、{{strategic-choice}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Team Conflict Resolution Strategy Prompt is a free AI prompt that reconciles clashing leadership viewpoint…
