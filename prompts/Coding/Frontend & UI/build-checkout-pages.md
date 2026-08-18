# Build Checkout Pages with React and Stripe

## 簡介

The Build Checkout Pages with React and Stripe prompt is a free AI prompt that generates a complete, production-ready checkout system for developers and product teams building e-commerce flows. It produces a multi-file React project with TypeScript, Tailwind CSS, and Stripe Elements integration, structured around a three-step flow (Info → Payment → Confirm) that balances speed, trust, and conversion psychology. This checkout pages prompt for ChatGPT runs on ChatGPT, Claude, and Cursor, and it outputs organized component architecture, hooks, utilities, Stripe PaymentIntent API logic, real-time form validation, and accessibility-compliant UI. Reach for this prompt when you need a mobile-first checkout experience with sub-300ms input response, express payment methods like Apple Pay and Google Pay, guest checkout, progress indicators, trust badges, and transparent pricing calculations that reduce cart abandonment. ● Outputs a complete multi-file React + TypeScript + Tailwind CSS codebase with Stripe Elements integration, organized into components/, hooks/, and utils/ directories. ● Includes real-time form validation, comprehensive error handling, optimistic UI patterns, automatic progress saving, and WCAG AA accessibility compliance. ● Provides express checkout options (Apple Pay, Google Pay), guest checkout, live order summary, trust signals, and security badges to minimize friction and maximize completion rates. ● Ships with setup documentation covering installation, environment variables, configuration, and deployment instructions, plus inline comments explaining conversion optimization decisions. ## Prompt

```
## Role

You are a full-stack developer specializing in high-conversion checkout systems. You understand the technical and psychological factors that drive purchase completion—trust signals, input responsiveness, error recovery, and friction elimination.

## Task

Build a complete, production-ready checkout system using React, TypeScript, Tailwind CSS, and Stripe Elements. The system should follow a three-step flow (Info → Payment → Confirm) with:

- Mobile-first responsive design with sub-300ms input response
- Real-time form validation and comprehensive error handling
- Multiple payment methods including express options (Apple Pay, Google Pay)
- Progress indicators, trust badges, and security signals
- Automatic progress saving and optimistic UI patterns
- Live order summary with transparent pricing calculations
- Guest checkout option to minimize friction
- WCAG AA accessibility and cross-browser compatibility
- Proper TypeScript types and organized component architecture (components/, hooks/, utils/)

## Context

{{checkout-requirements}}

Describe your use case: industry/product type, required payment methods and integrations, necessary form fields (shipping vs. digital delivery), compliance needs (tax calculation, regional pricing, regulatory requirements), and trust elements (security badges, guarantees, refund policies).

## Output

Provide a complete multi-file React project structured as:

**Requirements Analysis**  
Breakdown of checkout flow architecture and payment processing strategy

**Component Structure**  
Complete file structure with TypeScript type definitions

**UI Implementation**  
React components for checkout steps, order summary, payment forms, and success screens

**Stripe Integration**  
PaymentIntent API implementation with error handling and security measures

**Conversion Optimization**  
Trust signals, progress indicators, express checkout options, and friction reducers

**Responsive Design**  
Mobile-first implementation with smooth transitions and accessibility features

**Setup Documentation**  
README with installation, configuration, environment variables, and deployment instructions

Include detailed code comments explaining conversion optimization decisions.
```

## 用法 / Usage
- 必填變數 / Variables: {{checkout-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Build Checkout Pages with React and Stripe prompt is a free AI prompt that generates a complete, productio…
