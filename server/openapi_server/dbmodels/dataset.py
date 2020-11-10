# import json
from mongoengine import DictField, StringField
from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501


class Dataset(BaseDocument):
    # uuid = StringField(required=True)
    # id = DictField(primary_key=True)
    name = StringField(required=True)

    # def to_json(self):
    #     return {
    #         "_id": str(self.pk),
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "username": self.username,
    #         "password": self.password
    #     }

    # def to_json(self):
    #     dataset = {
    #         "id": str(self.id),
    #         }
    #     if self.name is not None:
    #         dataset['name'] = self.name

    #     return json.dumps(dataset)
