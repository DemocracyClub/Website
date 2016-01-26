# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0009_auto_20160124_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='ons_id',
            field=models.CharField(unique=True, max_length=100, null=True),
        ),
    ]
