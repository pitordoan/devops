#!/usr/bin/python

#Use this script to create EC2 instances.
#Make sure to install pip and use pip to install boto3 first before running this script.

import boto3
from datetime import datetime

def create_ec2_instance(tag_name, volume_size, userdata_file=None, sync=True):
    userdata = ''

    if userdata_file:
        with open(userdata_file, 'r') as f:
            userdata = ''.join(f.readlines())

    client = boto3.client('ec2')

    response = client.run_instances(
        DryRun=False,
        ImageId='ami-8ca83fec',
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[
            'sg-3640824d',
        ],
        UserData=userdata,
        InstanceType='t2.micro',
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'VolumeSize': volume_size, #GiB
                },
            },
        ],
        Monitoring={
            'Enabled': True
        },
        SubnetId='subnet-399e1370',
        DisableApiTermination=False,
        InstanceInitiatedShutdownBehavior='stop',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': tag_name
                    },
                ]
            },
        ]
    )

    #id of the newly created instance
    instance_id = response['Instances'][0]['InstanceId']

    #wait for the instance to by ready (Status Checks = 2/2 checks passed)
    if sync:
        waiter = client.get_waiter('instance_status_ok')
        waiter.wait(
            InstanceIds=[
                instance_id,
            ]
        )

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)

    return instance

#----------- main -----------
if __name__ == "__main__":
    instance = create_ec2_instance(tag_name='app01', volume_size=20, userdata_file='ec2_userdata.sh')
    print str(datetime.now()) + ' - Instance created, private IP: ' + instance.private_ip_address