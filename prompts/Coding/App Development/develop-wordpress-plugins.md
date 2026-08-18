# WordPress Plugin Generator for Production Code

## 簡介

The WordPress Plugin Generator for Production Code is a free AI prompt that generates complete, deployment-ready WordPress plugins with full architecture, security measures, and WordPress.org compliance for developers building commercial or client plugins. This WordPress plugin development prompt for ChatGPT, Claude, and Cursor takes your plugin requirements and outputs a complete directory structure with production code - main plugin file, admin interfaces, frontend components, database layers, REST API endpoints, and uninstall procedures. It builds plugins that follow WordPress VIP coding standards, implement nonces and prepared statements, use the Settings API and hooks system, and include internationalization support. Developers use it to scaffold plugins for client projects, commercial marketplaces, or internal tools that must pass WordPress.org review and handle real traffic. Reach for this prompt when you need a plugin foundation that implements security from day one, not as an afterthought, and when you want architecture that scales beyond a single-file hack. ● Outputs a complete file structure with singleton pattern, autoloading, and MVC separation into Admin, Frontend, Database, AJAX, and REST API classes. ● Implements comprehensive security measures including nonces, sanitization, validation, escaping, capability checks, and prepared statements in every interaction. ● Generates admin settings pages using the Settings API, Gutenberg blocks, shortcodes, template files with theme override support, and conditional asset enqueueing. ● Includes database table creation with dbDelta(), proper indexes, object cache integration, complete uninstall cleanup, PHPDoc blocks, and a WordPress.org-ready README.txt. ## Prompt

```
## Role

You are a senior WordPress architect with deep expertise in enterprise plugin development, WordPress VIP standards, and the official plugin repository requirements.

## Task

Generate a complete, production-ready WordPress plugin with full file structure and implementation code.

## Context

{{plugin-requirements}}

This code will be reviewed against WordPress.org repository standards and used in production environments. Security vulnerabilities, coding standard violations, or poor database queries are unacceptable.

## Requirements

The plugin must:

- Follow WordPress Coding Standards and VIP guidelines
- Implement comprehensive security: nonces, sanitization, validation, escaping, capability checks, prepared statements
- Use proper WordPress APIs: Settings API, REST API, hooks system
- Include admin interface, frontend display, and database operations
- Support internationalization with proper text domains
- Provide complete uninstall cleanup
- Be deployable immediately without placeholders or TODOs

## Output

Provide the complete plugin as a directory structure with full file contents:

**Foundation**
- Main plugin file with headers, constants, singleton pattern, autoloading
- Directory structure documentation

**Core Architecture**
- Separate classes for Admin, Frontend, Database, AJAX, REST API (MVC principles)

**Admin Interface**
- Settings pages using Settings API
- Meta boxes and admin notices
- Modern, accessible UI

**Frontend Integration**
- Shortcodes and Gutenberg blocks
- Template files with theme override capability

**Database Layer**
- Table creation with dbDelta(), proper charset/collation, indexes
- Cleanup procedures

**API Development**
- REST endpoints and AJAX handlers
- Authentication and rate limiting

**Asset Management**
- Conditional CSS/JS enqueueing with versioning and dependencies
- Performance optimization

**Performance & Caching**
- WordPress object cache integration
- Query optimization and lazy loading

**Documentation**
- PHPDoc blocks throughout
- Inline comments explaining complex logic
- Complete README.txt for WordPress.org

**Uninstall**
- Complete cleanup removing all data, options, and tables

Provide production-ready code for each file with detailed comments. Ensure all security measures are implemented and no placeholder code remains.
```

## 用法 / Usage
- 必填變數 / Variables: {{plugin-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The WordPress Plugin Generator for Production Code is a free AI prompt that generates complete, deployment-rea…
