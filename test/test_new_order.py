# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.new_order import NewOrder  # noqa: E501
from openapi_client.rest import ApiException

class TestNewOrder(unittest.TestCase):
    """NewOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.new_order.NewOrder()  # noqa: E501
        if include_optional :
            return NewOrder(
                instrumentToken = 56, 
                transactionType = 'BUY', 
                quantity = 56, 
                price = 1.337, 
                product = 'NORMAL', 
                validity = 'GFD', 
                variety = 'REGULAR', 
                disclosedQuantity = 56, 
                triggerPrice = 1.337, 
                tslo = openapi_client.models.tslo_parameters.TSLO Parameters(
                    spread = 1.337, 
                    trailing_price = 1.337, ), 
                bracket = openapi_client.models.brakcet_order_parameters.Brakcet Order Parameters(
                    spread = 1.337, 
                    trailing_price = 1.337, 
                    book_profit = 1.337, 
                    book_disclosed_qty = 56, ), 
                tslonew = openapi_client.models.tslo_parameters.TSLO Parameters(
                    spread = 1.337, 
                    trailing_price = 1.337, ), 
                bracketnew = openapi_client.models.brakcet_order_parameters.Brakcet Order Parameters(
                    spread = 1.337, 
                    trailing_price = 1.337, 
                    book_profit = 1.337, 
                    book_disclosed_qty = 56, ), 
                gtc = openapi_client.models.good_till_cancel_order.Good till Cancel Order(
                    close_date = '0', ), 
                ctd = openapi_client.models.convert_to_delivery.Convert to delivery(
                    convert_quantity = 56, ), 
                cod = openapi_client.models.call_of_the_day.Call of the Day(
                    square_off_flag = 56, ), 
                tag = '0'
            )
        else :
            return NewOrder(
        )

    def testNewOrder(self):
        """Test NewOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()