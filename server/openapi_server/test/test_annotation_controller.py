# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

# from openapi_server.models.any_of_text_date_annotation_text_person_name_annotation_text_physical_address_annotation import AnyOfTextDateAnnotationTextPersonNameAnnotationTextPhysicalAddressAnnotation  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_annotations import PageOfAnnotations  # noqa: E501
# from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAnnotationController(BaseTestCase):
    """AnnotationController integration test stubs"""

    def test_create_annotation(self):
        """Test case for create_annotation

        Create an annotation
        """
        unknown_base_type = {}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore/{annotation_store_id}/annotations'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_annotation(self):
        """Test case for delete_annotation

        Delete an annotation
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore/{annotation_store_id}/annotations/{annotation_id}'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example', annotation_id='annotation_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_annotation(self):
        """Test case for get_annotation

        Get an annotation
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore/{annotation_store_id}/annotations/{annotation_id}'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example', annotation_id='annotation_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_annotations(self):
        """Test case for list_annotations

        List the annotations in an annotation store
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore/{annotation_store_id}/annotations'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
