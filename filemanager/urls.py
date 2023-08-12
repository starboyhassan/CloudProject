from django.urls import path

from .views import file_api

urlpatterns = [
    path("api/files/", file_api, name="file_api"),
]
