# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django_extensions.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityGeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(editable=False, verbose_name='created', blank=True, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(editable=False, verbose_name='modified', blank=True, default=django.utils.timezone.now)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, geography=True, null=True, blank=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'ordering': ('-modified', '-created'),
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='authority',
            options={'verbose_name_plural': 'authorities'},
        ),
        migrations.RemoveField(
            model_name='authority',
            name='area',
        ),
        migrations.RemoveField(
            model_name='authority',
            name='location',
        ),
        migrations.AddField(
            model_name='authority',
            name='authority_geo',
            field=models.ForeignKey(to='authorities.AuthorityGeo', null=True),
        ),
    ]
