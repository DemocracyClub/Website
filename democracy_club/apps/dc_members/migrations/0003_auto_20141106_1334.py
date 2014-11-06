# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dc_members', '0002_member_mapit_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mapit_json',
            field=jsonfield.fields.JSONField(null=True),
            preserve_default=True,
        ),
    ]
