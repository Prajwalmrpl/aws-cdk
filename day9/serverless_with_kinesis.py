#Serverless Stream Processor Architecture with Kinesis
import aws_cdk as cdk
from aws_cdk import Stack 
import constructs as Construct
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_kinesis as _kinesis
from aws_cdk import aws_logs as _logs
from aws_cdk import aws_lambda_event_sources as _lambda_event_sources

class ServerlessStreamProcessArchitectureWithS3Stack(Stack):

     def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Create Kinesis Data Stream
        stream_data = _kinesis.Stream(
            self,
            "mykinesisDS",
            retention_period= cdk.Duration.hours(24),
            shard_count=1,
            stream_name="data-pipe"
        )

        #Create an S3 Bucket for Storing Data Stream
        stdata_store = _s3.Bucket(self,
                                "streamData",
                                removal_policy= cdk.RemovalPolicy.DESTROY
        )
        
        #Read the lambda code
        try:
            with open("files/lambda_src/stream_record_consumer.py",mode="r") as f:
                stream_consumer_fn_code = f.read()
        except OSError:
            print("Unable to read lambda function code")

        #Create an Lambda Function
        stream_consumer_fn = _lambda.Function(self,
                                                "streamConsumerFn",
                                                function_name="Stream-Consumer-Function",
                                                description="Process streaming data events from kinesis and store in S3",
                                                runtime= _lambda.Runtime.PYTHON_3_7,
                                                handler= "index.lambda_handler",
                                                code = _lambda.InlineCode(
                                                    stream_consumer_fn_code
                                                ),
                                                timeout= cdk.Duration.seconds(3),
                                                #reserved_concurrent_executions=1,
                                                environment={
                                                    "LOG_LEVEL": "INFO",
                                                    "BUCKET_NAME": f"{stdata_store.bucket_name}"
                                                }
                                                )

        #Update Lambda Permission to use stream
        stream_data.grant_read(stream_consumer_fn)

        #add permission to lambda to write to S3
        role_stm1 = _iam.PolicyStatement(
            effect= _iam.Effect.ALLOW,
            resources=[
                f"{stdata_store.bucket_arn}/*"
            ],
            actions=[
                "s3:PutObject"
            ]
        )
        role_stm1.sid="AllowLambdaToWriteToS3"
        stream_consumer_fn.add_to_role_policy(role_stm1)

        #Create Custom Loggroup for Consumer
        stream_consumer_lg = _logs.LogGroup(
                                self,
                                "streamConsumerLogGroup",
                                log_group_name=f"/aws/lambda/{stream_consumer_fn.function_name}",
                                removal_policy= cdk.RemovalPolicy.DESTROY,
                                retention= _logs.RetentionDays.ONE_DAY
                                )

        #Create Kinesis Event Source 
        stream_data_pipe_event_source = _lambda_event_sources.KinesisEventSource(
            stream=stream_data,
            starting_position=_lambda.StartingPosition.LATEST,
            batch_size=1
        )

        #Attach Kinesis Event Source to Lambda 
        stream_consumer_fn.add_event_source(stream_data_pipe_event_source)

        #Read the lambda Code
        try:
            with open("files/lambda_src/stream_data_producer.py", mode="r") as f:
                data_producer_fn_code = f.read()
        except OSError:
            print("Unable to read lambda function code")


        #create the Lambda Function 
        data_producer_fn = _lambda.Function(
            self,
            "streamDataProducerFn",
            function_name="data_producer_fn",
            description="Produce streaming data events and push to Kinesis stream",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler",
            code=_lambda.InlineCode(
                data_producer_fn_code
            ),
            timeout=cdk.Duration.seconds(60),
            #reserved_concurrent_executions=1,
            environment={
                "LOG_LEVEL":"INFO",
                "STREAM_NAME":f"{stream_data.stream_name}"
            }
        )

        # Grant our Lambda Producer privileges to write to Kinesis Data Stream
        stream_data.grant_read_write(data_producer_fn)

        #Create custom Loggroup for Producer
        data_producer_lg = _logs.LogGroup(
            self,
            "dataProducerLogGroup",
             log_group_name=f"/aws/lambda/{data_producer_fn.function_name}",
             removal_policy = cdk.RemovalPolicy.DESTROY,
             retention= _logs.RetentionDays.ONE_DAY
        )



