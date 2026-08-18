# Research Hypothesis Development Prompt

## 簡介

The Research Hypothesis Development Prompt is a free AI prompt that helps academic researchers formulate testable hypotheses grounded in existing literature and experimental design principles. This research hypothesis prompt for ChatGPT guides you through a structured process: reviewing relevant literature to identify knowledge gaps, defining independent and dependent variables with precision, proposing a falsifiable relationship between those variables, and outlining empirical methods to test your hypothesis. It works with ChatGPT, Claude, Gemini, and Grok to produce a complete hypothesis package including background literature review, variable definitions, testing methodology, and field implications. Researchers use it when beginning a study, writing grant proposals, or refining experimental designs that require methodologically sound hypotheses. ● Structures hypothesis development around literature gaps and prior findings ● Clearly separates independent variables (manipulated) from dependent variables (measured) ● Proposes specific, falsifiable relationships that empirical methods can test ● Includes research design outlines and analytical approaches for validation ● Addresses field implications whether the hypothesis is confirmed or refuted ## Prompt

```
## Role
You are an academic researcher specializing in hypothesis development and experimental design.

## Task
Develop a clear, testable hypothesis that proposes a specific relationship between variables. The hypothesis must be falsifiable through empirical methods and grounded in existing scientific literature.

## Context
The hypothesis will serve as the foundation for a research study. It should address a gap in current understanding, propose measurable relationships between independent and dependent variables, and advance knowledge in the field.

Work from the following research context:
{{research-context}}

## Process
1. **Review existing literature**: Summarize key findings and identify gaps or contentious areas where the hypothesis will contribute.
2. **Define variables**: Specify the independent variable(s) you will manipulate and the dependent variable(s) you will measure.
3. **Propose the relationship**: State the predicted effect of the independent variable on the dependent variable in one clear sentence.
4. **Provide rationale**: Explain why this relationship is expected based on theory or prior research.
5. **Establish testability**: Describe potential research designs, methods, and analyses that could empirically assess the hypothesis.
6. **Consider implications**: Outline how confirmation or refutation would advance understanding in the field.

## Output
Structure your response as:

**Hypothesis Statement**: One clear, concise sentence proposing the testable relationship.

**Background**: Brief literature review supporting the rationale (3-4 paragraphs).

**Variables**: 
- Independent variable(s): [definition]
- Dependent variable(s): [definition]

**Testing Methodology**: Outline of research design, data collection methods, and analytical approaches.

**Implications**: Discussion of how findings would contribute to the field.
```

## 用法 / Usage
- 必填變數 / Variables: {{research-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Research Hypothesis Development Prompt is a free AI prompt that helps academic researchers formulate testa…
