from mongoengine import FloatField, IntField, StringField, EmbeddedDocument


class TextDateAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    dateFormat = StringField(required=False)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
