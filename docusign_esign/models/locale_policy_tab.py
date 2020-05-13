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


class LocalePolicyTab(object):
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
        'address_format': 'str',
        'calendar_type': 'str',
        'culture_name': 'str',
        'currency_negative_format': 'str',
        'currency_positive_format': 'str',
        'custom_date_format': 'str',
        'custom_time_format': 'str',
        'date_format': 'str',
        'initial_format': 'str',
        'name_format': 'str',
        'time_format': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'address_format': 'addressFormat',
        'calendar_type': 'calendarType',
        'culture_name': 'cultureName',
        'currency_negative_format': 'currencyNegativeFormat',
        'currency_positive_format': 'currencyPositiveFormat',
        'custom_date_format': 'customDateFormat',
        'custom_time_format': 'customTimeFormat',
        'date_format': 'dateFormat',
        'initial_format': 'initialFormat',
        'name_format': 'nameFormat',
        'time_format': 'timeFormat',
        'time_zone': 'timeZone'
    }

    def __init__(self, address_format=None, calendar_type=None, culture_name=None, currency_negative_format=None, currency_positive_format=None, custom_date_format=None, custom_time_format=None, date_format=None, initial_format=None, name_format=None, time_format=None, time_zone=None):  # noqa: E501
        """LocalePolicyTab - a model defined in Swagger"""  # noqa: E501

        self._address_format = None
        self._calendar_type = None
        self._culture_name = None
        self._currency_negative_format = None
        self._currency_positive_format = None
        self._custom_date_format = None
        self._custom_time_format = None
        self._date_format = None
        self._initial_format = None
        self._name_format = None
        self._time_format = None
        self._time_zone = None
        self.discriminator = None

        if address_format is not None:
            self.address_format = address_format
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if culture_name is not None:
            self.culture_name = culture_name
        if currency_negative_format is not None:
            self.currency_negative_format = currency_negative_format
        if currency_positive_format is not None:
            self.currency_positive_format = currency_positive_format
        if custom_date_format is not None:
            self.custom_date_format = custom_date_format
        if custom_time_format is not None:
            self.custom_time_format = custom_time_format
        if date_format is not None:
            self.date_format = date_format
        if initial_format is not None:
            self.initial_format = initial_format
        if name_format is not None:
            self.name_format = name_format
        if time_format is not None:
            self.time_format = time_format
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def address_format(self):
        """Gets the address_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The address_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._address_format

    @address_format.setter
    def address_format(self, address_format):
        """Sets the address_format of this LocalePolicyTab.

          # noqa: E501

        :param address_format: The address_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._address_format = address_format

    @property
    def calendar_type(self):
        """Gets the calendar_type of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The calendar_type of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this LocalePolicyTab.

          # noqa: E501

        :param calendar_type: The calendar_type of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._calendar_type = calendar_type

    @property
    def culture_name(self):
        """Gets the culture_name of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The culture_name of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._culture_name

    @culture_name.setter
    def culture_name(self, culture_name):
        """Sets the culture_name of this LocalePolicyTab.

          # noqa: E501

        :param culture_name: The culture_name of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._culture_name = culture_name

    @property
    def currency_negative_format(self):
        """Gets the currency_negative_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The currency_negative_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._currency_negative_format

    @currency_negative_format.setter
    def currency_negative_format(self, currency_negative_format):
        """Sets the currency_negative_format of this LocalePolicyTab.

          # noqa: E501

        :param currency_negative_format: The currency_negative_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._currency_negative_format = currency_negative_format

    @property
    def currency_positive_format(self):
        """Gets the currency_positive_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The currency_positive_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._currency_positive_format

    @currency_positive_format.setter
    def currency_positive_format(self, currency_positive_format):
        """Sets the currency_positive_format of this LocalePolicyTab.

          # noqa: E501

        :param currency_positive_format: The currency_positive_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._currency_positive_format = currency_positive_format

    @property
    def custom_date_format(self):
        """Gets the custom_date_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The custom_date_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._custom_date_format

    @custom_date_format.setter
    def custom_date_format(self, custom_date_format):
        """Sets the custom_date_format of this LocalePolicyTab.

          # noqa: E501

        :param custom_date_format: The custom_date_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._custom_date_format = custom_date_format

    @property
    def custom_time_format(self):
        """Gets the custom_time_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The custom_time_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._custom_time_format

    @custom_time_format.setter
    def custom_time_format(self, custom_time_format):
        """Sets the custom_time_format of this LocalePolicyTab.

          # noqa: E501

        :param custom_time_format: The custom_time_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._custom_time_format = custom_time_format

    @property
    def date_format(self):
        """Gets the date_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The date_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this LocalePolicyTab.

          # noqa: E501

        :param date_format: The date_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def initial_format(self):
        """Gets the initial_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The initial_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._initial_format

    @initial_format.setter
    def initial_format(self, initial_format):
        """Sets the initial_format of this LocalePolicyTab.

          # noqa: E501

        :param initial_format: The initial_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._initial_format = initial_format

    @property
    def name_format(self):
        """Gets the name_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The name_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._name_format

    @name_format.setter
    def name_format(self, name_format):
        """Sets the name_format of this LocalePolicyTab.

          # noqa: E501

        :param name_format: The name_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._name_format = name_format

    @property
    def time_format(self):
        """Gets the time_format of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The time_format of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this LocalePolicyTab.

          # noqa: E501

        :param time_format: The time_format of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._time_format = time_format

    @property
    def time_zone(self):
        """Gets the time_zone of this LocalePolicyTab.  # noqa: E501

          # noqa: E501

        :return: The time_zone of this LocalePolicyTab.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this LocalePolicyTab.

          # noqa: E501

        :param time_zone: The time_zone of this LocalePolicyTab.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

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
        if issubclass(LocalePolicyTab, dict):
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
        if not isinstance(other, LocalePolicyTab):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
