# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20160424_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='branch',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
