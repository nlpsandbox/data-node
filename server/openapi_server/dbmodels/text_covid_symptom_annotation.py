from mongoengine import FloatField, IntField, StringField, EmbeddedDocument, EnumField  # noqa: E501
from enum import Enum


class Condition(Enum):
    FEVER = 'fever'
    CHILL = 'chill'
    COUGH = 'cough'
    FATIGUE = 'fatigue'
    NASAL_OBSTRUCTION = 'nasal_obstruction'
    LOSS_OF_APPETITE = 'loss_of_appetite'
    DIARRHEA = 'diarrhea'
    ABDOMINAL_PAIN = 'abdominal_pain'
    NAUSEA = 'nausea'
    VOMITING = 'vomiting'
    SORE_THROAT = 'sore_throat'
    HEADACHE = 'headache'
    MYALGIA = 'myalgia'
    LOSS_OF_TASTE = 'loss_of_taste'
    LOSS_OF_SMELL = 'loss_of_smell'
    DYSPNEA = 'dyspnea'
    CHEST_PAIN = 'chest_pain'
    DELIRIUM = 'delirium'
    HYPERSOMNIA = 'hypersomnia'
    CYANOSIS = 'cyanosis'


class Certainty(Enum):
    POSITIVE = 'positive'
    NEGATED = 'negated'
    POSSIBLE = 'possible'


class TextCovidSymptomAnnotation(EmbeddedDocument):
    start = IntField(required=True)
    length = IntField(required=True)
    text = StringField(required=True)
    confidence = FloatField(required=True)
    condition = EnumField(Condition, required=True)
    certainty = EnumField(Certainty, required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
