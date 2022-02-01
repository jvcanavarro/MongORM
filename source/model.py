from mongoengine import DynamicDocument
from mongoengine.fields import StringField, IntField, ListField


class MovieModel(DynamicDocument):
    fullplot = StringField()
    genres = ListField()
    runtime = IntField()
    title = StringField()
    meta = {"collection": "movies"}
