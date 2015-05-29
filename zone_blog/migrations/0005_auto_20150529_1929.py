# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zone_blog', '0004_auto_20150529_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_updated',
            field=models.DateField(null=True, verbose_name='Last update', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='last_updated',
            field=models.DateField(null=True, verbose_name='Last update', blank=True),
        ),
    ]
