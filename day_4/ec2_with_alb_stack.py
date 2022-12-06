#Highly Available Web Servers with AutoScaling & Application Load Balancer
from aws_cdk import (
    Stack, 
)
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_autoscaling as autoscaling
import aws_cdk as cdk
from constructs import Construct

class AlbAgStack(Stack):

    def __init__(self, scope: Construct, id: str,  **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Read BootStrap Script):
        try:
            with open("bootstrap_scripts/install_httpd.sh", mode="r") as file:
                user_data = file.read()
        except OSError:
            print('Unable to read UserData script')

        vpc = ec2.Vpc(
            self,
            "customVpcId",
            cidr="10.0.0.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", subnet_type=ec2.SubnetType.PUBLIC
                )
            ]
        )
    

        linux_ami =  ec2.AmazonLinuxImage(generation= ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                          edition= ec2.AmazonLinuxEdition.STANDARD,
                                          virtualization= ec2.AmazonLinuxVirt.HVM,
                                          storage= ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                          ) 
        
        #to create Application Load Balancer
        alb = elbv2.ApplicationLoadBalancer(
            self,
            "myALBId",
            vpc=vpc,
            internet_facing=True,
            load_balancer_name="MyALB"
        )

        #add listener to ALB
        listener = alb.add_listener("listenerID",
                                    port=80,
                                    open=True)

        # Webserver IAM Role
        web_server_role = iam.Role(self, "webServerRoleId",
                                    assumed_by= iam.ServicePrincipal(
                                        'ec2.amazonaws.com'),
                                    managed_policies=[
                                        iam.ManagedPolicy.from_aws_managed_policy_name(
                                            'AmazonSSMManagedInstanceCore'
                                        ),
                                        iam.ManagedPolicy.from_aws_managed_policy_name(
                                            'AmazonS3ReadOnlyAccess'
                                        )
                                    ])

        #create AutoScaling group with 2 EC2 instance
        web_server_asg = autoscaling.AutoScalingGroup(self,
                                                    "webserverAsgId",
                                                    vpc=vpc,
                                                    vpc_subnets= ec2.SubnetSelection(
                                                        subnet_type= ec2.SubnetType.PUBLIC
                                                    ),
                                                    instance_type= ec2.InstanceType(
                                                        instance_type_identifier="t2.micro"),
                                                    machine_image=linux_ami,
                                                    role=web_server_role,
                                                    min_capacity=2,
                                                    max_capacity=2,
                                                    desired_capacity=2,
                                                    user_data= ec2.UserData.custom(
                                                        user_data)
                                                    )

        #it allow ASG security group to revcive Traffic from ALB
        web_server_asg.connections.allow_from(alb, ec2.Port.tcp(80),
                                                description="Allows ASG Security group to recive traffic from ALB")

        #Add Autoscaling Group Instances to ALB Target Group
        listener.add_targets("listenerId", port=80, targets=[web_server_asg])

        #Output of the ALB Domain Name
        output_alb_1 = cdk.CfnOutput(self,
                                    "albDomainName",
                                    value=f"http://{alb.load_balancer_dns_name}",
                                    description="Web server ALB Domain name")

        
        
        
        
        
        