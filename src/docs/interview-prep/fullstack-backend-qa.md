---
title: "Fullstack Backend Qa"
---

Full Stack - Backend Interview Preparation: Exhaustive Topic List

1. Node.js (Runtime & Backend Engine)

Core Concepts:
- Node.js Architecture: Single-threaded, Event Loop, Libuv
- Event Loop Phases: timers, pending callbacks, idle, poll, check, close callbacks
- Synchronous vs Asynchronous execution
- Callback hell, Promises, Async/Await
- Error handling: try/catch, event emitters

Modules & NPM: CommonJS vs ESModules, npm scripts, semantic versioning, Monorepos (Lerna/Nx)

Express.js: Middleware chaining, RESTful routing, Error handling middleware, CORS, Custom headers

API Architecture:
- MVC / Clean / Hexagonal architecture
- Versioning: /api/v1/
- Request validation: Joi, zod, express-validator
- Centralized error handler

Authentication & Authorization:
- JWT (signing, verifying, expiration), OAuth2 & SSO
- RBAC middleware, Refresh tokens & session management

Database Integration:
- PostgreSQL/MySQL/MongoDB
- ORMs: Sequelize, Prisma, TypeORM, Mongoose
- Connection pooling, Transactions, Migrations

File Upload: multer, Sharp for compression, S3 signed URLs

Realtime: WebSockets (socket.io), EventEmitters, Message queues (RabbitMQ, Redis Pub/Sub)

Caching: node-cache, lru-cache, Redis, HTTP caching (ETags, Cache-Control)

Performance & Security: Rate limiting, Helmet middleware, Preventing XSS/CSRF/CORS, Clustering, Memory profiling

---

2. Next.js (Full-stack React Framework)

Core: Pages vs App Router, SSG, SSR, ISR, Client vs Server Components

Routing: Dynamic routes, Nested routing with layouts, Middleware (middleware.ts), Redirects/rewrites

Data Fetching: getStaticProps, getServerSideProps, App Router fetch/revalidate/cache, SWR/React Query

Authentication: NextAuth.js (providers, credentials, JWT), RBAC, Protected pages/API routes

Deployment: Vercel, Docker+AWS, Custom domains, CDN

Advanced: i18n, Image optimization, Custom server, SEO (Head, meta tags, OG images)

---

3. TypeScript

Type System: string, number, boolean, null, undefined, Arrays, Tuples, Enums, any, unknown, never, void

Advanced Types: Union, Intersection, Literal, Type Guards (typeof, in, instanceof), Discriminated unions

Interfaces vs Types: Extending, merging, readonly, optional, Index signatures

Generics: function identity<T>(arg: T): T { return arg; }
Bounded generics, constraints, Utility types with generics

Utility Types: Partial<T>, Required<T>, Pick<T>, Omit<T>, Record<K,T>, ReturnType<T>, Awaited<T>, Exclude<T>

---

4. AWS (Cloud Infrastructure)

Core Services: EC2, S3, Lambda, API Gateway, CloudFront, IAM

Backend Architectures:
- Serverless: API Gateway + Lambda + DynamoDB
- Containerized: Docker + ECS/EKS
- Monolith on EC2 vs microservices on Lambda

Databases: DynamoDB (NoSQL), RDS (PostgreSQL/MySQL), Aurora Serverless

CI/CD: CodePipeline + CodeBuild, GitHub Actions to AWS, CDK, Terraform

IaC: AWS CDK, Terraform, SAM

Security: IAM roles/policies, KMS, API Gateway authorizers

---

5. Testing

Types:
- Unit Tests: Jest, Vitest
- Integration: Supertest + Jest
- E2E: Cypress, Playwright
- Component: Testing Library, Jest DOM

Tools: jest.fn(), msw for HTTP mocking, supertest for Express, jest --coverage, Snapshot testing

Best Practices: Test pyramids, CI hooks, .test.ts/.spec.ts, test error conditions and edge cases

---

6. CI/CD Pipelines

Tools: GitHub Actions, GitLab CI/CD, CircleCI, Bitbucket Pipelines, Jenkins

CI Concepts: Lint → Test → Build → Deploy, Auto versioning, Secrets management

CD Concepts: Blue-green deployments, Canary deployments, Rollbacks, Infrastructure provisioning

GitHub Actions Example:
```yaml
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install && npm test && npm run build
```

DevOps: Docker (images, volumes, networks), Docker Compose, Kubernetes (pods, services, deployments), Helm charts

---

System Design Topics:
- RESTful API Design Best Practices
- GraphQL vs REST
- Rate Limiting, Throttling
- Caching Strategies (Client, CDN, Server)
- Stateless auth (JWT) vs Session
- Horizontal vs Vertical scaling
- Load Balancing (Nginx, AWS ALB)
- Message Queues (RabbitMQ, Kafka, SQS)
