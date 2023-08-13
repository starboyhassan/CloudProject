import django_filters

from .models import Directory, File


class FileFilter(django_filters.filterset):
    class Meta:
        model = File
        fields = ["user"]


class DirectoryFilter(django_filters.filterset):
    class Meta:
        model = Directory
        fields = ["user"]
