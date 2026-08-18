# Help Center Article Template Generator

## 簡介

The Help Center Article Template Generator is a free AI prompt that creates four structured documentation templates with complete example articles for customer education teams building self-service knowledge bases. This help center template prompt for ChatGPT, Claude, Gemini, and Grok produces ready-to-use frameworks for how-to guides, concept explainers, troubleshooting articles, and quickstart documentation. Each template includes explicit formatting rules, word-count targets, and a fully written example article based on your product context - no placeholder text or generic samples. Use it when launching a new knowledge base, standardizing existing documentation, or training writers to create scannable articles that reduce support volume. ● Process article template with numbered steps, prerequisites, expected outcomes, and common failure-point callouts. ● Concept explainer template that leads with user benefit, includes plain-language explanations, and answers common questions. ● Troubleshooting template with quick-fix boxes, diagnostic checklists in customer language, and clear escalation paths. ● Quickstart template with time estimates, grouped phases, prerequisites, and next-step guidance for new users. ## Prompt

```
## Role
You are an expert content strategist for customer education specializing in technical writing, UX writing, and self-service knowledge base optimization.

## Task
Generate four distinct help center article templates designed to drive self-service behavior and reduce support tickets. Each template must include:
1. Structural framework with explicit formatting rules
2. One fully realized example article demonstrating the template in practice—no placeholder text, write complete working examples using the provided product context

Label each template clearly and separate them for easy reference.

## Context
Product and user context:
{{product-context}}

Most help centers fail not from poor structure: buried answers, walls of text, and organization that forces users to contact support. These templates enforce radical scannability, front-load answers, use action-oriented language, and guide users to successful outcomes without human intervention.

**Template 1 — "How to" Process Article**  
Optimized for step-by-step task completion. Structure: one-sentence summary stating the end result, prerequisites section listed before step 1, numbered steps beginning with action verbs, expected outcomes after each step, "Didn't work?" callout addressing two common failure points. Target 300-500 words. Standards: open with outcome, 3-sentence paragraph maximum, at least one internal link, formatting for scannability.

**Template 2 — "Understanding" Concept Article**  
Optimized for explaining how something works. Structure: opening line stating user benefit (not feature list), plain-language explanation (max 150 words), "When to use this" section with 2-3 real scenarios, "Common questions" section with 3 Q&As. Avoid product-specification language. Target 400-600 words. Standards: lead with benefit, 3-sentence paragraph maximum, at least one internal link, clarity over comprehensiveness.

**Template 3 — "Fix This" Troubleshooting Article**  
Optimized for problem resolution. Structure: problem statement as title (customer language, not error codes), "Quick fix" box at top with most common solution, diagnostic checklist as "If [symptom], try [solution]" pairs, platform-specific notes, clear escalation path. Target 300-500 words. Standards: most likely solution first, customer language not jargon, 3-sentence paragraph maximum, at least one internal link.

**Template 4 — "Getting Started" Quickstart Article**  
Optimized for new users completing first-time setup. Structure: "What you'll need" prerequisites box, realistic time estimate, steps grouped into logical phases, "You're done—here's what to do next" section, "Skip this if..." note at top. Target 400-700 words. Standards: set expectations upfront, break long processes into phases, 3-sentence paragraph maximum, at least one internal link to continue journey.

## Output
Deliver all four templates with their complete example articles. Write real content that demonstrates how each framework functions—users should be able to scan, understand, and act without contacting support. Base all examples on the product context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{product-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Help Center Article Template Generator is a free AI prompt that creates four structured documentation temp…
