import aws_cdk as core
import aws_cdk.assertions as assertions

from day9.day9_stack import Day9Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in day9/day9_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Day9Stack(app, "day9")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
