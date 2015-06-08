# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zone_blog', '0006_auto_20150529_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code_url',
            field=models.URLField(null=True, verbose_name='Code url', blank=True),
        ),
    ]
