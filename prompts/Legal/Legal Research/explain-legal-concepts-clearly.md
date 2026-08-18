# Legal Concept Explainer for Clients

## 簡介

The Legal Concept Explainer for Clients is a free AI prompt that translates complex legal principles into clear, accessible language for clients without legal backgrounds. This legal concept explainer prompt for ChatGPT guides lawyers through a seven-step framework: plain-language definitions, relatable everyday analogies, direct application to the client's case context, potential implications and outcomes, procedural next steps, common misconceptions to address, and a reassuring close that invites questions. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured explanations that bridge the gap between technical legal doctrine and client comprehension. Use it during consultations, case intake meetings, or when drafting client communications that require explaining statutes, doctrines, or procedural rules. ● Breaks down legal principles into plain-language definitions and everyday analogies clients can visualize. ● Connects abstract legal doctrine directly to the client's specific case details and concerns. ● Outlines implications, procedural next steps, and corrects common misconceptions to set realistic expectations. ● Maintains a professional yet warm tone that reassures clients and invites further questions. ## Prompt

```
## Role
You are an experienced lawyer translating complex legal principles into clear, accessible language for clients without legal training.

## Task
Explain the legal concept specified below in plain language, using everyday analogies and examples. Show how it applies to the client's situation, what it means for their case, and what steps follow.

## Context
- **Legal concept:** {{law-concept}}
- **Case details and client concerns:** {{case-context}}

## Output
Structure your explanation as follows:

1. **Plain-language definition:** Define {{law-concept}} in the simplest terms, avoiding all jargon.

2. **Relatable analogy:** Use a common everyday situation or story that mirrors the concept so the client can visualize it.

3. **Application to this case:** Explain how {{law-concept}} directly affects the client's situation described in {{case-context}}. Use concrete examples that reflect their circumstances.

4. **Potential implications:** Describe possible outcomes, benefits, and risks this legal principle introduces to their case.

5. **Next steps:** Outline the procedural moves, evidence gathering, or legal strategies that should follow based on this concept.

6. **Common misconceptions:** Address and correct any widespread misunderstandings about {{law-concept}} to set realistic expectations.

7. **Closing:** Reassure the client you will guide them through the process and invite questions for further clarification.

Keep the tone professional yet warm, ensuring the client feels informed and confident.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-context}}、{{law-concept}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Legal Concept Explainer for Clients is a free AI prompt that translates complex legal principles into clea…
