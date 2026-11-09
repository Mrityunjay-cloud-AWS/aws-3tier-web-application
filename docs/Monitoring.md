# AWS CloudWatch and SNS Monitoring

## Overview

Amazon CloudWatch will monitor application infrastructure and provide alerts through Amazon SNS.

## Planned EC2 Monitoring

- CPU utilization
- Network activity
- Instance status checks
- Memory and disk metrics through CloudWatch Agent

## Planned ALB Monitoring

- RequestCount
- HealthyHostCount
- UnHealthyHostCount
- TargetResponseTime

## Planned RDS Monitoring

- CPUUtilization
- DatabaseConnections
- FreeStorageSpace
- ReadIOPS
- WriteIOPS

## Planned Alarms

- EC2 high CPU utilization
- ALB unhealthy targets
- RDS high CPU utilization

## SNS Notifications

Planned SNS topic: p1-alerts

Email notifications will be configured for alarm alerts.

## Current Status

CloudWatch and SNS architecture planned.
Alarms and dashboard pending deployment.
SNS topic and email subscription require confirmation.
