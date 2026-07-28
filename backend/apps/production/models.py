from django.db import models

from common.models import ProductionStatus, TimestampedUUIDModel


class Scene(TimestampedUUIDModel):
    episode = models.ForeignKey("stories.Episode", on_delete=models.CASCADE, related_name="scenes")
    code = models.CharField(max_length=32)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ("order", "created_at")
        constraints = [
            models.UniqueConstraint(fields=("episode", "code"), name="unique_scene_code_per_episode"),
            models.UniqueConstraint(fields=("episode", "order"), name="unique_scene_order_per_episode"),
        ]

    def __str__(self) -> str:
        return f"{self.code} - {self.title}"


class Shot(TimestampedUUIDModel):
    scene = models.ForeignKey("production.Scene", on_delete=models.CASCADE, related_name="shots")
    code = models.CharField(max_length=32)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=32,
        choices=ProductionStatus.choices,
        default=ProductionStatus.DRAFT,
    )

    class Meta:
        ordering = ("order", "created_at")
        constraints = [
            models.UniqueConstraint(fields=("scene", "code"), name="unique_shot_code_per_scene"),
            models.UniqueConstraint(fields=("scene", "order"), name="unique_shot_order_per_scene"),
        ]

    def __str__(self) -> str:
        return f"{self.code} - {self.title}"

# Create your models here.
