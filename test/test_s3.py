
import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "lambda_functions")
    )
)

from s3_remediation import lambda_handler


class TestS3Remediation(unittest.TestCase):

    def test_missing_bucket_name(self):
        response = lambda_handler({}, None)

        self.assertEqual(response["statusCode"], 400)
        self.assertEqual(response["body"], "Bucket name is required")


if __name__ == "__main__":
    unittest.main()
