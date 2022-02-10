from mongoengine import DynamicDocument, Document
from mongoengine.fields import StringField, IntField, ListField, DictField


class MovieModel(Document):
    genres = ListField()
    fullplot = StringField()
    awards = DictField()
    runtime = IntField()
    title = StringField()
    meta = {"collection": "movies", "strict": False}
