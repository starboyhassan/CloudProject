from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Directory, File

# Create your views here.


@login_required
def file_api(request):
    if request.user.is_superuser:
        files = File.objects.all()
        directories = Directory.objects.all()
    else:
        files = File.objects.filter(user=request.user)
        directories = Directory.objects.filter(user=request.user)

    file_data = [
        {"id": file.id, "name": file.name, "user": file.user.username} for file in files
    ]
    directory_data = [
        {"id": directory.id, "name": directory.name, "user": directory.user.username}
        for directory in directories
    ]

    data = {"files": file_data, "directories": directory_data}

    return JsonResponse(data)
