
# Cloud Security Incident Response Runbook

## 1. Incident Overview

Incident Name: Public S3 Bucket Exposure

Severity: HIGH

Description:
A cloud storage bucket may have been configured to allow
unauthorized public access. This can expose sensitive data.

## 2. Detection

- Monitor AWS API activity using Amazon EventBridge.
- Detect suspicious events such as PutBucketPolicy and PutBucketAcl.
- AWS Lambda processes matching security events.
- Amazon SNS sends security alerts.

## 3. Analysis

- Identify the affected S3 bucket.
- Review CloudTrail event details.
- Identify the user or role responsible.
- Check whether public access was enabled.
- Determine whether unauthorized access occurred.

## 4. Containment

- Run the S3 remediation Lambda function.
- Enable all four S3 Block Public Access settings.
- Restrict access to the affected bucket.
- Notify the security administrator.

## 5. Eradication

- Review and remove unauthorized bucket policies.
- Review bucket ACL permissions.
- Rotate exposed credentials if required.
- Check for other affected cloud resources.

## 6. Recovery

- Verify that public access is blocked.
- Restore only approved bucket permissions.
- Check application and storage functionality.
- Monitor the bucket for suspicious activity.

## 7. Manual Intervention

If automated remediation fails:

1. Notify the cloud administrator.
2. Open the AWS S3 console.
3. Select the affected bucket.
4. Open Permissions.
5. Enable all Block Public Access settings.
6. Review bucket policies and ACLs.
7. Record the actions taken.

## 8. NIST Incident Response Lifecycle

Preparation:
Create monitoring rules, Lambda functions and response procedures.

Detection and Analysis:
Identify suspicious API activity and investigate the incident.

Containment, Eradication and Recovery:
Block public access, remove unauthorized permissions
and restore secure operations.

Post-Incident Activity:
Document findings, review logs and improve security controls.

## 9. Prevention

- Keep S3 Block Public Access enabled.
- Follow least-privilege IAM permissions.
- Monitor AWS API activity.
- Review security configurations regularly.
- Test incident response procedures.
