---
title: "Docker vs Kubernetes"
---

# Docker vs Kubernetes

## 🐳 Docker

### High-level basics
Docker is a containerization platform. It packages your application and all its dependencies (libraries, runtime, system tools) into a container. This ensures the app runs the same everywhere—on a developer's laptop, test servers, or production. Unlike virtual machines, containers don't include an entire OS, making them lightweight and fast to start.

Key components:
- **Docker Engine** – runtime that runs containers
- **Dockerfile** – instructions to build container images
- **Docker Image** – a read-only template (like a snapshot of your app + environment)
- **Docker Container** – a running instance of the image

### Conceptual understanding
The real strength of Docker lies in solving the "works on my machine" problem. With containers, you standardize environments. For example, a Python app needing version 3.11 with specific libraries will always work regardless of the host system.

Docker also improves CI/CD pipelines. You can build once (image), test it, and deploy the same artifact to staging and production. This reduces deployment drift. Additionally, Docker supports isolation—each container runs independently, so different apps can coexist on the same server without dependency conflicts.

### Interview must-know topics
- Difference between containers vs virtual machines
- Dockerfile basics (FROM, RUN, COPY, CMD, ENTRYPOINT)
- What is a multi-stage build and why it's used (smaller images)
- Docker Networking (bridge, host, overlay)
- Volumes (persistent storage) vs container's ephemeral storage
- Best practices – small images, non-root user, health checks, security scanning

## ☸️ Kubernetes

### High-level basics
Kubernetes (K8s) is an open-source container orchestration platform. While Docker helps you create and run individual containers, Kubernetes helps you manage containers at scale across multiple servers. It handles deployment, scaling, networking, load balancing, and recovery of containers automatically.

Key components:
- **Pod** – smallest deployable unit, 1+ containers working together
- **Node** – a worker machine that runs pods
- **Cluster** – a set of nodes managed by Kubernetes
- **Control Plane** – brain of K8s (API Server, Scheduler, Controller Manager, etc.)
- **kubectl** – CLI tool to interact with the cluster

### Conceptual understanding
Kubernetes abstracts infrastructure into desired state management. Instead of manually starting containers, you declare (via YAML manifests) what you want:
- "I need 5 replicas of my web service"
- "This app should auto-scale if CPU > 70%"
- "Expose this service via a load balancer"

K8s ensures the actual cluster state matches your desired state—if a pod crashes, Kubernetes restarts it automatically.

K8s also enables service discovery & networking (Services, Ingress), config management (ConfigMaps, Secrets), and observability (logging, metrics). This makes it the industry standard for microservices architecture.

### Interview must-know topics
- Difference between Docker vs Kubernetes (complementary, not competing)
- Kubernetes Objects: Pod, Deployment, Service, Ingress, ConfigMap, Secret, Namespace
- Horizontal Pod Autoscaler (HPA) – scaling based on metrics
- StatefulSets vs Deployments (stateful apps vs stateless apps)
- DaemonSets (e.g., logging agents on all nodes)
- Networking: ClusterIP, NodePort, LoadBalancer
- Storage: Persistent Volumes (PV) and Persistent Volume Claims (PVC)
- Observability: how to debug with `kubectl logs`, `kubectl describe`, etc.
- Helm charts (package manager for K8s)
