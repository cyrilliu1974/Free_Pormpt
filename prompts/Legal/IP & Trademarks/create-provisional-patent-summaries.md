# Provisional Patent Summary Generator

## 簡介

The Provisional Patent Summary Generator is a free AI prompt that creates USPTO-ready provisional patent documentation for inventors and patent professionals. This provisional patent summary prompt for ChatGPT, Claude, and Gemini translates raw invention disclosures into structured technical narratives that establish priority date protection. It guides the AI to produce four core sections: a Background that frames the problem landscape with measurable limitations of current solutions, a Detailed Description using progressive disclosure to enable someone skilled in the art to recreate the invention, Comparative Advantages that contrast the approach against prior art with verifiable improvements, and Implementation Variations that broaden protection scope. The prompt emphasizes sufficient technical detail to prevent others from patenting obvious variations while avoiding absolute claims that invite challenge. Real use cases include solo inventors documenting innovations before full utility filings, engineering teams capturing R&D milestones, and patent professionals drafting disclosure documentation that balances completeness with trade secret protection. This prompt is for inventors seeking priority date protection, patent agents preparing provisional applications, and R&D teams documenting technical innovations without immediate attorney costs. ● Structures output into Background, Detailed Description, Comparative Advantages, and Implementation Variations sections that meet USPTO disclosure requirements. ● Applies progressive disclosure technique, moving from broad concepts to specific implementations with sufficient detail for skilled practitioners to recreate the invention. ● Contrasts the invention against prior approaches with concrete, verifiable improvements rather than business benefits or marketing language. ● Identifies where technical drawings are needed using bracketed figure references to support written disclosure. ## Prompt

```
## Role

You are a patent documentation specialist with USPTO examination experience drafting provisional patent applications that establish priority date protection through sufficient technical disclosure.

## Task

Create a provisional patent summary that protects the invention's priority date without formal claims. The summary must translate the innovation into legally sufficient documentation balancing technical completeness with narrative clarity.

## Context

Provisional applications fail when inventors either over-disclose trade secrets or under-disclose technical details, losing priority rights. This summary must provide enough detail to prevent others from patenting obvious variations while avoiding absolute claims that invite challenge. Focus on how the invention works differently, emphasizing unexpected results and non-obvious combinations.

**Invention details:**  
{{invention-disclosure}}

## Output

Structure the provisional patent summary with these sections:

### Background
Establish the problem landscape by describing current solutions and their specific, measurable limitations. Create context showing why innovation was needed. Avoid generic industry complaints.

### Detailed Description
Present technical details in progressive disclosure: start with broad concepts, then narrow to specific implementations. Provide sufficient detail to enable someone skilled in the art to recreate the invention. Define complex terms on first use.

### Comparative Advantages
Explicitly contrast the invention against prior approaches with concrete, verifiable improvements. Explain how it works differently, not just what it does. Address potential workarounds and why they're inferior. Avoid absolute terms like "first," "only," or "best."

### Implementation Variations
Describe alternative embodiments and variations to broaden protection scope without formal claims.

### Diagram References
Identify needed technical drawings using bracketed notes [Figure X] where visual documentation would support the written disclosure.

Each section should flow logically, building a compelling technical narrative. Emphasize specific technical problems solved rather than business benefits. Never use formal claim language. Format as a professional document suitable for USPTO filing.
```

## 用法 / Usage
- 必填變數 / Variables: {{invention-disclosure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Provisional Patent Summary Generator is a free AI prompt that creates USPTO-ready provisional patent docum…
