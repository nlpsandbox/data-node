# from enum import Enum
from mongoengine import StringField, IntField

from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501


# class AnnotationType(Enum):
#     TEXT_DATE = "text_date"
#     TEXT_PERSON_NAME = "text_person_name"
#     TEXT_PHYSICAL_ADDRESS = "text_physical_address"


class Annotation(BaseDocument):
    meta = {
        'allow_inheritance': True
    }
    annotationStore = StringField()
    # annotationSource = None
    annotationType = StringField()  # EnumField(AnnotationType)
    start = IntField()
    length = IntField()
    text = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()  # TODO try self.to_python()
        return doc
