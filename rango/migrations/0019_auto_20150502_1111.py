# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0018_auto_20150502_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavRedditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favRedditor', models.CharField(max_length=30)),
                ('redditorImage', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='userfavorites',
            name='redditorImage',
        ),
        migrations.AlterField(
            model_name='userfavorites',
            name='favRedditor',
            field=models.ForeignKey(to='rango.FavRedditor'),
        ),
    ]
