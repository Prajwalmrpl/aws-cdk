import aws_cdk as cdk
from aws_cdk import Stack
import constructs as Construct

import json


class StackFromCloudformationTemplate(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Import Existing Clouformation Template):
        try:
            with open("stacks_from_cfn/sample_templates/create_s3_bucket_template.json", mode="r") as file:
                cfn_template = json.load(file)
        except OSError:
            print("Unable to read Cfn Template")

        

        encrypted_bkt_arn = cdk.Fn.get_att("EncryptedS3Bucket", "Arn")

        # Output Arn of encrypted Bucket
        output_1 = cdk.CfnOutput(self,
                                  "EncryptedBucketArn",
                                  value=f"{encrypted_bkt_arn.to_string()}",
                                  description="Arn of Encrypted Bucket from Cfn Template"
                                  )
