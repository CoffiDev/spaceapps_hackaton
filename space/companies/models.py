# coding: utf-8

from __future__ import unicode_literals

from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=255)
    address = models.TextField()

    lat = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    lon = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )

    temperature = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    altitude = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    precipitation_mm = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    monoxid = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    water_quality = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )

    grade = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
