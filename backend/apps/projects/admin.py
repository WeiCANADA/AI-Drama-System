from django.contrib import admin

from apps.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "created_at", "updated_at")
    search_fields = ("code", "title")

# Register your models here.
