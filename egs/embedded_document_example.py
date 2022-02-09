from mongoengine import connect
from mongoengine.document import EmbeddedDocument, DynamicDocument
from mongoengine.fields import EmbeddedDocumentField, IntField, StringField
from mongoengine.queryset.visitor import Q

connect("examples")


class DateModel(EmbeddedDocument):
    year = IntField()
    day = IntField()
    month = IntField()


class SongModel(DynamicDocument):
    name = StringField()
    date = EmbeddedDocumentField(DateModel)
    meta = {"collection": "dev"}


class SongRepository:
    def get_songs_by_year(self, id, year):
        # return SongModel.objects(date__year=year).first()
        return SongModel.objects(Q(id=id) & Q(date_year == year)).first()


if __name__ == "__main__":
    song1 = SongModel(
        name="Faith & Decision",
        date=DateModel(year=2016, day=10, month=8),
    )
    song2 = SongModel(
        name="Judicial Noir",
        date=DateModel(year=2017, day=10, month=8),
    )
    song1.save()
    song2.save()

    print(SongRepository().get_songs_by_year(song1.id, 2016).name)
