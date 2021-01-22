# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_patients import PageOfPatients  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.models.patient_create_request import PatientCreateRequest  # noqa: E501
from openapi_server.models.patient_create_response import PatientCreateResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPatientController(BaseTestCase):
    """PatientController integration test stubs"""

    def test_create_patient(self):
        """Test case for create_patient

        Create a FHIR patient
        """
        patient_create_request = {
  "identifier" : "identifier",
  "gender" : "male"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Patient'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(patient_create_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_patient(self):
        """Test case for delete_patient

        Delete a FHIR patient
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Patient/{patient_id}'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example', patient_id='patient_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_patient(self):
        """Test case for get_patient

        Get a FHIR patient
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Patient/{patient_id}'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example', patient_id='patient_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_patients(self):
        """Test case for list_patients

        List the Patients in a FHIR store
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Patient'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
