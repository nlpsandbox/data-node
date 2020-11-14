import connexion
import six

# from openapi_server.models.any_of_text_date_annotation_text_person_name_annotation_text_physical_address_annotation import AnyOfTextDateAnnotationTextPersonNameAnnotationTextPhysicalAddressAnnotation  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_annotations import PageOfAnnotations  # noqa: E501
# from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def create_annotation(dataset_id, annotation_store_id, unknown_base_type=None):  # noqa: E501
    """Create an annotation

    Create an annotation # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param unknown_base_type:
    :type unknown_base_type: dict | bytes

    :rtype: AnyOfTextDateAnnotationTextPersonNameAnnotationTextPhysicalAddressAnnotation
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_annotation(dataset_id, annotation_store_id, annotation_id):  # noqa: E501
    """Delete an annotation

    Deletes the annotation specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param annotation_id: The ID of the annotation
    :type annotation_id: str

    :rtype: AnyOfTextDateAnnotationTextPersonNameAnnotationTextPhysicalAddressAnnotation
    """
    return 'do some magic!'


def get_annotation(dataset_id, annotation_store_id, annotation_id):  # noqa: E501
    """Get an annotation

    Returns the annotation specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param annotation_id: The ID of the annotation
    :type annotation_id: str

    :rtype: AnyOfTextDateAnnotationTextPersonNameAnnotationTextPhysicalAddressAnnotation
    """
    return 'do some magic!'


def list_annotations(dataset_id, annotation_store_id, limit=None, offset=None, annotation_type=None):  # noqa: E501
    """List the annotations in an annotation store

    Returns the annotations in an annotation store # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int
    :param annotation_type: Type of the annotations that must be returned
    :type annotation_type: str

    :rtype: PageOfAnnotations
    """
    return 'do some magic!'
