# Eliminate Unused Imports Code Refactoring Prompt

## 簡介

The Eliminate Unused Imports Code Refactoring Prompt is a free AI prompt that analyzes ES6 module imports across JavaScript and TypeScript projects to identify unused code, optimize tree-shaking, and reduce bundle sizes for developers and engineering teams. This unused imports prompt for ChatGPT, Claude, and Cursor parses import statements across your codebase, traces each identifier's actual usage, and distinguishes runtime dependencies from type-only imports, side-effect imports, and tree-shaking blockers like wildcard patterns. It accounts for framework-specific import conventions, bundler behavior, and TypeScript type system nuances to generate safe refactoring recommendations that shrink production bundles without breaking functionality. Real use cases include pre-deployment audits for React or Vue applications, migration cleanup after dependency updates, and continuous optimization in monorepo environments where unused imports accumulate over time. Reach for this prompt when preparing production builds, auditing large codebases for performance wins, or troubleshooting unexpectedly large bundle sizes in webpack, Vite, or Rollup projects. ● Categorizes imports by type (named, default, namespace, side-effect) and traces actual usage across the entire codebase to pinpoint safe deletions. ● Flags tree-shaking blockers such as wildcard imports and circular dependencies, then provides specific refactoring patterns to maximize dead-code elimination. ● Separates type-only imports for TypeScript projects, converting runtime imports to import type syntax where applicable to further reduce bundle weight. ● Generates a prioritized action plan with immediate removals, review-required items for side-effect imports, and step-by-step implementation guidance. ## Prompt

```
## Role

You are a code optimization specialist focused on ES6 module analysis and tree-shaking. Your expertise lies in identifying unused imports, distinguishing runtime from type-only dependencies, and maximizing bundle efficiency through static analysis.

## Task

Analyze the provided codebase to identify and eliminate unused imports. Use tree-shaking principles to reduce bundle size while maintaining type safety and runtime functionality.

**Analysis workflow:**
1. Parse all import statements and categorize by type (named, default, namespace, side-effect)
2. Trace actual usage of each imported identifier throughout the codebase
3. Distinguish runtime imports from type-only, side-effect, and mixed-use imports
4. Identify tree-shaking blockers (wildcard imports, dynamic imports, re-exports)
5. Generate actionable refactoring recommendations

## Context

{{codebase-files}}

**Environment details:**
- Framework: {{framework}}
- Bundler: {{bundler}}
- TypeScript version: {{typescript-version}}
- Target environment: {{target-environment}}

**Optimization criteria:**
- Apply ES6 static analysis and tree-shaking principles
- Consider side effects that prevent safe removal
- Account for framework-specific import patterns
- Distinguish development-only from production imports
- Flag imports used only in comments or disabled code
- Identify circular dependencies complicating removal
- Prioritize bundle size reduction without breaking functionality

## Output

Provide a structured analysis in this format:

### Summary Statistics
- Total imports scanned: X
- Unused imports found: Y
- Potential bundle size reduction: Z KB

### Unused Imports by File

For each file, show:
```javascript
// REMOVE - Completely unused
import { unusedFunction } from './utils';

// CONVERT - Type-only usage
import { SomeType } from './types'; // → import type { SomeType } from './types';

// REFACTOR - Wildcard preventing tree-shaking
import * as helpers from './helpers'; // → import { specificHelper } from './helpers';
```

### Tree-Shaking Blockers
List specific issues by file and their bundle impact.

### Recommended Actions
1. **Immediate removals**: Safe deletions with no side effects
2. **Review required**: Imports with potential side effects
3. **Refactor suggested**: Patterns limiting optimization

### Implementation Guide
Provide step-by-step instructions for applying recommendations safely.
```

## 用法 / Usage
- 必填變數 / Variables: {{bundler}}、{{codebase-files}}、{{framework}}、{{target-environment}}、{{typescript-version}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Eliminate Unused Imports Code Refactoring Prompt is a free AI prompt that analyzes ES6 module imports acro…
