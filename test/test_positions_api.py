# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.positions_api import PositionsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPositionsApi(unittest.TestCase):
    """PositionsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.positions_api.PositionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_positions(self):
        """Test case for positions

        Get's raw position from Trading Engine.  # noqa: E501
        """
        pass

    def test_positions_open(self):
        """Test case for positions_open

        Get's Open position.  # noqa: E501
        """
        pass

    def test_positions_stocks(self):
        """Test case for positions_stocks

        Get's Sell from Existing stocks.  # noqa: E501
        """
        pass

    def test_positions_today(self):
        """Test case for positions_today

        Get's Todays position.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
