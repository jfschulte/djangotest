# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_userfavorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfavorites',
            name='username',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
