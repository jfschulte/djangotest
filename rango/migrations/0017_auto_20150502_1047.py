# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0016_auto_20150502_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfavorites',
            old_name='username',
            new_name='redditUserName',
        ),
    ]
