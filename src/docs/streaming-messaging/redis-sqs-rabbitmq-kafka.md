---
title: "Redis Sqs Rabbitmq Kafka"
---

# Messaging System Comparison: Redis vs SQS vs RabbitMQ vs Kafka

## When to Use What

| System | Best For | Avoid When |
|--------|---------|------------|
| Redis PubSub | Fast broadcasts, presence | Need persistence |
| Redis Streams | light streaming with consumer groups | large scale |
| SQS Standard | Simple task queues, at-least-once | Ordering critical |
| SQSFIFO | Ordered processing | High throughput |
| RabbitMQ | Complex routing, acknowledgment | High throughput streaming |
| Kafka | Event log, replay, high throughput | Simple tasks |

## Redis PubSub

- **Model**: All subscribers receive every message
- **Persistence**: None - messages lost if no subscriber
- **Use case**: Live notifications, presence systems

```python
# Publish
redis.publish('channel', 'message')

# Subscribe
pubsub = redis.pubsub()
pubsub.subscribe('channel')
```

## SQS (AWS)

- **Model**: Pull-based, one consumer gets message
- **At-least-once**: Redelivery if not acked in visibility timeout
- **Use case**: Task queues, decoupling services

```python
# Send
sqs.send_message(QueueUrl='url', MessageBody='hello')

# Receive
mlgs = sqs.receive_message(QueueUrl='url', MaxNumberOfMessages=10)
```

## RabbitMQ

- **Model**: Protocol AMQP, exchanges + queues
- **Routing**: Direct, fanout, topic, headers
- **Ack**: Messages remain until acknowledged

```python
import pika

connection = pika.BlockingConnection()
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='hello')

# Publish
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
```

## Kafka

- **Model**: Log-based, append-only, partitioned topics
- **Retention**: Messages retained for configured period
- **Replay**: Consumers can read old messages

```python
from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('topic', b'hello')

consumer = KafkaConsumer('topic', group_id='my-group', bootstrap_servers='localhost:9092')
for msg in consumer:
    print(msg.value)
```

## Choice Guide

1. Simple task queue without ordering ? → SQS Standard
2. Ordered tasks, simple ? → SQSFIFO
3. Complex routing + acks ? → RabbitMQ
4. High throughput event stream + replay ? → Kafka
6. Fast in-memory broadcast ? → Redis PubSub
