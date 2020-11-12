import connexion
import six

from openapi_server.models.annotation_store import AnnotationStore  # noqa: E501
from openapi_server.models.annotation_stores import AnnotationStores  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util


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
    if connexion.request.is_json:
        annotation_store = AnnotationStore.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_annotation_store(dataset_id, annotation_store_id):  # noqa: E501
    """Delete an annotation store

    Deletes the annotation store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str

    :rtype: AnnotationStore
    """
    return 'do some magic!'


def get_annotation_store(dataset_id, annotation_store_id):  # noqa: E501
    """Get an annotation store

    Returns the annotation store specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str

    :rtype: AnnotationStore
    """
    return 'do some magic!'


def list_annotation_stores(dataset_id):  # noqa: E501
    """List the annotation stores in a dataset

    Returns the annotation stores # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str

    :rtype: AnnotationStores
    """
    return 'do some magic!'
