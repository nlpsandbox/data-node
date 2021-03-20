from mongoengine import StringField

from openapi_server.dbmodels.base_document import BaseDocument


class Note(BaseDocument):
    identifier = StringField()
    resourceName = StringField(required=True, unique=True)
    fhirStoreName = StringField()
    text = StringField()
    type = StringField()
    patientId = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)

        # remove internal properties
        del doc['resourceName']
        del doc['fhirStoreName']

        return doc
