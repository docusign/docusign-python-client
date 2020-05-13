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


class ListCustomField(object):
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
        'configuration_type': 'str',
        'error_details': 'ErrorDetails',
        'field_id': 'str',
        'list_items': 'list[str]',
        'name': 'str',
        'required': 'str',
        'show': 'str',
        'value': 'str'
    }

    attribute_map = {
        'configuration_type': 'configurationType',
        'error_details': 'errorDetails',
        'field_id': 'fieldId',
        'list_items': 'listItems',
        'name': 'name',
        'required': 'required',
        'show': 'show',
        'value': 'value'
    }

    def __init__(self, configuration_type=None, error_details=None, field_id=None, list_items=None, name=None, required=None, show=None, value=None):  # noqa: E501
        """ListCustomField - a model defined in Swagger"""  # noqa: E501

        self._configuration_type = None
        self._error_details = None
        self._field_id = None
        self._list_items = None
        self._name = None
        self._required = None
        self._show = None
        self._value = None
        self.discriminator = None

        if configuration_type is not None:
            self.configuration_type = configuration_type
        if error_details is not None:
            self.error_details = error_details
        if field_id is not None:
            self.field_id = field_id
        if list_items is not None:
            self.list_items = list_items
        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if show is not None:
            self.show = show
        if value is not None:
            self.value = value

    @property
    def configuration_type(self):
        """Gets the configuration_type of this ListCustomField.  # noqa: E501

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :return: The configuration_type of this ListCustomField.  # noqa: E501
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this ListCustomField.

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :param configuration_type: The configuration_type of this ListCustomField.  # noqa: E501
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def error_details(self):
        """Gets the error_details of this ListCustomField.  # noqa: E501


        :return: The error_details of this ListCustomField.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this ListCustomField.


        :param error_details: The error_details of this ListCustomField.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def field_id(self):
        """Gets the field_id of this ListCustomField.  # noqa: E501

        An ID used to specify a custom field.  # noqa: E501

        :return: The field_id of this ListCustomField.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ListCustomField.

        An ID used to specify a custom field.  # noqa: E501

        :param field_id: The field_id of this ListCustomField.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def list_items(self):
        """Gets the list_items of this ListCustomField.  # noqa: E501

          # noqa: E501

        :return: The list_items of this ListCustomField.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_items

    @list_items.setter
    def list_items(self, list_items):
        """Sets the list_items of this ListCustomField.

          # noqa: E501

        :param list_items: The list_items of this ListCustomField.  # noqa: E501
        :type: list[str]
        """

        self._list_items = list_items

    @property
    def name(self):
        """Gets the name of this ListCustomField.  # noqa: E501

        The name of the custom field.  # noqa: E501

        :return: The name of this ListCustomField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCustomField.

        The name of the custom field.  # noqa: E501

        :param name: The name of this ListCustomField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this ListCustomField.  # noqa: E501

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :return: The required of this ListCustomField.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ListCustomField.

        When set to **true**, the signer is required to fill out this tab  # noqa: E501

        :param required: The required of this ListCustomField.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def show(self):
        """Gets the show of this ListCustomField.  # noqa: E501

        A boolean indicating if the value should be displayed.  # noqa: E501

        :return: The show of this ListCustomField.  # noqa: E501
        :rtype: str
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this ListCustomField.

        A boolean indicating if the value should be displayed.  # noqa: E501

        :param show: The show of this ListCustomField.  # noqa: E501
        :type: str
        """

        self._show = show

    @property
    def value(self):
        """Gets the value of this ListCustomField.  # noqa: E501

        The value of the custom field.  Maximum Length: 100 characters.  # noqa: E501

        :return: The value of this ListCustomField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListCustomField.

        The value of the custom field.  Maximum Length: 100 characters.  # noqa: E501

        :param value: The value of this ListCustomField.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(ListCustomField, dict):
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
        if not isinstance(other, ListCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
