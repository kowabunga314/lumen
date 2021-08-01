from datetime import datetime
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Series(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='', blank=True)
    thumbnail = models.ImageField(upload_to='images/', default='images/placeholder.jpeg')

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.name

    def photo_count(self):
        return len(self.photos.all())


class Photo(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='', blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    location = models.CharField(max_length=128, blank=True)
    pub_date = models.DateField('Date of Publication', default=datetime.now)
    series = ForeignKey(Series, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.name

