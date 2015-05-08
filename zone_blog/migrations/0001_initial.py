# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('published_on', models.DateField(default=datetime.date.today, verbose_name='Published on')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('keywords', models.CharField(help_text=b'A comma-separated list of keywords', max_length=1000, verbose_name='Meta keywords')),
                ('views', models.IntegerField(default=0, verbose_name='Views', editable=False)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('published_on', models.DateField(default=datetime.date.today, verbose_name='Published on')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('keywords', models.CharField(help_text=b'A comma-separated list of keywords', max_length=1000, verbose_name='Meta keywords')),
                ('views', models.IntegerField(default=0, verbose_name='Views', editable=False)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('published_on', models.DateField(default=datetime.date.today, verbose_name='Published on')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('keywords', models.CharField(help_text=b'A comma-separated list of keywords', max_length=1000, verbose_name='Meta keywords')),
                ('views', models.IntegerField(default=0, verbose_name='Views', editable=False)),
                ('template', models.CharField(max_length=200, null=True, verbose_name='Template', blank=True)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_on'],
                'abstract': False,
            },
        ),
    ]
