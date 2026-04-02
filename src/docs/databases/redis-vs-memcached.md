---
title: "Redis vs Memcached"
---

# Redis vs Memcached

## 1. Redis
- **Nature:** In-memory data structure store, often used as cache, DB, and message broker. Supports persistence (RDB snapshots, AOF logs).
- **Key Features:** Rich data types (strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, geospatial), Pub/Sub messaging, Lua scripting, Transactions & pipelines, clustering + replication, persistence to disk.
- **Pros:** Very flexible (not just a cache). Persistence → can survive restarts. Strong ecosystem (Redis Streams, RedisJSON, RedisSearch). Good for leaderboards, queues, counters, rate-limiting.
- **Cons:** More memory-heavy than Memcached. Single-threaded (though now supports multi-threaded I/O in newer versions). Slightly more complex to operate at large scale.
- **Best for:** Caching + advanced scenarios (real-time analytics, pub/sub, rate-limiting, session store). When you need persistence + durability. When you need data structures beyond strings.

## 2. Memcached
- **Nature:** High-performance distributed memory cache system. Simple: only key-value (string → string).
- **Key Features:** In-memory, ephemeral (no persistence). Super lightweight. Multi-threaded → can utilize multiple CPU cores. Optimized for speed.
- **Pros:** Very fast for simple caching. Lightweight and simple to operate. Scales horizontally easily with client-side sharding. Lower memory overhead vs Redis (uses slab allocation).
- **Cons:** No persistence (data lost on restart). No complex data structures. Limited feature set compared to Redis.
- **Best for:** Simple key-value cache (caching HTML fragments, DB query results). When you don't need persistence or advanced features. Very high-throughput cache where simplicity is enough.

## Comparison Table

| Feature | Redis | Memcached |
|---|---|---|
| Data Types | Strings, lists, sets, sorted sets, hashes, bitmaps, streams, geo | Strings only |
| Persistence | Yes (RDB, AOF) | No |
| Memory Efficiency | Higher overhead (extra metadata) | More memory efficient for pure caching |
| Multi-threading | Single-threaded (multi-threaded I/O in newer versions) | Multi-threaded (better CPU usage) |
| Scaling | Replication + clustering | Horizontal scaling with client sharding |
| Pub/Sub | Yes | No |
| Advanced Features | Transactions, Lua scripting, streams, modules | None |
| Best Use Cases | Caching + queues, pub/sub, leaderboards, rate-limiting | Pure caching (lightweight, simple) |

## Interview Q&A

**Q1. When would you choose Memcached over Redis?**
If you just need a lightweight, blazing-fast key-value cache without persistence, data structures, or pub/sub. Example: caching rendered HTML fragments for a website.

**Q2. When would you choose Redis over Memcached?**
If you need advanced data structures, durability, or features like pub/sub, queues, counters, leaderboards, rate limiting. Example: using Redis Sorted Sets for a real-time leaderboard in a gaming app.

**Q3. Which one is faster?**
For simple key-value caching, Memcached is slightly faster and more memory efficient. But Redis offers more versatility with a small tradeoff in speed.

**Q4. Can Redis fully replace Memcached?**
Yes, in most modern systems Redis is chosen because it's a superset of Memcached's functionality. But Memcached is still used for very simple, high-throughput caching because of its simplicity and lower overhead.

## Quick Mental Model
- **Memcached** → Fast, simple, ephemeral cache (stateless).
- **Redis** → Rich data structures + persistence + more features (stateful).
