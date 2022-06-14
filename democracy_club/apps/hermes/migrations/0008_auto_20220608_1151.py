# Generated by Django 3.2.13 on 2022-06-08 10:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hermes", "0007_auto_20210920_0909"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]