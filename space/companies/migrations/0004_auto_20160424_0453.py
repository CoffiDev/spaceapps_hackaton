# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20160424_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationRecovered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('humidity', models.DecimalField(max_digits=10, decimal_places=4)),
                ('temperature', models.DecimalField(max_digits=10, decimal_places=4)),
                ('heat', models.DecimalField(max_digits=10, decimal_places=4)),
                ('light_resistance', models.DecimalField(max_digits=10, decimal_places=4)),
                ('precipitation_mm', models.DecimalField(max_digits=10, decimal_places=4)),
                ('monoxid', models.DecimalField(max_digits=10, decimal_places=4)),
                ('water_quality', models.DecimalField(max_digits=10, decimal_places=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='monoxid',
        ),
        migrations.RemoveField(
            model_name='company',
            name='precipitation_mm',
        ),
        migrations.RemoveField(
            model_name='company',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='company',
            name='water_quality',
        ),
        migrations.AddField(
            model_name='informationrecovered',
            name='company',
            field=models.ForeignKey(to='companies.Company'),
        ),
    ]
