---
title: "Backpressure In Queues"
---

BackPressure in Queues

What is Backpressure?
Backpressure happens when a producer sends messages faster than a consumer can process them.
Without handling it, queues can overflow, systems slow down, or messages get dropped.

How Each System Handles Backpressure:

1. RabbitMQ
* Uses bounded queues: if queue fills up, applies flow control (producers may be blocked or slowed).
* Can use acknowledgments + prefetch count (consumer tells broker how many messages it can handle).
* Dead-letter queues (DLQs) handle messages that can't be processed after retries.
* Backpressure handled with prefetch limits and flow control.

2. Kafka
* Kafka does NOT block producers (designed for high-throughput writes).
* Messages written to disk (log segments) - essentially unbounded queue until retention policy kicks in.
* If consumers are too slow: lag builds up; old data may expire (data loss from consumer's perspective).
* Consumers must scale horizontally (more partitions, more consumers).
* Backpressure = consumer lag. Kafka shifts responsibility to consumers.

3. Redis (Pub/Sub or Streams)
* Redis Pub/Sub: no backpressure - if subscriber is slow, it MISSES messages.
* Redis Streams: messages stored until acknowledged, consumers fetch at own pace, but memory is bounded.
    * Use max length trimming to avoid unbounded growth.
    * Slow consumers risk falling behind and losing trimmed messages.
* Pub/Sub: no backpressure (fire-and-forget). Streams: bounded memory + trimming.

4. SQS
* Pull model: consumers poll at their own pace.
* Messages stay in queue until consumed (or expire - default 4 days, max 14).
* Backlog grows if consumers slow, but producers unaffected.
* AWS scales queue storage elastically - no immediate overflow.
* Backpressure absorbed by queue backlog, but too much lag risks hitting retention limits.

Quick Summary:
* RabbitMQ: Flow control + prefetch (slows producers)
* Kafka: Consumer lag builds up; producer unaffected
* Redis Pub/Sub: None (slow consumers miss data)
* Redis Streams: Memory bounded; slow consumers risk trimming
* SQS: Elastic backlog; risk of hitting retention limit
