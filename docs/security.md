# AWS Security and IAM Configuration

## 1. Security Overview

The project uses AWS Security Groups and IAM roles to control network access and AWS permissions.

The intended traffic flow is:

Internet -> ALB -> EC2 Application -> RDS Database

## 2. Security Groups

### p1-alb-sg

Purpose: Controls incoming traffic to the Application Load Balancer.

Inbound rule:
- Protocol: TCP
- Port: 80
- Source: 0.0.0.0/0

### p1-app-sg

Purpose: Controls incoming traffic to EC2 application instances.

Inbound rule:
- Protocol: TCP
- Port: 80
- Source: p1-alb-sg

### p1-db-sg

Purpose: Controls incoming traffic to the database.

Inbound rule:
- Protocol: TCP
- Port: 3306
- Source: p1-app-sg

## 3. Security Group Design

The security groups establish the following access chain:

Internet
   |
   v
p1-alb-sg
   |
   v
p1-app-sg
   |
   v
p1-db-sg

This restricts application and database access instead of exposing every layer directly to the internet.

Default outbound rules were retained.

## 4. IAM Role

Role name: p1-ec2-role

Trusted entity:
- EC2

Attached AWS managed policies:

1. AmazonSSMManagedInstanceCore
   - Allows the EC2 instance to communicate with AWS Systems Manager services.

2. CloudWatchAgentServerPolicy
   - Provides permissions used by the CloudWatch Agent to publish monitoring data.

## 5. EC2 Security Configuration

The EC2 Launch Template uses:
- IAM role: p1-ec2-role
- Security Group: p1-app-sg
- IMDSv2: Required
- No SSH key pair configured

## 6. Security Best Practices

- Do not expose database port 3306 to the public internet.
- Do not allow unrestricted SSH access.
- Use IAM roles instead of storing AWS credentials on EC2.
- Require IMDSv2.
- Never upload passwords, private keys or access keys to GitHub.
- Keep database resources in private subnets.

## 7. Current Status

- ALB Security Group: Created
- Application Security Group: Created
- Database Security Group: Created
- EC2 IAM Role: Created
- IAM policies: Attached
- EC2 Launch Template security settings: Configured
- Actual EC2 and RDS deployment: Pending
