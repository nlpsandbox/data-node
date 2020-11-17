# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.annotation_store import AnnotationStore  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_annotation_stores import PageOfAnnotationStores  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAnnotationStoreController(BaseTestCase):
    """AnnotationStoreController integration test stubs"""

    def test_create_annotation_store(self):
        """Test case for create_annotation_store

        Create an annotation store
        """
        annotation_store = {
  "name" : "name"
}
        query_string = [('annotationStoreId', awesome-annotation-store)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore'.format(dataset_id='dataset_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(annotation_store),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_annotation_store(self):
        """Test case for delete_annotation_store

        Delete an annotation store
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore/{annotation_store_id}'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_annotation_store(self):
        """Test case for get_annotation_store

        Get an annotation store
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore/{annotation_store_id}'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_annotation_stores(self):
        """Test case for list_annotation_stores

        List the annotation stores in a dataset
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStore'.format(dataset_id='dataset_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
