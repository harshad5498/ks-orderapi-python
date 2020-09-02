# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.codcancel import Codcancel  # noqa: E501
from openapi_client.rest import ApiException

class TestCodcancel(unittest.TestCase):
    """Codcancel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Codcancel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.codcancel.Codcancel()  # noqa: E501
        if include_optional :
            return Codcancel(
                orderNo = '0'
            )
        else :
            return Codcancel(
        )

    def testCodcancel(self):
        """Test Codcancel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
