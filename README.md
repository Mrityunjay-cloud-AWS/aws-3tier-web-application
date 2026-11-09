##  AWS Three-Tier Web Application

 # Project Overview



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

