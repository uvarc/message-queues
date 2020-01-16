#!/usr/local/bin/python3

import sys
import urllib
import json
import boto3
import datetime
from datetime import datetime
import time
import os

""" 
Membership File Processing - Step 4 - Prepare for Catalist SUBMIT API call
Neal Magee <neal.magee@seiu.org>
v.1.0
-------------------------------------------------------------------------------
This collection of methods does the following:
 - checks an SQS queue for active messages (>0 or not?)
 - reads an SQS message when there is 1 or more in queue
 - generates an expiring signed URL for the membership file in S3
 - base64 encodes that URL
 - assembles the full Catalist API call
 - makes the Catalist API call based on the assembled URI
 - updates the MSSQL table accordingly
 - generates an SQS message for the next step of the process
 - deletes the SQS message it acted upon
 - LOGS each step with FileID appended
 - EXCEPTION handling where applicable - with option for SNS push
"""

# Global variables
fileid=""
status=""
flow=""
handle=""
datetimenow = str(datetime.now())

# CHECK QUEUE FOR FILES TO BE UPLOADED TO CATALIST
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
    global handle, status, fileid, flow
    handle = req['ReceiptHandle']
    status = req['MessageAttributes']['Status']['StringValue']
    flow = req['MessageAttributes']['Flow']['StringValue']
    fileid = req['MessageAttributes']['FileID']['StringValue']
    if "dedupe" in status:
        print(handle)
        print(fileid)
        print(status)
        print(flow)
        # print("The Receipt Handle is: ") handle
        # print("The Message Status is: %s") % (status)
        # print("The File ID is: %s") % (fileid)
        # print("The Flow is: %s") % (flow)
        delete_sqs_message(handle)
    else:
        print("No message exists with a status of GOOD")

def delete_sqs_message(handle):
    client = boto3.client('sqs', region_name='us-east-1')
    req = client.delete_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs',
        ReceiptHandle=handle
    )

get_queue_count()

