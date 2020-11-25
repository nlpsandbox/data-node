from mongoengine import EmbeddedDocument, EmbeddedDocumentField

from openapi_server.dbmodels.resource_source import ResourceSource


class AnnotationSource(EmbeddedDocument):
    resourceSource = EmbeddedDocumentField(ResourceSource)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
