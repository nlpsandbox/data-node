# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util


class AnnotationStoreCreateResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None):  # noqa: E501
        """AnnotationStoreCreateResponse - a model defined in OpenAPI

        :param name: The name of this AnnotationStoreCreateResponse.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'AnnotationStoreCreateResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnnotationStoreCreateResponse of this AnnotationStoreCreateResponse.  # noqa: E501
        :rtype: AnnotationStoreCreateResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AnnotationStoreCreateResponse.

        The resource name of the annotation store, of the form datasets/{datasetId}/annotationStores/{annotationStoreId}  # noqa: E501

        :return: The name of this AnnotationStoreCreateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnnotationStoreCreateResponse.

        The resource name of the annotation store, of the form datasets/{datasetId}/annotationStores/{annotationStoreId}  # noqa: E501

        :param name: The name of this AnnotationStoreCreateResponse.
        :type name: str
        """
        if name is not None and not re.search(r'^datasets\\/[a-z0-9]+(?:-[a-z0-9]+)*\\/annotationStores\\/[a-z0-9]+(?:-[a-z0-9]+)*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^datasets\\/[a-z0-9]+(?:-[a-z0-9]+)*\\/annotationStores\\/[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._name = name
