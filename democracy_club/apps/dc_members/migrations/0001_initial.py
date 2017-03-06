# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('constituency', models.CharField(max_length=255, blank=True)),
                ('postcode', models.CharField(max_length=20, blank=True)),
                ('token', models.CharField(
                    db_index=True, max_length=255, blank=True)),
                ('user', models.ForeignKey(
                    to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
