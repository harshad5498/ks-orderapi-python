# coding: utf-8

"""
    KS Trade API's

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.existing_mtf_order import ExistingMTFOrder  # noqa: E501
from openapi_client.rest import ApiException

class TestExistingMTFOrder(unittest.TestCase):
    """ExistingMTFOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExistingMTFOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.existing_mtf_order.ExistingMTFOrder()  # noqa: E501
        if include_optional :
            return ExistingMTFOrder(
                orderId = '0', 
                quantity = 56, 
                price = 1.337, 
                disclosedQuantity = 56, 
                triggerPrice = 1.337
            )
        else :
            return ExistingMTFOrder(
                orderId = '0',
        )

    def testExistingMTFOrder(self):
        """Test ExistingMTFOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
