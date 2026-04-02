---
title: "EC2 vs ECS vs EBS vs Serverless"
---

# EC2 vs ECS vs EBS vs Serverless

## Basics
- **EC2** → Raw VM instances.
- **Elastic Beanstalk** → PaaS that manages EC2 + scaling + deployment for you.
- **ECS (Elastic Container Service)** → Container orchestration (like Kubernetes).
- **Serverless (Lambda)** → Event-driven compute, pay-per-execution.

## Why Choose
- **EC2** → Full control, legacy workloads.
- **Beanstalk** → Simplified app deployment (for dev teams without ops).
- **ECS** → Containerized microservices.
- **Lambda** → Short-lived, event-driven tasks.

## When to Use
- **EC2** → Custom infra, stateful apps.
- **Beanstalk** → Rapid deployment of monoliths.
- **ECS** → Microservices, scalable APIs.
- **Lambda** → Event-driven tasks, automation, cost-optimized workloads.

## Interview Q&A
**Q: What are Lambda cold starts?**
Delay in starting a new container for function execution.

**Q: When not to use Lambda?**
For long-running, stateful processes, or workloads needing >15min execution.
