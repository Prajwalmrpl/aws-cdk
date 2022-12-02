import aws_cdk as cdk 
from aws_cdk import Stack
import constructs as Construct
from aws_cdk import aws_ec2 as _ec2
from aws_cdk import aws_ecs as _ecs
from aws_cdk import aws_ecs_patterns as _ecs_patterns


class ContainerizedMicroserviceArchitectureWithEcsStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Add the Stack 
        #Careate a VPC
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
                    name="app", cidr_mask=24, subnet_type=_ec2.SubnetType.PRIVATE_ISOLATED
                ),
               
            ]
        )

        micro_service_cluster = _ecs.Cluster(
            self,
            "webServiceCluster",
            vpc=vpc
        )

        #defining ECS Cluster Capacity
        micro_service_cluster.add_capacity("microServicsAuto-scaling-group",
                                            instance_type= _ec2.InstanceType("t2.micro")
                                            )
        
        #deploy container and attach a LoadBalancer
        load_balancer_ws = _ecs_patterns.ApplicationLoadBalancedEc2Service(
            self,
            "webService",
            cluster= micro_service_cluster,
            memory_reservation_mib= 512,
            task_image_options={
                "image": _ecs.ContainerImage.from_registry("mystique/web-server"),
                "environment": {
                    "ENVIRONEMNT": "PROD"
                }
            }
        )

        #output web service url
        output_1 = cdk.CfnOutput(
            self,
            "webServerUrl",
            value=f"{load_balancer_ws.load_balancer.load_balancer_dns_name}"
        ) 

       