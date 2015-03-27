# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20150327_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 7, 23, 53, 777105)),
        ),
    ]
