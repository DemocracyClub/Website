# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everyelection', '0005_auto_20160203_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorityelectionposition',
            name='seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
