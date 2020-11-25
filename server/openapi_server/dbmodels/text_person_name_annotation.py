from mongoengine import FloatField, IntField, StringField, EmbeddedDocument


class TextPersonNameAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField()
    confidence = FloatField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
