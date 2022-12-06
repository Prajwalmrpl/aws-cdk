1.Serverless REST API Architecture: APIGW, Lambda & DynamoDB.

    # Create the DynamoDB Table
    # Read the Lambda Code
    # Deploy the lambda function
    # Add DynamoDB Write Privileges To Lambda
    # Create Custom Loggroup
    # Add API GW front end for the Lambda
    # Output the API GW Url using CfnOutput

2.Serverless Stream Processor Architecture with Kinesis.

    # Create Kinesis Data Stream
    # Create an S3 Bucket for Storing Data Stream
    # Read the lambda code
    # Create the Lambda Function for consumer
    # Update Lambda Permission to use stream
    # add permission to lambda to write to S3
    # Create Custom Loggroup for Consumer
    # Create Kinesis Event Source 
    # Attach Kinesis Event Source to Lambda 
    # Read the lambda Code
    # create the Lambda Function for producer
    # Grant our Lambda Producer privileges to write to Kinesis  
    # Create custom Loggroup for Producer
        
3.Serverless DynamoDB Event Processor Architecture with DynamoDB Streams.

        # create the DynamoDB Table
        # Read the Lambda Code
        # Deploy the lambda function
        # Create New DDB Stream Event Source
        # Attach DDB Event Source As Lambda Trigger

4.Containerized Micro Service Architecture with ECS.

        # Create a VPC with CIDR 10.10.0.0/16 with max_azs=2 and 1 NAT Gateway and one public subnet and one private subnet
        # Create a ECS cluster
        # defining the ECS Cluster Capacity
        # deploy the container and attach a LoadBalancer
        # output web service url using CloudFormationOutput

5.Run Containers without managing servers using Fargate.

        # Create a VPC for hosting the micro service
        # Create the Fargate Cluster inside the VPC
        # Deploy Container in the micro Service with an Application Load Balancer
        # Server Health Checks
        # Output Web Service Url
        
6.Serverless Batch Job Architecture with Fargate

        # Add your stack resources below):
        # Create a VPC
        # Create a Fargate Cluster
        # Deploy the Batch Processing Container Task in Fargate with Cloudwatch Event Schedule
       