from mongoengine import Document


class BaseDocument(Document):
    meta = {
        'abstract': True
    }
