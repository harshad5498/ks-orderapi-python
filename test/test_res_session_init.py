# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.res_session_init import ResSessionInit  # noqa: E501
from openapi_client.rest import ApiException

class TestResSessionInit(unittest.TestCase):
    """ResSessionInit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResSessionInit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.res_session_init.ResSessionInit()  # noqa: E501
        if include_optional :
            return ResSessionInit(
                encryption = openapi_client.models.res_session_init_encryption.ResSessionInit_encryption(
                    type = 'PLAIN', 
                    publick_key = '0', 
                    key_size = 56, ), 
                redirect = openapi_client.models.res_session_init_redirect.ResSessionInit_redirect(
                    host = '0', 
                    key_size = 56, ), 
                weblink = openapi_client.models.res_session_init_weblink.ResSessionInit_weblink(
                    host = '0', 
                    key_size = 56, ), 
                message = '0', 
                userType = 'G', 
                status = 'Inactive'
            )
        else :
            return ResSessionInit(
        )

    def testResSessionInit(self):
        """Test ResSessionInit"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
