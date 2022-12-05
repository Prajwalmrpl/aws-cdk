#Deploy a static website with contents
import aws_cdk as cdk 
from aws_cdk import Stack 
import constructs as Construct
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_s3_deployment as _s3_deployment


class DeployStaticSiteStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 Bucket
        static_site_assets_bkt = _s3.Bucket(
            self,
            "assetsBucket",
            versioned=True,
            public_read_access=True,
            website_index_document="index.html",
            website_error_document="404.html",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        # Add assets to static site bucket using s3_deployment module
        add_assets_to_site = _s3_deployment.BucketDeployment(
            self,
            "deployStaticSiteAssets",
            sources=[
                _s3_deployment.Source.asset(
                    "files/static_assets"
                )
            ],
            destination_bucket=static_site_assets_bkt
        )
