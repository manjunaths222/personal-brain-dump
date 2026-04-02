---
title: "Multi Format Ingestion"
---

Multi-format ingestion strategy (JSON, Avro, Parquet, CSV)

Q: Your platform ingests data from multiple sources: CSV logs, Nested JSON from microservices, Avro events from Kafka, Parquet from internal data pipelines. How would you design a unified ingestion layer that handles all formats efficiently?

Good Answer:
* Use schema detection + schema registry for strongly typed formats (Avro, Parquet).
* CSV → enforce column mapping + header validation.
* JSON → use Spark schema inference only during dev, not prod; define schema manually.
* Batch ingestion via: Auto-loader (Databricks) OR Cloud storage notifications → Spark jobs
* Introduce a Bronze layer storing raw source as-is.
* Create separate ingestion processors for each format but standardize output metadata (_ingest_time, _source, _schema_version).
* Use incremental ingestion using watermarking or file-based checkpoints.

---

Handling schema evolution in JSON & Avro

Q: Your JSON data adds new fields every week. How will your ingestion pipeline handle schema evolution without breaking?

Answer:
* Use Avro/Confluent Schema Registry for events.
* Maintain versioned schemas in code + catalog.
* For JSON: Use PERMISSIVE mode in Spark, maintain "expected schema", add new fields as nullable, create schema evolution alerts
* Store raw JSON in Bronze, normalize only into Silver/Gold
* Avoid DROP operations.

---

Scaling to millions of events per minute

Q: How would you design ingestion pipelines to scale to millions of events per minute?

Answer:
* Use Kafka for real-time ingestion.
* Partition topics by user_id % partitions or geo.
* Use Spark streaming or Flink for transformation.
* Video assets → S3/GCS → metadata → pipeline.
* Use asynchronous ingestion + backpressure handling.
* Maintain Bronze/Silver/Gold layers.
* Use compaction to manage small files.

---

Data quality checks at ingestion time

Q: What data quality checks will you implement at ingestion time?

Answer:
* Schema validation
* Duplicate detection (hash, primary key)
* Null-checks on required fields
* Value constraints (e.g., age > 0, amount > 0)
* Outlier detection (e.g., suspicious user activity)
* Referential integrity checks
Tools: Great Expectations, Deequ, Databricks expectations.
