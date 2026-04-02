---
title: "GIL vs Multiprocessing vs Asyncio"
---

# GIL vs Multiprocessing vs Asyncio

## Global Interpreter Lock (GIL)
- **What it is:** A mutex in CPython that ensures only one thread executes Python bytecode at a time. Even on multi-core CPUs, only one thread runs at once (though OS may context-switch quickly).
- **Why GIL exists:** Makes memory management (reference counting) thread-safe. Simplifies implementation of CPython.
- **Impact:**
  - CPU-bound programs (math, ML loops) → GIL is a bottleneck.
  - I/O-bound programs (network, DB, file I/O) → threads can release GIL during blocking I/O, so threads are still useful.

## Multiprocessing
- **What it is:** Spawns multiple OS processes → each has its own Python interpreter and GIL. Allows true parallelism on multiple cores.
- **Use cases:** CPU-bound workloads: image processing, ML training, number crunching. Parallelizing heavy computation tasks.
- **Downsides:** Higher memory usage (each process has separate memory). Inter-process communication (IPC) is slower than threads (via queues/pipes).

## Asyncio
- **What it is:** A single-threaded event loop with async/await. Runs tasks concurrently via cooperative multitasking (tasks yield when waiting for I/O).
- **Use cases:** I/O-bound workloads: web servers, API calls, DB queries, websockets. Best when you have tens of thousands of concurrent I/O tasks.
- **Downsides:** Not useful for CPU-bound tasks (still one thread, blocked on heavy computation). Code is harder to debug (nested async).

## Interview Summary Table

| Feature | GIL (Threads) | Multiprocessing | Asyncio |
|---|---|---|---|
| Parallelism | ❌ (only 1 thread at a time) | ✅ (true parallelism) | ❌ (single-threaded) |
| Best for | I/O-bound (network/file ops) | CPU-bound (parallel compute) | I/O-bound (high concurrency) |
| Memory usage | Low (shared memory) | High (separate processes) | Low (single-threaded) |
| Ease of use | Medium | Medium/Hard (IPC needed) | Medium (async syntax) |
| Real-world use | Web servers with limited concurrency | Data processing, ML, ETL pipelines | High-scale APIs (FastAPI, aiohttp) |
