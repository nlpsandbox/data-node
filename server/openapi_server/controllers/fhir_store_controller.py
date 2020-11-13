import connexion
from mongoengine.errors import DoesNotExist

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.fhir_store import FhirStore  # noqa: E501
from openapi_server.models.fhir_stores import FhirStores  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore
from openapi_server.config import Config


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
    res = None
    status = None

    # build the store name
    fhir_store = None
    if dataset_id is not None and fhir_store_id is not None:
        store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)
        fhir_store = FhirStore(name=store_name)
    elif connexion.request.is_json:
        fhir_store = FhirStore.from_dict(connexion.request.get_json())

    # check that the dataset specified exists
    try:
        tokens = fhir_store.name.split('/')
        dataset_name = "/".join(tokens[:2])
        DbDataset.objects.get(name=dataset_name)
    except DoesNotExist:
        status = 404
        res = Error("The specified dataset was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    # create the store
    if status is None:
        try:
            db_fhir_store = DbFhirStore(name=fhir_store.name).save()
            res = FhirStore.from_dict(db_fhir_store.to_dict())
            status = 201
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def delete_fhir_store(dataset_id, fhir_store_id):  # noqa: E501
    """Delete a FHIR store

    Deletes the FHIR store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str

    :rtype: FhirStore
    """
    res = None
    status = None
    try:
        store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)
        db_fhir_store = DbFhirStore.objects.get(name=store_name)
        res = FhirStore.from_dict(db_fhir_store.to_dict())
        db_fhir_store.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_fhir_store(dataset_id, fhir_store_id):  # noqa: E501
    """Get a FHIR store

    Returns the FHIR store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str

    :rtype: FhirStore
    """
    res = None
    status = None
    try:
        store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)
        db_fhir_store = DbFhirStore.objects.get(name=store_name)
        res = FhirStore.from_dict(db_fhir_store.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_fhir_stores(dataset_id):  # noqa: E501
    """List the FHIR stores in a dataset

    Returns the FHIR stores # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str

    :rtype: FhirStores
    """
    res = None
    status = None
    try:
        dataset_name = "datasets/%s" % (dataset_id)
        db_fhir_stores = DbFhirStore.objects(name__startswith=dataset_name)
        res = FhirStores(fhir_stores=[
            FhirStore.from_dict(s.to_dict()) for s in db_fhir_stores])
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
