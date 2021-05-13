from mongoengine import FloatField, IntField, StringField, EmbeddedDocument


class TextIdAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    idType = StringField(required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
