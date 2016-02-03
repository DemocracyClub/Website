# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0011_auto_20160124_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapitArea',
            fields=[
                ('gss', models.CharField(primary_key=True, serialize=False, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('area_type', models.CharField(blank=True, max_length=100)),
                ('unit_id', models.CharField(blank=True, max_length=100)),
                ('type_name', models.CharField(blank=True, max_length=255)),
                ('country_name', models.CharField(blank=True, max_length=100)),
                ('parent_authority', models.ForeignKey(null=True, to='authorities.Authority')),
            ],
        ),
    ]
