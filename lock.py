import json

import boto3
import urllib.request


def lambda_handler(event, context):
   # ec2_client = boto3.client('ec2', region_name='us-east-1')
    ssm_client = boto3.client('ssm', region_name='us-east-1')
    #client = boto3.client('ssm')
    
    params={"commands":["usermod -L vimal"],"workingDirectory":["/tmp"],"executionTimeout":["3600"]}
    response = ssm_client.send_command(DocumentName="AWS-RunShellScript", InstanceIds=["i-099a78dc409ef9bf7"],Comment='logging the', TimeoutSeconds=600, Parameters=params)
    
    print(response)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('User Locked !')
    }

