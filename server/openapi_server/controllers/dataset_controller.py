import connexion
import six

from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_dataset import NewDataset  # noqa: E501
from openapi_server.models.page_of_datasets import PageOfDatasets  # noqa: E501
from openapi_server import util
from openapi_server.dbmodels.dataset import Dataset as DbDataset

def create_dataset(new_dataset=None):  # noqa: E501
    """Create a dataset

    Create a dataset with the name specified # noqa: E501

    :param new_dataset:
    :type new_dataset: dict | bytes

    :rtype: Dataset
    """
    if connexion.request.is_json:
        new_dataset = NewDataset.from_dict(connexion.request.get_json())  # noqa: E501
        print(f"new_dataset: {new_dataset}")
        dataset = DbDataset(name=new_dataset.name).save()
        print(f"db dataset: {dataset.to_mongo().to_dict()}")

    return 'do some magic!'


def delete_dataset(id):  # noqa: E501
    """Delete a dataset by ID

    Deletes the dataset for a given ID # noqa: E501

    :param id: The ID of the dataset
    :type id: str

    :rtype: Dataset
    """
    return 'do some magic!'


def get_dataset(id):  # noqa: E501
    """Get a dataset by ID

    Returns the dataset for a given ID # noqa: E501

    :param id: The ID of the dataset
    :type id: str

    :rtype: Dataset
    """
    return 'do some magic!'


def list_datasets(limit=None, offset=None):  # noqa: E501
    """Get all datasets

    Returns the datasets # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfDatasets
    """
    return 'do some magic!'
