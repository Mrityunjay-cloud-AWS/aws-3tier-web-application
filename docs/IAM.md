# EC2 IAM Role Configuration

## IAM Role

Name: p1-ec2-role

Trusted Entity:
- AWS Service
- EC2

## Attached Policies

### 1. AmazonSSMManagedInstanceCore

Purpose:
Allows EC2 instances to communicate with AWS Systems Manager.

Benefits:
- Session Manager connectivity.
- Remote instance management.
- Centralized administration.
- SSH access is not required for Session Manager.

### 2. CloudWatchAgentServerPolicy

Purpose:
Allows the CloudWatch Agent running on EC2 to publish monitoring information.

Benefits:
- Memory monitoring.
- Disk monitoring.
- Application log collection.
- Additional system metrics.

## Security Design

- EC2 uses an IAM role instead of permanent access keys.
- Temporary credentials are provided through the EC2 Instance Metadata Service.
- IMDSv2 will be required for the instance.
- The role follows workload-based identity and access management principles.

## Architecture Decision

The application instances will run in private subnets.

Systems Manager will be used for administrative access instead of exposing SSH port 22 to the internet.