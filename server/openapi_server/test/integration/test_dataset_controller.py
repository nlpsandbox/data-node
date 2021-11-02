# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestDatasetController(BaseTestCase):
    """DatasetController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbDataset.objects().delete()

    def tearDown(self):
        util.disconnect_db()

    def test_create_dataset(self):
        """Test case for create_dataset

        Create a dataset
        """
        dataset = {}
        query_string = [('datasetId', 'awesome-dataset')]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets',
            method='POST',
            headers=headers,
            data=json.dumps(dataset),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(
            response, 201,
            'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_dataset(self):
        """Test case for delete_dataset

        Delete a dataset by ID
        """
        util.create_test_dataset("awesome-dataset")
        headers = {
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}'.format(
                dataset_id='awesome-dataset'
            ),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dataset(self):
        """Test case for get_dataset

        Get a dataset by ID
        """
        util.create_test_dataset("awesome-dataset")
        headers = {
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}'.format(
                dataset_id='awesome-dataset'
            ),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_datasets(self):
        """Test case for list_datasets

        Get all datasets
        """
        util.create_test_dataset("awesome-dataset")
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
