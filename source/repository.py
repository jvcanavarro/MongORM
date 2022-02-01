from model import MovieModel


class MovieRepository:
    def __init__(self):
        self.model = MovieModel()

    def get_movie_by_id(self, id):
        return MovieModel.objects(id=id).first()
