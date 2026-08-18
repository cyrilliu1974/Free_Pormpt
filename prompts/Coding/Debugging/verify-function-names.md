# Function Name Verification Prompt for Debugging

## 簡介

The Function Name Verification Prompt for Debugging is a free AI prompt that performs character-by-character analysis of function definitions and calls to catch naming mismatches that cause "undefined function" errors for developers and code reviewers. This function name verification prompt for ChatGPT, Claude, Gemini, and Grok extracts every function definition in your codebase, locates all function call attempts, and compares them systematically to flag typos, capitalization errors (camelCase vs snake_case), transposed letters, missing prefixes or namespaces, and confusable characters like l vs 1 or O vs 0. The output is a structured report with line numbers, error types, exact corrections, and a summary of patterns - such as consistent case mismatches - so you can prevent recurrence. Reach for this prompt when you face cryptic runtime errors traced to simple spelling or casing mistakes, or when onboarding code from multiple authors with inconsistent naming conventions. ● Extracts all function definitions with exact spelling and case, then compares every call character-by-character. ● Flags each mismatch with error type (misspelling, case mismatch, missing prefix, transposed letters), incorrect call, and corrected version. ● Identifies naming patterns across errors - like camelCase vs snake_case confusion - to help prevent future mistakes. ● Returns a structured report with line numbers, a summary of total mismatches, the most common error type, and corrected code snippets ready to paste. ## Prompt

```
## Role
You are a code verification specialist who identifies function name mismatches—typos, capitalization errors, and prefix omissions that cause "undefined function" errors.

## Task
Given {{code-and-errors}}, systematically:

1. **Extract** every function definition (name, exact spelling, case)
2. **Locate** every function call attempt
3. **Compare** character-by-character: spelling, capitalization, underscores, prefixes, namespaces
4. **Flag** each mismatch with:
   - Incorrect call as written
   - Error type (misspelling, case mismatch, missing prefix, transposed letters, etc.)
   - Correct name from definition
   - Corrected call
5. **Identify patterns** (e.g., consistent camelCase vs snake_case confusion) to prevent recurrence

**Focus exclusively on function name mismatches.** Ignore other code issues. Pay attention to:
- camelCase / PascalCase / snake_case mixing
- Missing or extra underscores
- Transposed letters ("recieve" vs "receive")
- Confusable characters (l vs 1, O vs 0)
- Missing namespaces or prefixes

Provide exact corrections with line numbers or context, not general advice.

## Output
Structure your response as:

### Defined Functions Found
- List each function definition with exact spelling

### Function Call Errors Identified

**Error 1:**
- **Line/Location:** [context]
- **Incorrect Call:** `functionNaem()`
- **Error Type:** Misspelling
- **Correct Definition:** `functionName()`
- **Fixed Call:** `functionName()`

[Repeat for each error]

### Summary of Corrections
- Total mismatches found: [number]
- Most common error type: [pattern if detected]
- All corrections to implement: [list]

### Corrected Code
[Provide fixed versions of problematic lines]
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-errors}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Function Name Verification Prompt for Debugging is a free AI prompt that performs character-by-character a…
