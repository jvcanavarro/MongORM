from flask import Flask, request
from mongoengine import connect

from repository import MovieRepository

app = Flask(__name__)
connect("examples")


@app.route("/")
def index():
    return "Mongo ORM APP"


@app.route("/get_movie_by_id", methods=["POST"])
def get_movie_by_id():
    movie_id = request.get_json(force=True)["movie_id"]
    movie = MovieRepository().get_movie_by_id(movie_id)
    return f"Movie: {movie.title}"


if __name__ == "__main__":
    app.run(debug=True)
