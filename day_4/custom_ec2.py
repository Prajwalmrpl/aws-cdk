# Launch EC2 using CDK
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
import aws_cdk as cdk
from aws_cdk import core

class CustomEC2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        vpc = ec2.Vpc.from_lookup(self,
                                   "importedVPC",
                                   vpc_id="vpc-08f6152635aec0936")
        
        web_server = ec2.Instance(self,
                                   "Instance01Id",
                                   instance_type=ec2.InstanceType(
                                       instance_type_identifier="t2.micro"),
                                   instance_name="MyInstance1",
                                   machine_image=ec2.MachineImage.generic_linux(
                                       {"us-east-1": "ami-0fc61db8544a617ed"}
                                   ),
                                   vpc=vpc,
                                   vpc_subnets=ec2.SubnetSelection(
                                       subnet_type=ec2.SubnetType.PUBLIC
                                   ),
                                   )
        

        output_1 = core.CfnOutput(self,
                                  "MyInstance1Ip",
                                  description="MyInstancePublic Ip Address",
                                  value=f"http://{web_server.instance_public_ip}")

        
        web_server.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), description="Allow Web Traffic"
        )
    