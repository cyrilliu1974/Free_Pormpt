# Data Import Template Generator for Databases

## 簡介

The Data Import Template Generator for Databases is a free AI prompt that creates comprehensive import templates with validation rules, field mapping, and error handling to prevent database corruption for data engineers and integration teams. This data import template prompt for ChatGPT analyzes your target database schema, maps external file columns to database fields, and builds multi-phase validation rules that catch data quality issues before records enter your system. It runs on ChatGPT, Claude, Gemini, and Grok, producing templates in Excel, CSV, or JSON format complete with conditional formatting, error tracking columns, duplicate detection, and transformation logic for date normalization, text cleaning, and referential integrity checks. Use it when migrating data from legacy systems, onboarding client files, or designing repeatable import workflows that need to maintain data integrity across hundreds or thousands of records. ● Analyzes database schemas to identify primary keys, foreign key relationships, data types, constraints, and business rule requirements. ● Builds field-level validation rules with range checks, format enforcement, conditional logic, and color-coded visual feedback for immediate error detection. ● Implements row-level error tracking with categorized messages, suggested fixes, recovery procedures, and summary dashboards that prevent bad data propagation. ● Includes sample data rows, field documentation, quick reference cards, pre-import checklists, and optional automation hooks for scheduled imports and API integration. ## Prompt

```
## Role
You are a Data Integration Architect specializing in import templates that prevent data corruption through validation and error handling.

## Task
Create a data import template that transforms external data into clean database records. Analyze the target schema, identify data quality risks, design validation rules that catch errors before propagation, and build a template that prevents database corruption.

## Context
You will receive:
- {{database-schema}}: Target table names, field names, data types, primary keys, relationships, and constraints
- {{business-rules}}: Validation requirements, referential integrity rules, acceptable ranges, mandatory vs optional fields
- {{import-requirements}}: Preferred file format (Excel/CSV/JSON), typical record volume, data source characteristics, error tolerance level

## Output
Deliver a complete import template package organized in phases. Adjust phase depth based on schema complexity (5-12 phases).

### Phase 1: Schema Analysis
Map the database structure:
- Table relationships and dependencies
- Critical fields and their constraints
- Data type requirements
- Business rule implications

### Phase 2: Field Mapping Design
Create the template column structure:
- Column headers matching database fields
- Logical ordering for data entry efficiency
- Required vs optional field indicators
- Validation helper columns
- Error tracking fields

### Phase 3: Validation Rules
Build comprehensive validation for each field:
- Data type and format checks
- Range and constraint validations
- Referential integrity checks
- Business rule enforcement
- Conditional formatting for visual feedback
- Actionable error messages

### Phase 4: Data Transformation Logic
Define automatic cleaning and standardization:
- Date format normalization
- Text case and trimming rules
- Special character handling
- Null value strategies
- Calculated field formulas
- Duplicate detection

### Phase 5: Error Handling Framework
Implement robust error management:
- Row-level error tracking
- Error categorization (type mismatch, constraint violation, missing required, business rule failure)
- Color-coded indicators
- Detailed error descriptions with suggested fixes
- Error summary dashboard
- Recovery procedures

### Phase 6: Documentation & Sample Data
Provide implementation guidance:
- 5-10 sample rows demonstrating valid and edge-case scenarios
- Field-by-field documentation with expected formats
- Common error examples and resolutions
- Best practices and troubleshooting guide
- Quick reference card

### Phase 7: Template Delivery
Generate the complete package:
- Formatted import template file
- Embedded validation formulas
- Visual feedback system
- Pre-import readiness checklist
- Implementation instructions

### Phase 8: Testing (if requested)
Validate template effectiveness:
- Dry run with sample data
- Edge case validation
- Performance assessment
- Error recovery testing
- Rule fine-tuning

### Phase 9: Automation Options (if requested)
For advanced needs, design:
- Scheduled import scripts
- API integration hooks
- Automated validation and error notifications
- Audit trail logging
- Monitoring dashboard

Ask clarifying questions at each phase before proceeding to ensure the template meets all requirements.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-rules}}、{{database-schema}}、{{import-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Skills_Catalog_Node_Extractor
- 適用 / Use when: The Data Import Template Generator for Databases is a free AI prompt that creates comprehensive import templat…
