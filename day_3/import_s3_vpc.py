from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3
from aws_cdk import core


class CustomVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        prod_configs = self.node.try_get_context('envs')['prod']

        #Create a custom VPC
        custom_vpc = ec2.Vpc(
            self,
            "customVpcId",
            cidr=prod_configs['vpc_configs']['vpc_cidr'],
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                _ec2.SubnetConfiguration(
                    name="publicSubnet", cidr_mask=prod_configs['vpc_configs']['cidr_mask'], subnet_type=_ec2.SubnetType.PUBLIC
                ),
                _ec2.SubnetConfiguration(
                    name="privateSubnet", cidr_mask=prod_configs['vpc_configs']['cidr_mask'], subnet_type=_ec2.SubnetType.PRIVATE
                ),
                _ec2.SubnetConfiguration(
                    name="dbSubnet", cidr_mask=prod_configs['vpc_configs']['cidr_mask'], subnet_type=_ec2.SubnetType.ISOLATED
                )
            ]
        )
        
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

