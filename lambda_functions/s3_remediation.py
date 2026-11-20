
import json
import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

def lambda_handler(event, context):
    bucket_name = event.get("bucket_name")

    if not bucket_name:
        return {
            "statusCode": 400,
            "body": "Bucket name is required"
        }

    try:
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": True,
                "IgnorePublicAcls": True,
                "BlockPublicPolicy": True,
                "RestrictPublicBuckets": True
            }
        )

        print(f"Public access blocked for: {bucket_name}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "S3 public access blocked successfully",
                "bucket": bucket_name
            })
        }

    except Exception as error:
        print(f"Remediation failed: {error}")

        return {
            "statusCode": 500,
            "body": str(error)
        }
