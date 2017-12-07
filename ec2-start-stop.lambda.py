#!/usr/bin/env python3

import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    try:
        instance_id = event['instance_id']
        action = event['action']
        assert(action in ['start', 'stop'])
    except:
        print('ERROR: Expecting JSON input: { "instance_id": "${Instance}", "action": "start/stop" }')
        raise
        return

    print("%s instance %s" % (instance_id, action))
