# AWS VPC and Networking Configuration

## 1. VPC

- Name: p1-vpc
- CIDR: 10.0.0.0/16
- DNS Resolution: Enabled
- DNS Hostnames: Enabled

## 2. Subnet Configuration

The VPC contains six subnets across two Availability Zones.

| Subnet Name | CIDR | Layer |
|---|---|---|
| p1-public-a | 10.0.1.0/24 | Public |
| p1-public-b | 10.0.2.0/24 | Public |
| p1-app-a | 10.0.11.0/24 | Application |
| p1-app-b | 10.0.12.0/24 | Application |
| p1-db-a | 10.0.21.0/24 | Database |
| p1-db-b | 10.0.22.0/24 | Database |

## 3. Internet Gateway

- Name: p1-igw
- Attached to: p1-vpc
- Provides internet connectivity to resources in public subnets when their other network settings permit it.

## 4. Route Tables

### Public Route Table

Name: p1-public-rt

Routes:
- 10.0.0.0/16 -> local
- 0.0.0.0/0 -> Internet Gateway

Associated subnets:
- p1-public-a
- p1-public-b

### Application Route Table

Name: p1-app-rt

Routes:
- 10.0.0.0/16 -> local

Associated subnets:
- p1-app-a
- p1-app-b

A NAT Gateway route will be added during deployment.

### Database Route Table

Name: p1-db-rt

Routes:
- 10.0.0.0/16 -> local

Associated subnets:
- p1-db-a
- p1-db-b

No direct internet route is configured.

## 5. Traffic Flow

Planned application traffic:

Internet
   |
Internet Gateway
   |
Public Application Load Balancer
   |
Private EC2 Application Instances
   |
Private RDS Database

## 6. Current Status

- VPC: Created
- Six subnets: Created
- Internet Gateway: Created and attached
- Three custom route tables: Created
- Subnet associations: Completed
- NAT Gateway: Pending
- Application Load Balancer: Pending
- EC2 deployment: Pending
- RDS deployment: Pending
