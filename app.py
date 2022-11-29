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



app = cdk.App()

env_US = cdk.Environment(account="923407756913",region="us-east-1")
#env_Mumbai = core.Environment(account="923407756913",region="ap-south-1")

#DemoCdkStack(app, "Stack1", )
#DemoCdkStack(app, "Stack2", env=env_Mumbai)

#customvpc = CustomVpcStack(app, "CustomVPCStack", env=env_Mumbai )
#cdk.Tags.of(customvpc).add("Name", "CustomVPC")

#CustomEC2Stack(app, "customEC2Stack", env=env_Mumbai)

#CustomEc2InstanceProfileStack(app, "CustomEC2InstanceProfile", env=env_US)

#CustomEc2LatestAmiStack(app, "EC2withlatestAMI", env=env_US)

#CustomEc2PiopsStack(app, "ec2piopsstack", env=env_US)


#AlbAgStack(app, "ALB-AG-Stack", env=env_US)

#CustomParametersSecretsStack(app, "SSMStack", env=env_US)

CustomIamUsersGroupsStack(app, "IAM-Users-Groups-Stack", env=env_US)

CustomS3ResourcePolicyStack(app, "S3-Resource-Policy", env=env_US)

CustomSnsStack(app, "SnsStack", env=env_US)

CustomSqsStack(app, "SQSStack", env=env_US)

app.synth()
