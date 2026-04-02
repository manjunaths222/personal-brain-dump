---
title: "GENERAL - Interview Q&A"
---

# GENERAL - Interview Q&A

## 📌 Project-Specific

### Caramel (Serverless, Event-Driven)
**Q: How did you design the event-driven architecture with AWS Lambda, Step Functions, and SQS/SNS?**
A: I modeled each business workflow (e.g., vehicle onboarding, financing) as a state machine in Step Functions. Each step invoked a Lambda function that performed a small, isolated task. Events flowed through SQS for reliable queuing, ensuring retries and decoupling services. SNS handled pub-sub use cases where a single event needed to trigger multiple downstream systems. This gave us scalability (auto-scaling Lambdas), fault isolation, and modularity.

**Q: What were the biggest challenges in integrating 20+ third-party systems? How did you ensure reliability and fault-tolerance?**
A: The biggest challenge was varying SLAs, data formats, and failure modes. I addressed this by:
- Implementing adapter Lambdas for each integration (translation + retries).
- Adding circuit breakers and fallback logic for flaky APIs.
- Using DLQs (Dead Letter Queues) for failed events.
- Monitoring via CloudWatch + Datadog to catch anomalies early.
This made integrations resilient, observable, and recoverable without impacting the main workflow.

**Q: Why did you choose serverless over containerized solutions here?**
A: Caramel had bursty, unpredictable workloads (e.g., financing checks during business hours). Serverless was ideal since Lambda scales instantly and you only pay per use. Compared to ECS/EKS, serverless eliminated ops overhead and simplified scaling. For long-running tasks, Step Functions + Lambda chaining worked well.

### Hoag (Healthcare)
**Q: How did you handle HIPAA/PHI compliance in data exchange with Epic EHR?**
A: We ensured:
- Encryption in transit (TLS 1.2) and at rest (KMS for S3, RDS encryption).
- Tokenization/anonymization of PHI in logs.
- IAM role-based access control with least privilege.
- Audit logging for all data exchanges with Epic.
This satisfied HIPAA's security and auditability requirements.

**Q: How did you scale the system while ensuring low latency with third-party integrations like Stripe, Twilio, SendGrid?**
A: We decoupled synchronous vs async flows. For real-time needs (e.g., OTP via Twilio), APIs were kept lightweight with caching + retries. For non-critical tasks (e.g., sending receipts via SendGrid), we pushed events to SQS/Kinesis for async processing. This ensured low latency for user-facing flows while still scaling reliably.

### Pacify (Python + AWS ECS Fargate + Telehealth)
**Q: Can you walk me through the AWS architecture you designed? Why ECS Fargate instead of EKS or Lambda?**
A: I designed Pacify as:
- ECS Fargate services running Python Flask APIs.
- API Gateway + ALB as the entry point.
- Secrets Manager for credentials.
- CloudWatch + X-Ray for monitoring.
- Twilio + Zoom integrated for telehealth calls.
We picked ECS Fargate over Lambda since calls were long-running and stateful. EKS was overkill for our scale, while Fargate removed infra management overhead.

**Q: How did you handle real-time event processing with cron jobs + webhooks?**
A: For scheduled tasks, I used CloudWatch scheduled events to trigger Lambdas running cron jobs (e.g., nightly data sync). For webhooks (Zoom/Twilio/Healthie), I built Flask endpoints that validated signatures, then pushed events to SQS for async processing. This kept the system real-time, fault-tolerant, and loosely coupled.

### Clover (Reactive Java + Kubernetes)
**Q: Why did you use Reactive (WebFlux) vs traditional Spring MVC?**
A: Healthcare APIs required high concurrency and IO-bound operations (EHR lookups, Twilio calls). Spring MVC blocks a thread per request, while WebFlux uses reactive streams with event loops. This allowed us to serve 10x more concurrent users on the same hardware, reducing cost and improving responsiveness.

**Q: How did you ensure high availability in a containerized Kubernetes deployment?**
A:
- Multi-node, multi-AZ clusters for redundancy.
- Horizontal Pod Autoscaling (HPA) based on CPU/QPS.
- Rolling updates for zero downtime.
- Liveness/readiness probes to avoid routing traffic to unhealthy pods.
This gave us 99.9%+ availability with self-healing deployments.

## 📌 Cloud & Architecture

**Q: Design a scalable, low-latency system (ride-hailing / e-commerce).**
A:
- API Gateway ₒ Microservices behind ALB.
- Caching layer (Redis/Memcached) for hot data.
- Kafka/Kinesis for event streaming.
- Read-optimized DB (OpenSearch/Redis) + write DB (RDS/Postgres).
- Global load balancing (AWS Global Accelerator).
This ensures scalability, <100ms latency, and resilience.

