import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.fhir_store import FhirStore  # noqa: E501
from openapi_server.models.page_of_fhir_stores import PageOfFhirStores  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore
from openapi_server.dbmodels.note import Note as DbNote
from openapi_server.dbmodels.patient import Patient as DbPatient
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
            status = 200
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
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
    store_name = 'datasets/%s/fhirStores/%s' % (dataset_id, fhir_store_id)
    return delete_fhir_store_by_name(store_name)


def delete_fhir_store_by_name(fhir_store_name):
    res = None
    status = None
    try:
        db_fhir_store = DbFhirStore.objects.get(name=fhir_store_name)
        # delete resources in the store
        DbPatient.objects(fhirStoreName=fhir_store_name).delete()
        DbNote.objects(fhirStoreName=fhir_store_name).delete()
        # delete the store
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


def list_fhir_stores(dataset_id, limit=None, offset=None):  # noqa: E501
    """List the FHIR stores in a dataset

    Returns the FHIR stores # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfFhirStores
    """
    res = None
    status = None
    try:
        dataset_name = "datasets/%s" % (dataset_id,)
        db_fhir_stores = DbFhirStore.objects(
            name__startswith=dataset_name).skip(offset).limit(limit)  # noqa: E501
        fhir_stores = [FhirStore.from_dict(s.to_dict()) for s in db_fhir_stores]  # noqa: E501
        next_ = ""
        if len(fhir_stores) == limit:
            next_ = "%s/datasets/%s/FhirStores?limit=%s&offset=%s" % \
                (Config().server_api_url, dataset_id, limit, offset + limit)
        res = PageOfFhirStores(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            fhir_stores=fhir_stores)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
