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


class EnvelopesInformation(object):
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
        'continuation_token': 'str',
        'end_position': 'str',
        'envelopes': 'list[Envelope]',
        'envelope_transaction_statuses': 'list[EnvelopeTransactionStatus]',
        'folders': 'list[Folder]',
        'last_queried_date_time': 'str',
        'next_uri': 'str',
        'previous_uri': 'str',
        'result_set_size': 'str',
        'start_position': 'str',
        'total_set_size': 'str'
    }

    attribute_map = {
        'continuation_token': 'continuationToken',
        'end_position': 'endPosition',
        'envelopes': 'envelopes',
        'envelope_transaction_statuses': 'envelopeTransactionStatuses',
        'folders': 'folders',
        'last_queried_date_time': 'lastQueriedDateTime',
        'next_uri': 'nextUri',
        'previous_uri': 'previousUri',
        'result_set_size': 'resultSetSize',
        'start_position': 'startPosition',
        'total_set_size': 'totalSetSize'
    }

    def __init__(self, continuation_token=None, end_position=None, envelopes=None, envelope_transaction_statuses=None, folders=None, last_queried_date_time=None, next_uri=None, previous_uri=None, result_set_size=None, start_position=None, total_set_size=None):  # noqa: E501
        """EnvelopesInformation - a model defined in Swagger"""  # noqa: E501

        self._continuation_token = None
        self._end_position = None
        self._envelopes = None
        self._envelope_transaction_statuses = None
        self._folders = None
        self._last_queried_date_time = None
        self._next_uri = None
        self._previous_uri = None
        self._result_set_size = None
        self._start_position = None
        self._total_set_size = None
        self.discriminator = None

        if continuation_token is not None:
            self.continuation_token = continuation_token
        if end_position is not None:
            self.end_position = end_position
        if envelopes is not None:
            self.envelopes = envelopes
        if envelope_transaction_statuses is not None:
            self.envelope_transaction_statuses = envelope_transaction_statuses
        if folders is not None:
            self.folders = folders
        if last_queried_date_time is not None:
            self.last_queried_date_time = last_queried_date_time
        if next_uri is not None:
            self.next_uri = next_uri
        if previous_uri is not None:
            self.previous_uri = previous_uri
        if result_set_size is not None:
            self.result_set_size = result_set_size
        if start_position is not None:
            self.start_position = start_position
        if total_set_size is not None:
            self.total_set_size = total_set_size

    @property
    def continuation_token(self):
        """Gets the continuation_token of this EnvelopesInformation.  # noqa: E501

          # noqa: E501

        :return: The continuation_token of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this EnvelopesInformation.

          # noqa: E501

        :param continuation_token: The continuation_token of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._continuation_token = continuation_token

    @property
    def end_position(self):
        """Gets the end_position of this EnvelopesInformation.  # noqa: E501

        The last position in the result set.   # noqa: E501

        :return: The end_position of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """Sets the end_position of this EnvelopesInformation.

        The last position in the result set.   # noqa: E501

        :param end_position: The end_position of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._end_position = end_position

    @property
    def envelopes(self):
        """Gets the envelopes of this EnvelopesInformation.  # noqa: E501

          # noqa: E501

        :return: The envelopes of this EnvelopesInformation.  # noqa: E501
        :rtype: list[Envelope]
        """
        return self._envelopes

    @envelopes.setter
    def envelopes(self, envelopes):
        """Sets the envelopes of this EnvelopesInformation.

          # noqa: E501

        :param envelopes: The envelopes of this EnvelopesInformation.  # noqa: E501
        :type: list[Envelope]
        """

        self._envelopes = envelopes

    @property
    def envelope_transaction_statuses(self):
        """Gets the envelope_transaction_statuses of this EnvelopesInformation.  # noqa: E501

          # noqa: E501

        :return: The envelope_transaction_statuses of this EnvelopesInformation.  # noqa: E501
        :rtype: list[EnvelopeTransactionStatus]
        """
        return self._envelope_transaction_statuses

    @envelope_transaction_statuses.setter
    def envelope_transaction_statuses(self, envelope_transaction_statuses):
        """Sets the envelope_transaction_statuses of this EnvelopesInformation.

          # noqa: E501

        :param envelope_transaction_statuses: The envelope_transaction_statuses of this EnvelopesInformation.  # noqa: E501
        :type: list[EnvelopeTransactionStatus]
        """

        self._envelope_transaction_statuses = envelope_transaction_statuses

    @property
    def folders(self):
        """Gets the folders of this EnvelopesInformation.  # noqa: E501

          # noqa: E501

        :return: The folders of this EnvelopesInformation.  # noqa: E501
        :rtype: list[Folder]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this EnvelopesInformation.

          # noqa: E501

        :param folders: The folders of this EnvelopesInformation.  # noqa: E501
        :type: list[Folder]
        """

        self._folders = folders

    @property
    def last_queried_date_time(self):
        """Gets the last_queried_date_time of this EnvelopesInformation.  # noqa: E501

          # noqa: E501

        :return: The last_queried_date_time of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._last_queried_date_time

    @last_queried_date_time.setter
    def last_queried_date_time(self, last_queried_date_time):
        """Sets the last_queried_date_time of this EnvelopesInformation.

          # noqa: E501

        :param last_queried_date_time: The last_queried_date_time of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._last_queried_date_time = last_queried_date_time

    @property
    def next_uri(self):
        """Gets the next_uri of this EnvelopesInformation.  # noqa: E501

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :return: The next_uri of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this EnvelopesInformation.

        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null.   # noqa: E501

        :param next_uri: The next_uri of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """Gets the previous_uri of this EnvelopesInformation.  # noqa: E501

        The postal code for the billing address.  # noqa: E501

        :return: The previous_uri of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """Sets the previous_uri of this EnvelopesInformation.

        The postal code for the billing address.  # noqa: E501

        :param previous_uri: The previous_uri of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """Gets the result_set_size of this EnvelopesInformation.  # noqa: E501

        The number of results returned in this response.   # noqa: E501

        :return: The result_set_size of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this EnvelopesInformation.

        The number of results returned in this response.   # noqa: E501

        :param result_set_size: The result_set_size of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """Gets the start_position of this EnvelopesInformation.  # noqa: E501

        Starting position of the current result set.  # noqa: E501

        :return: The start_position of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """Sets the start_position of this EnvelopesInformation.

        Starting position of the current result set.  # noqa: E501

        :param start_position: The start_position of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._start_position = start_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this EnvelopesInformation.  # noqa: E501

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :return: The total_set_size of this EnvelopesInformation.  # noqa: E501
        :rtype: str
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this EnvelopesInformation.

        The total number of items available in the result set. This will always be greater than or equal to the value of the property returning the results in the in the response.  # noqa: E501

        :param total_set_size: The total_set_size of this EnvelopesInformation.  # noqa: E501
        :type: str
        """

        self._total_set_size = total_set_size

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
        if issubclass(EnvelopesInformation, dict):
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
        if not isinstance(other, EnvelopesInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
