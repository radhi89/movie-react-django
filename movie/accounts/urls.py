
from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.HomeView.as_view()),
    path('api/contact/', views.EnquiryCreateViewSet.as_view()),
    path('api/movies/', views.MovieReviewViewSet.as_view()),
    path('api/review/', views.MovieReviewDetailViewSet.as_view()),
    path('api/movies/<int:id>/', views.MovieDetailCustom.as_view()),

]
