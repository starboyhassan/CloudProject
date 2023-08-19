from django.urls import path

from . import views

urlpatterns = [
    path("api/files/", views.file_api, name="file_api"),
]
