# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.res_session2_fa import ResSession2FA  # noqa: E501
from openapi_client.rest import ApiException

class TestResSession2FA(unittest.TestCase):
    """ResSession2FA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResSession2FA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.res_session2_fa.ResSession2FA()  # noqa: E501
        if include_optional :
            return ResSession2FA(
                userId = '0', 
                clientCode = '0', 
                clientName = '0', 
                emailId = '0', 
                phoneNo = '0', 
                enabledSegments = [
                    '0'
                    ], 
                enabledProducts = [
                    '0'
                    ], 
                sessionToken = '0', 
                publicToken = '0', 
                loginTime = 56
            )
        else :
            return ResSession2FA(
        )

    def testResSession2FA(self):
        """Test ResSession2FA"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
