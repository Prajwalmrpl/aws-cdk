#!/usr/bin/env python3
import os

import aws_cdk as cdk

from day_7.day_7_stack import Day7Stack

app = cdk.App()
dy_st = Day8Stack(app, "Day8Stack",)

#Add Tags to CDK Resources On Creation
cdk.Tags.of(dy_st).add("Environment", "Production")

#Deploying stacks to Multiple AWS Regions & Accounts: Best Practice.
env_US = cdk.Environment(account="923407756913",region="us-east-1")
env_Mumbai = cdk.Environment(account="923407756913",region="ap-south-1")

#DTAP in CDK: Multi-Environment Deployment.
env_US = cdk.Environment(region="us-east-1")
env_Mumbai = cdk.Environment(region="ap-south-1")

CdkStack(app, "Stack1”, env=env_US)
CdkStack(app, "Stack2", env=env_Mumbai)

app.synth()
