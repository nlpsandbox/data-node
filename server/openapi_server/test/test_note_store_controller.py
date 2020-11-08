# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note_store import NoteStore  # noqa: E501
from openapi_server.models.page_of_note_stores import PageOfNoteStores  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNoteStoreController(BaseTestCase):
    """NoteStoreController integration test stubs"""

    def test_create_note_store(self):
        """Test case for create_note_store

        Create a note store linked to a dataset ID
        """
        note_store = {
  "name" : "awesome-note-store",
  "datasetId" : "datasetId"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/noteStore'.format(dataset_id='dataset_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(note_store),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_note_store(self):
        """Test case for delete_note_store

        Delete a note store by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/noteStore/{id}'.format(dataset_id='dataset_id_example', id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_note_store(self):
        """Test case for get_note_store

        Get a note store by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/noteStore/{id}'.format(dataset_id='dataset_id_example', id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_note_stores(self):
        """Test case for list_note_stores

        Get all note stores by dataset ID
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/noteStore'.format(dataset_id='dataset_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
