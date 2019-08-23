# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dc_members', '0004_member_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(
                null=True,
                to=settings.AUTH_USER_MODEL,
                unique=True,
                on_delete=models.CASCADE,
            ),
            preserve_default=True,
        ),
    ]
