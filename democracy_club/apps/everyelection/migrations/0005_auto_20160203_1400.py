# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('everyelection', '0004_auto_20160130_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityElectionSkipped',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', blank=True, editable=False, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', blank=True, editable=False, default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AlterField(
            model_name='authorityelection',
            name='election_date',
            field=models.DateField(default='2016-05-05'),
        ),
        migrations.AddField(
            model_name='authorityelectionskipped',
            name='authority_election',
            field=models.ForeignKey(to='everyelection.AuthorityElection'),
        ),
        migrations.AddField(
            model_name='authorityelectionskipped',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
