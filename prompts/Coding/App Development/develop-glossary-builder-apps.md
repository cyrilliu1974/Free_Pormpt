# Glossary Builder App Code Generator

## 簡介

The Glossary Builder App Code Generator is a free AI prompt that builds a complete, production-ready glossary application in React + TypeScript for teams managing terminology and documentation. This glossary builder prompt for ChatGPT generates a full-stack application with fuzzy search, alphabetical navigation, multi-select category filtering, admin interfaces, and export functionality in PDF and CSV formats. The prompt runs on ChatGPT, Claude, and Cursor, delivering complete component code with Tailwind CSS styling, localStorage persistence, and 20+ sample terms to demonstrate all features. It produces real working code with TypeScript interfaces, debounced search, keyboard shortcuts for power users, and accessibility features built in. Use it when your team needs a centralized terminology system, onboarding documentation tool, or knowledge base that goes beyond static glossaries. ● Outputs fuzzy search with match highlighting, alphabetical navigation, and multi-category filtering to help users find terms instantly. ● Includes admin functionality for adding and editing terms with rich usage examples and cross-reference linking between related concepts. ● Generates glassmorphic responsive UI with smooth animations, keyboard shortcuts, and semantic HTML with ARIA labels for accessibility. ● Delivers export capabilities in PDF and CSV formats plus localStorage implementation for client-side data persistence. ## Prompt

```
## Role

You are an expert information architect and enterprise UX developer specializing in documentation systems and knowledge management interfaces. You combine clean design principles with practical functionality to create glossary systems that teams use daily.

## Task

Build a complete, production-ready professional glossary application in React + TypeScript with Tailwind CSS. Implement instant fuzzy search, category filtering, cross-referencing, admin functionality, and export capabilities (PDF/CSV). Use localStorage for persistence and include 20+ realistic sample terms.

## Context

{{glossary-context}}

## Requirements

**Core Features**
- Fuzzy search across terms, definitions, and tags with match highlighting
- Alphabetical navigation and multi-select category filtering
- Individual term detail pages with cross-references to related terms
- Admin interface for adding/editing terms with rich usage examples
- Keyboard shortcuts for power users
- Export functionality (PDF and CSV formats)

**Technical Implementation**
- Complete React + TypeScript code with all components fully implemented
- Clear separation of concerns with reusable components
- TypeScript interfaces for type safety
- localStorage for data persistence
- Debounced search and loading states for performance
- Semantic HTML and ARIA labels for accessibility

**UI/UX Design**
- Glassmorphic design with smooth transitions and animations
- Mobile-first responsive layout
- Intuitive navigation patterns
- Clean, minimalist aesthetic

**Code Quality**
- No placeholder or incomplete implementations
- Proper error handling throughout
- Production-ready components
- Realistic sample data demonstrating all features

## Output

Provide complete working code organized as follows:

1. **Project Structure** - File organization and component architecture
2. **Core Components** - SearchBar, TermCard, CategoryFilter, AddTermForm, TermDetail
3. **Data Management** - TypeScript interfaces, sample data, localStorage implementation
4. **Search Functionality** - Fuzzy matching algorithm with highlighting
5. **UI Implementation** - Tailwind CSS styling, animations, responsive breakpoints
6. **Advanced Features** - Cross-referencing logic, export functions, keyboard shortcuts
7. **Deployment Setup** - Configuration and setup instructions for immediate use

Deliver a fully functional application ready for immediate deployment.
```

## 用法 / Usage
- 必填變數 / Variables: {{glossary-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Glossary Builder App Code Generator is a free AI prompt that builds a complete, production-ready glossary …
