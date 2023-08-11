from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Directory, File

# Create your views here.


@login_required
def user_files(request):
    user = request.user
    files = File.objects.filter(user=user)
    directories = Directory.objects.filter(user=user)
    response_data = {
        "files": [file.name for file in files],
        "directories": [directory.name for directory in directories],
    }
    return JsonResponse(response_data)


@staff_member_required
def admin_files(request):
    files = File.objects.all()
    directories = Directory.objects.all()
    response_data = {
        "files": [file.name for file in files],
        "directories": [directory.name for directory in directories],
    }
    return JsonResponse(response_data)
