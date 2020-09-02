# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.req_margin import ReqMargin  # noqa: E501
from openapi_client.rest import ApiException

class TestReqMargin(unittest.TestCase):
    """ReqMargin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReqMargin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.req_margin.ReqMargin()  # noqa: E501
        if include_optional :
            return ReqMargin(
                transactionType = 'BUY', 
                orderInfo = [
                    openapi_client.models.margi_info/.Margi info.(
                        instrument_token = 56, 
                        quantity = 56, 
                        price = 1.337, 
                        amount = 56, 
                        trigger_price = 1.337, )
                    ]
            )
        else :
            return ReqMargin(
        )

    def testReqMargin(self):
        """Test ReqMargin"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
