from django.contrib import admin

from apps.production.models import Scene, Shot


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "episode", "order", "created_at")
    list_filter = ("episode__story", "episode")
    search_fields = ("code", "title")
    ordering = ("episode", "order")


@admin.register(Shot)
class ShotAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "scene", "order", "status", "duration_seconds", "created_at")
    list_filter = ("status", "scene__episode", "scene")
    search_fields = ("code", "title")
    ordering = ("scene", "order")

# Register your models here.
