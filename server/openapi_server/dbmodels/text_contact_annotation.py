from mongoengine import FloatField, IntField, StringField, EmbeddedDocument


class TextContactAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    contactType = StringField(required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
