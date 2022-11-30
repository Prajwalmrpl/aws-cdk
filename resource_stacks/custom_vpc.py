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
        #import the S3 bucket from the same account
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

        #import existing VPC from the same account and same region using VPC-ID
        vpc2 = ec2.Vpc.from_lookup(self,
                                    "importedVPC",
                                    # is_default=True,
                                    vpc_id="vpc-d0a193aa"
                                    )

        cdk.CfnOutput(self,
                       "importedVpc2",
                       value=vpc2.vpc_id)

        #VPC Peering to connect between 2 VPC's imported vpc and the custom vpc
        peer_vpc = ec2.CfnVPCPeeringConnection(self,
                                                "peerVpc12",
                                                peer_vpc_id=custom_vpc.vpc_id,
                                                vpc_id=vpc2.vpc_id)