1.Launch EC2 using CDK

        # Import existing VPC using VPC-ID using ec2.Vpc.from_lookup method
        # output using the CfnOutput
        # Allow Port 80 https to instance Security group
    
2.Customize EC2 Instances by Bootstrapping them with user data

        # Bootstrapping in AWS simply means to add commands or scripts to AWS EC2’s instance User Data section that can be executed when the instance starts.
        # Read the BootStrap Script
        # output the url using CfnOutput 
        # Allow wen traffic for EC2 instance to connect to http port 80

3.Launch EC2 with Custom Instant Profile - SSM Agent Role - Login without SSH Keys

        # Create AWS secrets & SSM Parameters
        # Output the url using CfnOutput

4.Launch EC2 with latest AMI in any AWS Region - Portable Region Independent stack

        # Create AWS secrets & SSM Parameters
        # Create Secrets with Secrets manager
        # Create custom Secrets
        # output using the CfnOutput

5.Improve EC2 Performance with EBS Provisioned IOPS SSD Volumes

        #Create an vpc with CIDR 10.10.0.0/24 with max_azs=2 and one NAT gateway and subnet configuration with public and private subnets.
        # Read the BootStrap Script
        # Get the latest ami
        # Create an WebServer(EC2) Instance
        # Add EBS to EC2 instance with provisioned IOPS Storage.
        # Output the instance using the instance public-ip
        # Allow Web Traffic to WebServer by allowing port 80
        # Add permission to web server instance profile

6.Highly Available Web Servers with AutoScaling & Application Load Balancer

        # Read the BootStrap Script
        # Create a vpc with CIDR-10.0.0.0/24 with max_azs=2 and one nat gateway with subnet configuration public and private subnets
        # Create the latest amazon-linux AMI
        # Create a Application Load Balancer with internet facing
        # add listener to ALB
        # Create Webserver IAM Role
        # Create AutoScaling group with 2 EC2 instance
        # it allow ASG security group to recive Traffic from ALB
        # Add Autoscaling Group Instances to ALB Target Group
        # Output of the ALB Domain Name using CfnOutput


       
        
        
        
        
        
        
       
        
       