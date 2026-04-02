---
title: "Postgresql"
---

PostgreSQL Tutorial (Neon)

1. Getting Started: Install on Windows/macOS/Linux; connect via psql or GUI; sample DB: dvdrental or pagila.

2. Querying Data: SELECT, Column Aliases (AS), ORDER BY, DISTINCT

3. Filtering: WHERE, AND/OR, LIMIT/FETCH, IN, BETWEEN, LIKE/ILIKE (case-insensitive), IS NULL

4. Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, CROSS JOIN, NATURAL JOIN, SELF JOIN, Table Aliases

5. Grouping & Aggregation: GROUP BY, HAVING, GROUPING SETS (multiple grouping levels), CUBE (all combinations), ROLLUP (progressive aggregation)

6. Set Operations: UNION, UNION ALL, INTERSECT, EXCEPT

7. Subqueries & CTEs:
* Subquery: SELECT title FROM film WHERE length > (SELECT AVG(length) FROM film);
* Correlated Subquery, ANY/ALL/EXISTS
* CTE (WITH clause): Named subquery for reuse within a single query.
* Recursive CTE: For hierarchical/graph data.

8. Modifying Data: INSERT, UPDATE, DELETE, UPSERT (ON CONFLICT), MERGE, UPDATE/DELETE with JOIN

9. Transactions: BEGIN / COMMIT / ROLLBACK (ACID properties)

10. Import/Export: COPY command - COPY customers FROM '/tmp/customers.csv' CSV HEADER;

11. Managing Tables: CREATE/DROP/ALTER, TRUNCATE, Temporary Tables, SELECT INTO/CTAS, Identity Columns (SERIAL, GENERATED AS IDENTITY), Sequences, Generated Columns

12. Constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT

13. Rich Data Types: Boolean, CHAR/VARCHAR/TEXT, INTEGER/NUMERIC/DECIMAL/DOUBLE PRECISION, DATE/TIME/TIMESTAMP/INTERVAL, UUID, JSON/JSONB, hstore, Array, ENUM, XML, BYTEA, Composite types

14. Conditional Expressions: CASE, COALESCE, NULLIF, CAST

CTE Examples:
Simple CTE:
  WITH avg_orders AS (
    SELECT AVG(amount) AS avg_amount FROM orders
  )
  SELECT o.order_id, o.amount
  FROM orders o, avg_orders a
  WHERE o.amount > a.avg_amount;

Multiple CTEs:
  WITH
  high_value_orders AS (SELECT * FROM orders WHERE amount > 1000),
  customer_totals AS (SELECT customer_id, SUM(amount) AS total FROM orders GROUP BY customer_id)
  SELECT c.customer_id, c.total FROM customer_totals c JOIN high_value_orders h ON c.customer_id = h.customer_id;

Recursive CTE (Employee Hierarchy):
  WITH RECURSIVE employee_hierarchy AS (
    SELECT emp_id, name, manager_id FROM employees WHERE emp_id = 1  -- Anchor
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.emp_id     -- Recursive
  )
  SELECT * FROM employee_hierarchy;

Recursive CTE (Number Generator):
  WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 10
  )
  SELECT * FROM numbers;  -- Outputs 1 to 10

Key Points:
* CTEs = cleaner, reusable, easier to debug vs deeply nested subqueries
* Recursive CTEs = walk hierarchies, graphs, or generate data until stopping condition
* PostgreSQL supports both fully; MySQL supports CTEs since 8.0
