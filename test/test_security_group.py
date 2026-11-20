
import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "lambda_functions")
    )
)

from security_group_remediation import lambda_handler


class TestSecurityGroupRemediation(unittest.TestCase):

    def test_missing_security_group_id(self):
        response = lambda_handler({}, None)

        self.assertEqual(response["statusCode"], 400)
        self.assertEqual(response["body"], "Security Group ID is required")


if __name__ == "__main__":
    unittest.main()