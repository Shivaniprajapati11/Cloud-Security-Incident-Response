
import json
import os
import boto3

sns = boto3.client("sns")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")


def lambda_handler(event, context):
    detail = event.get("detail", {})

    event_name = detail.get("eventName", "Unknown")
    username = detail.get("userIdentity", {}).get(
        "userName", "Unknown"
    )

    suspicious_events = [
        "PutBucketPolicy",
        "PutBucketAcl",
        "AuthorizeSecurityGroupIngress",
        "CreateAccessKey",
        "ConsoleLogin"
    ]

    if event_name in suspicious_events:
        message = {
            "alert": "Suspicious AWS API activity detected",
            "event": event_name,
            "user": username,
            "severity": "HIGH"
        }

        print(json.dumps(message, indent=4))

        if SNS_TOPIC_ARN:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="AWS Security Alert",
                Message=json.dumps(message, indent=4)
            )

        return {
            "statusCode": 200,
            "body": "Security alert processed"
        }

    return {
        "statusCode": 200,
        "body": "No suspicious activity detected"
    }
