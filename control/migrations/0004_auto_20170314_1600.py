# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20170314_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagedata',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]
