---
title: "Database Concepts"
---

Database Concepts

1. Concepts Covered in MySQL vs PostgreSQL Tutorials:
Topic: Getting Started | MySQL: basics querying, filtering | PostgreSQL: install, connect to DB
Topic: Querying | MySQL: SELECT, ORDER BY, WHERE, operators | PostgreSQL: SELECT, aliases, DISTINCT, AND/OR/IN/BETWEEN/LIKE/IS NULL
Topic: Joins | MySQL: inner, left joins | PostgreSQL: INNER, LEFT, RIGHT, FULL OUTER, SELF-JOIN, NATURAL, CROSS + table aliases
Topic: Grouping | MySQL: COUNT, SUM, MAX, MIN, AVG | PostgreSQL: GROUP BY, HAVING, CUBE, ROLLUP
Topic: Set Ops | MySQL: basic UNION | PostgreSQL: UNION, INTERSECT, EXCEPT
Topic: Subqueries/CTEs | MySQL: subqueries | PostgreSQL: Correlated Subquery, ANY/ALL/EXISTS, CTEs, recursive CTEs
Topic: DML | MySQL: INSERT, UPDATE, DELETE | PostgreSQL: INSERT (single/multiple), UPDATE, DELETE, Upsert/MERGE
Topic: Transactions | MySQL: BEGIN/COMMIT/ROLLBACK | PostgreSQL: full transaction coverage
Topic: Data Types | MySQL: VARCHAR, TEXT, DATE, numeric | PostgreSQL: rich - arrays, enums, JSON, hstore, UUID, JSONB, composite types
Topic: Advanced | MySQL: stored procedures, hierarchical data | PostgreSQL: Views, Indexes, Triggers, Functions (PL/pgSQL), psql commands

Overall: PostgreSQL is more feature-rich; MySQL covers standard SQL basics.

2. SQL Join Types (tables: employees(emp_id, name, dept_id), departments(dept_id, dept_name)):

a) INNER JOIN: Return only matching rows from both tables.
   SELECT e.name, d.dept_name FROM employees e INNER JOIN departments d ON e.dept_id = d.dept_id;

b) LEFT JOIN: All rows from left table + matching from right (NULL where no match).
   SELECT e.name, d.dept_name FROM employees e LEFT JOIN departments d ON e.dept_id = d.dept_id;

c) RIGHT JOIN: All rows from right table + matching from left (NULL where no match).

d) FULL OUTER JOIN: All rows from both tables, NULLs where no match. (MySQL needs UNION workaround; PostgreSQL supports natively.)

e) CROSS JOIN: Cartesian product - every row of first paired with every row of second.
   10 employees x 3 departments = 30 rows.

f) NATURAL JOIN: Automatically join on all columns with same names; eliminates duplicate columns.
   Potential drawback: unexpected joins if new common column names added later.

g) SELF-JOIN: Join table to itself using aliases. Useful for hierarchical relations (manager-employee).
   SELECT e.name AS employee, m.name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.emp_id;

3. Normalization vs De-normalization:

Normalization: Reduce data redundancy, improve data integrity.
* 1NF: Eliminate repeating groups; atomic values; unique rows.
* 2NF: In 1NF + no partial dependency (all non-key attributes depend on whole primary key).
* 3NF: In 2NF + no transitive dependency (non-key columns depend only on primary key).

Example normalization:
Unnormalized: Orders(order_id, customer_name, customer_address, product_name, product_price, quantity)
Normalized:
  Customers(customer_id, customer_name, customer_address)
  Products(product_id, product_name, product_price)
  Orders(order_id, customer_id, product_id, quantity, order_date)

De-normalization: Intentionally introduce redundancy for performance/simplification (fewer joins, faster reads).
  OrderDetails(order_id, customer_name, product_name, order_date, quantity, total_price)
  Trade-off: faster reads but update anomalies, more storage, consistency issues.

Normalization Summary:
* 1NF: Atomic values, no repeats -> one row per product in orders
* 2NF: Remove partial dependency -> separate Customers, Products, Orders tables
* 3NF: Remove transitive dependency -> customer_city in Customers, not Orders

4. MySQL vs PostgreSQL Key Differences:
* Standards Compliance: PostgreSQL more compliant with SQL standards; MySQL more lenient historically.
* Advanced SQL: PostgreSQL has window functions, full outer joins, CTEs, CUBE/ROLLUP, advanced data types.
* Data Types: PostgreSQL richer (arrays, enums, JSON/JSONB, hstore, UUID, composite types).
* Performance: PostgreSQL better for complex queries; MySQL may be faster for simple read-heavy workloads.
* MVCC: PostgreSQL's implementation avoids many locking problems; more robust concurrency.
* Extensions: PostgreSQL has strong extension system (PostGIS, etc.); MySQL has broad hosting support.
* Licensing: PostgreSQL is fully open source (PostgreSQL License); MySQL owned by Oracle, dual licensing.
* FULL OUTER JOIN: PostgreSQL supports natively; MySQL needs UNION workaround.
* JSON: PostgreSQL more robust (JSONB with indexing); MySQL less powerful.

JSONB (PostgreSQL):
* Stores JSON in binary format; supports indexes on JSON keys; faster querying (->, ->>, @>, etc.)
* CREATE TABLE products (id SERIAL PRIMARY KEY, details JSONB);
* INSERT INTO products (details) VALUES ('{name: Laptop, brand: Dell}');
* SELECT details->>'brand' AS brand FROM products;
* Supports GIN indexes for fast JSON searches.
