---
title: "Mysql"
---

MySQL Tutorial Concepts

1. Getting Started: Open-source RDBMS; uses SQL for structured data. Sample classicmodels DB.

2. Querying Data (Basics):
* SELECT, ORDER BY, WHERE, Aliases (AS), DISTINCT, LIMIT/OFFSET
* Operators: =, <, >, <=, >=, <>, LIKE, IN, BETWEEN, IS NULL, AND/OR/NOT

3. Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN, Self-Join, USING vs ON
   WARNING: FULL OUTER JOIN not supported natively in MySQL; emulate using UNION of LEFT + RIGHT joins.

4. Grouping & Aggregates: GROUP BY, HAVING, COUNT/SUM/AVG/MIN/MAX, ROLLUP (subtotals/totals)

5. Subqueries: IN with Subquery, EXISTS, Correlated Subquery, Subquery in SELECT, Derived Tables (subquery in FROM)

6. DML: INSERT, INSERT IGNORE, REPLACE, UPDATE, DELETE, ON DUPLICATE KEY UPDATE (upserts)

7. DDL & Schema: CREATE TABLE, ALTER TABLE, DROP TABLE, TRUNCATE TABLE, SHOW/DESCRIBE, Temporary Tables, Indexes (PRIMARY, UNIQUE, FULLTEXT, SPATIAL)

8. Constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, DEFAULT, AUTO_INCREMENT, CHECK (MySQL 8.0+)

9. Views: CREATE VIEW, Updateable Views, WITH CHECK OPTION, DROP VIEW

10. Stored Procedures & Functions:
    DELIMITER //
    CREATE PROCEDURE GetOrders()
    BEGIN SELECT * FROM orders; END //
    DELIMITER ;
    IN/OUT Parameters; Stored Functions (return single value); Deterministic vs Non-deterministic.

11. Triggers & Events: BEFORE/AFTER triggers on INSERT/UPDATE/DELETE; Events for scheduled jobs.

12. Transactions: START TRANSACTION / COMMIT / ROLLBACK; SAVEPOINT; 
    Isolation Levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
    Uses InnoDB engine for ACID compliance.

13. Advanced Features:
* Prepared Statements (parameterized queries)
* Cursors (row-by-row iteration in procedures)
* Full-text Search
* JSON Support: JSON data type, JSON_EXTRACT, JSON_ARRAYAGG
* Window Functions (MySQL 8.0): ROW_NUMBER(), RANK(), etc.

14. Security & User Management: Users & Privileges, Roles, Authentication Plugins, SSL/encryption.

15. Import/Export: LOAD DATA INFILE, SELECT INTO OUTFILE, mysqldump.

16. Administration: SHOW DATABASES/TABLES, EXPLAIN (query execution plan), Performance Schema, Replication (master-slave), Partitioning.
