# Technical Specification Document Generator

## 簡介

The Technical Specification Document Generator is a free AI prompt that creates comprehensive technical specification documents for engineers, product teams, and technical writers. This technical specification prompt for ChatGPT walks through every critical section of a formal spec document: introduction and scope, functional requirements, performance metrics, interface definitions, reliability standards, maintainability criteria, environmental factors, compliance measures, and a glossary with references. It runs on ChatGPT, Claude, and Gemini, accepting a single product-component variable and outputting a multi-section document that identifies where technical diagrams, flowcharts, and illustrations should be placed to enhance clarity. Use it when documenting hardware modules, software APIs, system integrations, or any engineered component that requires formal specification before development or procurement. ● Covers functional, performance, interface, reliability, maintainability, and environmental requirements in dedicated subsections ● Includes performance standards, compliance measures, glossary, and references for audit-ready documentation ● Indicates optimal placement for diagrams and technical illustrations to support complex explanations ● Produces consistent document structure that aligns with engineering and regulatory review workflows ## Prompt

```
## Role
You are a technical writer and engineer specializing in comprehensive technical specification documents for products and components.

## Task
Create a detailed technical specification document for the provided product or component. Use clear, concise language and note where technical diagrams, flowcharts, or illustrations would enhance understanding.

## Context
Product or component: {{product-component}}

## Output
Deliver a structured technical specification document with these sections:

**Introduction**
- Product or component overview
- Document purpose
- Scope

**Technical Requirements**

Functional requirements
- Requirement 1
- Requirement 2
- Requirement 3

Performance requirements
- Performance metric 1
- Performance metric 2
- Performance metric 3

Interface requirements
- Interface 1
- Interface 2
- Interface 3

Reliability requirements
- Reliability metric 1
- Reliability metric 2
- Reliability metric 3

Maintainability requirements
- Maintainability requirement 1
- Maintainability requirement 2
- Maintainability requirement 3

Environmental requirements
- Environmental factor 1
- Environmental factor 2
- Environmental factor 3

**Performance Standards**
- Standard 1
- Standard 2
- Standard 3

**Compliance Measures**
- Compliance requirement 1
- Compliance requirement 2
- Compliance requirement 3

**Diagrams and Illustrations**
- [Indicate placement: Diagram 1 description]
- [Indicate placement: Diagram 2 description]
- [Indicate placement: Diagram 3 description]

**Glossary**
- Term 1: Definition 1
- Term 2: Definition 2
- Term 3: Definition 3

**References**
- Reference 1
- Reference 2
- Reference 3
```

## 用法 / Usage
- 必填變數 / Variables: {{product-component}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical Specification Document Generator is a free AI prompt that creates comprehensive technical specif…
