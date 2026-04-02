---
title: "Acid Base Cap"
---

BASE vs CAP vs ACID

1. ACID (Traditional Databases like SQL)
ACID defines how transactions behave to guarantee reliability.
* A - Atomicity: All operations in a transaction succeed or none do.
* C - Consistency: The database moves from one valid state to another valid state.
* I - Isolation: Concurrent transactions don't interfere.
* D - Durability: Once committed, data is safe (even after crash/power loss).
Ensures correctness, but adds overhead. Mostly used by SQL databases.

2. BASE (Typical NoSQL Systems)
BASE relaxes strict rules to gain scalability & availability.
* B - Basically Available: The system guarantees availability (responds even if some data not consistent yet).
* S - Soft state: Data may change over time even without input (replicas sync asynchronously).
* E - Eventually consistent: If no new updates happen, all replicas will converge to the same state.
Ensures performance and scale, but tolerates temporary inconsistency. Used by Cassandra, DynamoDB, MongoDB (AP mode).

3. CAP Theorem (Distributed Databases)
In a distributed database, you can only guarantee two of three:
* C - Consistency: All nodes return the same data at the same time.
* A - Availability: Every request gets a response, even if some nodes are down.
* P - Partition tolerance: System continues working even if communication between nodes breaks.
Trade-off:
* CP (Consistency + Partition tolerance): sacrifices Availability (e.g., MongoDB, HBase)
* AP (Availability + Partition tolerance): sacrifices Consistency (e.g., Cassandra, DynamoDB)
* CA: only possible in single-node systems

Putting It All Together
* ACID vs BASE: How individual transactions behave.
* CAP: How a distributed system behaves during network partitions.
* SQL -> ACID, often CP in distributed setups.
* NoSQL -> BASE, often AP in distributed setups.

Examples:
* Banking app (SQL + ACID + CP): partition may reject writes on one side but balances stay consistent.
* Social media feed (NoSQL + BASE + AP): partition still serves posts (high availability), but you might see old likes until replicas sync.

Summary:
* ACID: Transaction guarantees (correctness, safety)
* BASE: Practical approach for scale (speed, flexibility)
* CAP: Fundamental trade-off in distributed systems (pick 2 of 3)
