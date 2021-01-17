# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.annotation_store import AnnotationStore as DbAnnotationStore  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestAnnotationStoreController(BaseTestCase):
    """AnnotationStoreController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbDataset.objects().delete()
        DbAnnotationStore.objects().delete()
        util.create_test_dataset('awesome-dataset')

    def tearDown(self):
        util.disconnect_db()

    def test_create_annotation_store(self):
        """Test case for create_annotation_store

        Create an annotation store
        """
        annotation_store = {}
        query_string = [('annotationStoreId', 'awesome-annotation-store')]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            .format(dataset_id='awesome-dataset'),
            method='POST',
            headers=headers,
            data=json.dumps(annotation_store),
            content_type='application/json',
            query_string=query_string)
        self.assert201(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_annotation_store(self):
        """Test case for delete_annotation_store

        Delete an annotation store
        """
        util.create_test_annotation_store(
            'awesome-dataset', 'awesome-annotation-store')
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            '/{annotation_store_id}'.format(
                dataset_id='awesome-dataset',
                annotation_store_id='awesome-annotation-store'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_annotation_store(self):
        """Test case for get_annotation_store

        Get an annotation store
        """
        util.create_test_annotation_store(
            'awesome-dataset', 'awesome-annotation-store')
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            '/{annotation_store_id}'.format(
                dataset_id='awesome-dataset',
                annotation_store_id='awesome-annotation-store'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_annotation_stores(self):
        """Test case for list_annotation_stores

        List the annotation stores in a dataset
        """
        util.create_test_annotation_store(
            'awesome-dataset', 'awesome-annotation-store')
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            .format(dataset_id='awesome-dataset'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
