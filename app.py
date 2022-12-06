#!/usr/bin/env python3
import os

import aws_cdk as cdk

from day_7.day_7_stack import Day7Stack

app = cdk.App()
Day8Stack(app, "Day8Stack",)

app.synth()
