#!/usr/bin/env python3

import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    print("event: ", event)
    print("context: ", context)
