import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.models.annotation_store import AnnotationStore  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_annotation_stores import PageOfAnnotationStores  # noqa: E501
from openapi_server.dbmodels.annotation import Annotation as DbAnnotation  # noqa: E501
from openapi_server.dbmodels.annotation_store import AnnotationStore as DbAnnotationStore  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.config import Config


def create_annotation_store(dataset_id, annotation_store_id, annotation_store=None):  # noqa: E501
    """Create an annotation store

    Create an annotation store with the ID specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store that is being created.
    :type annotation_store_id: str
    :param annotation_store:
    :type annotation_store: dict | bytes

    :rtype: AnnotationStore
    """
    res = None
    status = None

    # build the store name
    fhir_store = None
    if dataset_id is not None and annotation_store_id is not None:
        store_name = "datasets/%s/annotationStores/%s" % (dataset_id, annotation_store_id)  # noqa: E501
        fhir_store = AnnotationStore(name=store_name)
    elif connexion.request.is_json:
        fhir_store = AnnotationStore.from_dict(connexion.request.get_json())

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
            db_fhir_store = DbAnnotationStore(name=fhir_store.name).save()
            res = AnnotationStore.from_dict(db_fhir_store.to_dict())
            status = 200
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def delete_annotation_store(dataset_id, annotation_store_id):  # noqa: E501
    """Delete an annotation store

    Deletes the annotation store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str

    :rtype: AnnotationStore
    """
    store_name = "datasets/%s/annotationStores/%s" % (dataset_id, annotation_store_id)  # noqa: E501
    return delete_annotation_store_by_name(store_name)


def delete_annotation_store_by_name(annotation_store_by_name):
    res = None
    status = None
    try:
        db_fhir_store = DbAnnotationStore.objects.get(
            name=annotation_store_by_name)
        # delete resources in the store
        DbAnnotation.objects(annotationStoreName=annotation_store_by_name) \
            .delete()
        # delete the store
        res = AnnotationStore.from_dict(db_fhir_store.to_dict())
        db_fhir_store.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_annotation_store(dataset_id, annotation_store_id):  # noqa: E501
    """Get an annotation store

    Returns the annotation store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str

    :rtype: AnnotationStore
    """
    res = None
    status = None
    try:
        store_name = "datasets/%s/annotationStores/%s" % (dataset_id, annotation_store_id)  # noqa: E501
        db_fhir_store = DbAnnotationStore.objects.get(name=store_name)
        res = AnnotationStore.from_dict(db_fhir_store.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_annotation_stores(dataset_id, limit=None, offset=None):  # noqa: E501
    """List the annotation stores in a dataset

    Returns the annotation stores # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfAnnotationStores
    """
    res = None
    status = None
    try:
        db_annotation_stores = DbAnnotationStore.objects(
            name__startswith='datasets/{dataset_id}/'.format(
                dataset_id=dataset_id
            )).skip(offset).limit(limit)
        annotation_stores = [AnnotationStore.from_dict(s.to_dict()) for s in db_annotation_stores]  # noqa: E501
        next_ = ""
        if len(annotation_stores) == limit:
            next_ = "%s/datasets/%s/annotationStores?limit=%s&offset=%s" % \
                (Config().server_api_url, dataset_id, limit, offset + limit)
        res = PageOfAnnotationStores(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            annotation_stores=annotation_stores)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
