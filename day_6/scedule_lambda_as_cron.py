# Schedule your Lambda Function: Cron in the cloud
from aws_cdk import Stack
import aws_cdk as cdk
import constructs as Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets


class CustomLambdaAsCronStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Serverless Event Processor using Lambda
        # Read Lambda Code
        try:
            with open("serverless_stacks/lambda_src/lambda_processor.py", mode="r") as f:
                konstone_fn_code = f.read()
        except OSError:
            print("Unable to read Lambda Function Code")

        # Simple Lambda Function to return event
        mynew_fn = _lambda.Function(self,
                                       "MyNew2Function",
                                       function_name="mynew2_function",
                                       runtime=_lambda.Runtime.PYTHON_3_7,
                                       handler="index.lambda_handler",
                                       code=_lambda.InlineCode(
                                           konstone_fn_code),
                                       timeout=cdk.Duration.seconds(3),
                                       #reserved_concurrent_executions=1,
                                       environment={
                                           "LOG_LEVEL": "INFO",
                                           "AUTOMATION": "SKON"
                                       }
                                       )

        # Run Every day at 16:00 UTC
        four_pm_cron = events.Rule(
            self,
            "fourPmRule",
            schedule= events.Schedule.cron(
                minute="0",
                hour="16",
                month="*",
                week_day="MON-FRI",
                year="*"
            )
        )

        # Setup Cron Based on Rate
        # Run Every 3 Minutes
        run_every_3_minutes = events.Rule(
            self,
            "runEvery3Minutes",
            schedule= events.Schedule.rate(cdk.Duration.minutes(3))
        )

        # Add Lambda to CW Event Rule
        four_pm_cron.add_target( targets.LambdaFunction(mynew_fn))
        run_every_3_minutes.add_target( targets.LambdaFunction(mynew_fn))

        
