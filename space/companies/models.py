# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings

from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=255)
    address = models.TextField()

    lat = models.DecimalField(
        decimal_places=8,
        max_digits=10
    )
    lon = models.DecimalField(
        decimal_places=8,
        max_digits=11
    )
    altitude = models.DecimalField(
        decimal_places=8,
        max_digits=16
    )

    employers_number = models.IntegerField()

    ocuped_area = models.DecimalField(
        decimal_places=8,
        max_digits=11
    )

    used_energies = models.TextField()

    branch = models.TextField()

    image = models.ImageField(
        max_length=500,
        blank=True,
        null=True,
       #default=open(settings.BASE_DIR + "/companies/static/images/black.jpg")
    )

    grade = models.DecimalField(
        decimal_places=5,
        max_digits=10
    )

    def __unicode__(self):
        return str(self.name)


class InformationRecovered(models.Model):

    company = models.ForeignKey(Company)

    # Recived from the sensor
    humidity = models.DecimalField(
        decimal_places=8,
        max_digits=10
    )
    temperature = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    heat = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )
    light_resistance = models.DecimalField(
        decimal_places=4,
        max_digits=10
    )

    #randomized
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

    def __unicode__(self):
        return str(self.company)