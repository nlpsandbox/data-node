from mongoengine import StringField

from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501


class FhirStore(BaseDocument):
    name = StringField(required=True, unique=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)

        return doc

    def get_dataset_name(self):
        return ""