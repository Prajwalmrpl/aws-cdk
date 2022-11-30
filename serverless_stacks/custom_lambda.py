from aws_cdk import Stack
import aws_cdk as cdk
import constructs as Construct 
from aws_cdk import aws_lambda as _lambda


class CustomLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Serverless Event Processor using Lambda):
        # Read the Lambda Code from lambda_processor.py
        try:
            with open("serverless_stacks/lambda_src/lambda_processor.py", mode="r") as f:
                new_fn_code = f.read()
        except OSError:
            print("Unable to read Lambda Function Code") 

        custom_fn = _lambda.Function(self,
                                       "MyLambdaFunction",
                                       function_name="newlambda_function",
                                       runtime=_lambda.Runtime.PYTHON_3_7,
                                       handler="index.lambda_handler",
                                       code=_lambda.InlineCode(
                                           new_fn_code),
                                       timeout=cdk.Duration.seconds(3),
                                       #reserved_concurrent_executions=1,
                                       environment={
                                           "LOG_LEVEL": "INFO"
                                       }
                                       )
