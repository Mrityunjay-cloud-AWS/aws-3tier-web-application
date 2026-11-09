
# EC2 Launch Template Configuration

## Overview

The EC2 Launch Template defines the configuration used to launch application instances.

## Configuration

- Launch Template: p1-app-template
- AMI: Amazon Linux 2023
- Instance Type: Small instance type selected during configuration
- Security Group: p1-app-sg
- IAM Role: p1-ec2-role
- Key Pair: None
- Metadata: IMDSv2 required

## User Data

The Launch Template includes a bootstrap script intended to:

1. Install Nginx.
2. Retrieve EC2 instance metadata using IMDSv2.
3. Display the instance ID and Availability Zone on the webpage.
4. Enable and start Nginx.

## Important

Nginx installation requires outbound access to the package repositories. Private instances will need suitable network connectivity, such as a NAT Gateway.

## Current Status

Launch Template created.
No EC2 instances have been launched yet.