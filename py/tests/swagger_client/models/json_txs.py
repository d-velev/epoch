# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.  # noqa: E501

    OpenAPI spec version: 0.6.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.signed_tx_json import SignedTxJSON  # noqa: F401,E501
from swagger_client.models.tx_objects import TxObjects  # noqa: F401,E501


class JSONTxs(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'transactions': 'list[SignedTxJSON]'
    }

    attribute_map = {
        'transactions': 'transactions'
    }

    def __init__(self, transactions=None):  # noqa: E501
        """JSONTxs - a model defined in Swagger"""  # noqa: E501

        self._transactions = None
        self.discriminator = None

        if transactions is not None:
            self.transactions = transactions

    @property
    def transactions(self):
        """Gets the transactions of this JSONTxs.  # noqa: E501


        :return: The transactions of this JSONTxs.  # noqa: E501
        :rtype: list[SignedTxJSON]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this JSONTxs.


        :param transactions: The transactions of this JSONTxs.  # noqa: E501
        :type: list[SignedTxJSON]
        """

        self._transactions = transactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, JSONTxs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
