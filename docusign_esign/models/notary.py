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


class Notary(object):
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
        'created_date': 'str',
        'enabled': 'str',
        'searchable': 'str',
        'user_info': 'UserInformation'
    }

    attribute_map = {
        'created_date': 'createdDate',
        'enabled': 'enabled',
        'searchable': 'searchable',
        'user_info': 'userInfo'
    }

    def __init__(self, created_date=None, enabled=None, searchable=None, user_info=None):  # noqa: E501
        """Notary - a model defined in Swagger"""  # noqa: E501

        self._created_date = None
        self._enabled = None
        self._searchable = None
        self._user_info = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if enabled is not None:
            self.enabled = enabled
        if searchable is not None:
            self.searchable = searchable
        if user_info is not None:
            self.user_info = user_info

    @property
    def created_date(self):
        """Gets the created_date of this Notary.  # noqa: E501

          # noqa: E501

        :return: The created_date of this Notary.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Notary.

          # noqa: E501

        :param created_date: The created_date of this Notary.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def enabled(self):
        """Gets the enabled of this Notary.  # noqa: E501

          # noqa: E501

        :return: The enabled of this Notary.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Notary.

          # noqa: E501

        :param enabled: The enabled of this Notary.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def searchable(self):
        """Gets the searchable of this Notary.  # noqa: E501

          # noqa: E501

        :return: The searchable of this Notary.  # noqa: E501
        :rtype: str
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this Notary.

          # noqa: E501

        :param searchable: The searchable of this Notary.  # noqa: E501
        :type: str
        """

        self._searchable = searchable

    @property
    def user_info(self):
        """Gets the user_info of this Notary.  # noqa: E501


        :return: The user_info of this Notary.  # noqa: E501
        :rtype: UserInformation
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this Notary.


        :param user_info: The user_info of this Notary.  # noqa: E501
        :type: UserInformation
        """

        self._user_info = user_info

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
        if issubclass(Notary, dict):
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
        if not isinstance(other, Notary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
