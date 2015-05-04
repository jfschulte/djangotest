# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0014_auto_20150502_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditusername',
            name='username',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
