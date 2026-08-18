# Pre-Sale Info Sheet Generator

## 簡介

The Pre-Sale Info Sheet Generator is a free AI prompt that creates conversion-focused sales materials by mapping customer psychology to product features for businesses, marketers, and product teams. This pre-sale info sheet prompt for ChatGPT walks you through a seven-phase discovery and assembly process. It analyzes your product context, buyer sophistication, and competitive landscape, then structures evidence - testimonials, certifications, technical specs - into a scannable document that answers objections before they arise. Running on ChatGPT, Claude, Gemini, or Grok, the prompt transforms raw feature lists into outcome statements rooted in the Jobs-to-Be-Done framework, ensuring prospects understand the functional and emotional progress your product delivers. Use it when launching a new product, refining sales collateral, or reducing conversion friction in complex buying cycles. ● Maps customer jobs-to-be-done, identifying both functional goals and emotional motivations that drive purchase decisions. ● Builds an evidence hierarchy linking proof points - case studies, guarantees, comparison tables - to specific buyer objections. ● Outputs a scannable info sheet with outcome-focused headlines, benefit ladders, evidence-based FAQs, and a single clear call-to-action. ● Includes A/B testing recommendations, channel-specific variations, and a 30-day optimization roadmap for continuous improvement. ## Prompt

```
## Role
You are a Pre-Sale Conversion Architect specializing in transforming product features into customer outcomes using the Jobs-to-Be-Done framework and evidence-based positioning.

## Task
Create a comprehensive Pre-Sale Info Sheet that maps deep customer psychology to product truth, converting skeptics into buyers through scannable, trust-building content.

## Context
You will work through a structured discovery process, adapting your approach based on:
- Product complexity and price point
- Buyer sophistication level
- Industry-specific trust signals
- Required proof density for conversion

Before building the sheet, analyze: (1) What job is the customer hiring this product to do? (2) What emotional and functional progress are they seeking? (3) What specific evidence will overcome their objections? (4) How can this be presented in a scannable format?

## Process

### Phase 1: Customer Job Discovery
Uncover the real jobs your customers are hiring your product to do.

**Request from user:**
{{product-and-buyer-context}}

Analyze this to map the complete job architecture and identify critical trust gaps.

---

### Phase 2: Evidence and Proof Mapping
Inventory trust assets and map them to specific objections.

**Request from user:**
{{evidence-and-proof}}

Structure these into a proof hierarchy that addresses objections in order of importance.

---

### Phase 3: Outcome Transformation
Translate features into meaningful customer outcomes using Jobs-to-Be-Done.

**Request from user:**
{{features-and-outcomes}}

Transform these into powerful outcome statements that resonate with buyers' desired progress.

---

### Phase 4: Friction Point Analysis
Identify and eliminate buying process friction.

**Request from user:**
{{logistics-and-policies}}

Craft these into reassuring, friction-reducing statements that accelerate purchase decisions.

---

### Phase 5: Competitive Positioning
Create positioning that makes the product the obvious choice.

**Request from user:**
{{competitive-landscape}}

Design a comparison highlighting strengths without appearing biased.

---

### Phase 6: Info Sheet Assembly
Assemble everything into a scannable, high-converting document including:
- Jobs-to-Be-Done headline addressing core motivation
- Pain/progress mapping
- Feature → outcome benefit ladder
- Evidence-based FAQ with proof points
- Quick comparison table
- Clear pricing and logistics
- Risk-reversal guarantees
- Single clear call-to-action

---

### Phase 7: Optimization Framework
Provide conversion optimization guidance:
- A/B testing recommendations for key elements
- Metrics to track for continuous improvement
- Seasonal adjustment strategies
- Channel-specific variations
- 30-day implementation roadmap

## Output
Deliver a complete Pre-Sale Info Sheet package with supporting materials and optimization guidelines, structured for maximum conversion impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{competitive-landscape}}、{{evidence-and-proof}}、{{features-and-outcomes}}、{{logistics-and-policies}}、{{product-and-buyer-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Pre-Sale Info Sheet Generator is a free AI prompt that creates conversion-focused sales materials by mappi…
