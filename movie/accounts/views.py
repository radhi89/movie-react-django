# Create your views here.
from collections import OrderedDict

from django.db.models import Q
from rest_framework import generics, pagination
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from accounts.filters import MovieFilter
from accounts.models import Movie, Enquiry, Review

from accounts.serializers import MovieSerializer, EnquiryModelSerializer, MovieReviewSerializer, ReviewSerializer


class CustomCoursePaginator(pagination.CursorPagination):
    page_size = 8
    page_size_query_param = 'page_size'

    # '-creation' is default

    def paginate_queryset(self, queryset, request, view=None):
        self.count = self.get_count(queryset)
        return super().paginate_queryset(queryset, request, view)

    def get_count(self, queryset):
        """
        Determine an object count, supporting either querysets or regular lists.
        """
        try:
            return queryset.count()
        except (AttributeError, TypeError):
            return len(queryset)

    def get_paginated_response(self, data):

        return Response(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class CustomPageNumber(PageNumberPagination):


    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('count', self.page.paginator.count),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data)
         ]))

class HomeView(ListAPIView):
    """
    A viewset for homepage.
    """
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumber
    page_size = 8
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class EnquiryCreateViewSet(CreateAPIView):
    """ Enquiry Create ViewSet """
    permission_classes = (AllowAny,)
    queryset = Enquiry.objects.all()
    serializer_class = EnquiryModelSerializer


class MovieReviewViewSet(ListAPIView):
    """
    A view for movie reviews.
    """
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumber
    queryset = Movie.objects.all().order_by('-release_date')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['genre', ]
    search_fields = ['genre', 'title', 'stars', 'director']
    serializer_class = MovieReviewSerializer

    def get_queryset(self):
        search = self.request.GET.get('search', "")
        results = super().get_queryset()

        if search:
            results = results.filter(Q(title__icontains=search) |
                                     Q(description__icontains=search))
        return results


class MovieReviewDetailViewSet(generics.ListCreateAPIView):
    """
    A view for movie reviews.
    """
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumber
    page_size = 8
    http_method_names = ['get', 'post', 'put']
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MovieDetailCustom(RetrieveUpdateDestroyAPIView):

    lookup_url_kwarg = "id"
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer





