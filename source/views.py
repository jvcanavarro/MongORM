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


@app.route("/get_movies_by_genre", methods=["POST"])
def get_movies_by_genre():
    movie_genre = request.get_json(force=True)["movie_genre"]
    movies = MovieRepository().get_movies_by_genre(movie_genre)
    return f"Movie: {movies[0].title}"


@app.route("/get_movies_by_awards", methods=["POST"])
def get_movies_by_awards():
    n_awards = request.get_json(force=True)["awards"]
    movies = MovieRepository().get_movies_by_awards(n_awards)
    return f"Movie: {movies[0].title}"


if __name__ == "__main__":
    app.run(debug=True)
