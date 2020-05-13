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


class ConnectSalesforceObject(object):
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
        'active': 'str',
        'description': 'str',
        'id': 'str',
        'insert': 'str',
        'on_complete_only': 'str',
        'select_fields': 'list[ConnectSalesforceField]',
        'sf_object': 'str',
        'sf_object_name': 'str',
        'update_fields': 'list[ConnectSalesforceField]'
    }

    attribute_map = {
        'active': 'active',
        'description': 'description',
        'id': 'id',
        'insert': 'insert',
        'on_complete_only': 'onCompleteOnly',
        'select_fields': 'selectFields',
        'sf_object': 'sfObject',
        'sf_object_name': 'sfObjectName',
        'update_fields': 'updateFields'
    }

    def __init__(self, active=None, description=None, id=None, insert=None, on_complete_only=None, select_fields=None, sf_object=None, sf_object_name=None, update_fields=None):  # noqa: E501
        """ConnectSalesforceObject - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._description = None
        self._id = None
        self._insert = None
        self._on_complete_only = None
        self._select_fields = None
        self._sf_object = None
        self._sf_object_name = None
        self._update_fields = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if insert is not None:
            self.insert = insert
        if on_complete_only is not None:
            self.on_complete_only = on_complete_only
        if select_fields is not None:
            self.select_fields = select_fields
        if sf_object is not None:
            self.sf_object = sf_object
        if sf_object_name is not None:
            self.sf_object_name = sf_object_name
        if update_fields is not None:
            self.update_fields = update_fields

    @property
    def active(self):
        """Gets the active of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The active of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ConnectSalesforceObject.

          # noqa: E501

        :param active: The active of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def description(self):
        """Gets the description of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The description of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectSalesforceObject.

          # noqa: E501

        :param description: The description of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The id of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectSalesforceObject.

          # noqa: E501

        :param id: The id of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def insert(self):
        """Gets the insert of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The insert of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._insert

    @insert.setter
    def insert(self, insert):
        """Sets the insert of this ConnectSalesforceObject.

          # noqa: E501

        :param insert: The insert of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._insert = insert

    @property
    def on_complete_only(self):
        """Gets the on_complete_only of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The on_complete_only of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._on_complete_only

    @on_complete_only.setter
    def on_complete_only(self, on_complete_only):
        """Sets the on_complete_only of this ConnectSalesforceObject.

          # noqa: E501

        :param on_complete_only: The on_complete_only of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._on_complete_only = on_complete_only

    @property
    def select_fields(self):
        """Gets the select_fields of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The select_fields of this ConnectSalesforceObject.  # noqa: E501
        :rtype: list[ConnectSalesforceField]
        """
        return self._select_fields

    @select_fields.setter
    def select_fields(self, select_fields):
        """Sets the select_fields of this ConnectSalesforceObject.

          # noqa: E501

        :param select_fields: The select_fields of this ConnectSalesforceObject.  # noqa: E501
        :type: list[ConnectSalesforceField]
        """

        self._select_fields = select_fields

    @property
    def sf_object(self):
        """Gets the sf_object of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The sf_object of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._sf_object

    @sf_object.setter
    def sf_object(self, sf_object):
        """Sets the sf_object of this ConnectSalesforceObject.

          # noqa: E501

        :param sf_object: The sf_object of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._sf_object = sf_object

    @property
    def sf_object_name(self):
        """Gets the sf_object_name of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The sf_object_name of this ConnectSalesforceObject.  # noqa: E501
        :rtype: str
        """
        return self._sf_object_name

    @sf_object_name.setter
    def sf_object_name(self, sf_object_name):
        """Sets the sf_object_name of this ConnectSalesforceObject.

          # noqa: E501

        :param sf_object_name: The sf_object_name of this ConnectSalesforceObject.  # noqa: E501
        :type: str
        """

        self._sf_object_name = sf_object_name

    @property
    def update_fields(self):
        """Gets the update_fields of this ConnectSalesforceObject.  # noqa: E501

          # noqa: E501

        :return: The update_fields of this ConnectSalesforceObject.  # noqa: E501
        :rtype: list[ConnectSalesforceField]
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this ConnectSalesforceObject.

          # noqa: E501

        :param update_fields: The update_fields of this ConnectSalesforceObject.  # noqa: E501
        :type: list[ConnectSalesforceField]
        """

        self._update_fields = update_fields

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
        if issubclass(ConnectSalesforceObject, dict):
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
        if not isinstance(other, ConnectSalesforceObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
