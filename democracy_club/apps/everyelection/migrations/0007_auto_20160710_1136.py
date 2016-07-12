# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everyelection', '0006_authorityelectionposition_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorityelectionposition',
            name='seats',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
