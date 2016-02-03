# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0012_mapitarea'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityElection',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('election_date', models.DateField()),
                ('percent_posts', models.IntegerField()),
                ('authority', models.ForeignKey(to='authorities.Authority')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorityElectionPositions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(editable=False, blank=True, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(editable=False, blank=True, default=django.utils.timezone.now, verbose_name='modified')),
                ('area', models.ForeignKey(to='authorities.MapitArea')),
                ('authority_election', models.ForeignKey(to='everyelection.AuthorityElection')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
    ]
