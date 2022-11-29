from aws_cdk import core
from aws_cdk import aws_rds as _rds
from aws_cdk import aws_ec2 as _ec2


class RdsDatabase3TierStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, asg_security_groups, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)