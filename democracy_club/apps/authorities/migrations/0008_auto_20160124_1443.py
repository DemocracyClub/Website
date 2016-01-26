# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0007_authorityservices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthorityServices',
            new_name='AuthorityServiceCategory',
        ),
    ]
