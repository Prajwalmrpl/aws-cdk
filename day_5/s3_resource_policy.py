# IAM Resource Policy: S3 Bucket Policy
from aws_cdk import (
    Stack, 
)
from constructs import Construct
import aws_cdk as cdk
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_iam as _iam


class CustomS3ResourcePolicyStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 Bucket
        new_bkt = _s3.Bucket(self,
                                  "Assets",
                                  versioned=True,
                                  removal_policy=cdk.RemovalPolicy.DESTROY
                                  )

        # Add Bucket Resource policy
        new_bkt.add_to_resource_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["s3:GetObject"],
                resources=[new_bkt.arn_for_objects("*.html")],
                principals=[_iam.AnyPrincipal()]
            )
        )

        new_bkt.add_to_resource_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.DENY,
                actions=["s3:*"],
                resources=[f"{new_bkt.bucket_arn}/*"],
                principals=[_iam.AnyPrincipal()],
                conditions={
                    "Bool": {"aws:SecureTransport": False}
                }
            )
        )
        