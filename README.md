# MongORM

Studying pymongo ORM (mongo-engine) with Flask by implementing adapter and model layers  in a simple architecture.

## Dataset and Environment

**Mflix dataset** extracted from [this repository](https://github.com/neelabalan/mongodb-sample-dataset).

The following command imports the movies collection into the examples database of mongo (local):

```bash
mongoimport -d examples -c movies sample_mflix/movies.json
```

## Sending a request

```bash
curl --request POST --url <localhost>/get_movie_by_id --data '{"movie_id": "573a1390f29313caabcd50e5"}'
```
