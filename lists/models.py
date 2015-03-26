from django.db import models
import datetime

class Item(models.Model):
    text = models.TextField(default='')
    date = models.DateTimeField(default=datetime.datetime.now())

