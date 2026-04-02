---
title: "Event Driven Architecture"
---

# Event-Driven Architecture

## Core Concepts

- **Event**: A notification that something happened (immutable, past tense)
- **Event Producer**: Service that emits events
- **Event Consumer**: Service that reacts to events
- **Event Broker**: Kafka, SNS, EventBridge, etc.

## Patterns

### Event Notification

Just notify that something happened - no payload.

```json
{"event": "user.signedup", "userId": "123", "timestamp": "2024-01-01"}
```

### Event Carried State Transfer

Event contains full payload - consumer has everything needed.

```json
{
  "event": "order.placed",
  "orderId": "456",
  "items": [{"sku": "ABC", "qty": 2}],
  "total": 99.99
}
```

### Event Sourcing

Events are the primary record of state changes. Rebuild state by replaying events.

```python
events = [
  {"type": "AccountCreated", "balance": 0},
  {"type": "MoneyDeposited", "amount": 100},
  {"type": "MoneyWithdrawn", "amount": 30},
]

def rebuild_state(events):
    balance = 0
    for event in events:
        if event["type"] == "MoneyDeposited":
            balance += event["amount"]
        elif event["type"] == "MoneyWithdrawn":
            balance -= event["amount"]
    return balance
```

### CQRS (Command Query Responsibility Segregation)

Separate read and write models.

- **Command**: changes state (write)
- **Query**: reads state (read)

## Tradeoffs

| Pros | Cons |
|------|------|
| Loose coupling | Eventual consistency |
| Scalability | Harder to debug |
| Resilience (subscriber down) | Event schema management |
| Easy to add consumers | Out-of-order events |

## Vs Request-Response

- **Request-Response**: Synchronous, direct coupling, immediate feedback
- **Event-Driven**: Asynchronous, decoupled, eventual consistency
