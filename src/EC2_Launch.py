import boto3
import sys


def check_connection():
    try:
        client_ec2 = boto3.client('ec2')
        response = client_ec2.describe_instances()
        assert isinstance(response, object)
        print(response)
    except:
        print("connection failed")


def launch_ec2():
    # Launch  Instances of various types using boto3
    instance_types = {'ami-07d0cf3af28718ef8': 't2.micro', 'ami-04ca2d0801450d495': 't2.micro'}
    client_ec2 = boto3.client('ec2')
    for instance, instance_type in instance_types.items():
        client_ec2.run_instances(ImageId=instance, InstanceType=instance_type, MinCount=1, MaxCount=1)
    # Get the  Instances ID which were running in ec2
    print(client_ec2.describe_instances())


def main():
    check_connection()
    launch_ec2()


if __name__ == "__main__":
    check_connection()
    launch_ec2()
