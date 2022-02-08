from mongoengine import DynamicDocument
from mongoengine.fields import StringField, IntField, ListField, DictField


class MovieModel(DynamicDocument):
    genres = ListField()
    fullplot = StringField()
    awards = DictField()
    runtime = IntField()
    title = StringField()
    meta = {"collection": "movies"}
