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


class AccountPasswordQuestionsRequired(object):
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
        'maximum_questions': 'str',
        'minimum_questions': 'str'
    }

    attribute_map = {
        'maximum_questions': 'maximumQuestions',
        'minimum_questions': 'minimumQuestions'
    }

    def __init__(self, maximum_questions=None, minimum_questions=None):  # noqa: E501
        """AccountPasswordQuestionsRequired - a model defined in Swagger"""  # noqa: E501

        self._maximum_questions = None
        self._minimum_questions = None
        self.discriminator = None

        if maximum_questions is not None:
            self.maximum_questions = maximum_questions
        if minimum_questions is not None:
            self.minimum_questions = minimum_questions

    @property
    def maximum_questions(self):
        """Gets the maximum_questions of this AccountPasswordQuestionsRequired.  # noqa: E501

          # noqa: E501

        :return: The maximum_questions of this AccountPasswordQuestionsRequired.  # noqa: E501
        :rtype: str
        """
        return self._maximum_questions

    @maximum_questions.setter
    def maximum_questions(self, maximum_questions):
        """Sets the maximum_questions of this AccountPasswordQuestionsRequired.

          # noqa: E501

        :param maximum_questions: The maximum_questions of this AccountPasswordQuestionsRequired.  # noqa: E501
        :type: str
        """

        self._maximum_questions = maximum_questions

    @property
    def minimum_questions(self):
        """Gets the minimum_questions of this AccountPasswordQuestionsRequired.  # noqa: E501

          # noqa: E501

        :return: The minimum_questions of this AccountPasswordQuestionsRequired.  # noqa: E501
        :rtype: str
        """
        return self._minimum_questions

    @minimum_questions.setter
    def minimum_questions(self, minimum_questions):
        """Sets the minimum_questions of this AccountPasswordQuestionsRequired.

          # noqa: E501

        :param minimum_questions: The minimum_questions of this AccountPasswordQuestionsRequired.  # noqa: E501
        :type: str
        """

        self._minimum_questions = minimum_questions

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
        if issubclass(AccountPasswordQuestionsRequired, dict):
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
        if not isinstance(other, AccountPasswordQuestionsRequired):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
