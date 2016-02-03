# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everyelection', '0003_auto_20160130_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorityelection',
            name='election_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
