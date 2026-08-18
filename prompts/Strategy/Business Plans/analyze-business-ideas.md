# Business Idea Feasibility Analysis Prompt

## 簡介

The Business Idea Feasibility Analysis Prompt is a free AI prompt that evaluates business concepts for real-world viability through structured market analysis and multi-perspective validation. This business idea analysis prompt for ChatGPT walks you through a six-part framework: core concept summary, target market identification, validation from three distinct customer personas (each with age, occupation, pain points, and honest adoption likelihood), comprehensive risk assessment (competition, timing, regulatory, execution, and demand), alternative business model suggestions, and a direct go/no-go/iterate verdict with actionable next steps. It runs on ChatGPT, Claude, and Gemini, producing a structured report that balances genuine merits against potential pitfalls without entrepreneurial cheerleading. Entrepreneurs use it to stress-test early-stage ideas, product managers apply it to feature concepts, and consultants deploy it for client validation work. ● Creates three distinct customer personas with specific pain points and candid adoption opinions ● Identifies 2-4 viable target markets and assesses five categories of market risk with severity ratings ● Suggests 2-3 alternative business models or pivots to improve the idea's commercial viability ● Delivers a clear go/no-go/iterate recommendation with concrete next steps, not vague encouragement ## Prompt

```
## Role
Pragmatic business strategist specializing in real-world feasibility assessment of business concepts.

## Task
Analyze {{business-idea}} objectively, weighing genuine merits against potential pitfalls. Deliver blunt, balanced validation through multi-persona feedback and strategic alternatives.

## Analysis Framework
1. **Business Idea Overview**: Summarize the core concept, value proposition, and intended market position.

2. **Potential Markets**: Identify 2-4 viable target segments with specific characteristics.

3. **Persona Validation**: Create three distinct theoretical personas, each including:
   - Age and occupation
   - Specific pain points relevant to the idea
   - Validation statement covering: the problem they face, how well this solution addresses it, and their honest opinion on adoption likelihood

4. **Market Risks**: Assess competition, timing, regulatory, execution, and demand risks without sugarcoating.

5. **Alternative Business Models**: Suggest 2-3 pivots or variations that might improve viability.

6. **Final Validation & Recommendation**: Provide a direct go/no-go/iterate verdict with specific next steps.

## Output Format
```
business_idea_overview: [2-3 sentence summary]

potential_markets: [bulleted list]

persona1:
age: [age]
occupation: [occupation]
pain_points: [specific pain points]
validation: "[problem statement]. [solution fit assessment]. [adoption opinion]"

persona2:
age: [age]
occupation: [occupation]
pain_points: [specific pain points]
validation: "[problem statement]. [solution fit assessment]. [adoption opinion]"

persona3:
age: [age]
occupation: [occupation]
pain_points: [specific pain points]
validation: "[problem statement]. [solution fit assessment]. [adoption opinion]"

market_risks: [3-5 concrete risks with severity assessment]

alternative_business_models: [2-3 specific alternatives with rationale]

final_validation_and_recommendation: [honest verdict with conditions or next actions]
```
```

## 用法 / Usage
- 必填變數 / Variables: {{business-idea}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Business Idea Feasibility Analysis Prompt is a free AI prompt that evaluates business concepts for real-wo…
