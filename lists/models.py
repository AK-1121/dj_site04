from django.db import models
import datetime

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    date = models.DateTimeField(default=datetime.datetime.now)

