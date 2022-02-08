from model import MovieModel


class MovieRepository:
    def __init__(self):
        self.model = MovieModel()

    def get_movie_by_id(self, id):
        return MovieModel.objects(id=id).first()

    def get_movies_by_genre(self, genre):
        return MovieModel.objects(genres=genre)

    def get_movies_by_awards(self, n_awards):
        return MovieModel.objects(awards__wins=int(n_awards))