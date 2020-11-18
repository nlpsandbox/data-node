from mongoengine import IntField, StringField, EmbeddedDocument


class TextPersonNameAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
