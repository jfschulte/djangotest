# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('redditor', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=50)),
            ],
        ),
    ]
