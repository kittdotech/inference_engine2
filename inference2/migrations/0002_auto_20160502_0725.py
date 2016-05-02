# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inference2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('col1', models.CharField(max_length=5, null=True, blank=True)),
                ('col2', models.CharField(max_length=500, null=True, blank=True)),
                ('col3', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
                'db_table': 'input',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='define3',
            options={'managed': True},
        ),
    ]
