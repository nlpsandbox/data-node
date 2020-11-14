from mongoengine import StringField

from openapi_server.dbmodels.annotation import Annotation


class TextDateAnnotation(Annotation):
    dateFormat = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()  # TODO try self.to_python()
        return doc
