# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0006_auto_20160122_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityServices',
            fields=[
                ('LGSL', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=800, blank=True)),
                ('providing_tier', models.CharField(max_length=100, blank=True)),
            ],
        ),
    ]
