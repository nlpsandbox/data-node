from mongoengine import StringField

from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501


class Dataset(BaseDocument):
    name = StringField(required=True, unique=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
