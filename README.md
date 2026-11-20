
# Cloud Security Incident Response

## Project Overview

This project demonstrates a cloud security incident response
system that detects suspicious AWS activities and helps
remediate common cloud security misconfigurations.

## Technologies Used

- Python
- AWS Lambda
- AWS CloudFormation
- Amazon S3
- Amazon SNS
- Amazon EventBridge
- Boto3
- Python Unittest

## Main Features

1. Detect suspicious AWS API activities.
2. Send security alerts using Amazon SNS.
3. Remediate public S3 access configurations.
4. Remediate overly permissive Security Groups.
5. Provide manual incident response procedures.
6. Follow the NIST Incident Response Lifecycle.

## Project Structure

```text
Cloud-Security-Incident-Response/
│
├── cloudformation/
│   └── security_stack.yaml
│
├── lambda_functions/
│   ├── alert_handler.py
│   ├── s3_remediation.py
│   └── security_group_remediation.py
│
├── runbook/
│   └── incident_response_runbook.md
│
├── test/
│   ├── test_s3.py
│   └── test_security_group.py
│
├── screenshots/
├── requirements.txt
└── README.md
```

## Installation

1. Install Python.
2. Create a virtual environment.
3. Activate the virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
python -m unittest discover -s test -v
```

## Testing Status

Local unit tests are used to verify input validation
and error handling.

## Disclaimer

This project is developed for educational purposes.
Deploy and test only in a controlled AWS environment.
Do not use real sensitive data.
