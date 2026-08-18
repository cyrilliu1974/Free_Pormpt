# Product Documentation Layout Generator

## 簡介

The Product Documentation Layout Generator is a free AI prompt that transforms a single uploaded product photo into a professional technical documentation layout complete with multi-view columns, hero render, and precise visual annotations. This product documentation prompt for Midjourney, Flux, and Nano Banana creates a four-view auxiliary column on the left - front, side, alternate angle, and detail - paired with a large photorealistic hero render on the right, all annotated with hairline vector callout lines that terminate at actual visible components. Each annotation label describes only what can be seen: materials identifiable by finish, structures visible in the geometry, and functions structurally implied by the design. The prompt enforces visual truth by forbidding category assumptions or hallucinated features, making it ideal for product designers, technical illustrators, e-commerce teams, and hardware startups preparing spec sheets, pitch decks, or portfolio presentations. Reach for this layout when you need studio-quality documentation that respects the actual product rather than filling space with marketing fluff. ● Configurable background surface, annotation line color, and design aesthetic (minimal, technical, editorial) ● Four auxiliary views automatically arranged with even spacing and alignment ● Hairline callout system that connects labels only to components actually visible in the upload ● Photorealistic hero render with soft studio lighting and exact material matching ## Prompt

```
Create a high-end industrial design product documentation layout for the uploaded product image.

**Composition**

Top left: Brand name in modern sans-serif typography, subtle and elegant.

Left column: Four auxiliary product views arranged vertically with even spacing—primary front view, secondary side view, alternate angle or rear view, and detail or top view. All views aligned and clearly visible.

Right section: Large hero product render, photorealistic with soft studio lighting. Materials and geometry must exactly match the uploaded product.

Background: {{background-surface}}

**Technical Annotations**

First, visually analyze the product to identify distinct physical components—materials, surfaces, interfaces, and structures that are actually visible. Ignore assumed internals or hidden features.

Then add hairline-thin vector annotation lines in {{line-color}}, each terminating at exact contact with one visible component. Every line connects to a label placed outside the product silhouette with consistent spacing and no overlaps.

Each label must describe exactly what that component is and does, based only on visual evidence. Use neutral, descriptive nouns. Mention material only if visually identifiable, function only if structurally implied. Avoid category-specific terminology unless the feature is clearly visible. One line = one component = one explanation.

Label typography: minimal technical sans-serif, factual and precise tone.

**Visual Style**

{{design-aesthetic}} aesthetic with calm, precise, professional mood. Neutral and restrained color palette. Ultra-high resolution rendering with soft, realistic shadows and exact proportions.

**Binding Rules**

- Do not assume the product category in advance
- Do not hallucinate features or use generic marketing language
- Every annotation must point to something actually visible
- No label may rely on category assumptions for meaning
- Maintain visual truth and semantic correctness throughout
```

## 用法 / Usage
- 必填變數 / Variables: {{background-surface}}、{{design-aesthetic}}、{{line-color}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Scientific_Figure_Design_Decision_Framework
- 適用 / Use when: The Product Documentation Layout Generator is a free AI prompt that transforms a single uploaded product photo…
