from constructs import Construct
from aws_cdk import aws_ec2 as ec2
from aws_cdk import Stack
import aws_cdk as cdk

class CustomVpcStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

     

        custom_vpc = ec2.Vpc(
            self,
            "customVpcId",
            cidr="10.83.0.0/20",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="publicSubnet", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name="privateSubnet", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                )
            ]
        )

        cdk.CfnOutput(self,
                    "customVpcOutput",
                    value=custom_vpc.vpc_id,
                    export_name="customVpcId")