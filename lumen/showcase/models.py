from datetime import datetime
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Series(models.Model):
    name = models.CharField(max_length=128)


class Photo(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=256)
    location = models.CharField(max_length=128)
    pub_date = models.DateField('Date of Publication', default=datetime.now)
    series = ForeignKey(Series, on_delete=models.CASCADE)

