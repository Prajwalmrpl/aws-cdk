import aws_cdk as core
import aws_cdk.assertions as assertions

from day_8.day_8_stack import Day8Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in day_8/day_8_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Day8Stack(app, "day-8")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
