# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0012_mapitarea'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authority',
            options={'ordering': ('name',), 'verbose_name_plural': 'authorities'},
        ),
    ]
