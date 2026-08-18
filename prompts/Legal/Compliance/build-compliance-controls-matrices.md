# Compliance Controls Matrix Builder

## 簡介

The Compliance Controls Matrix Builder is a free AI prompt that generates a complete, interactive web application for organizations managing complex regulatory requirements across multiple frameworks. This compliance controls matrix prompt for ChatGPT and Claude produces a full-stack React application with TypeScript and Tailwind CSS that connects regulatory citations to business processes and measurable controls. The output includes a sortable matrix interface, advanced filtering by regulation and risk level, a compliance dashboard with pass/fail metrics, detailed control modals with evidence tracking, a risk heat map visualizing coverage across frameworks, and CSV export capabilities. Real-world use cases include SOX audit preparation, GDPR compliance monitoring, HIPAA control tracking, and multi-framework regulatory reporting for enterprise compliance teams. The prompt runs on ChatGPT, Claude, and Cursor. Reach for this prompt when you need to replace scattered Excel files and outdated Word documents with a single source of truth for compliance management, or when preparing for audits across SOX, GDPR, HIPAA, SOC 2, or ISO 27001. ● Produces 8-12 business processes mapped to 20-30 controls across 5-6 regulatory frameworks with actual article numbers and three-lines-of-defense modeling ● Includes persistent filtering, window.storage-based state management, and virtualized tables that handle 50+ rows with smooth performance ● Generates evidence management interfaces with testing history timelines, remediation trackers, and audit trail indicators ● Delivers coverage heat maps, compliance dashboards, and export functions for audit reports in CSV and PDF formats ## Prompt

```
## Role

You are a regulatory compliance architect with deep expertise across SOX, GDPR, HIPAA, SOC 2, ISO 27001, and industry-specific mandates. You understand how auditors probe, how regulators think, and how operational teams need to work with compliance systems.

## Task

Build a comprehensive, interactive Compliance Controls Matrix web application that maps business processes to regulatory requirements and control activities with audit-level precision. The matrix serves as the single source of truth—connecting regulatory citations to actual business processes to measurable controls.

## Context

{{compliance-context}}

The organization needs immediate visibility into compliance posture: which processes are covered, which controls are failing, and where regulatory exposure exists. Current documentation is scattered across Excel files and outdated Word docs. The application must handle multiple overlapping regulatory frameworks simultaneously and provide the operational backbone for compliance management.

## Output

Deliver a single React artifact (application/vnd.ant.react) containing a complete, working Compliance Controls Matrix application with:

**Data Architecture Foundation**
- Core data models: ProcessArea, Regulation, Control with realistic enterprise scenarios
- 8-12 business processes, 20-30 controls, 5-6 regulatory frameworks
- Actual regulation names and article numbers (e.g., "GDPR Article 32", "SOX Section 404")
- Three-lines-of-defense model mapping
- Both IT and operational controls

**Core Matrix Interface**
- Main table component with sortable columns, inline status indicators, quick-action buttons
- Virtualization for 50+ rows with smooth performance
- Enterprise-grade styling: subtle borders, appropriate spacing, professional hover states
- Information-dense layout prioritizing scannability over whitespace
- Visual design: Bloomberg Terminal meets Airtable—serious, data-dense, instantly trustworthy

**Advanced Filtering System**
- Persistent filter panel with multi-select dropdowns, risk level toggles, status checkboxes, date range selectors
- Instant updates without "Apply" button
- Active filter count display
- Save preferences to window.storage

**Compliance Dashboard**
- Metrics cards: testing compliance rate, critical issues count, pass/fail distribution, upcoming deadlines
- Mini visualizations for impact
- Clickable metrics that auto-filter the matrix

**Detail Modal & Evidence Management**
- Comprehensive modal with full control details, testing history timeline, evidence section with realistic artifact names (e.g., "Q3_AccessReview_Results.pdf"), remediation tracker, notes section
- Action buttons that update data and refresh matrix view
- Audit trail indicators

**Risk Heat Map & Export**
- Coverage Map view: processes on X-axis, regulatory frameworks on Y-axis, color-coded cells by control maturity
- CSV export for filtered views
- Audit report generation in PDF/Excel formats

**Enterprise-Grade Polish**
- Smooth animations, loading states, empty states with guidance
- Keyboard shortcuts, tooltips, consistent icons, help panel
- All user edits saved to window.storage (shared: false) for persistence
- NEVER use localStorage or sessionStorage
- Must work flawlessly on desktop (primary) and tablet

**Technical Implementation**
- Tech Stack: React with TypeScript, Tailwind CSS, React hooks for state management
- Dark mode color palette: slate grays (#334155, #475569), clean whites, strategic accents (green: #10b981, amber: #f59e0b, red: #ef4444)
- Clean information hierarchy inspired by Linear.app combined with Stripe's trustworthy minimalism
- Color used sparingly and consistently
- Components: ComplianceMatrix.tsx, FilterPanel.tsx, ControlDetailModal.tsx, data.ts
- Clear component boundaries with descriptive names
- Comment sections: // === DASHBOARD METRICS ===, // === MAIN MATRIX TABLE ===
- Production-ready, well-structured code
- Human-friendly interface copy using sentence case

Provide complete, working code ready for immediate deployment.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Compliance Controls Matrix Builder is a free AI prompt that generates a complete, interactive web applicat…
