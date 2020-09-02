# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.existing_order import ExistingOrder  # noqa: E501
from openapi_client.rest import ApiException

class TestExistingOrder(unittest.TestCase):
    """ExistingOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExistingOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.existing_order.ExistingOrder()  # noqa: E501
        if include_optional :
            return ExistingOrder(
                orderId = '0', 
                quantity = 56, 
                price = 1.337, 
                disclosedQuantity = 56, 
                triggerPrice = 1.337, 
                tslo = openapi_client.models.tslo_parameters.TSLO Parameters(
                    order_indicator = 56, 
                    spread = 1.337, 
                    trailing_price = 1.337, ), 
                bracket = openapi_client.models.brakcet_order_parameters.Brakcet Order Parameters(
                    order_indicator = 56, 
                    spread = 1.337, 
                    trailing_price = 1.337, 
                    book_profit = 1.337, 
                    book_disclosed_qty = 56, ), 
                tslonew = openapi_client.models.tslo_parameters.TSLO Parameters(
                    order_indicator = 56, 
                    spread = 1.337, 
                    trailing_price = 1.337, ), 
                bracketnew = openapi_client.models.brakcet_order_parameters.Brakcet Order Parameters(
                    order_indicator = 56, 
                    spread = 1.337, 
                    trailing_price = 1.337, 
                    book_profit = 1.337, 
                    book_disclosed_qty = 56, ), 
                gtc = openapi_client.models.good_till_cancel_order.Good till Cancel Order(
                    gtc_order_no = '0', ), 
                ctd = openapi_client.models.convert_to_delivery.Convert to delivery(
                    convert_quantity = 56, ), 
                cod = openapi_client.models.call_of_the_day.Call of the Day(
                    order_no = '0', )
            )
        else :
            return ExistingOrder(
                orderId = '0',
        )

    def testExistingOrder(self):
        """Test ExistingOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
