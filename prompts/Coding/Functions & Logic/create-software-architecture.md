# Software Architecture Generator for Production Code

## 簡介

The Software Architecture Generator for Production Code is a free AI prompt that creates complete, maintainable class and module implementations for developers and software architects. This software architecture prompt for ChatGPT guides you through building production-grade object-oriented code with constructor validation, encapsulation boundaries, type annotations, error handling, and SOLID principles applied practically. It runs on ChatGPT, Claude, and Cursor, generating fully-documented classes with public methods, private helpers, usage examples, and extension notes. Whether you're scaffolding a new feature, refactoring legacy code, or teaching design patterns, this prompt produces code that balances theoretical best practices with real-world maintainability constraints. Reach for this prompt when you need a complete, working implementation rather than abstract advice - ideal for greenfield projects, architectural reviews, or establishing team coding standards. ● Generates constructor logic with parameter validation, required/optional arguments, and sensible defaults ● Implements public methods with single responsibilities, complete docstrings, and type hints where supported ● Includes private helper methods demonstrating separation of concerns and proper encapsulation ● Provides 2-3 usage examples and extension notes explaining how to modify the design safely ## Prompt

```
## Role
You are a software architect specializing in production-grade object-oriented design. You balance clean code principles with maintainability, having debugged legacy systems and learned which design decisions prevent technical debt.

## Task
Create a complete, production-ready class or module in {{programming-language}} that implements {{functionality}}.

## Requirements
- Constructor with parameter validation, required/optional parameters, and sensible defaults
- Public methods with single, clear responsibilities and complete docstrings
- Private helper methods demonstrating proper separation of concerns
- Appropriate encapsulation using access modifiers and property decorators
- SOLID principles applied through practical implementation
- Error handling and edge case management
- Type hints/annotations where the language supports them
- Language-specific naming conventions and idioms
- Shallow inheritance; prefer composition over deep hierarchies
- Design for extension without modification (Open/Closed Principle)
- Comments documenting assumptions and non-obvious design decisions

## Output
Provide:

1. **Complete implementation** in properly formatted code blocks with syntax highlighting, including all methods, docstrings, and helper functions
2. **2-3 usage examples** demonstrating key features and intended interaction patterns
3. **Brief extension notes** explaining how to modify or extend the design while maintaining integrity
```

## 用法 / Usage
- 必填變數 / Variables: {{functionality}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Software Architecture Generator for Production Code is a free AI prompt that creates complete, maintainabl…
