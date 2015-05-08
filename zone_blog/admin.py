from django.contrib import admin
from django import forms

from taggit.forms import TagWidget

import models


class CustomTagWidget(TagWidget):
    def render(self, name, value, attrs=None):
        widget = super(CustomTagWidget, self).render(name, value, attrs)
        return widget


class ContentForm(forms.ModelForm):
    class Meta:
        model = models.Content
        widgets = {
            'tags': CustomTagWidget(attrs={'data-role': 'tags'}),
        }
        exclude = []


class ContentAdmin(admin.ModelAdmin):

    form = ContentForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'published_on', 'is_published')

    def get_queryset(self, request):
        qs = super(ContentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(ContentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'author':
            if request.user.is_superuser:
                field.queryset = field.queryset
            else:
                field.queryset = field.queryset.filter(pk=request.user.pk)
        return field

    def get_form(self, request, obj=None, **kwargs):
        if obj is None and not request.user.is_superuser:
            form = super(ContentAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['author'].initial = request.user
            return form
        return super(ContentAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(models.Post, ContentAdmin)
admin.site.register(models.NewsItem, ContentAdmin)
admin.site.register(models.Project, ContentAdmin)
