---
title: "Schema Evolution Cdc"
---

Q4 — SCHEMA EVOLUTION / MULTI-SOURCE ALIGNMENT

The Original Question:
Aggregate logs from multiple sources with missing/extra columns. Design a schema-evolution–friendly approach + PySpark code.

Why this matters:
Real pipelines consume API outputs, CSVs, Parquet, logs with evolving schemas.
Skills needed: schema evolution, dynamic alignment, safe union of DataFrames.

Sample Data:
Source A: ts, event, user_id
Source B: ts, event, user_id, device
Source C: ts, event

Strong Design: Extract all possible columns, add missing as NULL, union with deterministic column order.

Strong Code:
```python
from pyspark.sql.functions import lit
from functools import reduce
from pyspark.sql import DataFrame

dfs = [dfA, dfB, dfC]
all_cols = sorted(set().union(*[set(df.columns) for df in dfs]))

def align_schema(df, all_cols):
    for col in all_cols:
        if col not in df.columns:
            df = df.withColumn(col, lit(None))
    return df.select(all_cols)

aligned_dfs = [align_schema(df, all_cols) for df in dfs]
final_df = reduce(DataFrame.unionByName, aligned_dfs)
```

---

Q6 — CDC (INSERT/UPDATE/DELETE) WITHOUT DELTA LAKE

Design a CDC pipeline using PySpark without Delta Lake — only Hive.

Sample CDC Data:
id=1, op=U (Update), id=5, op=I (Insert), id=3, op=D (Delete)

Strong Design:
1. Use Hive ACID
2. Base table stored as ORC with transactional properties
3. Incoming data in staging table
4. Use MERGE INTO syntax
5. Ensure compaction is enabled

Strong Code:
```sql
CREATE TABLE employees (id int, name string, salary int)
CLUSTERED BY (id) INTO 10 BUCKETS
STORED AS ORC
TBLPROPERTIES ("transactional"="true");
```

```python
spark.sql("""
MERGE INTO employees t
USING staging s
ON t.id = s.id
WHEN MATCHED AND s.op = 'U' THEN UPDATE SET *
WHEN MATCHED AND s.op = 'D' THEN DELETE
WHEN NOT MATCHED AND s.op = 'I' THEN INSERT *
""")
```

---

Q7 — SMALL FILE PROBLEM (COMPACTION)

Problem: Thousands of small files in S3 hurt performance (too many tasks, high latency, slow jobs).

Strong Code:
```python
df = spark.read.parquet("s3://bucket/events/*")
df \
    .repartition(50) \
    .write \
    .mode("overwrite") \
    .parquet("s3://bucket/events_compacted/")
```

---

SQL Interview Questions

Deduplicate records with priority field (pick latest updated_at):
```sql
SELECT id, value, updated_at
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) AS rn
    FROM table1
)
WHERE rn = 1;
```

Running total (cumulative sum):
```sql
SELECT 
    date, amount,
    SUM(amount) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM sales;
```
