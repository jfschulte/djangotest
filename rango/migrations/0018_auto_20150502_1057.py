# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0017_auto_20150502_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorites',
            name='favRedditor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userfavorites',
            name='redditorImage',
            field=models.CharField(max_length=50),
        ),
    ]
