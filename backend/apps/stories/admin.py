from django.contrib import admin

from apps.stories.models import Episode, Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "project", "order", "created_at")
    list_filter = ("project",)
    search_fields = ("code", "title")
    ordering = ("project", "order")


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "story", "order", "created_at")
    list_filter = ("story__project", "story")
    search_fields = ("code", "title")
    ordering = ("story", "order")

# Register your models here.
