from mongoengine import FloatField, IntField, StringField, EmbeddedDocument, EnumField  # noqa: E501
from enum import Enum


class AddressType(Enum):
    CITY = 'city'
    COUNTRY = 'country'
    DEPARTMENT = 'department'
    HOSPITAL = 'hospital'
    ORGANIZATION = 'organization'
    OTHER = 'other'
    ROOM = 'room'
    STATE = 'state'
    STREET = 'street'
    ZIP = 'zip'


class TextPhysicalAddressAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    addressType = EnumField(AddressType, required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
