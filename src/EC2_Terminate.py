import boto3
import sys


def terminate_ec2():
    # get the response through describe and get the instance id into an array
    instance_id = []
    client_ec2 = boto3.client('ec2')
    response = client_ec2.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            instance_id.append(i['InstanceId'])

    client_ec2.terminate_instances(InstanceIds=instance_id)


terminate_ec2()
