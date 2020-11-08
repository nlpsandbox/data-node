# import connexion
# import six

# from openapi_server.models.annotation_store import AnnotationStore  # noqa: E501
# from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.page_of_annotation_stores import PageOfAnnotationStores  # noqa: E501
# from openapi_server import util


def create_annotation_store(dataset_id, annotation_store=None):  # noqa: E501
    """Create an annotation store linked to a dataset ID

    Create an annotation store with the name specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store:
    :type annotation_store: dict | bytes

    :rtype: AnnotationStore
    """
    # if connexion.request.is_json:
    #     annotation_store = AnnotationStore.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_annotation_store(dataset_id, id):  # noqa: E501
    """Delete an annotation store by ID

    Deletes the annotation store for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param id: The ID of the annotation store
    :type id: str

    :rtype: AnnotationStore
    """
    return 'do some magic!'


def get_annotation_store(dataset_id, id):  # noqa: E501
    """Get an annotation store by ID

    Returns the annotation store for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param id: The ID of the annotation store
    :type id: str

    :rtype: AnnotationStore
    """
    return 'do some magic!'


def list_annotation_stores(dataset_id, limit=None, offset=None):  # noqa: E501
    """Get all annotation stores by dataset ID

    Returns the annotation stores for a given dataset ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfAnnotationStores
    """
    return 'do some magic!'
