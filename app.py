#!/usr/bin/env python3
import os

import aws_cdk as cdk

from demo_cdk.demo_cdk_stack import DemoCdkStack
from resource_stacks.custom_vpc import CustomVpcStack


app = cdk.App()

#env_US = cdk.Environment(account="934767487632",region="us-east-1")
#env_Mumbai = cdk.Environment(acccount="92376452763671",region="ap-south-1")

#DemoCdkStack(app, "Stack1", )
#DemoCdkStack(app, "Stack2", env=env_Mumbai)
CustomVpcStack(app, "CustomVPCStack" )



app.synth()
