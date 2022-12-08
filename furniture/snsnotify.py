import logging
import boto3
from botocore.exceptions import ClientError


''' a simple class to demonstrate how to publish messages using the SNS service'''

class Publisher:

    '''
        SNS demo: application-to-application communication
        
         publish a message to a given SNS topic
        
        :param my_message: the message to be sent
        :param mobile: the phone number to which you want to deliver an SMS message.
    '''
    def publish_message(self, topic_name, my_message, email_id):
        
        try:
           sns_client = boto3.client('sns')
           print('\npublishing the message {} to the SNS topic {}...\n'.format(my_message, topic_name))
           # recall that if the topic already exists, the create_topic() method returns that topic's ARN
           response = sns_client.create_topic(Name=topic_name)
           topic_arn = response['TopicArn']
           sns_client.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=email_id)
        
           response = sns_client.publish(TopicArn=topic_arn, Message=my_message)    
           print(response)
            
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
        
        
