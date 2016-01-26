# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0002_auto_20160122_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='authority_geo',
            field=models.OneToOneField(null=True, to='authorities.AuthorityGeo'),
        ),
    ]
