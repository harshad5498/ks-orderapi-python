# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.reports_api import ReportsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.reports_api.ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_order_report_by_order_id(self):
        """Test case for get_order_report_by_order_id

        Get order report by orderId  # noqa: E501
        """
        pass

    def test_get_order_reports(self):
        """Test case for get_order_reports

        Get order report  # noqa: E501
        """
        pass

    def test_get_trade_report(self):
        """Test case for get_trade_report

        Get trade report  # noqa: E501
        """
        pass

    def test_get_trade_report_by_order_id(self):
        """Test case for get_trade_report_by_order_id

        Get trade report by orderId  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