**Q: Serverless vs Kubernetes?**
A:
- Serverless (Lambda) → best for bursty, unpredictable workloads, lightweight services, pay-per-use.
- Kubernetes → better for long-running services, predictable traffic, or multi-tenant SaaS.
I choose based on workload patterns, cost, and ops maturity.

**Q: How would you ensure resilience in an event-driven system?**
A:
- Retries + DLQs for failures.
- Idempotency keys for duplicate events.
- Circuit breakers & rate limiting for flaky services.
- Replay support in Kafka for recovery.

**Q: What patterns do you use for distributed transactions?**
A:
- Saga pattern (choreography / orchestration).
- Event sourcing for auditability.
- Two-phase commit only when absolutely needed (rare).

## 📌 Event Streaming

**Q: Kafka vs Kinesis vs SQS/SNS?**
A:
- Kafka → high-throughput, replay, ordering.
- Kinesis → AWS-native Kafka alternative, fully managed.
- SQS/SNS → simple queue/pub-sub, no replay.

**Q: Kafka streams → OpenSearch analytics?**
A:
- Kafka → Kafka Connect / Logstash → OpenSearch.
- Use consumer groups for scaling.
- Tune for exactly-once semantics if needed.

**Q: Strategies for replay, ordering, backpressure?**
A:
- Replay: store events, use offsets.
- Ordering: partition key design.
- Backpressure: reactive streams, throttling consumers.

## 📌 Infra as Code

**Q: Walk through a Terraform module you've written.**
A: I wrote a VPC module with subnets, NATs, IGWs. It used variables for CIDRs and exposed outputs (VPC ID, subnet IDs). Reused across environments via terraform workspaces.

**Q: Terraform vs CloudFormation?**
A: Terraform → multi-cloud, modular, better DX. CloudFormation → AWS-native, tighter integration. I prefer Terraform for large, multi-team projects.

**Q: Multi-account AWS IaC?**
A:
- Terraform workspaces or separate state files per account.
- Centralized modules.
- Cross-account IAM roles for shared services (logging, monitoring).

## 📌 TDD / BDD

**Q: TDD in microservices?**
A: Write unit tests for handlers, mock dependencies, use contract tests for APIs, then integration tests in CI.

**Q: BDD scenario (appointment booking)?**
A: Given patient selects doctor, When insurance verified, Then appointment is confirmed.

**Q: Challenges in async tests?**
A: Flaky timing issues, test ordering, mocking brokers. Solved via TestContainers + eventually assertions.

## 📌 AI/ML with LLMs

**Q: LLM chatbot (LangChain + Pinecone)?**
A: User query → embed with LangChain → Pinecone vector search → context + prompt → LLM → response. Cached results, sanitized inputs, monitored latency.

**Q: Integrate LLMs into microservices?**
A: Wrap LLM calls in a service API, expose via REST/GraphQL, add caching + fallback.

**Q: Challenges (latency, cost, security)?**
A:
- Latency → optimize vector search, batch requests.
- Cost → cache, use smaller models.
- Security → prompt injection guardrails.

## 📌 Python & System Design

**Q: GIL vs multiprocessing vs asyncio?**
A:
- GIL → one thread runs Python bytecode.
- Multiprocessing → CPU-bound tasks.
- Asyncio → IO-bound tasks.

**Q: Flask vs FastAPI vs Django?**
A:
- Flask → lightweight, simple.
- FastAPI → async, great perf, type hints.
- Django → batteries-included, heavy.

**Q: Optimizing Python in prod?**
A: Use async for IO, C extensions for CPU, profile with cProfile, optimize queries, add caching, tune GC.

## 📌 Docker & Kubernetes

**Q: Zero downtime in K8s?**
A: Rolling updates, blue-green deployments, readiness/liveness probes, service mesh for traffic shaping.

**Q: HPA vs cluster autoscaling?**
A:
- HPA → scales pods.
- Cluster autoscaling → adds/removes nodes.

**Q: Multi-tenant SaaS in K8s?**
A: Namespace isolation, resource quotas, network policies, per-tenant configs, RBAC.

## 📌 Leadership

**Q: Time you led a large-scale design?**
A: Caramel: designed serverless system, integrated 20+ APIs, mentored team, aligned with business, delivered high-scale backend.

**Q: Balancing priorities vs trade-offs?**
A: Be transparent with stakeholders, prioritize business value, but negotiate for null/tech debt in roadmap.

**Q: Mentoring teams in design reviews?**
A: Encourage discussion, ask "why" questions, propose alternatives, share best practices, and coach juniors to think trade-offs, not just implementation.
