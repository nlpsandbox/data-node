import connexion
from mongoengine.errors import DoesNotExist

from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_dataset import NewDataset  # noqa: E501
from openapi_server.models.page_of_datasets import PageOfDatasets  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.config import Config


def create_dataset(new_dataset=None):  # noqa: E501
    """Create a dataset

    Create a dataset with the name specified # noqa: E501

    :param new_dataset:
    :type new_dataset: dict | bytes

    :rtype: Dataset
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            new_dataset = NewDataset.from_dict(connexion.request.get_json())
            dbDataset = DbDataset(name=new_dataset.name).save()
            res = Dataset.from_dict(dbDataset.to_dict())
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def delete_dataset(id_):  # noqa: E501
    """Delete a dataset by ID

    Deletes the dataset for a given ID # noqa: E501

    :param id: The ID of the dataset
    :type id: str

    :rtype: Dataset
    """
    res = None
    status = None
    try:
        dbDataset = DbDataset.objects.get(id=id_)
        res = Dataset.from_dict(dbDataset.to_dict())
        dbDataset.delete()
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_dataset(id_):  # noqa: E501
    """Get a dataset by ID

    Returns the dataset for a given ID # noqa: E501

    :param id: The ID of the dataset
    :type id: str

    :rtype: Dataset
    """
    res = None
    status = None
    try:
        dbDataset = DbDataset.objects.get(id=id_)
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
