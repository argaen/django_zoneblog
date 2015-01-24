from django.contrib import admin
from django.db import models as md

import models

class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, ContentAdmin)
admin.site.register(models.NewsItem, ContentAdmin)
admin.site.register(models.Project, ContentAdmin)
