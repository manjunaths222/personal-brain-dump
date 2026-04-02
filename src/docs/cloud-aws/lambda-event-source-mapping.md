---
title: "Lambda Event Source Mapping"
---

Event Source Mapping vs Long Polling vs Batching vs Grouping

1. Event Source Mapping (ESM)
A Lambda feature that connects a poll-based event source (SQS, Kinesis, DynamoDB Streams, Kafka, MQ) to your function.
AWS runs a poller in the background, fetches events, and invokes your function.
Handles: Polling, Batching (grouping multiple records into one Lambda invocation), Retries + checkpoints, Deleting messages (SQS only, on success)
When to use: Connect SQS/DynamoDB Streams/Kinesis to Lambda without managing polling yourself. Serverless automatic scaling (AWS handles concurrency, retries, backoff).

2. Long Polling (SQS feature)
SQS concept, not Lambda-specific. ReceiveMessage can wait up to 20 seconds for new messages.
Reduces empty responses -> saves cost.
In Lambda + SQS: ESM automatically uses long polling behind the scenes.
When to use: Building own consumer (EC2, container, on-prem) to avoid wasting API calls on empty queues. Sporadic/low frequency messages.

3. Batch Polling
Fetching multiple messages in a single poll request.
* SQS: MaxNumberOfMessages (up to 10)
* Lambda ESM: BatchSize (up to 10 for SQS FIFO/Standard, 10,000 for Kinesis/DynamoDB Streams)
If BatchSize=5, Lambda polls SQS and invokes function with up to 5 messages at once.
Improves throughput, reduces cost (fewer invocations).
WARNING: One bad message can fail the whole batch unless you use partial batch response.
When to use: High-throughput scenarios; messages processed independently; want to reduce cost.

4. Grouping (Message Grouping) - FIFO queues only
Messages with the same MessageGroupId processed in order, one group at a time.
Strict ordering within a group; parallelism across groups.
Example: Group A messages -> sequential; Group B messages -> parallel to Group A.
When to use: Business logic requires strict ordering (payments, stock trades, workflow steps).

How They Fit Together:
* Event Source Mapping: Lambda integration -> controls polling, batching, retries, deletes
* Long Polling: SQS feature -> how long a poll waits for messages (up to 20s)
* Batch Polling: SQS/ESM feature -> how many messages in one batch (batchSize=10)
* Grouping: SQS FIFO feature -> ordering guarantees per MessageGroupId

Example: SQS FIFO + Lambda
* FIFO queue with MessageGroupId=Customer123, batchSize=5, maximumBatchingWindow=10
* ESM long polls queue -> fetches up to 5 messages -> all Customer123 group -> invoked in order -> on success, ESM deletes them.

In short:
* ESM = automatic poller -> Lambda
* Long polling = wait for messages (reduce empty polls)
* Batch polling = multiple messages per invocation
* Grouping = ordering guarantee in FIFO queues
