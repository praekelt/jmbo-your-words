from django.contrib import admin
from jmboyourwords.models import YourStoryCompetition, YourStoryEntry
from ckeditor.widgets import AdminCKEditor
from django.db import models


class YourStoryCompetitionAdmin(admin.ModelAdmin):
    list_filter = ('created', 'publish_on', 'retract_on')
    list_display = ('title', 'published', 'created', 'publish_on', 'retract_on')
    exclude = [
        'published',
    ]
    ordering = ('-published', '-publish_on', '-updated', 'created',)
    save_on_top = True

    formfield_overrides = {
        models.TextField: {'widget': AdminCKEditor},
    }
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'publish_on', 'retract_on'),
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
        (None, {
            'fields': ('image', 'content'),
        }),
        (None, {
            'fields': ('categories', 'tags', 'sites'),
        })
    )

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()


class YourStoryEntryAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
    list_filter = ('created', 'your_story_competition')
    list_display = ('name', 'email', 'user', 'created', 'text',)
    readonly_fields = ('created', 'user')

admin.site.register(YourStoryEntry, YourStoryEntryAdmin)
admin.site.register(YourStoryCompetition, YourStoryCompetitionAdmin)
