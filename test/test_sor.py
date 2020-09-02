# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.sor import Sor  # noqa: E501
from openapi_client.rest import ApiException

class TestSor(unittest.TestCase):
    """Sor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Sor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.sor.Sor()  # noqa: E501
        if include_optional :
            return Sor(
                price = 1.337, 
                quantity = 1.337, 
                mesage = '0', 
                orderId = '0'
            )
        else :
            return Sor(
        )

    def testSor(self):
        """Test Sor"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
