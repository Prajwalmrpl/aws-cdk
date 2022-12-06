#Containerized Micro Service Architecture with ECS
from aws_cdk import core
from aws_cdk import aws_ec2 as _ec2
from aws_cdk import aws_ecs as _ecs
from aws_cdk import aws_ecs_patterns as _ecs_patterns


class ContainerizedMicroserviceArchitectureWithEcsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Create a VPC with CIDR 10.10.0.0/16 with max_azs=2 and 1 NAT Gateway and one public subnet and one private subnet
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
        #Create a ECS cluster
        micro_service_cluster = _ecs.Cluster(
            self,
            "webServiceCluster",
            vpc=vpc
        )

        #defining the ECS Cluster Capacity
        micro_service_cluster.add_capacity("microServicsAuto-scaling-group",
                                            instance_type= _ec2.InstanceType("t2.micro")
                                            )
        
        #deploy the container and attach a LoadBalancer
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