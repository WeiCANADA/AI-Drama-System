from django.db import models

from common.models import TimestampedUUIDModel


class Story(TimestampedUUIDModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="stories")
    code = models.CharField(max_length=32)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)

    class Meta:
        ordering = ("order", "created_at")
        constraints = [
            models.UniqueConstraint(fields=("project", "code"), name="unique_story_code_per_project"),
            models.UniqueConstraint(fields=("project", "order"), name="unique_story_order_per_project"),
        ]

    def __str__(self) -> str:
        return f"{self.code} - {self.title}"


class Episode(TimestampedUUIDModel):
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE, related_name="episodes")
    code = models.CharField(max_length=32)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)

    class Meta:
        ordering = ("order", "created_at")
        constraints = [
            models.UniqueConstraint(fields=("story", "code"), name="unique_episode_code_per_story"),
            models.UniqueConstraint(fields=("story", "order"), name="unique_episode_order_per_story"),
        ]

    def __str__(self) -> str:
        return f"{self.code} - {self.title}"

# Create your models here.
