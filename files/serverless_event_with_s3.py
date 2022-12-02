import aws_cdk as cdk 
from aws_cdk import Stack
import constructs as Construct
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_dynamodb as _dynamodb
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as _logs
from aws_cdk import aws_s3_notifications as _s3_notifications


class ServerlessEventProcessorArchitectureWithS3EventsStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Add your stack resources below
        # Create an S3 Bucket for storing our web store assets
        kk_store = _s3.Bucket(
            self,
            "kkStore",
            versioned=True
        )
        # DynamoDB Table
        kk_store_assets_table = _dynamodb.Table(
            self,
            "kkStoreAssetsDDBTable",
            table_name="kk_store_assets_tables",
            partition_key=_dynamodb.Attribute(
                name="_id",
                type=_dynamodb.AttributeType.STRING
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        # Read Lambda Code
        try:
            with open("files/lambda_src/s3_event_processor.py", mode="r") as f:
                kk_store_processor_fn_code = f.read()
        except OSError:
            print("Unable to read Lambda Function Code")

        
        kk_store_processor_fn = _lambda.Function(
            self,
            "kkStoreProcessorFn",
            function_name="kk_store_processor_fn",
            description="Process store events and update DDB",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler",
            code=_lambda.InlineCode(
                kk_store_processor_fn_code
            ),
            timeout=cdk.Duration.seconds(3),
            #reserved_concurrent_executions=1,
            environment={
                "LOG_LEVEL": "INFO",
                "DDB_TABLE_NAME": f"{kk_store_assets_table.table_name}"
            }
        )


        #add dynamodb write priviliges to lambda function
        kk_store_assets_table.grant_read_write_data(kk_store_processor_fn)

        # create a custom Loggroup
        kk_store_lg = _logs.LogGroup(
            self,
            "kkStoreLogGroup",
            log_group_name=f"/aws/lambda/{kk_store_processor_fn.function_name}",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            retention=_logs.RetentionDays.ONE_DAY
        )

        # create an s3 notification for the lambda function
        kk_store_backend = _s3_notifications.LambdaDestination(
            kk_store_processor_fn
        )

        # assign notification for the s3 event type for object created
        kk_store.add_event_notification(
            _s3.EventType.OBJECT_CREATED, kk_store_backend
        )
        



        