# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore
from openapi_server.dbmodels.patient import Patient as DbPatient
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestPatientController(BaseTestCase):
    """PatientController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbDataset.objects().delete()
        DbFhirStore.objects().delete()
        DbPatient.objects().delete()
        util.create_test_dataset('awesome-dataset')
        util.create_test_fhir_store('awesome-dataset', 'awesome-fhir-store')

    def tearDown(self):
        util.disconnect_db()

    def test_create_patient(self):
        """Test case for create_patient

        Create a FHIR Patient
        """
        patient = {
            "identifier": "identifier",
            "gender": "male",
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Patient'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store'),
            method='POST',
            headers=headers,
            data=json.dumps(patient),
            content_type='application/json')
        self.assert201(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_patient(self):
        """Test case for delete_patient

        Delete a FHIR Patient
        """
        patient = util.create_test_patient(
            'awesome-dataset', 'awesome-fhir-store')
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Patient/{patient_id}'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store',
                patient_id=patient.id),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_patient(self):
        """Test case for get_patient

        Get a FHIR Patient
        """
        patient = util.create_test_patient(
            'awesome-dataset', 'awesome-fhir-store')
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Patient/{patient_id}'.format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store',
                patient_id=patient.id),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_patients(self):
        """Test case for list_patients

        List the Patients in a FHIR store
        """
        util.create_test_patient('awesome-dataset', 'awesome-fhir-store')
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
            '/fhir/Patient'
            .format(
                dataset_id='awesome-dataset',
                fhir_store_id='awesome-fhir-store'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
