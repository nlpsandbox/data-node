from mongoengine import StringField

from openapi_server.dbmodels.base_document import BaseDocument


class Patient(BaseDocument):
    identifier = StringField()
    gender = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)

        return doc
