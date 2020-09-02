# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.res_sor_order_mod import ResSOROrderMod  # noqa: E501
from openapi_client.rest import ApiException

class TestResSOROrderMod(unittest.TestCase):
    """ResSOROrderMod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResSOROrderMod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.res_sor_order_mod.ResSOROrderMod()  # noqa: E501
        if include_optional :
            return ResSOROrderMod(
                orderId = '0', 
                message = '0'
            )
        else :
            return ResSOROrderMod(
        )

    def testResSOROrderMod(self):
        """Test ResSOROrderMod"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
