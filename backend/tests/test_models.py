from django.test import TestCase

from apps.production.models import Scene, Shot
from apps.projects.models import Project
from apps.stories.models import Episode, Story
from common.models import ProductionStatus


class HierarchyModelTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(code="PRJ-001", title="Pilot Production")
        self.story = Story.objects.create(
            project=self.project,
            code="STORY-001",
            order=1,
            title="Season One Arc",
        )
        self.episode = Episode.objects.create(
            story=self.story,
            code="EP-001",
            order=1,
            title="Episode One",
        )
        self.scene = Scene.objects.create(
            episode=self.episode,
            code="SC-001",
            order=1,
            title="Opening Scene",
        )

    def test_model_creation_and_relationships(self) -> None:
        shot = Shot.objects.create(
            scene=self.scene,
            code="SH-001",
            order=1,
            title="Establishing Shot",
            duration_seconds=8,
            status=ProductionStatus.DRAFT,
        )

        self.assertEqual(self.story.project, self.project)
        self.assertEqual(self.episode.story, self.story)
        self.assertEqual(self.scene.episode, self.episode)
        self.assertEqual(shot.scene, self.scene)
        self.assertEqual(shot.status, ProductionStatus.DRAFT)

    def test_ordering_respects_explicit_order_fields(self) -> None:
        Story.objects.create(
            project=self.project,
            code="STORY-002",
            order=2,
            title="Second Story",
        )
        Episode.objects.create(
            story=self.story,
            code="EP-002",
            order=2,
            title="Episode Two",
        )
        Scene.objects.create(
            episode=self.episode,
            code="SC-002",
            order=2,
            title="Second Scene",
        )
        Shot.objects.create(
            scene=self.scene,
            code="SH-002",
            order=2,
            title="Second Shot",
        )
        Shot.objects.create(
            scene=self.scene,
            code="SH-001",
            order=1,
            title="First Shot",
        )

        self.assertEqual(list(self.project.stories.values_list("code", flat=True)), ["STORY-001", "STORY-002"])
        self.assertEqual(list(self.story.episodes.values_list("code", flat=True)), ["EP-001", "EP-002"])
        self.assertEqual(list(self.episode.scenes.values_list("code", flat=True)), ["SC-001", "SC-002"])
        self.assertEqual(list(self.scene.shots.values_list("code", flat=True)), ["SH-001", "SH-002"])
