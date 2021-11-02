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
from openapi_server.config import config


def create_annotation(dataset_id, annotation_store_id, annotation_id):  # noqa: E501
    """Create an annotation

    Create an annotation # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param annotation_store_id: The ID of the annotation store
    :type annotation_store_id: str
    :param annotation_id: The ID of the annotation that is being created
    :type annotation_id: str

    :rtype: AnnotationCreateResponse
    """
    res = None
    status = None
    try:
        store_name = None
        try:
            store_name = "datasets/%s/annotationStores/%s" % \
                (dataset_id, annotation_store_id)
            DbAnnotationStore.objects.get(name=store_name)
        except DoesNotExist:
            status = 400
            res = Error("The specified annotation store was not found", status)
            return res, status

        try:
            annotation_create_request = AnnotationCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
            text_date_annotations = None
            text_person_name_annotations = None
            text_location_annotations = None
            text_id_annotations = None
            text_contact_annotations = None
            text_covid_symptom_annotations = None

            if annotation_create_request.text_date_annotations is not None:
                text_date_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation_create_request.text_date_annotations]

            if annotation_create_request.text_person_name_annotations is not None:  # noqa: E501
                text_person_name_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation_create_request.text_person_name_annotations]  # noqa: E501

            if annotation_create_request.text_location_annotations is not None:  # noqa: E501
                text_location_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation_create_request.text_location_annotations]  # noqa: E501

            if annotation_create_request.text_id_annotations is not None:  # noqa: E501
                text_id_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation_create_request.text_id_annotations]  # noqa: E501

            if annotation_create_request.text_contact_annotations is not None:  # noqa: E501
                text_contact_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation_create_request.text_contact_annotations]  # noqa: E501

            if annotation_create_request.text_covid_symptom_annotations is not None:  # noqa: E501
                text_covid_symptom_annotations = [
                    util.change_dict_naming_convention(
                        a.to_dict(), util.underscore_to_camel)
                    for a in annotation_create_request.text_covid_symptom_annotations]  # noqa: E501

            annotation_source = util.change_dict_naming_convention(
                annotation_create_request.annotation_source.to_dict(),
                util.underscore_to_camel)

            annotation_name = "%s/annotations/%s" % (store_name, annotation_id)

            db_annotation = DbAnnotation(
                name=annotation_name,
                annotationSource=annotation_source,
                annotationStoreName=store_name,
                textDateAnnotations=text_date_annotations,
                textPersonNameAnnotations=text_person_name_annotations,
                textLocationAnnotations=text_location_annotations,  # noqa: E501
                textIdAnnotations=text_id_annotations,
                textContactAnnotations=text_contact_annotations,
                textCovidSymptomAnnotations=text_covid_symptom_annotations
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

    :rtype: EmptyObject
    """
    res = None
    status = None
    try:
        annotation_name = "datasets/%s/annotationStores/%s/annotations/%s" % \
            (dataset_id, annotation_store_id, annotation_id)
        db_annotation = DbAnnotation.objects.get(name=annotation_name)
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
        annotation_name = "datasets/%s/annotationStores/%s/annotations/%s" % \
            (dataset_id, annotation_store_id, annotation_id)
        db_annotation = DbAnnotation.objects.get(name=annotation_name)
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
        db_objects = DbAnnotation.objects(annotationStoreName=store_name)
        db_annotations = db_objects.skip(offset).limit(limit)
        total_results = db_objects.count()
        annotations = [Annotation.from_dict(a.to_dict()) for a in db_annotations]  # noqa: E501
        next_ = ""
        if len(annotations) == limit:
            next_ = (
                "%s/datasets/%s/annotationStores/%s/annotations"
                "?limit=%s&offset=%s") % \
                (config.server_api_url, dataset_id, annotation_store_id, limit,  # noqa: E501
                    offset + limit)
        res = PageOfAnnotations(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            total_results=total_results,
            annotations=annotations)
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
