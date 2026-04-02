---
title: "Kafka vs Kinesis Streams"
---

# Kafka vs Kinesis Streams

## Kafka (Apache Kafka / Amazon MSK)
- **What it is:** Distributed event streaming platform.
- **Core Concepts:**
  - **Producer** → sends messages to topics.
  - **Topic** → a named stream of records, split into partitions for scalability.
  - **Broker** → Kafka server that stores and serves data.
  - **Consumer** → reads messages from topics.
   - **Consumer Group** → multiple consumers working together to balance load.
- **Features:** High throughput, low latency messaging. Durability via replication across brokers. Retention (can replay old events). Ecosystem: Kafka Streams, Kafka Connect, Schema Registry.
- **Use Cases:** Real-time data pipelines. Event-driven microservices. Log aggregation (e.g., Kafka → OpenSearch). Streaming analytics (Kafka Streams/Flink).

## Kafka Interview Questions

**Q1. How would you design Kafka for a global, high-throughput system?**
- Multi-AZ cluster with replication factor 3.
- Enable rack awareness.
- Partition data by keys (e.g., customer_id).
- Use MirrorMaker 2.0 for cross-region replication.
- Integrate with Schema Registry to ensure producer/consumer compatibility.

**Q2. How do you handle consumer lag?**
- Scale consumer groups horizontally.
- Optimize poll/batch sizes.
- Backpressure handling (pause/resume consumption).
- Offload old data to S3 via Kafka Connect (tiered storage).

## AWS Kinesis Streams
- **What it is:** Fully managed event streaming service (AWS-native).
- **Core Concepts:**
  - **Stream** → ordered sequence of records.
  - **Shard** → base throughput unit (1 MB/s write, 2 MB/s read).
  - **Partition key** → controls record ordering (within a shard).
  - **Producers** → put data into the stream.
  - **Consumers** → read data (standard or enhanced fan-out).
- **Features:** Managed, serverless scaling. Multi-AZ durability. Integrates natively with AWS. Retention from 24 hours to 365 days.
- **Use Cases:** Real-time analytics (IoT, clickstream). ETL pipelines. Stream-to-search pipelines.

## Principal-Level Kafka Questions

**1. Highly available Kafka cluster?**
- 3+ brokers across multiple AZs.
- Zookeeper/KRaft mode for controller quorum.
- Replication factor ≥ 3.
- Rack-awareness, ISR, monitoring.

**2. Schema evolution in Kafka?**
- Schema Registry (Avro, Protobuf, JSON Schema).
- Enforce compatibility modes. Integrate into CI/CD.

**3. Kafka vs Kinesis?**
- Kafka: better control, lower latency, requires ops.
- Kinesis: fully managed, AWS-native, higher cost for large sustained throughput.
