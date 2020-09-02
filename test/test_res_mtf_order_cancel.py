# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.res_mtf_order_cancel import ResMTFOrderCancel  # noqa: E501
from openapi_client.rest import ApiException

class TestResMTFOrderCancel(unittest.TestCase):
    """ResMTFOrderCancel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResMTFOrderCancel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.res_mtf_order_cancel.ResMTFOrderCancel()  # noqa: E501
        if include_optional :
            return ResMTFOrderCancel(
                orderId = '0', 
                message = '0'
            )
        else :
            return ResMTFOrderCancel(
        )

    def testResMTFOrderCancel(self):
        """Test ResMTFOrderCancel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
