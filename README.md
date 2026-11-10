
# Project Overview

This project demonstrates a secure three-tier web application architecture using AWS services.

## Architecture

1. Presentation Layer: Application Load Balancer in public subnets.
2. Application Layer: EC2 instances in private application subnets.
3. Database Layer: Amazon RDS MySQL in private database subnets.

### AWS Services and Progress

| Service | Purpose | Status |
|---|---|---|
| VPC | Isolated network | Created |
| Subnets | Network segmentation | Created |
| Internet Gateway | Public internet connectivity | Created |
| Route Tables | Network routing | Created |
| Security Groups | Network security | Created |
| IAM Role | EC2 permissions | Created |
| Launch Template | EC2 configuration | Created |
| Target Group | Application targets | Created |
| Auto Scaling Group | Instance management | Created |
| RDS Subnet Group | Database networking | Created |
| Flask Application | Web application | Created locally |
| NAT Gateway | Private subnet outbound access | Pending |
| EC2 Instances | Application hosting | Pending |
| RDS MySQL | Database | Pending |
| Application Load Balancer | Traffic distribution | Pending |
| CloudWatch | Monitoring | Pending |

## Network Architecture

VPC CIDR: `10.0.0.0/16`

| Subnet | CIDR | Purpose |
|---|---|---|
| p1-public-a | 10.0.1.0/24 | Public |
| p1-public-b | 10.0.2.0/24 | Public |
| p1-app-a | 10.0.11.0/24 | Application |
| p1-app-b | 10.0.12.0/24 | Application |
| p1-db-a | 10.0.21.0/24 | Database |
| p1-db-b | 10.0.22.0/24 | Database |

## Security

- Application instances will run in private subnets.
- RDS will not have public access.
- ALB traffic will be controlled using Security Groups.
- Database access will be restricted to the application Security Group.
- EC2 uses an IAM role.
- IMDSv2 is required.

## Application

The application uses:
- Python
- Flask
- MySQL Connector
- Gunicorn

Application files are stored in the `app/` directory.

## Current Progress

- AWS networking infrastructure created.
- Security Groups and IAM configured.
- Launch Template and Auto Scaling Group created.
- Flask application created and tested locally.
- AWS application deployment pending.
- RDS database deployment pending.
- End-to-end testing pending.

## Cost Management

Billable resources will be deployed for a controlled testing period and removed after validation.
 # Project Overview
=======
 ## AWS Three-Tier Web Application

 #Project Overview
>>>>>>> 71c48a0 (Add Flask application)



# This project demonstrates the design and deployment of a three-tier web application on AWS using secure networking, compute, database, load balancing, and monitoring services.

# 

# \## Architecture

# 

# The application follows a three-tier architecture:

# 

# 1\. Presentation Layer: Application Load Balancer (public subnets).

# 2\. Application Layer: EC2 instances managed by an Auto Scaling Group (private application subnets).

# 3\. Database Layer: Amazon RDS MySQL (private database subnets).

# 

# \## AWS Services

# 

# | AWS Service | Purpose | Status |

# |---|---|---|

# | Amazon VPC | Isolated network | Created |

# | Subnets | Public, application and database layers | Created |

# | Internet Gateway | Internet connectivity for public subnets | Created |

# | Route Tables | Network traffic routing | Created |

# | Security Groups | Network access control | Created |

# | IAM Role | EC2 permissions | Created |

# | EC2 Launch Template | Instance configuration | Created |

# | Target Group | Application target registration | Created |

# | Auto Scaling Group | EC2 scaling and management | Created, desired capacity 0 |

# | RDS Subnet Group | Database network placement | Created |

# | NAT Gateway | Outbound internet for private instances | Pending |

# | EC2 Instances | Application compute | Pending |

# | Amazon RDS | MySQL database | Pending |

# | Application Load Balancer | Application traffic distribution | Pending |

# | CloudWatch Alarms | Monitoring and alerts | Pending |

# 

# \## Network Architecture

# 

# VPC CIDR: `10.0.0.0/16`

# 

# | Subnet | CIDR | Purpose |

# |---|---|---|

# | p1-public-a | 10.0.1.0/24 | Public |

# | p1-public-b | 10.0.2.0/24 | Public |

# | p1-app-a | 10.0.11.0/24 | Application |

# | p1-app-b | 10.0.12.0/24 | Application |

# | p1-db-a | 10.0.21.0/24 | Database |

# | p1-db-b | 10.0.22.0/24 | Database |

# 

# \## Security Design

# 

# \- Application instances are planned for private subnets.

# \- Database instances will not have public access.

# \- ALB traffic will be permitted through the ALB security group.

# \- Application traffic will be permitted from the ALB security group.

# \- Database traffic will be permitted from the application security group.

# \- EC2 instances use an IAM role.

# \- IMDSv2 is required in the EC2 Launch Template.

# \- Secrets and credentials must never be committed to GitHub.

