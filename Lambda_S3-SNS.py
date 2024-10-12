import json
import boto3

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Extract bucket name and uploaded file key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Message to be sent via SNS
    message = f"A new file has been uploaded to S3. Bucket: {bucket_name}, File: {file_key}"

    # SNS topic ARN
    sns_topic_arn = 'arn:aws:sns:ap-south-1:352276167689:S3-Lambda'

    # Publish message to SNS
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject="S3 File Upload Notification"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }