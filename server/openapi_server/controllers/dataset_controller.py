from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.dataset_create_response import DatasetCreateResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_datasets import PageOfDatasets  # noqa: E501
from openapi_server.config import Config
from openapi_server.controllers.annotation_store_controller import delete_annotation_store_by_name, list_annotation_stores  # noqa: E501
from openapi_server.controllers.fhir_store_controller import delete_fhir_store_by_name, list_fhir_stores  # noqa: E501


def create_dataset(dataset_id):  # noqa: E501
    """Create a dataset

    Create a dataset with the name specified # noqa: E501

    :param dataset_id: The ID of the dataset that is being created
    :type dataset_id: str

    :rtype: DatasetCreateResponse
    """
    res = None
    status = None
    try:
        try:
            dataset_name = "datasets/%s" % (dataset_id,)
            dataset = Dataset(name=dataset_name)
        except Exception as error:
            status = 400
            res = Error("Invalid input", status, str(error))
            return res, status

        try:
            db_dataset = DbDataset(name=dataset.name).save()
            dataset = Dataset.from_dict(db_dataset.to_dict())
            res = DatasetCreateResponse(name=dataset.name)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_dataset(dataset_id):  # noqa: E501
    """Delete a dataset by ID

    Deletes the dataset for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str

    :rtype: DatasetCreateResponse
    """
    res = None
    status = None
    try:
        dataset_name = "datasets/%s" % (dataset_id,)
        db_dataset = DbDataset.objects.get(name=dataset_name)
        # delete resources in the dataset
        stores = list_annotation_stores(dataset_id)[0]
        for store in stores.annotation_stores:
            delete_annotation_store_by_name(store.name)
        stores = list_fhir_stores(dataset_id)[0]
        for store in stores.fhir_stores:
            delete_fhir_store_by_name(store.name)
        db_dataset.delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_dataset(dataset_id):  # noqa: E501
    """Get a dataset by ID

    Returns the dataset for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str

    :rtype: Dataset
    """
    res = None
    status = None
    try:
        dataset_name = "datasets/%s" % (dataset_id,)
        db_dataset = DbDataset.objects.get(name=dataset_name)
        res = Dataset.from_dict(db_dataset.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_datasets(limit=None, offset=None):  # noqa: E501
    """Get all datasets

    Returns the datasets # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfDatasets
    """
    res = None
    status = None
    try:
        db_datasets = DbDataset.objects.skip(offset).limit(limit)
        datasets = [Dataset.from_dict(d.to_dict()) for d in db_datasets]
        next_ = ""
        if len(datasets) == limit:
            next_ = "%s/datasets?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)
        res = PageOfDatasets(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            datasets=datasets)
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
