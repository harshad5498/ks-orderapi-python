# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.history import History  # noqa: E501
from openapi_client.rest import ApiException

class TestHistory(unittest.TestCase):
    """History unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test History
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.history.History()  # noqa: E501
        if include_optional :
            return History(
                version = 56, 
                orderQuantity = 56, 
                price = 1.337, 
                filledQuantity = 56, 
                exchangeStatus = '0', 
                status = 'placed', 
                disclosedQuantity = 56, 
                triggerPrice = 1.337, 
                validity = 'GFD', 
                exchOrderId = '0', 
                exchTradeId = '0', 
                message = '0', 
                activityTimestamp = '0'
            )
        else :
            return History(
        )

    def testHistory(self):
        """Test History"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
