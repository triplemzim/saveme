# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedata',
            name='contactno',
            field=models.CharField(max_length=15, default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='contactno',
            field=models.CharField(max_length=15),
        ),
    ]
