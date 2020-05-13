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


class PaymentDetails(object):
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
        'allowed_payment_methods': 'list[str]',
        'charge_id': 'str',
        'currency_code': 'str',
        'currency_code_metadata': 'PropertyMetadata',
        'customer_id': 'str',
        'custom_metadata': 'str',
        'custom_metadata_required': 'bool',
        'gateway_account_id': 'str',
        'gateway_account_id_metadata': 'PropertyMetadata',
        'gateway_display_name': 'str',
        'gateway_name': 'str',
        'line_items': 'list[PaymentLineItem]',
        'payment_option': 'str',
        'payment_source_id': 'str',
        'status': 'str',
        'total': 'Money'
    }

    attribute_map = {
        'allowed_payment_methods': 'allowedPaymentMethods',
        'charge_id': 'chargeId',
        'currency_code': 'currencyCode',
        'currency_code_metadata': 'currencyCodeMetadata',
        'customer_id': 'customerId',
        'custom_metadata': 'customMetadata',
        'custom_metadata_required': 'customMetadataRequired',
        'gateway_account_id': 'gatewayAccountId',
        'gateway_account_id_metadata': 'gatewayAccountIdMetadata',
        'gateway_display_name': 'gatewayDisplayName',
        'gateway_name': 'gatewayName',
        'line_items': 'lineItems',
        'payment_option': 'paymentOption',
        'payment_source_id': 'paymentSourceId',
        'status': 'status',
        'total': 'total'
    }

    def __init__(self, allowed_payment_methods=None, charge_id=None, currency_code=None, currency_code_metadata=None, customer_id=None, custom_metadata=None, custom_metadata_required=None, gateway_account_id=None, gateway_account_id_metadata=None, gateway_display_name=None, gateway_name=None, line_items=None, payment_option=None, payment_source_id=None, status=None, total=None):  # noqa: E501
        """PaymentDetails - a model defined in Swagger"""  # noqa: E501

        self._allowed_payment_methods = None
        self._charge_id = None
        self._currency_code = None
        self._currency_code_metadata = None
        self._customer_id = None
        self._custom_metadata = None
        self._custom_metadata_required = None
        self._gateway_account_id = None
        self._gateway_account_id_metadata = None
        self._gateway_display_name = None
        self._gateway_name = None
        self._line_items = None
        self._payment_option = None
        self._payment_source_id = None
        self._status = None
        self._total = None
        self.discriminator = None

        if allowed_payment_methods is not None:
            self.allowed_payment_methods = allowed_payment_methods
        if charge_id is not None:
            self.charge_id = charge_id
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_code_metadata is not None:
            self.currency_code_metadata = currency_code_metadata
        if customer_id is not None:
            self.customer_id = customer_id
        if custom_metadata is not None:
            self.custom_metadata = custom_metadata
        if custom_metadata_required is not None:
            self.custom_metadata_required = custom_metadata_required
        if gateway_account_id is not None:
            self.gateway_account_id = gateway_account_id
        if gateway_account_id_metadata is not None:
            self.gateway_account_id_metadata = gateway_account_id_metadata
        if gateway_display_name is not None:
            self.gateway_display_name = gateway_display_name
        if gateway_name is not None:
            self.gateway_name = gateway_name
        if line_items is not None:
            self.line_items = line_items
        if payment_option is not None:
            self.payment_option = payment_option
        if payment_source_id is not None:
            self.payment_source_id = payment_source_id
        if status is not None:
            self.status = status
        if total is not None:
            self.total = total

    @property
    def allowed_payment_methods(self):
        """Gets the allowed_payment_methods of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The allowed_payment_methods of this PaymentDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_payment_methods

    @allowed_payment_methods.setter
    def allowed_payment_methods(self, allowed_payment_methods):
        """Sets the allowed_payment_methods of this PaymentDetails.

          # noqa: E501

        :param allowed_payment_methods: The allowed_payment_methods of this PaymentDetails.  # noqa: E501
        :type: list[str]
        """

        self._allowed_payment_methods = allowed_payment_methods

    @property
    def charge_id(self):
        """Gets the charge_id of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The charge_id of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this PaymentDetails.

          # noqa: E501

        :param charge_id: The charge_id of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._charge_id = charge_id

    @property
    def currency_code(self):
        """Gets the currency_code of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The currency_code of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PaymentDetails.

          # noqa: E501

        :param currency_code: The currency_code of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_code_metadata(self):
        """Gets the currency_code_metadata of this PaymentDetails.  # noqa: E501


        :return: The currency_code_metadata of this PaymentDetails.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._currency_code_metadata

    @currency_code_metadata.setter
    def currency_code_metadata(self, currency_code_metadata):
        """Sets the currency_code_metadata of this PaymentDetails.


        :param currency_code_metadata: The currency_code_metadata of this PaymentDetails.  # noqa: E501
        :type: PropertyMetadata
        """

        self._currency_code_metadata = currency_code_metadata

    @property
    def customer_id(self):
        """Gets the customer_id of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this PaymentDetails.

          # noqa: E501

        :param customer_id: The customer_id of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def custom_metadata(self):
        """Gets the custom_metadata of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The custom_metadata of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._custom_metadata

    @custom_metadata.setter
    def custom_metadata(self, custom_metadata):
        """Sets the custom_metadata of this PaymentDetails.

          # noqa: E501

        :param custom_metadata: The custom_metadata of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._custom_metadata = custom_metadata

    @property
    def custom_metadata_required(self):
        """Gets the custom_metadata_required of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The custom_metadata_required of this PaymentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._custom_metadata_required

    @custom_metadata_required.setter
    def custom_metadata_required(self, custom_metadata_required):
        """Sets the custom_metadata_required of this PaymentDetails.

          # noqa: E501

        :param custom_metadata_required: The custom_metadata_required of this PaymentDetails.  # noqa: E501
        :type: bool
        """

        self._custom_metadata_required = custom_metadata_required

    @property
    def gateway_account_id(self):
        """Gets the gateway_account_id of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The gateway_account_id of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._gateway_account_id

    @gateway_account_id.setter
    def gateway_account_id(self, gateway_account_id):
        """Sets the gateway_account_id of this PaymentDetails.

          # noqa: E501

        :param gateway_account_id: The gateway_account_id of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._gateway_account_id = gateway_account_id

    @property
    def gateway_account_id_metadata(self):
        """Gets the gateway_account_id_metadata of this PaymentDetails.  # noqa: E501


        :return: The gateway_account_id_metadata of this PaymentDetails.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._gateway_account_id_metadata

    @gateway_account_id_metadata.setter
    def gateway_account_id_metadata(self, gateway_account_id_metadata):
        """Sets the gateway_account_id_metadata of this PaymentDetails.


        :param gateway_account_id_metadata: The gateway_account_id_metadata of this PaymentDetails.  # noqa: E501
        :type: PropertyMetadata
        """

        self._gateway_account_id_metadata = gateway_account_id_metadata

    @property
    def gateway_display_name(self):
        """Gets the gateway_display_name of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The gateway_display_name of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._gateway_display_name

    @gateway_display_name.setter
    def gateway_display_name(self, gateway_display_name):
        """Sets the gateway_display_name of this PaymentDetails.

          # noqa: E501

        :param gateway_display_name: The gateway_display_name of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._gateway_display_name = gateway_display_name

    @property
    def gateway_name(self):
        """Gets the gateway_name of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The gateway_name of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, gateway_name):
        """Sets the gateway_name of this PaymentDetails.

          # noqa: E501

        :param gateway_name: The gateway_name of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._gateway_name = gateway_name

    @property
    def line_items(self):
        """Gets the line_items of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The line_items of this PaymentDetails.  # noqa: E501
        :rtype: list[PaymentLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this PaymentDetails.

          # noqa: E501

        :param line_items: The line_items of this PaymentDetails.  # noqa: E501
        :type: list[PaymentLineItem]
        """

        self._line_items = line_items

    @property
    def payment_option(self):
        """Gets the payment_option of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The payment_option of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._payment_option

    @payment_option.setter
    def payment_option(self, payment_option):
        """Sets the payment_option of this PaymentDetails.

          # noqa: E501

        :param payment_option: The payment_option of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._payment_option = payment_option

    @property
    def payment_source_id(self):
        """Gets the payment_source_id of this PaymentDetails.  # noqa: E501

          # noqa: E501

        :return: The payment_source_id of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._payment_source_id

    @payment_source_id.setter
    def payment_source_id(self, payment_source_id):
        """Sets the payment_source_id of this PaymentDetails.

          # noqa: E501

        :param payment_source_id: The payment_source_id of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._payment_source_id = payment_source_id

    @property
    def status(self):
        """Gets the status of this PaymentDetails.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentDetails.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def total(self):
        """Gets the total of this PaymentDetails.  # noqa: E501


        :return: The total of this PaymentDetails.  # noqa: E501
        :rtype: Money
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PaymentDetails.


        :param total: The total of this PaymentDetails.  # noqa: E501
        :type: Money
        """

        self._total = total

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
        if issubclass(PaymentDetails, dict):
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
        if not isinstance(other, PaymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
