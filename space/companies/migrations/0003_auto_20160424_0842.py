# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20160424_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='employers_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='ocuped_area',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='used_energies',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
