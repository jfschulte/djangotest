# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0019_auto_20150502_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavorites',
            name='favRedditor',
        ),
        migrations.AddField(
            model_name='favredditor',
            name='userFavorites',
            field=models.ForeignKey(default=1, to='rango.UserFavorites'),
            preserve_default=False,
        ),
    ]
