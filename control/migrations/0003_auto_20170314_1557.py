# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20170313_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagedata',
            old_name='messageType',
            new_name='message',
        ),
    ]
