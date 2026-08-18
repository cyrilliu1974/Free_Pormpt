# Customer Feedback Loop Implementation Prompt

## 簡介

The Customer Feedback Loop Implementation Prompt is a free AI prompt that designs actionable feedback collection systems for sales teams and customer success professionals. This customer feedback prompt for ChatGPT produces a prioritized table of at least five feedback mechanisms spanning the entire customer journey - from initial contact through post-purchase follow-up. It blends digital and traditional approaches, quantitative and qualitative methods, then scores each mechanism by priority and implementation effort. Sales leaders use it to identify which feedback loops will deliver the fastest ROI, while customer experience managers deploy it to map touchpoints they're currently missing. The prompt runs on ChatGPT, Claude, Gemini, and Grok, accepting your business context and any existing feedback systems as inputs. Reach for this prompt when you need to move beyond ad-hoc surveys and build a repeatable system that turns customer insights into pipeline improvements and retention wins. ● Covers multiple customer journey stages - awareness, consideration, purchase, and post-sale - so no touchpoint is left unmonitored. ● Scores every feedback mechanism by both business priority and implementation effort, making resource allocation straightforward. ● Balances real-time methods like live chat sentiment analysis with asynchronous tools like NPS surveys and social listening. ● Outputs a clean, sortable table format that product, sales, and CX teams can immediately plug into roadmaps and sprint planning. ## Prompt

```
## Role
You are an expert in designing and implementing customer feedback collection mechanisms to strengthen customer engagement in sales processes.

## Task
Design and implement effective customer feedback loops to improve sales performance and customer satisfaction for the user's business. Provide a minimum of 5 different feedback mechanisms that cover various touchpoints across the customer journey, from initial contact to post-purchase follow-up. Consider both digital and traditional approaches, and include both quantitative and qualitative methods.

## Context
- Target audience and sales process: {{business-context}}
- Existing feedback mechanisms: {{current-feedback-loops}}

## Guidelines
- Prioritize feedback mechanisms that yield actionable insights and drive meaningful improvements in sales processes and customer engagement
- Avoid methods that are overly intrusive, time-consuming, or may negatively impact the customer experience
- Focus on mechanisms that cover different stages of the customer journey

## Output
Return a structured table with the following columns:

| Feedback Loop Type | Implementation Method | Expected Outcome | Priority Score (1-5) | Effort Score (1-5) |
|-------------------|----------------------|------------------|----------------------|-------------------|

**Column definitions:**
- **Feedback Loop Type**: Categorize the feedback mechanism (e.g., real-time feedback, post-purchase surveys, social media monitoring)
- **Implementation Method**: Describe how each feedback mechanism will be implemented and carried out
- **Expected Outcome**: Outline the desired results and benefits of each mechanism
- **Priority Score**: Rate importance and urgency (1-5, where 5 is highest priority)
- **Effort Score**: Rate ease of implementation (1-5, where 5 is least effort required)

Provide only the table without additional explanations.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{current-feedback-loops}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Customer Feedback Loop Implementation Prompt is a free AI prompt that designs actionable feedback collecti…
