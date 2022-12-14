from aws_cdk import aws_apigateway as _apigw
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as _logs
import aws_cdk as cdk 
from aws_cdk import Stack
import constructs as Construct


class CustomApiGatewayStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Serverless Event Processor using Lambda):
        # Read Lambda Code
        try:
            with open("serverless_stacks/lambda_src/konstone_hello_world.py", mode="r") as f:
                konstone_fn_code = f.read()
        except OSError:
            print("Unable to read Lambda Function Code")

        konstone_fn = _lambda.Function(self,
                                       "konstoneFunction",
                                       function_name="konstone_function",
                                       runtime=_lambda.Runtime.PYTHON_3_7,
                                       handler="index.lambda_handler",
                                       code=_lambda.InlineCode(
                                           konstone_fn_code),
                                       timeout=cdk.Duration.seconds(3),
                                       #reserved_concurrent_executions=1,
                                       environment={
                                           "LOG_LEVEL": "INFO",
                                           "Environment": "Production"
                                       }
                                       )

        # Create Custom Loggroup
        # /aws/lambda/function-name
        konstone_lg = _logs.LogGroup(self,
                                     "konstoneLoggroup",
                                     log_group_name=f"/aws/lambda/{konstone_fn.function_name}",
                                     retention=_logs.RetentionDays.ONE_WEEK,
                                     removal_policy=cdk.RemovalPolicy.DESTROY
                                     )

        #Add API-GW for the lambda Function
        konstone_fn_integration = _apigw.LambdaRestApi(
            self,
            "konstoneApiEndpoint",
            handler=konstone_fn
        )

        output_1 = cdk.CfnOutput(self,
                                  "ApiUrl",
                                  value=f"{konstone_fn_integration.url}",
                                  description="Use a browser to access this url"
                                  )
