# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore
from openapi_server.dbmodels.note import Note as DbNote
from openapi_server.dbmodels.patient import Patient as DbPatient
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestNoteController(BaseTestCase):
    """NoteController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbDataset.objects().delete()
        DbFhirStore.objects().delete()
        DbPatient.objects().delete()
        DbNote.objects().delete()
        util.create_test_dataset('awesome-dataset')
        util.create_test_fhir_store('awesome-dataset', 'awesome-fhir-store')
        self.patient = util.create_test_patient(
            'awesome-dataset',
            'awesome-fhir-store',
            'awesome-patient').to_dict()

    def tearDown(self):
        util.disconnect_db()

    def test_create_note(self):
        """Test case for create_note

        Create a note
        """
        note_create_request = {
            "type": "loinc:LP29684-5",
            "patientId": self.patient['identifier'],
            "text": "This is the content of a clinical note."
        }
        query_string = [('noteId', 'awesome-note')]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-API-Key': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Note'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store'),
            method='POST',
            headers=headers,
            data=json.dumps(note_create_request),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(
            response, 201,
            'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_note(self):
        """Test case for delete_note

        Delete a note
        """
        note = util.create_test_note(
            'awesome-dataset', 'awesome-fhir-store', 'awesome-note')
        headers = {
            'Accept': 'application/json',
            'X-API-Key': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Note/{note_id}'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store',
                note_id=note.identifier),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_note(self):
        """Test case for get_note

        Get a note
        """
        note = util.create_test_note(
            'awesome-dataset', 'awesome-fhir-store', 'awesome-note')
        headers = {
            'Accept': 'application/json',
            'X-API-Key': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Note/{note_id}'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store',
                note_id=note.identifier),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_notes(self):
        """Test case for list_notes

        List notes
        """
        util.create_test_note(
            'awesome-dataset', 'awesome-fhir-store', 'awesome-note')
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
            'X-API-Key': 'special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Note'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
