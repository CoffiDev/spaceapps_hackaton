# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20160424_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='lat',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
    ]
