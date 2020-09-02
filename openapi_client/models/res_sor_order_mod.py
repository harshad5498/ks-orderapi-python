# coding: utf-8

"""
    KS- Trade API



    The version of the OpenAPI document: 1.0

"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResSOROrderMod(object):
    """.
    

    
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'orderId': 'str',
        'message': 'str'
    }

    attribute_map = {
        'orderId': 'orderId',
        'message': 'message'
    }

    def __init__(self, orderId=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ResSOROrderMod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._orderId = None
        self._message = None
        self.discriminator = None

        if orderId is not None:
            self.orderId = orderId
        if message is not None:
            self.message = message

    @property
    def orderId(self):
        """Gets the orderId of this ResSOROrderMod.  # noqa: E501

        Order ID of the order to be modified  # noqa: E501

        :return: The orderId of this ResSOROrderMod.  # noqa: E501
        :rtype: str
        """
        return self._orderId

    @orderId.setter
    def orderId(self, orderId):
        """Sets the orderId of this ResSOROrderMod.

        Order ID of the order to be modified  # noqa: E501

        :param orderId: The orderId of this ResSOROrderMod.  # noqa: E501
        :type orderId: str
        """

        self._orderId = orderId

    @property
    def message(self):
        """Gets the message of this ResSOROrderMod.  # noqa: E501

        Order Status  # noqa: E501

        :return: The message of this ResSOROrderMod.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResSOROrderMod.

        Order Status  # noqa: E501

        :param message: The message of this ResSOROrderMod.  # noqa: E501
        :type message: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResSOROrderMod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResSOROrderMod):
            return True

        return self.to_dict() != other.to_dict()