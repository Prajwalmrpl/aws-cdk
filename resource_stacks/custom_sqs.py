from aws_cdk import aws_sqs as sqs
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import Stack


class CustomSqsStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Craete SQS Queue
        new_queue = sqs.Queue(self,
                                "newQueue",
                                queue_name="new_queue.fifo",
                                fifo = True,
                                encryption= sqs.QueueEncryption.KMS_MANAGED,
                                retention_period= cdk.Duration.days(4),
                                visibility_timeout= cdk.Duration.seconds(45)
                                )