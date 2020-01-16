#!/usr/local/bin/python3

import boto3

sqs = boto3.resource('sqs', region_name='us-east-1')
queue = sqs.get_queue_by_name(QueueName='learn-sqs')

# Create a new message
response = queue.send_message(MessageBody='File Ready', MessageAttributes={
    'FileID': {
        'StringValue': '45d4d49a15f043f4181c550f6020a0e2',
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
