#Launch EC2 with latest AMI in any AWS Region - Portable Region Independent stack
from aws_cdk import (
    Stack, 
)
import aws_cdk as cdk
from constructs import Construct

from aws_cdk import aws_ssm as _ssm
from aws_cdk import aws_secretsmanager as _secretsmanager

import json


class CustomParametersSecretsStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create AWS secrets & SSM Parameters
        param1 = _ssm.StringParameter(
            self,
            "parameter1",
            description="Load Testing Configuration",
            parameter_name="NoOfConcurrentUsers",
            string_value="100",
            tier=_ssm.ParameterTier.STANDARD
        )

        secret1 = _secretsmanager.Secret(self,
                                         "secret1",
                                         description="Customer DB password",
                                         secret_name="cust_db_pass"
                                         )

        templated_secret = _secretsmanager.Secret(self,
                                                  "secret2",
                                                  description="A Templated secret for user data",
                                                  secret_name="user_kon_attributes",
                                                  generate_secret_string=_secretsmanager.SecretStringGenerator(
                                                      secret_string_template=json.dumps(
                                                          {"username": "praj"}
                                                      ),
                                                      generate_string_key="password"
                                                  )
                                                  )

        output_2 = cdk.CfnOutput(self,
                                  "secret1Value",
                                  description="secret1",
                                  value=f"{secret1.secret_value}"
                                  )