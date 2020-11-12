import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.fhir_store import FhirStore  # noqa: E501
from openapi_server.models.fhir_stores import FhirStores  # noqa: E501
from openapi_server import util


def create_fhir_store(dataset_id, fhir_store_id, fhir_store=None):  # noqa: E501
    """Create a FHIR store

    Create a FHIR store with the ID specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store that is being created.
    :type fhir_store_id: str
    :param fhir_store: 
    :type fhir_store: dict | bytes

    :rtype: FhirStore
    """
    if connexion.request.is_json:
        fhir_store = FhirStore.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_fhir_store(dataset_id, fhir_store_id):  # noqa: E501
    """Delete a FHIR store

    Deletes the FHIR store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str

    :rtype: FhirStore
    """
    return 'do some magic!'


def get_fhir_store(dataset_id, fhir_store_id):  # noqa: E501
    """Get a FHIR store

    Returns the FHIR store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str

    :rtype: FhirStore
    """
    return 'do some magic!'


def list_fhir_stores(dataset_id):  # noqa: E501
    """List the FHIR stores in a dataset

    Returns the FHIR stores # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str

    :rtype: FhirStores
    """
    return 'do some magic!'
