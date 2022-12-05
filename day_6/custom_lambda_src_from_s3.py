#Serverless: Lambda Source Assets from S3
from aws_cdk import Stack
import aws_cdk as cdk
import constructs as Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as logs
from aws_cdk import aws_s3 as s3

class CustomLambdaSrcFromS3Stack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Import an S3 Bucket):
        mynew_bkt = s3.Bucket.from_bucket_attributes(self,
                                                         "AssetsBucket",
                                                         bucket_name="new-assets-bkt")

        # Create Lambda function with source code from S3 Bucket
        mylambda_fn = _lambda.Function(self,
                                       "MynewFunction",
                                       function_name="new_fn",
                                       runtime=_lambda.Runtime.PYTHON_3_7,
                                       handler="konstone_processor.lambda_handler",
                                       code=_lambda.S3Code(
                                           bucket=mynew_bkt,
                                           key="lambda_src/konstone_processor.zip"
                                       ),
                                       timeout=cdk.Duration.seconds(2),
                                       #reserved_concurrent_executions=1
                                       )

        # Create Custom Loggroup
        # /aws/lambda/function-name
        my_lg = logs.LogGroup(self,
                                     "MynewLoggroup",
                                     log_group_name=f"/aws/lambda/{mylambda_fn.function_name}",
                                     removal_policy=cdk.RemovalPolicy.DESTROY,
                                     retention= logs.RetentionDays.ONE_WEEK
                                     )
