# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.stocks import Stocks  # noqa: E501
from openapi_client.rest import ApiException

class TestStocks(unittest.TestCase):
    """Stocks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Stocks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.stocks.Stocks()  # noqa: E501
        if include_optional :
            return Stocks(
                instrumentToken = 56, 
                normal = 1.337, 
                supermultiple = 1.337, 
                mtf = 1.337
            )
        else :
            return Stocks(
        )

    def testStocks(self):
        """Test Stocks"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
