import aws_cdk as cdk 
from aws_cdk import Stack
import constructs as Construct 
from aws_cdk import aws_ecs as _ecs
from aws_cdk import aws_ec2 as _ec2 
from aws_cdk import aws_ecs_patterns as _ecs_patterns
from aws_cdk import aws_lambda as _lambda
from aws_cdk.aws_applicationautoscaling import Schedule


class ServerlessBatchProcessorArchitectureWithFargateStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #create resources
        #create a vpc
        vpc = _ec2.Vpc(
            self,
            "customVpcId",
            cidr="10.10.0.0/16",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                _ec2.SubnetConfiguration(
                    name="public", cidr_mask=24, subnet_type=_ec2.SubnetType.PUBLIC
                ),
                _ec2.SubnetConfiguration(
                    name="app", cidr_mask=24, subnet_type= _ec2.SubnetType.PRIVATE_ISOLATED
                ),
               
            ]
        )

        #Create a Fargate Cluster
        batch_process_cluster = _ecs.Cluster(self,
                                            "batchProcessorID",
                                            vpc=vpc
                                            )

        #deploy batch processing container stack in Fargate with cloudwatch Event shedule
        batch_processor_task = _ecs_patterns.ScheduledFargateTask(
            self,
            "fargatedID",
            cluster = batch_process_cluster,
            scheduled_fargate_task_definition_options={
                "image": _ecs.ContainerImage.from_registry("mystique/batch-job-runner"),
                "memory_limit_mib": 512,
                "cpu": 256,
                "environment": {
                    "name": "TRIGGEr",
                    "value": "CloudWatch Events"
                }
            },
            schedule=Schedule.expression("rate(2 minutes)")
        )
