# Satin Embroidery Patch Icon Generator

## 簡介

The Satin Embroidery Patch Icon Generator is a free AI prompt that retextures uploaded images into realistic satin embroidery patches with dense stitch detail and thread-accurate rendering. The prompt locks the shape and silhouette of your original image, then rebuilds every edge with satin stitch patterns, outline threadwork, and visible thread direction that follows object contours. This embroidery patch prompt for ChatGPT-assisted image models like Midjourney, Flux, and Nano Banana uses geometry-sensitive mapping to create relief depth from thread buildup, mild gloss along stitch direction, and bold stitched outlines in dark thread. Designers, sticker creators, and branding teams use it to turn logos, icons, and illustrations into photorealistic embroidered patches on matte black textile backgrounds. ● Applies high-gloss satin thread, dense embroidery floss, and tight needlepoint yarn with horizontal and curved thread flow. ● Renders vibrant cherry red, deep crimson, canary yellow, mustard gold, and tomato red with boosted saturation for maximum color pop. ● Produces flat studio lighting with mild thread glisten, tight inner shadows, and relief depth from stitch angles. ● Outputs stitch-only edges with bold dark outlines on solid matte black textile or seamless void backgrounds. ## Prompt

```
Retexture the image attached based on the JSON below
{
  "style_name": "High-Fidelity Satin Embroidery Patch",
  "retexture_mode": "shape_lock",
  "object_analysis": {
    "preserve_silhouette": true,
    "geometry_sensitive_mapping": true,
    "detail_retention": "rebuild object edges with dense satin stitch patterns and outline threadwork"
  },
  "material_properties": {
    "base_material": [
      "high-gloss satin thread",
      "dense embroidery floss",
      "tight needlepoint yarn"
    ],
    "surface_finish": "satin finish with visible thread direction and relief texture",
    "texture_behavior": "horizontal and curved thread flow that follows object contours with stitch segmentation",
    "branding_elements": "threaded logos and small fabric tags if applicable",
    "color_palette": {
      "primary": ["vibrant cherry red", "deep crimson", "canary yellow", "pure white", "charcoal black"],
      "accent": ["mustard gold", "tomato red", "cocoa brown", "lettuce green"],
      "background": ["solid matte black textile"]
    }
  },
  "lighting": {
    "type": "flat studio lighting",
    "angle": "frontal softbox mimic",
    "highlight_behavior": "mild thread glisten depending on stitch direction",
    "shadow": "tight, barely visible inner thread shadows"
  },
  "rendering": {
    "style_emphasis": "ultra-clean embroidery realism, cartoon proportions with uniform density",
    "border_treatment": "bold stitched outlines in dark thread, no drop shadow",
    "depth_emulation": "relief depth from thread buildup and stitch angles"
  },
  "post_processing": {
    "background_treatment": "pure black cloth-like texture or seamless void",
    "contrast_adjustment": "medium contrast to emphasize thread shading and texture",
    "saturation": "boosted for maximum thread color pop",
    "edge_cleanup": "stitch-only edges, no smooth graphic outlines"
  }
}
```

## 用法 / Usage
- 必填變數 / Variables: （無 / none） — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Satin Embroidery Patch Icon Generator is a free AI prompt that retextures uploaded images into realistic s…
