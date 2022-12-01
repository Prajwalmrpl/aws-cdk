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
from serverless_stacks.custom_apigw import CustomApiGatewayStack
from serverless_stacks.custom_privileges_to_lambda import CustomPrivilegesToLambdaStack

from stacks_from_cfn.stack_from_existing_cfn_template import StackFromCloudformationTemplate

from cw_monitoring_stacks.ec2_with_alarams import CustomEc2WithAlarmsStack
from cw_monitoring_stacks.cloudwatch_dashboard import CustomCloudwatchLiveDashboardStack


from app_db_stack.vpc_3tier_stack import Vpc3TierStack
from app_db_stack.web_server_3tier_stack import WebServer3TierStack
from app_db_stack.rds_3tier_stack import RdsDatabase3TierStack


from files.deploy_static_site import DeployStaticSiteStack
from files.cf_oai_static import DeployCloudfrontOaiStaticSiteStack
from files.serverless_event_with_s3 import ServerlessEventProcessorArchitectureWithS3EventsStack
from files.serverless_rest_api_architecture import ServerlessRestApiArchitectureStack

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

#CustomLambdaSrcFromS3Stack(app, "CustomLambdaSrcFromS3Stack", env=env_US)

#CustomLambdaAsCronStack(app, "CustomLambdaAsCronStack", env=env_US)

#StackFromCloudformationTemplate(app, "StackFromCloudformationTemplate", env=env_US)

#CustomEc2WithAlarmsStack(app, "CustomEC2WithAlaramsStack", env=env_US)

#DeployStaticSiteStack(app, "DeployStaticSiteStack", env=env_US)



"""vpc_3tier_stack = Vpc3TierStack(app, "multi-tier-app-vpc-stack")
app_3tier_stack = WebServer3TierStack(
     app, "multi-tier-app-web-server-stack", vpc=vpc_3tier_stack.vpc)
db_3tier_stack = RdsDatabase3TierStack(
     app,
     "multi-tier-app-db-stack",
     vpc=vpc_3tier_stack.vpc,
     asg_security_groups=app_3tier_stack.web_server_asg.connections.security_groups,
     description="Create Custom RDS Database"
 )"""

#CustomApiGatewayStack(app, "CustomApiGatewayStack", env=env_US)

#CustomPrivilegesToLambdaStack(app, "CustomPrivilegesToLambdaStack", env=env_US)

#CustomCloudwatchLiveDashboardStack(app, "CustomCloudwatchLiveDashboardStack", env=env_US)

#dp_stack=DeployCloudfrontOaiStaticSiteStack(app, "DeployCloudfrontOaiStaticSiteStack", env=env_US, description="Stack for DeployCloudfrontOaiStaticSiteStack")
#cdk.Tags.of(dp_stack).add("Name", "DeployCloudfrontOaiStaticSiteStack")

#se_stack=ServerlessEventProcessorArchitectureWithS3EventsStack(app, "ServerlessEventProcessorArchitectureWithS3EventsStack", env=env_US, description="Stack for ServerlessEventProcessorArchitectureWithS3EventsStack")
#cdk.Tags.of(dp_stack).add("Name", "ServerlessEventProcessorArchitectureWithS3EventsStack")

#serv_event = ServerlessEventProcessorArchitectureWithS3EventsStack(app, "Serverless-Event-Process-Architecture-With-S3-Events", env=env_US)
#cdk.Tags.of(serv_event).add("Name", "Serverless-Architcture-With-S3-Events")


rest_api=ServerlessRestApiArchitectureStack(app, "ServerlessRestApiArchitectureStack", env=env_US, description="Stack for ServerlessRestApiArchitectureStack")
cdk.Tags.of(rest_api).add("Name", "ServerlessRestApiArchitectureStack")

app.synth()
