This prject is deployed using AWS SAM and CircleCI.

CircleCI will take care of the deployment. For information on how it does it,
reading the file in `.circleci/config.yml` is likely to be the easiest thing 
to do.

This document explains the steps needed to create a new deployment in a new 
AWS account.

It borrows heavlly from https://github.com/DemocracyClub/aggregator-api/blob/master/docs/new-aws-account-setup.md

# IAM, deploy user

In the IAM console, create:

## Policy: DCWebsiteDeployer

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "apigateway:DELETE",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "cloudformation:CreateChangeSet",
                "cloudformation:DescribeChangeSet",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStacks",
                "cloudformation:ExecuteChangeSet",
                "cloudformation:GetTemplateSummary",
                "lambda:AddPermission",
                "lambda:CreateAlias",
                "lambda:CreateFunction",
                "lambda:DeleteAlias",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:GetFunctionConfiguration",
                "lambda:GetLayerVersion",
                "lambda:InvokeFunction",
                "lambda:ListTags",
                "lambda:ListVersionsByFunction",
                "lambda:PublishLayerVersion",
                "lambda:PublishVersion",
                "lambda:RemovePermission",
                "lambda:TagResource",
                "lambda:UntagResource",
                "lambda:UpdateAlias",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "logs:CreateLogGroup",
                "logs:PutRetentionPolicy",
                "s3:AbortMultipartUpload",
                "s3:GetObject",
                "s3:ListBucketMultipartUploads",
                "s3:ListMultipartUploadParts",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectTagging",
                "events:*"
            ],
            "Resource": [
                "arn:aws:apigateway:eu-west-2:*:/restapis",
                "arn:aws:apigateway:eu-west-2:*:/restapis/*",
                "arn:aws:cloudformation:eu-west-2:*:changeSet/samcli-deploy*/*",
                "arn:aws:cloudformation:eu-west-2:*:stack/dc-website-*/*",
                "arn:aws:cloudformation:eu-west-2:aws:transform/Serverless-2016-10-31",
                "arn:aws:lambda:eu-west-2:*:function:DCWebsite*",
                "arn:aws:lambda:eu-west-2:*:layer:DependenciesLayer",
                "arn:aws:lambda:eu-west-2:*:layer:DependenciesLayer:*",
                "arn:aws:logs:eu-west-2:*:log-group:/aws/lambda/dc-website-*",
                "arn:aws:logs:eu-west-2:*:log-group:/aws/lambda/DCWebsite*",
                "arn:aws:s3:::dc-website-deployment-artifacts-*",
                "arn:aws:s3:::dc-website-deployment-artifacts-*/*",
                "arn:aws:events:eu-west-2:*:rule/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ssm:*",
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": [
                "arn:aws:iam::*:role/DCWebsiteLambdaExecutionRole"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```


## Role: DCWebsiteLambdaExecutionRole

* Select the use-case creation shortcut for Lambda
* Attach the AWS-managed policy: AWSLambdaBasicExecutionRole

Tag the Role:

* dc-environment: as appropriate
* dc-product: dc-website

After creation, ensure the trust relationship looks like this:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```



## Group: DCWebsiteDeployers

During creation:

Attach the DC-managed policies:

* DCWebsiteDeployer

## User: CircleCI

Add an IAM User named CircleCI.

During creation:

* Select "Programmatic access" only.
* Add them to the group AggregatorApiDeployers
* Tag the user:
  * dc-environment: as appropriate
  * dc-product: aggregator-api

After creation, copy the generated access key ID and secret access key, and paste them inside an appropriately-named CircleCI "Context", with each value stored under its relevant standard AWS environment variable name.

Make very, very sure that you capture the key ID and secret precisely! Ensure that, when you paste it into the CircleCI UI, you don't accidentally insert any leading or trailing whitespace, and that you've copied the entire string each time - even if the string contains word-break characters that stop your browser from selecting the whole string!


# S3 buckets

### Deployment artifact bucket

In the [AWS S3 web UI](https://s3.console.aws.amazon.com/s3/home?region=eu-west-2), create an S3 bucket.

- Name: `dc-website-deployment-artifacts-<environment>-<several-random-characters>`
- Region: Wherever you're deploying the Aggregator API; probably eu-west-2
- Public access: entirely disabled
- Versioning: disabled
- Tags:
    - `dc-environment`: as appropriate
    - `dc-product`: `dc-website`
- Encryption: doesn't matter

After creation, view the bucket and select the "Management" tab.

Select "Create lifecycle rule".

- Rule name: `delete-any-file-1-day-after-upload`
- Apply to all objects
- Tick the options for:
    - "Expire current versions of objects"
    - "Delete expired delete markers or incomplete multipart uploads"
- For "Expire current versions of objects":
    - Enter "1" day
- For "Delete expired delete markers or incomplete multipart uploads":
    - Tick "Delete incomplete multipart uploads"
    - Enter "1" day

Create the rule.

## SAM config

* Create a file called `samconfig.toml.d/ci-<environment>.toml`
* Copy the values from another related file, making sure to use the name of 
  the newly created bucket and the right tags

## CircleCI

1. Set up a new context as per the existing naming convention there.
2. Add the credentials from the CircleCI user created above as:
   1. AWS_ACCESS_KEY_ID: from step above
   2. AWS_DEFAULT_REGION: `eu-west-2`
   3. AWS_SECRET_ACCESS_KEY: from step above
   4. SENTRY_AUTH_TOKEN: from sentry


# Cert 

Create a cert _in the `us-east-1` region. CloudFront needs a cert in that 
region to work. Make a note of the ARN for later.

## RDS

Set up an RDS / have a username and password for an RDS ready for the next step

## Parameter Store

Log in to the AWS console and go to the Parameter Store page.

Create enteries for each of:

* AppPostgresDatabaseName
* AppPostgresHost
* AppPostgresPassword
* AppSecretKey
* AppSentryDSN
* AppStorageBucketName
* CertificateArn
* FQDN
* STORAGE_BUCKET_NAME
