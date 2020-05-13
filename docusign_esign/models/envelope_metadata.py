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


class EnvelopeMetadata(object):
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
        'allow_advanced_correct': 'str',
        'allow_correct': 'str',
        'enable_sign_with_notary': 'str'
    }

    attribute_map = {
        'allow_advanced_correct': 'allowAdvancedCorrect',
        'allow_correct': 'allowCorrect',
        'enable_sign_with_notary': 'enableSignWithNotary'
    }

    def __init__(self, allow_advanced_correct=None, allow_correct=None, enable_sign_with_notary=None):  # noqa: E501
        """EnvelopeMetadata - a model defined in Swagger"""  # noqa: E501

        self._allow_advanced_correct = None
        self._allow_correct = None
        self._enable_sign_with_notary = None
        self.discriminator = None

        if allow_advanced_correct is not None:
            self.allow_advanced_correct = allow_advanced_correct
        if allow_correct is not None:
            self.allow_correct = allow_correct
        if enable_sign_with_notary is not None:
            self.enable_sign_with_notary = enable_sign_with_notary

    @property
    def allow_advanced_correct(self):
        """Gets the allow_advanced_correct of this EnvelopeMetadata.  # noqa: E501

          # noqa: E501

        :return: The allow_advanced_correct of this EnvelopeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._allow_advanced_correct

    @allow_advanced_correct.setter
    def allow_advanced_correct(self, allow_advanced_correct):
        """Sets the allow_advanced_correct of this EnvelopeMetadata.

          # noqa: E501

        :param allow_advanced_correct: The allow_advanced_correct of this EnvelopeMetadata.  # noqa: E501
        :type: str
        """

        self._allow_advanced_correct = allow_advanced_correct

    @property
    def allow_correct(self):
        """Gets the allow_correct of this EnvelopeMetadata.  # noqa: E501

          # noqa: E501

        :return: The allow_correct of this EnvelopeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._allow_correct

    @allow_correct.setter
    def allow_correct(self, allow_correct):
        """Sets the allow_correct of this EnvelopeMetadata.

          # noqa: E501

        :param allow_correct: The allow_correct of this EnvelopeMetadata.  # noqa: E501
        :type: str
        """

        self._allow_correct = allow_correct

    @property
    def enable_sign_with_notary(self):
        """Gets the enable_sign_with_notary of this EnvelopeMetadata.  # noqa: E501

          # noqa: E501

        :return: The enable_sign_with_notary of this EnvelopeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._enable_sign_with_notary

    @enable_sign_with_notary.setter
    def enable_sign_with_notary(self, enable_sign_with_notary):
        """Sets the enable_sign_with_notary of this EnvelopeMetadata.

          # noqa: E501

        :param enable_sign_with_notary: The enable_sign_with_notary of this EnvelopeMetadata.  # noqa: E501
        :type: str
        """

        self._enable_sign_with_notary = enable_sign_with_notary

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
        if issubclass(EnvelopeMetadata, dict):
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
        if not isinstance(other, EnvelopeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
