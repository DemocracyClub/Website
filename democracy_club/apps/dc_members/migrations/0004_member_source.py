# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dc_members', '0003_auto_20141106_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='source',
            field=models.CharField(default='', max_length=800, blank=True),
            preserve_default=False,
        ),
    ]
