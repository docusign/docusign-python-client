# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DisplayApplianceInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, document_data=None, document_pages=None, envelope_data=None, page_data=None, recipient_data=None):
        """
        DisplayApplianceInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'document_data': 'list[DisplayApplianceDocument]',
            'document_pages': 'list[DisplayApplianceDocumentPage]',
            'envelope_data': 'DisplayApplianceEnvelope',
            'page_data': 'list[DisplayAppliancePage]',
            'recipient_data': 'list[DisplayApplianceRecipient]'
        }

        self.attribute_map = {
            'document_data': 'documentData',
            'document_pages': 'documentPages',
            'envelope_data': 'envelopeData',
            'page_data': 'pageData',
            'recipient_data': 'recipientData'
        }

        self._document_data = document_data
        self._document_pages = document_pages
        self._envelope_data = envelope_data
        self._page_data = page_data
        self._recipient_data = recipient_data

    @property
    def document_data(self):
        """
        Gets the document_data of this DisplayApplianceInfo.
        

        :return: The document_data of this DisplayApplianceInfo.
        :rtype: list[DisplayApplianceDocument]
        """
        return self._document_data

    @document_data.setter
    def document_data(self, document_data):
        """
        Sets the document_data of this DisplayApplianceInfo.
        

        :param document_data: The document_data of this DisplayApplianceInfo.
        :type: list[DisplayApplianceDocument]
        """

        self._document_data = document_data

    @property
    def document_pages(self):
        """
        Gets the document_pages of this DisplayApplianceInfo.
        

        :return: The document_pages of this DisplayApplianceInfo.
        :rtype: list[DisplayApplianceDocumentPage]
        """
        return self._document_pages

    @document_pages.setter
    def document_pages(self, document_pages):
        """
        Sets the document_pages of this DisplayApplianceInfo.
        

        :param document_pages: The document_pages of this DisplayApplianceInfo.
        :type: list[DisplayApplianceDocumentPage]
        """

        self._document_pages = document_pages

    @property
    def envelope_data(self):
        """
        Gets the envelope_data of this DisplayApplianceInfo.

        :return: The envelope_data of this DisplayApplianceInfo.
        :rtype: DisplayApplianceEnvelope
        """
        return self._envelope_data

    @envelope_data.setter
    def envelope_data(self, envelope_data):
        """
        Sets the envelope_data of this DisplayApplianceInfo.

        :param envelope_data: The envelope_data of this DisplayApplianceInfo.
        :type: DisplayApplianceEnvelope
        """

        self._envelope_data = envelope_data

    @property
    def page_data(self):
        """
        Gets the page_data of this DisplayApplianceInfo.
        

        :return: The page_data of this DisplayApplianceInfo.
        :rtype: list[DisplayAppliancePage]
        """
        return self._page_data

    @page_data.setter
    def page_data(self, page_data):
        """
        Sets the page_data of this DisplayApplianceInfo.
        

        :param page_data: The page_data of this DisplayApplianceInfo.
        :type: list[DisplayAppliancePage]
        """

        self._page_data = page_data

    @property
    def recipient_data(self):
        """
        Gets the recipient_data of this DisplayApplianceInfo.
        

        :return: The recipient_data of this DisplayApplianceInfo.
        :rtype: list[DisplayApplianceRecipient]
        """
        return self._recipient_data

    @recipient_data.setter
    def recipient_data(self, recipient_data):
        """
        Sets the recipient_data of this DisplayApplianceInfo.
        

        :param recipient_data: The recipient_data of this DisplayApplianceInfo.
        :type: list[DisplayApplianceRecipient]
        """

        self._recipient_data = recipient_data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
