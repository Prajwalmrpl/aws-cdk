from aws_cdk import core
from aws_cdk import aws_rds as rds
from aws_cdk import aws_ec2 as ec2


class RdsDatabase3TierStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, asg_security_groups, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #create an RDS Database
        rds_db = rds.DatabaseInstance(self,
                                        "newrdsdb",
                                        master_username="rdsdb",
                                        database_name="newrdsdb",
                                        engine= rds.DatabaseInstanceEngine.MYSQL,
                                        vpc=vpc,
                                        port=3306,
                                        allocated_storage=30,
                                        multi_az=False,
                                        
                                        )

