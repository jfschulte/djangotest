# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0013_userfavorites_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedditUserName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='userfavorites',
            old_name='redditor',
            new_name='favRedditor',
        ),
        migrations.RenameField(
            model_name='userfavorites',
            old_name='image',
            new_name='redditorImage',
        ),
        migrations.AlterField(
            model_name='userfavorites',
            name='username',
            field=models.ForeignKey(to='rango.RedditUserName'),
        ),
    ]
