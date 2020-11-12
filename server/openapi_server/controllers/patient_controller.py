import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_patients import PageOfPatients  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server import util


def create_patient(dataset_id, fhir_store_id, patient=None):  # noqa: E501
    """Create a FHIR Patient

    Create a FHIR Patient # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient: 
    :type patient: dict | bytes

    :rtype: Patient
    """
    if connexion.request.is_json:
        patient = Patient.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Delete a FHIR Patient

    Deletes the FHIR Patient specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the FHIR Patient
    :type patient_id: str

    :rtype: Patient
    """
    return 'do some magic!'


def get_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Get a FHIR Patient

    Returns the FHIR Patient specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the FHIR Patient
    :type patient_id: str

    :rtype: Patient
    """
    return 'do some magic!'


def list_patients(dataset_id, fhir_store_id, limit=None, offset=None):  # noqa: E501
    """List the Patients in a FHIR store

    Returns the Patients in a FHIR store # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfPatients
    """
    return 'do some magic!'
