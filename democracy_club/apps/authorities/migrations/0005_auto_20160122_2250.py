# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0004_auto_20160122_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoritygeo',
            name='authority',
            field=models.OneToOneField(to='authorities.Authority', related_name='authority_geo', null=True),
        ),
    ]
