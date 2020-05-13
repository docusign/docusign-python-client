# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RecipientIdentityInputOption(object):
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
        'name': 'str',
        'phone_number_list': 'list[RecipientIdentityPhoneNumber]',
        'value_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone_number_list': 'phoneNumberList',
        'value_type': 'valueType'
    }

    def __init__(self, name=None, phone_number_list=None, value_type=None):  # noqa: E501
        """RecipientIdentityInputOption - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._phone_number_list = None
        self._value_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if phone_number_list is not None:
            self.phone_number_list = phone_number_list
        if value_type is not None:
            self.value_type = value_type

    @property
    def name(self):
        """Gets the name of this RecipientIdentityInputOption.  # noqa: E501

          # noqa: E501

        :return: The name of this RecipientIdentityInputOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecipientIdentityInputOption.

          # noqa: E501

        :param name: The name of this RecipientIdentityInputOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_number_list(self):
        """Gets the phone_number_list of this RecipientIdentityInputOption.  # noqa: E501

          # noqa: E501

        :return: The phone_number_list of this RecipientIdentityInputOption.  # noqa: E501
        :rtype: list[RecipientIdentityPhoneNumber]
        """
        return self._phone_number_list

    @phone_number_list.setter
    def phone_number_list(self, phone_number_list):
        """Sets the phone_number_list of this RecipientIdentityInputOption.

          # noqa: E501

        :param phone_number_list: The phone_number_list of this RecipientIdentityInputOption.  # noqa: E501
        :type: list[RecipientIdentityPhoneNumber]
        """

        self._phone_number_list = phone_number_list

    @property
    def value_type(self):
        """Gets the value_type of this RecipientIdentityInputOption.  # noqa: E501

          # noqa: E501

        :return: The value_type of this RecipientIdentityInputOption.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this RecipientIdentityInputOption.

          # noqa: E501

        :param value_type: The value_type of this RecipientIdentityInputOption.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

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
        if issubclass(RecipientIdentityInputOption, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecipientIdentityInputOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
