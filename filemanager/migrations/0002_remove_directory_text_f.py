# Generated by Django 4.2.4 on 2023-08-10 11:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("filemanager", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="directory",
            name="text_f",
        ),
    ]
