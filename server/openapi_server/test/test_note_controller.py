# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.page_of_notes import PageOfNotes  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNoteController(BaseTestCase):
    """NoteController integration test stubs"""

    def test_create_note(self):
        """Test case for create_note

        Create a note
        """
        note = {
  "noteType" : "loinc:LP29684-5",
  "patientId" : "507f1f77bcf86cd799439011",
  "id" : "id",
  "text" : "This is the content of a clinical note."
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(note),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_note(self):
        """Test case for delete_note

        Delete a note
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note/{note_id}'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example', note_id='note_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_note(self):
        """Test case for get_note

        Get a note
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note/{note_id}'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example', note_id='note_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_notes(self):
        """Test case for list_notes

        List notes
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
