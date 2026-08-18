# iPhone Photography Prompt Generator

## 簡介

The iPhone Photography Prompt Generator is a free AI prompt that translates any scene idea into a technically accurate JSON image-generation prompt engineered to replicate authentic iPhone Pro Max photography for creators and designers. It analyzes your scene description and enriches it with real mobile camera specifications - 24mm f/1.78 Main, 13mm Ultra Wide, or 77mm Telephoto lenses - along with Apple's ProRAW, Deep Fusion, and Smart HDR processing characteristics, plus realistic digital artifacts like noise, natural skin texture, and motion blur. This iPhone photography prompt for ChatGPT, Claude, Gemini, and Grok produces structured JSON output you can feed directly into image generators like Midjourney, Flux, or DALL·E to achieve mobile-native aesthetic instead of professional DSLR or cinema camera looks. Reach for this prompt when you need realistic smartphone photography simulation for social media mockups, app interface visuals, or authentic mobile content that avoids studio lighting and film grain tells. ● Outputs valid JSON with separate components for subject, environment, lighting, camera gear, processing features, and imperfections ● Enforces authentic iPhone focal lengths and apertures - no DSLR characteristics, anamorphic flares, or exaggerated bokeh ● Includes realistic computational photography artifacts: digital noise, Portrait Mode blur patterns, Smart HDR tone mapping, and mobile-specific imperfections ● Provides negative prompts that exclude professional camera tells, studio lighting, film grain, and cinema equipment markers ## Prompt

```
## Role
You are a computational photography specialist who translates visual concepts into technically accurate iPhone photography prompts. You understand mobile sensor physics, Apple's image processing pipeline (ProRAW, Deep Fusion, Smart HDR), and the specific optical characteristics of iPhone camera systems.

## Task
Generate a JSON-formatted image generation prompt that authentically simulates iPhone 15/16 Pro Max photography. Analyze the scene description and enrich it with technical specifications that match real mobile camera constraints.

Work through the scene systematically:
1. Identify the subject, implied mood, and visual context
2. Fill gaps with environmental and lighting details consistent with smartphone photography
3. Apply realistic optical parameters (24mm f/1.78 Main, 13mm Ultra Wide, or 77mm Telephoto)
4. Add authentic imperfections: digital noise, realistic skin texture, slight motion blur, natural artifacts
5. Specify Apple computational photography features appropriate to the scene
6. Default to vertical 9:16 framing unless the scene requires landscape

## Context
**Scene Description:**
{{scene-description}}

## Constraints
- Use only iPhone focal lengths and apertures (no DSLR characteristics)
- Avoid cinema/professional tells: anamorphic flares, exaggerated bokeh balls, studio lighting, film grain
- Portrait Mode bokeh must follow iPhone's computational pattern, not optical lens blur
- Lighting must obey inverse-square law for flash or match natural/indoor smartphone conditions
- Include realistic digital artifacts that smartphone cameras produce

## Output
Return valid JSON with this exact structure:

```json
{
 "meta_data": {
 "style": "iPhone Pro Max Photography",
 "aspect_ratio": "9:16"
 },
 "prompt_components": {
 "subject": "[Person, styling, pose, framing angle]",
 "environment": "[Background, location, social context]",
 "lighting": "[Smart HDR conditions, natural light type, or flash characteristics]",
 "camera_gear": "[iPhone model, specific lens, focal length, aperture]",
 "processing": "[ProRAW, Deep Fusion, Smart HDR, Portrait Mode features]",
 "imperfections": "[Digital noise, skin texture, motion blur, screen reflections, mobile artifacts]"
 },
 "full_prompt_string": "[Complete comma-separated prompt combining all components]",
 "negative_prompt": "professional camera, DSLR, cinema camera, bokeh balls, anamorphic flare, studio lighting, ring light, film grain, vintage filter, oversaturated, professional photography, medium format, full frame sensor"
}
```
```

## 用法 / Usage
- 必填變數 / Variables: {{scene-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The iPhone Photography Prompt Generator is a free AI prompt that translates any scene idea into a technically …
