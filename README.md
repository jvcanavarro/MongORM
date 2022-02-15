# MongORM

Studying pymongo ORM (mongo-engine) with Flask by implementing adapter and model layers  in a simple architecture.

## Dataset and Environment

**Mflix dataset** extracted from [this repository](https://github.com/neelabalan/mongodb-sample-dataset).

The following command imports the movies collection into the examples database of mongo (local):

```bash
mongoimport -d examples -c movies sample_mflix/movies.json
```

In order to access, query the imported dataset and make it available to mongoengine, simply run `mongosh` on the terminal

```sql
➜  ~ mongosh
Current Mongosh Log ID: xxxxxxxxxxxxxxxxxxxxxx
Connecting to:  mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9
Using MongoDB:  4.2.8
Using Mongosh:  1.1.9

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

test> show dbs
admin       41 kB
config     111 kB
examples  21.8 MB
local     73.7 kB
test> use examples
switched to db examples
examples> show tables
movies
examples> db.movies.findOne()["title"]
The Great Train Robbery
```

## Endpoints

Up to now, three endpoints have been implemented: `get_movie_by_id`, `get_movies_by_genre` and `get_movies_by_awards`.

### Examples

```bash
$ - curl --request POST --url <localhost>/get_movie_by_id --data '{"movie_id": "573a1390f29313caabcd50e5"}'
Movie: Gertie the Dinosaur

$ - curl --request POST --url http://127.0.0.1:5000/get_movies_by_genre --data '{"movie_genre": "Western"}'
Movie: The Great Train Robbery

$ - curl --request POST --url http://127.0.0.1:5000/get_movies_by_awards --data '{"awards": "3"}'
Movie: The Big Parade
```

## Extra: Querying a `EmbeddedDocument`
The `egs/` folder contains examples of queries to filter a model by id and EmbeddedDocument field value at the same time. It also contain a example of adding a new `EmbeddedDocument` model to a `EmbeddedDocumentListField`.

## TODO

- [ ] Add Swagger support.
