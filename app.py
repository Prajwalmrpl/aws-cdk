#!/usr/bin/env python3
import os

import aws_cdk as cdk


from demo_cdk.demo_cdk_stack import DemoCdkStack
#from resource_stacks.custom_vpc import CustomVpcStack
#from resource_stacks.custom_ec2 import CustomEC2Stack
#from resource_stacks.custom_ec2_instance_profile import CustomEc2InstanceProfileStack
#from resource_stacks.ec2_with_latest_ami import CustomEc2LatestAmiStack
#from resource_stacks.ec2_with_ebs_piops import CustomEc2PiopsStack
from resource_stacks.alb_ag_stack import AlbAgStack
#from resource_stacks.vpc_stack import VpcStack
from resource_stacks.ssm_parameter_secrets import CustomParametersSecretsStack
from resource_stacks.custom_iam_users_groups import CustomIamUsersGroupsStack
from resource_stacks.s3_resource_policy import CustomS3ResourcePolicyStack
from resource_stacks.custom_sns import CustomSnsStack
from resource_stacks.custom_sqs import CustomSqsStack

from serverless_stacks.custom_lambda import CustomLambdaStack
from serverless_stacks.custom_lambda_src_from_s3 import CustomLambdaSrcFromS3Stack
from serverless_stacks.custom_lambda_as_cron import CustomLambdaAsCronStack

from stacks_from_cfn.stack_from_existing_cfn_template import StackFromCloudformationTemplate

app = cdk.App()

env_US = cdk.Environment(account="923407756913",region="us-east-1")
#env_Mumbai = core.Environment(account="923407756913",region="ap-south-1")

#DemoCdkStack(app, "Stack1", )
#DemoCdkStack(app, "Stack2", env=env_Mumbai)

#customvpc = CustomVpcStack(app, "CustomVPCStack", env=env_Mumbai )
#cdk.Tags.of(customvpc).add("Name", "CustomVPC")

#CustomEC2Stack(app, "customEC2Stack", env=env_Mumbai)

#CustomEc2InstanceProfileStack(app, "CustomEC2InstanceProfile")

#CustomEc2LatestAmiStack(app, "EC2withlatestAMI")

#CustomEc2PiopsStack(app, "ec2piopsstack")


#AlbAgStack(app, "ALB-AG-Stack")

#CustomParametersSecretsStack(app, "SSMStack")

#CustomIamUsersGroupsStack(app, "IAM-Users-Groups-Stack"

#CustomS3ResourcePolicyStack(app, "S3-Resource-Policy")

#CustomSnsStack(app, "SnsStack")

#CustomSqsStack(app, "SQSStack")

#CustomLambdaStack(app, "CustomLambdaStack")

CustomLambdaSrcFromS3Stack(app, "CustomLambdaSrcFromS3Stack", env=env_US)

CustomLambdaAsCronStack(app, "CustomLambdaAsCronStack", env=env_US)

StackFromCloudformationTemplate(app, "StackFromCloudformationTemplate", env=env_US)


app.synth()
