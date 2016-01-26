# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0005_auto_20160122_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='ons_id',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='mapit_id',
            field=models.CharField(max_length=100, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='authoritygeo',
            name='authority',
            field=models.OneToOneField(to='authorities.Authority', null=True),
        ),
    ]
