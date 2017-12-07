#!/usr/bin/env python3

# Very simple EC2 Start/Stop lambda function.
# Author: Michael Ludvig @ aws.nz
#
# Expects 'event' input in JSON format:
# {
#    "instance_id": "i-1234567890abcdefgh",
#    "action": "start" (or "stop")
# }
#
# Best to call from AWS CloudWatch Events scheduler rule

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    try:
        instance_id = event['instance_id']
        action = event['action']
        assert(action in ['start', 'stop'])
    except:
        print('ERROR: Expecting JSON input: { "instance_id": "${Instance}", "action": "start/stop" }')
        raise
        return

    print("%s instance %s" % (instance_id, action))
