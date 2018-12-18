from django.urls import path
from . import views
# Users/index/
urlpatterns = [
    path("home/", views.home),
    path("index/",views.index),
    path("friends/", views.friends),
]