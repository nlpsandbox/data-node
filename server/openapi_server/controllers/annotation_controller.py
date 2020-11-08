# import connexion
# import six

# from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.one_of_stored_annotation_stored_date_annotation import OneOfStoredAnnotationStoredDateAnnotation  # noqa: E501
# from openapi_server.models.page_of_annotations import PageOfAnnotations  # noqa: E501
# from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
# from openapi_server import util


def create_annotation(dataset_id, store_id, unknown_base_type=None):  # noqa: E501
    """Create an annotation linked to a dataset ID and store ID

    Create an annotation # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param unknown_base_type:
    :type unknown_base_type: dict | bytes

    :rtype: OneOfStoredAnnotationStoredDateAnnotation
    """
    # if connexion.request.is_json:
    #     unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_annotation(dataset_id, store_id, id):  # noqa: E501
    """Delete an annotation by ID

    Deletes the annotation for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param id: The ID of the dataset to delete
    :type id: str

    :rtype: OneOfStoredAnnotationStoredDateAnnotation
    """
    return 'do some magic!'


def get_annotation(dataset_id, store_id, id):  # noqa: E501
    """Get an annotation by ID

    Returns the annotation for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param id: The ID of the annotation to fetch
    :type id: str

    :rtype: OneOfStoredAnnotationStoredDateAnnotation
    """
    return 'do some magic!'


def list_annotations(dataset_id, store_id, limit=None, offset=None):  # noqa: E501
    """Get all annotations linked to a dataset ID and store ID

    Returns the annotations for a given dataset ID and store ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfAnnotations
    """
    return 'do some magic!'
