#!/usr/local/bin/python3

import sys
import urllib
import json
import boto3
import datetime
from datetime import datetime
import time
import os

datetimenow = str(datetime.now())

def get_queue_count():
    client = boto3.client('sqs', region_name='us-east-1')
    currentcount = client.get_queue_attributes(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs',
        AttributeNames=[
            'ApproximateNumberOfMessages',
        ]
    )['Attributes']['ApproximateNumberOfMessages']
    if int(currentcount) == 0:
        print("0 messages in the queue.")
    else:
        print(">0 messages in the queue.")
        check_sqs_queue()

def check_sqs_queue():
    client = boto3.client('sqs', region_name='us-east-1')
    req = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs',
        MessageAttributeNames=[
            'FileID',
            'Status',
            'Flow',
        ],
	WaitTimeSeconds=20,
        MaxNumberOfMessages=1
    )['Messages'][0]
    handle = req['ReceiptHandle']
    status = req['MessageAttributes']['Status']['StringValue']
    flow = req['MessageAttributes']['Flow']['StringValue']
    fileid = req['MessageAttributes']['FileID']['StringValue']
    if "dedupe" in status:
        print(handle)
        print(fileid)
        print(status)
        print(flow)
        delete_sqs_message(handle)
    else:
        print("No message exists like that.")

def delete_sqs_message(handle):
    client = boto3.client('sqs', region_name='us-east-1')
    req = client.delete_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs',
        ReceiptHandle=handle
    )

get_queue_count()
