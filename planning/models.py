import uuid

from django.core.exceptions import ValidationError
from django.db import models


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name="stories",
    )


class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    story = models.ForeignKey(
        Story,
        on_delete=models.PROTECT,
        related_name="episodes",
    )
    episode_order = models.PositiveIntegerField()
    episode_code = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["episode_order", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["story", "episode_order"],
                name="planning_episode_story_episode_order_uniq",
            )
        ]


class Scene(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    episode = models.ForeignKey(
        Episode,
        on_delete=models.PROTECT,
        related_name="scenes",
    )
    scene_order = models.PositiveIntegerField()
    scene_code = models.CharField(max_length=255, blank=True)
    scene_purpose = models.TextField(blank=True)
    dramatic_objective = models.TextField(blank=True)
    time_context_text = models.TextField(blank=True)
    location_context_text = models.TextField(blank=True)

    class Meta:
        ordering = ["scene_order", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["episode", "scene_order"],
                name="planning_scene_episode_scene_order_uniq",
            )
        ]


class Shot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scene = models.ForeignKey(
        Scene,
        on_delete=models.PROTECT,
        related_name="shots",
    )
    shot_order = models.PositiveIntegerField()
    shot_code = models.CharField(max_length=255, blank=True)
    narrative_purpose = models.TextField(blank=True)
    action_intent = models.TextField(blank=True)
    subject_focus = models.TextField(blank=True)

    class Meta:
        ordering = ["shot_order", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["scene", "shot_order"],
                name="planning_shot_scene_shot_order_uniq",
            )
        ]


class Storyboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scene = models.ForeignKey(
        Scene,
        on_delete=models.PROTECT,
        related_name="storyboards",
    )
    title = models.CharField(max_length=255, blank=True)


class StoryboardPanel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storyboard = models.ForeignKey(
        Storyboard,
        on_delete=models.PROTECT,
        related_name="panels",
    )
    panel_order = models.PositiveIntegerField()
    primary_shot = models.ForeignKey(
        Shot,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="storyboard_panels",
    )
    panel_notes = models.TextField(blank=True)

    class Meta:
        ordering = ["panel_order", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["storyboard", "panel_order"],
                name="planning_storyboardpanel_storyboard_panel_order_uniq",
            )
        ]

    def clean(self) -> None:
        super().clean()
        if self.primary_shot_id and self.storyboard_id:
            if self.primary_shot.scene_id != self.storyboard.scene_id:
                raise ValidationError(
                    {"primary_shot": "Primary shot must belong to the same scene as the storyboard."}
                )
