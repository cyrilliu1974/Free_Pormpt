# Virtual Office Platform Development Prompt

## 簡介

The Virtual Office Platform Development Prompt is a free AI prompt that produces a structured technical implementation guide for building spatial computing-based virtual office platforms for full-stack developers and 3D web architects. This virtual office platform development prompt for ChatGPT walks you through the complete technical stack required to build a production-ready remote collaboration environment that goes beyond standard video conferencing. It covers 3D scene rendering with WebGL and Three.js, real-time multiplayer infrastructure using WebRTC and WebSockets, avatar systems with character controllers and collision detection, spatial audio and video integration, builder interfaces, and performance optimization strategies. The output includes production-ready code examples, specific technical configurations, and actionable implementation steps tailored to your project context. You can run it on ChatGPT, Claude, Gemini, or Grok by providing your project requirements in the project-context variable. Reach for this prompt when you need a complete architectural blueprint for building a 3D virtual office platform that rivals native application performance across browsers and devices. ● Delivers technical architecture decisions covering framework selection, data layers, and infrastructure choices for spatial computing platforms. ● Provides complete code examples for Three.js scene setup, real-time state synchronization, avatar movement systems, and spatial audio integration. ● Includes performance optimization strategies like LOD implementation, instancing techniques, network optimization, and bundle size reduction. ● Covers production deployment with CI/CD pipelines, monitoring setup, and cross-browser testing strategies for varied device capabilities. ## Prompt

```
## Role

You are an expert full-stack architect and 3D web development specialist.

## Task

Create a comprehensive technical implementation guide for building a production-ready virtual office platform using spatial computing for remote collaboration. Transform spatial computing concepts into working code that rivals native application performance.

## Context

{{project-context}}

The platform must transcend typical video conferencing through spatial computing. Cover the full technical stack: 3D scene rendering (WebGL, Three.js), real-time multiplayer infrastructure, avatar systems, spatial audio/video, and intuitive builder interfaces while maintaining exceptional performance across target devices.

## Output

Provide a structured implementation guide organized into these sections:

● **Technical Architecture and Stack Decisions** – framework selection, data layer, infrastructure choices
● **3D Scene Foundation and Camera Systems** – Three.js/WebGL setup, scene graph, camera controls
● **Real-Time Collaboration Infrastructure** – WebRTC, WebSocket architecture, state synchronization
● **Avatar and Movement Systems** – character controllers, collision detection, navigation
● **Spatial Audio and Video Integration** – positional audio, video textures, quality adaptation
● **Builder Interface and User Experience** – editing tools, spatial UI patterns, onboarding
● **Performance Optimization and Scaling** – LOD strategies, instancing, network optimization, bundle size
● **Production Deployment and Testing Strategy** – CI/CD, monitoring, cross-browser/device testing

For each section, include:
- Complete code examples with specific technical configurations
- Actionable implementation steps tailored to the project context
- Performance considerations and common pitfalls
- Progressive enhancement strategies for varied device capabilities

Present all guidance in clear bullet points using ● markers, with production-ready code snippets and concrete technical recommendations.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Virtual Office Platform Development Prompt is a free AI prompt that produces a structured technical implem…
