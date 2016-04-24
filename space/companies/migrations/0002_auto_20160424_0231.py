# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='altitude',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='grade',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='lon',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='monoxid',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='precipitation_mm',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='temperature',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='company',
            name='water_quality',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
    ]
