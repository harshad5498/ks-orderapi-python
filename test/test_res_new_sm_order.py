# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.res_new_sm_order import ResNewSMOrder  # noqa: E501
from openapi_client.rest import ApiException

class TestResNewSMOrder(unittest.TestCase):
    """ResNewSMOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResNewSMOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.res_new_sm_order.ResNewSMOrder()  # noqa: E501
        if include_optional :
            return ResNewSMOrder(
                orderId = '0', 
                message = '0'
            )
        else :
            return ResNewSMOrder(
        )

    def testResNewSMOrder(self):
        """Test ResNewSMOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()