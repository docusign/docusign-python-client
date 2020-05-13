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


class Folder(object):
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
        'error_details': 'ErrorDetails',
        'filter': 'Filter',
        'folder_id': 'str',
        'folder_items': 'list[FolderItemV2]',
        'folders': 'list[Folder]',
        'has_access': 'str',
        'has_sub_folders': 'str',
        'item_count': 'str',
        'name': 'str',
        'owner': 'UserInfo',
        'parent_folder_id': 'str',
        'parent_folder_uri': 'str',
        'sub_folder_count': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'error_details': 'errorDetails',
        'filter': 'filter',
        'folder_id': 'folderId',
        'folder_items': 'folderItems',
        'folders': 'folders',
        'has_access': 'hasAccess',
        'has_sub_folders': 'hasSubFolders',
        'item_count': 'itemCount',
        'name': 'name',
        'owner': 'owner',
        'parent_folder_id': 'parentFolderId',
        'parent_folder_uri': 'parentFolderUri',
        'sub_folder_count': 'subFolderCount',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, error_details=None, filter=None, folder_id=None, folder_items=None, folders=None, has_access=None, has_sub_folders=None, item_count=None, name=None, owner=None, parent_folder_id=None, parent_folder_uri=None, sub_folder_count=None, type=None, uri=None):  # noqa: E501
        """Folder - a model defined in Swagger"""  # noqa: E501

        self._error_details = None
        self._filter = None
        self._folder_id = None
        self._folder_items = None
        self._folders = None
        self._has_access = None
        self._has_sub_folders = None
        self._item_count = None
        self._name = None
        self._owner = None
        self._parent_folder_id = None
        self._parent_folder_uri = None
        self._sub_folder_count = None
        self._type = None
        self._uri = None
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details
        if filter is not None:
            self.filter = filter
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_items is not None:
            self.folder_items = folder_items
        if folders is not None:
            self.folders = folders
        if has_access is not None:
            self.has_access = has_access
        if has_sub_folders is not None:
            self.has_sub_folders = has_sub_folders
        if item_count is not None:
            self.item_count = item_count
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if parent_folder_uri is not None:
            self.parent_folder_uri = parent_folder_uri
        if sub_folder_count is not None:
            self.sub_folder_count = sub_folder_count
        if type is not None:
            self.type = type
        if uri is not None:
            self.uri = uri

    @property
    def error_details(self):
        """Gets the error_details of this Folder.  # noqa: E501


        :return: The error_details of this Folder.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Folder.


        :param error_details: The error_details of this Folder.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def filter(self):
        """Gets the filter of this Folder.  # noqa: E501


        :return: The filter of this Folder.  # noqa: E501
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Folder.


        :param filter: The filter of this Folder.  # noqa: E501
        :type: Filter
        """

        self._filter = filter

    @property
    def folder_id(self):
        """Gets the folder_id of this Folder.  # noqa: E501

          # noqa: E501

        :return: The folder_id of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this Folder.

          # noqa: E501

        :param folder_id: The folder_id of this Folder.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_items(self):
        """Gets the folder_items of this Folder.  # noqa: E501

        A list of the envelopes in the specified folder or folders.   # noqa: E501

        :return: The folder_items of this Folder.  # noqa: E501
        :rtype: list[FolderItemV2]
        """
        return self._folder_items

    @folder_items.setter
    def folder_items(self, folder_items):
        """Sets the folder_items of this Folder.

        A list of the envelopes in the specified folder or folders.   # noqa: E501

        :param folder_items: The folder_items of this Folder.  # noqa: E501
        :type: list[FolderItemV2]
        """

        self._folder_items = folder_items

    @property
    def folders(self):
        """Gets the folders of this Folder.  # noqa: E501

        A collection of folder objects returned in a response.  # noqa: E501

        :return: The folders of this Folder.  # noqa: E501
        :rtype: list[Folder]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this Folder.

        A collection of folder objects returned in a response.  # noqa: E501

        :param folders: The folders of this Folder.  # noqa: E501
        :type: list[Folder]
        """

        self._folders = folders

    @property
    def has_access(self):
        """Gets the has_access of this Folder.  # noqa: E501

          # noqa: E501

        :return: The has_access of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._has_access

    @has_access.setter
    def has_access(self, has_access):
        """Sets the has_access of this Folder.

          # noqa: E501

        :param has_access: The has_access of this Folder.  # noqa: E501
        :type: str
        """

        self._has_access = has_access

    @property
    def has_sub_folders(self):
        """Gets the has_sub_folders of this Folder.  # noqa: E501

          # noqa: E501

        :return: The has_sub_folders of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._has_sub_folders

    @has_sub_folders.setter
    def has_sub_folders(self, has_sub_folders):
        """Sets the has_sub_folders of this Folder.

          # noqa: E501

        :param has_sub_folders: The has_sub_folders of this Folder.  # noqa: E501
        :type: str
        """

        self._has_sub_folders = has_sub_folders

    @property
    def item_count(self):
        """Gets the item_count of this Folder.  # noqa: E501

          # noqa: E501

        :return: The item_count of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this Folder.

          # noqa: E501

        :param item_count: The item_count of this Folder.  # noqa: E501
        :type: str
        """

        self._item_count = item_count

    @property
    def name(self):
        """Gets the name of this Folder.  # noqa: E501

          # noqa: E501

        :return: The name of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Folder.

          # noqa: E501

        :param name: The name of this Folder.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Folder.  # noqa: E501


        :return: The owner of this Folder.  # noqa: E501
        :rtype: UserInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Folder.


        :param owner: The owner of this Folder.  # noqa: E501
        :type: UserInfo
        """

        self._owner = owner

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this Folder.  # noqa: E501

          # noqa: E501

        :return: The parent_folder_id of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this Folder.

          # noqa: E501

        :param parent_folder_id: The parent_folder_id of this Folder.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def parent_folder_uri(self):
        """Gets the parent_folder_uri of this Folder.  # noqa: E501

          # noqa: E501

        :return: The parent_folder_uri of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_uri

    @parent_folder_uri.setter
    def parent_folder_uri(self, parent_folder_uri):
        """Sets the parent_folder_uri of this Folder.

          # noqa: E501

        :param parent_folder_uri: The parent_folder_uri of this Folder.  # noqa: E501
        :type: str
        """

        self._parent_folder_uri = parent_folder_uri

    @property
    def sub_folder_count(self):
        """Gets the sub_folder_count of this Folder.  # noqa: E501

          # noqa: E501

        :return: The sub_folder_count of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._sub_folder_count

    @sub_folder_count.setter
    def sub_folder_count(self, sub_folder_count):
        """Sets the sub_folder_count of this Folder.

          # noqa: E501

        :param sub_folder_count: The sub_folder_count of this Folder.  # noqa: E501
        :type: str
        """

        self._sub_folder_count = sub_folder_count

    @property
    def type(self):
        """Gets the type of this Folder.  # noqa: E501

          # noqa: E501

        :return: The type of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Folder.

          # noqa: E501

        :param type: The type of this Folder.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this Folder.  # noqa: E501

          # noqa: E501

        :return: The uri of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Folder.

          # noqa: E501

        :param uri: The uri of this Folder.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(Folder, dict):
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
        if not isinstance(other, Folder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
