from django.db.models import Value
from rest_framework import serializers
from .models import Movie, Enquiry, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ()


class EnquiryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enquiry
        exclude = ('phone',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ()


class MovieReviewSerializer(serializers.ModelSerializer):

    review = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'review', 'banner_image', 'genre', 'release_date',
                  'director', 'duration', 'stars', ]

    def get_review(self, obj):
        movie = Review.objects.filter(movie=obj).first()
        if movie:
            return movie.review
        else:
            return 0.0


