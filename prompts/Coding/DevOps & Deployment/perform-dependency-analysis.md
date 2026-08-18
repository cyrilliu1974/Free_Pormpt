# Dependency Analysis and Optimization Prompt

## 簡介

The Dependency Analysis and Optimization Prompt is a free AI prompt that conducts deep dependency overhead analysis for engineers managing production software systems. This dependency analysis prompt for ChatGPT, Claude, Gemini, and Grok calculates total dependency weight including all transitive dependencies, maps the complete dependency tree to surface redundant packages and version conflicts, compares actual code usage against overhead, researches lighter alternatives, and delivers a prioritized elimination strategy ranked by risk and impact. Engineers use it to reduce bundle sizes before deployment, audit legacy codebases with bloated node_modules folders, evaluate framework migrations, and optimize build pipelines in CI/CD environments. Reach for this prompt when you need actionable insights into which dependencies contribute disproportionate weight relative to their utility, or when planning a phased rollout to strip unnecessary packages without introducing breaking changes. ● Maps transitive dependency trees to expose hidden redundancies and version conflicts across the entire project graph. ● Compares actual code usage against dependency overhead to identify packages that consume disproportionate space. ● Suggests lighter alternatives for heavy dependencies and provides specific elimination candidates with fallback options. ● Delivers a phased implementation roadmap with risk assessments, testing requirements, and success metrics for each optimization. ## Prompt

```
## Role

You are a dependency optimization engineer specializing in bundle analysis, transitive dependency mapping, and elimination strategies for production software systems.

## Task

Conduct a comprehensive dependency overhead analysis of the provided project. Calculate total dependency weight including all transitive dependencies, map the complete dependency tree to identify redundant packages and version conflicts, compare actual code usage against dependency overhead, research lighter alternatives for heavy dependencies, develop a prioritized elimination strategy considering risk and impact, and provide specific recommendations for bundle size reduction.

## Context

{{project-context}}

Focus on transitive dependencies, bundle size impact, and version conflicts. Identify packages that contribute disproportionate weight relative to their utility. Prioritize optimizations by risk, impact, and implementation effort.

## Output

Structure your analysis in markdown format with these sections:

- **Executive Summary** – key findings and total potential savings
- **Dependency Weight Analysis** – total weight, heaviest packages, overhead metrics
- **Transitive Dependency Tree** – visual mapping of dependency chains, redundancies, and version conflicts
- **Optimization Recommendations** – lighter alternatives, elimination candidates, and bundle size tactics ranked by impact
- **Risk Assessment** – breaking change probability, fallback options, and testing requirements for each recommendation
- **Implementation Roadmap** – phased rollout plan with specific next steps and success metrics

Include concrete numbers, package names, version ranges, and actionable commands where applicable.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Dependency Analysis and Optimization Prompt is a free AI prompt that conducts deep dependency overhead ana…
