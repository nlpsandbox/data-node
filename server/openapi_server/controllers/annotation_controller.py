import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.models.annotation import Annotation  # noqa: E501
from openapi_server.models.annotation_create_request import AnnotationCreateRequest  # noqa: E501
from openapi_server.models.annotation_create_response import AnnotationCreateResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_annotations import PageOfAnnotations  # noqa: E501
from openapi_server.dbmodels.annotation_store import AnnotationStore as DbAnnotationStore  # noqa: E501
from openapi_server.dbmodels.annotation import Annotation as DbAnnotation
from openapi_server import util
from openapi_server.config import Config


def create_annotation(dataset_id, annotation_store_id, annotation_create_request=None):  # noqa: E501
    """Create an annotation

    Create an annotation # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param annotation_create_request:
    :type annotation_create_request: dict | bytes

    :rtype: AnnotationCreateResponse
    """
    res = None
    status = None

    if dataset_id is None:
        status = 400
        res = Error("The query parameter datasetId is not specified", status)
    elif annotation_store_id is None:
        status = 400
        res = Error("The query parameter annotationStoreId is not specified", status)  # noqa: E501

    # check if the annotation store exists
    store_name = None
    if status is None:
        try:
            store_name = "datasets/%s/annotationStores/%s" % (dataset_id, annotation_store_id)  # noqa: E501
            DbAnnotationStore.objects.get(name=store_name)
        except DoesNotExist:
            status = 400
            res = Error("The specified annotation store was not found", status)
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    # create the annotation
    if status is None and connexion.request.is_json:
        try:
            annotation = Annotation.from_dict(connexion.request.get_json())
            text_date_annotations = None
            text_person_name_annotations = None
            text_physical_address_annotations = None

            if annotation.text_date_annotations is not None:
                text_date_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation.text_date_annotations]

            if annotation.text_person_name_annotations is not None:
                text_person_name_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation.text_person_name_annotations]

            if annotation.text_physical_address_annotations is not None:
                text_physical_address_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation.text_physical_address_annotations]

            annotation_source = util.change_dict_naming_convention(
                annotation.annotation_source.to_dict(),
                util.underscore_to_camel)

            # create the annotation
            db_annotation = DbAnnotation(
                annotationSource=annotation_source,
                annotationStoreName=store_name,
                textDateAnnotations=text_date_annotations,
                textPersonNameAnnotations=text_person_name_annotations,
                textPhysicalAddressAnnotations=text_physical_address_annotations  # noqa: E501
            ).save()

            annotation = Annotation.from_dict(db_annotation.to_dict())
            res = AnnotationCreateResponse(name=annotation.name)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def delete_annotation(dataset_id, annotation_store_id, annotation_id):  # noqa: E501
    """Delete an annotation

    Deletes the annotation specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param annotation_id: The ID of the annotation
    :type annotation_id: str

    :rtype: object
    """
    res = None
    status = None
    try:
        db_annotation = DbAnnotation.objects.get(id=annotation_id)
        db_annotation.delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_annotation(dataset_id, annotation_store_id, annotation_id):  # noqa: E501
    """Get an annotation

    Returns the annotation specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param annotation_id: The ID of the annotation
    :type annotation_id: str

    :rtype: Annotation
    """
    res = None
    status = None
    try:
        db_annotation = DbAnnotation.objects.get(id=annotation_id)
        res = Annotation.from_dict(db_annotation.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_annotations(dataset_id, annotation_store_id, limit=None, offset=None):  # noqa: E501
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

    :rtype: PageOfAnnotations
    """
    res = None
    status = None
    try:
        store_name = "datasets/%s/annotationStores/%s" % (dataset_id, annotation_store_id)  # noqa: E501
        db_annotations = DbAnnotation.objects(annotationStoreName=store_name) \
            .skip(offset).limit(limit)
        annotations = [Annotation.from_dict(a.to_dict()) for a in db_annotations]  # noqa: E501
        next_ = ""
        if len(annotations) == limit:
            next_ = (
                "%s/datasets/%s/annotationStores/%s/annotations"
                "?limit=%s&offset=%s") % \
                (Config().server_api_url, dataset_id, annotation_store_id, limit,  # noqa: E501
                    offset + limit)
        res = PageOfAnnotations(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            annotations=annotations)
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
