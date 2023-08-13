from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from .filters import DirectoryFilter, FileFilter
from .models import Directory, File

# Create your views here.


@login_required
def file_api(request):
    if request.user.is_superuser:
        files = File.objects.all()
        directories = Directory.objects.all()
    else:
        files = FileFilter(request.GET, queryset=File.objects.all())
        directories = DirectoryFilter(request.GET, queryset=Directory.objects.all())

    file_data = serializers.serialize("json", files)
    directory_data = serializers.serialize("json", directories)

    data = {"files": file_data, "directories": directory_data}

    return JsonResponse(data, safe=False)
