---
title: "REST vs GraphQL"
---

# REST vs GraphQL

## Basics

### REST (Representational State Transfer)
- An architectural style for building APIs.
- Uses HTTP methods (GET, POST, PUT, DELETE) to work with resources.
- Resources are identified by URLs (e.g., /users/123).
- Response format: usually JSON, sometimes XML.
- Stateless → each request contains all needed info (no server-side session).

Example:
```
GET /users/123
→ { "id": 123, "name": "Alice", "orders": [101, 102] }
```

### GraphQL
- A query language for APIs created by Facebook (2015).
- Clients define exactly what data they need in a single request.
- Uses a single endpoint (e.g., /graphql).
- Strongly typed schema (SDL: Schema Definition Language).
- Supports queries, mutations, and subscriptions (real-time).

Example:
```graphQL
query {
  user(id: 123) {
    name
    orders {
      id
      total
    }
  }
}
```
Response:
```json
{ 
  "data": { 
    "user": { 
      "name": "Alice", 
      "orders": [{ "id": 101, "total": 200 }] 
    } 
  } 
}
```

## Key Differences

| Feature | REST | GraphQL |
|---|---|---|
| Endpoints | Multiple endpoints per resource (/users, /orders) | Single endpoint (/graphql) |
| Data Fetching | Fixed responses → may cause over-fetching or under-fetching | Client specifies exactly what it needs |
| Versioning | Requires versioning (/v1/users, /v2/users) | No versioning, schema evolves via deprecation |
| Flexibility | Rigid, server decides response format | Flexible, client decides |
| Real-time | Needs WebSockets, SSE, or polling | Native via subscriptions |
| Performance | Can be more efficient for simple requests | Can be expensive on server for complex nested queries |
| Caching | Easy with HTTP (CDNs, RESTful caching) | Harder, needs custom caching (Apollo, Relay) |
| Learning Curve | Easier (HTTP basics) | Steeper (schemas, resolvers, tooling) |

## When to Use

**✅ Use REST when:**
- Your API is simple, with well-defined resources.
- You want easy caching via HTTP/CDNs.
- Your client apps don't need high flexibility.
- You want lower server complexity.
- Example: Blog APIs, CMS APIs, microservices APIs.

**✅ Use GraphQL when:**
- You have multiple clients (web, mobile, IoT) needing different data.
- You want to reduce round-trips (fetch related data in one request).
- Your API evolves rapidly (avoid versioning overhead).
- You need real-time updates (subscriptions).
- Example: SaaS dashboards, social media feeds, e-commerce apps.

## Interview Q&A

**Q1. What problem does GraphQL solve that REST cannot?**
GraphQL solves over-fetching and under-fetching issues. REST endpoints return fixed responses, while GraphQL lets clients request exactly the fields they need.

**Q2. What are downsides of GraphQL compared to REST?**
Harder caching, more complex backend implementation, potential for expensive nested queries (N+1 problem), and a steeper learning curve. REST is simpler for small APIs.

**Q3. If you're designing a mobile app API, would you choose REST or GraphQL? Why?**
Likely GraphQL, because mobile apps often need custom, optimized responses to save bandwidth and reduce multiple API calls. But if the API is small and stable, REST might be enough.

**Q4. How do you handle performance issues in GraphQL?**
Techniques include:
- Query depth limiting (avoid very deep nested queries).
- Caching (Apollo, DataLoader for batching).
- Persisted queries.
- Rate limiting.

## Quick Summary
- **REST** → Simpler, cache-friendly, resource-based.
- **GraphQL** → Flexible, efficient data fetching, better for modern multi-client apps.
