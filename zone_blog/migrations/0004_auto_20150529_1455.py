# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zone_blog', '0003_auto_20150508_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='template',
        ),
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(default='http://django.zone', verbose_name='Project url'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(help_text=b'A comma-separated list of keywords. Used for Google indexing.', max_length=1000, null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='keywords',
            field=models.CharField(help_text=b'A comma-separated list of keywords. Used for Google indexing.', max_length=1000, null=True, verbose_name='Meta keywords', blank=True),
        ),
    ]
