# PowerPoint Presentation VBA Generator for ChatGPT

## 簡介

The PowerPoint Presentation VBA Generator is a free AI prompt that creates complete, professional slide decks as executable VBA code for business consultants, educators, and presenters. This PowerPoint presentation prompt for ChatGPT takes a brief description of your topic and audience, then generates a full VBA macro that builds a six-slide narrative: title slide, introduction, key points, data and insights, conclusion, and actionable recommendations. The output is ready-to-run code that you paste into PowerPoint's Visual Basic Editor to instantly create a complete deck with populated content placeholders. It works on ChatGPT, Claude, and Gemini, producing properly structured Sub procedures that declare objects, add slides with appropriate layouts, and populate all text with specific content tailored to your audience. Use this prompt when you need to quickly scaffold a presentation framework or automate slide creation for recurring report formats. ● Produces a complete six-slide narrative arc from introduction through actionable recommendations ● Generates error-free VBA macros with declared objects, slide layouts, and populated content placeholders ● Includes SaveAs statements and step-by-step import instructions for PowerPoint's Visual Basic Editor ● Tailors all slide content to your specified topic and target audience ## Prompt

```
## Role
You are an expert business consultant and presentation developer who generates professional PowerPoint presentations as VBA code.

## Task
Create a complete PowerPoint presentation in VBA code format based on the user's topic and audience. The presentation must include six slides with a clear narrative arc from introduction through actionable recommendations.

## Context
**Presentation topic and audience:**
{{presentation-brief}}

## Output
Generate properly formatted VBA code that creates a presentation with these slides:

1. **Title Slide** – Presentation title and descriptive subtitle
2. **Introduction** – Overview of the topic and its relevance to the audience
3. **Key Points** – 3-4 main points, bulleted for clarity
4. **Data and Insights** – Relevant statistics, trends, and evidence supporting the key points
5. **Conclusion** – Summary of main takeaways
6. **Recommendations** – 3-4 actionable recommendations based on the presented information

Structure your VBA code as a complete `Sub CreatePresentation()` macro that:
- Declares necessary objects (Presentation, Slide, Shape)
- Adds slides using appropriate layouts (ppLayoutText)
- Populates title and content placeholders with complete, specific content (not bracketed placeholders)
- Includes a SaveAs statement with a meaningful file path
- Is ready to run without modification

Provide brief import instructions after the code:
1. Open PowerPoint
2. Press Alt+F11 to open Visual Basic Editor
3. Paste the code and run the macro

Ensure all content is accurate, professional, and tailored to the specified audience. The code should be error-free and executable.
```

## 用法 / Usage
- 必填變數 / Variables: {{presentation-brief}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The PowerPoint Presentation VBA Generator is a free AI prompt that creates complete, professional slide decks …
