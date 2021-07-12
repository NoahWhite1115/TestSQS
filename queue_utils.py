import boto3
from botocore.exceptions import ClientError
import logging

sqs = boto3.resource('sqs')
logger = logging.getLogger(__name__)

def get_queue(name):
    try:
        queue = sqs.get_queue_by_name(QueueName=name)
        logger.info("Got queue '%s' with URL=%s", name, queue.url)
    except ClientError as error:
        logger.exception("Couldn't get queue named %s.", name)
        raise error
    else:
        return queue

def send_to_queue(queue, messageBody, messageKeys = None):
    if not messageKeys:
        messageKeys = {}

    try:
        response = queue.send_message(
            MessageBody=messageBody,
            MessageAttributes=messageKeys
        )
    except ClientError as error:
        logger.exception("Send message failed: %s", messageBody)
        raise error
    else:
        return response