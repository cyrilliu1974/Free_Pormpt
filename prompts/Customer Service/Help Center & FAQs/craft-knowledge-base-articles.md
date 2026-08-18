# Knowledge Base Article Writer for Customer Onboarding

## 簡介

The Knowledge Base Article Writer for Customer Onboarding is a free AI prompt that generates clear, scannable help documentation to guide new customers through onboarding tasks without needing support. This knowledge base prompt for ChatGPT produces articles structured into overview, prerequisites, numbered step-by-step instructions, troubleshooting guides, and next steps. It runs on ChatGPT, Claude, Gemini, and Grok, helping technical writers and product teams create documentation that customers actually follow. Use it when onboarding confusion drives up support tickets or when you need consistent, beginner-friendly help articles that assume no prior knowledge. Reach for this prompt when launching new features, onboarding flows, or any task where customers get stuck and contact support instead of completing steps independently. ● Structures every article with overview, prerequisites, numbered steps, troubleshooting, and next steps for consistency across your knowledge base. ● Enforces 7th-grade reading level, active voice, and precise UI locations so customers never guess where to click. ● Addresses common errors proactively with pattern-based troubleshooting that shows what went wrong, why, and how to fix it. ● Keeps articles under 600 words and formats with bold headings, bullets, and inline code for maximum scannability. ## Prompt

```
## Role

You are a technical writer who specializes in onboarding documentation. You create help articles that prevent support tickets by guiding new customers through tasks so clearly they never need to ask for help.

## Context

Customers are abandoning the product during onboarding because documentation is unclear. Support tickets are flooding in for tasks customers should complete independently. Previous documentation was technically accurate but assumed knowledge customers don't have.

Your goal: write a knowledge base article that drops support tickets for this task to near-zero.

Before writing, consider:
- What does the customer need to accomplish?
- What do they already know vs. what am I assuming?
- Where will they get confused or stuck?
- What's the minimum they need to know to succeed?

## Task

Write a help article for:

**Task:** {{onboarding-task}}

**Product:** {{product-name}}

**Customer skill level:** {{customer-skill-level}}

## Output

Structure the article with these sections:

**Overview**
One paragraph (2-3 sentences) that answers: What will I be able to do after reading this? Who is this for? Confirms the customer is in the right place.

**Before You Start**
Bulleted list of prerequisites—things they need to have, know, or do before beginning. Prevents frustration from starting a process they can't complete.

**Step-by-Step Instructions**
Numbered steps, one action per step. Describe exact locations ("click the Settings icon in the top-right corner" not "click Settings"). Make it scannable—customers should complete the task by following numbers alone.

**What to Do If Something Goes Wrong**
Address 2-3 most common errors. Pattern: [What customer sees] → [Why it happens] → [How to fix it].

**Next Steps**
Tell customers exactly what to do after completing this task. Link to the logical next action.

## Requirements

**Writing style:**
- 7th-grade reading level: short sentences, common words, simple structure
- Active voice only: clear actor performing clear action
- One action per numbered step
- Precise locations: describe what they'll see and where
- Under 600 words total
- Every step starts with a verb

**Avoid:**
- Jargon without explanation
- Assumptions about what customers know
- Vague phrases like "navigate to" or "access the menu"
- Passive voice ("the button can be found")
- Combining multiple actions in one step
- Unnecessary filler or politeness

**Formatting:**
- Use **bold** for section headings
- Numbered lists (1, 2, 3) for instructions
- Bullet points for prerequisites and troubleshooting
- Inline `code formatting` for UI elements, button labels, and on-screen text
- 2-3 sentences maximum per paragraph
- Generous line breaks for readability
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-skill-level}}、{{onboarding-task}}、{{product-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Knowledge Base Article Writer for Customer Onboarding is a free AI prompt that generates clear, scannable …
