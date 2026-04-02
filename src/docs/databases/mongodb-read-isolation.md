---
title: "Mongodb Read Isolation"
---

# MongoDB Read Isolation & Concurrency Control

## Read Concerns

MongoDB read concern controls which version of data is returned:

- **local**: Read from primary (default) - may not be rollback safe
- **majority**: Read data acknowledged by majority of replica members
- **linearizable**: Strongest - read own writes, linearizable order
- **snapshot**: Transactional read isolation

```javascript
const result = await users.findOne(
  { _id: objectId },
  { readConcern: { level: "majority" }}
);
```

## Write Concerns

- **w=1**: Ack from primary only
- **w=majority**: Ack from majority of replicas
- **j=true**: Flush to journal before ack

```javascript
const result = await users.insertOne(
  { name: "John" },
  { writeConcern: { w: "majority", j: true } }
);
```

## Transactions (Multi-document)

MongoDB 4.0+ supports ACID transactions across multiple documents.

```javascript
const session = client.startSession();
try {
  session.startTransaction();
  await orders.insertOne({ order: "123" }, { session });
  await inventory.updateOne({ item: "pizza" }, { $inc: { qty: -1 } }, { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
} finally {
  await session.endSession();
}
```

## Concurrency Control

- **Optimistic Concurrency**: Use `version` field and check during update
- **Pessimistic Locking**: MongoDB doesn't have this natively

```javascript
// Optimistic - update only if version matches
const result = await users.updateOne(
  { _id: id, version: 1 },
  { $set: { name: "New Name" }, $inc: { version: 1 } }
);
if (result.modifiedCount === 0) {
  throw new Error("Conflict: record was modified");
}
```

## Causal Consistency

```javascript
// Use causal consistency sessions for read-after-write
const session = client.startSession({ causalConsistency: true });
```
