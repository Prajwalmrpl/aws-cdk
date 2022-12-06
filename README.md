1.CDK Tokens: How to Export/Import Stack Values | Cfn Intrinsic Functions.

2.infrastructure-Is-Code: Version control your Infrastructure.
	
	With the AWS CDK, developers or administrators can define their cloud infrastructure by using a supported programming language. CDK applications 
	should be organized into logical units, such as API, database, and monitoring resources, and optionally have a pipeline for automated deployments. The 	logical units should be
    implemented as constructs including the following:

* Infrastructure (such as Amazon S3 buckets, Amazon RDS databases, or an Amazon VPC network)
* Runtime code (such as AWS Lambda functions)
* Configuration code
Stacks define the deployment model of these logical units.
At deployment time, the AWS CDK synthesizes a cloud assembly that contains the following:
* AWS CloudFormation templates that describe your infrastructure in all target environments
* File assets that contain your runtime code and their supporting file.

With the CDK, every commit in your application's main version control branch can represent a complete, consistent, deployable version of your application.
Application can then be deployed automatically whenever a change is made.

3.Opt-Out from CDK Metadata Version Reporting.

To shave off a couple of lines from our CloudFormation templates, we can opt of our metadata reporting.
Metadata is used by the CDK team in order to collect analytics in regards to how developers use the CDK service.

If we want to disable version reporting for all commands we issue on the CDK app level, we can edit the contents of our cdk.json file and set the versionReporting key to false:
After that if u check the contents of the CloudFormation template in the cdk.out directory, we can see that the CDKMetadata section has been removed:
Also if we issue the cdk synth command we won't see the CDKMetadata section anymore:
Turn off Metadata for a single command:

We can also opt out of metadata reporting for a single command, by adding the --no-version-reporting flag to the cdk deploy command:
— cdk --no-version-reporting deploy
By taking the --no-version-reporting flag approach you would have to include the flag every time you issue a synth or deploy command, so the versionReporting boolean in the cdk.json file is the more convenient option.

4.CDK Stacks: Resources & Reusability.
* Mix all of it into a single construct or stack.
* Separate the resources into constructs of their own.
*  Remove hardcoded values in constructs.
* Make constructs generic and put them in a repo.
 U can also use Reuse a parent CDK Stack in other Application:
* Create root stack
	Create a core root stack containing the common resources you want the customer stacks to use. You will need the arn/name of the resources you want to have access to in your customer stacks. One way is to use CfnOutput to write to the cdk.context.json file.
* Create Custom root stack
	For each customer you would have something such as a customerRootStack which defines the root resources that you already created - since you don't want to overwrite/recreate you will want to create them using the existing ARN/name.

5.DTAP in CDK: Multi-Environment Deployment.
	we can deploy the stack into multiple environment.
	in app.py mention the cdk.Environment and multi regions to deploy the stack.

	env_US = cdk.Environment(region="us-east-1")
	env_Mumbai = cdk.Environment(region="ap-south-1")

	CdkStack(app, "Stack1”, env=env_US)
	CdkStack(app, "Stack2", env=env_Mumbai)

6.Deploying stacks to Multiple AWS Regions & Accounts: Best Practice.
	to deploy the stack into multi AWS regions and specified account no in app.py
	if we not mentioned the region and account in stack it will take the default account and deploy the stack in the default account.
	now the stack will bind to specified account and specified region.
	env_US = cdk.Environment(account="934767487632",region="us-east-1")
	env_Mumbai = cdk.Environment(acccount="92376452763671",region="ap-south-1")

	DemoCdkStack(app, "Stack1", env=env_US)
	DemoCdkStack(app, "Stack2", env=env_Mumbai)