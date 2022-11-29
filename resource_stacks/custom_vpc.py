from aws_cdk import (
    Stack, 
)
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3


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
        
        my_bkt = s3.Bucket(self, "custombktId")

        cdk.Tag.add(my_bkt, "Owner", "Admin")

        
        # Resource in same account.
        bkt1 = s3.Bucket.from_bucket_name(
            self,
            "MyImportedBuket",
            "sample-bkt-cdk-010"
        )

        bkt2 = s3.Bucket.from_bucket_arn(self,
                                          "crossAccountBucket",
                                          "arn:aws:s3:::SAMPLE-CROSS-BUCKET")

        cdk.CfnOutput(self,
                       "myimportedbucket",
                       value=bkt1.bucket_name)