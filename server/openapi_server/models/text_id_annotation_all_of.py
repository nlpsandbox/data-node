# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TextIdAnnotationAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id_type=None):  # noqa: E501
        """TextIdAnnotationAllOf - a model defined in OpenAPI

        :param id_type: The id_type of this TextIdAnnotationAllOf.  # noqa: E501
        :type id_type: str
        """
        self.openapi_types = {
            'id_type': str
        }

        self.attribute_map = {
            'id_type': 'idType'
        }

        self._id_type = id_type

    @classmethod
    def from_dict(cls, dikt) -> 'TextIdAnnotationAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextIdAnnotation_allOf of this TextIdAnnotationAllOf.  # noqa: E501
        :rtype: TextIdAnnotationAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_type(self):
        """Gets the id_type of this TextIdAnnotationAllOf.

        Type of ID information  # noqa: E501

        :return: The id_type of this TextIdAnnotationAllOf.
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this TextIdAnnotationAllOf.

        Type of ID information  # noqa: E501

        :param id_type: The id_type of this TextIdAnnotationAllOf.
        :type id_type: str
        """
        allowed_values = ["account", "bio_id", "device", "health_plan", "id_num", "license", "medical_record", "ssn", "vehicle"]  # noqa: E501
        if id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `id_type` ({0}), must be one of {1}"
                .format(id_type, allowed_values)
            )

        self._id_type = id_type