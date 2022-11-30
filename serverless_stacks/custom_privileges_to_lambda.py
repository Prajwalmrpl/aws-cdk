import aws_cdk as cdk 
from aws_cdk import Stack 
import constructs as Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_iam as iam


class CustomPrivilegesToLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Create DynamoDB Table
        konstone_s3_assets_table = dynamodb.Table(
            self,
            "konstoneAssetsDDBTable",
            table_name="konstone-asset-table",
            partition_key= dynamodb.Attribute(
                name="_id",
                type= dynamodb.AttributeType.STRING
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY
        )


        # Read Lambda Code
        try:
            with open("serverless_stacks/lambda_src/konstone_s3_inventory_generator.py", mode="r") as f:
                konstone_fn_code = f.read()
        except OSError:
            print("Unable to read Lambda Function Code")

        # Deploy the lambda function
        konstone_fn = _lambda.Function(self,
                                       "konstoneFunction",
                                       function_name="konstone_function_s3_inventory_generator",
                                       runtime=_lambda.Runtime.PYTHON_3_7,
                                       handler="index.lambda_handler",
                                       code=_lambda.InlineCode(
                                           konstone_fn_code),
                                       timeout=cdk.Duration.seconds(3),
                                       #reserved_concurrent_executions=1,
                                       environment={
                                           "LOG_LEVEL": "INFO",
                                           "DDB_TABLE_NAME": f"{konstone_s3_assets_table.table_name}"
                                       }
                                        )

        #Add S3 Read Only Managed Policy to Lambda
        konstone_fn.role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonS3ReadOnlyAccess"
            )
        )
        
        #Add DynamoDB Write Privilages To Lambda
        konstone_s3_assets_table.grant_write_data(konstone_fn)

        
    

