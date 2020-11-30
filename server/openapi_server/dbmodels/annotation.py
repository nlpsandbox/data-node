# from enum import Enum
from mongoengine import StringField, EmbeddedDocumentField, \
    EmbeddedDocumentListField

from openapi_server.dbmodels.annotation_source import AnnotationSource  # noqa: E501
from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501
from openapi_server.dbmodels.text_date_annotation import TextDateAnnotation  # noqa: E501
from openapi_server.dbmodels.text_person_name_annotation import TextPersonNameAnnotation  # noqa: E501
from openapi_server.dbmodels.text_physical_address_annotation import TextPhysicalAddressAnnotation  # noqa: E501


class Annotation(BaseDocument):
    annotationStoreName = StringField(required=True)
    annotationSource = EmbeddedDocumentField(AnnotationSource, required=True)
    textDateAnnotations = EmbeddedDocumentListField(TextDateAnnotation)
    textPersonNameAnnotations = EmbeddedDocumentListField(TextPersonNameAnnotation)  # noqa: E501
    textPhysicalAddressAnnotations = EmbeddedDocumentListField(TextPhysicalAddressAnnotation)  # noqa: E501

    def to_dict(self):
        doc = self.to_mongo().to_dict()  # TODO try self.to_python()
        doc["id"] = str(self.pk)
        doc["name"] = "%s/annotations/%s" % (doc["annotationStoreName"], doc["id"])  # noqa: E501
        return doc
