from mongoengine import FloatField, IntField, StringField, EmbeddedDocument, EnumField  # noqa: E501
from enum import Enum


class IdType(Enum):
    ACCOUNT = 'account'
    BIO_ID = 'bio_id'
    DEVICE = 'device'
    HEALTH_PLAN = 'health_plan'
    ID_NUM = 'id_num'
    LICENSE = 'license'
    MEDICAL_RECORD = 'medical_record'
    SSN = 'ssn'
    VEHICLE = 'vehicle'


class TextIdAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    idType = EnumField(IdType, required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
