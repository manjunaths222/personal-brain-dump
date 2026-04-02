---
title: "S3 Public Buckets"
---

Best Practices around S3 Public Buckets

How Public Access Can Be Granted on S3:
By default, S3 buckets and objects are PRIVATE. Public access can creep in through:
1. Bucket Policies - JSON-based rules allowing access to Principal:"*" (everyone).
2. Access Control Lists (ACLs) - Legacy mechanism (object- or bucket-level grants).
3. IAM Policies - If combined with bucket policies, can unintentionally open access.

Block Public Access (BPA):
AWS S3 Block Public Access = four switches that override ACLs and bucket policies.
Apply BPA at: Bucket level (per bucket) or Account level (all buckets in account).
The Four Settings:
1. BlockPublicAcls - Prevents adding new public ACLs, ignores existing ones.
2. IgnorePublicAcls - Ignores all public ACLs on the bucket/objects.
3. BlockPublicPolicy - Prevents creation of bucket policies granting public access.
4. RestrictPublicBuckets - Blocks access to buckets with public policies unless request comes from AWS service or account.
By default, when you create a new bucket -> all four are enabled (recommended).

Best Practice: Keep Buckets Private
* Enable all 4 BPA settings at ACCOUNT level.
* This guarantees no bucket can ever be made public accidentally.
* Manage access through IAM roles/policies or VPC endpoints, not via public access.

When You Actually Need Public Access (e.g., hosting static websites):
1. Disable/block public access only for that specific bucket (fine-tuned).
2. Instead of making bucket public, use Amazon CloudFront with Origin Access Control (OAC):
   * CloudFront fetches objects from your S3 bucket.
   * OAC ensures ONLY CloudFront can access the bucket.
   * End users access content through CloudFront (HTTPS, caching, security headers).
   * Bucket itself stays PRIVATE.
   This is the recommended approach for static websites and public content distribution.

Summary:
* Bucket Policy / ACL: Can allow public access if misconfigured
* Block Public Access (BPA): Override mechanism to stop public exposure
* Best Practice: Enable all 4 BPA settings account-wide
* For Public Websites: Use CloudFront + OAC instead of direct bucket public access

In short: Always block public access everywhere. For static sites -> use CloudFront in front with OAC, not direct S3 public access.
