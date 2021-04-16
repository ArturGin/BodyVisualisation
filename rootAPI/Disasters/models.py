from django.db import models


class Disasters(models.Model):
    year = models.IntegerField(blank=True, null=True)
    disaster_type = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    people_died = models.IntegerField(blank=True, null=True)
