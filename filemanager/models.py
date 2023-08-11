from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from account.models import CustomUser

#################################


class Directory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
