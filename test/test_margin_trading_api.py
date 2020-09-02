# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.margin_trading_api import MarginTradingApi  # noqa: E501
from openapi_client.rest import ApiException


class TestMarginTradingApi(unittest.TestCase):
    """MarginTradingApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.margin_trading_api.MarginTradingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_mtf_order(self):
        """Test case for cancel_mtf_order

        Cancel an order  # noqa: E501
        """
        pass

    def test_modify_mtf_order(self):
        """Test case for modify_mtf_order

        Modify an existing MTF order  # noqa: E501
        """
        pass

    def test_place_new_mtf_order(self):
        """Test case for place_new_mtf_order

        Place a New MTF order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
