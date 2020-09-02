# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.trades import Trades  # noqa: E501
from openapi_client.rest import ApiException

class TestTrades(unittest.TestCase):
    """Trades unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Trades
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.trades.Trades()  # noqa: E501
        if include_optional :
            return Trades(
                tradeId = 1.337, 
                orderId = '0', 
                exchangeTradeId = '0', 
                instrumentName = '0', 
                instrumentToken = '0', 
                exchange = 'NSE', 
                price = 1.337, 
                quantity = 56, 
                transactionType = 'BUY', 
                product = 'NORMAL', 
                orderTimestamp = '0', 
                tradeTimestamp = '0'
            )
        else :
            return Trades(
        )

    def testTrades(self):
        """Test Trades"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
