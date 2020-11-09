from mongoengine import Document, StringField


class Dataset(Document):
    name = StringField(required=True)
