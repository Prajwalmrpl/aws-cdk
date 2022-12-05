#Create SNS Topic & Subscriptions
import aws_cdk as cdk
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from aws_cdk import Stack
import constructs as Construct

class CustomSnsStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create SNS Topic
        new_sns_topic = sns.Topic(self,
                                    "newTopics",
                                    display_name="latest topics",
                                    topic_name="newSNSTopics"
                                    )
        
        #Add Subscription to SNS Topic
        new_sns_topic.add_subscription(
            subs.EmailSubscription("prajwal.p@moreretail.in")
        )