
# EC2 Auto Scaling Configuration

## Overview

The Auto Scaling Group manages the desired number of EC2 application instances.

## Configuration

- ASG Name: p1-app-asg
- Launch Template: p1-app-template
- Application Subnets: p1-app-a, p1-app-b
- Target Group: p1-app-tg
- Minimum Capacity: 0
- Desired Capacity: 0
- Maximum Capacity: 4

## Planned Deployment Configuration

During the final deployment:

- Minimum Capacity: 2
- Desired Capacity: 2
- Maximum Capacity: 4

## Scaling Policy

Target tracking scaling is planned with an average CPU utilization target of 50%.

## Health Checks

EC2 and Elastic Load Balancing health checks are intended to support unhealthy instance replacement.

## Current Status

Auto Scaling Group created.
No EC2 instances launched.
Scaling policy configuration pending.
