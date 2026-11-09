
# Amazon RDS Database Configuration

## Overview

Amazon RDS MySQL will provide the database layer for the three-tier application.

## Prepared Configuration

- Planned Database Engine: MySQL
- Planned DB Identifier: p1-mysql-db
- Planned Database Name: employees
- DB Subnet Group: p1-db-subnet-group
- Database Security Group: p1-db-sg
- Public Access: No
- Deployment: Single-AZ initially to control lab costs

## Database Networking

The database will be deployed in private database subnets:

- p1-db-a: 10.0.21.0/24
- p1-db-b: 10.0.22.0/24

The DB security group permits TCP port 3306 from p1-app-sg.

## Planned Security

- Encryption at rest enabled.
- Encrypted connections using TLS where configured.
- Automated backups enabled.
- Database credentials stored securely.
- No database passwords committed to GitHub.

## Current Status

RDS DB Subnet Group created.
Actual RDS database instance not created yet.
