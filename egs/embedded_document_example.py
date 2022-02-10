from mongoengine import connect
from mongoengine.document import EmbeddedDocument, DynamicDocument, Document
from mongoengine.fields import EmbeddedDocumentListField, IntField, StringField
from mongoengine.base.datastructures import EmbeddedDocumentList
from bson.objectid import ObjectId

from pprint import pprint

connect("examples")


class DateModel(EmbeddedDocument):
    year = IntField()
    day = IntField()
    month = IntField()


class SongModel(Document):
    name = StringField()
    date = EmbeddedDocumentListField(DateModel)
    meta = {"collection": "dev", "strict": False}


class SongRepository:
    def update_song_year(
        self, id: ObjectId, current_year: int, new_year: int
    ) -> SongModel:
        """Update all songs  with id=id and date.year=current_year with new_year"""
        model = SongModel.objects(id=id, date__year=current_year).modify(
            # __raw__={"$set": {"date.$.year": 7}}
            set__date__S__year=new_year,
            upsert=True,
            new=True,
        )
        print(f"\nModel Id: {model.id}\n")
        return model

    def read_song_date_by_id(self, id: str) -> EmbeddedDocumentList:
        """return songs.date by id"""
        return SongModel.objects.get(id=id).date


def print_dates(dates):
    pprint([date.to_json() for date in dates])


if __name__ == "__main__":
    song1 = SongModel(
        name="Faith & Decision",
        date=[
            DateModel(year=2016, day=10, month=8),
            DateModel(year=2014, day=12, month=10),
        ],
    ).save()
    song2 = SongModel(
        name="Judicial Noir",
        date=[
            DateModel(year=2010, day=5, month=4),
            DateModel(year=2018, day=10, month=8),
        ],
    ).save()

    dates = SongRepository().read_song_date_by_id(song1.id)

    print("Song:", song1.name)
    print_dates(song1.date)

    print(f"\nSong Id: {song2.id}\n")
    print("--Song dates before update--")
    print_dates(song2.date)

    model = SongRepository().update_song_year(song2.id, 2018, 2021)

    print("--Song dates after update--")
    print_dates(model.date)
