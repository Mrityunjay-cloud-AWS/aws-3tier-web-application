
# Application Testing and Validation

## Planned Network Tests

- Verify VPC and subnet configuration.
- Verify route table associations.
- Verify ALB-to-EC2 connectivity.
- Verify EC2-to-RDS connectivity.
- Verify database port 3306 accessibility only from the application layer.

## Planned EC2 Tests

- Check Nginx service status.
- Verify application HTTP response.
- Check cloud-init logs.
- Verify instance metadata access using IMDSv2.

## Planned Database Tests

- Verify database connectivity.
- Connect using MySQL client.
- Create and retrieve test records.
- Verify application database operations.

## Planned Load Balancer Tests

- Verify target registration.
- Verify target health.
- Access application through ALB DNS name.
- Verify traffic distribution across healthy instances.

## Planned Monitoring Tests

- Check CloudWatch metrics.
- Verify alarm state transitions.
- Verify SNS email notifications.

## Current Status

These are planned validation steps.
End-to-end application testing has not yet been performed.
Results will be recorded after deployment.
