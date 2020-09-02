# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.normal_order_api import NormalOrderApi  # noqa: E501
from openapi_client.rest import ApiException


class TestNormalOrderApi(unittest.TestCase):
    """NormalOrderApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.normal_order_api.NormalOrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_normal_order(self):
        """Test case for cancel_normal_order

        Cancel a Normal order  # noqa: E501
        """
        pass

    def test_modify_normal_order(self):
        """Test case for modify_normal_order

        Modify an existing normal order  # noqa: E501
        """
        pass

    def test_place_new_normal_order(self):
        """Test case for place_new_normal_order

        Place a New normal order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
