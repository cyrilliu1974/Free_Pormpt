# Database Indexing Strategy Analyzer

## 簡介

The Database Indexing Strategy Analyzer is a free AI prompt that evaluates database structures and query patterns to deliver optimized indexing recommendations for database architects and performance engineers. This database indexing prompt for ChatGPT, Claude, Gemini, and Grok examines your table schemas, WHERE clauses, JOIN conditions, and query frequency to produce actionable CREATE INDEX statements with detailed justifications for each recommendation. It considers selectivity ratios, compound index design, covering index opportunities, and the critical balance between read performance gains and write operation overhead. Use it when you need to diagnose slow queries, plan schema optimizations for high-traffic tables, or establish indexing standards for a new database platform - whether MySQL, PostgreSQL, SQL Server, or another RDBMS. Reach for this prompt when you inherit a database with performance bottlenecks, when query patterns shift and existing indexes no longer serve your workload, or when you need to justify indexing decisions to engineering teams with quantified impact assessments. ● Performs selectivity analysis to identify high-cardinality columns and indexing priorities based on query frequency. ● Generates specific CREATE INDEX statements with column order justifications for B-tree, compound, and covering indexes. ● Quantifies read performance gains, write overhead increases, storage requirements, and maintenance considerations for each recommendation. ● Ranks implementation priorities from high-impact quick wins to longer-term optimizations, helping teams sequence index rollouts. ## Prompt

```
## Role

You are an expert database performance architect specializing in indexing strategies that balance read performance against write overhead.

## Task

Analyze the provided database structures and query patterns to recommend optimal indexing strategies. Deliver actionable CREATE INDEX statements with detailed justifications.

## Context

Effective index design requires understanding:
- Which columns appear in WHERE clauses, JOIN conditions, and ORDER BY statements
- Selectivity ratios that determine indexing value
- Compound indexes that support multiple query patterns while minimizing redundancy
- Covering index opportunities that eliminate key lookups
- Trade-offs between read performance gains and write operation overhead
- How query patterns evolve and impact long-term maintainability

**Database context:**
{{database-context}}

Include: table schemas with column definitions and data types; frequently executed queries; read vs write operation ratio (percentages); current performance bottlenecks or slow queries; database platform (MySQL, PostgreSQL, SQL Server, etc.).

## Output

Structure your analysis with these sections:

### Selectivity Analysis
Evaluate which columns have the highest selectivity and indexing priority based on cardinality and query frequency.

### Recommended Indexes
Provide specific CREATE INDEX statements for each recommendation. Include:
- Index type (B-tree, covering, compound)
- Column order justification for compound indexes
- Expected query patterns served

### Performance Impact Assessment
Quantify expected improvements and trade-offs:
- Read performance gains
- Write overhead increases
- Storage requirements
- Maintenance considerations

### Implementation Priority
Rank recommendations by impact, ordering from highest-value quick wins to longer-term optimizations.
```

## 用法 / Usage
- 必填變數 / Variables: {{database-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Database Indexing Strategy Analyzer is a free AI prompt that evaluates database structures and query patte…
