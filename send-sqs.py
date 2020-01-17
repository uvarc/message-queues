#!/usr/local/bin/python3

import boto3
import uuid

sqs = boto3.resource('sqs', region_name='us-east-1')
queue = sqs.get_queue_by_name(QueueName='learn-sqs')

randomval = uuid.uuid4().hex

# Create a new message
response = queue.send_message(MessageBody='File Ready', MessageAttributes={
    'FileID': {
        'StringValue': randomval,
        'DataType': 'String'
    },
    'Status': {
        'StringValue': 'dedupe',
        'DataType': 'String'
    },
    'Flow': {
        'StringValue': '1',
        'DataType': 'String'
    },
})

print(response)
