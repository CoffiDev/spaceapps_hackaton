# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('lat', models.DecimalField(max_digits=4, decimal_places=4)),
                ('lon', models.DecimalField(max_digits=4, decimal_places=4)),
                ('temperature', models.DecimalField(max_digits=4, decimal_places=4)),
                ('altitude', models.DecimalField(max_digits=4, decimal_places=4)),
                ('precipitation_mm', models.DecimalField(max_digits=4, decimal_places=4)),
                ('monoxid', models.DecimalField(max_digits=4, decimal_places=4)),
                ('water_quality', models.DecimalField(max_digits=4, decimal_places=4)),
                ('grade', models.DecimalField(max_digits=4, decimal_places=4)),
            ],
        ),
    ]
