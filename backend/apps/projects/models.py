from django.db import models

from common.models import TimestampedUUIDModel


class Project(TimestampedUUIDModel):
    code = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("title", "created_at")

    def __str__(self) -> str:
        return f"{self.code} - {self.title}"

# Create your models here.
