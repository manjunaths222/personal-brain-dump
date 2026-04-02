---
title: "Terraform Vs Cloudformation"
---

Terraform vs CloudFormation

Conceptual / Comparison:
1. Key Differences:
   * CloudFormation: AWS-native IaC, tightly integrated with AWS, strong drift detection and auto-rollback.
   * Terraform: Cloud-agnostic, supports multiple providers (AWS, GCP, Azure, Kubernetes, SaaS), rich module ecosystem.
   * Terraform = declarative + state-driven; CloudFormation = declarative but AWS-only.
   * Use Terraform for multi-cloud; CloudFormation for AWS-only compliance-driven environments.

2. Terraform State Management:
   * Remote backends: S3 + DynamoDB lock for AWS, or Terraform Cloud/Enterprise.
   * Enforce state locking to avoid race conditions.
   * Sensitive data: encryption at rest (SSE-S3/KMS) and at transit (TLS).
   * Drift detection: run `terraform plan` in CI/CD regularly.

3. Drift Detection:
   * Terraform: detects during `terraform plan` (state file vs actual infra). No auto-correction unless applied.
   * CloudFormation: built-in Drift Detection API. Highlights drifted resources; correction is manual.

4. Pros/Cons:
   * CloudFormation Pros: AWS-native, IAM integration, rollback on failure, managed by AWS (no state mgmt).
   * CloudFormation Cons: AWS-only, slower deployment, less modular.
   * Terraform Pros: Multi-cloug, huge provider ecosystem, modular, faster execution.
   * Terraform Cons: State management overhead, fewer enterprise guardrails (unless using Cloud/Enterprise).

Architecture & Best Practices:
5. Large Org Structure: Modular architecture; separate workspaces/states per env; remote state with locking; naming conventions + tagging; policy as code (OPA/Conftest, Sentinel).
   Folder structure: /environments/{prod,dev}/main.tf + /modules/{network,compute}/

6. CI/CD:
   * Terraform: Lint -> Validate -> Plan -> Apply -> Post-apply verification; state in S3+DynamoDB; GitHub Actions/GitLab CI/CodePipeline.
   * CloudFormation: validate-template -> package -> deploy; Change Sets for preview.
   * Manual approvals for prod; automated tests (Terratest, TaskCat).

7. Secrets Management: Never hardcode.
   * Terraform: AWS Secrets Manager, SSM Parameter Store, Vault. Use `sensitive = true`.
   * CloudFormation: Dynamic References. Password: {{resolve:secretsmanager:mysecret:SecretString:password}}

8. Avoiding resource recreation:
   * Idempotent modules in terraform; `lifecycle { prevent_destroy = true }` in Terraform.
   * `ignore_changes` in Terraform or `UpdatePolicy` in CloudFormation for mutable fields.
   * `create_before_destroy` when replacement is unavoidable.

Advanced / Governance:
9. Governance: Terraform Sentinel (Enterprise) or OPA/Conftest; CloudFormation Service Catalog with pre-approved templates; Checkov, tfsec, cfn-nag in CI/CD.
10. Migrating 500+ CFN stacks to Terraform: `terraform import`; Terraformer tool; parallel strategy (CFN for legacy, Terraform for new).
11. Multi-team IaC: Internal module registry; GitOps workflows; namespacing, tagging, account separation (AWS Organizations).
12. Failed CFN stack: Investigate via `describe-stack-events`; use automatic rollback or disable for debugging; Change Sets next time.

Practical Examples:
Terraform S3 bucket:
  resource "aws_s3_bucket" "example" {
    bucket = "my-bucket-${var.env}"
    tags = { Environment = var.env, Owner = "PlatformTeam" }
  }

CloudFormation S3 bucket:
  Resources:
    MyS3Bucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: !Sub "my-bucket-${Environment}"
