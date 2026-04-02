---
title: "Kafka Zookeepers vs KRaft"
---

# Kafka Zookeepers vs KRaft

Excellent question 🚀 — this goes to the heart of why Kafka moved away from ZooKeeper to KRaft. Let's break it down step by step.

## Problems with ZooKeeper in Kafka

### 1. Two systems to manage
- Kafka relied on ZooKeeper for cluster metadata.
- Operators had to install, secure, monitor, and scale ZooKeeper separately.
- This made deployment and upgrades more complex.

### 2. Split Brain Risk (Controller Election)
- In Kafka (with ZooKeeper), one broker is elected as the controller.
- If ZooKeeper lost sync or had a network partition, multiple controllers could be elected ("split brain").
- This caused instability: conflicting metadata changes, temporary inconsistencies.

### 3. Scalability Limits
- ZooKeeper isn't designed for high-throughput metadata writes.
- In large clusters (thousands of brokers, millions of partitions), ZooKeeper became a bottleneck.
- Example:
  - Adding partitions → ZooKeeper had to handle large amounts of write traffic.
  - Reassignments → huge metadata bursts overloaded ZooKeeper.

### 4. Complex State Synchronization
- Metadata was in ZooKeeper, but actual data was in Kafka brokers.
- Keeping both consistent was harder: brokers had to constantly sync metadata with ZooKeeper.
- Recovery after failures required extra coordination.

### 5. Limited Visibility
- ZooKeeper metadata was stored in znodes (hierarchical tree).
- Harder to query/debug at scale.

## How KRaft Solves These Problems

KRaft (Kafka Raft mode) replaces ZooKeeper with a built-in, Raft-based metadata quorum inside Kafka itself.

### 1. Single System, Simpler Ops
- No separate ZooKeeper cluster.
- Kafka manages both data and metadata.
- Deployment, monitoring, upgrades are easier.

### 2. Raft Consensus = No Split Brain
- KRaft uses the Raft consensus algorithm for metadata replication.
- Only one leader controller exists at a time, guaranteed by Raft's majority voting.
- Eliminates split brain and ensures strong consistency.

### 3. Better Scalability
- Metadata is stored in an internal Kafka topic (metadata log).
- Updates are written like normal Kafka messages → high-throughput, append-only log.
- KRaft handles millions of partitions more efficiently than ZooKeeper.

### 4. Unified Storage (No Dual Systems)
- Metadata and data both live in Kafka (brokers + controller quorum).
- Recovery is easier:
  - A broker only needs to replay the metadata log to catch up.
- No external ZooKeeper sync needed.

### 5. Stronger Fault Tolerance
- Metadata is replicated across KRaft controller nodes (3 or 5 recommended).
- On failure, Raft ensures safe leader re-election and no data loss.

### 6. Improved Observability
- Metadata log is just a Kafka topic → can be queried, monitored, audited.
- Easier debugging compared to ZooKeeper's znodes.

## Summary Table

| Problem in ZooKeeper | KRaft Solution |
|---|---|
| Separate cluster to manage | Metadata stored directly in Kafka (no external system) |
| Split-brain controller elections | Raft consensus ensures one true leader |
| Scalability bottleneck for large clusters | Metadata stored as Kafka log → scalable & efficient |
| Complex metadata–broker sync | Unified metadata + data in Kafka itself |
| Hard to debug metadata | Metadata log is queryable like any Kafka topic |

## Feature Comparison

| Feature | ZooKeeper Nodes | KRaft Nodes (Controllers) |
|---|---|---|
| Introduced in | Pre-Kafka 2.8 | Kafka 2.8+ (production-ready in 3.3+) |
| Dependency | External system (ZooKeeper) | Built into Kafka itself |
| Consensus Algo | Zab protocol | Raft consensus |
| Cluster metadata | Stored in ZooKeeper znodes | Stored in Kafka internal metadata log |
| Scalability | Limited (ZooKeeper bottleneck) | Scales better with large clusters |
| Ops Complexity | Higher (need to manage ZooKeeper) | Lower (single Kafka cluster) |
| State recovery | From ZooKeeper | From replicated metadata log |
