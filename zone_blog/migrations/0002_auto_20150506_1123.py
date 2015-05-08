# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zone_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='photo',
            field=models.ImageField(upload_to=b'img/posts/', null=True, verbose_name='Picture', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=b'img/posts/', null=True, verbose_name='Picture', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(upload_to=b'img/posts/', null=True, verbose_name='Picture', blank=True),
        ),
    ]
