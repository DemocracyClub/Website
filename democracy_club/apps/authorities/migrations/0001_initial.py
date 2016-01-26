# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('authority_id', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('authority_type', models.CharField(blank=True, max_length=10)),
                ('mapit_id', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('postcode', models.CharField(null=True, blank=True, max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(geography=True, blank=True, null=True, srid=4326)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
