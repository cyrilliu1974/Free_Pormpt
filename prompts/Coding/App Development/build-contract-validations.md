# Contract Cross-Reference Validation App Builder

## 簡介

The Contract Cross-Reference Validation App Builder is a free AI prompt that generates a complete React application for validating cross-references in legal contracts, designed for legal technology specialists and developers building document review tools. This contract validation prompt for ChatGPT, Claude, and Cursor outputs a full-stack TypeScript application that parses uploaded contracts (PDF, DOCX, TXT), extracts section references, defined terms, exhibit citations, and schedule references, then cross-validates each one against the actual document structure. It catches non-existent clauses, incorrect paragraph numbering, and ambiguous citations - common errors that can derail M&A transactions and due diligence processes. The generated app uses regex patterns tuned to legal document formats, Bluebook citation standards, and complex numbering schemes like "Section 3.2(a)(ii)." Reach for this prompt when you need a client-side contract review tool that processes 100-page documents in under 10 seconds without sending data to a server. ● Extracts and validates section references, defined terms, exhibits, schedules, and clause citations using legal-document-aware regex patterns ● Maps complete document structure and flags errors by severity (CRITICAL for non-existent references, HIGH for incorrect numbering, MEDIUM for ambiguous citations, LOW for formatting inconsistencies) ● Generates a three-panel interface with live validation results, side-by-side reference comparison with context snippets, color-coded badges, and an interactive document structure tree ● Outputs TypeScript code using React 18, Tailwind CSS, shadcn/ui, Zustand state management, react-pdf, mammoth, and jsPDF with dark mode styling, keyboard shortcuts, web workers for non-blocking processing, and auto-save every 30 seconds ## Prompt

```
## Role

You are a legal technology specialist building contract validation tools. You combine legal document precision with systematic software architecture thinking.

## Task

Build a production-ready React application that validates cross-references in legal contracts. The system must catch section references pointing to non-existent clauses, definitions referencing wrong paragraphs, exhibits cited incorrectly, and other structural errors.

**Core Features:**

1. **Document Processing** — Parse uploaded contracts (PDF, DOCX, TXT) and extract all cross-references: section references, defined terms, exhibit references, schedule references, clause citations

2. **Structure Mapping** — Build a complete document map showing actual structure with all sections, subsections, definitions, exhibits, schedules with real numbering

3. **Validation Engine** — Cross-validate every reference against actual document structure using:
   - Section detection: `/(?:Section|§)\s*(\d+(?:\.\d+)*)/gi`
   - Defined terms: `/(?:"([^"]+)"|'([^']+)')\s+(?:means|shall mean|refers to)/gi`
   - Exhibit references: `/Exhibit\s+([A-Z](?:-\d+)?)/gi`
   - Handle nested references like "as defined in Section 3.2(a)(ii)"

4. **Error Classification** — Flag discrepancies by severity:
   - CRITICAL: non-existent references
   - HIGH: incorrect numbering
   - MEDIUM: ambiguous references
   - LOW: formatting inconsistencies

5. **Interactive Interface** — Three-panel layout:
   - Document upload/preview
   - Live validation results with side-by-side comparison (extracted reference vs actual target with context snippets)
   - Document structure tree
   - Color-coded reference badges: green (valid), red (broken), yellow (ambiguous)

6. **Professional Reporting** — Generate PDF reports with executive summary, detailed findings table, and remediation recommendations

## Context

**Tech Stack:** React 18, TypeScript, Tailwind CSS, shadcn/ui, Zustand, react-pdf, mammoth, jsPDF

**Visual Design:** Linear.app-inspired minimalism with dark mode (slate-900 background), emerald-500 success indicators, rose-500 error highlights

**Performance:** Process 100-page contract in under 10 seconds using web workers to avoid UI blocking

**Security:** All processing client-side only, never upload to server, clear data after session

**UX Details:**
- Keyboard shortcuts: Cmd+U (upload), Cmd+R (validate), Cmd+E (export)
- Animated progress indicators showing extraction/mapping/validation stages
- Auto-save validation state every 30 seconds
- User-friendly error messages for upload failures, missing structure, zero references detected

**Legal Accuracy:** Use Bluebook citation standards, recognize legal document patterns, handle peculiar numbering schemes

**User Inputs:**
- {{contract-file}} — the contract document to validate (PDF, DOCX, or TXT)
- {{error-threshold}} — minimum severity level to report: CRITICAL, HIGH, MEDIUM, or LOW
- {{report-branding}} — company name and logo URL for PDF output

## Output

Provide a single, complete React application with:

**Component Structure:**
- App → ContractValidator → [DocumentUploader, ValidationEngine, ResultsPanel, StructureTree, ReportGenerator]

**Custom Hooks:**
- useContractParser
- useReferenceExtractor
- useValidationEngine

**Code Requirements:**
- Full TypeScript interfaces for all data structures
- Tailwind utility classes only (no custom CSS)
- Self-contained code using allowed libraries only
- Sample contracts with intentional errors for demonstration
- Conversational interface language ("Upload Contract" not "Ingest Document")
- Gentle animations and helpful empty states
```

## 用法 / Usage
- 必填變數 / Variables: {{contract-file}}、{{error-threshold}}、{{report-branding}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Contract Cross-Reference Validation App Builder is a free AI prompt that generates a complete React applic…
