# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.margin_api import MarginApi  # noqa: E501
from openapi_client.rest import ApiException


class TestMarginApi(unittest.TestCase):
    """MarginApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.margin_api.MarginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_margin_required(self):
        """Test case for margin_required

        Get Margin Required for an order by amount or quantity.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
