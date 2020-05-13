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


class SettingsMetadata(object):
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
        'is21_cfr_part11': 'str',
        'options': 'list[str]',
        'rights': 'str',
        'ui_hint': 'str',
        'ui_order': 'str',
        'ui_type': 'str'
    }

    attribute_map = {
        'is21_cfr_part11': 'is21CFRPart11',
        'options': 'options',
        'rights': 'rights',
        'ui_hint': 'uiHint',
        'ui_order': 'uiOrder',
        'ui_type': 'uiType'
    }

    def __init__(self, is21_cfr_part11=None, options=None, rights=None, ui_hint=None, ui_order=None, ui_type=None):  # noqa: E501
        """SettingsMetadata - a model defined in Swagger"""  # noqa: E501

        self._is21_cfr_part11 = None
        self._options = None
        self._rights = None
        self._ui_hint = None
        self._ui_order = None
        self._ui_type = None
        self.discriminator = None

        if is21_cfr_part11 is not None:
            self.is21_cfr_part11 = is21_cfr_part11
        if options is not None:
            self.options = options
        if rights is not None:
            self.rights = rights
        if ui_hint is not None:
            self.ui_hint = ui_hint
        if ui_order is not None:
            self.ui_order = ui_order
        if ui_type is not None:
            self.ui_type = ui_type

    @property
    def is21_cfr_part11(self):
        """Gets the is21_cfr_part11 of this SettingsMetadata.  # noqa: E501

        When set to **true**, indicates that this module is enabled on the account.  # noqa: E501

        :return: The is21_cfr_part11 of this SettingsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._is21_cfr_part11

    @is21_cfr_part11.setter
    def is21_cfr_part11(self, is21_cfr_part11):
        """Sets the is21_cfr_part11 of this SettingsMetadata.

        When set to **true**, indicates that this module is enabled on the account.  # noqa: E501

        :param is21_cfr_part11: The is21_cfr_part11 of this SettingsMetadata.  # noqa: E501
        :type: str
        """

        self._is21_cfr_part11 = is21_cfr_part11

    @property
    def options(self):
        """Gets the options of this SettingsMetadata.  # noqa: E501

          # noqa: E501

        :return: The options of this SettingsMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SettingsMetadata.

          # noqa: E501

        :param options: The options of this SettingsMetadata.  # noqa: E501
        :type: list[str]
        """

        self._options = options

    @property
    def rights(self):
        """Gets the rights of this SettingsMetadata.  # noqa: E501

          # noqa: E501

        :return: The rights of this SettingsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """Sets the rights of this SettingsMetadata.

          # noqa: E501

        :param rights: The rights of this SettingsMetadata.  # noqa: E501
        :type: str
        """

        self._rights = rights

    @property
    def ui_hint(self):
        """Gets the ui_hint of this SettingsMetadata.  # noqa: E501

          # noqa: E501

        :return: The ui_hint of this SettingsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._ui_hint

    @ui_hint.setter
    def ui_hint(self, ui_hint):
        """Sets the ui_hint of this SettingsMetadata.

          # noqa: E501

        :param ui_hint: The ui_hint of this SettingsMetadata.  # noqa: E501
        :type: str
        """

        self._ui_hint = ui_hint

    @property
    def ui_order(self):
        """Gets the ui_order of this SettingsMetadata.  # noqa: E501

          # noqa: E501

        :return: The ui_order of this SettingsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._ui_order

    @ui_order.setter
    def ui_order(self, ui_order):
        """Sets the ui_order of this SettingsMetadata.

          # noqa: E501

        :param ui_order: The ui_order of this SettingsMetadata.  # noqa: E501
        :type: str
        """

        self._ui_order = ui_order

    @property
    def ui_type(self):
        """Gets the ui_type of this SettingsMetadata.  # noqa: E501

          # noqa: E501

        :return: The ui_type of this SettingsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._ui_type

    @ui_type.setter
    def ui_type(self, ui_type):
        """Sets the ui_type of this SettingsMetadata.

          # noqa: E501

        :param ui_type: The ui_type of this SettingsMetadata.  # noqa: E501
        :type: str
        """

        self._ui_type = ui_type

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
        if issubclass(SettingsMetadata, dict):
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
        if not isinstance(other, SettingsMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
