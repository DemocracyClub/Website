# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hermes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hermes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.CharField(
                default=b"", max_length=500, db_index=True, blank=True
            ),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name="post",
            name="hero",
            field=models.ImageField(
                upload_to=hermes.models.post_hero_upload_to,
                null=True,
                verbose_name="hero",
                blank=True,
            ),
            preserve_default=True,
        ),
    ]
