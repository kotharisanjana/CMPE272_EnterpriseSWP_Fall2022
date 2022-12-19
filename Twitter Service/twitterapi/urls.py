from django.urls import path
from . import views

## Author: Sanjana Rajesh Kotari and Naga Bathula
## This file contains the views for the Twitter API application.

# URL configuration
urlpatterns = [
    path('create_tweet/', views.create_tweet),
    path('get_timeline_tweets/', views.get_timeline_tweets),
    path('delete_tweet/', views.delete_tweet)
]
