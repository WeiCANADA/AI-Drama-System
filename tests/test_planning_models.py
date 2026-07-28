import uuid

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import ManyToManyField
from django.db.models.deletion import ProtectedError
from django.test import TestCase

from planning.models import Episode, Project, Scene, Shot, Story, Storyboard, StoryboardPanel


class PlanningModelTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create()
        self.story = Story.objects.create(project=self.project)
        self.episode = Episode.objects.create(story=self.story, episode_order=1)
        self.scene = Scene.objects.create(episode=self.episode, scene_order=1)
        self.shot = Shot.objects.create(scene=self.scene, shot_order=1)
        self.storyboard = Storyboard.objects.create(scene=self.scene)

    def test_uuid_primary_keys(self) -> None:
        instances = [
            self.project,
            self.story,
            self.episode,
            self.scene,
            self.shot,
            self.storyboard,
            StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1),
        ]
        for instance in instances:
            self.assertIsInstance(instance.pk, uuid.UUID)

    def test_real_hierarchy(self) -> None:
        self.assertEqual(self.story.project, self.project)
        self.assertEqual(self.episode.story, self.story)
        self.assertEqual(self.scene.episode, self.episode)
        self.assertEqual(self.shot.scene, self.scene)

    def test_episode_order_unique_within_story(self) -> None:
        with self.assertRaises(IntegrityError):
            Episode.objects.create(story=self.story, episode_order=1)

    def test_episode_order_can_repeat_across_stories(self) -> None:
        other_project = Project.objects.create()
        other_story = Story.objects.create(project=other_project)
        other_episode = Episode.objects.create(story=other_story, episode_order=1)
        self.assertEqual(other_episode.episode_order, 1)

    def test_scene_order_unique_within_episode(self) -> None:
        with self.assertRaises(IntegrityError):
            Scene.objects.create(episode=self.episode, scene_order=1)

    def test_scene_order_can_repeat_across_episodes(self) -> None:
        other_episode = Episode.objects.create(story=self.story, episode_order=2)
        other_scene = Scene.objects.create(episode=other_episode, scene_order=1)
        self.assertEqual(other_scene.scene_order, 1)

    def test_shot_order_unique_within_scene(self) -> None:
        with self.assertRaises(IntegrityError):
            Shot.objects.create(scene=self.scene, shot_order=1)

    def test_shot_order_can_repeat_across_scenes(self) -> None:
        other_scene = Scene.objects.create(episode=self.episode, scene_order=2)
        other_shot = Shot.objects.create(scene=other_scene, shot_order=1)
        self.assertEqual(other_shot.shot_order, 1)

    def test_panel_order_unique_within_storyboard(self) -> None:
        StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1)
        with self.assertRaises((ValidationError, IntegrityError)):
            StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1)

    def test_panel_order_can_repeat_across_storyboards(self) -> None:
        other_storyboard = Storyboard.objects.create(scene=self.scene)
        panel = StoryboardPanel.objects.create(storyboard=other_storyboard, panel_order=1)
        self.assertEqual(panel.panel_order, 1)

    def test_panel_can_exist_without_primary_shot(self) -> None:
        panel = StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1)
        self.assertIsNone(panel.primary_shot)

    def test_shot_can_have_zero_panels(self) -> None:
        other_shot = Shot.objects.create(scene=self.scene, shot_order=2)
        self.assertEqual(StoryboardPanel.objects.filter(primary_shot=other_shot).count(), 0)

    def test_shot_can_have_multiple_panels(self) -> None:
        StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1, primary_shot=self.shot)
        StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=2, primary_shot=self.shot)
        self.assertEqual(StoryboardPanel.objects.filter(primary_shot=self.shot).count(), 2)

    def test_no_multi_shot_relation_exists(self) -> None:
        field_names = {field.name for field in StoryboardPanel._meta.get_fields()}
        self.assertIn("primary_shot", field_names)
        self.assertNotIn("secondary_shots", field_names)
        many_to_many_fields = [field.name for field in StoryboardPanel._meta.get_fields() if isinstance(field, ManyToManyField)]
        self.assertEqual(many_to_many_fields, [])

    def test_cross_scene_panel_primary_shot_validation_fails(self) -> None:
        other_episode = Episode.objects.create(story=self.story, episode_order=2)
        other_scene = Scene.objects.create(episode=other_episode, scene_order=1)
        other_shot = Shot.objects.create(scene=other_scene, shot_order=1)
        panel = StoryboardPanel(storyboard=self.storyboard, panel_order=3, primary_shot=other_shot)
        with self.assertRaises(ValidationError):
            panel.full_clean()

    def test_cross_scene_panel_primary_shot_save_rejected(self) -> None:
        other_episode = Episode.objects.create(story=self.story, episode_order=2)
        other_scene = Scene.objects.create(episode=other_episode, scene_order=1)
        other_shot = Shot.objects.create(scene=other_scene, shot_order=1)
        panel = StoryboardPanel(storyboard=self.storyboard, panel_order=4, primary_shot=other_shot)
        with self.assertRaises(ValidationError):
            panel.save()

    def test_cross_scene_panel_primary_shot_create_rejected(self) -> None:
        other_episode = Episode.objects.create(story=self.story, episode_order=2)
        other_scene = Scene.objects.create(episode=other_episode, scene_order=1)
        other_shot = Shot.objects.create(scene=other_scene, shot_order=1)
        with self.assertRaises(ValidationError):
            StoryboardPanel.objects.create(
                storyboard=self.storyboard,
                panel_order=5,
                primary_shot=other_shot,
            )

    def test_same_scene_panel_primary_shot_validation_passes(self) -> None:
        panel = StoryboardPanel(storyboard=self.storyboard, panel_order=3, primary_shot=self.shot)
        panel.full_clean()

    def test_same_scene_panel_primary_shot_save_succeeds(self) -> None:
        panel = StoryboardPanel(storyboard=self.storyboard, panel_order=6, primary_shot=self.shot)
        panel.save()
        self.assertIsNotNone(panel.pk)

    def test_panel_without_primary_shot_save_succeeds(self) -> None:
        panel = StoryboardPanel(storyboard=self.storyboard, panel_order=7)
        panel.save()
        self.assertIsNone(panel.primary_shot)

    def test_project_protected_while_story_exists(self) -> None:
        with self.assertRaises(ProtectedError):
            self.project.delete()

    def test_story_protected_while_episode_exists(self) -> None:
        with self.assertRaises(ProtectedError):
            self.story.delete()

    def test_episode_protected_while_scene_exists(self) -> None:
        with self.assertRaises(ProtectedError):
            self.episode.delete()

    def test_scene_protected_while_shot_exists(self) -> None:
        with self.assertRaises(ProtectedError):
            self.scene.delete()

    def test_scene_protected_while_storyboard_exists(self) -> None:
        scene_without_shots = Scene.objects.create(episode=self.episode, scene_order=2)
        storyboard = Storyboard.objects.create(scene=scene_without_shots)
        with self.assertRaises(ProtectedError):
            scene_without_shots.delete()
        storyboard.delete()

    def test_storyboard_protected_while_panel_exists(self) -> None:
        StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1)
        with self.assertRaises(ProtectedError):
            self.storyboard.delete()

    def test_shot_protected_while_referenced_by_panel(self) -> None:
        StoryboardPanel.objects.create(storyboard=self.storyboard, panel_order=1, primary_shot=self.shot)
        with self.assertRaises(ProtectedError):
            self.shot.delete()

    def test_scene_optional_descriptive_fields(self) -> None:
        scene = Scene.objects.create(episode=self.episode, scene_order=2)
        self.assertEqual(scene.scene_code, "")
        self.assertEqual(scene.scene_purpose, "")
        self.assertEqual(scene.dramatic_objective, "")
        self.assertEqual(scene.time_context_text, "")
        self.assertEqual(scene.location_context_text, "")

    def test_shot_optional_descriptive_fields(self) -> None:
        shot = Shot.objects.create(scene=self.scene, shot_order=2)
        self.assertEqual(shot.shot_code, "")
        self.assertEqual(shot.narrative_purpose, "")
        self.assertEqual(shot.action_intent, "")
        self.assertEqual(shot.subject_focus, "")
