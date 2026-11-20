
import json
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

DANGEROUS_PORTS = [22, 3389]


def lambda_handler(event, context):
    security_group_id = event.get("security_group_id")

    if not security_group_id:
        return {
            "statusCode": 400,
            "body": "Security Group ID is required"
        }

    try:
        response = ec2.describe_security_groups(
            GroupIds=[security_group_id]
        )

        removed_rules = []

        for group in response["SecurityGroups"]:
            for rule in group.get("IpPermissions", []):
                from_port = rule.get("FromPort")
                to_port = rule.get("ToPort")

                if from_port not in DANGEROUS_PORTS:
                    continue

                if to_port != from_port:
                    continue

                public_ranges = [
                    item for item in rule.get("IpRanges", [])
                    if item.get("CidrIp") == "0.0.0.0/0"
                ]

                if not public_ranges:
                    continue

                permission = {
                    "IpProtocol": rule["IpProtocol"],
                    "FromPort": from_port,
                    "ToPort": to_port,
                    "IpRanges": public_ranges
                }

                ec2.revoke_security_group_ingress(
                    GroupId=security_group_id,
                    IpPermissions=[permission]
                )

                removed_rules.append(from_port)

        print("Removed public rules:", removed_rules)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Security Group check completed",
                "security_group": security_group_id,
                "removed_ports": removed_rules
            })
        }

    except Exception as error:
        print("Remediation failed:", str(error))

        return {
            "statusCode": 500,
            "body": str(error)
        }
