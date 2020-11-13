from mongoengine import StringField

from openapi_server.dbmodels.base_document import BaseDocument


class Patient(BaseDocument):
    fhir_store_name = StringField()
    text = StringField()
    noteType = StringField()
    patientId = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)
        # remove internal properties
        del doc['fhir_store_name']
        return doc
