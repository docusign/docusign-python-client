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


class AccountPasswordStrengthTypeOption(object):
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
        'minimum_length': 'str',
        'name': 'str',
        'password_include_digit': 'str',
        'password_include_digit_or_special_character': 'str',
        'password_include_lower_case': 'str',
        'password_include_special_character': 'str',
        'password_include_upper_case': 'str'
    }

    attribute_map = {
        'minimum_length': 'minimumLength',
        'name': 'name',
        'password_include_digit': 'passwordIncludeDigit',
        'password_include_digit_or_special_character': 'passwordIncludeDigitOrSpecialCharacter',
        'password_include_lower_case': 'passwordIncludeLowerCase',
        'password_include_special_character': 'passwordIncludeSpecialCharacter',
        'password_include_upper_case': 'passwordIncludeUpperCase'
    }

    def __init__(self, minimum_length=None, name=None, password_include_digit=None, password_include_digit_or_special_character=None, password_include_lower_case=None, password_include_special_character=None, password_include_upper_case=None):  # noqa: E501
        """AccountPasswordStrengthTypeOption - a model defined in Swagger"""  # noqa: E501

        self._minimum_length = None
        self._name = None
        self._password_include_digit = None
        self._password_include_digit_or_special_character = None
        self._password_include_lower_case = None
        self._password_include_special_character = None
        self._password_include_upper_case = None
        self.discriminator = None

        if minimum_length is not None:
            self.minimum_length = minimum_length
        if name is not None:
            self.name = name
        if password_include_digit is not None:
            self.password_include_digit = password_include_digit
        if password_include_digit_or_special_character is not None:
            self.password_include_digit_or_special_character = password_include_digit_or_special_character
        if password_include_lower_case is not None:
            self.password_include_lower_case = password_include_lower_case
        if password_include_special_character is not None:
            self.password_include_special_character = password_include_special_character
        if password_include_upper_case is not None:
            self.password_include_upper_case = password_include_upper_case

    @property
    def minimum_length(self):
        """Gets the minimum_length of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The minimum_length of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._minimum_length

    @minimum_length.setter
    def minimum_length(self, minimum_length):
        """Sets the minimum_length of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param minimum_length: The minimum_length of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._minimum_length = minimum_length

    @property
    def name(self):
        """Gets the name of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The name of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param name: The name of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password_include_digit(self):
        """Gets the password_include_digit of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The password_include_digit of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._password_include_digit

    @password_include_digit.setter
    def password_include_digit(self, password_include_digit):
        """Sets the password_include_digit of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param password_include_digit: The password_include_digit of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._password_include_digit = password_include_digit

    @property
    def password_include_digit_or_special_character(self):
        """Gets the password_include_digit_or_special_character of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The password_include_digit_or_special_character of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._password_include_digit_or_special_character

    @password_include_digit_or_special_character.setter
    def password_include_digit_or_special_character(self, password_include_digit_or_special_character):
        """Sets the password_include_digit_or_special_character of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param password_include_digit_or_special_character: The password_include_digit_or_special_character of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._password_include_digit_or_special_character = password_include_digit_or_special_character

    @property
    def password_include_lower_case(self):
        """Gets the password_include_lower_case of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The password_include_lower_case of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._password_include_lower_case

    @password_include_lower_case.setter
    def password_include_lower_case(self, password_include_lower_case):
        """Sets the password_include_lower_case of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param password_include_lower_case: The password_include_lower_case of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._password_include_lower_case = password_include_lower_case

    @property
    def password_include_special_character(self):
        """Gets the password_include_special_character of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The password_include_special_character of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._password_include_special_character

    @password_include_special_character.setter
    def password_include_special_character(self, password_include_special_character):
        """Sets the password_include_special_character of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param password_include_special_character: The password_include_special_character of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._password_include_special_character = password_include_special_character

    @property
    def password_include_upper_case(self):
        """Gets the password_include_upper_case of this AccountPasswordStrengthTypeOption.  # noqa: E501

          # noqa: E501

        :return: The password_include_upper_case of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :rtype: str
        """
        return self._password_include_upper_case

    @password_include_upper_case.setter
    def password_include_upper_case(self, password_include_upper_case):
        """Sets the password_include_upper_case of this AccountPasswordStrengthTypeOption.

          # noqa: E501

        :param password_include_upper_case: The password_include_upper_case of this AccountPasswordStrengthTypeOption.  # noqa: E501
        :type: str
        """

        self._password_include_upper_case = password_include_upper_case

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
        if issubclass(AccountPasswordStrengthTypeOption, dict):
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
        if not isinstance(other, AccountPasswordStrengthTypeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
