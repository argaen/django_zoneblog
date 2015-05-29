# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zone_blog', '0005_auto_20150529_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='last_updated',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='last_updated',
            new_name='last_update',
        ),
    ]
