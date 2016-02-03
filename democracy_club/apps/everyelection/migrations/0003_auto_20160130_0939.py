# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('everyelection', '0002_auto_20160129_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorityelection',
            old_name='id',
            new_name='election_id'
        ),
    ]
