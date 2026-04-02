---
title: "From list"
---

PySpark

Introduction: Python API for Apache Spark — big data processing and distributed computing.
Why: Handles massive datasets, distributed computing, ETL pipelines, ML, integrates with Hadoop/Hive/HDFS.

Core Concepts:
- SparkSession: entry point for PySpark applications
- RDD (Resilient Distributed Dataset): low-level distributed data structure
- DataFrame: high-level API for structured data (similar to pandas)
- SparkContext: manages connections to the Spark cluster

Creating SparkSession:
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("PySpark Example").getOrCreate()
```

Creating DataFrames:
```python
# From list
df = spark.createDataFrame([("Alice", 30), ("Bob", 25)], ["Name", "Age"])
# From CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)
# From Parquet (recommended for big data)
df = spark.read.parquet("data.parquet")
```

Data Exploration: .show(), .printSchema(), .columns, .describe()

Data Cleaning:
```python
df.fillna(0)          # fill missing values
df.dropna()           # drop rows with NaN
df.dropDuplicates()
df = df.withColumn("Age", col("Age").cast("Integer"))
```

Data Transformation:
```python
df = df.withColumn("Country", lit("USA"))
filtered_df = df.filter(df['Age'] > 30)
df.sort("Age", ascending=False)
```

Grouping & Aggregation:
```python
df.groupBy("Country").agg(F.avg("Age").alias("Avg_Age")).show()
```

Joins: inner, left, right — same as SQL
```python
df1.join(df2, "ID", "inner").show()
```

PySpark SQL:
```python
df.createOrReplaceTempView("people")
spark.sql("SELECT Name, Age FROM people WHERE Age > 30").show()
```

Writing Data:
- df.write.csv("output.csv", header=True)
- df.write.parquet("output.parquet")  # recommended for large data
- df.write.json("output.json")

PySpark ML (MLlib):
```python
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
data = assembler.transform(df)
model = LinearRegression(featuresCol="features", labelCol="target").fit(data)
predictions = model.transform(data)
```

Performance Optimization:
- Use .select() instead of * for column selection
- Use .cache() for repeated data access
- Use .repartition() to improve parallelism
- Avoid unnecessary .count() (expensive operation)

Real-World ETL Pipeline:
```python
sales_df = spark.read.csv("sales.csv", header=True, inferSchema=True)
sales_df = sales_df.dropna()
sales_df = sales_df.withColumn("Total_Sales", col("Quantity") * col("Price"))
summary_df = sales_df.groupBy("Region").agg(sum("Total_Sales").alias("Total_Sales"))
summary_df.write.csv("sales_summary.csv", header=True)
```
