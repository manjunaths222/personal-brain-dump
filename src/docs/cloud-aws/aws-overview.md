---
title: "Aws Overview"
---

AWS

Here's a detailed breakdown of the AWS Solutions Architect Professional (SAP-C02) interview topics.

1. AWS Architecture & Design
High Availability & Fault Tolerance
* Multi-AZ vs. Multi-Region:
    * Multi-AZ improves availability within a single region (e.g., RDS Multi-AZ).
    * Multi-Region ensures disaster recovery across geographically distant AWS regions (e.g., S3 Cross-Region Replication, DynamoDB Global Tables).
* Disaster Recovery Strategies:
    * Backup & Restore: Simple, periodic backups stored in S3/Glacier.
    * Pilot Light: Core components always running; rest activated in a disaster.
    * Warm Standby: A scaled-down live version that can scale up quickly.
    * Multi-Site (Active-Active): Full redundancy across regions.
* AWS Services for HA & DR: Elastic Load Balancer (ELB), Auto Scaling, Route 53 DNS failover.

Microservices & Serverless
* Serverless architecture with API Gateway + Lambda.
* Event-driven patterns using SNS, SQS, and EventBridge to decouple services.
* Service discovery with AWS Cloud Map & Route 53.
* App Mesh for managing service-to-service communication.

Networking & Security
* VPC Peering vs. Transit Gateway (Peering = 2 VPCs, TGW = multiple VPCs + on-prem)
* PrivateLink vs. NAT Gateway
* Security: IAM least privilege, AWS WAF, Shield, Firewall Manager, GuardDuty, Macie, Config

2. Cost Optimization
* Compute: Savings Plans, Reserved Instances (RIs), Spot Instances
* Storage: S3 Intelligent-Tiering, Glacier Deep Archive, EBS Snapshot Lifecycle
* Database: RDS Proxy, Aurora Serverless

3. Databases & Storage
* Relational: RDS (PostgreSQL, MySQL, SQL Server, Oracle), Aurora
* NoSQL: DynamoDB (Global Tables), Amazon Timestream
* Data Warehousing: Redshift for OLAP
* Storage: EBS (block, EC2), EFS (shared file, Linux), FSx (Windows/Lustre)

4. Disaster Recovery & Backup
* AWS Backup for automated snapshots
* Replication: S3 CRR, DynamoDB Streams, RDS Read Replicas
* Failover: Route 53 DNS failover, Auto Scaling with health checks

5. Migration Strategies (6 Rs)
* Rehost (Lift & Shift), Replatform (Lift & Tweak), Refactor, Repurchase, Retire, Retain
* Tools: AWS Migration Hub, DMS (Database Migration Service), SMS (Server Migration Service)

6. Security & Compliance
* GuardDuty: Threat detection
* Macie: S3 sensitive data scanning
* AWS Config: Tracks resource changes
* KMS for encryption key management, CloudHSM for dedicated HSM
* Shared Responsibility Model: AWS secures cloud infra; customer secures apps & data

7. Performance Optimization
* Compute: Graviton EC2, Auto Scaling
* Databases: Aurora Read Replicas, DAX (DynamoDB Accelerator), RDS Proxy
* Networking: Global Accelerator, CloudFront, Route 53 latency-based routing

8. Monitoring & Logging
* AWS X-Ray: Distributed tracing
* CloudWatch: Logs, Alarms, Metrics
* CloudTrail: API call logging for auditing

9. DevOps & CI/CD
* CodePipeline, CodeBuild, CodeDeploy
* IaC: CloudFormation, AWS CDK, Terraform
* Containers: ECS (Fargate vs EC2), EKS (managed Kubernetes)
* Deployments: Blue/Green, Canary using ALB & Lambda versions

10. Hybrid & Edge Computing
* AWS Outposts (on-prem AWS services), Local Zones
* Direct Connect vs. VPN: Dedicated vs. encrypted tunnels
* AWS Wavelength (5G ultra-low latency), Snowball/Snowmobile (large data migration)

EC2 Instance Families:
* General Purpose (T, M) - balanced workloads
* Compute Optimized (C) - HPC
* Memory Optimized (R, X, Z) - large in-memory apps
* Storage Optimized (I, D, H) - high IOPS
* GPU (P, G, F) - ML/FPGA
* Graviton (A, C, M, R) - cost-efficient ARM

Placement Groups: Cluster (low latency), Spread (failure isolation), Partition (large distributed apps)

Containers & Kubernetes:
* ECS - managed Docker orchestration
* EKS - managed Kubernetes
* Fargate - serverless containers
* App Runner - minimal config container deployment
* ECR - private Docker image registry

Lambda: Event-driven compute, Provisioned Concurrency (reduces cold starts), Layers, Step Functions orchestration

EventBridge vs SQS vs SNS:
* EventBridge - event-driven architectures
* SNS - Pub/Sub notifications
* SQS - Message queuing, decoupling

Machine Learning on AWS:
* SageMaker: Jupyter notebooks, training, deployment, Feature Store, Pipelines, Model Registry
* AI Services: Rekognition (images), Comprehend (NLP), Lex/Polly (chatbots/TTS), Textract (OCR)
* ML Compute: P4/G5 instances, Inferentia & Trainium chips
* Storage for ML: S3 (training data), DynamoDB/RDS (inference results), Glue & Data Wrangler (ETL)
* MLOps: SageMaker Pipelines, Step Functions, Model Registry
