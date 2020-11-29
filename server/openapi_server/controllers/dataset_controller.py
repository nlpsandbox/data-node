from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_datasets import PageOfDatasets  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.config import Config


def create_dataset(dataset_id, dataset=None):  # noqa: E501
    """Create a dataset

    Create a dataset with the name specified # noqa: E501

    :param dataset_id: The ID of the dataset that is being created.
    :type dataset_id: str
    :param dataset:
    :type dataset: dict | bytes

    :rtype: Dataset
    """
    res = None
    status = None
    if dataset_id is not None:
        try:
            dataset_name = "datasets/%s" % (dataset_id,)
            dataset = Dataset(name=dataset_name)
            db_dataset = DbDataset(name=dataset.name).save()
            res = Dataset.from_dict(db_dataset.to_dict())
            status = 200
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 422
        res = Error("The query parameter datasetId is not specified", status)

    return res, status


def delete_dataset(dataset_id):  # noqa: E501
    """Delete a dataset by ID

    Deletes the dataset for a given ID # noqa: E501

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
        db_dataset.delete()
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
        print(f"dataset name: {dataset_name}")
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
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
