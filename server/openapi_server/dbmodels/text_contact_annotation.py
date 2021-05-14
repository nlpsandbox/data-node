from mongoengine import FloatField, IntField, StringField, EmbeddedDocument, EnumField  # noqa: E501
from enum import Enum


class ContactType(Enum):
    EMAIL = 'email'
    FAX = 'fax'
    PHONE = 'phone'
    URL = 'url'
    OTHER = 'other'


class TextContactAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    contactType = EnumField(ContactType, required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
