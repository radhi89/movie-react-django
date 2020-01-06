import rest_framework_filters as filters

from accounts.models import Movie


class MovieFilter(filters.FilterSet):
    movie = filters.BooleanFilter(field_name='movie', method='filter_movie')

    class Meta:
        model = Movie
        fields = []

    def filter_movie(self, qs, name, value):
        movie_list = Movie.objects.filter(
            title=self.title).values_list('review', flat=True)
        qs = qs.filter(id__in=movie_list)
        return qs