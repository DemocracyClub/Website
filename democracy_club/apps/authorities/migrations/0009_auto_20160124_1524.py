# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0008_auto_20160124_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityServiceDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('LAid', models.IntegerField(blank=True, null=True)),
                ('LGIL', models.IntegerField(blank=True, null=True)),
                ('URL', models.URLField(blank=True)),
                ('last_updated', models.DateTimeField(blank=True)),
                ('LGSL', models.ForeignKey(to='authorities.AuthorityServiceCategory')),
            ],
        ),
        migrations.AlterField(
            model_name='authority',
            name='ons_id',
            field=models.CharField(max_length=100, blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='authorityservicedetails',
            name='SNAC',
            field=models.ForeignKey(to_field='ons_id', to='authorities.Authority'),
        ),
    ]
