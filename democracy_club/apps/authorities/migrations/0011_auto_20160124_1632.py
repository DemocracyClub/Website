# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0010_auto_20160124_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorityservicedetails',
            name='URL',
            field=models.URLField(blank=True, max_length=800),
        ),
    ]
