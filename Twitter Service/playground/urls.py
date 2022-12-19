from django.urls import path
from . import views

## Author: Sanjana Rajesh Kotari and Naga Bathula
## This file contains the views for the Twitter API application.

# URL configuration
urlpatterns = [
    path('home/',views.load_home_page, name='home'),
]
