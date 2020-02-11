# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BulkSendingCopyTab(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, initial_value=None, tab_label=None):
        """
        BulkSendingCopyTab - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'initial_value': 'str',
            'tab_label': 'str'
        }

        self.attribute_map = {
            'initial_value': 'initialValue',
            'tab_label': 'tabLabel'
        }

        self._initial_value = initial_value
        self._tab_label = tab_label

    @property
    def initial_value(self):
        """
        Gets the initial_value of this BulkSendingCopyTab.
        The original value of the tab.

        :return: The initial_value of this BulkSendingCopyTab.
        :rtype: str
        """
        return self._initial_value

    @initial_value.setter
    def initial_value(self, initial_value):
        """
        Sets the initial_value of this BulkSendingCopyTab.
        The original value of the tab.

        :param initial_value: The initial_value of this BulkSendingCopyTab.
        :type: str
        """

        self._initial_value = initial_value

    @property
    def tab_label(self):
        """
        Gets the tab_label of this BulkSendingCopyTab.
        The label string associated with the tab.

        :return: The tab_label of this BulkSendingCopyTab.
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """
        Sets the tab_label of this BulkSendingCopyTab.
        The label string associated with the tab.

        :param tab_label: The tab_label of this BulkSendingCopyTab.
        :type: str
        """

        self._tab_label = tab_label

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other