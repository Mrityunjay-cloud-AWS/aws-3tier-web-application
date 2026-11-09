
# Application Deployment Plan

## Deployment Architecture

The application will use three layers:

1. Public layer: Application Load Balancer.
2. Private application layer: EC2 instances managed by Auto Scaling.
3. Private database layer: Amazon RDS MySQL.

## Planned Deployment Sequence

1. Create NAT Gateway and configure private application subnet routing.
2. Launch EC2 instances through the Auto Scaling Group.
3. Verify EC2 connectivity and Nginx installation.
4. Create Amazon RDS MySQL.
5. Configure application-to-database connectivity.
6. Deploy the application code.
7. Create the Application Load Balancer.
8. Associate the ALB with the target group.
9. Verify target health and application accessibility.
10. Configure monitoring and alerts.
11. Complete testing and documentation.

## Access and Security

- ALB will be internet-facing.
- EC2 instances will remain in private subnets.
- RDS will remain private.
- Security Groups will restrict traffic between layers.
- Systems Manager Session Manager is planned for instance access.

## Cost Management

Billable resources will be created for a controlled testing period and removed after project validation.

## Current Status

Deployment preparation completed.
Actual application deployment pending.
