# coding: utf-8

"""
    KS- Trade API



    The version of the OpenAPI document: 1.0

"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Codmodify(object):
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
        'orderNo': 'str'
    }

    attribute_map = {
        'orderNo': 'orderNo'
    }

    def __init__(self, orderNo=None, local_vars_configuration=None):  # noqa: E501
        """Codmodify - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._orderNo = None
        self.discriminator = None

        if orderNo is not None:
            self.orderNo = orderNo

    @property
    def orderNo(self):
        """Gets the orderNo of this Codmodify.  # noqa: E501

        Order Number to modify  # noqa: E501

        :return: The orderNo of this Codmodify.  # noqa: E501
        :rtype: str
        """
        return self._orderNo

    @orderNo.setter
    def orderNo(self, orderNo):
        """Sets the orderNo of this Codmodify.

        Order Number to modify  # noqa: E501

        :param orderNo: The orderNo of this Codmodify.  # noqa: E501
        :type orderNo: str
        """

        self._orderNo = orderNo

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
        if not isinstance(other, Codmodify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Codmodify):
            return True

        return self.to_dict() != other.to_dict()
