1.Create AWS SSM Parameter & AWS Secrets.

AWS Secrets Manager helps you organize and manage important configuration data such as credentials, passwords, and license keys. Parameter Store, a capability of AWS Systems Manager, is integrated with Secrets Manager so that you can retrieve Secrets Manager secrets when using other AWS services that already support references to Parameter Store parameters.
#create AWS secrets & SSM Parameters

2.Create IAM Role, Inline & Managed Policy.

	 # create IAM Users & Groups
     # Add User1 with SecretsManager Password
     # Add User2 with Literal Password
     # Add IAM Group
     # Login Url Autogeneration

3.IAM Resource Policy: S3 Bucket Policy.

	# Create an S3 Bucket
    # Add Bucket Resource policy

4.Create RDS Database.

	# Create an RDS Database
    # Allow EC2 ASG access to RDS MySQL
    # Output RDS Database EndPoint Address

5.Import pre-existing Cloud formation templates into CDK.

	# Import Existing Clouformation Template):
    # Output Arn of encrypted Bucket
  
6.Create SNS Topic & Subscriptions

	# Create SNS Topic
    # Add Subscription to SNS Topic
      
7.SQS: Fully Managed Message Queues for Microservices.

	#Create SQS Queue with FIFO Poilcy
    #Add encryption to queue
    #set the retention period and visibality timeout
      
        
    