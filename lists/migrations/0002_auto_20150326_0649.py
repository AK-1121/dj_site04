# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 6, 49, 18, 523258)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
