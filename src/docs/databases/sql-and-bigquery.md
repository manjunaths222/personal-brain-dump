---
title: "Sql And Bigquery"
---

SQL and BigQuery

Scope: Core SQL fundamentals, Advanced SQL patterns, BigQuery (GoogleSQL) specifics.

1 — Core SQL Concepts

Relational model: Tables = rows x columns. Schema = column names + types.
Primary key (PK), foreign keys (FK), constraints (NOT NULL, UNIQUE, CHECK).

Data types: Numeric (integer, decimal, floats), Text (CHAR/VARCHAR/TEXT), Temporal (DATE, TIME, TIMESTAMP), Binary/BLOB, JSON/XML, Arrays, Composite.

DDL: CREATE DATABASE/SCHEMA/TABLE, ALTER TABLE, DROP TABLE, CREATE VIEW, CREATE MATERIALIZED VIEW.
DML: SELECT, INSERT, UPDATE, DELETE, MERGE.

SQL Logical Processing Order: FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

Joins: INNER JOIN, LEFT/RIGHT/FULL OUTER JOIN, CROSS JOIN, SEMI/ANTI JOIN

Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD(), FIRST_VALUE(), LAST_VALUE()
ROWS BETWEEN / RANGE BETWEEN for moving averages.

CTEs: WITH cte AS (...) SELECT ... FROM cte
Recursive CTEs for tree/graph traversal.

Set operations: UNION / UNION ALL, INTERSECT, EXCEPT

Transactions & ACID: atomicity, consistency, isolation, durability.
Isolation levels: READ COMMITTED, REPEATABLE READ, SERIALIZABLE.

2 — Query Optimization

- Filter early (sargable predicates)
- Select only needed columns (avoid SELECT *)
- Use proper joins & keys; avoid cross-joins
- Use materialized views for expensive aggregations
- Use EXPLAIN plan to debug slow queries
- Join algorithms: nested loop, hash join, merge join

3 — BigQuery (GoogleSQL)

BigQuery is serverless, columnar, distributed — no traditional B-tree indexes.
Uses partitioning, clustering and column pruning for performance.
SQL dialect: GoogleSQL (ANSI-compliant with Google extensions).

BigQuery Data Types:
- Scalar: INT64, FLOAT64, NUMERIC, BIGNUMERIC, BOOL, STRING, BYTES, DATE, DATETIME, TIME, TIMESTAMP
- Complex: ARRAY<T> (ordered list), STRUCT (record with named fields)
- GEOGRAPHY (geospatial), JSON type
- Arrays of arrays NOT allowed; arrays of STRUCTs OK.

UNNEST: Main operator to flatten arrays.
project.dataset.orders

Partitioning & Clustering:
- Partitioning: breaks table into date/timestamp/integer-range partitions (huge cost & speed win)
- Clustering: sorts data within storage by columns (helps pruning, faster aggregations)
- Best practice: filter by partition key in WHERE clause
p.d.eventsp.d.raw_events

Time Travel:
p.d.orders

External Tables & Federated Queries:
- Query GCS Parquet/CSV/Avro/JSON, Google Drive, Bigtable, Sheets without importing
- EXTERNAL_QUERY for Cloud SQL, AlloyDB, Spanner

Views vs Materialized Views:
- Views: saved queries (virtual)
- Materialized views: precomputed + incrementally refreshed, great for dashboards

BigQuery ML (BQML):
myproj.myds.sales_modelmyproj.myds.training_datamyproj.myds.sales_modelmyproj.myds.new_data

Security:
- Project/dataset/table IAM
- Row-level security (row access policies)
- Column-level access control (policy tags via Data Catalog)
- Authorized views, VPC Service Controls, data masking

Performance & Cost Best Practices:
- Always specify columns needed; avoid SELECT *
- Filter early on partition column
- Use clustering for interested filter keys
- Use materialized views for heavy, repeated aggregations
- Dry-run query to estimate bytes billed
- Use APPROX_COUNT_DISTINCT() for huge cardinalities
- Use Query Plan to identify bottlenecks

Common BigQuery Recipes:
1. Flatten nested arrays & aggregate
2. Partitioned table SELECT with partition filter
3. BigQuery ML — train and predict
4. Time travel (point-in-time)
5. Stored procedure + dynamic SQL

BigQuery vs Traditional RDBMS:
- Serverless & columnar —"no VM cluster
- Nested/repeated types first-class (ARRAY, STRUCT)
- No conventional B-tree indexes — use partitioning & clustering
- Built-in ML via SQL (BigQuery ML)
