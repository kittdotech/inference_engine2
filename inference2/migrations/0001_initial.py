# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Define3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra', models.CharField(max_length=5, null=True, blank=True)),
                ('type', models.CharField(max_length=3, null=True, blank=True)),
                ('word', models.CharField(max_length=66, null=True, blank=True)),
                ('rel', models.CharField(max_length=4, null=True, blank=True)),
                ('definition', models.CharField(max_length=470, null=True, blank=True)),
            ],
            options={
                'db_table': 'define3',
                'managed': False,
            },
        ),
    ]
