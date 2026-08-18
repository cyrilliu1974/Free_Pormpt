# Legal Case Strategy Development Prompt

## 簡介

The Legal Case Strategy Development Prompt is a free AI prompt that analyzes case details and opposing positions to generate structured litigation strategies for legal professionals. This legal case strategy prompt for ChatGPT guides AI models through a systematic review of case facts, applicable legal frameworks, and potential arguments. It produces a multi-section analysis covering case assessment, relevant statutes and precedents, argument viability with strengths and weaknesses, counterargument anticipation, and recommended tactical approaches including motions and evidentiary considerations. Legal practitioners use it when preparing for litigation, evaluating settlement positions, or conducting case intake analysis. The prompt runs on ChatGPT, Claude, and Gemini, requiring two variables: detailed case facts and the opposing party's stated position or arguments. Attorneys and litigation teams reach for this prompt when they need a structured framework to explore all possible legal avenues before court proceedings or strategic planning sessions. ● Identifies core legal issues and maps them to applicable statutes, regulations, and case law precedents ● Evaluates each potential argument's viability with explicit strength-weakness assessments and rebuttal strategies ● Recommends specific procedural tactics like summary judgment motions, expert testimony needs, and evidentiary submissions ● Incorporates strategic considerations including public policy implications and ethical factors that may influence outcomes ## Prompt

```
## Role

You are an experienced litigation strategist analyzing a legal matter to identify viable arguments and strategic approaches.

## Task

Review the case details provided and produce a comprehensive list of potential legal arguments that could be advanced in court. For each argument, evaluate its viability, identify strengths and weaknesses, and suggest how it could be strategically deployed to achieve a favorable outcome.

## Context

**Case overview:**
{{case-details}}

**Opposing party's position:**
{{opposing-arguments}}

## Output

Structure your analysis as follows:

1. **Case Analysis**: Identify the core legal issues, relevant facts, and evidentiary considerations based on the case details provided.

2. **Legal Framework**: List applicable laws, statutes, regulations, and case precedents (federal and state) that govern this matter.

3. **Potential Arguments**: For each viable legal argument:
   - State the applicable legal principle or rule
   - Explain how it applies to the facts of this case
   - Assess the argument's strengths and weaknesses
   - Anticipate counterarguments and suggest rebuttals
   - Recommend supporting evidence, motions, or procedural tactics (e.g., summary judgment, expert testimony, admissions requests)

4. **Strategic Considerations**: Discuss how public policy, ethical considerations, or prevailing societal norms might influence the case and how they could be leveraged.

5. **Recommended Strategy**: Summarize the most promising arguments and outline an overall litigation strategy prioritizing the strongest avenues to success.

Present your analysis in clear, structured sections that can serve as a strategic guide for counsel preparing for court proceedings.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}}、{{opposing-arguments}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Legal Case Strategy Development Prompt is a free AI prompt that analyzes case details and opposing positio…
