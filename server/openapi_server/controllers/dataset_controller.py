import connexion
from mongoengine.errors import DoesNotExist

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
    dataset = None
    if dataset_id is not None:
        datasetName = "datasets/%s" % (dataset_id,)
        dataset = Dataset(name=datasetName)
    elif connexion.request.is_json:
        dataset = Dataset.from_dict(connexion.request.get_json())

    res = None
    status = None
    try:
        dbDataset = DbDataset(name=dataset.name).save()
        res = Dataset.from_dict(dbDataset.to_dict())
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

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
        datasetName = "datasets/%s" % (dataset_id,)
        dbDataset = DbDataset.objects.get(name=datasetName)
        res = Dataset.from_dict(dbDataset.to_dict())
        dbDataset.delete()
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
        datasetName = "datasets/%s" % (dataset_id,)
        dbDataset = DbDataset.objects.get(name=datasetName)
        res = Dataset.from_dict(dbDataset.to_dict())
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
        dbDatasets = DbDataset.objects.skip(offset).limit(limit)
        datasets = [Dataset.from_dict(d.to_dict()) for d in dbDatasets]
        next_ = "%s/datasets?limit=%s&offset=%s" % \
            (Config().server_api_url, limit, offset + limit)
        res = PageOfDatasets(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            items=datasets)
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
