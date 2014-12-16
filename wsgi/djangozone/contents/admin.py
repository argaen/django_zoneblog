from django.contrib import admin
from django.db import models as md

from markdownx.widgets import MarkdownxInput

import models

class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        md.TextField: {'widget': MarkdownxInput(attrs={'cols': 150}, )},
    }
    class Media:
        js = (
            'https://code.jquery.com/jquery-2.1.1.min.js',
        )
        css = {
            'all': ('/static/css/markdownx.css',)
            }

admin.site.register(models.Post, ContentAdmin)
admin.site.register(models.NewsItem, ContentAdmin)
admin.site.register(models.Project, ContentAdmin)
