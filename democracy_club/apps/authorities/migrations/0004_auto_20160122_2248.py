# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0003_auto_20160122_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authority',
            name='authority_geo',
        ),
        migrations.AddField(
            model_name='authoritygeo',
            name='authority',
            field=models.OneToOneField(null=True, to='authorities.Authority'),
        ),
    ]
