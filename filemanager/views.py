from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core import serializers
from django.http import JsonResponse

from account.models import CustomUser  # Import your custom user model

from .filters import DirectoryFilter, FileFilter
from .models import Directory, File


# Create your views here.
@login_required
def validate_token(user, token):
    return default_token_generator.check_token(user, token)


def file_api(request):
    token = request.META.get("HTTP_AUTHORIZATION", "").split(" ")[-1]

    try:
        user = CustomUser.objects.get(
            username="shady"
        )  # Replace 'john_doe' with the username of the user
    except CustomUser.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    file_filter = FileFilter(request.GET, queryset=File.objects.all())
    directory_filter = DirectoryFilter(request.GET, queryset=Directory.objects.all())

    files = file_filter.qs if user.is_superuser else file_filter.data
    directories = directory_filter.qs if user.is_super else directory_filter.data

    file_data = serializers.serialize("json", files)
    directory_data = serializers.serialize("json", directories)

    data = {"files": file_data, "directories": directory_data}

    return JsonResponse(data, safe=False)
