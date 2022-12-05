#!/usr/bin/env python3
import os

import aws_cdk as cdk

from day_7.day_7_stack import Day7Stack
from day_7.ec2_with_alaram import CustomEc2WithAlarmsStack
from day_7.cw_metrics import CustomEc2WithAlarmsStack
from day_7.cw_live_dashboard import CustomCloudwatchLiveDashboardStack


app = cdk.App()
Day8Stack(app, "Day8Stack",)

deploy_cloud_st = DeployCloudfrontOaiStaticSiteStack(app, "DeployCloudfrontOaiStaticSiteStack", description="Stack to DeployCloudfrontOaiStaticSiteStack")
cdk.Tags.of(deploy_cloud_st).add("Name", "CfnStack")

DeployStaticSiteStack(app, "DeployStaticSiteStack", description="Stack for DeployStaticSiteStack")

app.synth()
