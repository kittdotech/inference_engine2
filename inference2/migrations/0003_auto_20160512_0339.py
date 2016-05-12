# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inference2', '0002_auto_20160502_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='define3',
            name='type',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
    ]
