# Application Load Balancer Configuration

## Overview

An internet-facing Application Load Balancer will distribute HTTP requests across healthy application instances.

## Prepared Target Group

- Name: p1-app-tg
- Target Type: Instances
- Protocol: HTTP
- Port: 80
- VPC: p1-vpc
- Health Check Path: /

## Health Check Configuration

- Protocol: HTTP
- Path: /
- Success Code: 200
- Interval: 30 seconds
- Timeout: 5 seconds
- Healthy Threshold: 5
- Unhealthy Threshold: 2

## Planned ALB Configuration

- Name: p1-alb
- Scheme: Internet-facing
- IP Address Type: IPv4
- VPC: p1-vpc
- Subnets: p1-public-a and p1-public-b
- Security Group: p1-alb-sg
- Listener: HTTP port 80
- Forwarding Target: p1-app-tg

## Current Status

Target Group created.
No targets registered.
Application Load Balancer not created yet.
