from django.urls import path

from . import views

urlpatterns = [
    path("api/user/files/", views.user_files, name="user_files"),
    path("api/admin/files/", views.admin_files, name="admin_files"),
]
