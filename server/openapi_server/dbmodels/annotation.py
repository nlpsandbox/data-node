# from enum import Enum
from mongoengine import StringField, EmbeddedDocumentField, \
    EmbeddedDocumentListField

from openapi_server.dbmodels.annotation_source import AnnotationSource  # noqa: E501
from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501
from openapi_server.dbmodels.text_date_annotation import TextDateAnnotation  # noqa: E501
from openapi_server.dbmodels.text_person_name_annotation import TextPersonNameAnnotation  # noqa: E501
from openapi_server.dbmodels.text_physical_address_annotation import TextPhysicalAddressAnnotation  # noqa: E501
from openapi_server.dbmodels.text_id_annotation import TextIdAnnotation  # noqa: E501
from openapi_server.dbmodels.text_contact_annotation import TextContactAnnotation  # noqa: E501
from openapi_server.dbmodels.text_covid_symptom_annotation import TextCovidSymptomAnnotation  # noqa: E501


class Annotation(BaseDocument):
    name = StringField(required=True, unique=True)
    annotationStoreName = StringField(required=True)
    annotationSource = EmbeddedDocumentField(AnnotationSource, required=True)
    textDateAnnotations = EmbeddedDocumentListField(TextDateAnnotation)
    textPersonNameAnnotations = EmbeddedDocumentListField(TextPersonNameAnnotation)  # noqa: E501
    textPhysicalAddressAnnotations = EmbeddedDocumentListField(TextPhysicalAddressAnnotation)  # noqa: E501
    textIdAnnotations = EmbeddedDocumentListField(TextIdAnnotation)  # noqa: E501
    textContactAnnotations = EmbeddedDocumentListField(TextContactAnnotation)  # noqa: E501
    textCovidSymptomAnnotations = EmbeddedDocumentListField(TextCovidSymptomAnnotation)  # noqa: E501

    def to_dict(self):
        doc = self.to_mongo().to_dict()  # TODO try self.to_python()
        # doc["id"] = str(self.pk)
        return doc
