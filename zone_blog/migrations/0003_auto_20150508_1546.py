# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zone_blog', '0002_auto_20150506_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='author',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='tags',
        ),
        migrations.DeleteModel(
            name='NewsItem',
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'img/posts/', null=True, verbose_name='Picture', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'img/posts/', null=True, verbose_name='Picture', blank=True),
            preserve_default=True,
        ),
    ]
