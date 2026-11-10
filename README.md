# AWS Three-Tier Web Application

## Project Overview

This project demonstrates the design and deployment of a secure, highly available three-tier web application on Amazon Web Services (AWS).

The application uses Flask and MySQL and is deployed across multiple Availability Zones using private and public subnets, an Application Load Balancer, and an Auto Scaling Group.

## Architecture

The application follows a three-tier architecture:

1. **Presentation Layer:** Application Load Balancer deployed in public subnets.
2. **Application Layer:** EC2 instances running Flask, deployed in private application subnets and managed by an Auto Scaling Group.
3. **Database Layer:** Amazon RDS for MySQL deployed in private database subnets.

## AWS Services Used

| AWS Service | Purpose | Status |
|---|---|---|
| Amazon VPC | Isolated network | Completed |
| Subnets | Network segmentation | Completed |
| Internet Gateway | Public internet connectivity | Completed |
| NAT Gateway | Outbound internet access for private instances | Completed |
| Route Tables | Network routing | Completed |
| Security Groups | Network access control | Completed |
| IAM Role | EC2 permissions | Completed |
| EC2 Launch Template | Instance configuration | Completed |
| Auto Scaling Group | Instance management and scaling | Completed |
| Application Load Balancer | Traffic distribution | Completed |
| Target Group | Application health checks | Completed |
| Amazon RDS MySQL | Managed relational database | Completed |
| Flask Application | Web application | Deployed |
| Amazon CloudWatch | Monitoring and dashboards | Completed |
| CloudWatch Alarms | Resource alerts | Completed |
| Amazon SNS | Email notifications | Configured |

## Network Architecture

**VPC CIDR:** `10.0.0.0/16`

| Subnet | CIDR | Purpose |
|---|---|---|
| p1-public-a | 10.0.1.0/24 | Public |
| p1-public-b | 10.0.2.0/24 | Public |
| p1-app-a | 10.0.11.0/24 | Application |
| p1-app-b | 10.0.12.0/24 | Application |
| p1-db-a | 10.0.21.0/24 | Database |
| p1-db-b | 10.0.22.0/24 | Database |

## Application Technology

- Python
- Flask
- MySQL
- MySQL Connector
- Gunicorn
- Nginx

Application source code is stored in the `app/` directory.

## Security Design

- Application instances are deployed in private subnets.
- RDS is configured without public access.
- ALB accepts HTTP traffic through its security group.
- Application instances accept traffic from the ALB security group.
- Database access is restricted to the application security group.
- EC2 instances use an IAM role.
- IMDSv2 is required in the EC2 Launch Template.

## Load Balancing and Auto Scaling

- Application traffic is distributed through an Application Load Balancer.
- The target group performs application health checks.
- EC2 instances are managed by an Auto Scaling Group.
- Target tracking scaling uses average CPU utilization with a 50% target.
- Configured Auto Scaling capacity: Minimum 2, Desired 2, Maximum 4.

## Database

Amazon RDS for MySQL is used as the application's managed relational database.

The Flask application connects to RDS through the private network using database connection environment variables.

Database credentials are not stored in the GitHub repository.

## Monitoring and Alerting

Amazon CloudWatch is used to monitor:

- EC2 CPU utilization
- ALB healthy and unhealthy hosts
- ALB request count
- RDS CPU utilization
- RDS database connections
- RDS free storage

CloudWatch alarms are configured to send notifications through Amazon SNS.

## Application Validation

The deployed application was tested through the Application Load Balancer.

The following functionality was verified:

- Application accessibility through the ALB.
- Flask application running on EC2.
- Connectivity between EC2 and RDS.
- Employee record insertion into MySQL.
- Employee records displayed by the web application.

## Cost Management

AWS resources were deployed for project development and testing.

Billable resources should be stopped or deleted after evidence and documentation have been preserved.

## Repository Structure

```text
aws-3tier-web-application/
├── app/
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│   ├── static/
│   └── templates/
├── docs/
├── .gitignore
└── README.md
```

## Security Note

Never commit database passwords, AWS access keys, secret keys, or other sensitive credentials to GitHub.
