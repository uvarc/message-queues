# Amazon SQS

- Install the `awscli` - `pip install awscli`.
- Install the `boto3` library for Python3.
- Determine either the name or the URL of the SQS queue you want to use.

## Python3

* Send messages (with attributes) - [`send-sqs.py`](send-sqs.py)
* Get 1 message (with attributes) - [`get-sqs.py`](get-sqs.py)

## Command Line

### Simple Message with Body

    aws sqs send-message \
      --queue-url https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs \
      --message-body "blah blah blah" \

    aws sqs receive-message \
      --queue-url https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs

### Message with Attributes

    aws sqs send-message \
      --queue-url https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs \
      --message-body "blah blah blah" \
      --message-attributes '{"firstAttribute":{"DataType":"String","StringValue":"hello world"},"secondAttribute":{"DataType":"String","StringValue":"goodbye world"}}'

    aws sqs receive-message \
      --queue-url https://sqs.us-east-1.amazonaws.com/474683445819/learn-sqs \
      --attribute-names "All"
