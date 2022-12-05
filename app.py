#!/usr/bin/env python3
import os

import aws_cdk as cdk

from day_8.day_8_stack import Day8Stack
from day_8.s3_with_cloudfront import DeployCloudfrontOaiStaticSiteStack
from day_8.static_with_contents import DeployStaticSiteStack


app = cdk.App()
Day8Stack(app, "Day8Stack",)

DeployCloudfrontOaiStaticSiteStack(app, "DeployCloudfrontOaiStaticSiteStack", description="Stack to DeployCloudfrontOaiStaticSiteStack")

DeployStaticSiteStack(app, "DeployStaticSiteStack", description="Stack for DeployStaticSiteStack")

app.synth()
