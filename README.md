1.Customize Stack Parameters: CDK Context variables.

	context variables are the variable which can be set either at compile time or runtime.
	it can be changed and allows variables which would otherwise be hardcoded to be more dynamic.
	create a json payload in cdk.json and store the values in cdk.json.
	“context”: {
		“env1”: {
			“region”: “ap-south-1”,
			“account”: “983674826464”
		},
		“env2”: {
			“region”: “us-east-1”,
			“account”: “934782983749”
		}
	We can access the context variables in stack.py 
	Using : self.node.try_get_context(‘env-1’)[‘region’]
	
	In app.py:
	env_US = cdk.Environment(account=app.node.try_get_context(‘env1’)[‘account’])
	env_Mumbai = cdk.Environment(account=app.node.try_get_context(‘env2’)[‘account’])

2.Build Multi-AZ Production Ready Custom VPC.

    # create a custom vpc with the configuration CIDR-10.83.0.0/20 wit azs=2 and one NAT Gateway and subnet configuration of public and private subnets.
	t_name="customVpcId")

	the above stack will create a vpc with the configuration cidr block: 10.83.0.0/20, in two availability zones and one nat gateway for public access to the 		internet with the subnet configuration with one one public subnet and one private subnet.

3.Add Tags to CDK Resources On Creation.

	Tags are key - value pairs we attach on AWS resources to easier distinguish and filter between them.
	In AWS CDK we can add tags to constructs. By default, when we tag a construct, the tag is automatically applied to all of the construct's children 	that are taggable.

	cdk.Tags.of(stack).add(“Environment”, “Production”)

4.Import Pre-Existing External Resources: S3, VPC.

    # Resource in same account.
    # import the S3 bucket from the same account using the bucket_name
    # import the S3 bucket from CrossAccount using bucket ARN
    #import existing VPC from the same account and same region using VPC-ID
    # Create VPC Peering to connect between 2 VPC's imported vpc and the custom vpc
        