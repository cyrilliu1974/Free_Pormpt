# QR Code Generator App Builder Prompt

## 簡介

The QR Code Generator App Builder Prompt is a free AI prompt that generates a complete, production-ready QR code creator as a single React component with TypeScript for developers and technical teams. This QR code generator prompt for ChatGPT, Claude, and Cursor produces a professional-grade application with a three-panel layout (input, preview, actions), real-time QR generation using the qrcode npm package, multiple error correction levels (L, M, Q, H), and export capabilities in PNG, SVG, and JPEG formats at high resolution suitable for print and scaling. It includes a camera-based scan testing feature, dark mode UI with lime accents, and full WCAG accessibility compliance. Marketing teams, event organizers, and businesses can use it to create pixel-perfect, scannable codes that rival commercial SaaS products without ads or functionality limits. Reach for this prompt when you need to build a complete QR code tool that goes beyond basic generators - offering advanced customization, offline capability, and professional output quality for print production and digital materials. ● Generates a single-file React component with TypeScript, real-time state management, and live QR preview updates. ● Supports multiple error correction levels and exports high-resolution codes in PNG, SVG, and JPEG formats. ● Includes camera-based scan testing to verify QR code reliability across devices before distribution. ● Delivers a responsive, accessible interface with professional animations, dark mode, and comprehensive error handling. ## Prompt

```
## Role

You are an expert full-stack developer specializing in React, TypeScript, and QR code technology.

## Task

Create a complete, production-ready QR Code Creator as a single React component with TypeScript. Build a professional-grade tool with advanced customization, premium UI/UX, and export capabilities that rival commercial SaaS products.

## Context

This application must surpass basic online QR generators that are cluttered with ads and limited in functionality. Target users—marketing teams, event organizers, and businesses—need pixel-perfect, scannable codes with meaningful customization for professional materials and print production.

{{requirements}}

## Output

Deliver a single React component artifact with TypeScript that includes:

### Architecture
- Three-panel layout: input / preview / actions
- Real-time state management for live updates
- Offline-capable (no external dependencies beyond npm packages)

### Core Functionality
- Real-time QR generation using the `qrcode` npm package
- Error correction levels: L, M, Q, H
- Multiple export formats: PNG, SVG, JPEG
- High-resolution output suitable for print and scaling
- Camera-based scan testing feature

### Design & UX
- Dark mode interface with lime-400 accents
- Professional animations and transitions
- Comprehensive error handling with clear user feedback
- Fully responsive across all device sizes
- WCAG accessibility compliance

### Implementation Phases

1. **Component Architecture** – Set up state management and component structure
2. **Input Panel** – Build the customization interface with advanced options
3. **Live Preview** – Implement real-time QR generation and display
4. **Export System** – Add multi-format download functionality
5. **Testing Feature** – Integrate camera-based scan verification
6. **Polish Layer** – Apply animations, error handling, and edge cases
7. **Responsive & A11y** – Ensure mobile compatibility and accessibility

The final application must produce production-quality QR codes that scan reliably across all devices and maintain quality when printed or scaled.
```

## 用法 / Usage
- 必填變數 / Variables: {{requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The QR Code Generator App Builder Prompt is a free AI prompt that generates a complete, production-ready QR co…
