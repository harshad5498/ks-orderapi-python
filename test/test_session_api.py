# coding: utf-8

"""
    Session-Order-Margin-API



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.session_api import SessionApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSessionApi(unittest.TestCase):
    """SessionApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.session_api.SessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_session2_fa(self):
        """Test case for generate_session2_fa

        Generate final Session Token  # noqa: E501
        """
        pass

    def test_login_with_user_id(self):
        """Test case for login_with_user_id

        Login using Userid  # noqa: E501
        """
        pass

    def test_session_init(self):
        """Test case for session_init

        Initialise Session  # noqa: E501
        """
        pass

    def test_session_logout(self):
        """Test case for session_logout

        Invalidate Session Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()